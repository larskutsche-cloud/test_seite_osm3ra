"""Seiten 10 bis 21 des Brand Guides: Bezeichnungen, Bausteine, Symbole, Raster, Hintergründe, Bild, Print, Präsentation, PDF, Anhang."""
from guide_a import B, E, T, mono, head, title


def icon(cls, tone="osm-icon--klein", extra=""):
    return f'<span class="osm-icon {tone} {extra}"><i class="{cls}"></i></span>'


# ------------------------------------------------------------------ 10 Bezeichnungen
def p_namen(n):
    rows = [
        ("osmera", "immer klein, in Urbanist", "Name, Marke, Logo-Wort. Am Satzanfang bleibt es klein."),
        ("osmera flow", "Ausfallmanagement mit Co-Pilot", "Modul: zeigt bei einer Krankmeldung, wer einspringen kann, darf und am besten geeignet ist."),
        ("osmera sync", "Die intelligente Dienstplan-Berechnung", "Modul mit dem Zuteilungsalgorithmus <span class=\"osm-marke\">osmera core</span>."),
        ("osmera bridge", "Basis-Modul", "Kleines Programm im Klinik-Netz, trennt Klarnamen von Kennungen (anonyme Token)."),
        ("osmera mapper", "Basis-Modul", "Übersetzt den Export des Altsystems in das osmera-Format."),
        ("horizon · audit", "in Vorbereitung", "KI-Forecast und Controlling. Immer als „In Vorbereitung“ kennzeichnen."),
        ("Kurzform", "flow, Sync, bridge, mapper", "Nach der ersten Nennung ohne Präfix, in Urbanist. Am Satzanfang großgeschrieben („Sync erstellt …“)."),
    ]
    body = "".join(f'<tr><td class="nw"><b class="osm-marke osm-marke--titel" style="font-size:15px">{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Sprache", "Bezeichnungen und Schreibweisen", "Einheitliche Namen sind Teil der Marke. Die folgenden Begriffe stehen so auf der Website.")}
  <div class="g2" style="grid-template-columns:1.35fr 1fr;align-items:start">
    <div><table class="t"><tr><th>Name</th><th>Beiname</th><th>Bedeutung</th></tr>{body}</table></div>
    <div>
      <div class="box"><h3>Wörter {B}</h3>
        <table class="t"><tr><td><b>Add-on</b></td><td>groß, mit Bindestrich</td></tr><tr><td><b>Dienstplanprogramm</b></td><td>ein Wort; das System der Klinik</td></tr><tr><td><b>Pilotprojekt, Pilotkunde</b></td><td>ein Wort, groß</td></tr><tr><td><b>Mitarbeitende</b></td><td>statt „Mitarbeiter“</td></tr><tr><td><b>Zero-Knowledge</b></td><td>mit Bindestrich</td></tr></table></div>
      <div class="box mt-s"><h3>Rollen {B}</h3>
        <p class="small" style="margin:0">Planende · Das Team · PR / MAV · HR &amp; IT · Leitung &amp; DSB. Beim ersten Auftreten in Print und Folien ausschreiben {E}: Personalrat / Mitarbeitervertretung, Datenschutzbeauftragte.</p></div>
      <div class="box mt-s"><h3>Menü und Aktionen {B}</h3>
        <p class="small" style="margin:0">Die Lösung · Ihr Mehrwert · Die Plattform · Sicherheit · <b>Pilotprojekt</b> (Button).<br>Aktionen: <b>Pilotkunde werden</b> (primär), <b>Die Lösung verstehen</b> (Glas).</p></div>
    </div>
  </div>
  <div class="g3 mt">
    <div class="box do"><h3>So {E}</h3><p style="margin:0">„<span class="osm-marke">osmera</span> fragt passende Kolleginnen und Kollegen per App an. Sie entscheiden.“</p></div>
    <div class="box dont"><h3>Nicht so {E}</h3><p style="margin:0">„Wir rufen Ihre Mitarbeiter an.“ (Telefon als Vorteil, nicht gegendert, „osmera“ in Inter)</p></div>
    <div class="box flat"><h3>Überschriften-Muster {B}</h3><p style="margin:0">Zwei kurze Sätze mit Punkt: „Ein Upgrade. Ohne Systemwechsel.“ Eyebrow darüber nennt den Menü-Namen des Abschnitts.</p></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 11 Bausteine 1
def p_komp1(n):
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Bausteine", "Überschriften, Schalter, Listen", "Alle Beispiele sind mit osmera-brand.css gesetzt. Die Klassen stehen unter den Beispielen.")}
  <div class="g2" style="grid-template-columns:1.1fr 1fr;align-items:start">
    <div>
      <div class="demo" style="text-align:center;padding:14px"><span class="osm-eyebrow" style="font-size:15px;margin-bottom:2px">Die Lösung</span><div class="osm-h2" style="font-size:26px">Ein Upgrade. Ohne Systemwechsel.</div><div class="osm-lead" style="font-size:14px;margin-top:4px">Unsere vier Komponenten einer intelligenten Dienstplanung.</div></div>
      <span class="cap"><code>.osm-eyebrow</code> · <code>.osm-h2</code> · <code>.osm-lead</code> · Abschnittskopf zentriert, Eyebrow = Menü-Name {B}</span>
      <div class="demo mt" style="display:flex;gap:10px;flex-wrap:wrap;align-items:center"><a class="osm-btn osm-btn--primaer">Pilotkunde werden</a><a class="osm-btn osm-btn--glas">Die Lösung verstehen</a><a class="osm-btn osm-btn--primaer osm-btn--klein">Pilotprojekt</a></div>
      <span class="cap"><code>.osm-btn--primaer</code> · <code>.osm-btn--glas</code> · <code>.osm-btn--klein</code> (Navigation) {B}. Alle Formen sind Pillen (Radius voll).</span>
      <div class="demo dark mt" style="display:flex;gap:10px;flex-wrap:wrap;align-items:center"><a class="osm-btn osm-btn--hell">Pilotkunde werden</a><a class="osm-btn osm-btn--primaer osm-btn--primaer-aa">Kleine Schrift (AA)</a></div>
      <span class="cap"><code>.osm-btn--hell</code> auf dunklem Band {B}; <code>.osm-btn--primaer-aa</code> mit #0369A1 für kleine Schrift {E}.</span>
    </div>
    <div>
      <div class="demo" style="display:flex;gap:8px;flex-wrap:wrap;align-items:center"><span class="osm-chip osm-chip--aktiv osm-rolle-1">{icon("fa-solid fa-users-gear", "osm-icon--klein osm-icon--rolle", "")}Planende</span><span class="osm-chip osm-rolle-2">{icon("fa-solid fa-user-nurse", "osm-icon--klein osm-icon--rolle")}Das Team</span><span class="osm-badge">Basis-Modul</span><span class="osm-badge osm-badge--blau">In Vorbereitung</span></div>
      <span class="cap"><code>.osm-chip</code> · <code>.osm-chip--aktiv</code> · <code>.osm-badge</code> {B}</span>
      <div class="demo mt"><ul class="osm-haken"><li>Das Altsystem bleibt unabhängig und voll funktionsfähig</li><li>Keine gefährlichen Firewall-Öffnungen nach innen</li></ul></div>
      <span class="cap"><code>.osm-haken</code>: Häkchen in Haken-Grün, Text Schiefer {B}</span>
      <div class="demo mt" style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
        <span class="osm-icon"><i class="fa-solid fa-plug"></i></span><span class="osm-icon osm-icon--klein"><i class="fa-solid fa-lock"></i></span>
        <span class="osm-icon osm-icon--rolle osm-rolle-3"><i class="fa-solid fa-handshake-angle"></i></span><span class="osm-icon osm-icon--rolle osm-rolle-5"><i class="fa-regular fa-building"></i></span>
        <span class="osm-icon osm-icon--rolle osm-rolle-2"><i class="fa-solid fa-user-nurse"></i></span></div>
      <span class="cap"><code>.osm-icon</code> (Blau-Ton, 56 px), <code>--klein</code> (40 px), <code>--rolle</code> + <code>.osm-rolle-1 bis 5</code> {B}</span>
    </div>
  </div>
  <div class="g2 mt">
    <div class="box flat"><h3>Zustände {E}</h3><p class="small" style="margin:0">Hover: Button dunkler (#0369A1), Karte hebt sich 4 bis 8 px. Fokus: sichtbarer 2-px-Ring in osmera-Blau. Aktiv: weiße Fläche mit Schatten.</p></div>
    <div class="box flat"><h3>Abstände und Beschriftung {B}</h3><p class="small" style="margin:0">Überschrift zu Lead 16 px, Abschnittskopf zu Inhalt 40 px, Karten untereinander 24 px (Mehrwert: 56 px). Schalter sind Verben („Pilotkunde werden“), keine Ausrufezeichen, höchstens vier Wörter.</p></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 12 Bausteine 2: Karten
def p_komp2(n):
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Bausteine", "Karten", "Fünf Kartentypen decken die Website ab. Radius groß, Schatten weich, Kanten hell.")}
  <div class="g3" style="align-items:start">
    <div><div class="demo" style="padding:14px"><div class="osm-glas osm-karte--blau-oben" style="padding:18px;border-radius:16px;border-top:4px solid var(--osm-blau)">
      {icon("fa-solid fa-plug", "", "")}<div class="osm-h4" style="margin:10px 0 4px">Verbindung</div><p class="osm-small" style="margin:0">Ihr Dienstplanprogramm liefert die Daten so, wie sie ohnehin verarbeitet werden.</p></div></div>
      <span class="cap"><b>Lösungs-Karte</b> {B}: <code>.osm-glas</code> + blauer Rand oben 4 px, Radius 16 px.</span></div>
    <div><div class="demo" style="padding:14px"><div class="osm-karte osm-karte--blau-oben" style="padding:18px;box-shadow:var(--osm-shadow-xl)">
      <div style="display:flex;align-items:center;gap:10px"><span class="osm-icon"><i class="fa-regular fa-calendar-check"></i></span><span class="osm-marke osm-marke--titel" style="font-size:24px;color:var(--osm-navy)">osmera sync</span></div>
      <p style="margin:8px 0 0;font-weight:700;color:#1e293b">Die intelligente Dienstplan-Berechnung.</p><span class="osm-chip" style="margin-top:8px;font-size:12px">Mehr <i class="fa-solid fa-chevron-down" style="font-size:10px"></i></span></div></div>
      <span class="cap"><b>Modul-Karte</b> {B}: weiß, Titel in Urbanist Bold, „Mehr“-Chip klappt Text auf (Hover am Desktop, Tippen mobil).</span></div>
    <div><div class="demo" style="padding:14px"><div class="osm-karte osm-karte--rolle osm-rolle-2" style="padding:18px">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px"><span class="osm-icon osm-icon--rolle"><i class="fa-solid fa-user-nurse"></i></span><span class="osm-h3" style="font-size:22px">Das Team</span></div>
      <p class="osm-small" style="margin:0 0 8px">Den Dienstplan haben Sie auf Ihrem Smartphone jederzeit im Blick.</p><ul class="osm-haken" style="font-size:12px"><li>Entlastung durch partizipative Dienstplanung</li></ul></div></div>
      <span class="cap"><b>Rollenkarte</b> {B}: weiß, Rollenfarbe nur im Symbol und als zarte Ecke, <b>kein Farbbalken</b>.</span></div>
  </div>
  <div class="g3 mt" style="align-items:start">
    <div><div class="demo photo" style="position:relative;height:128px;background:url(../img/hero-zwei-personen-960.webp) 50% 30%/cover"><div class="osm-glas osm-glas--stark" style="position:absolute;left:14px;right:60px;bottom:14px;border-radius:16px;padding:10px 12px;display:flex;align-items:center;gap:10px">
      <span style="width:36px;height:36px;border-radius:99px;background:var(--osm-meldung-ton);color:var(--osm-meldung);display:grid;place-items:center"><i class="fa-solid fa-bell"></i></span><div><div style="font-weight:700;color:#1e293b;font-size:13px">Krankmeldung Station A</div><div style="font-size:11px;color:#64748b;font-weight:500">Frühschicht unbesetzt</div></div><span style="width:8px;height:8px;border-radius:99px;background:var(--osm-meldung);margin-left:auto"></span></div></div>
      <span class="cap"><b>Hero-Kachel</b> {B}: <code>.osm-glas--stark</code> über dem Foto, nie über Gesichtern.</span></div>
    <div><div class="demo dark" style="padding:14px"><div class="osm-glas--dunkel" style="border-radius:16px;padding:16px"><div style="display:flex;align-items:center;gap:10px;color:#fff;font-weight:700;font-size:16px"><i class="fa-solid fa-building-shield" style="color:var(--osm-himmel)"></i>Ihre Bridge</div><p style="margin:6px 0 0;font-size:12px;color:var(--osm-auf-dunkel-2)">Ein ressourcenschonendes Modul in Ihrem Netzwerk.</p></div></div>
      <span class="cap"><b>Dunkle Glas-Karte</b> {B}: <code>.osm-glas--dunkel</code>, Symbol in Himmelblau, Text #94A3B8.</span></div>
    <div><div class="demo" style="padding:10px;display:grid;gap:8px">
      <div class="osm-glas osm-rolle-1" style="border-radius:16px;padding:10px 12px;display:flex;align-items:center;gap:10px;background:#fff"><span class="osm-icon osm-icon--klein osm-icon--rolle"><i class="fa-solid fa-users-gear"></i></span><b style="flex:1;color:var(--osm-navy)">Planende</b><i class="fa-solid fa-chevron-up" style="color:#64748b;font-size:11px"></i></div>
      <div class="osm-glas osm-rolle-2" style="border-radius:16px;padding:10px 12px;display:flex;align-items:center;gap:10px"><span class="osm-icon osm-icon--klein osm-icon--rolle"><i class="fa-solid fa-user-nurse"></i></span><b style="flex:1;color:var(--osm-navy)">Das Team</b><i class="fa-solid fa-chevron-down" style="color:#64748b;font-size:11px"></i></div></div>
      <span class="cap"><b>Akkordeon (Handy)</b> {B}: eine Rolle offen, übrige als Zeile mit Symbol und Pfeil.</span></div>
  </div>
  <div class="g3 mt"><div class="box flat"><h3>Radien {B}</h3><p class="small" style="margin:0">Schalter, Chips, Navigation: voll (Pille). Foto-Rahmen, große Karten: 24 px. Karten: 16 px. Symbole, Listenpunkte: 12 px.</p></div>
    <div class="box flat"><h3>Schatten {B}</h3><p class="small" style="margin:0">Schalter md; Karten xl; hervorgehobene und Fotos 2xl (<code>0 25px 50px -12px</code> bei 25 %). Glas: 0 4px 6px bei 5 %.</p></div>
    <div class="box flat"><h3>Ränder {B}</h3><p class="small" style="margin:0">Karten 1 px weiß 50 bis 90 %. Auf Fotos Glas weiß 82 %. Dunkles Glas: Rand weiß 10 %. Blauer Oberrand 4 px nur bei Lösungs- und Modulkarten.</p></div></div>
</section>'''


# ------------------------------------------------------------------ 13 Symbole
ICONS = [
    ("fa-solid fa-users-gear", "users-gear", "Planende"), ("fa-solid fa-user-nurse", "user-nurse", "Das Team"), ("fa-solid fa-handshake-angle", "handshake-angle", "PR / MAV"),
    ("fa-solid fa-server", "server", "HR &amp; IT"), ("fa-regular fa-building", "building (regular)", "Leitung &amp; DSB"),
    ("fa-solid fa-mobile-screen-button", "mobile-screen-button", "osmera flow, „Anfrage per App“"), ("fa-regular fa-calendar-check", "calendar-check (regular)", "osmera sync"),
    ("fa-solid fa-lock", "lock", "osmera bridge"), ("fa-solid fa-right-left", "right-left", "osmera mapper"), ("fa-solid fa-rocket", "rocket", "In Vorbereitung"),
    ("fa-solid fa-plug", "plug", "Verbindung"), ("fa-solid fa-calculator", "calculator", "Optimierung"), ("fa-solid fa-file-export", "file-export", "Rückgabe"),
    ("fa-solid fa-paper-plane", "paper-plane", "Anfragen versenden"), ("fa-solid fa-building-shield", "building-shield", "Ihre Bridge (Sicherheit)"), ("fa-solid fa-cloud", "cloud", "Unser Server"),
    ("fa-solid fa-network-wired", "network-wired", "Dedizierte Infrastruktur"), ("fa-solid fa-bell", "bell", "Ausfall gemeldet (rot)"), ("fa-solid fa-check", "check", "Listenhaken (grün)"),
    ("fa-solid fa-chevron-down", "chevron-down", "Aufklappen, Mehr"), ("fa-regular fa-envelope", "envelope (regular)", "E-Mail"), ("fa-solid fa-bars", "bars", "Menü (mobil)"),
]


def p_icons(n):
    cells = "".join(f'<div class="box" style="display:flex;gap:8px;align-items:center;padding:7px 8px"><span class="osm-icon osm-icon--klein" style="flex:none"><i class="{c}"></i></span><div><b style="color:var(--osm-navy);font-size:12px">{t}</b><br><small>{u}</small></div></div>' for c, t, u in ICONS)
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Symbole", "Symbole und ihre Bedeutung", "Es gibt eine einzige Symbolfamilie: Font Awesome 6 Free (Version 6.4.0 auf der Website). Jedes Symbol hat eine feste Aufgabe, damit es nicht beliebig wird.")}
  <div class="g4" style="grid-template-columns:repeat(5,minmax(0,1fr));gap:7px">{cells}</div>
  <div class="g3 mt">
    <div class="box flat"><h3>Regeln {E}</h3><ul class="pl" style="margin:0"><li>Standard ist <b>solid</b>. <b>regular</b> nur bei building, calendar-check, envelope.</li><li>Ein Symbol steht für einen Begriff, nie dekorativ gestreut.</li><li>Neue Symbole nur aus derselben Familie und im selben Strichstil.</li></ul></div>
    <div class="box flat"><h3>Darstellung {B}</h3><ul class="pl" style="margin:0"><li>In getönter Kachel: 56 px (Karten), 40 px (klein), Radius 16 bzw. 12 px.</li><li>Farbe: osmera-Blau oder Rollenfarbe, auf Dunkel Himmelblau.</li><li>Haken grün, Meldung rot, sonst keine Zusatzfarben.</li></ul></div>
    <div class="box flat"><h3>Print und Folien {E}</h3><ul class="pl" style="margin:0"><li>Als SVG aus Font Awesome exportieren, nicht als Schrift einbetten.</li><li>Mindestgröße 6 mm bzw. 24 px, in Kacheln 12 mm.</li><li>Lizenz: Font Awesome Free (Icons CC BY 4.0), Namensnennung im Impressum oder Anhang.</li></ul></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 14 Raster und Form
def p_raster(n):
    spacing = [4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96]
    bars = "".join(f'<div class="bar-row"><span style="width:44px">{s}px</span><i style="width:{s*2}px"></i></div>' for s in spacing)
    rh = [("Hero", "#fff", "Foto + Kacheln"), ("Die Lösung", "rgb(255 255 255 / .5)", "Glas-Band"), ("Ihr Mehrwert", "linear-gradient(90deg,rgb(255 101 49 / .12),#fff 40%,rgb(56 189 248 / .2))", "Schimmer"), ("Die Plattform", "#fff", "hell"), ("Sicherheit", "#0f172a", "dunkel"), ("Pilotprojekt", "#fff", "hell"), ("Abschluss", "#0f172a", "Foto-Band + Footer")]
    strip = "".join(f'<div style="background:{b};color:{"#fff" if b=="#0f172a" else "#334155"}">{a}<br><span style="font-weight:500;opacity:.8">{c}</span></div>' for a, b, c in rh)
    shadows = "".join(f'<div style="text-align:center"><div style="height:46px;border-radius:12px;background:#fff;box-shadow:{s}"></div><small>{t}</small></div>' for t, s in (("md", "var(--osm-shadow-md)"), ("xl", "var(--osm-shadow-xl)"), ("2xl", "var(--osm-shadow-2xl)")))
    rad = "".join(f'<div style="text-align:center"><div style="height:46px;background:var(--osm-blau-hell);border:1px solid #bae6fd;border-radius:{r}"></div><small>{t}</small></div>' for t, r in (("Pille", "99px"), ("24 px", "24px"), ("16 px", "16px"), ("12 px", "12px")))
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Raster", "Raster, Abstände und Form", "Die Seite ist ein ruhiger Fluss aus Abschnitten. Immer gleiche Abstände, wenige Radien, weiche Schatten.")}
  <h3>Seitenrhythmus {B}</h3>
  <div class="rhythm">{strip}</div>
  <div class="g3 mt" style="align-items:start">
    <div class="box"><h3>Abstände {B}</h3>{bars}<p class="small" style="margin:6px 0 0">Skala aus 4 px. Abschnitt oben und unten 64 px (Handy) bzw. 80 px; Abschnittskopf zu Inhalt 40 px.</p></div>
    <div class="box"><h3>Breiten {B}</h3>
      <table class="t"><tr><td><b>Inhaltsbreite</b></td><td>max. 80 rem (1280 px)</td></tr><tr><td><b>Seitenrand</b></td><td>16 px · ab 640 px 24 px · ab 1024 px 32 px</td></tr><tr><td><b>Navigation</b></td><td>Pille, max. 56 rem, oben mit 16 px Abstand</td></tr><tr><td><b>Fließtext</b></td><td>max. 65 bis 75 Zeichen</td></tr><tr><td><b>Umbrüche</b></td><td>640 · 768 · 1024 · 1280 px</td></tr></table>
      <h3 style="margin-top:12px">Glas {B}</h3><p class="small" style="margin:0">Weiß 40 % (Karten), 82 % (über Fotos), Navy 60 % (dunkel), Weichzeichner 20 px, Rand weiß 50 %.</p></div>
    <div class="box"><h3>Radien</h3><div class="g4" style="grid-template-columns:repeat(4,minmax(0,1fr));gap:6px">{rad}</div><h3 style="margin-top:12px">Schatten</h3><div class="g3" style="grid-template-columns:repeat(3,minmax(0,1fr));gap:8px">{shadows}</div></div>
  </div>
  <div class="g2 mt"><div class="box flat"><h3>Print {E}</h3><p class="small" style="margin:0">Satzspiegel A4 hoch: Ränder links 25 mm, rechts 20 mm, oben 20 mm, unten 18 mm. Rasterbasis 4 mm, Spaltenabstand 6 mm, Zeilenabstand 14 pt bei 10 pt Schrift.</p></div>
  <div class="box flat"><h3>Folien {E}</h3><p class="small" style="margin:0">1920 × 1080 px, Ränder 120 px seitlich, 96 px oben und unten, Inhaltsfläche 1680 × 888 px, Basisraster 24 px.</p></div></div>
</section>'''


# ------------------------------------------------------------------ 15 Hintergründe
def p_hintergrund(n):
    tile = lambda cls, cap: f'<div><div class="osm-aurora {cls}" style="height:150px;border-radius:14px;border:1px solid var(--osm-linie);overflow:hidden;display:grid;place-items:center"><div class="osm-karte" style="padding:10px 14px;border-radius:12px;font-size:12px;font-weight:700;color:var(--osm-navy);box-shadow:var(--osm-shadow-md)">Karte auf Schimmer</div></div><span class="cap">{cap}</span></div>'
    net = '<svg viewBox="0 0 300 130" style="width:100%;height:130px;display:block">' + "".join(
        f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#0284c7" stroke-opacity=".22" stroke-width="1"/>' for a, b in
        [((20, 30), (90, 70)), ((90, 70), (160, 25)), ((90, 70), (140, 110)), ((160, 25), (240, 60)), ((140, 110), (240, 60)), ((240, 60), (285, 105)), ((20, 30), (60, 105)), ((60, 105), (140, 110))]) + "".join(
        f'<circle cx="{x}" cy="{y}" r="3" fill="#94a3b8" fill-opacity=".5"/>' for x, y in [(20, 30), (90, 70), (160, 25), (140, 110), (240, 60), (285, 105), (60, 105)]) + '</svg>'
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Hintergründe", "Aurora, Netz und dunkle Flächen", "Hintergründe bleiben zurückhaltend. Sie geben Tiefe, aber nie Kontrast zum Inhalt her.")}
  <div class="g4" style="align-items:start">
    {tile("", "Sehr leicht {B}: so auf der Website („Ihr Mehrwert“). Blau rechts, Orange links.".replace("{B}", B))}
    {tile("osm-aurora--leicht", "Leicht {E}: für Folien und Titelseiten.".replace("{E}", E))}
    {tile("osm-aurora--halb", "Halb {E}: Deckblatt, Plakat.".replace("{E}", E))}
    {tile("osm-aurora--gespiegelt osm-aurora--leicht", "Gespiegelt {E}: Blau links, warm rechts.".replace("{E}", E))}
  </div>
  <div class="g3 mt" style="align-items:start">
    <div class="box"><h3>Regeln für den Schimmer</h3><ul class="pl" style="margin:0"><li>Blau auf der <b>rechten</b>, warmes Orange (#FF6531) auf der <b>linken</b> Seite {B}.</li><li>Orange nie über 10 % Deckkraft in der Standardstufe. Nie unter Text hinter kleiner Schrift mit zu wenig Kontrast.</li><li>Oben und unten laufen die Farbflächen weich aus (150 px), damit keine Kante entsteht.</li><li>Aus Koralle (#FF9892) oder Pfirsich (#FF9989) lassen sich Varianten bilden {E}.</li></ul></div>
    <div class="box"><h3>Netz-Animation {B}</h3>{net}<p class="small" style="margin:0">Dünne Linien in osmera-Blau (Deckkraft 25 %), Knoten in Schiefer, nur auf dem hellen Seitengrund. In Print und Folien als ruhige Grafik verwenden.</p></div>
    <div class="box" style="background:var(--osm-navy);border-color:var(--osm-navy)"><h3 style="color:#fff">Dunkle Flächen {B}</h3><p class="small" style="color:#cbd5e1;margin:0">Navy <code>#0F172A</code>, bei Foto-Band und Navigation über Dunkel mit 60 % Deckkraft. Verlauf nur als „Navy nach Tiefblau“ (160°, bis #0C4A6E) und ein heller Himmelblau-Schein oben rechts {E}.</p></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 16 Bildwelt
def p_bild(n):
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Bildwelt", "Fotos und Bildeinsatz", "Echte Menschen in echten Situationen: ruhig, natürlich, klinisch glaubwürdig. Das Tablet verbindet die Bilder mit dem Produkt.")}
  <div style="display:flex;gap:20px;align-items:flex-start">
    <div style="width:250px;flex:none"><div style="border-radius:24px;overflow:hidden;box-shadow:var(--osm-shadow-2xl);height:250px"><img src="../img/hero-zwei-personen-960.webp" style="width:100%;height:100%;object-fit:cover;display:block" alt="Pflegekraft und Ärztin besprechen etwas auf einem Tablet"></div><span class="cap"><b>Hero</b> {B}: quadratisch, Radius 24 px, Schatten 2xl, leichter Verlauf von unten.</span></div>
    <div style="flex:1;min-width:0"><div style="border-radius:24px;overflow:hidden;box-shadow:var(--osm-shadow-2xl);background:var(--osm-navy);height:250px"><img src="../img/band-aerztin-1280.webp" style="width:100%;height:100%;object-fit:cover;object-position:60% 30%;display:block" alt="Ärztin mit Tablet im Klinikflur"></div><span class="cap"><b>Foto-Band</b> {B}: Foto in Navy-Karte, links weich in Navy ausgeblendet, Text und Schalter links.</span></div>
  </div>
  <div class="g3 mt">
    <div class="box"><h3>Auswahl {E}</h3><ul class="pl" style="margin:0"><li>Pflege und Ärzteschaft in Berufskleidung, natürliche Mimik, Blick in die Kamera oder auf das Tablet.</li><li>Umgebung, Kleidung und Gesichter wirken für ein deutsches Krankenhaus passend.</li><li>Bildschirmhell, ruhige Farben, Blau und Weiß dominieren.</li></ul></div>
    <div class="box"><h3>Gestaltung {B}</h3><ul class="pl" style="margin:0"><li>Kacheln über dem Foto verdecken nie Gesichter oder das Tablet.</li><li>Abgerundete Rahmen, Schatten 2xl, keine Rahmenlinie.</li><li>Alt-Text beschreibt die Szene in einem Satz.</li></ul></div>
    <div class="box"><h3>Technik und Lizenz {B}</h3><ul class="pl" style="margin:0"><li>AVIF und WebP in vier Breiten, Hero mit hoher Priorität, übrige verzögert laden.</li><li>iStock Standardlizenz mit Model- und Property-Release. Originale nicht im Webordner ablegen, Lizenznachweis aufbewahren.</li><li>Dieselbe Ärztin erscheint in Hero und Band (gleiche Serie).</li></ul></div>
  </div>
  <p class="small mt-s">Print: Fotos aus dem Original (6880 × 4584 px) neu zuschneiden, 300 dpi, nicht aus den Web-Dateien hochskalieren {E}.</p>
</section>'''


# ------------------------------------------------------------------ 17 Print
def p_print(n):
    letter = '''<div class="mini-wrap" style="width:270px;height:382px;background:#fff;position:relative;flex:none">
  <div style="position:absolute;left:0;top:0;width:210mm;height:297mm;transform:scale(.34);transform-origin:top left;background:#fff;font-family:Inter,sans-serif;color:#0f172a">
    <img src="logos/osmera-logo-navy.svg" style="position:absolute;left:25mm;top:18mm;width:45mm" alt="">
    <div style="position:absolute;left:25mm;top:50mm;width:85mm;font-size:6.5pt;color:#64748b;border-bottom:.3mm solid #cbd5e1;padding-bottom:1mm">Kutsche Köhl GbR · Zeithstraße 26 · 53721 Siegburg</div>
    <div style="position:absolute;left:25mm;top:57mm;width:85mm;font-size:10pt;line-height:1.5">Musterklinikum<br>Abteilung Personal<br>Musterstraße 1<br>12345 Musterstadt</div>
    <div style="position:absolute;right:20mm;top:57mm;width:50mm;font-size:8.5pt;line-height:1.5;color:#475569">kontakt@osmera.de<br>osmera.de<br><br>Datum: 17.10.2026</div>
    <div style="position:absolute;left:25mm;top:110mm;width:165mm;font-size:11pt;font-weight:700">Pilotprojekt: Ihr nächster Schritt</div>
    <div style="position:absolute;left:25mm;top:122mm;width:165mm;font-size:10pt;line-height:1.5;color:#1e293b">Sehr geehrte Damen und Herren,<br><br>osmera ergänzt Ihr Dienstplanprogramm, ohne es zu ersetzen. Im Pilotprojekt zeigen wir Ihnen an Ihren eigenen Daten, was möglich ist.<br><br>Mit freundlichen Grüßen<br>Lars Kutsche</div>
    <div style="position:absolute;left:25mm;right:20mm;bottom:12mm;font-size:7.5pt;color:#64748b;border-top:.3mm solid #cbd5e1;padding-top:2mm;display:flex;justify-content:space-between"><span>osmera · Kutsche Köhl GbR</span><span>Zeithstraße 26 · 53721 Siegburg</span><span>kontakt@osmera.de</span></div>
  </div></div>'''
    cards = '''<div style="display:flex;gap:10px;flex-wrap:wrap">
  <div style="width:240px;height:155px;background:#fff;border:1px solid #e2e8f0;border-radius:6px;box-shadow:0 8px 18px -12px rgb(15 23 42 / .5);padding:16px 18px;display:flex;flex-direction:column;justify-content:space-between"><img src="logos/osmera-logo-navy.svg" style="height:20px;align-self:flex-start" alt=""><div><div style="font-weight:800;font-size:15px;color:#0f172a;line-height:1.2">Lars Kutsche</div><div style="font-size:11px;color:#0284c7;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin-top:2px">Development</div><div style="font-size:10.5px;color:#475569;margin-top:8px;line-height:1.5">kontakt@osmera.de<br>osmera.de</div></div></div>
  <div class="osm-aurora osm-aurora--dunkel" style="width:240px;height:155px;border-radius:6px;box-shadow:0 8px 18px -12px rgb(15 23 42 / .5);display:grid;place-items:center;overflow:hidden"><img src="logos/osmera-logo-weiss.svg" style="height:26px" alt=""></div></div>'''
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Print", "Briefbogen, Visitenkarte, Druckdaten", "Alle Maße in diesem Kapitel sind Empfehlungen {E}. Die Beispiele zeigen die Anordnung. Namen und Anschrift stammen aus dem Impressum der Website.".replace("{E}", E))}
  <div style="display:flex;gap:26px;align-items:flex-start">
    {letter}
    <div style="flex:1;min-width:0">
      <div class="g2" style="grid-template-columns:1fr 1fr;gap:12px">
        <div class="box"><h3>Briefbogen A4 (DIN 5008, Form B)</h3><table class="t"><tr><td>Logo</td><td>45 mm breit, 25 mm von links, 18 mm von oben</td></tr><tr><td>Rücksendezeile</td><td>50 mm von oben, 6,5 pt Inter, Linie hellgrau</td></tr><tr><td>Anschrift</td><td>57 mm von oben, 25 mm von links, 85 × 45 mm</td></tr><tr><td>Betreff</td><td>110 mm von oben, Inter Bold 11 pt</td></tr><tr><td>Text</td><td>Inter Regular 10 pt, Zeilenabstand 14 pt, Navy-Schiefer #1E293B</td></tr><tr><td>Fuß</td><td>12 mm vom Rand, 7,5 pt, #64748B</td></tr></table></div>
        <div class="box"><h3>Druckdaten</h3><ul class="pl" style="margin:0"><li>PDF/X-4, 300 dpi, Beschnitt 3 mm, Sicherheitsabstand 5 mm.</li><li>Farben: Datei in sRGB anlegen, Druckerei konvertiert mit ICC-Profil und liefert Proof. Kleine Schrift (unter 9 pt) in Schwarz oder Navy, nicht in Mischfarbe.</li><li>Papier: weiß, matt, ungestrichen oder seidenmatt. Die helle Hintergrundfarbe #F8FAFC wird nicht gedruckt (Weiß lassen).</li><li>Logo immer als SVG/PDF einsetzen, nie als Pixelbild.</li></ul></div>
      </div>
      <h3 style="margin-top:12px">Visitenkarte 85 × 55 mm (Vorder- und Rückseite)</h3>
      {cards}
      <p class="small mt-s">Telefonnummern erscheinen nicht, da osmera Anrufe überflüssig machen will. Kontakt über kontakt@osmera.de.</p>
    </div>
  </div>
</section>'''


# ------------------------------------------------------------------ 18 Präsentation 1
def p_praes1(n):
    grid = '''<div class="mini-wrap" style="width:600px;height:337px;position:relative;background:#f8fafc;border:1px solid #cbd5e1;border-radius:6px;overflow:hidden;flex:none">
  <div style="position:absolute;left:37.5px;right:37.5px;top:30px;bottom:30px;border:1px dashed #0284c7;background:rgb(2 132 199 / .05)"></div>
  <img src="logos/osmera-logo-navy.svg" style="position:absolute;left:37.5px;top:20px;height:17.5px" alt="">
  <div style="position:absolute;left:37.5px;top:70px;font:700 7px/1 Inter;letter-spacing:.05em;color:#0284c7;text-transform:uppercase">Eyebrow</div>
  <div style="position:absolute;left:37.5px;top:84px;font:800 25px/1.1 Inter;color:#0f172a">Titel der Folie.<br>Eine Aussage.</div>
  <div style="position:absolute;left:37.5px;top:150px;width:240px;font:500 12.5px/1.4 Inter;color:#475569">Fließtext 20 pt. Maximal drei Zeilen pro Absatz.</div>
  <div style="position:absolute;right:37.5px;bottom:14px;font:500 8.5px Inter;color:#64748b">12</div>
  <div style="position:absolute;left:0;top:0;bottom:0;width:37.5px;display:grid;place-items:center;font:700 7px Inter;color:#0284c7;writing-mode:vertical-rl">120</div>
</div>'''
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Präsentation", "Folienraster und Regeln", "Format 16:9 (13,333 × 7,5 Zoll, 33,87 × 19,05 cm). Als HTML-Folie 1920 × 1080 px, dort entspricht 1 px genau 0,5 pt. Alle Werte {E}.".replace("{E}", E))}
  <div style="display:flex;gap:26px;align-items:flex-start;flex-wrap:wrap">
    {grid}
    <div style="flex:1;min-width:300px"><table class="t"><tr><th>Element</th><th>Wert (Folie 1920 × 1080)</th><th>PowerPoint</th></tr>
      <tr><td>Ränder</td><td>120 px seitlich, 96 px oben/unten</td><td>2,0 / 1,6 cm</td></tr>
      <tr><td>Logo</td><td>oben links, 56 px hoch, Abstand oben 64 px</td><td>Folienmaster</td></tr>
      <tr><td>Eyebrow</td><td>32 px Bold, Versalien, osmera-Blau</td><td>16 pt</td></tr>
      <tr><td>Titel</td><td>80 px ExtraBold (Titelfolie 112 px)</td><td>40 pt (56 pt)</td></tr>
      <tr><td>Text</td><td>40 px Medium, Schiefer</td><td>20 pt</td></tr>
      <tr><td>Klein, Quellen</td><td>32 px, #64748B</td><td>16 pt (Minimum)</td></tr>
      <tr><td>Seitenzahl</td><td>rechts unten, 28 px</td><td>14 pt</td></tr></table></div>
  </div>
  <div class="g3 mt">
    <div class="box"><h3>Regeln</h3><ul class="pl" style="margin:0"><li>Eine Aussage pro Folie, Titel als Satz mit Punkt.</li><li>Höchstens drei Karten oder Punkte nebeneinander.</li><li>Keine Schrift unter 16 pt, auch keine Fußnoten.</li></ul></div>
    <div class="box"><h3>Hintergründe</h3><ul class="pl" style="margin:0"><li>Standard: Grund #F8FAFC mit leichtem Schimmer (Blau rechts, Orange links).</li><li>Dunkle Folie (Navy) für Sicherheit und Abschnittswechsel.</li><li>Fotos mit dunklem Verlauf, Text darauf in Weiß.</li></ul></div>
    <div class="box"><h3>Bewegung</h3><ul class="pl" style="margin:0"><li>Nur „Einblenden“, kurz (0,3 s).</li><li>Keine Übergänge außer Überblenden.</li><li>Diagramme mit Rollen- und Markenfarben, nie mehr als vier Farben.</li></ul></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 19 Präsentation 2: Musterfolien
def p_praes2(n):
    def sl(inner, cls="", bg=""):
        return f'<div class="mini-wrap" style="width:480px;height:270px;flex:none"><div class="osm-folie {cls}" style="transform:scale(.25);transform-origin:top left;{bg}">{inner}</div></div>'
    s1 = sl('<img class="osm-folie__logo" src="logos/osmera-logo-navy.svg" alt=""><span class="osm-eyebrow" style="margin-top:250px">Pilotprojekt</span><h1>Intelligente Dienstplanung. <span class="osm-gradient-text">Verbunden mit Ihrem System.</span></h1>', "osm-aurora osm-aurora--leicht")
    s2 = sl('<img class="osm-folie__logo" src="logos/osmera-logo-navy.svg" alt=""><span class="osm-eyebrow" style="margin-top:130px">Die Lösung</span><h2>Ein Upgrade. Ohne Systemwechsel.</h2><div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:40px;margin-top:70px"><div class="osm-karte" style="padding:36px"><span class="osm-icon" style="width:100px;height:100px;font-size:44px;border-radius:28px"><i class="fa-solid fa-plug"></i></span><div class="osm-h4" style="font-size:46px;margin-top:22px">Verbindung</div></div><div class="osm-karte" style="padding:36px"><span class="osm-icon" style="width:100px;height:100px;font-size:44px;border-radius:28px"><i class="fa-solid fa-calculator"></i></span><div class="osm-h4" style="font-size:46px;margin-top:22px">Optimierung</div></div><div class="osm-karte" style="padding:36px"><span class="osm-icon" style="width:100px;height:100px;font-size:44px;border-radius:28px"><i class="fa-solid fa-file-export"></i></span><div class="osm-h4" style="font-size:46px;margin-top:22px">Rückgabe</div></div></div><span class="osm-folie__nr">3</span>')
    s3 = sl('<img class="osm-folie__logo" src="logos/osmera-logo-weiss.svg" alt=""><span class="osm-eyebrow osm-eyebrow--dunkel" style="margin-top:130px">Sicherheit</span><h2>Datenschutz als Fundament.</h2><p style="max-width:1100px;margin-top:30px">Sensible Personaldaten bleiben geschützt in Ihrem Klinik-Netzwerk. Nach außen gehen nur anonyme Token.</p><span class="osm-folie__nr" style="color:#94a3b8">4</span>', "osm-folie--dunkel")
    s4 = sl('<div style="display:flex;flex-direction:column;justify-content:center;height:100%"><img src="logos/osmera-logo-weiss.svg" style="height:120px;align-self:flex-start;margin-bottom:60px" alt=""><h2 style="font-size:96px">Gemeinsam Ergebnisse sichtbar machen.</h2><p style="margin-top:34px">kontakt@osmera.de · osmera.de</p></div>', "osm-folie--dunkel osm-aurora osm-aurora--dunkel")
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Präsentation", "Vier Musterfolien", "Titel, Inhalt mit Karten, dunkler Abschnitt, Abschluss. Gerendert mit osmera-brand.css (<code>.osm-folie</code>).")}
  <div class="slides" style="display:grid;grid-template-columns:repeat(2,480px);gap:14px;justify-content:center">{s1}{s2}{s3}{s4}</div>
</section>'''


# ------------------------------------------------------------------ 20 PDF und Dokumente
def p_pdf(n):
    return f'''<section class="pg" id="s{n}">{head(n)}{title("PDF und Dokumente", "Export, Office, Barrierefreiheit", "Gilt für Angebote, Datenblätter, Handreichungen und alles, was als PDF an Kliniken geht. Alle Regeln {E}.".replace("{E}", E))}
  <div class="g3" style="align-items:start">
    <div class="box"><h3>PDF für den Bildschirm</h3><ul class="pl" style="margin:0"><li>Farbraum sRGB, Schriften eingebettet, Größe unter 5 MB.</li><li>Titel, Autor („osmera“) und Sprache (Deutsch) in den Dokumenteigenschaften setzen.</li><li>Getaggtes PDF mit Lesereihenfolge, Alternativtexten, Lesezeichen und aktiven Links.</li><li>Kontraste prüfen (Kapitel „Farbkonzepte und Kontrast“). Kleine Schrift nicht in Himmelblau auf Weiß.</li></ul></div>
    <div class="box"><h3>PDF für den Druck</h3><ul class="pl" style="margin:0"><li>PDF/X-4, Beschnitt 3 mm, Schnittmarken, 300 dpi.</li><li>Farben von der Druckerei konvertieren und proofen lassen.</li><li>Logo als Vektor (SVG nach PDF), nie als Screenshot.</li><li>Navy #0F172A als Volltonfläche nicht über große Flächen mit kleiner heller Schrift (Läuft zu).</li></ul></div>
    <div class="box"><h3>Word, Pages, Google Docs</h3><table class="t"><tr><td>Titel</td><td>Inter ExtraBold 28 pt, Navy</td></tr><tr><td>Überschrift 1 / 2 / 3</td><td>20 / 14 / 11 pt, Inter Bold, Navy</td></tr><tr><td>Standard</td><td>Inter 10 pt, Zeilenabstand 1,4, #1E293B</td></tr><tr><td>Zitat</td><td>Inter Medium 11 pt, Schiefer, linker Strich osmera-Blau</td></tr><tr><td>Rand</td><td>25 / 20 / 20 / 18 mm</td></tr></table></div>
  </div>
  <div class="g2 mt">
    <div class="box"><h3>PowerPoint, Keynote, Google Slides</h3><ul class="pl" style="margin:0"><li>Format 16:9, Folienmaster mit Logo oben links und Seitenzahl unten rechts.</li><li>Designfarben: Akzent 1 #0284C7, 2 #38BDF8, 3 #0369A1, 4 #9333EA, 5 #059669, 6 #D97706. Text dunkel #0F172A, hell #FFFFFF.</li><li>Schriften: Überschrift „Inter ExtraBold“, Text „Inter“. Inter und Urbanist vorher installieren. Weitergabe als PDF, nicht als Datei.</li></ul></div>
    <div class="box"><h3>Dateinamen</h3><p class="small" style="margin:0 0 6px"><code>osmera_&lt;Dokument&gt;_&lt;Kunde&gt;_v&lt;Nr&gt;_&lt;JJJJ-MM-TT&gt;.pdf</code></p><table class="t"><tr><td>Angebot</td><td><code>osmera_Angebot_Musterklinikum_v1_2026-10-17.pdf</code></td></tr><tr><td>Datenblatt</td><td><code>osmera_Datenblatt_flow_v2_2026-11-03.pdf</code></td></tr></table><p class="small mt-s" style="margin:6px 0 0">Keine Leerzeichen und Umlaute in Dateinamen, Version mit Zähler.</p></div>
  </div>
  <div class="g2 mt-s">
    <div class="box"><h3>Kopf- und Fußzeile</h3><p class="small" style="margin:0">Kopf: Logo links (Navy, 45 mm), rechts Dokumenttitel in 8,5 pt Schiefer. Fuß: Linie hellgrau, links „osmera · Kutsche Köhl GbR“, Mitte Seitenzahl „Seite 2 von 6“, rechts kontakt@osmera.de. Vertraulichkeit als Hinweis in der Fußzeile, nicht als Wasserzeichen.</p></div>
  </div>
</section>'''


# ------------------------------------------------------------------ 21 Anhang
def p_anhang(n):
    cells = [f'<tr><td><span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:{c["hex"]};border:1px solid #e2e8f0;vertical-align:middle"></span></td><td><code>--osm-{k}</code></td><td>{c["hex"]}</td></tr>' for k, c in T["farben"].items()]
    half = (len(cells) + 1) // 2
    tok = lambda part: '<table class="t tight" style="font-size:10.5px"><tr><th></th><th>Variable</th><th>HEX</th></tr>' + "".join(part) + '</table>'
    findings = [
        ("Kontrast", "osmera-Blau #0284C7 erreicht auf Weiß nur 4,10:1. Für kleine Schrift und Button-Beschriftung #0369A1 (5,93:1) verwenden."),
        ("Favicon", "Die Website hat kein Favicon. Vorschlag: <code>logos/osmera-app-icon.svg</code>."),
        ("Schrift", "„Outfit“ wird geladen, aber nirgends genutzt. Entfernen spart eine Anfrage."),
        ("Logo-Farbe", "Der Ring erbt auf der Website die Seitenfarbe #1E293B, die Wortmarke ist #0F172A. Einheitlich Navy #0F172A setzen."),
        ("Zwei Markenwelten", "Das Design System von Juni 2026 (Produkt-Oberfläche) nutzt Insignia/Rubik, #071E3D und Cyan #00F0D4 und dasselbe Präfix <code>--osm-</code>. Vor dem Einsatz auf Folien, Print oder in der App festlegen, welche Welt gilt, und das Präfix trennen."),
        ("Tailwind", "Tailwind kommt per CDN-Skript. Für den Dauerbetrieb ein gebautes CSS verwenden."),
    ]
    fl = "".join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a, b in findings)
    return f'''<section class="pg" id="s{n}">{head(n)}{title("Anhang", "Beobachtungen, Tokens, Verlauf")}
  <div class="g2" style="grid-template-columns:1fr 1.25fr;align-items:start">
    <div><div class="box"><h3>Beobachtungen an der Website (17.10.2026)</h3><table class="t">{fl}</table></div>
      <div class="box mt-s"><h3>Änderungsverlauf</h3><table class="t"><tr><td><b>1.0</b></td><td>17.10.2026</td><td>Erste Fassung aus dem Stand der Website (Commit 602bef7).</td></tr></table>
      <p class="small mt-s" style="margin:6px 0 0">Neue Versionen: Nummer erhöhen, Datum und Änderungen eintragen, <code>osmera-tokens.json</code> mitführen.</p></div></div>
    <div class="box"><h3>Farb-Tokens</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">{tok(cells[:half])}{tok(cells[half:])}</div></div>
  </div>
</section>'''
