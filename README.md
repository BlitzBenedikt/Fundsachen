# Fundsachen Webseite - Quick Start Guide

## 🚀 Schneller Start (5 Minuten)

### 1. Dateien kopieren
Du hast jetzt diese Dateien:
- `index.html` - Die Webseite
- `SETUP.md` - Detaillierte Anleitung
- `generate-test-images.py` - Script zum Erstellen von Test-Bildern (optional)
- `load-items.php` - PHP Script für Auto-Loading (optional)

### 2. Test-Bilder erstellen (Optional)
Wenn du schnell testen möchtest, führe aus:
```bash
cd /home/benediktjansen/Dokumente/Fundsachen
python3 generate-test-images.py
```

Das erstellt einige Platzhalter-Bilder zum Testen.

### 3. Deine eigenen Bilder hinzufügen
1. Lege deine Fotos im `images` Ordner ab
2. Benennen mit sprechenden Namen: `schwarzer-rucksack.jpg`, `blaue-wasserflasche.jpg`, etc.
3. Für mehrere Bilder pro Gegenstand: `schwarzer-rucksack.jpg`, `schwarzer-rucksack-2.jpg`

### 4. Items in der HTML konfigurieren
Öffne `index.html` mit einem Text-Editor und ersetze in der `loadItems()` Funktion die Items mit deinen Gegenständen.

**Beispiel:**
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
];
```

### 5. Deine Kontaktdaten eintragen
Suche nach `const CONFIG = {` in der `index.html` und ersetze:
- `phone`: Deine Telefonnummer
- `email`: Deine Email-Adresse
- `address`: Deine Adresse

### 6. Email-Formular einrichten (Optional aber wichtig!)
Gehe zu **https://formspree.io/**
1. Kostenlos registrieren
2. Neues Formular erstellen
3. Kopiere deine Form-ID
4. Ersetze in `index.html` die `formSubmitUrl`:
   ```javascript
   formSubmitUrl: 'https://formspree.io/f/YOUR_FORM_ID',
   ```

### 7. Öffne die Webseite
Doppelklick auf `index.html` oder öffne sie im Browser.

---

## 📱 Features

✅ **Mobile First Design** - Perfekt für Handys
✅ **Fancy Animationen** - Smooth Scrolling, Transitions, Hover-Effekte
✅ **Bildergalerie** - Durch Bilder mit Pfeilen swipen
✅ **Kontakt Modal** - Mit deinen Infos
✅ **Intelligentes Formular** - Auto-Artikelnummer, Validierung
✅ **Dark Mode** - Modernes Design
✅ **Responsive** - Funktioniert auf allen Geräten

---

## 🛠️ Troubleshooting

### Problem: Bilder werden nicht angezeigt
**Lösung:**
- Stelle sicher, dass der `images` Ordner im gleichen Verzeichnis wie `index.html` ist
- Überprüfe die Dateinamen - keine Umlaute verwenden (außer in Deutsch: ä, ö, ü sind ok)
- Verwende Formate: JPG, PNG, GIF, WebP

### Problem: Formular funktioniert nicht
**Lösung:**
- Hast du Formspree eingerichtet?
- Ist die Form-ID in `index.html` richtig?
- Öffne Browser-Konsole (F12) und suche nach Fehlermeldungen

### Problem: Webseite sieht komisch aus
**Lösung:**
- Browser-Cache leeren: `Ctrl+Shift+Delete`
- Verschiedenen Browser versuchen

---

## 📖 Weitere Dokumentation

Siehe `SETUP.md` für ausführliche Anleitung!

---

**Viel Spaß mit deiner Webseite!** 🎉

