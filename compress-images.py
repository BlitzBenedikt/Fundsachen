#!/usr/bin/env python3
"""
Einfaches Script zum Komprimieren von Bildern für bessere Performance
Verwendung: python3 compress-images.py
"""

import os
from PIL import Image
import sys

def compress_image(input_path, output_path, quality=85, max_width=1200):
    """
    Komprimiere ein Bild
    
    Args:
        input_path: Pfad zum Original-Bild
        output_path: Pfad zum komprimierten Bild
        quality: JPEG Qualität (1-100, default: 85)
        max_width: Maximale Breite in Pixeln
    """
    
    try:
        img = Image.open(input_path)
        
        # Wenn zu groß, skalieren
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Konvertiere zu RGB wenn nötig (für JPEG)
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = rgb_img
        
        # Speichere mit Kompression
        img.save(output_path, quality=quality, optimize=True)
        
        # Gebe Ersparnis aus
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        saved = original_size - compressed_size
        saved_percent = (saved / original_size) * 100
        
        print(f"✓ {os.path.basename(input_path)}: {original_size//1024}KB → {compressed_size//1024}KB (Ersparnis: {saved_percent:.1f}%)")
        
        return True
        
    except Exception as e:
        print(f"✗ Fehler bei {input_path}: {e}")
        return False

def main():
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    
    if not os.path.isdir(images_dir):
        print(f"❌ Fehler: {images_dir} nicht gefunden!")
        sys.exit(1)
    
    print("🖼️  Starte Bildkompression...\n")
    
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    total_saved = 0
    compressed_count = 0
    
    # Finde alle Bilder
    for filename in os.listdir(images_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(images_dir, filename)
            
            # Erstelle Backup und speichere komprimiert
            if os.path.isfile(input_path):
                # Komprimiere
                if compress_image(input_path, input_path, quality=85, max_width=1200):
                    compressed_count += 1
    
    print(f"\n✓ {compressed_count} Bilder komprimiert!")
    print("\n💡 Tipp: Wiederhole dies vor dem Deployment für beste Performance.")

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
