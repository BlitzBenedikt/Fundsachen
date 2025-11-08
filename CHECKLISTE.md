# ✅ Fundsachen Webseite - Komplette Checkliste

## 🎯 Phase 1: Vorbereitung

### Bilder sammeln
- [ ] Alle Fotos der Fundsachen aufnehmen
- [ ] Bilder in guter Qualität speichern (min. 800x800px)
- [ ] Dateinamen aussagekräftig benennen (z.B. `schwarzer-rucksack.jpg`)
- [ ] Für mehrere Bilder: Nummerierung (z.B. `schwarzer-rucksack.jpg`, `schwarzer-rucksack-2.jpg`)
- [ ] Bilder in `images` Ordner legen

### Kontaktdaten sammeln
- [ ] Telefonnummer bereit
- [ ] Email-Adresse
- [ ] Adresse/Ort
- [ ] Falls vorhanden: Website/Social Media

### Formspree Setup
- [ ] Account auf formspree.io erstellen
- [ ] Form ID erhalten
- [ ] Email-Bestätigung durchgeführt

---

## 🔧 Phase 2: Konfiguration

### index.html anpassen
- [ ] Kontaktdaten in CONFIG eingeben:
  ```javascript
  phone: 'DEINE_NUMMER',
  email: 'DEINE_EMAIL',
  address: 'DEINE_ADRESSE',
  formSubmitUrl: 'https://formspree.io/f/FORM_ID',
  ```

### Items hinzufügen
- [ ] In `loadItems()` Funktion
- [ ] Format für jeden Gegenstand:
  ```javascript
  {
      id: 'ITEM-001',
      title: 'Gegenstand Name',
      images: ['images/bild1.jpg', 'images/bild2.jpg'],
  }
  ```

### Text ändern (optional)
- [ ] Hero-Titel: "🔍 Fundsachen"
- [ ] Hero-Text: Beschreibung
- [ ] Section-Title: "Gefundene Gegenstände"

---

## 🧪 Phase 3: Testen (Lokal)

### Grundfunktionalität
- [ ] Öffne index.html im Browser
- [ ] Seite lädt fehlerfrei
- [ ] Keine Fehler in Browser-Konsole (F12)

### Desktop-Version
- [ ] Alle Bilder werden angezeigt
- [ ] Carousel funktioniert (Pfeile, Dots)
- [ ] Animationen sehen gut aus
- [ ] Kontakt-Button funktioniert
- [ ] Modal öffnet und schließt
- [ ] Tabs wechseln funktioniert

### Mobile-Version
- [ ] Öffne auf Smartphone/Tablet
- [ ] Layout ist responsive
- [ ] Alle Bilder sichtbar
- [ ] Buttons gut zu drücken (mindestens 50px)
- [ ] Text ist lesbar
- [ ] Kontakt-FAB Button sichtbar

### Formular testen
- [ ] Alle Input-Felder funktionieren
- [ ] Validierung funktioniert (min. 1 Kontaktmethode)
- [ ] Email und Telefon validieren
- [ ] Submit Button funktioniert
- [ ] Test-Email wird versendet
- [ ] Email kommt bei dir an

### Browser-Kompatibilität
- [ ] Chrome/Chromium ✓
- [ ] Firefox ✓
- [ ] Safari (macOS/iOS) ✓
- [ ] Edge ✓

---

## 🚀 Phase 4: Optimierung

### Performance
- [ ] Bilder komprimieren: `python3 compress-images.py`
- [ ] Bilder sind unter 500KB pro Stück
- [ ] Webseite lädt schnell (unter 3 Sekunden)
- [ ] Keine Konsolenwarnung

### SEO (optional)
- [ ] Meta-Description überprüft
- [ ] Keywords in HTML eingebunden
- [ ] Mobile-friendly Test bestanden (Google)

### Sicherheit
- [ ] Keine sensiblen Daten in JavaScript
- [ ] Formspree ist SSL verschlüsselt
- [ ] Kontaktdaten sind geschützt

---

## 📦 Phase 5: Deployment

