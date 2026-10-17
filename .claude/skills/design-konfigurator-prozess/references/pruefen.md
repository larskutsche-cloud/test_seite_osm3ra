# Prüfen und berichten

Grundsatz: gemessen wird im echten Browser (Headless-Chrome), nicht im Kopf. `scripts/cdp.mjs` bedient die Seite wie ein Mensch und liefert Zahlen und Bilder.

## Aufträge (jobs.json) in Kürze

```json
[{"url":"http://127.0.0.1:8780/seite.html?var=b","w":1361,"h":734,"dpr":1,
  "steps":[{"eval":"window.scrollTo(0,800);1","wait":1200},
           {"mouse":[500,300],"wait":900},
           {"click":[500,300]},
           {"wheel":[950,400,300]},
           {"eval":"JSON.stringify({sw:document.documentElement.scrollWidth,iw:innerWidth})"}],
  "shot":"bild.png"}]
```
Aufruf: `node scripts/cdp.mjs jobs.json`. Handy: `"mobile":true,"touch":true` und Schritte `tap`. Touch-Gerät ohne Hover: `"media":[{"name":"hover","value":"none"},{"name":"pointer","value":"coarse"}]`. Druck: `"mediaType":"print"`.

Die Ausgabe enthält die Rückgaben der `eval`-Schritte und `ERRORS: [...]`, wenn die Seite JavaScript-Fehler meldet.

## Prüfmatrix

| Was | Wie | Erfolg |
|---|---|---|
| Seitlicher Überlauf | `scrollWidth === innerWidth` bei 375, 390, 430, 640, 768, 820, 1024, 1280, 1366, 1440, 1920 | gleich |
| Wer läuft über | Elemente mit `getBoundingClientRect().right > innerWidth + 2` auflisten (Tabellen und Karussell-Spuren ausnehmen) | leere Liste |
| Umschaltpunkte | je eine Breite direkt unter und über jedem Breakpoint (639/640, 1023/1024) | Layout wie erwartet |
| JavaScript-Fehler | `ERRORS` in der Ausgabe | keine |
| Hover, Klick, Tippen | `mouse`, `click`, `tap` und Zustand per `eval` lesen | Klassen und `aria-expanded` stimmen |
| Mausrad / Scroll-Effekte | `wheel` oder `window.scrollTo` an Anteile der Strecke (0, .25, .5, .75, 1), Zustand lesen | aktive Karte wechselt wie geplant |
| Abstände | Differenzen von `getBoundingClientRect()` zwischen Elementen | gleichmäßig (Toleranz 4 px) |
| Menü-Sprünge | `el.scrollIntoView()` und Abstand Überschrift zu Menü-Unterkante messen | alle Abschnitte gleich |
| Seitenende | `scrollTo(0, scrollHeight)`, dann Position der letzten Elemente | nichts angeschnitten |
| Druck (A4) | Medium `print`, Fenster 1123 × 794, je Seite `scrollHeight - clientHeight` | ≤ 1 px |
| Schrift und Verlauf | `getComputedStyle(...).fontFamily`, `backgroundImage`, `webkitTextFillColor` | wie die Markenregel |
| Kontrast | WCAG-Verhältnis rechnen (Formel in `brand`-Tokens oder selbst) | ≥ 4,5 (Text), ≥ 3 (groß) |

Beispiel Überlauf-Liste:
```js
JSON.stringify([...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width&&r.right>innerWidth+2&&!e.closest('table,.track,iframe')}).slice(0,8).map(e=>e.tagName+'.'+String(e.className).slice(0,24)+' '+Math.round(e.getBoundingClientRect().right)))
```

Beispiel Druck-Überlauf (Seiten, die über ihre feste Höhe hinausragen):
```js
JSON.stringify([...document.querySelectorAll('.pg')].map((e,i)=>({p:i+1,over:e.scrollHeight-e.clientHeight})).filter(x=>x.over>1))
```

## Bilder

- Immer erst messen, dann Bild: Zahlen schlagen den Eindruck. Das Bild zeigt, was die Zahlen nicht zeigen (Gewicht, Rhythmus, Farbe).
- **Kontaktbogen** beschriften (Kennung, Stufe, Seite), damit der Auftraggeber „L1 links unten“ sagen kann. Mit Pillow zusammenfügen, Raster 2 Spalten, Maßstab 0,5 bis 0,6. Kopf mit Text per `ImageDraw`.
- Schärfe: `dpr` 2 oder 4 und Ausschnitt zuschneiden, wenn es um Details geht (Logo, Ausrichtung auf Pixel genau).
- Ganzseiten-Aufnahme: `"full":true` (bis 16000 px Höhe). Vorher einmal durch die Seite scrollen, damit verzögert geladene Bilder da sind. Zustände mit Übergängen (Autoplay, Überblendung) vorher anhalten, sonst erscheinen halb überblendete Karten. Das ist ein Messartefakt, im echten Fenster ist alles sauber. Im Zweifel mit Fenster-Aufnahmen gegenprüfen.
- Handy-Ansicht von Karten und Menü zusätzlich mit echter Breite (390) aufnehmen, nicht nur verkleinert.

## Bericht

Kurz, in dieser Reihenfolge: Neues (Kennungen) · Bedienung (Link, Schalter) · Gemessen (Zahlen, Breiten) · Einschränkungen (was nicht geprüft ist) · Empfehlung · eine Frage. Keine Aufzählung von Tools. Bilder tragen die Erklärung in der Beschriftung.
