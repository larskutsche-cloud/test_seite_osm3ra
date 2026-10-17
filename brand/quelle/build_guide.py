#!/usr/bin/env python3
"""Baut brand/osmera-brand-guide.html (+ CSS, Tokens) aus den Bausteinen in brand-src/. Ausgabe: <worktree>/brand/"""
import json, shutil, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import guide_a as A
import guide_b as B

OUT = HERE.parent   # Ordner brand/

order = ["titel", "inhalt", "marke", "logo1", "logo2", "farben", "farben2", "konzepte", "typo1", "typo2", "namen", "komp1", "komp2", "icons", "raster", "hintergrund", "bild", "print", "praes1", "praes2", "pdf", "anhang"]
toc_titles = [("Marke", "marke"), ("Logo", "logo1"), ("Farben", "farben"), ("Farbkonzepte und Kontrast", "konzepte"), ("Typografie", "typo1"), ("Bezeichnungen und Sprache", "namen"),
              ("Bausteine: Überschriften, Schalter, Karten", "komp1"), ("Symbole", "icons"), ("Raster, Abstände, Form", "raster"), ("Hintergründe", "hintergrund"), ("Bildwelt", "bild"),
              ("Print", "print"), ("Präsentation", "praes1"), ("PDF und Dokumente", "pdf"), ("Anhang", "anhang")]
toc = [(t, order.index(k) + 1) for t, k in toc_titles]
fn = {"titel": A.p_titel, "inhalt": lambda n: A.p_inhalt(n, toc), "marke": A.p_marke, "logo1": A.p_logo1, "logo2": A.p_logo2, "farben": A.p_farben, "farben2": A.p_farben2, "konzepte": A.p_konzepte,
      "typo1": A.p_typo1, "typo2": A.p_typo2, "namen": B.p_namen, "komp1": B.p_komp1, "komp2": B.p_komp2, "icons": B.p_icons, "raster": B.p_raster,
      "hintergrund": B.p_hintergrund, "bild": B.p_bild, "print": B.p_print, "praes1": B.p_praes1, "praes2": B.p_praes2, "pdf": B.p_pdf, "anhang": B.p_anhang}


import re
VOID = {"img", "br", "hr", "input", "meta", "link", "line", "circle", "rect", "path", "stop", "use"}
WORD = re.compile(r"(?<![\w@./-])osmera(?![\w@])(?!\.(?:de|css|json|html|pdf|svg|png))")


def urbanist(html):
    """Jedes freistehende "osmera" im Text in Urbanist setzen (außer in Code, Titel, Skript, SVG und bereits gesetzten Markenwörtern)."""
    out, stack = [], []
    for part in re.split(r"(<[^>]+>)", html):
        if part.startswith("<!") or not part.startswith("<"):
            skip = any(f for _, f, _ in stack); heading = any(h for _, _, h in stack)
            if part and not skip:
                cls = "osm-marke osm-marke--titel" if heading else "osm-marke"
                part = WORD.sub(f'<span class="{cls}">osmera</span>', part)
            out.append(part); continue
        m = re.match(r"<(/?)([a-zA-Z0-9]+)([^>]*)>", part)
        if m:
            close, name, rest = m.group(1), m.group(2).lower(), m.group(3)
            if close:
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i][0] == name: del stack[i:]; break
            elif name not in VOID and not rest.rstrip().endswith("/"):
                flag = name in ("code", "title", "style", "script", "svg", "pre") or "osm-marke" in rest or "font-logo" in rest or "osm-font-marke" in rest or "Urbanist" in rest
                stack.append((name, flag, name in ("h1", "h2", "h3", "h4")))
        out.append(part)
    return "".join(out)


SCRIPT = """<script>
/* Folien und Briefbogen auf schmalen Bildschirmen verkleinern (im Druck nicht) */
(function () {
  function fit() {
    document.querySelectorAll('.mini-wrap').forEach(function (m) {
      m.style.zoom = '';
      var avail = m.parentElement.clientWidth - 2, w = m.offsetWidth;
      if (w > avail && avail > 0) m.style.zoom = (avail / w).toFixed(3);
    });
  }
  window.addEventListener('load', fit); window.addEventListener('resize', fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
})();
</script>"""


def build():
    pages = "\n".join(fn[k](i + 1) for i, k in enumerate(order))
    css = (HERE / "guide.css").read_text(encoding="utf-8")
    doc = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>osmera Brand Guide 1.0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Urbanist:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="osmera-brand.css">
<style>
{css}
</style>
</head>
<body class="osm" style="background:#e8edf4">
<main class="sheet">
{pages}
</main>
{SCRIPT}
</body>
</html>
'''
    return urbanist(doc)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "osmera-brand-guide.html").write_text(build(), encoding="utf-8")
    shutil.copy2(HERE / "tokens.json", OUT / "osmera-tokens.json")   # osmera-brand.css liegt direkt in brand/ und wird dort gepflegt
    print("Guide:", (OUT / "osmera-brand-guide.html").stat().st_size // 1024, "KB")
