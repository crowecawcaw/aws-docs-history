# Create your first Amazon Location Maps and Places

application

In this section, you will create your first application with Maps and Places.

**Prerequisite:**

If you already created an API key in the [Use the Amazon Location Service console to authenticate](set-up-auth.md "set-up-auth.md") steps, let's
get started.

If you haven't created an API key yet, follow [Use the Amazon Location Service console to authenticate](set-up-auth.md "set-up-auth.md") before
continuing to build the application. If you have any questions, see [Use API keys to authenticate](using-apikeys.md "using-apikeys.md") and [Amazon Location supported regions](location-regions.md "location-regions.md") for more
information.

Here’s a step-by-step tutorial for creating an Amazon Location Service map application with MapLibre GL JS. This guide will walk you through setting up the map, adding styling options, and enabling place search functionality.

In this section, we will set up the initial page and folder structure.

#### Add required libraries and stylesheets

Create an `index.html` file. To render the map, you need MapLibre
GL JS and MapLibre GL Geocoder. You will add the MapLibre and Geocoder
stylesheets and JavaScript scripts.

Copy and paste the following code into your `index.html`
file.

```
<!DOCTYPE html>
<html lang="en">
<head>

    <title>Amazon Location Service - Getting Started with First Map App</title>
    <meta charset='utf-8'>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Interactive map application using Amazon Location Service">

    <!--Link to MapLibre CSS and JavaScript library for map rendering and visualization -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/maplibre-gl@5.x/dist/maplibre-gl.css" />
    <script src="https://cdn.jsdelivr.net/npm/maplibre-gl@5.x/dist/maplibre-gl.js"></script>

    <!--Link to MapLibre Geocoder CSS and JavaScript library for place search and geocoding -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@maplibre/maplibre-gl-geocoder@1.7.0/dist/maplibre-gl-geocoder.css" />
    <script src="https://cdn.jsdelivr.net/npm/@maplibre/maplibre-gl-geocoder@1.7.0/dist/maplibre-gl-geocoder.js"></script>

    <!--Link to amazon-location JavaScript librarie -->
    <script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-utilities-auth-helper@1"></script>
    <script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-client@1.2"></script>

    <!-- Link to the first Amazon Location Map App's CSS and JavaScript -->
    <script src="utils.js"></script>
    <link rel="stylesheet" href="style.css"/>


</head>
<body>
    <main>

    </main>
    <script>
        // Step 1: Setup API Key and AWS Region
        // Step 2.1 Add maps to application
        // Step 2.2 initialize the map
        // Step 3: Add places features to application
        // Step 3.1: Get GeoPlaces instance. It will be used for addion search box and map click functionality
        // Step 3.2: Add search box to the map
        // Step 3.3.: Setup map click functionality
        // Add functions
    </script>
</body>
</html>
```

#### Create the Map container

Under the `<body>` element of the HTML file, create a `<div>` element in your HTML to hold the map. You can style this `<div>` in your CSS to set dimensions as needed for your application. You must download the CSS file, `style.css`, from our GitHub repository. This will help you focus on business logic.

Save the `style.css` and `index.html` files in the same folder.

