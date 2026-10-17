#!/usr/bin/env python3
"""Vorlage für den Einbau eines entschiedenen Designs in eine KOPIE der echten Seite (Staging).

Die Quelle (echte Seite) wird nur gelesen. Jede Ersetzung muss genau einmal treffen (assert), sonst bricht das Skript ab.
Ablauf: Abschnitt ersetzen → altes CSS und altes Skript entfernen → neues CSS und Skript einfügen → Begleitdateien kopieren.

  python3 einbau-skript.py           baut den Staging-Ordner neu
  python3 einbau-skript.py --check   prüft, ob der Staging-Ordner noch zur aktuellen Quelle passt ("Staging aktuell zur Basis: True")
  python3 einbau-skript.py --diff    schreibt aenderungen.diff neben das Skript und nennt die Zeilenzahl

Anpassen: nur den Block KONFIGURATION. Anker sind kurze, eindeutige Textstellen der Quelle.
"""
import difflib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent

# ----------------------------------------------------------------------------- KONFIGURATION
SRC = Path("/PFAD/zur/echten/Seite")            # Ordner mit index.html (nur lesen!)
OUT = HERE / "out" / "site"                     # Staging-Ordner (wird neu geschrieben)
PAGE = "index.html"
COPY_FILES = ["impressum.html", "datenschutz.html", "CNAME"]   # Begleitdateien, falls vorhanden
COPY_DIRS = ["img"]

SECTION_START = '    <section id="abschnitt"'      # erster Anker: Beginn des alten Abschnitts
SECTION_END = '    <section id="naechster"'        # zweiter Anker: Beginn des nächsten Abschnitts (bleibt erhalten)
NEW_SECTION = HERE / "abschnitt.html"              # neuer Abschnitt (Inhalt EINMAL, Umschalten per CSS)

CSS_OLD_FROM = "        /* altes CSS Anfang */"     # alter CSS-Block, wird durch NEW_CSS ersetzt (von hier ...
CSS_OLD_TO = "        /* hinter dem alten CSS */"  # ... bis hier, dieser Anker bleibt erhalten)
NEW_CSS = HERE / "abschnitt.css"

JS_REMOVE_LINES = [                                # alte Zeilen, die genau einmal vorkommen und ganz entfallen
    # "        const alterContainer = document.getElementById('abschnitt');\n",
]
JS_OLD_FROM = None                                 # optional: alter Skriptblock von ... (None = überspringen)
JS_OLD_TO = None                                   # ... bis (dieser Anker bleibt)
NEW_JS = HERE / "abschnitt.js"                     # kommt vor </body>, in einer geschlossenen Funktion
# --------------------------------------------------------------------------------------------


def once(s: str, anchor: str) -> int:
    n = s.count(anchor)
    assert n == 1, f"Anker kommt {n}x vor (erwartet 1x): {anchor[:70]!r}"
    return s.index(anchor)


def replace_between(s: str, start: str, end: str, new: str) -> str:
    a, b = once(s, start), once(s, end)
    assert a < b, f"Reihenfolge der Anker stimmt nicht: {start[:40]!r} / {end[:40]!r}"
    return s[:a] + new + s[b:]


def build() -> str:
    s = (SRC / PAGE).read_text(encoding="utf-8")
    s = replace_between(s, SECTION_START, SECTION_END, NEW_SECTION.read_text(encoding="utf-8"))
    s = replace_between(s, CSS_OLD_FROM, CSS_OLD_TO, NEW_CSS.read_text(encoding="utf-8") + "\n")
    for line in JS_REMOVE_LINES:
        once(s, line)
        s = s.replace(line, "")
    if JS_OLD_FROM:
        s = replace_between(s, JS_OLD_FROM, JS_OLD_TO, "")
    once(s, "</body>")
    return s.replace("</body>", NEW_JS.read_text(encoding="utf-8") + "</body>")


def write_out(html: str) -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / PAGE).write_text(html, encoding="utf-8")
    for f in COPY_FILES:
        if (SRC / f).exists():
            shutil.copy2(SRC / f, OUT / f)
    for d in COPY_DIRS:
        if (SRC / d).exists():
            shutil.copytree(SRC / d, OUT / d)


if __name__ == "__main__":
    html = build()
    if "--check" in sys.argv:
        print("Staging aktuell zur Basis:", (OUT / PAGE).exists() and (OUT / PAGE).read_text(encoding="utf-8") == html)
    elif "--diff" in sys.argv:
        a = (SRC / PAGE).read_text(encoding="utf-8").splitlines(keepends=True)
        d = list(difflib.unified_diff(a, html.splitlines(keepends=True), PAGE + " (Quelle)", PAGE + " (Staging)"))
        (HERE / "aenderungen.diff").write_text("".join(d), encoding="utf-8")
        print("aenderungen.diff:", len(d), "Zeilen")
    else:
        write_out(html)
        print(OUT / PAGE, (OUT / PAGE).stat().st_size // 1024, "KB")
