# How to add an icon on the map

Amazon Location Service enables you to add icons, preferably in PNG format, to the map. You can add
icons to specific geolocations and style them as needed.

## Add a static icon

In this example, you will use an external URL to add an icon to the map using a
symbol layer.

index.html

```

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Static icon on map</title>
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
                const mapStyle = "Standard";  // e.g., Standard, Monochrome, Hybrid, Satellite
                const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
                const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

                const map = new maplibregl.Map({
                    container: 'map', // container id
                    style: styleUrl, // style URL
                    center: [-123.1144289, 49.2806672], // starting position [lng, lat] (e.g., Vancouver)
                    zoom: 12, // starting zoom
                });

                map.on('load', async () => {
                    image = await map.loadImage('https://upload.wikimedia.org/wikipedia/commons/1/1e/Biking_other.png');
                    map.addImage('biking', image.data);
                    map.addSource('point', {
                        'type': 'geojson',
                        'data': {
                            'type': 'FeatureCollection',
                            'features': [
                                {
                                    'type': 'Feature',
                                    'geometry': {
                                        'type': 'Point',
                                        'coordinates': [-123.1144289, 49.2806672]
                                    }
                                }
                            ]
                        }
                    });
                    map.addLayer({
                        'id': 'points',
                        'type': 'symbol',
                        'source': 'point',
                        'layout': {
                            'icon-image': 'biking',
                            'icon-size': 0.25
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
