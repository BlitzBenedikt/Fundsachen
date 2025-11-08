# 🎯 Dateinamens-System & Filter-Dokumentation

## Das Namensschema verstehen

Deine Bilder folgen einem cleveren System mit automatischer Kategorisierung!

### 📋 Format: `Titel_Typ-Subtyp.jpg`

```
"Schwarzer Hoddi mit zipper_Hoddi-2.jpg"
 ↑                                ↑
 Titel (Beschreibung)         Typ-Subtyp
```

### 🎨 Komponenten:

| Teil | Beispiel | Beschreibung |
|------|----------|-------------|
| **Titel** | `Schwarzer Hoddi mit zipper` | Beschreibung des Gegenstands |
| **Trennzeichen** | `_` | Pipe zwischen Titel und Kategorie |
| **Typ** | `Hoddi` | Hauptkategorie/Produkttyp |
| **Subtyp** | `2` oder `Einzeln` | Unterkategorie/Variante |
| **Bild-Nummer** | `-2` | 2. Bild des gleichen Artikels |
| **Dateiformat** | `.jpg` | Bildformat (jpg, png, webp, etc.) |

---

## 📁 Beispiele aus deinem System

### Hoddi (Pullover)
```
Schwarzer Hoddi für Leute die Warm undercover gehen möchten_Hoddi.jpg
Schwarzer Hoddi für Leute die Warm undercover gehen möchten_Hoddi-2.jpg
Schwarzer Hoddi mit zipper für leute die schnell undercover gehen möchten wenn ihnen Kalt wird_Hoddi.jpg
Schwarzer Hoddi mit zipper für leute die schnell undercover gehen möchten wenn ihnen Kalt wird_Hoddi-2.jpg
```
→ **Typ**: Hoddi | **Subtyp**: 2 (2. Bild eines Items)

### Socken (mit 2 Subtypes!)
```
Weiß Socke_Socke-Einzeln.jpg           → Typ: Socke | Subtyp: Einzeln
Adidas Socke ohen Partner_Socke-Einteln.jpg
Central Perk Socke_Socke-Einzeln.jpg
```
→ **Subtyp**: Einzeln (eine einzelne Socke)

```
Adidas Socken für Maloca_Socken-Paar.jpg
Schwarze Lange Socken suchen lange Beine_Paar-Socken.jpg
Socken mit Katzen logo_Socken-Paar.jpg
```
→ **Subtyp**: Paar (zwei Socken zusammen)

### T-Shirt
```
Graues_T-shirt.jpg                    → Keine Unterkategorie (wird zu "Allgemein")
Pushin_T-shirt.jpg
```

### Shampo/Duschgel
```
Axe für Leute die nach Alaska möchten_Shampo.jpg
Balea Duschgel für leute mit Wengi Zeit 3in1_Shampo.jpg
Dusch das für leute die sich von einer Shampo flasche zum Duschen zwingen_Shampo.jpg
Nivea Pflegedusche für leute die gepfelgt sein wollen_shampo.jpg
```

### Spezialfälle
```
Einsames Stück Stoff sucht zuhause.jpg           → Kein _ → Typ: "Sonstige"
Großes Weißes Stofflacken für Beamer_Bettlacken.jpg
Grüner Knopf Unterhose_Unterhose.jpg
```

---

## 🔍 Wie das Filter-System funktioniert

### 1. Automatische Kategorisierung
Die Webseite **parst alle Dateinamen** automatisch:
- Extrahiert **Titel** (alles vor `_`)
- Extrahiert **Typ** (Wort vor `-`)
- Extrahiert **Subtyp** (Wort nach `-`)
- Gruppiert **Bilder** nach Titel (z.B. -2 = 2. Bild)

### 2. Filter-Hierarchie
```
1. HAUPT-FILTER: Typ (Kategorie)
   └─ Socke, Hoddi, Unterhose, Shampo, etc.

2. UNTER-FILTER: Subtyp (nur wenn Typ gewählt)
   └─ Für Socke: Einzeln, Paar
   └─ Für Hoddi: -2, -3, etc.
```

### 3. Suche
- Durchsucht **Titel**, **Typ** und **Subtyp**
- Case-insensitive (Groß/Kleinschreibung egal)
- Real-time während man tippt

---

## 🎯 Filter-Beispiele

### Szenario 1: User sucht nach Socken
```
1. Klick auf Filter "Socke" (Hauptkategorie)
   → Zeigt alle Socken an

2. Sieht zusätzlichen Filter "Socke-Subtyp"
   → Optionen: "Einzeln" oder "Paar"

3. Klick auf "Einzeln"
   → Zeigt nur einzelne Socken
   → Z.B.: "Weiß Socke_Socke-Einzeln.jpg"

4. Klick auf "Paar"
   → Zeigt nur Sockenpaare
   → Z.B.: "Adidas Socken für Maloca_Socken-Paar.jpg"
```

### Szenario 2: User sucht nach "Hoddi"
```
1. Klick auf Filter "Hoddi"
   → Zeigt alle Hoddis an

2. Sieht zusätzlichen Filter "Hoddi-Subtyp"
   → Optionen: "-2" (2. Bild eines Artikels)

3. Klick auf "-2"
   → Zeigt nur 2. Bilder von Hoddis
```

### Szenario 3: User nutzt Suchleiste
```
Tippt: "Schwarzer"
→ Alle Artikel mit "Schwarzer" im Titel werden gefunden:
   - "Schwarzer Hoddi für Leute..."
   - "Schwarzer Hoddi mit zipper..."
   - "Schwarze Lange Socken..."
   - "Schwarze Socken suchen..."
```

---

## 🛠️ Technische Details

