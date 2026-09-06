

# How to create a 3D map
<a name="how-to-create-a-3d-map"></a>

Amazon Location Service lets you add three-dimensional features to maps, such as `Terrain3D` to display elevation data as a three-dimensional surface, or `Buildings3D` to display urban structures with height and volume. 

## Create a map with three-dimensional terrain details
<a name="how-to-show-3d-terrain-map"></a>

This example shows how to create a map with `Terrain3D` parameter. 

### Terrain3D example
<a name="how-to-show-3d-terrain-map-code"></a>

------
#### [ index.html ]

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

------
#### [ style.css ]

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

------

## Create a map with three-dimensional buildings details
<a name="how-to-show-3d-buildings-map"></a>

This example shows how to create a map with `Buildings3D` parameter. 

### Buildings3D example
<a name="how-to-show-3d-buildings-map-code"></a>

------
#### [ index.html ]

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

------
#### [ style.css ]

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

------

## Enable/disable Globe view
<a name="how-to-enable-disable-globe-view"></a>

This example shows how to enable or disable the Globe view projection. By default, Globe view is enabled. 

### Globe view example
<a name="how-to-enable-disable-globe-view-code"></a>

------
#### [ index.html ]

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Globe View</title>
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
                `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`,
                center: [-74.5, 40],
                zoom: 2,
                validateStyle: false, // Disable style validation for faster map load
            });

            map.on('style.load', () => {
                // Globe view is enabled by default
                // To disable globe view, uncomment the next line:
                // map.setProjection({});
            });
        </script>
    </body>
</html>
```

------
#### [ style.css ]

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

------