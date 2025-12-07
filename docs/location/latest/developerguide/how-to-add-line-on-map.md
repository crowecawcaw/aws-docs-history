# How to add a line on the map

With Amazon Location Service, you can add both pre-recorded GPS traces as line-strings and real-time
GPS traces to dynamic maps.

## Adding a pre-recorded line

In this example, you will add a pre-recorded GPS trace as a GeoJSON (main.js) to
the dynamic map. To do so, you need to add a source (like GeoJSON) and a layer with
line styling of your choice to the map.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Add a line on the map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
        <script src='main.js'></script>
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
                center: [-123.126575, 49.290585],
                zoom: 12.5
            });

            map.on('load', () => {
                map.addSource('vancouver-office-to-stanley-park-route', {
                    type: 'geojson',
                    data: routeGeoJSON
                });

                map.addLayer({
                    id: 'vancouver-office-to-stanley-park-route',
                    type: 'line',
                    source: 'vancouver-office-to-stanley-park-route',
                    layout: {
                        'line-cap': 'round',
                        'line-join': 'round'
                    },
                    paint: {
                        'line-color': '#008296',
                        'line-width': 2
                    }
                });
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

main.js

```

const routeGeoJSON = {
    type: "FeatureCollection",
    features: [
        {
            type: "Feature",
            geometry: {
                type: "LineString",
                coordinates: [
                    [-123.117011, 49.281306],
                    [-123.11785, 49.28011],
                    ...
                    [-123.135735, 49.30106]
                ]
            },
            properties: {
                name: "Amazon YVR to Stanley Park",
                description: "An evening walk from Amazon office to Stanley Park."
            }
        }
    ]
};

```

## Add a line in real-time

In this example, you will simulate adding new GPS coordinates one by one to create
a real-time GPS trace. This is useful for tracking real-time data updates.

index.html

```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Add a line on the map in real-time</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <link rel='stylesheet' href='style.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
        <script src='main.js'></script>
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
                center: [-123.126575, 49.290585],
                zoom: 12.5
            });

            map.on('load', () => {
                const coordinates = routeGeoJSON.features[0].geometry.coordinates;
                routeGeoJSON.features[0].geometry.coordinates = [coordinates[0], coordinates[20]];

                map.addSource('vancouver-office-to-stanley-park-route', {
                    type: 'geojson',
                    data: routeGeoJSON
                });

                map.addLayer({
                    id: 'vancouver-office-to-stanley-park-route',
                    type: 'line',
                    source: 'vancouver-office-to-stanley-park-route',
                    layout: {
                        'line-cap': 'round',
                        'line-join': 'round'
                    },
                    paint: {
                        'line-color': '#008296',
                        'line-width': 2
                    }
                });

                map.jumpTo({center: coordinates[0], zoom: 14});
                map.setPitch(30);

                let i = 0;
                const timer = window.setInterval(() => {
                    if (i < coordinates.length) {
                        routeGeoJSON.features[0].geometry.coordinates.push(coordinates[i]);
                        map.getSource('vancouver-office-to-stanley-park-route').setData(routeGeoJSON);
                        map.panTo(coordinates[i]);
                        i++;
                    } else {
                        window.clearInterval(timer);
                    }
                }, 100);
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

main.js

```

const routeGeoJSON = {
    type: "FeatureCollection",
    features: [
        {
            type: "Feature",
            geometry: {
                type: "LineString",
                coordinates: [
                    [-123.117011, 49.281306],
                    [-123.11785, 49.28011],
                    ...
                    [-123.135735, 49.30106]
                ]
            },
            properties: {
                name: "Amazon YVR to Stanley Park",
                description: "An evening walk from Amazon office to Stanley Park."
            }
        }
    ]
};

```

## Developer tips

**Fitting bounds:** You can fit the line to the map
bounds by calculating the bounds of the line's coordinates:

```

const coordinates = routeGeoJSON.features[0].geometry.coordinates;
const bounds = coordinates.reduce((bounds, coord) => bounds.extend(coord), new maplibregl.LngLatBounds(coordinates[0], coordinates[0]));
map.fitBounds(bounds, { padding: 20 });

```
