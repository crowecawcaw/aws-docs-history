# How to show 3D features on a map

Amazon Location Service lets you add three-dimensional features to maps, such as `Terrain3D` to display elevation data as a
three-dimensional surface, or `Buildings3D` to display urban structures with height and volume.

## Create a map with three-dimensional terrain details

This example shows how to create a map with `Terrain3D` parameter.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>3D Terrain</title>
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
                style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?terrain=Terrain3D&key=${apiKey}`,
                center: [7.6583, 45.9763],
                zoom: 12,
                pitch: 60, // Tilt angle (0-85 degrees)
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

## Create a map with three-dimensional buildings details

This example shows how to create a map with `Buildings3D` parameter.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>3D Buildings</title>
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
                style:
                `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?buildings=Buildings3D&key=${apiKey}`,
                center: [7.6583, 45.9763],
                zoom: 12,
                pitch: 60, // Tilt angle (0-85 degrees)
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
