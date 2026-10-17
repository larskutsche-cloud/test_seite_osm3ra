"""Erzeugt die osmera-Logos als reine Vektoren (Schrift in Pfade umgewandelt, Urbanist Bold, OFL).

Maße stammen aus der Website (Navigation): Ring außen 28 px (Rand 2 px), Ring innen 20 px (Rand 2 px), konzentrisch,
Abstand Ring zu Wortmarke 10 px, Schriftgröße 27,2 px (1,7 rem), Laufweite -0,025 em (tracking-tight).
Der Ringmittelpunkt liegt auf der Mitte der x-Höhe der Wortmarke (vom User so bestätigt).
"""
import json, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

F = 1000.0                       # Schriftgröße in SVG-Einheiten
SITE_F = 27.2                    # Schriftgröße auf der Website in px
k = F / SITE_F                   # Umrechnung px (Website) -> SVG-Einheiten
ring_outer_d = 28 * k            # Außendurchmesser Ring
stroke = 2 * k
r_out = ring_outer_d / 2 - stroke / 2          # Mittellinie äußerer Ring
r_in = (20 * k) / 2 - stroke / 2               # Mittellinie innerer Ring
gap = 10 * k
tracking = -0.025 * F

font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "Urbanist-700.ttf")   # von Google Fonts laden, siehe README
tt = TTFont(font_path); upem = tt["head"].unitsPerEm; gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
blob = hb.Blob.from_file_path(font_path); face = hb.Face(blob); hbfont = hb.Font(face)
buf = hb.Buffer(); buf.add_str("osmera"); buf.guess_segment_properties(); hb.shape(hbfont, buf, {"kern": True})
scale = F / upem
x_height = tt["OS/2"].sxHeight * scale
cap = tt["OS/2"].sCapHeight * scale

cx = ring_outer_d / 2
baseline = ring_outer_d / 2 + x_height / 2     # Ring-Mitte = Mitte der x-Höhe
x = ring_outer_d + gap
path_d = []; xmin = None; xmax = 0
for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
    name = order[info.codepoint]
    sp = SVGPathPen(gs)
    tp = TransformPen(sp, (scale, 0, 0, -scale, x + pos.x_offset * scale, baseline))
    gs[name].draw(tp)
    bp = BoundsPen(gs); gs[name].draw(TransformPen(bp, (scale, 0, 0, -scale, x + pos.x_offset * scale, baseline)))
    if bp.bounds:
        xmin = bp.bounds[0] if xmin is None else min(xmin, bp.bounds[0]); xmax = max(xmax, bp.bounds[2])
    path_d.append(sp.getCommands())
    x += pos.x_advance * scale + tracking
word_d = " ".join(path_d)
W = xmax                                        # rechte Kante der Wortmarke (ohne Nachlauf)
H = ring_outer_d

def r(v): return f"{v:.1f}"
def logo_svg(color, title, bg=None):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {r(W)} {r(H)}" role="img" aria-label="{title}">
  <title>{title}</title>
  <g fill="none" stroke="{color}" stroke-width="{r(stroke)}"><circle cx="{r(cx)}" cy="{r(H/2)}" r="{r(r_out)}"/><circle cx="{r(cx)}" cy="{r(H/2)}" r="{r(r_in)}"/></g>
  <path fill="{color}" d="{word_d}"/>
</svg>
'''
def mark_svg(color, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {r(H)} {r(H)}" role="img" aria-label="{title}">
  <title>{title}</title>
  <g fill="none" stroke="{color}" stroke-width="{r(stroke)}"><circle cx="{r(cx)}" cy="{r(H/2)}" r="{r(r_out)}"/><circle cx="{r(cx)}" cy="{r(H/2)}" r="{r(r_in)}"/></g>
</svg>
'''
def icon_svg():
    # Vorschlag: App-Icon / Favicon (Bildmarke in Weiß auf osmera-Blau)
    s = 1024.0; scl = 0.56 * s / H; off = (s - H * scl) / 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" role="img" aria-label="osmera App-Icon">
  <title>osmera App-Icon (Vorschlag)</title>
  <rect width="1024" height="1024" rx="228" fill="#0284c7"/>
  <g transform="translate({r(off)} {r(off)}) scale({r(scl)})" fill="none" stroke="#ffffff" stroke-width="{r(stroke)}"><circle cx="{r(cx)}" cy="{r(H/2)}" r="{r(r_out)}"/><circle cx="{r(cx)}" cy="{r(H/2)}" r="{r(r_in)}"/></g>
</svg>
'''

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logos")
files = {
  "osmera-logo-navy.svg": logo_svg("#0f172a", "osmera Logo, Navy"),
  "osmera-logo-weiss.svg": logo_svg("#ffffff", "osmera Logo, Weiß"),
  "osmera-logo-schwarz.svg": logo_svg("#000000", "osmera Logo, Schwarz"),
  "osmera-logo-blau.svg": logo_svg("#0284c7", "osmera Logo, osmera-Blau"),
  "osmera-marke-navy.svg": mark_svg("#0f172a", "osmera Bildmarke, Navy"),
  "osmera-marke-weiss.svg": mark_svg("#ffffff", "osmera Bildmarke, Weiß"),
  "osmera-marke-blau.svg": mark_svg("#0284c7", "osmera Bildmarke, osmera-Blau"),
  "osmera-app-icon.svg": icon_svg(),
}
for n, c in files.items():
    open(os.path.join(out, n), "w", encoding="utf-8").write(c)
geo = dict(viewBox=[round(W, 1), round(H, 1)], ring_outer_d=round(ring_outer_d, 1), stroke=round(stroke, 1), r_out=round(r_out, 1), r_in=round(r_in, 1),
           gap=round(gap, 1), x_height=round(x_height, 1), cap_height=round(cap, 1), tracking_em=-0.025, font="Urbanist Bold 700", wordmark_x0=round(ring_outer_d + gap, 1), width_over_height=round(W / H, 3))
json.dump(geo, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo-geometrie.json"), "w"), indent=1)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "wordmark-path.txt"), "w").write(word_d)
print(json.dumps(geo)); print("Dateien:", ", ".join(files))
