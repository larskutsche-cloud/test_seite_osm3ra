"""Seiten 1 bis 9 des Brand Guides: Titel, Inhalt, Marke, Logo, Farben, Typografie."""
import json
from pathlib import Path

HERE = Path(__file__).parent
T = json.loads((HERE / "tokens.json").read_text(encoding="utf-8"))
G = json.loads((HERE / "logo-geometrie.json").read_text(encoding="utf-8"))
WORD = (HERE / "wordmark-path.txt").read_text(encoding="utf-8")

B = '<span class="tag b">Bestand</span>'
E = '<span class="tag e">Empfehlung</span>'


def mono(s): return f"<code>{s}</code>"


def logo_g(color="#0f172a"):
    """Logo als <g> in Logo-Einheiten (ViewBox 0 0 W H) für Diagramme."""
    W, H = G["viewBox"]
    return (f'<g fill="none" stroke="{color}" stroke-width="{G["stroke"]}"><circle cx="{G["ring_outer_d"]/2}" cy="{H/2}" r="{G["r_out"]}"/>'
            f'<circle cx="{G["ring_outer_d"]/2}" cy="{H/2}" r="{G["r_in"]}"/></g><path fill="{color}" d="{WORD}"/>')


def sw(key, show_use=True):
    c = T["farben"][key]
    dark = sum(c["rgb"]) < 380
    txt = "#fff" if dark else "#0f172a"
    border = "box-shadow:inset 0 -1px 0 rgb(15 23 42 / .08);" if c["hex"] in ("#FFFFFF", "#F8FAFC", "#F1F5F9", "#E0F2FE", "#EFF6FF") else ""
    r, g, b = c["rgb"]; cm = c["cmyk_naeherung"]
    use = f'<span class="u">{c["verwendung"]}</span>' if show_use else ""
    return (f'<div class="sw"><div class="c" style="background:{c["hex"]};color:{txt};{border}">{c["hex"]}</div>'
            f'<div class="m"><b>{c["name"]} <span class="tag {"b" if c["herkunft"]=="Bestand" else "e"}">{c["herkunft"]}</span></b>'
            f'RGB {r} {g} {b}<br>CMYK≈ {cm[0]} {cm[1]} {cm[2]} {cm[3]}<br><code>--osm-{key}</code>{use}</div></div>')


def head(n, dark=False):
    src = "logos/osmera-logo-weiss.svg" if dark else "logos/osmera-logo-navy.svg"
    return f'<div class="pg-head"><img src="{src}" alt="osmera"><span>Brand Guide · Version 1.0 · Seite {n}</span></div>'


def title(k, h, p=""):
    return f'<div class="pg-title"><span class="k">{k}</span><h2>{h}</h2>{("<p>" + p + "</p>") if p else ""}</div>'


# ------------------------------------------------------------------ 1 Titel
def p_titel(n):
    return f'''<section class="pg osm-aurora osm-aurora--leicht" id="s{n}" style="display:flex;flex-direction:column;justify-content:space-between;min-height:794px">
  <div class="pg-head" style="margin:0"><span></span><span>Version 1.0 · verbindlich ab 17. Oktober 2026</span></div>
  <div>
    <img src="logos/osmera-logo-navy.svg" alt="osmera" style="height:92px;display:block;margin-bottom:56px">
    <span class="osm-eyebrow">Brand Guide</span>
    <h1 class="osm-h1" style="font-size:64px;max-width:14ch">Das Erscheinungsbild von <span class="osm-gradient-text">osmera.</span></h1>
    <p class="osm-lead" style="margin-top:20px;max-width:56ch;font-size:20px">Logo, Farben, Schrift, Bausteine und Anwendungen für Web, Print, PDF und Präsentationen. Abgeleitet aus der Website und deren Abschnitt „Ihr Mehrwert“.</p>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap">
    <div class="small" style="max-width:60ch">Der Guide unterscheidet {B} (so auf der Website umgesetzt) und {E} (neu festgelegt für Print, Folien und Dokumente).</div>
    <div class="small">osmera · Kutsche Köhl GbR · kontakt@osmera.de</div>
  </div>
</section>'''


