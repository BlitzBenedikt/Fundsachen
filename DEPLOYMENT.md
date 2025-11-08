# Deployment Guide - Fundsachen Webseite Online stellen

## Option 1: GitHub Pages (Empfohlen - Kostenlos & Einfach) 🌟

### Schritt 1: GitHub Account erstellen
1. Gehe zu [github.com](https://github.com)
2. Klicke auf "Sign up"
3. Folge den Anweisungen (kostenlos!)

### Schritt 2: Neues Repository erstellen
1. Klicke oben rechts auf "+" → "New repository"
2. Repository Name: `fundsachen` (oder beliebig)
3. Description: "Meine Fundsachen vom CodeCamp 2025" (optional)
4. Wähle "Public" (wichtig!)
5. Klicke "Create repository"

### Schritt 3: Dateien hochladen
**Option A: Via GitHub Website (Einfach)**
1. Im Repository, klicke "Add file" → "Upload files"
2. Ziehe die Dateien rein oder wähle sie aus:
   - `index.html`
   - `config.json`
   - `manifest.json`
   - `sw.js`
   - `.htaccess`
   - `images` Ordner mit allen Bildern
3. Schreibe Commit-Message: "Initial commit - Fundsachen Webseite"
4. Klicke "Commit changes"

**Option B: Via Git Command Line (Profis)**
```bash
cd /home/benediktjansen/Dokumente/Fundsachen
git init
git add .
git commit -m "Initial commit - Fundsachen Webseite"
git branch -M main
git remote add origin https://github.com/DEIN_USERNAME/fundsachen.git
git push -u origin main
```

### Schritt 4: GitHub Pages aktivieren
1. Gehe in deinem Repository zu "Settings"
2. Auf der linken Seite: "Pages"
3. Unter "Source", wähle "main" Branch
4. Klicke "Save"
5. Warte eine Minute...
6. Deine Webseite ist jetzt online unter: `https://DEIN_USERNAME.github.io/fundsachen`

### Schritt 5: Custom Domain (Optional)
Wenn du eine eigene Domain hast (z.B. `beispiel.de`):
1. In GitHub Pages Settings, unter "Custom domain"
2. Gib deine Domain ein: `fundsachen.beispiel.de`
3. DNS-Settings bei deinem Domain-Anbieter anpassen (siehe GitHub Anweisungen)

---

## Option 2: Netlify (Noch einfacher - Kostenlos) ⚡

### Schritt 1: Netlify Account erstellen
1. Gehe zu [netlify.com](https://netlify.com)
2. Klicke "Sign up"
3. Melde dich mit GitHub an (einfacher!)

### Schritt 2: Site erstellen
1. Klicke "New site from Git"
2. Wähle GitHub
3. Autorisiere Netlify
4. Wähle dein `fundsachen` Repository
5. Klicke "Deploy"
6. Netlify baut automatisch deine Seite!

### Schritt 3: Custom Domain (Optional)
1. In Netlify Dashboard → "Domain settings"
2. "Add custom domain"
3. Folge den Anweisungen

---

## Option 3: Traditionelles Web-Hosting (Mit Hoster)

Wenn du einen Web-Hoster hast (z.B. 1&1, Strato, etc.):

### Schritt 1: FTP Zugang besorgen
- Finde die FTP-Zugangsdaten bei deinem Hoster
- Typisch: FTP-Server, Benutzername, Passwort

### Schritt 2: FTP Client installieren
- Download: [FileZilla](https://filezilla-project.org/) (kostenlos)
- Oder nutze den eingebauten FTP im Hosting-Panel

### Schritt 3: Dateien hochladen
1. Verbinde dich mit FTP
2. Navigiere zum `public_html` oder `www` Ordner
3. Lade alle Dateien hoch:
   - index.html
   - Alle anderen Dateien
   - images Ordner mit Bildern

### Schritt 4: Fertig!
Deine Webseite ist jetzt online unter deiner Domain

---

## Wichtige Checkliste vor dem Go-Live 📋

- [ ] Alle Bilder im `images` Ordner hochgeladen
- [ ] `index.html` konfiguriert mit deinen Kontaktdaten
- [ ] Formspree ID eingetragen und bestätigt
- [ ] Alle Links testen (auf dem Smartphone testen!)
- [ ] Kontaktformular testen (Test-Email versenden)
- [ ] Bilder laden schnell? Evtl. komprimieren
- [ ] Mobile-Ansicht überprüfen
- [ ] Animationen funktionieren?

---

## Performance optimieren 🚀

### Bilder komprimieren
Große Bilder = langsame Seite. Komprimiere deine Fotos:
- Online: [TinyPNG.com](https://tinypng.com)
- Lokal: `python3 compress-images.py` (siehe unten)

### JavaScript/CSS minifizieren
Die index.html ist schon optimiert, aber du kannst sie weiter minifizieren mit:
- Online: [Minifier.org](https://www.minifier.org)

---

## Sicherheit 🔒

### HTTPS (Wichtig!)
- GitHub Pages: ✓ Automatisch (kostenlos)
- Netlify: ✓ Automatisch (kostenlos)
- Eigenes Hosting: Installiere SSL-Zertifikat (kostenlos via Let's Encrypt)

### Formspree Sicherheit
- Formspree verschlüsselt automatisch deine Daten
- Überprüfe regelmäßig die empfangenen Mails

---

## SEO & Social Media 📱

Die Webseite hat bereits Meta-Tags für bessere Auffindbarkeit:
- Meta Description
- Open Graph Tags (für Social Media)
- Structured Data

Aber du kannst die noch anpassen im `index.html` Header.

---

## Backup & Versionierung 💾

### GitHub Backup (Wichtig!)
Mit GitHub hast du automatisches Backup:
- Alle Versionen deiner Dateien sind gespeichert
- Du kannst jederzeit zu älteren Versionen zurück
- Kostenlos!

### Lokales Backup
```bash
# Regelmäßig auf USB-Stick kopieren:
cp -r /home/benediktjansen/Dokumente/Fundsachen /media/usb-stick/
```

---

## Monitoring & Analytics (Optional)

Möchtest du wissen, wer deine Seite besucht?

### Google Analytics (Kostenlos)
1. Gehe zu [analytics.google.com](https://analytics.google.com)
2. Erstelle einen Property für deine Seite
3. Kopiere den Tracking Code
4. Füge diesen vor `</body>` in `index.html` ein

### Netlify Analytics
- Automatisch in Netlify vorhanden (kostenlos Basic-Plan)

---

## Troubleshooting bei Deployment 🔧

### Problem: Bilder werden nicht angezeigt
- Stelle sicher, dass der `images` Ordner hochgeladen wurde
- Überprüfe die Dateipfade in `index.html` (case-sensitive!)

### Problem: Formular funktioniert nicht online
- Ist die Formspree ID richtig?
- Ist die Email in Formspree bestätigt?
- Überprüfe die Browser-Konsole (F12) auf Fehler

### Problem: Seite sieht komisch aus
- Browser-Cache leeren: Ctrl+Shift+Delete
- Versuch einen anderen Browser

### Problem: Domain funktioniert nicht
- DNS-Propagation kann 24-48 Stunden dauern
- Überprüfe die DNS-Settings bei deinem Domain-Anbieter

---

## Support 💬

Falls etwas nicht funktioniert:
1. Überprüfe die Browser-Konsole (F12)
2. Suche nach Fehlermeldungen
3. Teste auf verschiedenen Geräten
4. Frag im CodeClub nach Hilfe!

---

**Glückwunsch zu deiner neuen Webseite!** 🎉

