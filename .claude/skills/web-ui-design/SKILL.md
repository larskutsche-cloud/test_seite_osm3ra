---
name: web-ui-design
description: Leitfaden für Frontend- und Web-UI-Design. Konzepte entwickeln, Layouts, Heroes und Bildeinsatz gestalten, Seiten responsiv und barrierearm umsetzen, Bilder optimieren und lizenzsicher einsetzen, Gestaltung prüfen. Verwenden bei Aufgaben wie "Design verbessern", "Konzepte für die Startseite", "Foto einbauen", "Landingpage gestalten", "Hero", "Layout prüfen", "UI-Review", "Tailwind-Seite". Use for web UI design, landing pages, image placement, creative concepts, responsive and accessibility checks.
---

# Web-UI-Design

Dieser Skill führt durch kreative Webdesign-Aufgaben vom Konzept bis zur geprüften Umsetzung. Er ist allgemein gehalten. Projektspezifisches (zum Beispiel osmera) steht unter `references/`.

## 1. Zuerst klären

- Gibt es Projektregeln (CLAUDE.md, Memory, Aussagen des Users)? Sie gehen vor. Typisch: nur in einem bestimmten Ordner arbeiten, Änderungen vor dem Kopieren zeigen, fertige Texte (zum Beispiel juristisch geprüfte Datenschutztexte) nicht anfassen.
- Was ist das eine Ziel der Seite oder des Abschnitts (erster Eindruck, Vertrauen, Anfrage)? Wer liest sie?
- Welche Bilder und Marken-Vorgaben gibt es, und sind die Bilder lizenziert? Siehe Abschnitt 5.
- Gibt es ein bestehendes Design (Farben, Schriften, Komponenten)? Dann daran halten.
- Bei Aufgaben für **osmera** (Dienstplan-Add-on für Kliniken) zuerst `references/osmera.md` lesen. Es enthält Ordnerregeln, Marke, Texte und den aktuellen Stand der Bildarbeit.

## 2. Ablauf

1. **Referenzen ansehen.** Die vom User genannten Seiten wirklich öffnen und die Struktur lesen (Abschnitte, Bildrolle, Abstände). Wenn die Seite im Browser ohne Styles lädt, trotzdem DOM und Bild-URLs auswerten und Bilder direkt öffnen.
2. **Konzepte entwerfen.** Mindestens drei wirklich verschiedene Ideen, keine Varianten derselben. Verschiedene Orte durchdenken: Hero, Abschluss vor dem Footer, Statement-Band in der Seitenmitte, Foto im Kontakt-Abschnitt, Produkt-Mockup statt Foto.
3. **Prototypen im Staging bauen**, nie direkt im geschützten Ordner. Jeder Prototyp ist lauffähig und responsiv.
4. **Prüfen** (Abschnitt 6) und Ergebnisse ehrlich berichten, auch was nicht geprüft wurde.
5. **Entscheidungsvorlage liefern:** Konzept-Board mit Mockup, Stärken, Risiken, Aufwand, Kombinationen und offenen Fragen. Bei Bedarf als privates Artifact veröffentlichen, damit der Link bestehen bleibt.
6. **Umsetzen erst nach Entscheidung.** Vor dem Schreiben in den Projektordner die Änderungen zeigen (Diff oder Liste), Backup des Vorzustands ablegen, danach prüfen.

## 3. Gestaltungsgrundsätze

- **Hierarchie:** pro Bildschirm ein Hauptakzent. Überschrift, Unterzeile, Button in dieser Reihenfolge lesbar.
- **Raster und Abstand:** Abstände aus einer Skala (4/8 px). Gleiche Rollen haben gleiche Abstände, Radien und Schatten.
- **Typografie:** höchstens zwei Familien, feste Größenskala, Fließtext 60 bis 75 Zeichen breit, Überschriften mit `text-wrap: balance`.
- **Farbe:** Markenfarbe als einziger Akzent. Kontrast Text auf Fläche mindestens 4,5:1, große Schrift 3:1. Neutrale Grautöne zur Markenfarbe hin färben.
- **Weißraum:** lieber ein Element weniger. Ruhe wirkt hochwertig.
- **Karten sparsam:** Rand, Fläche, Radius und Schatten nur dort, wo ein Element wirklich abgesetzt werden soll.
- **Bewegung:** höchstens ein orchestrierter Moment. Immer `prefers-reduced-motion` respektieren.
- **Texte:** vorhandene Texte der Seite wiederverwenden. Neue Texte als Platzhalter kennzeichnen. Keine erfundenen Zitate, Zahlen oder Kundennamen.

## 4. Bildeinsatz

Orte, an denen ein großes Foto wirkt:

| Ort | Wirkung | Hinweis |
|---|---|---|
| Hero | erster Eindruck | Foto trägt keine Kacheln über dem Gesicht |
| Band vor dem Footer | bleibender Abschluss | große Fläche mit Freiraum, CTA davor, mobil eigener Ausschnitt |
| Statement-Band in der Seitenmitte | Atempause | ein Satz, Text im unscharfen Bereich |
| Kontakt-/Pilotabschnitt | Gesicht bei der Entscheidung | Button unter dem Foto statt darüber |
| Avatar im Produkt-Mockup | Menschlichkeit ohne Textlast | klein, kein Gesicht-Problem |

