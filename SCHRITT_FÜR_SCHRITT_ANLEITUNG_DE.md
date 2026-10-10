# Schritt-für-Schritt-Anleitung: Entwicklung und Deployment für osmera.de

Diese Anleitung erklärt, wie Sie Code pushen, Worktrees im Browser überprüfen und Access-Tokens für Staging-Umgebungen erhalten.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie:
1. Das Repository geklont haben: `git clone <repo-url>`
2. In das Projektverzeichnis gewechselt sind: `cd osmera.de`
3. Die initialen Worktrees eingerichtet haben (falls noch nicht geschehen):
   ```bash
   git checkout -b 101026_NewVersion
   git worktree add development 101026_NewVersion
   git checkout -b 101028_VersionTwo
   git worktree add staging-101028 101028_VersionTwo
   ```

## Schritt 1: Arbeiten im Development-Worktree

### 1.1 Wechseln Sie zum Development-Worktree
```bash
cd development
# Jetzt sind Sie im 101026_NewVersion Branch
```

### 1.2 Machen Sie Ihre Änderungen
Bearbeiten Sie die Dateien nach Bedarf (z. B. index.html, impressum.html).

### 1.3 Überprüfen Sie Ihre Änderungen lokal
```bash
# Mit Python (empfohlen, keine Abhängigkeiten)
python3 -m http.server 8000
# Öffnen Sie dann http://localhost:8000 in Ihrem Browser

# Oder mit Node.js (falls installiert)
npx serve .
# Öffnen Sie dann http://localhost:5000 in Ihrem Browser
```

### 1.4 Committen Sie Ihre Änderungen
```bash
git add .
git commit -m "Beschreibung Ihrer Änderungen"
```

### 1.5 Pushen Sie zum Remote-Repository
```bash
git push origin 101026_NewVersion
```

**Wichtig:** Beim Pushen des Development-Branches (`101026_NewVersion`) wird **kein** Staging-Deployment ausgelöst. Dieser Branch dient ausschließlich der Entwicklung.

## Schritt 2: Arbeiten im Staging-Worktree (für Preview/Review)

### 2.1 Wechseln Sie zum Staging-Worktree
```bash
cd ../staging-101028
# Jetzt sind Sie im 101028_VersionTwo Branch
```

### 2.2 Machen Sie Ihre Änderungen
Bearbeiten Sie die Dateien nach Bedarf für Ihre Preview-Version.

### 2.3 Committen Sie Ihre Änderungen
```bash
git add .
git commit -m "Beschreibung Ihrer Staging-Änderungen"
```

### 2.4 Pushen Sie zum Remote-Repository (löst Staging-Deployment aus)
```bash
git push origin 101028_VersionTwo
```

**Wichtig:** Beim Pushen eines Staging-Branches (wie `101028_VersionTwo`) löst dies **automatisch** ein Staging-Deployment über GitHub Actions aus.

## Schritt 3: Überprüfen Sie das Staging-Deployment im Browser

### 3.1 Warten Sie auf das GitHub Actions Deployment
Nach dem Pushen sollten Sie sehen, dass GitHub Actions beginnt zu arbeiten. Sie können den Fortschritt unter:
- GitHub Repository → Actions → [Ihr jüngster Workflow Run]

### 3.2 Finden Sie die Staging-URL und das Token
Nach erfolgreichem Deployment sehen Sie in den GitHub Actions Logs etwas wie folgt:

```
Staging-Deployment erfolgreich!
Staging-URL: https://osmera.de/staging-a7x9/
Access-Token: abc123def456ghi789jkl012mno345pqr678stu901vwx
Vollzugriffs-URL: https://osmera.de/staging-a7x9/?token=abc123def456ghi789jkl012mno345pqr678stu901vwx
```

### 3.3 Öffnen Sie die Staging-URL im Browser
Verwenden Sie die **Vollzugriffs-URL** aus den Logs:
```
https://osmera.de/staging-a7x9/?token=abc123def456ghi789jkl012mno345pqr678stu901vwx
```

**Wichtig:** Sie müssen den Token-Parameter `?token=...` in der URL enthalten haben, um Zugriff zu erhalten. Ohne diesen Token sehen Sie nur eine Warteseite.

### 3.4 Testen Sie die Staging-Umgebung
- Überprüfen Sie, ob Ihre Änderungen korrekt angezeigt werden
- Testen Sie alle Links und Funktionalitäten
- Teilen Sie die Vollzugriffs-URL mit Stakeholdern für Review

## Schritt 4: Von Staging zur Produktion gehen

### 4.1 Review-Prozess
Nachdem Sie das Staging-Deployment überprüft haben und alle Stakeholder zugestimmt haben:

### 4.2 Erstellen Sie einen Pull-Request
1. Gehen Sie zu Ihrem GitHub Repository
2. Klicken Sie auf "Pull Requests" → "New Pull Request"
3. Wählen Sie `base: main` und `compare: 101028_VersionTwo` (oder Ihren Feature-Branch)
4. Erstellen Sie den Pull-Request mit einer aussagekräftigen Beschreibung
5. Lassen Sie den PR von Teammitgliedern reviewen

