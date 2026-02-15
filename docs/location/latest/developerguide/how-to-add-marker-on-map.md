# How to add a marker on the map

With Amazon Location, you can add both fixed and draggable markers, and you can also
customize the color of the markers based on your data and preferences.

## Add a fixed marker

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Add marker on a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "<API_KEY>";
            const mapStyle = "Standard";  // e.g., Standard, Monochrome, Hybrid, Satellite
            const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map', // container id
                style: styleUrl, // style URL
                center: [0, 0], // starting position [lng, lat]
                zoom: 1, // starting zoom
            });

            const marker = new maplibregl.Marker() // Create fixed marker
                .setLngLat([85.1376, 25.5941]) // Set coordinates [long, lat] for marker (e.g., Patna, BR, IN)
                .addTo(map); // Add marker to the map
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Add a draggable marker

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Add draggable marker on a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "<API_KEY>";
            const mapStyle = "Standard";  // e.g., Standard, Monochrome, Hybrid, Satellite
            const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map', // container id
                style: styleUrl, // style URL
                center: [0, 0], // starting position [lng, lat]
                zoom: 1, // starting zoom
            });

            const marker = new maplibregl.Marker({ draggable: true }) // Create draggable marker
                .setLngLat([85.1376, 25.5941]) // Set coordinates [long, lat] for marker (e.g., Patna, BR, IN)
                .addTo(map); // Add marker to the map
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Changing marker color

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Adding colorful marker on a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "<API_KEY>";
            const mapStyle = "Monochrome";  // e.g., Standard, Monochrome, Hybrid, Satellite
            const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map', // container id
                style: styleUrl, // style URL
                center: [0, 0], // starting position [lng, lat]
                zoom: 1, // starting zoom
            });

            const marker = new maplibregl.Marker({ color: "black" }) // Create colored marker
                .setLngLat([85.1376, 25.5941]) // Set coordinates [long, lat] for marker (e.g., Patna, BR, IN)
                .addTo(map); // Add marker to the map
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Add multiple markers

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Adding multiple markers on a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div id="map"></div>
        <script>
            const apiKey = "<API_KEY>";
            const mapStyle = "Standard";  // e.g., Standard, Monochrome, Hybrid, Satellite
            const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
            const colorScheme ="Dark"; // e.g., Dark, Light (default)
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?color-scheme=${colorScheme}&key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map', // container id
                style: styleUrl, // style URL
                center: [0, 0], // starting position [lng, lat]
                zoom: 1, // starting zoom
            });

            const locations = [
                { lng: 85.1376, lat: 25.5941, label: 'Patna', color: '#FF5722' },
                { lng: 77.1025, lat: 28.7041, label: 'Delhi', color: '#2196F3' },
                { lng: 77.5946, lat: 12.9716, label: 'Bangalore', color: '#FF9800' },
                { lng: 78.4867, lat: 17.3850, label: 'Hyderabad', color: '#9C27B0' },
                { lng: -87.6298, lat: 41.8781, label: 'Chicago', color: '#4CAF50' },
                { lng: -122.3321, lat: 47.6062, label: 'Seattle', color: '#FFC107' },
                { lng: 4.3517, lat: 50.8503, label: 'Brussels', color: '#3F51B5' },
                { lng: 2.3522, lat: 48.8566, label: 'Paris', color: '#E91E63' },
                { lng: -0.1276, lat: 51.5074, label: 'London', color: '#795548' },
                { lng: 28.0473, lat: -26.2041, label: 'Johannesburg', color: '#673AB7' },
                { lng: -123.1216, lat: 49.2827, label: 'Vancouver', color: '#FF5722' },
                { lng: -104.9903, lat: 39.7392, label: 'Denver', color: '#FF9800' },
                { lng: -97.7431, lat: 30.2672, label: 'Austin', color: '#3F51B5' }
            ];

            // Loop through the locations array and add a marker for each one
            locations.forEach(location => {
                const marker = new maplibregl.Marker({ color: location.color, draggable: true }) // Create colored marker
                    .setLngLat([location.lng, location.lat]) // Set longitude and latitude
                    .addTo(map); // Add marker to the map
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
