# How to set style features for a

map

Amazon Location Service enables you to set style features to customize your map. You can add terrain,
contour density, traffic, and travel mode features to your map.

- **Terrain**: Enable topographic visualization to show
  elevation changes and geographic features, helping users understand the physical
  landscape of their mapped areas.
- **ContourDensity**: Adjust contour lines density levels to
  display terrain steepness and elevation changes.
- **Traffic**: Overlay real-time traffic data to show current
  traffic conditions such as current road congestion, construction, and incidents,
  enabling informed routing decisions.
- **TravelMode**: Select transportation-specific layers to
  display relevant routing information for public transit or truck navigation with
  road restrictions.
  In this example, you will create a map with check boxes to visualize terrain
  and contour lines individually or simultaneously.

Index.html

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Terrain and Contour Map</title>
        <meta charset='utf-8'>
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
                <style>
            .controls {
                position: absolute;
                top: 10px;
                left: 10px;
                background: white;
                padding: 10px;
                border-radius: 5px;
                z-index: 1000;
            }
        </style>
                <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <div class="controls">
            <label><input type="checkbox" id="terrain" checked> Terrain</label><br>
                <label><input type="checkbox" id="contour" checked> Contour Lines</label>
        </div>
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "Add Your Api Key";
            const mapStyle = "Standard";
            const awsRegion = "us-east-1";

            let terrainEnabled = true;
            let contourEnabled = true;

            function updateMap() {
                // Built-in JavaScript API that handles URL query parameters
                const params = new URLSearchParams({ key: apiKey });

                if (terrainEnabled) params.append('terrain', 'Hillshade');
                if (contourEnabled) params.append('contour-density', 'Medium');

                const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?${params}`;
                map.setStyle(styleUrl);
            }

            const map = new maplibregl.Map({
                container: 'map',
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?terrain=Hillshade&contour-density=Medium&key=${apiKey}`,
                center: [-119.5383, 37.8651], // Yosemite coordinates for terrain visibility
                zoom: 10,
            });

            document.getElementById('terrain').addEventListener('change', (e) => {
                terrainEnabled = e.target.checked;
                updateMap();
            });

            document.getElementById('contour').addEventListener('change', (e) => {
                contourEnabled = e.target.checked;
                updateMap();
            });
        </script>
    </body>
</html>

```

In this example, you will create a map with the truck travel mode layer
enabled to show truck-specific routing information and road restrictions.

Index.html

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Truck routing map</title>
        <meta charset='utf-8'>
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
                <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
    </head>
    <body>
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "Add Your Api Key";
            const mapStyle = "Standard";
            const awsRegion = "us-east-1";

            const truckMapStyleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?travel-modes=Truck&key=${apiKey}`;

            const map = new maplibregl.Map({
                container: 'map',
                style: truckMapStyleUrl,
                center: [-74.0060, 40.7128], // NYC coordinates
                zoom: 12,
            });
        </script>
    </body>
</html>

```
