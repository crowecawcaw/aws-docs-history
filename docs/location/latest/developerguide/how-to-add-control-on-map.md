# How to add control on the map

Amazon Location Service allows you to add multiple controls to the map, including navigation,
geolocation, fullscreen, scale, and attribution controls.

- **Navigation control**: Contains zoom buttons and
  a compass.
- **Geolocate control**: Provides a button that
  uses the browser's geolocation API to locate the user on the map.
- **Fullscreen control**: Contains a button for
  toggling the map in and out of fullscreen mode.
- **Scale control**: Displays the ratio of a
  distance on the map to the corresponding distance on the ground.
- **Attribution control**: Presents the map's
  attribution information. By default, the attribution control is expanded
  (regardless of map width).
  You can add the controls to any corner of the map: top-left, bottom-left,
  bottom-right, or top-right.

## Adding map controls

In the following example, you'll add the map controls listed above.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Map Controls</title>
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
            const mapStyle = "Standard"; // e.g., Standard, Monochrome, Hybrid, Satellite
            const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map', // container id
                style: styleUrl, // style URL
                center: [-123.13203602550998, 49.28726257639254], // starting position [lng, lat]
                zoom: 10, // starting zoom
                attributionControl: false, // hide default attributionControl in bottom left
            });

            // Adding controls to the map
            map.addControl(new maplibregl.NavigationControl()); // Zoom and rotation controls
            map.addControl(new maplibregl.FullscreenControl()); // Fullscreen control
            map.addControl(new maplibregl.GeolocateControl()); // Geolocation control
            map.addControl(new maplibregl.AttributionControl(), 'bottom-left'); // Attribution in bottom-left
            map.addControl(new maplibregl.ScaleControl(), 'bottom-right'); // Scale control in bottom-right
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body, #map { height: 100%; }

```

## Developer tips

```

new maplibregl.NavigationControl({
    showCompass: true, // show or hide compass (default: true)
    showZoom: true // show or hide zoom controls (default: true)
});

```

```

new maplibregl.GeolocateControl({
    positionOptions: { enableHighAccuracy: true }, // default: false
    trackUserLocation: true // default: false
});

```

```

new maplibregl.AttributionControl({
    compact: true, // compact (collapsed) mode (default: false)
});

```

```

new maplibregl.ScaleControl({
    maxWidth: 100, // width of the scale (default: 50)
    unit: 'imperial' // imperial or metric (default: metric)
});

```

```

map.addControl(new maplibregl.FullscreenControl({
    container: document.querySelector('body') // container for fullscreen mode
}));

```
