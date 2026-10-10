# Vollständiger Entwicklungs- & Deployment-Workflow für osmera.de

Dieses Dokument bietet einen umfassenden Überblick über den modernen Entwicklungs- und Deployment-Workflow, der für die statische Website osmera.de implementiert wurde.

## Übersicht

Dieses Projekt implementiert einen anspruchsvollen **git-worktree-basierten Workflow** mit **sicheren Staging-Umgebungen** und **automatisiertem GitHub Actions Deployment** für eine statische HTML-Website mit Tailwind CSS, Font Awesome und Vanilla JavaScript.

## Aktuelle Architektur

### Repository-Struktur

```
osmera.de/
├── .github/workflows/deploy.yml          # GitHub Actions Deployment-Workflow
├── .gitignore                              # Git Ignore-Regeln
├── .staging/                               # Staging-Infrastruktur
│   ├── access-control.js                  # Token-basierte Zugriffskontrolle für Staging
│   └── robots.txt                         # Staging robots.txt (blockiert alle Crawler)
├── CNAME                                   # Custom Domain Mapping (osmera.de)
├── development/                           # Worktree für Development-Branch
│   ├── .git                                # Worktree Git-Referenz
│   ├── CNAME
│   ├── index.html
│   └── impressum.html
├── impressum.html                         # Impressum-Seite
├── index.html                             # Haupt-Landingpage
├── README.md                              # Projektdokumentation
├── robots.txt                             # Production robots.txt (erlaubt alle)
├── sitemap.xml                            # XML-Sitemap für Suchmaschinen
└── staging-101028/                        # Worktree für Staging-Branch
    ├── .git                                # Worktree Git-Referenz
    ├── CNAME
    ├── index.html
    ├── impressum.html
    ├── access-control.js                  # Wird während Deployment injiziert
    └── robots.txt                         # Wird während Deployment injiziert
```

### Aktive Worktrees

1. **`main`** (Production)
   - Branch: `main`
   - Deployed zu: `https://osmera.de/`
   - Status: Live-Seite

2. **`development/`** (Development)
   - Branch: `101026_NewVersion`
   - Verwendet für: Aktive Feature-Entwicklung und Experimente
   - Status: Aktiver Worktree

3. **`staging-101028/`** (Staging)
   - Branch: `101028_VersionTwo`
   - Verwendet für: Staging/Preview-Umgebungen
   - Status: Aktiver Worktree

## Git Worktree Architektur

### Kern-Befehle

```bash
# Erstellen eines neuen Development-Worktrees
git checkout -b 101026_NewVersion
git worktree add development 101026_NewVersion

# Erstellen eines neuen Staging-Worktrees
git checkout -b 101028_VersionTwo
git worktree add staging-101028 101028_VersionTwo

# Alle aktiven Worktrees auflisten
git worktree list

# Zwischen Worktrees wechseln
cd development
# Jetzt sind Sie im Development-Worktree
cd ../staging-101028
# Jetzt sind Sie im Staging-101028-Worktree

# Einen Worktree entfernen (wenn nicht mehr benötigt)
git worktree remove development
git worktree remove staging-101028

# Veraltete Worktree-Referenzen bereinigen
git worktree prune
```

### Best Practices für Worktree-Management

- **Löschen Sie `.git` Dateien NIEMALS manuell** — verwenden Sie stattdessen `git worktree remove`
- **Bereinigen Sie immer** mit `git worktree prune` beim Entfernen von Worktrees
- **Verwenden Sie beschreibende Namen** für Worktree-Verzeichnisse (z. B. `staging-101028`)
- **Halten Sie Worktrees leichtgewichtig** — sie duplizieren Dateien, teilen sich aber die Git-Objektdatenbank

## Deployment-Strategie

### Production Deployment (`main` Branch)

**Auslöser:** Push auf den `main` Branch

**Prozess:**
1. GitHub Actions führt den Deployment-Workflow aus
2. Deployed das gesamte Repository in das Root-Verzeichnis von GitHub Pages
3. Seite wird verfügbar unter: `https://osmera.de/`
4. Keine Zugriffskontrolle oder Einschränkungen angewendet