### Parsing-Logik (im JavaScript)
```javascript
function parseFilename(filename) {
    // Entferne Dateiendung
    const nameWithoutExt = filename.replace(/\.[^/.]+$/, '');
    
    // Splitte bei _
    const parts = nameWithoutExt.split('_');
    
    // Titel = alles vor _
    const title = parts[0];
    
    // Typ-Subtyp = alles nach _
    const typeInfo = parts[parts.length - 1];
    
    // Parse Typ und Subtyp
    if (typeInfo.includes('-')) {
        [type, subtype] = typeInfo.split('-');
    }
    
    return { title, type, subtype };
}
```

### Grouping-Logik
Bilder mit gleichem **Titel** werden zu einem Item zusammengefasst:
```
Item "Schwarzer Hoddi mit zipper"
├── Hoddi-2.jpg (Bild 1)
└── Hoddi-2.jpg (Bild 2)  ← Wird als Carousel angezeigt
```

---

## ✅ Regeln für korrektes Naming

### 📝 Do's ✓
```
✓ "Schwarzer Rucksack_Rucksack.jpg"
✓ "Weiße Socke_Socke-Einzeln.jpg"
✓ "Rote Socken Paar_Socke-Paar.jpg"
✓ "Hoddi zweites Bild_Hoddi-2.jpg"
✓ "Titel mit Leerzeichen_Typ-Subtyp.jpg"
```

### ❌ Don'ts ✗
```
✗ "Schwarzer Rucksack.jpg"           (Kein _ → wird zu "Sonstige")
✗ "Schwarzer_Rucksack_Bild2.jpg"     (Mehrere _ verwirren Parser)
✗ "Schwarzer Rucksack-2.jpg"         (Kein _ → -2 wird ignoriert)
✗ "schwarzer-rucksack_rucksack.jpg"  (Mehrere - vor _)
```

---

## 🎨 Filter-Button Farbcodierung

In der Webseite werden die Filter farblich markiert:

| Element | Farbe | Bedeutung |
|---------|-------|-----------|
| **Typ-Filter** | Gelb 🟨 | Hauptkategorie |
| **Subtyp-Filter** | Pink 🟩 | Unterkategorie |
| **Active Filter** | Lila-Pink Gradient | Aktuell ausgewählt |
| **Suchleiste** | Transparent | Keyword-Suche |

---

## 📊 Deine aktuellen Kategorien

### Typen (Hauptkategorien):
- **Socke** (mit Subtypes: Einzeln, Paar)
- **Hoddi**
- **Shampo**
- **T-shirt**
- **Unterhose**
- **Hose**
- **Bettlacken**
- **Lapen**
- **Handtuch**
- **Schraubendreher**
- **Sonstige**

### Subtypes (Wenn vorhanden):
- **Für Socke**: Einzeln, Paar
- **Für Hoddi**: -2 (2. Bild), -3 (3. Bild), etc.
- **Für andere**: Meist nur eine Variante

---

## 🚀 So funktioniert es im Browser

### Suchleiste oben
```
🔍 Suche nach Gegenständen...  [✕]
```
→ Echtzeit-Suche während tippen

### Filter-Buttons
```
Alle Kategorien [✓]  Socke  Hoddi  Shampo  T-shirt  ...
```
→ Klick wechselt Kategorie

### Subtype-Filter (Conditional)
```
Wenn Socke ausgewählt:
  Alle Typen [✓]  Einzeln  Paar
```
→ Nur sichtbar wenn Typ mit Subtypes gewählt

### Ergebnis-Info
```
Zeige 5 von 42 Artikeln
```
→ Update bei jedem Filter/Suche

---

## 🔄 Workflow beim Hochladen neuer Bilder

1. **Fotografiere Gegenstand**
2. **Benenne nach System**: `Beschreibung_Typ-Subtyp.jpg`
3. **Lade ins `images/` Folder hoch**
4. **Webseite aktualisiert automatisch** (reload)
5. **Neuer Filter wird hinzugefügt** (wenn neuer Typ)
6. **Bilder werden gruppiert** (wenn gleicher Titel)

---

## 💡 Pro-Tipps

### Tipp 1: Konsistente Schreibweise
Nutze immer die gleiche Schreibweise für Typen:
```
✓ "Socke-Einzeln" konsistent
✓ "Socke-Paar" konsistent
✗ "socke-einzeln" (Klein, wird anders sortiert)
```

### Tipp 2: Sprechende Namen
Je aussagekräftiger der Titel, desto einfacher die Suche:
```
✓ "Schwarzer Rucksack mit großen Taschen"
✗ "Ruck1"
```

### Tipp 3: Nummerierung für Mehrfach-Bilder
Nutze konsistente Nummerierung:
```
✓ "Hoddi_Hoddi-2.jpg", "Hoddi_Hoddi-3.jpg"
✗ "Hoddi_Hoddi_b.jpg" (Buchstaben verwirrend)
```

### Tipp 4: Keine Umlaute im Typ
```
✓ "Schönes Ding_Sonstiges.jpg"
✗ "Schönes Ding_Sönstiges.jpg" (Umlaut im Typ)
```

---

## 🎯 Zusammenfassung

| Aspekt | Detail |
|--------|--------|
| **Format** | `Titel_Typ-Subtyp-Nummer.jpg` |
| **Automatisches Parsing** | ✓ Ja |
| **Gruppierung** | Nach Titel |
| **Filter-Ebenen** | 2 (Typ + Subtyp) |
| **Suche** | Real-time, alle Felder |
| **Carousel** | Für mehrere Bilder pro Artikel |
| **Mobile-optimiert** | ✓ Ja |
| **Performance** | Super schnell |

**Dein System ist smart und effizient!** 🚀
