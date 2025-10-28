# How to add a polygon on the map

Amazon Location Service allows you to add polygons to the map. You can style the polygon based on
your business needs, including adding fill and border styling.

## Add a polygon

In this example, you will add a polygon to the map and style it with a fill color
and a border.

index.html

```

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Overlay a Polygon on a Map</title>
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
                    center: [-123.13203602550998, 49.28726257639254],
                    zoom: 16
                });

                map.on('load', () => {
                    map.addSource('barclayHeritageSquare', {
                        type: 'geojson',
                        data: barclayHeritageSquare
                    });

                    map.addLayer({
                        id: 'barclayHeritageSquare-fill',
                        type: 'fill',
                        source: 'barclayHeritageSquare',
                        layout: {},
                        paint: {
                            'fill-color': '#008296',
                            'fill-opacity': 0.25
                        }
                    });

                    map.addLayer({
                        id: 'barclayHeritageSquare-outline',
                        type: 'line',
                        source: 'barclayHeritageSquare',
                        layout: {},
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

    const barclayHeritageSquare = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "park_id": 200,
                    "park_name": "Barclay Heritage Square",
                    "area_ha": 0.63255076039675,
                    "park_url": "http://covapp.vancouver.ca/parkfinder/parkdetail.aspx?inparkid=200"
                },
                "geometry": {
                    "type": "MultiPolygon",
                    "coordinates": [
                        [
                            [-123.1320948511985, 49.287379401361406],
                            [-123.13179672786798, 49.2871908081159],
                            [-123.13148154587924, 49.28739992437733],
                            [-123.1313830551372, 49.28733617069321],
                            [-123.13118648745055, 49.287208851500054],
                            [-123.13128257706838, 49.28714532642171],
                            [-123.13147941881572, 49.28727228533418],
                            ...
                            [-123.13177619357138, 49.28759081706052],
                            [-123.1320948511985, 49.287379401361406]
                        ]
                    ]
                }
            }
        ]
    };

```
