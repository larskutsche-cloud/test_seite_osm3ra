// Headless-Chrome-Prüfwerkzeug (DevTools-Protokoll, kein npm nötig; Node 22+ und Google Chrome).
//
//   node cdp.mjs jobs.json        (Chrome-Pfad abweichend: CHROME_PATH=/pfad/chrome)
//
// jobs.json = Liste von Aufträgen. Jeder Auftrag:
//   url, w, h              Fenstergröße in CSS-Pixeln (Pflicht)
//   dpr                    Pixeldichte (1, 2, 4 für scharfe Ausschnitte)
//   mobile, touch          true = Handy-Emulation / Touch-Ereignisse
//   mediaType: "print"     Druck-Medium (für Überlauf-Prüfung von A4-Seiten)
//   media: [{name:"hover",value:"none"},{name:"pointer",value:"coarse"}]   Medien-Merkmale (Touch-Geräte ohne Hover)
//   steps: [ ... ]         Schritte nacheinander. Je Schritt (alle optional) und "wait" in ms danach (Standard 900):
//       eval: "JS"         wird ausgeführt, Rückgabe landet im Ergebnis (mit JSON.stringify Objekte liefern)
//       mouse: [x,y]       Maus bewegen (Hover)
//       click: [x,y]       Klick
//       tap:   [x,y]       Touch-Tippen
//       wheel: [x,y,dy]    Mausrad drehen (dy z.B. 300)
//   shot: "pfad.png"       Bildschirmfoto am Ende; full:true = ganze Seite (bis 16000 px hoch)
//   clips: "CSS-Selektor", clipPrefix: "pfad/prefix_"   je Treffer ein Bild (z.B. jede Druckseite ".pg"), clipScale
// Ausgabe je Auftrag eine JSON-Zeile {shot, out:[...]}. JavaScript-Fehler der Seite erscheinen als "ERRORS: ...".
import { spawn } from 'node:child_process';
import { readFileSync, writeFileSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const jobs = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const PORT = 9333 + Math.floor(Math.random() * 300);
const dir = mkdtempSync(join(tmpdir(), 'cdp-'));
const chrome = spawn(process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ['--headless=new', '--disable-gpu', '--hide-scrollbars', `--remote-debugging-port=${PORT}`, `--user-data-dir=${dir}`, 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
async function up() { for (let i = 0; i < 60; i++) { try { if ((await fetch(`http://127.0.0.1:${PORT}/json/version`)).ok) return; } catch {} await sleep(250); } throw new Error('Chrome startet nicht'); }

async function run(job) {
  const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json();
  const ws = new WebSocket(t.webSocketDebuggerUrl);
  await new Promise((r) => (ws.onopen = r));
  let id = 0; const pend = new Map(); const waiters = []; const errs = [];
  ws.onmessage = (m) => {
    const d = JSON.parse(m.data);
    if (d.method === 'Runtime.exceptionThrown') errs.push((d.params.exceptionDetails.exception?.description || d.params.exceptionDetails.text || '').slice(0, 220));
    if (d.method === 'Runtime.consoleAPICalled' && d.params.type === 'error') errs.push('console.error: ' + (d.params.args[0]?.value || '').toString().slice(0, 160));
    if (d.id && pend.has(d.id)) { pend.get(d.id)(d); pend.delete(d.id); } else if (d.method) waiters.forEach((w) => w(d));
  };
  const send = (method, params = {}) => new Promise((res) => { const i = ++id; pend.set(i, res); ws.send(JSON.stringify({ id: i, method, params })); });
  await send('Page.enable'); await send('Runtime.enable');
  if (job.media || job.mediaType) await send('Emulation.setEmulatedMedia', { media: job.mediaType || '', features: job.media || [] });
  if (job.touch) await send('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 1 });
  await send('Emulation.setDeviceMetricsOverride', { width: job.w, height: job.h, deviceScaleFactor: job.dpr || 1, mobile: !!job.mobile });
  const loaded = new Promise((r) => waiters.push((d) => d.method === 'Page.loadEventFired' && r()));
  await send('Page.navigate', { url: job.url });
  await loaded; await sleep(2800);               // Schriften und Skripte (Tailwind per CDN) brauchen einen Moment
  const out = [];
  for (const st of job.steps || []) {
    if (st.mouse) await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: st.mouse[0], y: st.mouse[1] });
    if (st.click) { const [x, y] = st.click; await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x, y }); await send('Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 }); await send('Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 }); }
    if (st.tap) { await send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: st.tap[0], y: st.tap[1] }] }); await sleep(60); await send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] }); }
    if (st.wheel) { await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: st.wheel[0], y: st.wheel[1] }); await send('Input.dispatchMouseEvent', { type: 'mouseWheel', x: st.wheel[0], y: st.wheel[1], deltaX: 0, deltaY: st.wheel[2] }); }
    if (st.eval) { const r = await send('Runtime.evaluate', { expression: st.eval, awaitPromise: true, returnByValue: true }); out.push(r.result?.result?.value ?? r.result?.exceptionDetails?.text); }
    await sleep(st.wait ?? 900);
  }
  if (job.clips) {
    const rects = JSON.parse((await send('Runtime.evaluate', { expression: `JSON.stringify([...document.querySelectorAll(${JSON.stringify(job.clips)})].map(e=>{const r=e.getBoundingClientRect();return [r.left+scrollX,r.top+scrollY,r.width,r.height]}))`, returnByValue: true })).result.result.value);
    let i = 0; for (const [x, y, w, h] of rects) { i++; const r = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x, y, width: w, height: h, scale: job.clipScale || 1 } }); writeFileSync(`${job.clipPrefix}${String(i).padStart(2, '0')}.png`, Buffer.from(r.result.data, 'base64')); }
    out.push('clips ' + rects.length);
  }
  if (job.shot && job.full) {
    const lm = await send('Page.getLayoutMetrics'); const H = Math.ceil(lm.result.cssContentSize.height);
    const r = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: job.w, height: Math.min(H, 16000), scale: 1 } });
    writeFileSync(job.shot, Buffer.from(r.result.data, 'base64')); out.push('fullH ' + H);
  } else if (job.shot) { const r = await send('Page.captureScreenshot', { format: 'png' }); writeFileSync(job.shot, Buffer.from(r.result.data, 'base64')); }
  if (errs.length) out.push('ERRORS: ' + JSON.stringify(errs));
  ws.close(); await fetch(`http://127.0.0.1:${PORT}/json/close/${t.id}`);
  return out;
}
try { await up(); for (const j of jobs) { const o = await run(j); console.log(JSON.stringify({ shot: j.shot, out: o })); } }
finally { chrome.kill(); }
