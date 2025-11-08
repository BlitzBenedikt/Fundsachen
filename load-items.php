<?php
/**
 * Auto-load images from images folder
 * Dieses Script erstellt automatisch die Items aus den Bildern im images Ordner
 * 
 * Verwendung: Füge im HTML-Script ein:
 * <script src="load-items.php"></script>
 */

header('Content-Type: application/javascript');

$imagesDir = __DIR__ . '/images';
$items = [];
$imagesByName = [];

// Suche alle Bilder
if (is_dir($imagesDir)) {
    $files = scandir($imagesDir);
    
    foreach ($files as $file) {
        if (in_array(pathinfo($file, PATHINFO_EXTENSION), ['jpg', 'jpeg', 'png', 'gif', 'webp'])) {
            // Extrahiere den Namen ohne Erweiterung und Nummer
            $basename = pathinfo($file, PATHINFO_FILENAME);
            
            // Finde die Basis des Namens (ohne -2, -3, etc.)
            $baseName = preg_replace('/-\d+$/', '', $basename);
            
            if (!isset($imagesByName[$baseName])) {
                $imagesByName[$baseName] = [];
            }
            
            $imagesByName[$baseName][] = 'images/' . $file;
        }
    }
    
    // Sortiere und erstelle Items
    ksort($imagesByName);
    $itemId = 1;
    
    foreach ($imagesByName as $name => $images) {
        sort($images); // Sortiere Bilder alphabetisch
        
        $items[] = [
            'id' => 'ITEM-' . str_pad($itemId, 3, '0', STR_PAD_LEFT),
            'title' => ucwords(str_replace(['-', '_'], ' ', $name)),
            'images' => $images,
        ];
        
        $itemId++;
    }
}

// Gebe JavaScript aus
echo "// Auto-loaded items from images folder\n";
echo "const AUTO_LOADED_ITEMS = " . json_encode($items, JSON_PRETTY_PRINT) . ";\n";
echo "\n";
echo "// Ersetze die items Variable in der loadItems() Funktion mit AUTO_LOADED_ITEMS\n";
echo "// items = AUTO_LOADED_ITEMS;\n";
?>
