# osmera (nur für dieses Projekt)

Stand: 17.10.2026 (Brand Guide verbindlich). Dieses Dokument gehört zum Projekt osmera und wird nur bei osmera-Aufgaben gelesen.

## Projekt

- Statische Seite für ein Dienstplan-Add-on für Kliniken. Live unter https://osmera.de (GitHub Pages).
- Repo: `/Volumes/Scico/osmera_website_gh/test_seite_osm3ra/`. Der Hauptordner ist live. `development/` (Branch `101026_NewVersion`) und `staging-101028/` sind eigene Worktrees.
- Arbeiten nur in `development/`, außer der User erlaubt etwas anderes. Hauptordner und Staging sind tabu.
- Vor jedem Schreiben nach `development/` die Änderungen zeigen und auf OK warten. Backup des Vorzustands im Scratchpad ablegen.
- Der Edit-Hook blockiert in einer Worktree-Session Schreibzugriffe nach `development/`. Vorgehen: im Scratchpad vorbereiten, dem User den Diff zeigen, nach seinem OK per Shell kopieren (`cp`). Nichts committen, wenn der User es nicht verlangt.

## Marke und Design

- **Verbindlich ist der Brand Guide 1.0 (seit 17.10.2026).** Er löst das „Osmera Design System“ vom Juni 2026 (Insignia/Rubik, #071E3D, Cyan #00F0D4) und die KI-Markenboards vom 17.10. ab. Bei Widerspruch gilt der Guide. Quelle: Branch `entwurf/brand-guide-und-skill`, Ordner `brand/` (`osmera-brand.css`, `osmera-tokens.json`, `logos/`, PDF, Bauskripte in `quelle/`). Kopie im iCloud-Ordner `Osmera/01_Marke-und-Design/Brand Guide Website v1.0 (2026-10-17)/`. Das alte Design System liegt unverändert unter `Osmera/Osmera Design System/` (die Bauskripte des Pitch Decks lesen dort), weiteres Abgelöstes unter `Osmera/99_Archiv-abgeloest/`. Nicht als Vorlage verwenden.
- Kleine Schrift und Schalter in `#0369a1`, weil `#0284c7` auf Weiß nur 4,10:1 hat. Warme Töne nur als Hintergrund-Schimmer.
- Stack: HTML, Tailwind Play CDN (cdn.tailwindcss.com), Font Awesome (cdnjs), Google Fonts (Inter, Urbanist). Referenzseite für das Design ist `index.html`.
- Farben: `osmera.blue #0284c7`, `accent #38bdf8`, `dark #0f172a`, `light #f8fafc`, `bluelight #e0f2fe`.
- Logo: zwei konzentrische Ringe plus Wortmarke "osmera" in Urbanist. Die Ringe sind ein verwendbares Motiv.
- Stil: heller Glas-Look (`glass-card`, `glass-nav`), Partikel-Netz im Hintergrund, dunkler Sicherheitsabschnitt.
- Abschnitte: Hero, Die Lösung, Ihr Mehrwert, Die Plattform, Sicherheit, Pilotprojekt (#kontakt), Footer.
- Texte der Seite sind vorhanden und wiederzuverwenden (Hero, Lösung, Pilotprojekt-Schritte, Sicherheit).

## Marken-Haltung

- Telefonieren wird als überflüssig dargestellt. Kein Foto mit telefonierenden Personen als Positivbild.
- Zielgruppe: deutsche Krankenhäuser. Bilder wirken natürlich und nicht zu uneuropäisch.
- Datenschutz ist Kernbotschaft (Zero-Knowledge, Bridge, Token). Keine echten Klinikdaten in Mockups.

## Rechtliches

- Die Datenschutzerklärung ist juristisch geprüft. Nur auf ausdrücklichen Wunsch ändern. Verantwortliche Stelle: "Kutsche Köhl GbR".
- Das Impressum nennt ebenfalls "Kutsche Köhl GbR". Offen: Gesellschafter nennen und den Hinweis "in Gründung" prüfen (Entscheidung des Users).
- Lizenziertes Foto: iStock 1189304032 (Modell- und Property-Freigabe laut Metadaten). Das Canva-Foto darf nicht veröffentlicht werden.

## Stand (17.10.2026)

- Live auf osmera.de: Hero mit Zwei-Personen-Foto und zwei Kacheln, Foto-Band mit Footer, Pilotprojekt-Schritte, neue Sektion "Ihr Mehrwert" (Titel und Rollen-Liste kleben links, Karten laufen vorbei; Tablet Rollen-Chips; Handy Akkordeon; sehr leichter Orange-Schimmer links, Blau rechts), ausklappbare Karten für osmera flow und sync. Letzter Commit auf `main`: `602bef7`.
- Die iStock-Originale liegen außerhalb des Repos in `/Volumes/Scico/osmera_website_gh/originale/` (nicht committen, Lizenz).
- Deployment: Pushes auf `main` gehen live. Die Branches `101026_NewVersion`, `101027_*`, `101028_VersionTwo` erzeugen eine geschützte Staging-Vorschau (dabei werden nur `index.html` und `impressum.html` kopiert). Alle anderen Branch-Namen werden nicht ausgeliefert.
- Brand Guide (Version 1.0, verbindlich) mit Logos als SVG, Stylesheet `osmera-brand.css`, Tokens und PDF: Ordner `brand/` (liegt auf dem Branch `entwurf/brand-guide-und-skill`, nicht auf `main`, nie dorthin mergen). Übergabe für Mobil- und Cloud-Sitzungen: `docs/UEBERGABE.md` auf demselben Branch.
- Offen: Der eigene Workflow „Deploy to GitHub Pages“ scheitert seit mindestens 14.10.2026 im Schritt „Clean up old staging directories“ (Git-Identität fehlt). Live geht die Seite trotzdem über GitHubs „pages build and deployment“ aus `main`. Staging-Kopien der Branches `101026_*`/`101028_*` entstehen vermutlich nicht.

## Typografie-Regel (vom User festgelegt)

- Überschriften, Fließtext und Bedienelemente immer in **Inter**. Nur osmera-Begriffe (das Wort, Produktnamen, Logo) in **Urbanist** (`font-logo`).
- Hervorgehobene Überschriftwörter nutzen den Seitenverlauf `.text-gradient`. Keine eigenen Mehrfarb-Verläufe.

## Arbeitsweise mit dem User

- Für Gestaltungsentscheidungen den Skill `design-konfigurator-prozess` verwenden: Optionen mit Kennungen, Konfigurator-Seite, lokale Vorschau, Messung, Einbau in Staging, Diff, Freigabe.
- Der User nennt Entscheidungen mit Kennungen (D2, P2, l7). Bericht auf Deutsch, knapp, mit Bildern.
