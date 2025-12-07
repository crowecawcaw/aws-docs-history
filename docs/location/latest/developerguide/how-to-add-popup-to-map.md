# How to add a popup to a map

Amazon Location Service allows you to add popups to the map. You can add simple popups,
click-triggered popups on markers, hover-triggered popups, and popups for multiple
markers.

## Add your first popup

In this example, you will add your first popup.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Display a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "<API_KEY>";
            const mapStyle = "Standard";
            const awsRegion = "eu-central-1";
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map',
                style: styleUrl,
                center: [-96, 37.8],
                zoom: 2
            });

            const popup = new maplibregl.Popup({closeOnClick: false})
                .setLngLat([-96, 37.8])
                .setHTML('<h1>Hello USA!</h1>')
                .addTo(map);
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Show popup on click on a marker

In this example, you will attach a popup to a marker and display it on
click.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Display a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "<API_KEY>";
            const mapStyle = "Standard";
            const awsRegion = "eu-central-1";
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            const centralpark_nyc = [-73.966,40.781];
            const map = new maplibregl.Map({
                container: 'map',
                style: styleUrl,
                center: centralpark_nyc,
                zoom: 13
            });

            const popup = new maplibregl.Popup({offset: 25}).setText(
                'Central Park, NY is one of the most filmed locations in the world, appearing in over 240 feature films since 1908.'
            );

            new maplibregl.Marker()
                .setLngLat(centralpark_nyc)
                .setPopup(popup)
                .addTo(map);
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Show popup on hover on a marker

In this example, you will attach a popup to a marker and display it on
hover.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Display a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "<API_KEY>";
            const mapStyle = "Standard";
            const awsRegion = "eu-central-1";
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            const centralpark_nyc = [-73.966,40.781];
            const map = new maplibregl.Map({
                container: 'map',
                style: styleUrl,
                center: centralpark_nyc,
                zoom: 13
            });

            const marker = new maplibregl.Marker().setLngLat([-73.968285, 40.785091]).addTo(map);
            const popup = new maplibregl.Popup({ offset: 25 })
                .setHTML("<h3>Central Park</h3><p>Welcome to Central Park, NYC!</p>");

            const markerElement = marker.getElement();
            markerElement.addEventListener('mouseenter', () => {
                popup.setLngLat([-73.968285, 40.785091]).addTo(map);
            });
            markerElement.addEventListener('mouseleave', () => {
                popup.remove();
            });
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Show popup on click on multiple

markers

In this example, you will attach a popup to multiple markers and display it on
click.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Display a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "Your API Key";
            const mapStyle = "Monochrome";
            const awsRegion = "eu-central-1";
            const colorScheme ="Light";
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?color-scheme=${colorScheme}&key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map',
                style: styleUrl,
                center: [-123.126979, 49.2841563],
                zoom: 15,
                minZoom: 13,
                maxZoom: 17
            });

            const locations = [
                { id: 1, lat: 49.281108, lng: -123.117049, name: "Amazon - YVR11 office" },
                { id: 2, lat: 49.285580, lng: -123.115806, name: "Amazon - YVR20 office" },
                { id: 3, lat: 49.281661, lng: -123.114174, name: "Amazon - YVR14 office" },
                { id: 4, lat: 49.280663, lng: -123.114379, name: "Amazon - YVR26 office" },
                { id: 5, lat: 49.285343, lng: -123.129119, name: "Amazon - YVR25 office" }
            ];

            const geojson = {
                type: "FeatureCollection",
                features: locations.map(location => ({
                    type: "Feature",
                    properties: { id: location.id, name: location.name },
                    geometry: {
                        type: "Point",
                        coordinates: [location.lng, location.lat]
                    }
                }))
            };

            map.on('load', async () => {
                try {
                    const image = await loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1200px-Amazon_Web_Services_Logo.svg.png');
                    map.addImage('aws', image);

                    map.addSource('places', { type: 'geojson', data: geojson });

                    map.addLayer({
                        'id': 'places',
                        'type': 'symbol',
                        'source': 'places',
                        'layout': {
                            'icon-image': 'aws',
                            'icon-size': 0.025,
                            'icon-allow-overlap': true
                        }
                    });

                    const popup = new maplibregl.Popup({ closeButton: false, closeOnClick: false });

                    map.on('click', 'places', (e) => {
                        map.getCanvas().style.cursor = 'pointer';
                        const coordinates = e.features[0].geometry.coordinates.slice();
                        const name = e.features[0].properties.name;
                        popup.setLngLat(coordinates).setHTML(name).addTo(map);
                    });

                    map.on('mouseleave', 'places', () => {
                        map.getCanvas().style.cursor = '';
                        popup.remove();
                    });
                } catch (error) {
                    console.error('Error loading image:', error);
                }
            });

            async function loadImage(url) {
                return new Promise((resolve, reject) => {
                    const img = new Image();
                    img.crossOrigin = 'anonymous';
                    img.onload = () => resolve(img);
                    img.onerror = (error) => reject(error);
                    img.src = url;
                });
            }
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Show popup on hover on multiple

