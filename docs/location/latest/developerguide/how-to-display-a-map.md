# How to display a map

Amazon Location Service allows you to display both interactive and non-interactive maps using our map
styles. See [AWS map styles and features](map-styles.md "map-styles.md") to learn more.

## Interactive map

In this example, you will display an interactive map that allows users to zoom,
pan, pinch, and pitch.

index.html

```

                                    <!DOCTYPE html>
                                    <html lang="en">
                                        <head>
                                            <title>Display a map</title>
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
                                                const mapStyle = "Standard"; // e.g., Standard, Monochrome, Hybrid, Satellite
                                                const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
                                                const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

                                                const map = new maplibregl.Map({
                                                    container: 'map', // container id
                                                    style: styleUrl, // style URL
                                                    center: [25.24, 36.31], // starting position [lng, lat]
                                                    zoom: 2, // starting zoom
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

## Restrict map panning beyond an area

In this example, you will restrict the map from being panned beyond a defined
boundary.

index.html

```

                        <!DOCTYPE html>
                        <html lang="en">
                            <head>
                                <title>Display a map</title>
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
                                    const mapStyle = "Standard"; // e.g., Standard, Monochrome, Hybrid, Satellite
                                    const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
                                    const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

                                    var bounds = [
                                        [90.0, -21.943045533438166], // Southwest coordinates
                                        [146.25, 31.952162238024968] // Northeast coordinates
                                    ];

                                    const map = new maplibregl.Map({
                                        container: 'map', // container id
                                        style: styleUrl, // style URL
                                        maxBounds: bounds, // Sets bounds of SE Asia
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

## Non-interactive map

In this example, you will display a non-interactive map by disabling user
interaction.

index.html

```

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Display a map</title>
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
                const mapStyle = "Standard"; // e.g., Standard, Monochrome, Hybrid, Satellite
                const awsRegion = "eu-central-1"; // e.g., us-east-2, us-east-1, us-west-2, etc.
                const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

                const map = new maplibregl.Map({
                    container: 'map', // container id
                    style: styleUrl, // style URL
                    center: [25.24, 36.31], // starting position [lng, lat]
                    zoom: 2, // starting zoom
                    interactive: false, // Disable pan & zoom handlers
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
