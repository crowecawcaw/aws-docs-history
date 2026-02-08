# How to show real-time traffic on a map

Using Amazon Location Service you can add traffic features to your map. This provides real-time traffic data to show current traffic conditions such as current road congestion, construction, and incidents, helping you make routing choices.

## Make a map with real-time traffic

This example shows how to create a map with real-time traffic data.

index.html

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Traffic Map</title>
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
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?traffic=All&key=${apiKey}`,
                center: [-74.0060 ,40.7128], // New York City coordinates for traffic visibility
                zoom: 12,
                validateStyle: false, // Disable style validation for faster map load
            });
        </script>
    </body>
</html>
```

style.css

```
body {
    margin: 0;
    padding: 0;
}

#map {
    width: 100%;
    height: 100vh;
}
```
