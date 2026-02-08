# How to create a logistics map

The TravelModes feature lets you build logistic maps using Amazon Location Service. TravelModes displays relevant routing information for Truck navigation with related road restrictions. Use [Transit TravelMode](how-to-show-transit-details-map.md "how-to-show-transit-details-map.md") to show public transportation details.

## Create a map with Truck TravelMode

This example shows how to create a map with `Truck` `TravelMode` for logistic routing.

index.html

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Truck Map</title>
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
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?travel-modes=Truck&key=${apiKey}`,
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
