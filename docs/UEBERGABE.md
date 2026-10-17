# Übergabe: osmera Website, Brand Guide und Design-Prozess

Stand: 17.10.2026. Dieser Branch (`entwurf/brand-guide-und-skill`) ist **kein Website-Stand**. Er liegt auf GitHub, damit Arbeit am Handy oder in einer Cloud-Sitzung anknüpfen kann. Er wird vom Deploy-Workflow nicht ausgeliefert.

## Wichtigste Regeln

1. **Diesen Branch nie nach `main` mergen.** Der Deploy von `main` veröffentlicht den ganzen Ordner (auch `brand/`, `docs/`, `konzepte/`) auf osmera.de. Die Website-Datei `index.html` ist auf diesem Branch identisch mit `main` (Commit `602bef7`).
2. **Das Repo ist öffentlich.** Alles auf diesem Branch ist für jeden lesbar, auch wenn es nicht auf der Website erscheint. Keine Zugangsdaten, keine Kundendaten, keine internen Zahlen ablegen.
3. **Deploy-Auslöser** (`.github/workflows/deploy.yml`): Push auf `main` (Produktion), `101026_NewVersion`, `101027_*`, `101028_VersionTwo` (Staging). Branches mit anderen Namen, zum Beispiel `entwurf/*`, werden nicht ausgeliefert. Den manuellen Workflow-Start (`workflow_dispatch`) nicht mit diesem Branch ausführen.
4. **Push auf `main` ist der Live-Gang.** Nur auf ausdrücklichen Wunsch von Lars, und vorher die Änderung zeigen.
5. **Änderungen immer erst zeigen, dann übernehmen.** Erst Diff oder Vorschau, dann OK abwarten, dann schreiben.
6. **Datenschutztext** (`datenschutz.html`) ist juristisch geprüft. Nur auf ausdrückliche Anweisung ändern.
7. **Inhaltliche Leitplanken:** Zielgruppe sind deutsche Krankenhäuser. Keine erfundenen Zahlen, Zitate oder Referenzkunden. Telefonate nie als Vorteil darstellen (osmera macht Anrufe überflüssig).
8. **Verbindliches Design:** Der Brand Guide 1.0 in `brand/` gilt seit 17.10.2026 als maßgeblich für alle neuen Unterlagen und Oberflächen. Er löst das ältere „Osmera Design System“ (Juni 2026: Insignia, Rubik, `#071E3D`, Cyan `#00F0D4`) ab. Nie daraus ableiten. Bei Widerspruch gilt der Guide.
9. **Schrift:** Alles in Inter. Nur osmera-Begriffe (Wort „osmera“, Produktnamen, Logo) in Urbanist, im Code als Klasse `font-logo`. Hervorgehobene Wörter in Überschriften nutzen `.text-gradient`.

## Stand der Website

- Live: https://osmera.de (Stand `main` = `602bef7`, 17.10.2026).
- Stack: statisches HTML, Tailwind über Play-CDN, Font Awesome 6.4.0, Google Fonts (Inter, Urbanist). Die Tailwind-CDN braucht JavaScript, die Seite also über HTTP öffnen, nicht per `file://`.
- Zuletzt fertig: Abschnitt **„Ihr Mehrwert“** (`#vorteile`). Desktop: Titel und Rollenliste kleben links, die Karten laufen rechts vorbei. Tablet (640 bis 1023 px): Rollen-Chips mit einer Karte, wechselt alle 7 Sekunden bis zur ersten Eingabe. Handy (unter 640 px): Akkordeon. Hintergrund: sehr leichtes Orange links, Blau rechts.
- Arbeitsordner auf dem Mac von Lars: `development/` (Branch `101026_NewVersion`) ist der Ort für Änderungen, der Hauptordner ist live, `staging-101028/` ist tabu.

## Was auf diesem Branch liegt

| Pfad | Inhalt |
|---|---|
| `brand/` | Brand-Paket v1.0: `osmera-brand-guide.pdf` (22 Seiten A4 quer), HTML-Version, `osmera-brand.css`, `osmera-tokens.json`, `osmera-farben.gpl`, `logos/` (8 SVG), `quelle/` (Skripte, die alles erzeugen), `README.md` |
| `konzepte/` | Konfigurator-Seiten für „Ihr Mehrwert“: `mehrwert-layout.html` (final, mit Hintergrund-Stufen, Blau-Seite, Farbspot) und `mehrwert-runde2.html` (Galerie D1 bis D5, P1 bis P3). Im Browser über HTTP öffnen. |
| `.claude/skills/design-konfigurator-prozess/` | Skill für den Arbeitsablauf „Optionen bauen, auf der Seite umschaltbar zeigen, auswählen, einbauen“ (Kennungen wie M1, D2, l7, Konfigurator-Vorlage, Mess-Skripte, Einbau- und Deploy-Hinweise) |
| `.claude/skills/web-ui-design/` | Allgemeiner Web-Design-Skill samt `references/osmera.md` (Projektregeln) |
| `.claude/agents/web-ui-design-lead.md` | Agent für Gestaltungskonzepte, verweist auf den Konfigurator-Skill |
| `docs/UEBERGABE.md` | diese Datei |