**Security Headers (via Meta-Tags):**
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Content-Security-Policy: Umfassende CSP`

### Staging Deployment (Feature Branches)

**Auslöser:** Push auf beliebige Feature-Branches (z. B. `101026_NewVersion`, `101028_VersionTwo`)

**Prozess:**
1. GitHub Actions generiert einen zufälligen 4-Zeichen-Hash (z. B. `a7x9`)
2. **WICHTIG:** Erstellt ein separates Staging-Verzeichnis (`staging-deploy/`) in der Arbeitskopie, um zu verhindern, dass das Staging-Verzeichnis in sich selbst kopiert wird
3. Kopiert alle Seiten-Dateien in das Staging-Verzeichnis
4. Injiziert Staging-spezifische Dateien und Konfigurationen:
   - `robots.txt` (blockiert alle Crawler)
   - `access-control.js` (token-basierte Zugriffskontrolle)
   - Meta noindex Tags in HTML-Dateien
5. Deployed zu: `https://osmera.de/staging-{hash}/`

**Sicherheits-Ebenen:**

1. **Zufällige Subverzeichnis-URLs**
   - Muster: `https://osmera.de/staging-{random-hash}/`
   - Sicherheit durch Unbekanntheit

2. **robots.txt Blockierung**
   ```
   User-agent: *
   Disallow: /
   ```

3. **Meta Noindex Tags**
   - Fallback-Mechanismus falls robots.txt ignoriert wird
   - Wird in den HTML `<head>` Bereich injiziert

4. **Token-basierte Zugriffskontrolle**
   - JavaScript-Skript erfordert ein geheimes Token in der URL
   - Token wird pro Deployment von GitHub Actions generiert
   - Zugriffs-URL: `https://osmera.de/staging-{hash}/?token={secret-token}`

**Wichtiger Fix für Staging 404:**

**Problem:** Staging-URLs (`https://osmera.de/staging-{hash}/`) gaben 404-Fehler zurück, weil `force_orphan: true` in der GitHub Actions Workflow jedes Deployment löschte und die Staging-Subverzeichnisse in der gh-pages Branch verworfen wurden.

**Lösung:**
- Entfernt `force_orphan: true` aus der Workflow
- Fügt `keep_files: true` hinzu, um Dateien aus anderen Deploymenten zu erhalten
- Fügt einen Cleanup-Schritt vor Produktions-Deploymenten hinzu, um alte Staging-Verzeichnisse zu entfernen
- Verwendet ein separates Staging-Verzeichnis (`staging-deploy/`) für Staging-Deploymenten, um zu verhindern, dass das Staging-Verzeichnis in sich selbst kopiert wird

**Ergebnis:** Produktion und Staging können jetzt auf derselben gh-pages Branch koexistieren ohne sich gegenseitig zu löschen.

## Security & SEO Implementation

### Production SEO Optimierung

**robots.txt (Production):**
```
User-agent: *
Allow: /
Sitemap: https://osmera.de/sitemap.xml
```

**sitemap.xml:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://osmera.de/</loc>
    <lastmod>2026-10-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://osmera.de/impressum.html</loc>
    <lastmod>2026-10-10</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

**HTML Meta Tags (index.html und impressum.html):**

```html
<!-- SEO Meta Tags -->
<meta name="robots" content="index, follow">
<meta name="description" content="Intelligente Dienstplanung für Krankenhäuser. Verbindet sich nahtlos mit Ihrem System. Mehr Zeit für Patienten, weniger für Planung.">

<!-- Security Headers (via Meta Tags) -->
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://kit.fontawesome.com; style-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://fonts.googleapis.com https://cdnjs.cloudflare.com; img-src 'self' data: https:; font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self';">

<!-- Staging Noindex Fallback (JavaScript) -->
<script>
  // Staging noindex fallback: falls URL-Pfad /staging- enthält, noindex Meta-Tag injizieren
  if (window.location.pathname.includes('/staging-')) {
    var metaRobots = document.createElement('meta');
    metaRobots.name = 'robots';
    metaRobots.content = 'noindex, nofollow';
    document.head.appendChild(metaRobots);
  }
</script>
```

### Staging Security Implementation

**access-control.js (Staging):**

Ein umfassendes JavaScript-basiertes Zugriffskontrollsystem, das:

