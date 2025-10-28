# Use Amazon Location MapLibre Geocoder GL

plugin

The Amazon Location MapLibre geocoder plugin is designed to make it easier for you
to incorporate Amazon Location functionality into your JavaScript applications,
when working with map rendering and geocoding using the
[maplibre-gl-geocoder](https://github.com/maplibre/maplibre-gl-geocoder "https://github.com/maplibre/maplibre-gl-geocoder") library.

## Installation

Install Amazon Location MapLibre geocoder plugin from NPM for usage with modules. Type this
command:

```
npm install @aws/amazon-location-for-maplibre-gl-geocoder
```

You can also import HTML and CSS files for usage directly in the
browser with a script:

```
<script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-for-maplibre-gl-geocoder@2"></script>
<link
  href="https://cdn.jsdelivr.net/npm/@aws/amazon-location-for-maplibre-gl-geocoder@2/dist/amazon-location-for-mlg-styles.css"
  rel="stylesheet"
/>
```

## Usage with module - standalone GeoPlaces SDK

This example uses the [AWS SDK for JavaScript
V3](https://github.com/aws/aws-sdk-js-v3 "https://github.com/aws/aws-sdk-js-v3") to get a GeoPlacesClient to provide to the library and
[AuthHelper](https://github.com/aws-geospatial/amazon-location-utilities-auth-helper-js "https://github.com/aws-geospatial/amazon-location-utilities-auth-helper-js") for authenticating the GeoPlacesClient. It
enables all APIs for the geocoder.

```
// Import MapLibre GL JS
import maplibregl from "maplibre-gl";
// Import from the AWS JavaScript SDK V3
import { GeoPlacesClient } from "@aws-sdk/client-geo-places";
// Import the utility functions
import { withAPIKey } from "@aws/amazon-location-utilities-auth-helper";
// Import the AmazonLocationMaplibreGeocoder
import {
  buildAmazonLocationMaplibreGeocoder,
  AmazonLocationMaplibreGeocoder,
} from "@aws/amazon-location-for-maplibre-gl-geocoder";

const apiKey = "<API Key>";
const mapName = "Standard";
const region = "<Region>"; // region containing Amazon Location API Key

// Create an authentication helper instance using an API key and region
const authHelper = await withAPIKey(apiKey, region);

const client = new GeoPlacesClient(authHelper.getClientConfig());

// Render the map
const map = new maplibregl.Map({
  container: "map",
  center: [-123.115898, 49.295868],
  zoom: 10,
  style: `https://maps.geo.${region}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`,
});

// Gets an instance of the AmazonLocationMaplibreGeocoder Object.
const amazonLocationMaplibreGeocoder = buildAmazonLocationMaplibreGeocoder(client, { enableAll: true });

// Now we can add the Geocoder to the map.
map.addControl(amazonLocationMaplibreGeocoder.getPlacesGeocoder());
```

## Usage with a browser - standalone GeoPlaces SDK

This example uses the Amazon Location client to make a request that
authenticates using an API key.

###### Note

Some of these example use the Amazon Location GeoPlacesClient. This client is based on the [AWS SDK for
JavaScript V3](https://github.com/aws/aws-sdk-js-v3 "https://github.com/aws/aws-sdk-js-v3") and allows for making calls to Amazon Location
through a script referenced in an HTML file.

Include the following in an HTML file:

```
<!-- Import the Amazon Location For Maplibre Geocoder -->
<script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-for-maplibre-gl-geocoder@2"></script>
<link
  href="https://cdn.jsdelivr.net/npm/@aws/amazon-location-for-maplibre-gl-geocoder@2/dist/amazon-location-for-mlg-styles.css"
  rel="stylesheet"
/>
<!-- Import the Amazon GeoPlacesClient -->
<script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-client@1"></script>
```

Include the following in a JavaScript file:

```
const apiKey = "<API Key>";
const mapStyle = "Standard";
const region = "<Region>"; // region containing Amazon Location API key

// Create an authentication helper instance using an API key and region
const authHelper = await amazonLocationClient.withAPIKey(apiKey, region);

const client = new amazonLocationClient.GeoPlacesClient(authHelper.getClientConfig());

// Render the map
const map = new maplibregl.Map({
  container: "map",
  center: [-123.115898, 49.295868],
  zoom: 10,
  style: `https://maps.geo.${region}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`,
});

// Initialize the AmazonLocationMaplibreGeocoder object
const amazonLocationMaplibreGeocoderObject = amazonLocationMaplibreGeocoder.buildAmazonLocationMaplibreGeocoder(
  client,
  { enableAll: true },
);

// Use the AmazonLocationWithMaplibreGeocoder object to add a geocoder to the map.
map.addControl(amazonLocationMaplibreGeocoderObject.getPlacesGeocoder());
```

## Functions

Listed below are the functions used in the Amazon Location MapLibre geocoder
plugin:

- `buildAmazonLocationMaplibreGeocoder`

This class creates an instance of the
`AmazonLocationMaplibreGeocder`, which is the entry point to
the other all other calls.

Using standalone `GeoPlacesClient` API calls (client is
instance of `GeoPlacesClient`):

```
const amazonLocationMaplibreGeocoder = buildAmazonLocationMaplibreGeocoder(client, { enableAll: true });
```

Using consolidated `LocationClient` API calls (client is instance of `LocationClient`):

```
const amazonLocationMaplibreGeocoder = buildAmazonLocationMaplibreGeocoder(client, {
  enableAll: true,
  placesIndex: placeIndex,
});
```

- `getPlacesGeocoder`

Returns a ready-to-use IControl object that can be added directly to a
map.

```
const geocoder = getPlacesGeocoder();

// Initialize map see: <insert link to initializing a map instance here>
let map = await initializeMap();

// Add the geocoder to the map.
map.addControl(geocoder);
```
