// Service Worker für Fundsachen Webseite
// Ermöglicht Offline-Funktionalität und App-Installation

const CACHE_NAME = 'fundsachen-v1';
const ASSETS_TO_CACHE = [
    '/',
    '/index.html',
    '/manifest.json',
    '/config.json'
];

// Install Event
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            console.log('Service Worker: Caching assets');
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
    self.skipWaiting();
});

// Activate Event
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('Service Worker: Deleting old cache', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

// Fetch Event - Network first, fallback to cache
self.addEventListener('fetch', (event) => {
    // Nur für GET requests
    if (event.request.method !== 'GET') {
        return;
    }

    event.respondWith(
        fetch(event.request)
            .then((response) => {
                // Cache successful responses
                if (response && response.status === 200) {
                    const responseToCache = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                }
                return response;
            })
            .catch(() => {
                // Fallback to cache
                return caches.match(event.request)
                    .then((response) => {
                        if (response) {
                            return response;
                        }
                        
                        // Fallback für Images
                        if (event.request.destination === 'image') {
                            return new Response(
                                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400"><rect fill="#333" width="400" height="400"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" fill="#999" font-size="30">Offline</text></svg>',
                                { headers: { 'Content-Type': 'image/svg+xml' } }
                            );
                        }
                        
                        return response;
                    });
            })
    );
});

// Background Sync (optional - für Formular bei offline)
self.addEventListener('sync', (event) => {
    if (event.tag === 'sync-form') {
        event.waitUntil(
            // Versuche Formular zu resenden wenn wieder online
            new Promise((resolve) => {
                console.log('Service Worker: Syncing form data');
                resolve();
            })
        );
    }
});
