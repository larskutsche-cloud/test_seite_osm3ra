// Seite als PDF drucken (Chrome DevTools). Nutzung: node pdf.mjs <url> <ausgabe.pdf> [breite=1123] [höhe=794]
// Wichtig: Die Fenstergröße wird fest gesetzt, damit Breiten-Medienabfragen im Druck stimmen; Responsive-Regeln im CSS
// deshalb auf @media screen beschränken. Papier A4 quer; CSS "@page { size: A4 landscape; margin: 0 }" hat Vorrang.
import { spawn } from 'node:child_process';
import { writeFileSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
const [url, out] = process.argv.slice(2);
const VW = Number(process.argv[4] || 1123), VH = Number(process.argv[5] || 794);
const PORT = 9700 + Math.floor(Math.random() * 200);
const dir = mkdtempSync(join(tmpdir(), 'pdf-'));
const chrome = spawn(process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', ['--headless=new', '--disable-gpu', `--remote-debugging-port=${PORT}`, `--user-data-dir=${dir}`, 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
try {
  for (let i = 0; i < 60; i++) { try { if ((await fetch(`http://127.0.0.1:${PORT}/json/version`)).ok) break; } catch {} await sleep(250); }
  const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json();
  const ws = new WebSocket(t.webSocketDebuggerUrl); await new Promise((r) => (ws.onopen = r));
  let id = 0; const pend = new Map(); const waiters = [];
  ws.onmessage = (m) => { const d = JSON.parse(m.data); if (d.id && pend.has(d.id)) { pend.get(d.id)(d); pend.delete(d.id); } else if (d.method) waiters.forEach((w) => w(d)); };
  const send = (method, params = {}) => new Promise((res) => { const i = ++id; pend.set(i, res); ws.send(JSON.stringify({ id: i, method, params })); });
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', { width: VW, height: VH, deviceScaleFactor: 1, mobile: false });
  const loaded = new Promise((r) => waiters.push((d) => d.method === 'Page.loadEventFired' && r()));
  await send('Page.navigate', { url }); await loaded; await sleep(3000);
  await send('Runtime.evaluate', { expression: 'document.fonts.ready.then(()=>1)', awaitPromise: true });
  await sleep(1200);
  const r = await send('Page.printToPDF', { preferCSSPageSize: true, paperWidth: 11.693, paperHeight: 8.268, marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0, printBackground: true, displayHeaderFooter: false, transferMode: 'ReturnAsBase64' });
  writeFileSync(out, Buffer.from(r.result.data, 'base64')); console.log('PDF', out);
  ws.close();
} finally { chrome.kill(); }
