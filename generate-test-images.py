#!/usr/bin/env python3
"""
Einfaches Script zum Erstellen von Test-Bildern für die Fundsachen Webseite
Verwendung: python3 generate-test-images.py
"""

import os
from PIL import Image, ImageDraw, ImageFont
import sys

def create_test_image(filename, title, width=400, height=400):
    """Erstelle ein einfaches Test-Bild mit Text"""
    
    # Farben
    bg_color = (51, 51, 51)  # Dunkelgrau
    text_color = (255, 255, 255)  # Weiß
    
    # Erstelle Bild
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Zeichne einen Rahmen
    draw.rectangle([(10, 10), (width-10, height-10)], outline=text_color, width=3)
    
    # Versuche Standard-Font zu verwenden, fallback auf default
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font = ImageFont.load_default()
        small_font = font
    
    # Zeichne Text
    text = title
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 40
    
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Zeichne Platzhalter
    draw.text(((width - 200) // 2, height - 80), "🔍 Platzhalter Bild", fill=text_color, font=small_font)
    
    # Speichere Bild
    img.save(filename)
    print(f"✓ Erstellt: {filename}")

def main():
    # Erstelle images Ordner wenn nicht vorhanden
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    # Erstelle Test-Bilder
    test_items = [
        ("schwarzer-rucksack", "Schwarzer Rucksack", 2),
        ("blaue-wasserflasche", "Blaue Wasserflasche", 1),
        ("graue-mütze", "Graue Mütze", 2),
        ("rote-kappe", "Rote Kappe", 1),
        ("silbernes-besteck", "Silbernes Besteck", 3),
    ]
    
    print("Erstelle Test-Bilder für Fundsachen Webseite...\n")
    
    for item_name, item_title, image_count in test_items:
        for i in range(image_count):
            if i == 0:
                filename = f"{item_name}.png"
            else:
                filename = f"{item_name}-{i+1}.png"
            
            filepath = os.path.join(images_dir, filename)
            create_test_image(filepath, item_title)
    
    print(f"\n✓ {len(test_items)} Test-Gegenstände erstellt!")
    print(f"Alle Bilder sind im '{images_dir}' Ordner")
    print("\nDu kannst diese Bilder jetzt mit echten Fotos ersetzen.")

if __name__ == '__main__':
    try:
        main()
    except ImportError:
        print("❌ Fehler: PIL (Pillow) ist nicht installiert!")
        print("\nInstalliere es mit:")
        print("  pip install pillow")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Fehler: {e}")
        sys.exit(1)
