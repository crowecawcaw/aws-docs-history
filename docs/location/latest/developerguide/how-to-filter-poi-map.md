# How to filter POI on the map

With Amazon Location Service, you can control which points of interest (POIs) appear on your map and how
many are shown. The recommended approach uses the `PoiCategories` and
`PoiDensity` query parameters in the [GetStyleDescriptor](../APIReference/API_geomaps_GetStyleDescriptor.md "../APIReference/API_geomaps_GetStyleDescriptor.md") API. Filtering is configured server-side, so maps
display correctly with no additional client-side code — on web, mobile, and headless
renderers alike.

For styles that do not support these parameters, you can use client-side layer
visibility toggling as a fallback. For more information about supported styles and
values, see [Rich
POI](standard-map-style.md#standard-rich-poi "standard-map-style.md#standard-rich-poi").

Pass `PoiCategories` and `PoiDensity` as query
parameters when requesting the style descriptor. Amazon Location Service returns a style that
renders only the requested categories at the chosen density.

Filter by category
Show only food and transportation POIs:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>POI Category Filter</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css" />
        <script src="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js"></script>
    </head>
    <body style="margin: 0; padding: 0;">
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "YOUR_API_KEY";
            const region = "eu-central-1";
            const mapStyle = "Standard";
            const colorScheme = "Light";

            // Filter to show only FoodAndDrink and Transportation POIs
            // Each category is passed as a separate query parameter
            const styleUrl = `https://maps.geo.${region}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}&color-scheme=${colorScheme}&poi-categories=FoodAndDrink&poi-categories=Transportation`;

            const map = new maplibregl.Map({
                container: "map",
                style: styleUrl,
                center: [-73.966148, 40.781803],
                zoom: 15
            });
        </script>
    </body>
</html>
```

Control density
Reduce POI clutter by setting density to Sparse:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>POI Density Control</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css" />
        <script src="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js"></script>
    </head>
    <body style="margin: 0; padding: 0;">
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "YOUR_API_KEY";
            const region = "eu-central-1";
            const mapStyle = "Standard";
            const colorScheme = "Light";

            // Set POI density to Sparse for a cleaner map
            const poiDensity = "Sparse";

            const styleUrl = `https://maps.geo.${region}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}&color-scheme=${colorScheme}&poi-density=${poiDensity}`;

            const map = new maplibregl.Map({
                container: "map",
                style: styleUrl,
                center: [-73.966148, 40.781803],
                zoom: 15
            });
        </script>
    </body>
</html>
```

Combined
Show only SightsAndMuseums and FoodAndDrink at Dense level — ideal for a tourist map:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>POI Tourist Map</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css" />
        <script src="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js"></script>
    </head>
    <body style="margin: 0; padding: 0;">
        <div id="map" style="width: 100%; height: 100vh;"></div>
        <script>
            const apiKey = "YOUR_API_KEY";
            const region = "eu-central-1";
            const mapStyle = "Standard";
            const colorScheme = "Light";

            // Combine category filtering with density control
            // Each category is passed as a separate query parameter
            const poiDensity = "Dense";

            const styleUrl = `https://maps.geo.${region}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}&color-scheme=${colorScheme}&poi-categories=SightsAndMuseums&poi-categories=FoodAndDrink&poi-density=${poiDensity}`;

            const map = new maplibregl.Map({
                container: "map",
                style: styleUrl,
                center: [-73.966148, 40.781803],
                zoom: 15
            });
        </script>
    </body>
</html>
```

###### Note

The `PoiCategories` and `PoiDensity` parameters
are supported on the Standard and Hybrid styles.

For map styles that do not support server-side POI filtering, you can
toggle MapLibre layer visibility on the client side. This approach requires
knowledge of the specific layer names in the style descriptor.

In this example, you display an interactive map that allows you to filter on
POI categories by toggling layer visibility.

Index.html

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>POI demo</title>
        <meta property="og:description" content="" />
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.css" />
        <link rel='stylesheet' href='style.css' />
        <script src="https://unpkg.com/maplibre-gl@5.x/dist/maplibre-gl.js"></script>

    </head>
    <body>

        <div id="map"></div>
        <ul id="buttons"></ul>
        <script>
            // -------------------------------------------------------------------------------------------
            // Function to set layer state
            // -------------------------------------------------------------------------------------------

            const initialLayerState = {
                Buildings: {
                    layers: ['poi_900_areas_buildings'],
                    visibility: 'visible'
                },
                'Business & Services': {
                    layers: ['poi_700_business_services'],
                    visibility: 'visible'
                },
                Shopping: { layers: ['poi_600_shopping'], visibility: 'visible' },
                'Leisure & Outdoors': {
                    layers: ['poi_550_leisure_outdoor'],
                    visibility: 'visible'
                },
                Facilities: { layers: ['poi_800_facilities'], visibility: 'visible' },
                Transit: { layers: ['poi_400_transit'], visibility: 'visible' },
                'Sights & Museums': {
                    layers: ['poi_300_sights_museums'],
                    visibility: 'visible'
                },
                'Food & Drink': {
                    layers: ['poi_100_food_drink'],
                    visibility: 'visible'
                },
                'Going Out & Entertainment': {
                    layers: ['poi_200_going_out_entertainment'],
                    visibility: 'visible'
                },
                Accommodations: {
                    layers: ['poi_500_accommodations'],
                    visibility: 'visible'
                },
                Parks: { layers: ['poi_landuse_park'], visibility: 'visible' },
                'Public Complexes': {
                    layers: ['poi_landuse_public_complex'],
                    visibility: 'visible'
                }
            };

            // -------------------------------------------------------------------------------------------
            // Setup auth and state
            // -------------------------------------------------------------------------------------------

            let state = { ...initialLayerState };

                const API_KEY = "<api key>"; // check how to create api key for Amazon Location
                const AWS_REGION = "eu-central-1"; // Replace with your AWS region

                const mapStyle = "Standard";
                const colorScheme = "Light";


            // Style URL
            const styleUrl = `https://maps.geo.${AWS_REGION}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${API_KEY}&color-scheme=${colorScheme}`;


            // Render the map with the stylesheet
            map = new maplibregl.Map({
                container: 'map',
                style: styleUrl,
                center: [-73.966148, 40.781803],
                zoom: 17
            });

            const buttonContainer = document.getElementById('buttons');

            for (const category of Object.keys(state)) {
                const newButton = document.createElement('li');
                newButton.classList.add('button');
                newButton.classList.add('active');
                newButton.id = category;

                // Each config has a label
                newButton.textContent = category;

                // On click, we want to switch the value between 'on' and 'off'
                // We could check the config for available options in more complex cases
                newButton.onclick = () => {
                    onClickCategory(category);
                };

                // Append the button to our button container
                buttonContainer.appendChild(newButton);
            }

            // -------------------------------------------------------------------------------------------
            // LAYER VISIBILITY FUNCTION
            // -------------------------------------------------------------------------------------------

            // On click, get the stylesheet, update the language, and set the style
            const onClickCategory = category => {
                const categoryState = state[category];
                const { visibility, layers } = categoryState;

                let nextState;

                // For active button styling
                const activeButton = document.getElementById(category);

                if (visibility === 'visible') {
                    nextState = 'none';
                    activeButton.classList.remove('active');
                } else {
                    nextState = 'visible';
                    activeButton.classList.add('active');
                }

                layers.forEach(id =>
                    map.setLayoutProperty(id, 'visibility', nextState)
                );

                state[category].visibility = nextState;
            };
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
html,
body,
#map {
    height: 100%;
}


#buttons {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: absolute;
    top: 0;
    min-width: 100px;
    max-height: calc(100% - 2rem);
    overflow: auto;
    padding: 1rem;
    background-color: white;
    margin: 0;
}

.button {
    display: inline-block;
    cursor: pointer;
    padding: 8px;
    border-radius: 3px;
    margin-top: 10px;
    font-size: 12px;
    text-align: center;
    color: #fff;
    background: #8a8a8a;
    font-family: sans-serif;
    font-weight: bold;
}

.button:first-child {
    margin-top: 0;
}

.active {
    background: #ee8a65;
}

```
