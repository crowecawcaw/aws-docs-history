# How to show transit details on a map

Amazon Location Service lets you add transit features to maps. The `Transit` `TravelMode` displays routing information for public transit, such as color-coded train lines. Also check how to set [logistics TravelMode](how-to-create-logistic-map.md "how-to-create-logistic-map.md") for additional options.

## Create a map with transit details

This example shows how to create a map with transit details with Transit TravelMode for public transportation.

index.html

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Transit Map</title>
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
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?travel-modes=Transit&key=${apiKey}`,
                center: [-74.0060 ,40.7128],
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