Skill-Version: `design-konfigurator-prozess` 1.0 mit Konfigurator-Vorlage, Einbau-Skript-Vorlage und Anleitung zur Pflege des Guides (`references/marke-und-guide.md`).

## Brand Guide in einem Absatz

Logo: zwei konzentrische Ringe (außen ⌀28, innen ⌀20, Strich 2) plus „osmera“ in Urbanist Bold, Abstand 10, Laufweite −0,025 em, Ringmitte auf Höhe der Mitte der Kleinbuchstaben. Farben: osmera-Blau `#0284c7`, Blau dunkel `#0369a1`, Himmelblau `#38bdf8`, Navy `#0f172a`, Grund `#f8fafc`, Rollenfarben (Planende Blau, Team Violett `#9333ea`, PR/MAV Grün `#059669`, HR & IT Grau `#475569`, Leitung & DSB Bernstein `#d97706`). Warmes Orange `#ff6531` nur als Hintergrund-Schimmer unter 10 % Deckkraft, nie für Text oder Buttons. Werte sind entweder „Bestand“ (so auf der Website) oder „Empfehlung“ (neu festgelegt, etwa für Print und Folien).

## Offene Punkte

1. **Kontrast:** osmera-Blau auf Weiß hat 4,10:1 und verfehlt WCAG AA für kleine Schrift. Für kleinen Text und Buttons Blau dunkel `#0369a1` (5,93:1) verwenden. Auf der Website noch nicht angepasst.
2. **Favicon fehlt.** Vorschlag liegt als `brand/logos/osmera-app-icon.svg`.
3. **Altes Design System:** ist abgelöst (entschieden 17.10.2026). Bestehende Unterlagen im alten Stil, vor allem das Pitch Deck 09/2026, bei der nächsten Überarbeitung auf den Brand Guide umstellen. Das alte System nutzt dasselbe Präfix `--osm-`, deshalb nie Dateien mischen.
4. **Logo-Ringfarbe:** auf der Website `#1E293B`, Wortmarke `#0F172A`. Vereinheitlichen?
5. **Font „Outfit“** wird geladen, aber nirgends benutzt.
6. **Tailwind per CDN** (Play-CDN, nicht für Produktion gedacht). Langfristig Build-Schritt erwägen.
7. **CMYK-Werte** im Guide sind rechnerische Näherungen. Für den Druck Profil (zum Beispiel PSO Coated v3) und Proof bei der Druckerei einplanen. Keine Pantone-Zuordnung vorhanden.
8. **Deploy-Workflow:** „Deploy to GitHub Pages“ scheitert seit mindestens 14.10.2026 im Schritt „Clean up old staging directories“ (Git-Identität fehlt, Exit 128). Die Seite geht trotzdem über GitHubs „pages build and deployment“ aus `main` live. Staging-Kopien der Branches `101026_*` und `101028_*` entstehen vermutlich nicht. Nicht behoben.
9. **Sitemap:** `lastmod` für `index.html` und `impressum.html` steht noch auf 2026-10-10.

## Guide neu erzeugen

Zum Neubauen nur Python 3 nötig. Für neue Logos zusätzlich `pip install fonttools uharfbuzz` und die Schrift Urbanist Bold (Google Fonts, SIL OFL) als `brand/quelle/fonts/Urbanist-700.ttf`.

```bash
cd brand/quelle
python3 tokens.py        # rechnet die Farben, schreibt tokens.json (im aktuellen Ordner)
python3 make_logos.py    # nur bei Logo-Änderung, braucht die Schrift (siehe oben)
python3 build_guide.py   # schreibt ../osmera-brand-guide.html und ../osmera-tokens.json
```

`osmera-brand.css` liegt direkt in `brand/` und wird dort von Hand gepflegt. Das PDF entsteht aus der HTML-Datei per Headless-Chrome. Dazu den **Repo-Stamm** (nicht `brand/`) über einen lokalen Server bereitstellen, damit die Fotos unter `../img/` gefunden werden (zum Beispiel `python3 -m http.server 8780` im Repo-Stamm) und dann:

```bash
node .claude/skills/design-konfigurator-prozess/scripts/pdf.mjs http://localhost:8780/brand/osmera-brand-guide.html brand/osmera-brand-guide.pdf
```

Danach prüfen: 22 Seiten, nichts läuft über den Rand, und **alle Seiten als Bild ansehen** (Fotos, Logos, Bildmarke, App-Icon müssen da sein; fehlende Bilder erscheinen als Alt-Text mit Platzhalter-Symbol).