### 4.3 Mergen Sie in main
Nachdem der PR genehmigt wurde:
1. Klicken Sie auf "Merge pull request"
2. Bestätigen Sie den Merge
3. GitHub Actions deployed automatisch die `main` Branch auf Production (`https://osmera.de/`)

## Schritt 5: Arbeiten mit zusätzlichen Worktrees

### 5.1 Erstellen Sie einen neuen Feature-Branch für zukünftige Arbeit
```bash
# Vom main Branch ausgehend
git checkout main
git pull origin main

# Neuen Branch erstellen
git checkout -b 101030_NextFeature
git worktree add feature-101030 101030_NextFeature
```

### 5.2 Arbeiten Sie im neuen Feature-Worktree
```bash
cd feature-101030
# Machen Sie Änderungen, committen, pushen
git add .
git commit -m "Initialer Commit für nächstes Feature"
git push origin 101030_NextFeature
```

### 5.3 Dieses pushen löst ein Staging-Deployment aus
Genau wie beim Staging-Worktree wird beim Pushen von `101030_NextFeature` ein neues Staging-Deployment mit einer neuen zufälligen URL ausgelöst.

## Schritt 6: Aufräumen alter Worktrees

### 6.1 Entfernen Sie Worktrees, die nicht mehr benötigt werden
```bash
# Vom Hauptverzeichnis aus
git worktree remove development
git worktree remove staging-101028
git worktree remove feature-101030
```

### 6.2 Bereinigen Sie veraltete Referenzen
```bash
git worktree prune
```

### 6.3 Löschen Sie lokale Branches (optional)
```bash
git branch -d 101026_NewVersion
git branch -d 101028_VersionTwo
git branch -d 101030_NextFeature
```

## Häufige Probleme und Lösungen

### Problem: "Ich sehe nur eine Warteseite beim Aufruf der Staging-URL"
**Lösung:** Sie haben wahrscheinlich den Token-Parameter vergessen. Die URL muss so aussehen:
```
https://osmera.de/staging-{hash}/?token={Ihr-Token}
```
Ohne den `?token=...` Teil sehen Sie nur die Warteseite.

### Problem: "Mein Staging-Deployment funktioniert nicht"
**Lösung:** 
1. Überprüfen Sie, ob Sie einen Feature-Branch gepusht haben (nicht den main Branch)
2. Schauen Sie in den GitHub Actions Logs nach Fehlermeldungen
3. Stellen Sie sicher, dass Ihr Branch name mit den im workflow.yml definierten Mustern übereinstimmt:
   - `main` → Production
   - `101026_NewVersion` → Staging
   - `101028_*` → Staging (alle Branches die mit 101028_ beginnen)

### Problem: "Die Icons werden im Staging nicht angezeigt"
**Lösung:** Dies könnte ein CSP-Problem sein. Stellen Sie sicher, dass die Content-Security-Policy in Ihren HTML-Dateien `https://cdnjs.cloudflare.com` in sowohl `style-src` als auch `font-src` erlaubt.

### Problem: "Ich kann zwischen Worktrees nicht wechseln"
**Lösung:** 
1. Stellen Sie sicher, dass Sie `git worktree remove` verwendet haben und nicht manuell `.git` Ordner gelöscht haben
2. Führen Sie `git worktree prune` aus um veraltete Referenzen zu bereinigen
3. Erstellen Sie den Worktree bei Bedarf neu

## Best Practices

1. **Entwickeln Sie immer im development/ Worktree** für neue Features
2. **Verwenden Sie Staging-Worktrees nur für Preview/Review** bevor Sie in main mergen
3. **Teilen Sie niemals Staging-URLs ohne Token** - sie sind zwar schwer zu erraten, aber nicht öffentlich zugänglich gemacht werden sollten
4. **Committen Sie häufig** mit aussagekräftigen Nachrichten
5. **Pull Requests sind wichtig** für Code Review bevor Sie in main mergen
6. **Löschen Sie alte Worktrees** um Ihr Arbeitsverzeichnis sauber zu halten
7. **Überprüfen Sie immer zuerst lokal** bevor Sie pushen (`python3 -m http.server 8000`)

## Nützliche Befehle auf einen Blick

### Worktree Verwaltung
```bash
# Alle Worktrees auflisten
git worktree list

# Neuen Development-Worktree erstellen
git checkout -b branch-name
git worktree add pfad/zum/worktree branch-name

# Worktree entfernen
git worktree remove pfad/zum/worktree

# Veraltete Referenzen bereinigen
git worktree prune
```

### Entwicklung Workflow
```bash
# Lokal testen
python3 -m http.server 8000

# Änderungen committen und pushen
git add .
git commit -m "Nachricht"
git push origin branch-name

# Zwischen Worktrees wechseln
cd ../anderer-worktree
```

### Staging Zugriff
```bash
# Nach erfolgreichem Deployment in GitHub Actions Logs nachschauen:
# Staging-URL: https://osmera.de/staging-{hash}/
# Access-Token: {Ihr-Token}
# Vollzugriff: https://osmera.de/staging-{hash}/?token={Ihr-Token}
```

---

*Letzte Aktualisierung: 2026-10-10*
*Diese Anleitung gilt für das osmera.de Repository mit dem beschriebenen Git-Worktree- und GitHub Actions Deployment-Workflow.*