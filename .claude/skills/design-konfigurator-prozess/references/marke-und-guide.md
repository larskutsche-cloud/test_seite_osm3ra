# Verbindliche Marke und Pflege des Brand Guides

## Rangfolge bei Widersprüchen

1. Ausdrückliche Worte des Auftraggebers in der Sitzung.
2. Der **verbindliche Brand Guide** (wenn es einen gibt). Prototypen und Einbau übernehmen seine Werte, sie erfinden keine neuen.
3. Der Code der echten Seite (Bestand). Der Guide beschreibt ihn; weicht beides ab, ist das ein Befund für den Bericht.
4. Älteres und abgelöstes Material (alte Design Systems, KI-Entwürfe, frühere Website-Fassungen): **nie** als Quelle für neue Arbeit verwenden. Es liegt im Archiv.

## osmera: was verbindlich ist (seit 17.10.2026)

Der Brand Guide **Version 1.0** der Website ist die maßgebliche Grundlage für alle neuen osmera-Unterlagen und Oberflächen (Website, Print, PDF, Präsentationen, Dokumente). Er löst das „Osmera Design System“ vom Juni 2026 (Insignia/Rubik, #071E3D, Cyan #00F0D4) ab. Die KI-Markenboards vom 17.10. (Türkis, Sofia Pro) sind Entwürfe, keine Marke.

| Was | Wo |
|---|---|
| Quelle in Git | Branch `entwurf/brand-guide-und-skill`, Ordner `brand/` (Guide, CSS, Tokens, Logos, `quelle/` mit den Bauskripten). **Nie nach `main`**, der Deploy von `main` veröffentlicht den ganzen Ordner. |
| Arbeitsablage iCloud | `Osmera/01_Marke-und-Design/Brand Guide Website v1.0 (2026-10-17)/` mit PDF, `Brand-Paket/`, Prototypen, Screenshots, Skill-Kopie |
| Abgelöstes | `Osmera/99_Archiv-abgeloest/`. Ausnahme: `Osmera/Osmera Design System/` bleibt am alten Platz, weil die Bauskripte des Pitch Decks 2026-09 diesen Pfad lesen. Nicht als Vorlage benutzen. |

Was Prototypen und Einbau aus dem Guide nehmen:
- Farben und Namen aus `osmera-tokens.json` (Klassen und Variablen mit Präfix `.osm-` / `--osm-` aus `osmera-brand.css`).
- Logo nur aus `logos/` (SVG, Schrift in Pfaden), Schutzzone und Mindestgrößen wie im Guide.
- Typografie: alles in Inter, nur osmera-Begriffe in Urbanist (`font-logo`), Hervorhebung in Überschriften mit `.text-gradient`.
- Kleine Schrift und Schalter in `#0369a1` (Blau dunkel), weil osmera-Blau `#0284c7` auf Weiß nur 4,10:1 erreicht.
- Warme Töne (Orange `#ff6531`, Koralle, Pfirsich) nur als Hintergrund-Schimmer, nie für Text oder Schalter.
- Neue Farbe, neue Schrift, neues Logo-Motiv nur mit ausdrücklicher Entscheidung des Auftraggebers, danach in den Guide eintragen.

## Schritt 10: Marke nachziehen (nach jeder Übernahme)

Berührt die Entscheidung die Marke (neuer Baustein, neue Karte, neuer Hintergrund, neue Farbe, neue Regel), wird der Guide in derselben Runde fortgeschrieben, sonst läuft er der Seite davon.

1. **Eintragen.** Baustein in `quelle/guide_a.py` oder `guide_b.py` auf der passenden Seite ergänzen (Bestand oder Empfehlung kennzeichnen), Farben in `quelle/tokens.py`, Klassen in `osmera-brand.css`.
2. **Version erhöhen.** Neue Werte oder Seiten = Minor (1.0 → 1.1). Änderung, die bestehende Unterlagen ungültig macht = Major (2.0). Nur Text oder Schreibfehler = Fassung beibehalten, Datum im Änderungsverlauf. Die Nummer steht an fünf Stellen und muss überall gleich sein: Titelseite und Seitenkopf (`guide_a.py`), Änderungsverlauf (`guide_b.py`, Seite 22), `README.md`, Kopf von `osmera-brand.css`, `meta` in `tokens.py`.
3. **Neu bauen.**
   ```bash
   cd brand/quelle && python3 tokens.py && python3 build_guide.py   # schreibt ../osmera-brand-guide.html und ../osmera-tokens.json
   ```
4. **Prüfen.** Druck-Emulation, Fenster 1123 × 794: keine Seite darf über ihre feste Höhe hinausragen (Beispiel in `pruefen.md`). Seitenzahl nennen. Schriftregel (Markenwörter in Urbanist) und Kontraste stichprobenartig ansehen.
5. **PDF erzeugen.** Den **Repo-Stamm** (nicht `brand/`) über einen lokalen Server bereitstellen, weil das HTML die Fotos unter `../img/` sucht, dann `node scripts/pdf.mjs http://localhost:PORT/brand/osmera-brand-guide.html brand/osmera-brand-guide.pdf`. Prüfen: Seitenzahl, Format (297 × 210 mm), und **alle Seiten als Kontaktbogen ansehen** (Fotos, Logos, Bildmarke, App-Icon da?). Testserver danach beenden. Vorher per `cdp.mjs` bestätigen, dass `document.images` keine kaputten Bilder enthält.
6. **Ablegen.** Neuer iCloud-Ordner `Brand Guide Website vX.Y (JJJJ-MM-TT)` unter `01_Marke-und-Design/`, die alte Fassung nach `99_Archiv-abgeloest/` verschieben (nichts überschreiben). Entwurfs-Branch committen und pushen (`entwurf/…`), nur die Pfade `brand/`, `konzepte/`, `docs/`, Skills und Agent, nie `.claude/launch.json`.
7. **Memory und Übergabe aktualisieren** (`docs/UEBERGABE.md`, Projekt-Memory).

## Ordner neu ordnen (iCloud oder Projekt)

Gelernt am 17.10.2026: Vor dem Verschieben die **Abhängigkeiten** suchen (absolute Pfade in Bau-Skripten, Verweise in Anleitungen und Listen, relative Geschwister-Verweise). Was abhängt, bleibt am Platz oder zieht zusammen um. Nur verschieben, nichts löschen oder umbenennen, Vorher/Nachher vergleichen (Dateizahl und Bytes je Eintrag), ein Protokoll und ein Rückgängig-Skript ablegen. Namen mit Umlauten vergleichen mit normalisierter Schreibweise (macOS liefert sie zerlegt).
