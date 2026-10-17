---
name: design-konfigurator-prozess
description: Prozess, um ein Design gemeinsam mit dem Auftraggeber zu entwickeln und zu entscheiden. Optionen mit klaren Nummern und Namen (D1, P2, L7), ein Konfigurator auf der Seite zum Umschalten, Vorschau auf localhost im Browser-Bereich der App, Messung mit Headless-Chrome, Einbau in eine Kopie der echten Seite, Diff, Freigabe, Übernahme. Verwenden bei "Design-Varianten ausprobieren", "mehrere Optionen zeigen", "Konfigurator", "Prototyp im Browser", "Layout und Hintergrund durchprobieren", "Runde 2", "zeig mir alles im Gesamtblick", "localhost-Server starten". Use for iterative design decisions with versioned options, an on-page configurator and a verified hand-over to the real site.
---

# Design im Konfigurator-Prozess

Dieser Ablauf hat sich in der osmera-Sitzung (Oktober 2026) bewährt: Der Auftraggeber sieht echte, bedienbare Varianten, nennt Nummern statt Beschreibungen, und am Ende steht eine geprüfte Übernahme in die echte Seite. Er ist für jedes Web-Design mit Entscheidungsbedarf wiederholbar.

Ergänzend gilt der Skill `web-ui-design` (Gestaltungsgrundsätze, Bilder, Qualitätsprüfung). Projektregeln (Memory, CLAUDE.md) gehen immer vor.

## Die Schleife (eine "Runde")

1. **Auftrag fassen.** Anhänge und Screenshots des Auftraggebers wirklich ansehen und aufschreiben, was daraus übernommen wird („Aufbau und Funktionsweise der Karten“, nicht „gefällt mir“). Inhalte nur aus der echten Seite nehmen. Neue Texte, Zahlen, Zitate werden nicht erfunden; Abgeleitetes ist als Vorschlag markiert.
2. **Optionen benennen.** Jede Variante und jede Stufe bekommt eine feste Kennung, die in der Oberfläche, im Bericht und im Memory gleich lautet. Schema in `references/benennung.md`.
3. **Konfigurator bauen.** Eine Seite mit Leiste oben: Ansicht (Fenster, Desktop, Tablet, Handy), Layout-Variante, Hintergrund, Seite, Detailregler. Jede Dimension ist ein eigener Schalter, damit Kombinationen entstehen (D2 + P2 + L7 + Blau rechts). Zustand steht in der Adresse (`?var=b&pal=l7&flip=1`) und wird im Browser gemerkt. Startpunkt: `assets/konfigurator-vorlage.html` (getestet).
4. **Lokal zeigen.** Server über die App starten, nicht per Hand: `.claude/launch.json` mit `python3 -m http.server PORT --directory ORDNER` und `preview_start` öffnet die Seite im Browser-Bereich. Dem Auftraggeber zusätzlich die Adresse `http://localhost:PORT/...` nennen. Der Browser-Bereich ist oft schmal (um 343 px): Deshalb zeigt die Leiste Breite und Layout-Modus an, und der Ansicht-Umschalter rendert Desktop, Tablet und Handy in einem Rahmen mit fester Breite.
5. **Messen, nicht schätzen.** Mit `scripts/cdp.mjs` Matrix der Breiten (375 bis 1920), seitlicher Überlauf, JavaScript-Fehler, Hover, Tippen, Mausrad, Druck-Überlauf, Abstände. Bilder immer mit Beschriftung zu Kontaktbögen zusammenfassen. Was nicht geprüft wurde, wird benannt. Details und Messskripte: `references/pruefen.md`.
6. **Bericht in fester Form.** Was ist neu (Kennungen), wie bedient man es (Link, Schalter), was wurde gemessen, was bleibt offen, Empfehlung mit Begründung, die eine Entscheidungsfrage am Schluss. Bilder (Kontaktbogen, Gesamtbild) mitschicken.
7. **Feedback einarbeiten.** Der Auftraggeber antwortet mit Kennungen und Wünschen. Varianten werden ergänzt (neue Stufen, neue Schalter), nicht ersetzt, und der Favorit wird zur Voreinstellung. Jede Runde im Memory festhalten (`references/memory-vorlage.md`).
8. **Einbau und Gesamtblick.** Entscheidung steht, dann in eine Kopie der echten Seite einbauen (Staging), Diff erzeugen, die ganze Seite im Zusammenhang zeigen (Vollseite, Ausschnitte der Übergänge, Tablet, Handy). Muster in `references/einbau.md`.
9. **Freigabe, Übernahme, Kontrolle.** Erst nach ausdrücklichem OK: Backup, kopieren, Commit, Push nur wenn erlaubt. Danach live prüfen (Status, Inhalt, Breiten). Memory aktualisieren.

## Regeln, die den Prozess tragen

- **Nichts im geschützten Ordner, bevor es gezeigt und freigegeben ist.** Gebaut wird im Scratchpad/Staging. Vorher Diff zeigen, Backup anlegen.
- **Einmal sagen, was Bestand und was Vorschlag ist.** Neue Werte, die die Seite nicht belegt, sind gekennzeichnet.
- **Optionen vergleichbar machen:** gleiche Inhalte, gleiche Breite, gleicher Zustand. Vorteile und Nachteile je Variante, eine Empfehlung.
- **Kleine Schritte:** jede Rückmeldung sofort sichtbar umsetzen und erneut zeigen, statt Sammelrunden.
- **Mobil ist gleichwertig:** Desktop, Tablet (zwischen Desktop und Handy) und Handy werden getrennt gestaltet und getrennt abgenommen.
- **Zugänglichkeit mitliefern:** Kontraste rechnen, Fokus und Tastatur, `prefers-reduced-motion`.
- **Ehrlich berichten:** Messwerte nennen, Artefakte der Messung erklären, offene Punkte nicht verstecken.
- **Git und Deployment bewusst:** vor jedem Push klären, welche Branches ausgeliefert werden (siehe `references/einbau.md`). Nur die Dateien committen, die gemeint sind.

## Dateien dieses Skills

| Datei | Zweck |
|---|---|
| `assets/konfigurator-vorlage.html` | Funktionierende Vorlage der Optionen-Seite (Leiste, Ansicht-Umschalter, URL-Zustand, Rahmen-Sync) |
| `scripts/cdp.mjs` | Headless-Chrome-Prüfwerkzeug: Klicks, Tippen, Mausrad, Hover, Messen, Bilder, Druck-Medium |
| `scripts/pdf.mjs` | Seite als PDF drucken (A4 quer, Hintergründe, feste Fenstergröße) |
| `references/benennung.md` | Kennungsschema und Antwortformat |
| `references/pruefen.md` | Prüfmatrix, Messskripte, Kontaktbögen |
| `references/einbau.md` | Einbau in die echte Seite, Diff, Gesamtblick, Git und Deployment |
| `references/fallstricke.md` | Gesammelte Fehler und Lösungen |
| `references/memory-vorlage.md` | Wie der Stand zwischen Sitzungen festgehalten wird |