Download the `style.css` file from [GitHub](https://github.com/aws-geospatial/amazon-location-samples-js/blob/quick_start_sample_js/quick-start/style.css "https://github.com/aws-geospatial/amazon-location-samples-js/blob/quick_start_sample_js/quick-start/style.css").

```
<main role="main" aria-label="Map Container">
    <div id="map"></div>
</main>

```

#### Add API key and AWS Region details

Add the API key you created in [Use API keys to authenticate](using-apikeys.md "using-apikeys.md") to this file,
along with the AWS Region where the key was created.

```
<!DOCTYPE html>
<html lang="en">
.....
.....
<body>
    <main role="main" aria-label="Map Container">
        <div id="map"></div>
    </main>
    <script>
        // Step 1: Setup API Key and AWS Region
        const API_KEY = "Your_API_Key";
        const AWS_REGION = "Region_where_you_created_API_Key";
        // Step 2: Add maps to application
            // Step 2.1 initialize the map
            // Step 2.2 Add navigation controls to the map
        // Step 3: Add places feature to application
            // Step 3.1: Get GeoPlaces instance. It will be used for addion search box and map click functionality
            // Step 3.2: Add search box to the map
            // Step 3.3.: Setup map click functionality
    </script>
</body>
</html>

```

In this section, we will add Map capabilities to the application. Before you
start, your files should be in this folder structure.

If have not already done so, please download the `style.css` file from [GitHub](https://github.com/aws-geospatial/amazon-location-samples-js/blob/quick_start_sample_js/quick-start/style.css "https://github.com/aws-geospatial/amazon-location-samples-js/blob/quick_start_sample_js/quick-start/style.css").

```
|---FirstApp [Folder]
|-------------- index.html [File]
|-------------- style.css [File]
```

#### Create a Function to Initialize the Map

To set up your map, create the following function, `initializeMap(...)`, after the line `//Add functions`.

Choose an initial center location and zoom level. In this example, we set the map center to Vancouver, Canada, with a zoom level of 10. Add navigation controls for easy zooming.

```

/**
 * Initializes the map with the specified style and color scheme.
 */
function initializeMap(mapStyle = "Standard", colorScheme = "Dark") {
     const styleUrl = `https://maps.geo.${AWS_REGION}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${API_KEY}&color-scheme=${colorScheme}`;
     const map = new maplibregl.Map({
         container: 'map',                 // The ID of the map container
         style: styleUrl,                  // The style URL for the map
         center: [-123.116226, 49.246292], // Starting center coordinates
         zoom: 10,                         // Initial zoom level
         validateStyle: false              // Disable style validation
     });
     return map;                           // Return the initialized map
}

```

#### Initialize the Map

Call `initializeMap(...)` to initialize the map. Optionally, you can initialize it with your preferred style
and color scheme after the `initializeMap` function. For more style options, see [AWS map styles and features](map-styles.md "map-styles.md").

```

// Step 1: Setup API Key and AWS Region
const API_KEY = "Your_API_Key";
const AWS_REGION = "Region_where_you_created_API_Key";

// Step 2.1 Add maps to application
// Step 2.2 initialize the map
const map = initializeMap("Standard","Light");

// Step 3: Add places features to application

```

Open `index.html` in a browser to see the map in action.

#### Add Navigation Control

Optionally, you can add navigation controls (zoom and rotation) to the map. This should be done after calling `initializeMap(...)`.

```

// Step 2.1 initialize the map
const map = initializeMap("Standard","Light");

// Step 2.2 Add navigation controls to the map
map.addControl(new maplibregl.NavigationControl());

// Step 3: Add places features to application

```

#### Review the Map Code

Congratulations! Your first app is ready to use a map. Open `index.html` in a browser. Make sure `style.css` is in the same folder as `index.html`.

Your final HTML should look like this:

```

<!DOCTYPE html>
<html lang="en">
<head>

   <title>Amazon Location Service - Getting Started with First Map App</title>
   <meta charset='utf-8'>
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <meta name="description" content="Interactive map application using Amazon Location Service">

   <!-- Link to MapLibre CSS and JavaScript library for map rendering and visualization -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/maplibre-gl@5.x/dist/maplibre-gl.css" />
   <script src="https://cdn.jsdelivr.net/npm/maplibre-gl@5.x/dist/maplibre-gl.js"></script>

   <!-- Link to MapLibre Geocoder CSS and JavaScript library for place search and geocoding -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@maplibre/maplibre-gl-geocoder@1.7.0/dist/maplibre-gl-geocoder.css" />
   <script src="https://cdn.jsdelivr.net/npm/@maplibre/maplibre-gl-geocoder@1.7.0/dist/maplibre-gl-geocoder.js"></script>

   <!-- Link to amazon-location JavaScript library -->
   <script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-utilities-auth-helper@1"></script>
   <script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-client@1.2"></script>

   <!-- Link to the first Amazon Location Map App's CSS and JavaScript -->
   <script src="utils.js"></script>
   <link rel="stylesheet" href="style.css"/>
</head>

<body>
    <main role="main" aria-label="Map Container">
        <div id="map"></div>
    </main>
    <script>
        const API_KEY = "Your_API_Key";
        const AWS_REGION = "Region_where_you_created_API_Key";

        function initializeMap(mapStyle, colorScheme) {
            const styleUrl = `https://maps.geo.${AWS_REGION}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${API_KEY}&color-scheme=${colorScheme}`;

            const map = new maplibregl.Map({
                container: 'map',                 // ID of the HTML element for the map
                style: styleUrl,                  // URL for the map style
                center: [-123.116226, 49.246292], // Initial map center [longitude, latitude]
                zoom: 10                          // Initial zoom level
            });
            map.addControl(new maplibregl.NavigationControl());
            return map;
        }

        const map = initializeMap("Standard", "Light");

    </script>
</body>
</html>

```

In this section, we will set up add places capabilities to the application.
Download the JavaScript file from GitHub, [`utils.js`](https://github.com/aws-geospatial/amazon-location-samples-js/blob/quick_start_sample_js/quick-start/utils.js "https://github.com/aws-geospatial/amazon-location-samples-js/blob/quick_start_sample_js/quick-start/utils.js").

Before you start, your files should be in this folder structure:

```
|---FirstApp [Folder]
|-------------- index.html [File]
|-------------- style.css [File]
|-------------- utils.js [File]
```

#### Create Function to Create GeoPlaces

To add search functionality, initialize the `GeoPlaces` class using `AuthHelper` and `AmazonLocationClient`. Add the following `getGeoPlaces(map)` function before the `</script>` tag in `index.html`.

```

/**
 * Gets a GeoPlaces instance for Places operations.
 */
function getGeoPlaces(map) {
    const authHelper = amazonLocationClient.withAPIKey(API_KEY, AWS_REGION);                      // Authenticate using the API key and AWS region
    const locationClient = new amazonLocationClient.GeoPlacesClient(authHelper.getClientConfig()); // Create a GeoPlaces client
    const geoPlaces = new GeoPlaces(locationClient, map);                                          // Create GeoPlaces instance
    return geoPlaces;                                                                              // Return the GeoPlaces instance
}

```

#### Create Function to Add Search Box to the Application

Add the following `addSearchBox(map, geoPlaces)`, `renderPopup(feature)`, and `createPopup(feature)` functions before the `</script>` tag in `index.html` to complete the search functionality setup.

```

/**
 * Adds search box to the map.
 */
function addSearchBox(map, geoPlaces) {
    const searchBox = new MaplibreGeocoder(geoPlaces, {
        maplibregl,
        showResultsWhileTyping: true,                    // Show results while typing
        debounceSearch: 300,                             // Debounce search requests
        limit: 30,                                       // Limit number of results
        popuprender: renderPopup,                        // Function to render popup
        reverseGeocode: true,                            // Enable reverse geocoding
        zoom: 14,                                        // Zoom level on result selection
        placeholder: "Search text or nearby (lat,long)"  // Placeholder text for search box.
    });

    // Add the search box to the map
    map.addControl(searchBox, 'top-left');

    // Event listener for when a search result is selected
    searchBox.on('result', async (event) => {
        const { id, result_type } = event.result;                     // Get result ID and type
        if (result_type === "Place") {                                // Check if the result is a place
            const placeResults = await geoPlaces.searchByPlaceId(id); // Fetch details for the selected place
            if (placeResults.features.length) {
                createPopup(placeResults.features[0]).addTo(map);     // Create and add popup for the place
            }
        }
    });
}

/**
 * Renders the popup content for a given feature.
 */
function renderPopup(feature) {
    return `
        <div class="popup-content">
            <span class="${feature.place_type.toLowerCase()} badge">${feature.place_type}</span><br>
            ${feature.place_name}
        </div>`;
}

/**
 * Creates a popup for a given feature and sets its position.
 */
function createPopup(feature) {
    return new maplibregl.Popup({ offset: 30 })      // Create a new popup
        .setLngLat(feature.geometry.coordinates)     // Set the popup position
        .setHTML(renderPopup(feature));              // Set the popup content
}

```

#### Add Search Box to the Application

Create a `GeoPlaces` object by calling `getGeoPlaces(map)` as defined in Section 3.1 and then call `addSearchBox(map, geoPlaces)` to add the search box to the application.

```

// Step 2: Add maps to application
// Step 2.1 initialize the map
const map = initializeMap("Standard","Light");
// Step 2.2 Add navigation controls to the map
map.addControl(new maplibregl.NavigationControl());

// Step 3: Add places feature to application
// Step 3.1: Get GeoPlaces instance. It will be used for adding search box and map click functionality
const geoPlaces = getGeoPlaces(map);
// Step 3.2: Add search box to the map
addSearchBox(map, geoPlaces);

```

Your place search is ready to use. Open `index.html` in a browser to see it in action.

#### Add Function to Show Popup on User Click on the Map

Create a function `addMapClick(map, geoPlaces)` to display a popup when the user clicks on the map. Add this function just before the `</script>` tag.

```

/**
 * Sets up reverse geocoding on map click events.
 */
function addMapClick(map, geoPlaces) {
    map.on('click', async ({ lngLat }) => {                     // Listen for click events on the map
        const response = await geoPlaces.reverseGeocode({ query: [lngLat.lng, lngLat.lat], limit: 1, click: true }); // Perform reverse geocoding

        if (response.features.length) {                         // If there are results
            const clickMarker = new maplibregl.Marker({ color: "orange" }); // Create a marker
            const feature = response.features[0];               // Get the clicked feature
            const clickedPopup = createPopup(feature);          // Create popup for the clicked feature
            clickMarker.setLngLat(feature.geometry.coordinates) // Set marker position
                .setPopup(clickedPopup)                         // Attach popup to marker
                .addTo(map);                                    // Add marker to the map

            clickedPopup.on('close', () => clickMarker.remove()).addTo(map); // Remove marker when popup is closed
        }
    });
}

```

#### Call Function to Add Map Click Feature

To enable the map click action, call `addMapClick(map, geoPlaces)` after the line containing `addSearchBox(map, geoPlaces)`.

```

// Step 3: Add places feature to application
// Step 3.1: Get GeoPlaces instance. It will be used for adding search box and map click functionality
const geoPlaces = getGeoPlaces(map);
// Step 3.2: Add search box to the map
addSearchBox(map, geoPlaces);
// Step 3.3: Setup map click functionality
addMapClick(map, geoPlaces);

```

#### Review Maps and Places application

Congratulations! Your first application is ready to use Maps and Places. Open
`index.html` in a browser. Make sure `style.css` and
`utils.js` are in the same folder with `index.html`.

Your final HTML should look like this:

```
<!DOCTYPE html>
<html lang="en">
<head>

   <title>Amazon Location Service - Getting Started with First Map App</title>
    <meta charset='utf-8'>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Interactive map application using Amazon Location Service">

    <!--Link to MapLibre CSS and JavaScript library for map rendering and visualization -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/maplibre-gl@5.x/dist/maplibre-gl.css" />
    <script src="https://cdn.jsdelivr.net/npm/maplibre-gl@5.x/dist/maplibre-gl.js"></script>

    <!--Link to MapLibre Geocoder CSS and JavaScript library for place search and geocoding -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@maplibre/maplibre-gl-geocoder@1.7.0/dist/maplibre-gl-geocoder.css" />
    <script src="https://cdn.jsdelivr.net/npm/@maplibre/maplibre-gl-geocoder@1.7.0/dist/maplibre-gl-geocoder.js"></script>

    <!--Link to amazon-location JavaScript librarie -->
    <script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-utilities-auth-helper@1"></script>
    <script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-client@1.2"></script>

    <!-- Link to the first Amazon Location Map App's CSS and JavaScript -->
    <script src="utils.js"></script>
    <link rel="stylesheet" href="style.css"/>


</head>
<body>
    <main role="main" aria-label="Map Container">
        <div id="map"></div>
    </main>
    <script>
        // Step 1: Setup API Key and AWS Region
        const API_KEY = "Your_API_Key";
        const AWS_REGION = "Region_where_you_created_API_Key";


        // Step 2: Add maps to application
        // Step 2.1 initialize the map
        const map = initializeMap("Standard","Light");
        // Step 2.2 Add navigation controls to the map
        map.addControl(new maplibregl.NavigationControl());

        // Step 3: Add places feature to application
        // Step 3.1: Get GeoPlaces instance. It will be used for addion search box and map click functionality
        const geoPlaces =  getGeoPlaces(map);
        // Step 3.2: Add search box to the map
        addSearchBox(map, geoPlaces);
        // Step 3.3.: Setup map click functionality
        addMapClick(map, geoPlaces);



        /**
         * Functions to add maps and places feature.
         */

         /**
         * Initializes the map with the specified style and color scheme.
         */
        function initializeMap(mapStyle = "Standard", colorScheme = "Dark") {
            const styleUrl = `https://maps.geo.${AWS_REGION}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${API_KEY}&color-scheme=${colorScheme}`;
            const map = new maplibregl.Map({
                container: 'map',                   // The ID of the map container
                style: styleUrl,                    // The style URL for the map
                center: [-123.116226, 49.246292],   // Starting center coordinates
                zoom: 10,                           // Initial zoom level
                validateStyle: false                // Disable style validation
            });
            return map;                             // Return the initialized map
        }

        /**
         * Gets a GeoPlaces instance for Places operations.
         */
        function getGeoPlaces(map) {
            const authHelper =  amazonLocationClient.withAPIKey(API_KEY, AWS_REGION);                      // Authenticate using the API key and AWS region
            const locationClient = new amazonLocationClient.GeoPlacesClient(authHelper.getClientConfig()); // Create a GeoPlaces client
            const geoPlaces = new GeoPlaces(locationClient, map);                                          // Create GeoPlaces instance
                return geoPlaces;                                                                          // Return the GeoPlaces instance
        }

         /**
         * Adds search box to the map.
         */

        function addSearchBox(map, geoPlaces) {
            const searchBox = new MaplibreGeocoder(geoPlaces, {
                maplibregl,
                showResultsWhileTyping: true,                    // Show results while typing
                debounceSearch: 300,                             // Debounce search requests
                limit: 30,                                       // Limit number of results
                popuprender: renderPopup,                        // Function to render popup
                reverseGeocode: true,                            // Enable reverse geocoding
                zoom: 14,                                        // Zoom level on result selection
                placeholder: "Search text or nearby (lat,long)"  // Place holder text for search box.
            });

            // Add the search box to the map
            map.addControl(searchBox, 'top-left');

            // Event listener for when a search result is selected
            searchBox.on('result', async (event) => {
                const { id, result_type } = event.result;                     // Get result ID and type
                if (result_type === "Place") {                                // Check if the result is a place
                    const placeResults = await geoPlaces.searchByPlaceId(id); // Fetch details for the selected place
                    if (placeResults.features.length) {
                        createPopup(placeResults.features[0]).addTo(map);     // Create and add popup for the place
                    }
                }
            });
        }

        /**
         * Renders the popup content for a given feature.
         */
        function renderPopup(feature) {
            return `
                <div class="popup-content">
                    <span class="${feature.place_type.toLowerCase()} badge">${feature.place_type}</span><br>
                    ${feature.place_name}
                </div>`;
        }

        /**
         * Creates a popup for a given feature and sets its position.
         */
        function createPopup(feature) {
            return new maplibregl.Popup({ offset: 30 })      // Create a new popup
                .setLngLat(feature.geometry.coordinates)     // Set the popup position
                .setHTML(renderPopup(feature));              // Set the popup content
        }

        /**
         * Sets up reverse geocoding on map click events.
         */
        function addMapClick(map, geoPlaces) {
            map.on('click', async ({ lngLat }) => {                     // Listen for click events on the map
                const response = await geoPlaces.reverseGeocode({ query: [lngLat.lng, lngLat.lat], limit: 1, click:true }); // Perform reverse geocoding

                if (response.features.length) {                         // If there are results
                    const clickMarker = new maplibregl.Marker({ color: "orange" }); // Create a marker
                    const feature = response.features[0];               // Get the clicked feature
                    const clickedPopup = createPopup(feature);          // Create popup for the clicked feature
                    clickMarker.setLngLat(feature.geometry.coordinates) // Set marker position
                        .setPopup(clickedPopup)                         // Attach popup to marker
                        .addTo(map);                                    // Add marker to the map

                    clickedPopup.on('close', () => clickMarker.remove()).addTo(map); // Remove marker when popup is closed
                }
            });
        }

    </script>
</body>
</html>

```

You have completed the quick start tutorial, and should have an idea of how
Amazon Location Service is used to build applications. To get more out of Amazon Location, you can
check out the following resources:

- **Query suggestion details** - Consider
  extending the `GeoPlaces` class or using a similar approach
  to `ReverseGeocode` to get more details about results
  returned by the `Suggestion` API.
- **Choose the right API for your business needs** - To determine the best Amazon Location API for
  your requirements, check out this resource: [Choose the right API](choose-an-api.md "choose-an-api.md").
- **Check out Amazon Location "how-to"
  guides** - Visit the [Amazon Location Service Developer
  Guide](../../../location.md "../../../location.md") for tutorials and further resources.
- **Documentation and product information**

* For complete documentation, visit the [Amazon Location Service Developer Guide](../../../location.md "../../../location.md") .
  To learn more about the product, go to the [Amazon Location Service Product](https://aws.amazon.com/location "https://aws.amazon.com/location") page.