### GitHub Pages Deployment
- [ ] GitHub Account erstellt
- [ ] Repository erstellt (`fundsachen`)
- [ ] Alle Dateien hochgeladen:
  - [ ] index.html
  - [ ] config.json
  - [ ] manifest.json
  - [ ] sw.js
  - [ ] .htaccess
  - [ ] images/ Ordner mit Bildern
- [ ] GitHub Pages aktiviert (Settings → Pages)
- [ ] Webseite ist online unter: `https://USERNAME.github.io/fundsachen`

### Oder: Netlify Deployment
- [ ] Netlify Account erstellt
- [ ] Mit GitHub verbunden
- [ ] Repository verknüpft
- [ ] Automatisches Deployment aktiv
- [ ] Webseite ist online

### Oder: Eigenes Hosting
- [ ] FTP-Zugang bekommen
- [ ] Alle Dateien hochgeladen
- [ ] Dateirechte gesetzt (644 für Dateien, 755 für Ordner)
- [ ] Webseite ist online

---

## ✔️ Phase 6: Live-Check

### Link testen
- [ ] URL öffnet die Webseite
- [ ] Seite lädt vollständig
- [ ] Alle Bilder sichtbar
- [ ] Keine 404-Fehler

### Responsiv Test
- [ ] Auf verschiedenen Geräten testen
- [ ] Mobile, Tablet, Desktop
- [ ] Chrome DevTools für verschiedene Auflösungen

### Formular-Test (Live)
- [ ] Kontakt-Modal öffnet
- [ ] Formular ausgefüllt
- [ ] Email versendet
- [ ] Email kommt an

### Social Media (optional)
- [ ] Link auf Facebook/Instagram posten
- [ ] Vorschau sieht gut aus
- [ ] QR-Code generieren (für Flyer)

---

## 📢 Phase 7: Ankündigung

### Freunde/CodeCamp benachrichtigen
- [ ] Link teilen in CodeClub-Chat
- [ ] Auf Social Media posten
- [ ] Link zu Flyer/Aushang hinzufügen
- [ ] In Email-Signatur einfügen

### Weitere Verbreitung
- [ ] Bei lokaler Gruppe posten
- [ ] In Schulblatt/Newsletter
- [ ] QR-Code ausdrucken (führt zur Webseite)

---

## 🎉 Phase 8: Wartung

### Regelmäßige Aufgaben
- [ ] Neue Gegenstände hinzufügen
- [ ] Gefundene Gegenstände entfernen (mit "✓ ABGEHOLT")
- [ ] Bilder aktualisieren
- [ ] Emails checken

### Monatscheck
- [ ] Webseite funktioniert noch?
- [ ] Alle Links aktiv?
- [ ] Emails werden zugestellt?
- [ ] Statistiken checken (falls Analytics aktiv)

### Bei Problemen
- [ ] Fehler in Konsole? (F12)
- [ ] Bilder-Pfade richtig?
- [ ] Formspree noch aktiv?
- [ ] Domain registriert?

---

## 📞 Support & Hilfe

Wenn was nicht funktioniert:

1. **Konsole überprüfen**: F12 → Console → Fehlertext lesen
2. **Browser-Cache leeren**: Ctrl+Shift+Delete
3. **Im GitHub Issue eröffnen** (falls GitHub Pages)
4. **CodeClub um Hilfe bitten**
5. **Online-Foren**: Stack Overflow, Gists, Reddit

---

## 🎓 Das hast du gelernt!

- ✓ HTML/CSS/JavaScript
- ✓ Responsive Design
- ✓ Web-Animationen
- ✓ Formulare & Validierung
- ✓ Deployment
- ✓ Git/GitHub (optional)

---

## 📅 Timeline

| Phase | Zeit | Status |
|-------|------|--------|
| Vorbereitung | 1-2 Tage | ⬜ |
| Konfiguration | 1 Tag | ⬜ |
| Testen | 1-2 Tage | ⬜ |
| Optimierung | 1 Tag | ⬜ |
| Deployment | 1 Tag | ⬜ |
| Live-Check | 1 Tag | ⬜ |
| Ankündigung | Laufend | ⬜ |
| **Gesamt** | **1-2 Wochen** | **⬜** |

---

**Viel Erfolg mit deinem Projekt!** 🚀

Markiere die Checkboxen, während du vorankommst.

