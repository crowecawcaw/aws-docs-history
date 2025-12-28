# How to create topographic maps

Amazon Location Service allows you to create topographic maps using Terrain and Contour density features to visualize elevation changes and geographic characteristics.

## Show Hillshade

The Terrain feature allows you to visualize Hillshade, elevation changes and related geographic features.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Terrain Map</title>
        <meta charset='utf-8'>
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
                <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body style="margin: 0; padding: 0;">
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "Add Your Api Key";
            const mapStyle = "Standard";
            const awsRegion = "us-east-1";

            const map = new maplibregl.Map({
                container: 'map',
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?terrain=Hillshade&key=${apiKey}`,
                center: [-119.5383, 37.8651], // Yosemite coordinates for terrain visibility
                zoom: 12,
                validateStyle: false, // Disable style validation for faster map load
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

## Show elevation with Contour Density lines

Amazon Location Service allows you to add Contour Density features to your map. This provides visualization of geographic steepness and elevation changes.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Contour Map</title>
        <meta charset='utf-8'>
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
                <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body style="margin: 0; padding: 0;">
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "Add Your Api Key";
            const mapStyle = "Standard";
            const awsRegion = "us-east-1";

            const map = new maplibregl.Map({
                container: 'map',
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?contour-density=Medium&key=${apiKey}`,
                center: [-119.3047, 37.7887],
                zoom: 12,
                validateStyle: false, // Disable style validation for faster map load
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

## Show both Hillshade and Contour Density lines

With Amazon Location Service you to combine both Hillshade and Contour Density features on your map for comprehensive terrain visualization. This provides enhanced depth perception and a complete understanding of topographical variations and terrain characteristics.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hillshade and Contour Map</title>
        <meta charset='utf-8'>
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css' />
                <script src='https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js'></script>
    </head>
    <body style="margin: 0; padding: 0;">
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "Add Your Api Key";
            const mapStyle = "Standard";
            const awsRegion = "us-east-1";

            const map = new maplibregl.Map({
                container: 'map',
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?contour-density=Medium&terrain=Hillshade&key=${apiKey}`,
                center: [-119.3047, 37.7887],
                zoom: 12,
                validateStyle: false, // Disable style validation for faster map load
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