markers

In this example, you will attach a popup to multiple markers and display it on
hover.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Display a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "You API Key";
            const mapStyle = "Monochrome";  // eg. Standard, Monochrome, Hybrid, Satellite
            const awsRegion = "eu-central-1"; // eg. us-east-2, us-east-1, etc.
            const colorScheme ="Light"; // eg Dark, Light (default)
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?color-scheme=${colorScheme}&key=${apiKey}`;

            // Initialize the map
            const map = new maplibregl.Map({
                container: 'map', // Container id
                style: styleUrl, // Style URL
                center: [-123.126979, 49.2841563], // Starting position [lng, lat]
                zoom: 15, // Starting zoom
                minZoom: 13, // Minimum zoom level
                maxZoom: 17 // Maximum zoom level
            });

            const locations = [
                { id: 1, lat: 49.281108, lng: -123.117049, name: "Amazon - YVR11 office" },
                { id: 2, lat: 49.285580, lng: -123.115806, name: "Amazon - YVR20 office" },
                { id: 3, lat: 49.281661, lng: -123.114174, name: "Amazon - YVR14 office" },
                { id: 4, lat: 49.280663, lng: -123.114379, name: "Amazon - YVR26 office" },
                { id: 5, lat: 49.285343, lng: -123.129119, name: "Amazon - YVR25 office" }
            ];

            // Convert locations to GeoJSON
            const geojson = {
                type: "FeatureCollection",
                features: locations.map(location => ({
                    type: "Feature",
                    properties: {
                        id: location.id,
                        name: location.name // Use the name property for popup
                    },
                    geometry: {
                        type: "Point",
                        coordinates: [location.lng, location.lat] // GeoJSON uses [lng, lat]
                    }
                }))
            };

            // Add the GeoJSON source and layers when the map loads
            map.on('load', async () => {
                try {
                    // Load the PNG image for the marker
                    const image = await loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1200px-Amazon_Web_Services_Logo.svg.png'); // Ensure this URL points to a valid PNG
                    map.addImage('aws', image);

                    // Add a GeoJSON source
                    map.addSource('places', {
                        type: 'geojson',
                        data: geojson
                    });

                    // Add a layer showing the places with custom icons
                    map.addLayer({
                        'id': 'places',
                        'type': 'symbol',
                        'source': 'places',
                        'layout': {
                            'icon-image': 'aws',
                            'icon-size': 0.025, // Adjust as needed
                            'icon-allow-overlap': true // Allow icons to overlap
                        }
                    });

                    // Create a popup
                    const popup = new maplibregl.Popup({
                        closeButton: false,
                        closeOnClick: false
                    });

                    // Event handlers for mouse enter and leave
                    map.on('mouseenter', 'places', (e) => {
                        map.getCanvas().style.cursor = 'pointer';
                        const coordinates = e.features[0].geometry.coordinates.slice();
                        const name = e.features[0].properties.name;

                        // Set popup content and position
                        popup.setLngLat(coordinates).setHTML(name).addTo(map);
                    });

                    map.on('mouseleave', 'places', () => {
                        map.getCanvas().style.cursor = '';
                        popup.remove();
                    });
                } catch (error) {
                    console.error('Error loading image:', error);
                }
            });

            // Helper function to load the image
            async function loadImage(url) {
                return new Promise((resolve, reject) => {
                    const img = new Image();
                    img.crossOrigin = 'anonymous'; // Enable CORS
                    img.onload = () => resolve(img);
                    img.onerror = (error) => reject(error);
                    img.src = url;
                });
            }
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```
