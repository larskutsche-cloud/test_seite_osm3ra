// Prüft, ob Overlay-Kacheln das Gesicht oder das Kernobjekt eines Fotos berühren.
// Im Browser (javascript_tool) ausführen, dann bei jeder Breite chk() aufrufen.
//
// Anpassen:
//  - FIG:    Selektor des Foto-Rahmens (Element, in dem das Bild mit object-cover liegt)
//  - CARDS:  Selektor der Overlay-Kacheln
//  - FACES: Liste von Gesichtszonen (mehrere Personen möglich), OBJ: Kernobjekt (Tablet, Hände)
//    Zonen als Anteile des QUADRATISCHEN Quellbilds (x0, y0, x1, y1, jeweils 0 bis 1)
//
// Die Zonen werden aus dem Quellbild abgelesen (Vorschau ansehen) und großzügig gewählt.
// Beispiel für ein Porträt, bei dem das Gesicht oben mittig und das Tablet unten rechts liegt:
//   FACES = [[0.36, 0.08, 0.64, 0.42]];  OBJ = [0.42, 0.68, 0.88, 0.89]
// Beispiel Zwei-Personen-Foto: FACES = [[.22,.09,.46,.40],[.55,.19,.83,.48]]; OBJ = [.40,.58,.79,.80]
window.chk = () => {
  const FIG = 'figure', CARDS = '.glass-card-strong';
  const FACES = [[0.36, 0.08, 0.64, 0.42]], OBJ = [0.42, 0.68, 0.88, 0.89];

  const fig = document.querySelector(FIG);
  const fr = fig.getBoundingClientRect();
  const W = fr.width, H = fr.height, S = Math.max(W, H);          // object-cover skaliert auf die längere Seite
  const pos = getComputedStyle(fig.querySelector('img')).objectPosition.split(' ');
  const px = parseFloat(pos[0]) / 100, py = parseFloat(pos[1]) / 100;
  const ox = fr.left + (W - S) * px, oy = fr.top + (H - S) * py;   // Versatz des Bildes im Rahmen

  const zone = (z) => ({ l: ox + z[0] * S, t: oy + z[1] * S, r: ox + z[2] * S, b: oy + z[3] * S });
  const area = (a, b) =>
    Math.max(0, Math.min(a.r, b.r) - Math.max(a.l, b.l)) *
    Math.max(0, Math.min(a.b, b.b) - Math.max(a.t, b.t));

  const faces = FACES.map(zone), obj = zone(OBJ);
  const cards = [...document.querySelectorAll(CARDS)]
    .filter((c) => getComputedStyle(c).display !== 'none')
    .map((c) => c.getBoundingClientRect())
    .map((r) => ({ l: r.left, t: r.top, r: r.right, b: r.bottom }));

  return innerWidth + 'px | Foto ' + Math.round(W) + 'x' + Math.round(H) +
    ' | scrollW ' + document.documentElement.scrollWidth +
    ' | Karten ' + cards.length +
    faces.map((f, i) => ' | Gesicht' + (i + 1) + ' ' + cards.map((c) => Math.round(area(c, f))).join(',')).join('') +
    ' | Objekt ' + cards.map((c) => Math.round(area(c, obj))).join(',');
};
'ok';