1. **URL-Tokens validiert** gegen ein deployment-spezifisches Token
2. **Eine Warteseite anzeigt** falls kein gültiges Token bereitgestellt wird
3. **Inhaltszugriff erlaubt** wenn ein gültiges Token vorhanden ist
4. **Mit Cookies funktioniert** für persistente Zugriffe
5. **Edge Cases behandelt** (localhost, direkter Zugriff, etc.)

**robots.txt (Staging):**
```
# Staging robots.txt — osmera.de
# Diese Datei blockiert Suchmaschinen vom Indexieren von Staging/Preview-Umgebungen.
# Sie wird von GitHub Actions Workflow in jedes zufällige Staging-Subverzeichnis kopiert.

User-agent: *
Disallow: /

# Erlaubt spezifische Assets, die auch im Staging crawlbar sein sollen
# (nützlich für Tracking-Pixel, etc.)
# Allow: /images/*

# Referenziert die Production Sitemap — Staging-Seiten sollten NICHT indexiert werden
# aber falls doch indexiert, sollten sie nicht mit Production konkurrieren
Sitemap: https://osmera.de/sitemap.xml

# Zusätzliche Direktiven für spezifische Crawler
User-agent: Googlebot
Disallow: /

User-agent: Bingbot
Disallow: /

User-agent: Applebot
Disallow: /

# Ende der Datei
```

## GitHub Actions Workflow

### Datei: `.github/workflows/deploy.yml`

**Hauptfunktionen:**

1. **Branch-basierte Deployment-Logik**
   - `main` → Production (Root von GitHub Pages)
   - Feature Branches → Staging (zufälliges Subverzeichnis)

2. **Zufällige Staging-URLs**
   - Generiert einzigartigen 4-Zeichen-Hash für jedes Staging-Deployment
   - Beispiel: `staging-a7x9`

3. **Staging-Datei-Vorbereitung**
   - Kopiert `robots.txt` und `access-control.js` in Staging-Verzeichnis
   - Injiziert Meta noindex Tags in HTML-Dateien
   - Injiziert Access-Control-Skript in HTML-Dateien
   - Generiert und bettet einzigartiges Zugriffs-Token ein

4. **Umfassendes Logging**
   - Klare Ausgabe der Deployment-Ergebnisse
   - URLs und Tokens für einfaches Teilen
   - Erfolgs-/Fehler-Benachrichtigungen

5. **Fehlerbehandlung**
   - Korrekte Bereinigung temporärer Dateien
   - Validierung der Deployment-Parameter

### Workflow-Auslöser

```yaml
on:
  push:
    branches:
      - main
      - '101026_NewVersion'
      - '101028_*'

  # Erlaubt manuelles Auslösen (z. B. zum Testen von Staging-Deployments)
  workflow_dispatch:
    inputs:
      branch:
        description: 'Branch zum Deployen (main für Production verwenden)'
        required: true
        default: 'main'
```

## Entwicklungs-Workflow

### Lokale Entwicklungseinrichtung

```bash
# Repository klonen
git clone <repo-url>
cd osmera.de

# Development-Worktree erstellen (falls noch nicht vorhanden)
git checkout -b 101026_NewVersion
git worktree add development 101026_NewVersion

# Staging-Worktree erstellen (Beispiel: 101028_VersionTwo)
git checkout -b 101028_VersionTwo
git worktree add staging-101028 101028_VersionTwo
```

### Arbeiten mit Worktrees

**Development Worktree (`development/`):**

```bash
cd development
# Dateien in diesem Verzeichnis bearbeiten
# Änderungen auf den 101026_NewVersion Branch committen
# Zu Remote pushen
```

**Staging Worktree (`staging-101028/`):**

```bash
cd staging-101028
# Dateien in diesem Verzeichnis bearbeiten
# Änderungen auf den 101028_VersionTwo Branch committen
# Zu Remote pushen (löst GitHub Actions Deployment aus)
```

### Lokales Testen

```bash
# Mit Python (keine Abhängigkeiten)
python3 -m http.server 8000

# Mit Node.js (falls installiert)
npx serve .
```

Öffnen Sie `http://localhost:8000` in Ihrem Browser.

## Beitrags-Workflow

### Schritt-für-Schritt Prozess

1. **Neuen Feature-Branch erstellen**
   ```bash
   git checkout -b 101029_NewFeature
   git worktree add feature-101029 101029_NewFeature
   ```

