# Einbau in die echte Seite

Erst wenn der Auftraggeber Layout, Hintergrund und Einstellungen gewählt hat.

## 1. Staging-Kopie, nie direkt

- Quelle ist der aktuelle Stand der echten Seite (lesen, nicht ändern). Das Ergebnis liegt in einem eigenen Ordner (z.B. `scratchpad/out/site/`) mit allem, was die Seite braucht (Bilder, Unterseiten).
- Der Einbau läuft als **Skript** (`build_site.py`), das die Quelle liest, den Abschnitt ersetzt und die Kopie schreibt. Vorteile: jeder Fehler ist wiederholbar behebbar, die Basis kann nach Änderungen neu gebaut werden, es entsteht ein sauberer Diff. Das Skript prüft per `assert`, dass jede Ersetzung genau einmal trifft.
- Danach das Skript gegen die Quelle laufen lassen und vergleichen („Staging aktuell zur Basis: True“), bevor kopiert wird. Wenn sich die Quelle inzwischen geändert hat, nicht blind überschreiben.

## 2. Bausteine für den Abschnitt

- **Inhalt einmal im HTML.** Keine doppelten Texte für Desktop, Tablet und Handy. Umschalten macht das CSS (Breakpoints 640 und 1024), nicht doppelte Elemente. Beispiel: je Rolle ein Element mit Akkordeon-Kopf und Karte; Kopf nur am Handy sichtbar.
- **Gescopte Klassen.** Eigene Klassen mit Präfix (`mw-`, `osm-`), Variablen am Abschnitt (`#vorteile{--mw-b1:…}`), nichts Globales. Bestehende Regeln der Seite (Tailwind-Preflight, vorhandene Karten) nicht überschreiben.
- **Skript als eigener Block** vor `</body>`, in einer geschlossenen Funktion, mit `matchMedia` für die Modi. Keine Abhängigkeit von Bibliotheken, `prefers-reduced-motion` beachten.
- **Alten Code entfernen**, nicht nur überlagern: CSS-Regeln, Skriptblock im Scroll-Handler, Konstanten. Danach nach Resten suchen (`grep` auf alte Klassennamen).
- **Texte unverändert** aus der Seite übernehmen. Markenwörter (hier „osmera“) nach der Typografie-Regel setzen.
- **Sticky und Anker:** `position: sticky; top` auf die tatsächliche Menühöhe abstimmen; Sprungziele über negative `scroll-margin-top`-Werte so einstellen, dass die Überschrift bei allen Abschnitten gleich weit unter dem Menü landet (messen, nicht schätzen).
- **Abstände zum Nachbarn ausgleichen**: Abstand letzte Karte des Vorgängers → Überschrift und letzte Karte → nächste Überschrift sollen gleich sein (hier 161/160 px).

## 3. Diff und Gesamtblick

- `diff -u quelle staging > aenderungen-<thema>.diff`, Zeilenzahl nennen, bestätigen, dass nur die vorgesehenen Dateien abweichen.
- **Gesamtblick:** (a) Vollseite bei Desktop-Breite, in vier Streifen nebeneinander montiert, (b) die neue Sektion im Zusammenhang mit Übergängen, (c) Tablet und Handy mit echter Breite. Die Seite zusätzlich im Browser-Bereich öffnen (`preview_start` / `navigate`) und die Adresse nennen.

## 4. Übernahme

1. OK des Auftraggebers abwarten.
2. Backup der Zieldatei(en) ablegen (Scratchpad).
3. Kopieren, Gleichheit mit `cmp` bestätigen.
4. Commit nur der betroffenen Datei(en): `git add datei` und `git commit -m "…" -- datei` (so bleiben fremde lokale Änderungen, z.B. an `.gitignore`, draußen).
5. Nach dem Commit nichts pushen, außer der Auftraggeber hat es ausdrücklich erlaubt („Du kannst pushen“).

## 5. Deployment verstehen, bevor gepusht wird

- `.github/workflows/*.yml` lesen: Welche Branches lösen eine Auslieferung aus? Welche gehen live, welche als geschützte Vorschau?
- **Live-Branch (z.B. `main`)** veröffentlicht den ganzen committeten Ordner. Nur Dateien committen, die öffentlich sein dürfen (keine Originale in voller Auflösung, keine internen Guides, keine Lizenzdateien).
- Ein Branch mit einem Namen, der nicht zu den Auslöser-Mustern passt, liegt auf GitHub, ohne ausgeliefert zu werden. Das ist der Weg für Arbeitsstände, die mobil erreichbar sein sollen. Ist das Repository öffentlich, ist der Inhalt dort sichtbar, auch wenn er nicht als Website läuft.
- Nach dem Push im Hintergrund auf die neue Version warten (`curl` in einer Schleife, Suchbegriff aus der neuen Version, Zwischenspeicher mit `?cb=` umgehen) und dann dieselben Prüfungen gegen die echte Adresse fahren (Status, Inhalt, Überlauf bei drei Breiten).

## 6. Danach

Memory aktualisieren (Commit, was live ist, was offen bleibt). Erkenntnisse, die die Marke betreffen (Schrift, Farbe), als Regel festhalten.