# ------------------------------------------------------------------ 2 Inhalt
def p_inhalt(n, toc):
    items = "".join(f'<a href="#s{pn}">{t}<span>{pn}</span></a>' for t, pn in toc)
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Übersicht", "Inhalt und Aufbau")}
  <div class="g2" style="grid-template-columns:1.1fr 1fr;gap:34px">
    <div class="toc" style="columns:1">{items}</div>
    <div>
      <h3>So lesen Sie diesen Guide</h3>
      <p>{B} Dieser Wert steht genau so auf der Website (Code oder Konfiguration geprüft, Stand 17.10.2026).</p>
      <p>{E} Dieser Wert ist neu festgelegt, weil die Website ihn nicht braucht (zum Beispiel Mindestgrößen des Logos, Print-Maße, Folien).</p>
      <h3 style="margin-top:16px">Dateien im Paket</h3>
      <table class="t">
        <tr><td>{mono("osmera-brand.css")}</td><td>Tokens und Bausteine (Präfix <code>.osm-</code>)</td></tr>
        <tr><td>{mono("osmera-tokens.json")}</td><td>Farben mit HEX, RGB, CMYK≈, Kontrast</td></tr>
        <tr><td>{mono("logos/")}</td><td>8 Vektor-Dateien (SVG, Schrift in Pfade umgewandelt)</td></tr>
        <tr><td>{mono("…guide.html / .pdf")}</td><td>Dieser Guide (Browser, PDF A4 quer)</td></tr>
      </table>
      <h3 style="margin-top:16px">Geltung</h3>
      <p>Dieser Guide ist ab dem 17.10.2026 die <b>verbindliche Grundlage</b> für alle neuen osmera-Unterlagen und Oberflächen (Website, Print, PDF, Präsentationen, Dokumente). Er löst das ältere „Osmera Design System“ (Juni 2026: Insignia, Rubik, #071E3D, Cyan #00F0D4) ab. Bei Widerspruch gilt dieser Guide. Bestehende Unterlagen im alten Stil (zum Beispiel das Pitch Deck 09/2026) bei der nächsten Überarbeitung auf diesen Guide umstellen.</p>
      <h3 style="margin-top:16px">Wichtig vor dem Druck</h3>
      <p>CMYK-Werte in diesem Guide sind <b>rechnerische Näherungen</b> aus den Bildschirmfarben. Die Druckerei konvertiert mit ICC-Profil (zum Beispiel PSO Coated v3) und liefert einen Proof. Sonderfarben (Pantone) sind nicht festgelegt.</p>
    </div>
  </div>
</section>'''


# ------------------------------------------------------------------ 3 Marke
def p_marke(n):
    rollen = [("fa-solid fa-users-gear", "Planende", 1), ("fa-solid fa-user-nurse", "Das Team", 2), ("fa-solid fa-handshake-angle", "PR / MAV", 3), ("fa-solid fa-server", "HR &amp; IT", 4), ("fa-regular fa-building", "Leitung &amp; DSB", 5)]
    chips = "".join(f'<span class="osm-chip osm-rolle-{i}"><span class="osm-icon osm-icon--klein osm-icon--rolle" style="width:1.8rem;height:1.8rem;font-size:.8rem"><i class="{ic}"></i></span>{t}</span>' for ic, t, i in rollen)
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Marke", "Wofür osmera steht", "osmera ist das Add-on für bestehende Dienstplanprogramme in Kliniken. Es plant und organisiert den Ausfall, ohne das vorhandene System zu ersetzen.")}
  <div class="g3">
    <div class="box"><h3>Versprechen {B}</h3>
      <ul class="pl"><li><b>Ein Upgrade. Ohne Systemwechsel.</b> Das Dienstplanprogramm bleibt die einzige offizielle Quelle.</li>
      <li><b>Datenschutz als Fundament.</b> In jeder Schicht verankert, Zero-Knowledge-Ansatz.</li>
      <li><b>Kontrolle bleibt beim Menschen.</b> osmera schlägt vor, Planende entscheiden. Die Mitbestimmung wird nicht umgangen, sondern gefördert.</li></ul></div>
    <div class="box"><h3>Zielgruppe {B}</h3>
      <p>Kliniken, vor allem deutsche Krankenhäuser. Angesprochen werden fünf Rollen mit eigener Perspektive:</p>
      <div style="display:flex;flex-wrap:wrap;gap:6px">{chips}</div></div>
    <div class="box"><h3>Tonalität {E}</h3>
      <ul class="pl"><li>Ansprache in der Sie-Form, sachlich, ruhig, konkret.</li>
      <li>Geschlechtergerecht und einfach: „Mitarbeitende“, „Kolleginnen und Kollegen“.</li>
      <li>Keine erfundenen Zahlen, Zitate oder Referenzkunden. Nur belegbare Aussagen.</li>
      <li>Telefonieren wird nicht als Vorteil dargestellt. osmera macht Anrufe unnötig (Anfrage per App, Messenger oder SMS).</li></ul></div>
  </div>
  <div class="g2 mt" style="grid-template-columns:1.2fr 1fr">
    <div class="box flat"><h3>Kernaussagen der Website {B}</h3>
      <table class="t">
        <tr><td><b>Intelligente Dienstplanung.</b> <span class="osm-gradient-text" style="font-weight:800">Verbunden mit Ihrem System.</span></td><td><small>Startseite (H1)</small></td></tr>
        <tr><td><b>Ein Upgrade. Ohne Systemwechsel.</b></td><td><small>Die Lösung</small></td></tr>
        <tr><td><b>Ein Werkzeug, vielfacher Nutzen.</b></td><td><small>Ihr Mehrwert</small></td></tr>
        <tr><td><b>Modular erweiterbar. Wächst mit Ihren Anforderungen.</b></td><td><small>Die Plattform</small></td></tr>
        <tr><td><b>Datenschutz als Fundament. In jeder Schicht verankert.</b></td><td><small>Sicherheit</small></td></tr>
        <tr><td><b>Gemeinsam Ergebnisse sichtbar machen.</b> · <b>So einfach starten wir</b></td><td><small>Pilotprojekt</small></td></tr>
      </table></div>
    <div class="box flat"><h3>Beschreibung (Footer) {B}</h3>
      <p style="font-size:14px;color:var(--osm-navy);font-weight:600">„Intelligente Dienstplanung und Ausfallmanagement für Kliniken. Die nahtlose Erweiterung für Ihr bestehendes Dienstplanprogramm.“</p>
      <h3 style="margin-top:12px">Seitentitel {B}</h3>
      <p style="margin:0">osmera | Intelligente Dienstplanung per Add-on</p>
      <h3 style="margin-top:12px">Betreiber</h3>
      <p style="margin:0">Kutsche Köhl GbR, Zeithstraße 26, 53721 Siegburg · kontakt@osmera.de</p></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 4 Logo: Aufbau und Varianten
def p_logo1(n):
    Wv, Hv = G["viewBox"]; pad = 360; padr = 1760
    vb = f"{-pad} {-pad - 140} {Wv + pad + padr} {Hv + 2*pad + 140}"
    anat = f'''<svg viewBox="{vb}" style="width:100%;height:auto;max-height:240px;display:block" font-family="Inter, sans-serif">
  {logo_g()}
  <g stroke="#0284c7" stroke-width="9" fill="none" stroke-dasharray="26 18"><line x1="{-pad+60}" y1="{Hv/2}" x2="{Wv+60}" y2="{Hv/2}"/></g>
  <g fill="#0284c7" font-size="86" font-weight="600"><text x="{Wv+110}" y="{Hv/2-12}">Mittellinie:</text><text x="{Wv+110}" y="{Hv/2+88}">Ringmitte =</text><text x="{Wv+110}" y="{Hv/2+188}">Mitte der x-Höhe</text></g>
  <g stroke="#0284c7" stroke-width="8" fill="none">
    <line x1="0" y1="{-110}" x2="{G["ring_outer_d"]}" y2="{-110}"/><line x1="0" y1="{-150}" x2="0" y2="{-70}"/><line x1="{G["ring_outer_d"]}" y1="{-150}" x2="{G["ring_outer_d"]}" y2="{-70}"/>
    <line x1="{G["ring_outer_d"]}" y1="{-110}" x2="{G["wordmark_x0"]}" y2="{-110}" stroke="#ff6531"/><line x1="{G["wordmark_x0"]}" y1="{-150}" x2="{G["wordmark_x0"]}" y2="{-70}" stroke="#ff6531"/>
  </g>
  <g font-size="84" font-weight="700" text-anchor="middle">
    <text x="{G["ring_outer_d"]/2 - 130}" y="{-185}" fill="#0284c7">Ring ⌀ 28</text>
    <text x="{(G["ring_outer_d"]+G["wordmark_x0"])/2 + 420}" y="{-185}" fill="#ff6531">Abstand 10</text>
  </g>
  <g font-size="76" font-weight="600" fill="#475569"><text x="-60" y="{Hv+230}">Ring: Rand 2, innen ⌀ 20 (Rand 2), konzentrisch</text><text x="{G["wordmark_x0"]+800}" y="{Hv+230}">Urbanist Bold, 27,2 · Laufweite −0,025 em</text></g>
</svg>'''
    var = lambda src, bg, cap, extra="": (f'<div class="demo" style="background:{bg};display:grid;place-items:center;height:92px;{extra}"><img src="logos/{src}" style="{ "width:100%;max-width:150px;height:auto" if "marke" not in src and "icon" not in src else "height:46px;width:46px" }" alt=""></div><span class="cap">{cap}</span>')
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Logo", "Aufbau und Varianten", "Das Logo besteht aus der Bildmarke (zwei konzentrische Ringe) und der Wortmarke „osmera“ in Urbanist Bold. Die Schrift ist in den Dateien in Pfade umgewandelt, es muss keine Schrift installiert sein.")}
  <div class="box" style="padding:10px 18px">{anat}</div>
  <p class="small mt-s">Maße {B} aus der Navigation der Website (in px bei Schriftgröße 27,2 px). Die Ringfarbe ist auf der Website derzeit Schiefer #1E293B (erbt die Seitenfarbe), die Wortmarke Navy #0F172A. Der Guide legt für beide <b>Navy #0F172A</b> fest {E}.</p>
  <div class="g6 mt" style="grid-template-columns:repeat(6,minmax(0,1fr))">
    <div>{var("osmera-logo-navy.svg", "#fff", "Navy auf Hell (Standard)")}</div>
    <div>{var("osmera-logo-weiss.svg", "#0f172a", "Weiß auf Dunkel")}</div>
    <div>{var("osmera-logo-schwarz.svg", "#fff", "Schwarz, einfarbiger Druck")}</div>
    <div>{var("osmera-logo-blau.svg", "#fff", "osmera-Blau, sparsam")}</div>
    <div>{var("osmera-marke-navy.svg", "#fff", "Bildmarke allein")}</div>
    <div>{var("osmera-app-icon.svg", "#e8edf4", "App-Icon / Favicon " + E, "")}</div>
  </div>
</section>'''


# ------------------------------------------------------------------ 5 Logo: Schutzzone, Anordnung, Fehler
def p_logo2(n):
    Wv, Hv = G["viewBox"]; x = Hv / 2   # Schutzzone = Ringradius
    cz = f'''<svg viewBox="{-x-200} {-x-200} {Wv+2*x+400} {Hv+2*x+400}" style="width:100%;height:auto;display:block">
  <rect x="{-x}" y="{-x}" width="{Wv+2*x}" height="{Hv+2*x}" fill="rgb(2 132 199 / .08)" stroke="#0284c7" stroke-width="8" stroke-dasharray="30 20"/>
  <rect x="0" y="0" width="{Wv}" height="{Hv}" fill="#fff" stroke="#cbd5e1" stroke-width="6"/>
  {logo_g()}
  <g fill="#0284c7"><rect x="{-x}" y="{-x}" width="{x}" height="{x}" opacity=".35"/><rect x="{Wv}" y="{Hv}" width="{x}" height="{x}" opacity=".35"/>
  <text x="{-x/2}" y="{-x/2+28}" font-size="84" font-weight="800" text-anchor="middle" font-family="Inter">x</text><text x="{Wv+x/2}" y="{Hv+x/2+28}" font-size="84" font-weight="800" text-anchor="middle" font-family="Inter">x</text></g>
</svg>'''
    bad = lambda cap, inner: f'<div><div class="demo dont" style="height:76px;display:grid;place-items:center;overflow:hidden;background:#fff">{inner}</div><span class="cap">{cap}</span></div>'
    L = '<img src="logos/osmera-logo-navy.svg" style="height:26px" alt="">'
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Logo", "Schutzzone, Mindestgröße, Anordnung")}
  <div class="g3" style="grid-template-columns:1.05fr 1fr 1fr;align-items:start">
    <div class="box"><h3>Schutzzone {E}</h3>{cz}<p class="small" style="margin:6px 0 0">Rundum frei bleibt <b>x = Ringradius</b> (halbe Ringhöhe). Weder Text noch Bildkanten ragen hinein.</p></div>
    <div class="box"><h3>Mindestgröße {E}</h3>
      <table class="t"><tr><th>Variante</th><th>Bildschirm</th><th>Druck</th></tr>
      <tr><td>Logo (Bild + Wort)</td><td>96 px breit</td><td>25 mm breit</td></tr>
      <tr><td>Bildmarke allein</td><td>16 px</td><td>5 mm</td></tr>
      <tr><td>App-Icon</td><td>32 px (Favicon 16 px)</td><td>–</td></tr></table>
      <h3 style="margin-top:12px">Farbwahl {E}</h3>
      <ul class="pl"><li>Auf Hell und Weiß: Navy (Standard).</li><li>Auf Navy, Foto-Overlay, osmera-Blau: Weiß.</li><li>Einfarbiger Druck, Stempel, Fax: Schwarz.</li><li>Blaue Version nur sparsam, zum Beispiel Titel auf Weiß.</li></ul></div>
    <div class="box"><h3>Anordnung {B}/{E}</h3>
      <ul class="pl"><li><b>Web:</b> Logo links in der Navigation (Glas-Pille), im Footer links oberhalb der Beschreibung.</li><li><b>Seiten und Folien:</b> oben links, an der Satzspiegel-Kante, nie zentriert über dem Titel.</li><li><b>Logo und Claim:</b> Claim in Inter Medium, darunter, linksbündig zum Ring.</li><li><b>Produktnamen</b> („osmera flow“) werden als Text in Urbanist Bold gesetzt, ohne Ring.</li></ul>
      <div class="demo" style="margin-top:8px;padding:12px"><div class="osm-logo-claim"><img src="logos/osmera-logo-navy.svg" style="height:26px;display:block" alt=""><span>Intelligente Dienstplanung per Add-on</span></div></div></div>
  </div>
  <h3 class="mt">Fehlanwendungen {E}</h3>
  <div class="g6" style="grid-template-columns:repeat(6,minmax(0,1fr))">
    {bad("nicht strecken", f'<div style="transform:scaleX(1.22)">{L}</div>')}
    {bad("nicht umfärben", '<img src="logos/osmera-logo-navy.svg" style="height:26px;filter:hue-rotate(120deg) saturate(8)" alt="">')}
    {bad("keine Effekte", '<img src="logos/osmera-logo-navy.svg" style="height:26px;filter:drop-shadow(3px 3px 2px #f97316)" alt="">')}
    {bad("nicht drehen", f'<div style="transform:rotate(-12deg)">{L}</div>')}
    {bad("keine andere Schrift", '<span style="display:inline-flex;align-items:center;gap:6px"><img src="logos/osmera-marke-navy.svg" style="height:26px" alt=""><span style="font:700 25px Georgia,serif;color:#0f172a">osmera</span></span>')}
    {bad("nicht auf unruhigem Grund", '<div style="width:100%;height:100%;display:grid;place-items:center;background:linear-gradient(90deg,#38bdf8,#0284c7,#0f172a)"><img src="logos/osmera-logo-navy.svg" style="height:26px" alt=""></div>')}
  </div>
</section>'''


# ------------------------------------------------------------------ 6 Farben
def p_farben(n):
    kern = "".join(sw(k, True) for k in ("blau", "blau-dunkel", "himmel", "blau-hell"))
    neutral = "".join(sw(k, True) for k in ("navy", "text", "text-2", "text-3", "linie", "grund"))
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Farben", "Primärpalette und Neutraltöne", "Die Seite ist hell. osmera-Blau ist die einzige Aktionsfarbe, Navy trägt Überschriften und die dunklen Abschnitte. Alle Werte stammen aus der Tailwind-Konfiguration und den Klassen der Website.")}
  <h3>Marke</h3>
  <div class="g4">{kern}</div>
  <h3 class="mt">Neutral</h3>
  <div class="g6" style="grid-template-columns:repeat(6,minmax(0,1fr))">{neutral}</div>
  <p class="small mt-s">CMYK≈ sind rechnerische Näherungen. Für den Druck ICC-Konvertierung und Proof durch die Druckerei, keine Pantone-Zuordnung festgelegt. Tailwind-Namen: osmera.blue = sky-600, osmera.accent = sky-400, osmera.dark = slate-900, osmera.light = slate-50.</p>
</section>'''


# ------------------------------------------------------------------ 7 Farben II: Rollen, Warm, Status
def p_farben2(n):
    roles = "".join(
        f'<div class="sw"><div class="c" style="background:{v["farbe"]["hex"]};color:#fff">{v["farbe"]["hex"]}</div><div class="m" style="background:{v["tonung"]["hex"]}"><b>{v["name"]}</b>Tönung <code>{v["tonung"]["hex"]}</code><br>CMYK≈ {" ".join(str(x) for x in v["farbe"]["cmyk_naeherung"])}</div></div>'
        for v in T["rollen"].values())
    warm = "".join(sw(k, True) for k in ("orange", "koralle", "pfirsich"))
    status = "".join(sw(k, False) for k in ("meldung", "meldung-ton", "haken"))
    dunkel = "".join(sw(k, False) for k in ("auf-dunkel", "auf-dunkel-2"))
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Farben", "Rollen-, Warm- und Statusfarben", "Sie ergänzen die Primärpalette, sind aber an feste Aufgaben gebunden.")}
  <h3>Rollenfarben (Ihr Mehrwert) {B}</h3>
  <div class="g5" style="grid-template-columns:repeat(5,minmax(0,1fr))">{roles}</div>
  <div class="g2 mt-s" style="grid-template-columns:1.1fr 1.3fr;align-items:start">
    <div><h3>Warm: nur als Schimmer</h3><div class="g3" style="grid-template-columns:repeat(3,minmax(0,1fr))">{warm}</div></div>
    <div><h3>Status und Text auf Dunkel</h3><div class="g5" style="grid-template-columns:repeat(5,minmax(0,1fr))">{status}{dunkel}</div></div>
  </div>
  <div class="g3 mt-s">
    <div class="box flat"><h3>Weiß und Glas {B}</h3><p class="small" style="margin:0">Karten Weiß; Glas weiß 40 % (normal), 82 % (über Fotos), Navy 60 % (dunkel), Weichzeichner 20 px, Rand weiß 50 %.</p></div>
    <div class="box flat"><h3>Verlauf für Text {B}</h3><p style="margin:0;font-size:20px;font-weight:800" class="osm-gradient-text">Verbunden mit Ihrem System.</p><small>135° von #0284C7 nach #0369A1 (<code>.osm-gradient-text</code>)</small></div>
    <div class="box flat"><h3>Auf Dunkel {B}</h3><p class="small" style="margin:0">Text <code>#CBD5E1</code>, gedämpft <code>#94A3B8</code>, Akzent <code>#38BDF8</code>, Linie weiß 10 bis 15 %. Rolle und Status behalten ihre Farbe, nur ihre Tönung entfällt.</p></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 8 Farbkonzepte und Kontrast
def p_konzepte(n):
    rows = ""
    for k in T["kontrast"]:
        fg, bg = k["vordergrund"], k["hintergrund"]
        n_ok = k["normaler_text"] == "AA"; g_ok = k["grosser_text"] == "AA"
        rows += (f'<tr><td><span style="display:inline-block;min-width:44px;text-align:center;padding:2px 8px;border-radius:6px;background:{bg};color:{fg};font-weight:800;border:1px solid #e2e8f0">Aa</span></td>'
                 f'<td>{k["verwendung"]}</td><td><b>{k["verhaeltnis"]:.2f}:1</b></td><td><span class="tag {"ok" if n_ok else "no"}">{"AA" if n_ok else "unter 4,5"}</span></td><td><span class="tag {"ok" if g_ok else "no"}">{"AA" if g_ok else "unter 3"}</span></td></tr>')
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Farbkonzepte", "Wo welche Farbe wirkt, und ob der Kontrast reicht")}
  <div class="g4">
    <div class="box"><h3>1 · Hell und Glas {B}</h3><p class="small" style="margin:0">Standard. Grund <code>#F8FAFC</code>, weiße Karten, Glas, Text Navy und Schiefer, Aktionen in osmera-Blau.</p></div>
    <div class="box" style="background:var(--osm-navy);border-color:var(--osm-navy)"><h3 style="color:#fff">2 · Dunkel {B}</h3><p class="small" style="color:#cbd5e1;margin:0">Sicherheit und Foto-Band. Navy, dunkles Glas, Text <code>#CBD5E1</code>, Akzent Himmelblau <code>#38BDF8</code>.</p></div>
    <div class="box"><h3>3 · Rollenfarben {B}</h3><p class="small" style="margin:0">Nur dort, wo eine Rolle oder Zielgruppe unterschieden wird. Kein Dekor, nie für Buttons.</p></div>
    <div class="box"><h3>4 · Warmer Schimmer {B}</h3><p class="small" style="margin:0">Blau rechts, Orange links, sehr leicht (Orange unter 10 % Deckkraft). Nur Hintergrund, nie Text oder Schalter.</p></div>
  </div>
  <h3 class="mt">Kontrast nach WCAG 2.1 {E}</h3>
  <table class="t tight"><tr><th></th><th>Paar</th><th>Verhältnis</th><th>Normaler Text (4,5)</th><th>Großer Text (3)</th></tr>{rows}</table>
  <p class="small mt-s"><b>Hinweis:</b> Weißer Text auf osmera-Blau und osmera-Blau auf Weiß erreichen 4,10:1. Das genügt für große Schrift (ab 18,66 px fett), nicht für kleine. Für kleine Schrift und Buttons <b>Blau dunkel #0369A1</b> (5,93:1) verwenden {E}. Das Haken-Grün ist nur ein Zeichen neben Text, nie Träger einer Information.</p>
</section>'''


# ------------------------------------------------------------------ 8 Typografie 1
def p_typo1(n):
    weights = "".join(f'<tr><td style="width:90px"><b>Inter {w}</b></td><td style="font-weight:{w};font-size:17px;color:var(--osm-navy);line-height:1.2;white-space:nowrap">Intelligente Dienstplanung.</td><td><small>{u}</small></td></tr>'
                      for w, u in ((400, "Print-Fließtext"), (500, "Web-Fließtext, Lead"), (600, "Buttons, Hervorhebung"), (700, "Überschriften klein, Eyebrow"), (800, "Überschriften groß")))
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Typografie", "Zwei Schriften, eine klare Regel", "Inter setzt alles, was die Website sagt. Urbanist setzt nur osmera: das Logo, den Namen und alle osmera-Begriffe im Text.")}
  <div class="g2" style="grid-template-columns:1.2fr 1fr;align-items:start">
    <div class="box"><h3>Inter {B} <small>Schrift für Überschriften, Fließtext, Bedienelemente</small></h3>
      <div style="font-size:46px;font-weight:800;line-height:1;color:var(--osm-navy);letter-spacing:-.02em">Aa Gg 123</div>
      <table class="t tight mt-s">{weights}</table>
      <p class="small mt-s">Frei bei Google Fonts (SIL Open Font License). Auf der Website geladen: 300 bis 800.</p></div>
    <div>
      <div class="box"><h3>Urbanist {B} <small>nur osmera-Begriffe</small></h3>
        <div style="font-family:var(--osm-font-marke);font-size:44px;font-weight:700;line-height:1;color:var(--osm-navy);letter-spacing:-.025em">osmera</div>
        <p style="margin-top:10px;font-size:20px;font-family:var(--osm-font-marke);font-weight:700;color:var(--osm-navy);line-height:1.5">osmera flow · osmera sync<br>osmera bridge · osmera mapper</p>
        <p class="small">Logo und Produktnamen: Bold 700, Laufweite −0,025 em. Im Fließtext <span class="osm-marke">osmera</span>: Gewicht 550, Größe 1,09 em (<code>.osm-marke</code>, auf der Website <code>.font-logo</code>).</p></div>
      <div class="box mt-s" style="background:#fffbeb;border-color:#fde68a"><h3>Regel</h3>
        <p style="margin:0">Jedes „osmera“ im Text steht in Urbanist, nie in Inter. Der Rest des Satzes bleibt Inter. Überschriften, auch große, sind <b>immer Inter</b>.</p></div>
      <p class="small mt-s">Hinweis {E}: Die Website lädt zusätzlich „Outfit“, nutzt sie aber nirgends. Sie gehört nicht zur Marke und kann entfernt werden.</p></div>
  </div>
  <div class="demo mt" style="padding:18px 24px"><p style="margin:0;font-size:20px;line-height:1.5;color:var(--osm-text-2);font-weight:500;max-width:80ch">Ersatz benötigt? <span class="osm-marke" style="color:var(--osm-navy)">osmera</span> schlägt passende Kolleginnen und Kollegen vor, geprüft nach Verfügbarkeit und Qualifikation, und fragt sie bequem per Mitarbeitenden-App an.</p><span class="cap">Beispiel aus dem Abschnitt „Die Lösung“: „osmera“ in Urbanist, der Satz in Inter Medium.</span></div>
</section>'''


# ------------------------------------------------------------------ 9 Typografie 2: Hierarchie
def p_typo2(n):
    rows = [
        ("Display / H1", "48 px, ab 768 px 60 px · ExtraBold 800 · LH 1,2 · −0,025 em", "28 bis 36 pt · ExtraBold", "112 px = 56 pt", "font-size:26px;font-weight:800;letter-spacing:-.025em;line-height:1.1", "Intelligente Dienstplanung."),
        ("H2", "36 px · ExtraBold 800 · LH 1,25", "20 pt · ExtraBold", "80 px = 40 pt", "font-size:21px;font-weight:800;line-height:1.15", "Ein Werkzeug, vielfacher Nutzen."),
        ("H3 / Kartentitel groß", "30 px · Bold 700 (Module in Urbanist)", "14 pt · Bold", "52 px = 26 pt", "font-size:18px;font-weight:700", "Planende"),
        ("H4 / Kartentitel", "20 px · Bold 700", "11 pt · Bold", "44 px = 22 pt", "font-size:17px;font-weight:700", "Ihre Bridge"),
        ("Lead", "20 px · Medium 500 · Schiefer", "12 pt · Medium", "44 px = 22 pt", "font-size:16px;font-weight:500;color:#475569", "Einfach umgesetzt, im laufenden Betrieb."),
        ("Fließtext", "16 bis 18 px · Medium 500 · LH 1,65", "10 pt · Regular 400", "40 px = 20 pt", "font-size:14px;font-weight:500;color:#475569", "Sie behalten die volle Kontrolle."),
        ("Klein", "14 px · Medium 500", "8,5 pt", "32 px = 16 pt (Minimum)", "font-size:12px;font-weight:500;color:#475569", "Geprüft nach Verfügbarkeit und Qualifikation"),
        ("Eyebrow", "18 px · Bold · Versalien · +0,05 em · osmera-Blau", "9 pt", "32 px = 16 pt", "font-size:13px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#0284c7", "Ihr Mehrwert"),
        ("Badge", "10 px · Bold · Versalien · +0,05 em", "7 pt (Minimum)", "nicht auf Folien", "font-size:10px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#64748b", "Basis-Modul"),
    ]
    body = "".join(f'<tr><td><b>{a}</b></td><td class="nw"><span style="{st}">{ex}</span></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d, st, ex in rows)
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Typografie", "Schriftgrößen für Web, Print und Folien", "Web-Werte " + B + " stammen aus den Klassen der Website, Print- und Folienwerte " + E + " sind darauf abgestimmt (Folie 1920 × 1080 px: 1 px entspricht 0,5 pt).")}
  <table class="t tight"><tr><th>Rolle</th><th>Beispiel</th><th>Web (Bestand)</th><th>Print A4</th><th>Folie</th></tr>{body}</table>
  <div class="g3 mt">
    <div class="box"><h3>Satz {E}</h3><ul class="pl"><li>Zeilenlänge 60 bis 75 Zeichen, Fließtext linksbündig.</li><li>Überschriften in zentrierten Abschnitten mittig, sonst linksbündig.</li><li>Überschriften mit ausgewogenem Umbruch, Fließtext in Print mit Silbentrennung.</li></ul></div>
    <div class="box"><h3>Ersatzschriften {E}</h3><p class="small">Falls Inter fehlt: Segoe UI (Windows), SF Pro (macOS), Arial. Urbanist fehlt: Inter Bold. Im Web ist die Rückfallkette <code>Inter, system-ui, Arial, sans-serif</code>.</p></div>
    <div class="box"><h3>Zahlen und Zeichen {E}</h3><p class="small">Tausenderpunkt (1.500), Uhrzeit „14:30 Uhr“, Gedankenstrich mit Leerzeichen „ – “, deutsche Anführungszeichen „so“. Nie das Wort osmera großschreiben.</p></div>
  </div>
</section>'''