2. **Feature entwickeln**
   ```bash
   cd feature-101029
   # Dateien bearbeiten, Änderungen vornehmen
   git add .
   git commit -m "Neues Feature hinzufügen"
   git push origin 101029_NewFeature
   ```

3. **Feature testen**
   - Der GitHub Actions Workflow deployed das Feature automatisch auf eine zufällige Staging-URL
   - Staging-URL mit Stakeholdern zur Review teilen
   - Den im Deployment-Output bereitgestellten Access Token verwenden

4. **Review und Merge**
   - Staging-Deployment prüfen
   - Falls zufriedenstellend, Pull Request vom Feature-Branch zu `main` erstellen
   - In `main` mergen um in Production zu deployen

### Branch-Strategie

- **`main`**: Production-fertiger Code
- **Feature Branches** (z. B. `101026_NewVersion`, `101028_VersionTwo`): Entwicklung und Staging
- **Worktrees**: Lokale Entwicklungsumgebungen für jeden Branch

## Sicherheitsempfehlungen

### Für Staging-Umgebungen

1. **Staging-URLs NIEMALS öffentlich teilen** ohne Access Tokens
2. **Einzigartige Tokens** für jedes Staging-Deployment verwenden
3. **Tokens regelmäßig rotieren** für Hochsicherheits-Umgebungen
4. **Staging-Zugriffslogs überwachen** falls möglich
5. **Zusätzliche Sicherheitsebenen in Betracht ziehen** (z. B. Cloudflare Workers) für sensible Features

### Für Production

1. **`CNAME` Datei sicher aufbewahren** (bereits im Repository)
2. **HTTPS verwenden** (GitHub Pages stellt dies automatisch bereit)
3. **Regelmäßige Sicherheitsaudits** von HTML und JavaScript
4. **Auf ungewöhnliche Traffic-Muster achten**

## Fehlerbehebung

### Häufige Probleme

**Problem: Staging-URL nicht erreichbar**
- **Lösung:** Prüfen ob der Access Token korrekt an die URL angehängt ist
- **Beispiel:** `https://osmera.de/staging-a7x9/?token=abc123def456`

**Problem: Staging-Seite zeigt Warteseite**
- **Lösung:** Verifizieren dass der korrekte Access Token verwendet wird
- **Lösung:** Prüfen dass der URL-Pfad `/staging-` enthält (z. B. `https://osmera.de/staging-a7x9/`)

**Problem: Production-Seite aktualisiert nicht**
- **Lösung:** GitHub Actions Workflow Logs prüfen
- **Lösung:** Verifizieren dass Änderungen auf den `main` Branch committed wurden

**Problem: Worktree funktioniert nicht**
- **Lösung:** `git worktree prune` ausführen um veraltete Referenzen zu bereinigen
- **Lösung:** Worktree falls notwendig neu erstellen

### Hilfe erhalten

1. **GitHub Actions Workflow Logs** auf Deployment-Fehler prüfen
2. **README.md** für Setup-Anweisungen lesen
3. **DEPLOYMENT_WORKFLOW.md** für detaillierte Dokumentation prüfen
4. **Entwicklungsteam kontaktieren** unter `kontakt@osmera.de`

## Zukünftige Verbesserungen

### Empfohlene Erweiterungen

1. **Cloudflare Pages Integration**
   - Cloudflare Pages für echte passwortgeschützte Staging-Umgebungen nutzen
   - Bietet Enterprise-Grade Sicherheit für Preview-Umgebungen

2. **Erweiterte Zugriffskontrolle**
   - IP-basierte Zugriffsbeschränkungen implementieren
   - Zeitlich begrenzte Access Tokens hinzufügen
   - Integration mit bestehenden Authentifizierungssystemen

3. **Automatisiertes Testen**
   - Visuelle Regressionstests für Staging-Deployments hinzufügen
   - Accessibility-Testing implementieren
   - Performance-Testing hinzufügen

4. **Erweitertes Monitoring**
   - Staging-Deployment-Metriken tracken
   - Zugriffsmuster und Sicherheitsereignisse überwachen
   - Alerts für ungewöhnliche Aktivitäten einrichten

## Lizenz

Siehe [impressum.html](impressum.html) für rechtliche Informationen.

---

*Letzte Aktualisierung: 2026-10-10*
*Version: 1.0*
*Autor: Entwicklungsteam*
