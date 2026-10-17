# Fallstricke und Lösungen

Alle Punkte sind in der osmera-Sitzung (Oktober 2026) aufgetreten.

## Vorschau und Messung
- **Datei-Vorschau ohne Styles:** Seiten mit Tailwind-CDN brauchen JavaScript und Netz. Immer über einen lokalen HTTP-Server öffnen, nie `file://`.
- **Schmaler Browser-Bereich (≈ 343 px):** Alle Desktop-Layouts zeigen dort ihre Handy-Ansicht. Auftraggeber sehen dann „D2 funktioniert gar nicht“, obwohl das Desktop-Layout nie aktiv war. Gegenmittel: Breiten-Anzeige in der Leiste, Ansicht-Umschalter mit festem Rahmen, Hinweis im Bericht.
- **Bilder verzögert (`loading=lazy`):** vor Ganzseiten-Aufnahmen durch die Seite scrollen.
- **Ganzseiten-Aufnahme zeigt halb überblendete Karten:** Autoplay und Überblendungen laufen weiter. Vorher anhalten (eine Interaktion auslösen) oder im Fenster prüfen.
- **Smooth-Scroll der Seite verschluckt `scrollTo`:** vor dem Messen `document.documentElement.style.scrollBehavior='auto'` setzen.
- **Zusammenfassungen von Bildern:** Ein Foto pro Zustand, beschriftet. Sonst sieht der Auftraggeber „irgendeinen“ Zustand.

## Layout
- **Grid-Spalten mit `1fr` laufen über,** wenn Inhalte nicht schrumpfen. Immer `minmax(0,1fr)`.
- **Sticky links funktioniert nicht,** wenn das Grid `align-items: start` hat: die Spalte hat dann keine Höhe zum Mitlaufen. `align-items: stretch` und die Spalte innen `position: sticky`.
- **Feste Spaltenzahl in Inline-Styles** (`repeat(6,1fr)`) bricht auf Handys. Entweder `auto-fit` mit `minmax(min(100%,…),1fr)` oder per Medienabfrage überschreiben (`!important` nur im Guide, nicht in Produktions-CSS).
- **Tablet ist ein eigenes Layout,** kein gestrecktes Handy und kein gestauchter Desktop.
- **Scroll-Fänger (400vh)** wird nicht verstanden, wenn der Fortschritt nicht sichtbar ist. Besser normales Scrollen mit klebendem Titel oder Karten, die einzeln vorbeilaufen.
- **Unterschiedlich hohe Karten (Aufklappen):** `align-self: start`, damit nicht beide mitwachsen. Auf Tablet gleiche Höhe der geschlossenen Karten über eine Mindesthöhe.
- **Logo-Ausrichtung:** Ringmitte = Mitte der x-Höhe der Wortmarke, nicht Grundlinie. Per Pixelmessung bei dpr 4 prüfen (Tinte oben/unten je Element).

## Druck und PDF
- **Responsive Regeln nur für `screen`:** Chrome wertet Breiten-Medienabfragen im PDF mit einer anderen Breite aus (Standard-Papier). `@media screen and (max-width:…)`, und im Drucker-Skript Fenstergröße und Papiergröße fest setzen.
- **`background-clip: text` (Verlaufstext) wird im PDF mit Rahmen gezeichnet.** Im Druck auf Vollton umstellen.
- **Seiten mit fester Höhe:** Überlauf in Druck-Emulation messen (scrollHeight minus clientHeight je Seite) und kürzen, statt zu verkleinern.
- **Bilder fehlen im PDF, ohne dass etwas meldet:** Chrome druckt nicht ladbare Bilder als Alt-Text mit Platzhalter-Symbol, Überlauf- und Seitenzahl-Prüfung bleiben grün. Ursache war ein Testserver mit falscher Wurzel (relative Pfade wie `../img/` lösten ins Leere auf). Server-Wurzel so wählen, dass alle relativen Pfade stimmen, vor dem Druck kaputte Bilder per Skript zählen (`document.images`, `naturalWidth`), danach jede PDF-Seite als Bild ansehen. Überlauf-Prüfung allein genügt nicht.
- **Variable Schriften in PDFs** erscheinen mit leeren Namen in der Schriftenliste, das ist normal. Mit Bild und Textauszug prüfen.
- **SVG ohne Breite/Höhe** in `display:grid; place-items:center` mit `width:auto; max-width:100%` kann auf 0 kollabieren. Feste Maße setzen.

## Marke
- **Schriftregel:** Überschriften in der Textschrift, Markenwörter in der Markenschrift. Beim Guide dieselbe Regel automatisch anwenden (alle freistehenden Markenwörter in einen Span, außer in Code, Titel, SVG).
- **Kontrast des Markenblaus** auf Weiß prüfen (hier 4,10:1). Kleine Schrift und Schalter brauchen die dunklere Stufe.
- **Wärmefarben nur als Hintergrund-Schimmer,** nie für Text oder Schalter.
- **Zwei Design-Systeme mit gleichem Präfix** (hier `--osm-`) nie in einem Dokument mischen. Eines verbindlich erklären, das andere ins Archiv. Neue Arbeit nie aus dem abgelösten ableiten, auch nicht „nur die Farben“.
- **KI-erzeugte Markenboards** (Bildgenerator) sind Anregung, keine Marke: erfundene Namen, Schriften und Farben stehen darin als Platzhalter.

## Arbeitsweise
- **Ordner umbauen, ohne etwas zu zerbrechen:** vorher Abhängigkeiten suchen (absolute Pfade in Bau-Skripten, Verweise in Anleitungen und Bildlisten, relative `../`-Verweise zwischen Geschwisterordnern). Nur verschieben, Vorher/Nachher vergleichen, Protokoll und Rückgängig-Skript ablegen. Ordner, von denen Skripte abhängen, bleiben am Platz. Umlaute in Namen vor dem Vergleichen normalisieren (macOS liefert sie zerlegt). Ordner mit Vermerken wie „NDA“ oder „intern“ nicht öffnen, nur als Ganzes verschieben.
- **Eigener Deploy-Workflow kann scheitern, obwohl die Seite live geht:** mit `gh run list` prüfen, welcher Lauf was tut. Hier scheiterte der eigene Workflow „Deploy to GitHub Pages“ im ersten Schritt (Git-Identität fehlt), die Seite ging über GitHubs eingebautes „pages build and deployment“ aus `main` trotzdem live. Melden, nicht stillschweigend ändern.
- **Mehrere Orte für dasselbe Paket** (Git-Branch, Cloud-Ordner, Skill-Ordner) laufen auseinander. Eine Quelle festlegen (hier der Git-Branch), die anderen sind Kopien und werden nach jeder Änderung abgeglichen (`diff -rq`).
- **Rückmeldung mitten in der Arbeit:** Neue Wünsche (z.B. „Logo ist jetzt zu hoch“) sofort einarbeiten und den Messwert nennen, der jetzt stimmt. Ein Zwischenstand, der nicht passt, wird nicht verteidigt.
- **Freigabe bleibt Freigabe:** „Gefällt mir sehr gut, du kannst pushen“ erlaubt genau das Genannte (diese Seite). Weitere Ablagen (z.B. interne Guides) nicht auf den Live-Branch legen.
