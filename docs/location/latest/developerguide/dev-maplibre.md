# Use MapLibre tools and related libraries with Amazon Location

[MapLibre](https://maplibre.org/ "https://maplibre.org/") is primarily a rendering
engine for displaying maps in a web or mobile application. However, it also includes
support for plug-ins and provides functionality for working with other aspects of
Amazon Location. The following describes tools that you can use, based on the area or location
that you want to work with.

###### Note

To use any aspect of Amazon Location, install the [AWS SDK for the language that you
want to use](dev-by-language.md "dev-by-language.md").

- **Maps**

To display maps in your application, you need a map rendering engine that
will use the data provided by Amazon Location, and draw to the screen. Map
rendering engines also provide functionality to pan and zoom the map, or to
add markers or pushpins and other annotations to the map.

Amazon Location Service recommends rendering maps using the [MapLibre](https://github.com/maplibre/maplibre-gl-js "https://github.com/maplibre/maplibre-gl-js")
rendering engine. MapLibre GL JS is an engine for displaying maps in
JavaScript, while MapLibre Native provides maps for either iOS or
Android.

MapLibre also has a plug-in ecosystem to extend the core functionality.
For more information, visit [https://maplibre.org/maplibre-gl-js/docs/plugins/](https://maplibre.org/maplibre-gl-js/docs/plugins/ "https://maplibre.org/maplibre-gl-js/docs/plugins/").

- **Places search**

To make creating a search user interface simpler, you can use the [MapLibre geocoder](https://github.com/maplibre/maplibre-gl-geocoder "https://github.com/maplibre/maplibre-gl-geocoder")
for web (Android applications can use the [Android Places plug-in](https://github.com/maplibre/maplibre-plugins-android/tree/master/plugin-places "https://github.com/maplibre/maplibre-plugins-android/tree/master/plugin-places")).

Use the [Amazon Location for MapLibre geocoder library](https://github.com/aws-geospatial/amazon-location-for-maplibre-gl-geocoder?tab=readme-ov-file "https://github.com/aws-geospatial/amazon-location-for-maplibre-gl-geocoder?tab=readme-ov-file") to simplify the process of
using Amazon Location with `amazon-location-for-maplibre-gl-geocoder` in
JavaScript Applications.

For more information, see [Use Amazon Location MapLibre Geocoder GL
plugin](dev-maplibre-geocoder.md "dev-maplibre-geocoder.md").

- **Routes**
- **Geofences and Trackers**

MapLibre doesn't have any specific rendering or tools for geofences and tracking,
but you can use the rendering functionality and [plug-ins](https://maplibre.org/maplibre-gl-js/docs/plugins/ "https://maplibre.org/maplibre-gl-js/docs/plugins/") to
show the geofences and tracked devices on the map.

The devices being tracked can use [MQTT](tracking-using-mqtt.md "tracking-using-mqtt.md") or
manually send updates to Amazon Location Service. Geofence events can be responded to using [AWS Lambda](../../../lambda.md "../../../lambda.md").
Many open source libraries are available to provide additional functionality for
Amazon Location Service, for example [Turf](https://github.com/Turfjs/turf "https://github.com/Turfjs/turf") which provide
spatial analysis functionality.

Many libraries use the open standard [GeoJSON](https://geojson.org/ "https://geojson.org/") formatted data. Amazon Location Service provides a library to convert responses
into GeoJSON for use in JavaScript applications. For more information, see [SDKs and frameworks for Amazon Location Service](dev-sdks.md "dev-sdks.md").
