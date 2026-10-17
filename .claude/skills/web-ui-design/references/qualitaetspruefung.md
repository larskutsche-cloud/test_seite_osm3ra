# Qualitätsprüfung

## Vorschau starten

```bash
cd ORDNER && python3 -m http.server 8765 --bind 127.0.0.1    # im Hintergrund laufen lassen
```

Danach im Browser-Bereich `http://127.0.0.1:8765/seite.html` öffnen. `file://` zeigt bei Tailwind-Play-CDN-Seiten nur rohen Text, weil der Schnappschuss ohne JavaScript rendert. Server nach der Arbeit beenden (`pkill -f "http.server 8765"`).

## Breiten

375, 414, 640, 768, 1023, 1024, 1062, 1279, 1280, 1440, 1920. Haltepunkte von Tailwind (640, 768, 1024, 1280, 1536) immer einmal knapp darunter und darauf testen. Die Breite des eingebauten Browser-Bereichs ist oft nur etwa 1060 px. Dort muss das Design auch gut aussehen.

## Messen statt schätzen

Per JavaScript im Browser:

- `document.documentElement.scrollWidth === innerWidth` (kein seitliches Scrollen)
- Elemente, deren `getBoundingClientRect().right > innerWidth`
- Überlagerungen mit `references/overlay-check.js`
- Konsolenfehler lesen (`read_console_messages` nur Fehler)
- Interne Links per `fetch` anfragen (kein 404)

## Checkliste

- [ ] Kein horizontales Scrollen bei allen Breiten
- [ ] Gesicht und Kernobjekt von keiner Kachel, keinem Verlauf und keinem Text überdeckt
- [ ] Paare (Problem und Lösung) immer zusammen sichtbar
- [ ] Mobil: Bild und Text gestapelt, Buttons mindestens 44 px hoch
- [ ] Kontrast Text/Fläche mindestens 4,5:1 (große Schrift 3:1)
- [ ] Tastaturfokus sichtbar, Alt-Texte vorhanden, Überschriftenfolge logisch
- [ ] `prefers-reduced-motion` respektiert
- [ ] Hell und dunkel geprüft, wenn die Seite beides kann
- [ ] Bilder: AVIF/WebP, Größe passend, kein Original im Repo
- [ ] Drittanbieter-Ressourcen in der Datenschutzerklärung genannt oder selbst gehostet
- [ ] Keine Konsolenfehler, keine toten Links

## Ergebnis berichten

- Was gemessen wurde (Breiten, Prüfungen) und mit welchem Ergebnis.
- Was nur angesehen wurde (Screenshot) und was nicht geprüft wurde.
- Offene Punkte mit Vorschlag.
