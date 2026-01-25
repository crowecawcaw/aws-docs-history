# How to set the political view of a

map

Amazon Location Service enables you to set the political view to ensure your application complies
with local laws. You can set a political view and compare maps from different political
perspectives.

###### Note

For more information, see [Localization and internationalization](maps-localization-internationalization.md "maps-localization-internationalization.md").

## Set political view and compare with

international perspective

In this example, you will create and compare maps from two different political
views: an international perspective and Turkey's view on Cyprus.

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
        <script src="https://unpkg.com/@mapbox/mapbox-gl-sync-move@0.3.1"></script>
        <script src='main.js'></script>
    </head>
    <body>
        <!-- Map container -->
        <div class="maps">
        <div id="internationalView"></div>
        <div id="turkeyView"></div>
        </div>
        <script>

            const apiKey = "Add Your Api Key";
            const mapStyle = "Standard";
            const awsRegion = "eu-central-1";

            // International perspective without political-view query parameter
            const internationalViewMapStyleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

            // Turkey perspective with political-view query parameter
            const turkeyViewMapStyleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?political-view=TUR&key=${apiKey}`;

            const internationalViewMap = new maplibregl.Map({
                container: 'internationalView', // container id
                style: internationalViewMapStyleUrl, // style URL
                center: [33.0714561, 35.1052139], // starting position [lng, lat]
                zoom: 7.5,
            });

            const turkeyViewMap = new maplibregl.Map({
                container: 'turkeyView', // container id
                style: turkeyViewMapStyleUrl, // style URL
                center: [33.0714561, 35.1052139],
                zoom: 7.5,
            });

            // Sync map zoom and center
            syncMaps(internationalViewMap, turkeyViewMap);

            // Informational popup for international view
            new maplibregl.Popup({closeOnClick: false})
                .setLngLat([33, 35.5])
                .setHTML('<h4>International view <br> recognizes <br> Cyprus</h4>')
                .addTo(internationalViewMap);

            // Informational popup for Turkey's view
            new maplibregl.Popup({closeOnClick: false})
                .setLngLat([33, 35.5])
                .setHTML('<h4>Turkey does not <br> recognize <br> Cyprus</h4>')
                .addTo(turkeyViewMap);
        </script>
    </body>
</html>

```

style.css

```

body { margin: 0; padding: 0; }
html, body { height: 100%; }
#internationalView, #turkeyView { height: 100%; width: 100%; }
.maps {
    display: flex;
    width: 100%;
    height: 100%;
}

```