Regeln:

- **Das Gesicht wird nie überdeckt.** Overlays nur in freien Zonen (unscharfer Hintergrund, Wand, Kleidung). Vor jedem Overlay die Fläche rechnerisch prüfen (`references/overlay-check.js`).
- **Kacheln mit Geschichte (Problem und Lösung) immer als Paar zeigen oder gar nicht.** Eine einzelne Lösungs-Kachel ohne Problem ergibt keinen Sinn.
- **Overlay-Größen relativ zum Foto planen**, nicht mit festen Pixeln. Ein Foto ist im schmalen Browserfenster nur etwa 460 px breit.
- **Text auf Foto** nur im unscharfen Bereich mit Verlauf darunter. Mobil das Foto über den Text stapeln, nicht darunterlegen.
- **Eigener Ausschnitt pro Breite** (Quadrat, Querformat, mobil), Gesicht im oberen Drittel, Hände und Gerät im unteren.
- **Alt-Text** beschreibt Sichtbares neutral ("Eine Ärztin mit Tablet lächelt in die Kamera"), ohne Namen und ohne Vermutungen.
- **Natürliche, ruhige Fotos** vor gestellten Gruppenfotos. Blickkontakt und Freiraum zum Text hin.

## 5. Bilder und Lizenzen

Bilder in drei Schritten behandeln. Befehle stehen in `references/bild-pipeline.md`.

1. **Herkunft klären.** Dateiname, Metadaten (XMP/IPTC mit `strings`), Hinweis auf Freigaben. Eine "SVG-Grafik" ist oft ein Foto in einem SVG-Mantel (Base64-JPEG): herauslösen, nicht einbetten.
2. **Rechte einschätzen** (keine Rechtsberatung, das dem User sagen):
   - *Canva:* Pro-Inhalte nicht als eigenständiges Element, für unbearbeitete Medien online gibt es Pixelgrenzen. Für eine Website unsicher.
   - *Unsplash, Pexels, Pixabay:* Urheberrecht frei, Modellfreigaben nicht garantiert. Erkennbare Personen auf einer Firmenseite sind riskant. Fotograf nach Freigabe fragen.
   - *iStock, Adobe Stock, Getty, Shutterstock:* Freigaben werden geprüft. Metadaten zeigen "Model and Property Released". Rechnung aufbewahren.
   - *Unsplash+:* Freigaben und Rechtsschutz inklusive, Abo nötig.
   - *Eigenes Shooting:* beste Authentizität, Einwilligungen schriftlich einholen.
3. **Veröffentlichen nur optimiert:** AVIF und WebP in mehreren Größen, Originale und Wrapper bleiben aus dem Repo. In veröffentlichten Mockups (Artifacts, Boards) nur lizenzierte Bilder verwenden, sonst Platzhalter.

## 6. Prüfen

Vollständige Liste: `references/qualitaetspruefung.md`. Kurzfassung:

- Vorschau über **HTTP**, nicht über `file://`. Seiten mit Tailwind-Play-CDN brauchen JavaScript, ein statischer Schnappschuss zeigt nur rohen Text. Lokalen Server im Hintergrund starten.
- Breiten: 375, 414, 640, 768, 1023, 1024, 1062, 1279, 1280, 1440, 1920. Kein horizontales Scrollen, keine Konsolenfehler.
- Overlay-Prüfung gegen Gesichts- und Gerätezone bei allen Breiten.
- Hell und dunkel, wenn die Seite beides kann. Tastaturfokus sichtbar. Alt-Texte vorhanden.
- Erst melden, was gemessen wurde. Annahmen als Annahmen kennzeichnen.

## 7. Datenschutz (Deutschland)

- Schriften, Icons und Skripte von Drittanbietern übertragen die IP-Adresse. Sie gehören in die Datenschutzerklärung oder werden selbst gehostet. Das Tailwind-Play-CDN ist laut Tailwind nur für die Entwicklung gedacht. Empfehlung für den Livebetrieb: CSS vorab bauen, Schriften und Icons selbst hosten.
- Juristisch geprüfte Texte nicht ändern, außer der User verlangt es ausdrücklich. Ergänzungen als eigene Textblöcke kennzeichnen.
- Mockups ohne echte Klinik- oder Personendaten.

## 8. Zusammenarbeit

- Auf Deutsch antworten, knapp, ohne Ausschmückung. Ergebnis zuerst.
- Bei Entscheidungen mit mehreren guten Wegen eine Empfehlung nennen und begründen.
- Nach jedem Schreibzugriff in geschützte Ordner den Stand per `git status` zeigen.
- Sessions erzeugen Erkenntnisse (zum Beispiel "Overlay muss relativ zum Foto sein"). Dauerhaft Wichtiges in die Memory schreiben.
