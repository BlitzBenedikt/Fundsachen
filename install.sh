#!/bin/bash
# 🎉 Fundsachen Webseite - Installationsskript
# Dieses Script richtet alles automatisch ein

echo "🎉 Willkommen bei der Fundsachen Webseite Installation!"
echo ""
echo "📁 Projektverzeichnis: $(pwd)"
echo ""

# Prüfe Python
if command -v python3 &> /dev/null; then
    echo "✓ Python3 gefunden"
else
    echo "✗ Python3 nicht gefunden (optional, für Skripte nötig)"
fi

# Erstelle images Ordner
if [ ! -d "images" ]; then
    mkdir -p images
    echo "✓ images/ Ordner erstellt"
else
    echo "✓ images/ Ordner existiert bereits"
fi

# Prüfe wichtige Dateien
echo ""
echo "Prüfe Projektdateien:"
for file in index.html config.json manifest.json sw.js
do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ✗ $file FEHLT!"
    fi
done

echo ""
echo "Prüfe Dokumentation:"
for file in START.md README.md SETUP.md DEPLOYMENT.md CHECKLISTE.md
do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ✗ $file FEHLT!"
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Installation fertig!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📖 Nächste Schritte:"
echo "  1. Öffne: START.md"
echo "  2. Folge: Den Anweisungen"
echo "  3. Teste: index.html im Browser"
echo "  4. Deploy: Mit DEPLOYMENT.md"
echo ""
echo "🌐 Webseite öffnen:"
echo "  Gib im Browser ein oder Doppelklick auf:"
echo "  $(pwd)/index.html"
echo ""
echo "💡 Hilfreich:"
echo "  - START.md     → Erste Schritte"
echo "  - docs.html    → Visuelle Doku"
echo "  - OVERVIEW.md  → Komplette Übersicht"
echo ""
echo "🚀 Viel Erfolg! Du schaffst das!"
