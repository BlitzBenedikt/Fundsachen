# Fundsachen Webseite - Setup Guide

## Willkommen! 👋

Diese Webseite wurde speziell für deine Fundsachen vom CodeCamp 2025 erstellt. Hier ist eine Schritt-für-Schritt Anleitung zum Einrichten.

## 1. Bilder hinzufügen 📸

1. Erstelle einen Ordner `images` im gleichen Verzeichnis wie die `index.html`
2. Lege deine Bilder dort ab. Der Dateiname wird zum Titel des Gegenstandes
   - Format: `Gegenstands-Beschreibung.jpg`
   - Beispiele: `schwarzer-rucksack.jpg`, `blaue-wasserflasche.jpg`, `graue-mütze.jpg`

### Für mehrere Bilder von einem Gegenstand:
- Benenne sie mit Nummerierung am Ende: `schwarzer-rucksack.jpg`, `schwarzer-rucksack-2.jpg`

## 2. Deine Kontaktdaten eintragen 📞

Öffne `index.html` in einem Editor und suche nach dieser Zeile im `<script>` Bereich:

```javascript
const CONFIG = {
    phone: '+49 XXX XXXXXXXX',
    email: 'dein.email@example.com',
    address: 'Deine Straße 1\n12345 Deine Stadt',
    formSubmitUrl: 'https://formspree.io/f/DEINE_FORM_ID',
};
```

Ersetze:
- `+49 XXX XXXXXXXX` → Deine Telefonnummer
- `dein.email@example.com` → Deine Email-Adresse
- `Deine Straße 1\n12345 Deine Stadt` → Deine physische Adresse (mit `\n` für Zeilenumbruch)

## 3. Email-Formular einrichten (Formspree) 📧

Die Webseite verwendet **Formspree.io** um Nachrichten an dich zu versenden. Das ist kostenlos!

### Schritte:
1. Gehe zu https://formspree.io/
2. Erstelle einen kostenlosen Account
3. Erstelle ein neues Formular
4. Du erhältst eine **Form ID** (sieht so aus: `mnopqrst`)
5. Ersetze in der `index.html` die `DEINE_FORM_ID`:
   ```javascript
   formSubmitUrl: 'https://formspree.io/f/mnopqrst',
   ```
6. **Wichtig**: Bestätige deine Email-Adresse in Formspree (die bekommst du per Email)

### Alternative ohne Email-Service:
Wenn du kein Formspree verwenden möchtest, kannst du auch:
- Das Kontaktformular durch einen simple "Click to Email" Button ersetzen
- Ein Backend-Script verwenden (mehr Aufwand)

## 4. Items hinzufügen (Automatisch) 🔄

Die Webseite kann automatisch Bilder laden. Um das einzustellen:

1. Öffne `index.html` in einem Editor
2. Suche nach der `loadItems()` Funktion
3. Du siehst dort ein Demo-Beispiel mit Items

### Manuelles Hinzufügen (Empfohlen):

In der `loadItems()` Funktion, ersetze die Demo-Items:

```javascript
items = [
    {
        id: 'ITEM-001',
        title: 'Schwarzer Rucksack',
        images: ['images/schwarzer-rucksack.jpg', 'images/schwarzer-rucksack-2.jpg'],
    },
    {
        id: 'ITEM-002',
        title: 'Blaue Wasserflasche',
        images: ['images/blaue-wasserflasche.jpg'],
    },
    // ... weitere Items
];
```

**Format:**
- `id`: Eindeutige Nummer für jeden Gegenstand (ITEM-001, ITEM-002, etc.)
- `title`: Name des Gegenstandes
- `images`: Array mit Pfaden zu den Bildern

## 5. Die Webseite öffnen 🌐

Einfach `index.html` im Browser öffnen:
- Doppelklick auf die Datei, ODER
- Im Browser: `Datei → Öffnen` und die `index.html` auswählen

## 6. Im Internet verfügbar machen (Optional) 🚀

Wenn du die Webseite online haben möchtest:

### Option 1: GitHub Pages (Kostenlos & Einfach)
1. Erstelle ein GitHub Konto auf github.com
2. Erstelle ein neues Repository (Repo Namen egal)
3. Lade alle Dateien (index.html + images Ordner) hoch
4. Gehe zu Repository Settings → Pages
5. Wähle "Source: main" und speichern
6. Deine Webseite ist jetzt unter `https://dein-username.github.io/repo-name` erreichbar

### Option 2: Netlify (Kostenlos & Super Einfach)
1. Gehe zu netlify.com
2. Melde dich mit GitHub an
3. "New site from Git" → wähle dein Repository
4. Netlify baut und deployed deine Seite automatisch
5. Du bekommst eine öffentliche URL

### Option 3: Traditionelles Web-Hosting
- Lade die Dateien via FTP auf deinen Hosting-Provider

## 7. Features der Webseite ✨

✅ **Mobile-optimiert**: Perfekt für Handys, Tablets und Desktop
✅ **Fancy Animationen**: Smooth Scrolling, Hover-Effekte, etc.
✅ **Bildergalerie**: Mit Navigation und Dots für mehrere Bilder pro Gegenstand
✅ **Kontakt-Modal**: Mit zwei Tabs (Kontaktdaten + Formular)
✅ **Intelligentes Formular**: 
  - Artikelnummer kann vorausgefüllt werden
  - Validierung (mindestens eine Kontaktmethode)
  - Versendet automatisch per Email

## 8. Customization 🎨

### Farben ändern (Dark Mode):
Suche nach `:root {` in der `<style>` section:

```css
:root {
    --primary-color: #6366f1;      /* Hauptfarbe (lila) */
    --secondary-color: #ec4899;    /* Sekundärfarbe (pink) */
    --dark-bg: #0f172a;            /* Dunkler Hintergrund */
    --text-primary: #f1f5f9;       /* Haupttext */
}
```

### Text ändern:
- Hero-Überschrift: "🔍 Fundsachen"
- Hero-Text: "Du hast etwas..."
- Section-Titel: "Gefundene Gegenstände"

## 9. Troubleshooting 🔧

### Bilder werden nicht angezeigt
- Stelle sicher, dass die Bilder im `images` Ordner sind
- Dateinamen dürfen keine Umlaute haben (ä, ö, ü verwenden ist ok, aber test mit ASCII)
- Verwende Formate: JPG, PNG, GIF, WebP

### Formular funktioniert nicht
- Hast du Formspree konfiguriert?
- Hast du deine Email in Formspree bestätigt?
- Fehlerlog im Browser öffnen: F12 → Console

### Webseite sieht komisch aus
- Leere den Browser-Cache: `Ctrl+Shift+Delete` oder `Cmd+Shift+Delete`
- Versuche einen anderen Browser

## 10. Support & Hilfe 💬

Falls was nicht funktioniert:
1. Schau dir die Browser-Konsole an (F12)
2. Suche nach Fehlermeldungen
3. Überprüfe die `index.html` auf Tippfehler

---

**Viel Spaß mit deiner Webseite!** 🎉

Wenn du noch Fragen hast, schreib mir eine Nachricht über dein Kontaktformular! 😄
