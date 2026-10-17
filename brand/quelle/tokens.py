"""Design-Tokens der Marke osmera (Quelle: Website index.html, Tailwind-Konfiguration und Klassen, Stand 17.10.2026).

Jeder Eintrag: Schlüssel, deutscher Name, HEX, Herkunft ("Bestand" = steht so auf der Website, "Empfehlung" = neu festgelegt),
Verwendung. Alle Zahlen (RGB, HSL, CMYK-Näherung, Kontrast) werden hier gerechnet.
"""
import colorsys
import json

# (key, name, hex, herkunft, verwendung, tailwind)
CORE = [
    ("blau", "osmera-Blau", "#0284c7", "Bestand", "Primärfarbe: Buttons, Eyebrows, Links, Marken-Akzent, Auswahlfarbe", "osmera.blue / sky-600"),
    ("blau-dunkel", "Blau dunkel", "#0369a1", "Bestand", "Hover von Buttons, Ende des Textverlaufs, Text in kleiner Größe auf Hell", "sky-700"),
    ("himmel", "Himmelblau", "#38bdf8", "Bestand", "Akzent auf Dunkel (Eyebrows, Hover, Glow), Netz-Animation", "osmera.accent / sky-400"),
    ("blau-hell", "Blau hell", "#e0f2fe", "Bestand", "Flächen-Tönung, Marken-Hellblau", "osmera.bluelight / sky-100"),
    ("blau-ton", "Blau-Ton", "#eff6ff", "Bestand", "Icon-Kacheln (Hintergrund)", "blue-50"),
    ("blau-rand", "Blau-Rand", "#dbeafe", "Bestand", "Rand von Icon-Kacheln", "blue-100"),
]
NEUTRAL = [
    ("navy", "Navy", "#0f172a", "Bestand", "Überschriften, dunkle Abschnitte, Footer-Band, Logo", "osmera.dark / slate-900"),
    ("nacht", "Nacht", "#020617", "Bestand", "tiefster Ton (in der Tailwind-Konfiguration definiert)", "osmera.darker / slate-950"),
    ("text", "Text", "#1e293b", "Bestand", "Fließtext (Seiten-Standard)", "slate-800"),
    ("text-2", "Text sekundär", "#475569", "Bestand", "Absätze, Beschreibungen", "slate-600"),
    ("text-3", "Text gedämpft", "#64748b", "Bestand", "Hinweise, kleine Beschriftung", "slate-500"),
    ("linie", "Linie", "#e2e8f0", "Bestand", "Trennlinien, Ränder", "slate-200"),
    ("flaeche", "Fläche", "#f1f5f9", "Bestand", "Chips, Hintergründe kleiner Elemente", "slate-100"),
    ("grund", "Grund", "#f8fafc", "Bestand", "Seitenhintergrund", "osmera.light / slate-50"),
    ("weiss", "Weiß", "#ffffff", "Bestand", "Karten, Glasflächen, Text auf Dunkel", "white"),
]
ONDARK = [
    ("auf-dunkel", "Text auf Dunkel", "#cbd5e1", "Bestand", "Fließtext auf Navy", "slate-300"),
    ("auf-dunkel-2", "Text auf Dunkel gedämpft", "#94a3b8", "Bestand", "Hinweise auf Navy", "slate-400"),
]
FUNCTION = [
    ("haken", "Haken-Grün", "#22c55e", "Bestand", "Häkchen in Listen (check), Status-Punkt \"Lösung gefunden\"", "green-500"),
    ("meldung", "Meldung-Rot", "#ef4444", "Bestand", "Status \"Ausfall gemeldet\" in der Hero-Kachel (Symbol und Punkt), nie für Fließtext", "red-500"),
    ("meldung-ton", "Meldung-Ton", "#fee2e2", "Bestand", "Hintergrund des Meldungs-Symbols", "red-100"),
]
ROLES = [
    ("rolle-planende", "Planende", "#0284c7", "#e0f2fe", "Bestand/Empfehlung", "Rolle 1, Symbol users-gear"),
    ("rolle-team", "Das Team", "#9333ea", "#f3e8ff", "Bestand/Empfehlung", "Rolle 2, Symbol user-nurse"),
    ("rolle-prmav", "PR / MAV", "#059669", "#d1fae5", "Bestand/Empfehlung", "Rolle 3, Symbol handshake-angle"),
    ("rolle-hrit", "HR & IT", "#475569", "#e2e8f0", "Bestand/Empfehlung", "Rolle 4, Symbol server"),
    ("rolle-leitung", "Leitung & DSB", "#d97706", "#fef3c7", "Bestand/Empfehlung", "Rolle 5, Symbol building"),
]
WARM = [
    ("orange", "Orange", "#ff6531", "Bestand", "nur als sehr leichter Hintergrund-Schimmer (Deckkraft unter 10 %), nie für Text oder Buttons", "Hintergrund Ihr Mehrwert"),
    ("koralle", "Koralle", "#ff9892", "Empfehlung", "weicher warmer Akzent für Hintergründe in Print und Folien (Deckkraft unter 35 %)", "alternative Wärme"),
    ("pfirsich", "Pfirsich", "#ff9989", "Empfehlung", "wie Koralle, etwas wärmer", "alternative Wärme"),
]


def rgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(h):
    def f(c):
        c /= 255; return c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    r, g, b = rgb(h); return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)


def contrast(a, b):
    la, lb = lum(a), lum(b); hi, lo = max(la, lb), min(la, lb); return (hi + .05) / (lo + .05)


def cmyk(h):
    r, g, b = [c / 255 for c in rgb(h)]
    k = 1 - max(r, g, b)
    if k >= 1: return (0, 0, 0, 100)
    c = (1 - r - k) / (1 - k); m = (1 - g - k) / (1 - k); y = (1 - b - k) / (1 - k)
    return tuple(round(v * 100) for v in (c, m, y, k))


def hsl(h):
    r, g, b = [c / 255 for c in rgb(h)]; hh, l, s = colorsys.rgb_to_hls(r, g, b)
    return (round(hh * 360), round(s * 100), round(l * 100))


def detail(h):
    return dict(hex=h.upper(), rgb=rgb(h), hsl=hsl(h), cmyk_naeherung=cmyk(h))


# Kontrast-Paare (Text, Hintergrund, Verwendung)
PAIRS = [
    ("#0f172a", "#f8fafc", "Überschrift Navy auf Grund"),
    ("#1e293b", "#ffffff", "Fließtext auf Weiß"),
    ("#475569", "#ffffff", "Absatz sekundär auf Weiß"),
    ("#64748b", "#ffffff", "Hinweis gedämpft auf Weiß"),
    ("#0284c7", "#ffffff", "osmera-Blau auf Weiß (Eyebrow, Link)"),
    ("#0369a1", "#ffffff", "Blau dunkel auf Weiß"),
    ("#ffffff", "#0284c7", "Weißer Text auf osmera-Blau (Button)"),
    ("#ffffff", "#0369a1", "Weißer Text auf Blau dunkel (Button hover)"),
    ("#38bdf8", "#0f172a", "Himmelblau auf Navy (Eyebrow dunkel)"),
    ("#cbd5e1", "#0f172a", "Text auf Dunkel"),
    ("#94a3b8", "#0f172a", "Hinweis auf Dunkel"),
    ("#22c55e", "#ffffff", "Haken-Grün auf Weiß (nur Symbol)"),
]


def build():
    out = dict(
        meta=dict(name="osmera Design-Tokens", version="1.0", stand="2026-10-17", quelle="Website index.html (Tailwind-Konfiguration und Klassen)",
                  hinweis="CMYK-Werte sind rechnerische Näherungen aus sRGB. Für den Druck vom Druckdienstleister mit ICC-Profil (zum Beispiel PSO Coated v3) umrechnen und proofen lassen."),
        farben={}, rollen={}, kontrast=[])
    for grp, items in (("kern", CORE), ("neutral", NEUTRAL), ("auf-dunkel", ONDARK), ("funktion", FUNCTION), ("warm", WARM)):
        for key, name, hx, herk, use, tw in items:
            out["farben"][key] = dict(name=name, gruppe=grp, herkunft=herk, verwendung=use, tailwind=tw, **detail(hx))
    for key, name, hx, tint, herk, note in ROLES:
        out["rollen"][key] = dict(name=name, farbe=detail(hx), tonung=detail(tint), herkunft=herk, hinweis=note)
    for fg, bg, use in PAIRS:
        c = contrast(fg, bg)
        out["kontrast"].append(dict(vordergrund=fg, hintergrund=bg, verwendung=use, verhaeltnis=round(c, 2),
                                    normaler_text="AA" if c >= 4.5 else "nicht erfüllt", grosser_text="AA" if c >= 3 else "nicht erfüllt"))
    return out


if __name__ == "__main__":
    t = build()
    for k in t["kontrast"]:
        print(f'{k["verhaeltnis"]:5.2f}  Text {k["normaler_text"]:14s} | groß {k["grosser_text"]:14s} | {k["verwendung"]}')
    json.dump(t, open("tokens.json", "w"), ensure_ascii=False, indent=1)
    print("tokens.json", len(json.dumps(t)) // 1024, "KB")
