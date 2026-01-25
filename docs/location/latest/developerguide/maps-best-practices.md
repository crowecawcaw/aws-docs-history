# Best practices for Amazon Location Service

When working with Amazon Location Service, adhering to best practices ensures your maps are optimized
for performance, accuracy, and user experience. This section outlines key considerations
for working with static maps, geographical bounds, and GeoJSON data to enhance map
functionality and visualization.

## Dynamic maps

The following are a few best practices for working with dynamic maps in
Amazon Location Service.

### Rendering optimization with

MapLibre

The following are few features of MapLibre which help optimize rendering for
AWS map styles. For more information, see [AWS map styles and features](map-styles.md "map-styles.md").

#### Skip validation of style

If you are using the AWS map style, set `validateStyle` to
`false`. This will turn off load-time style validation,
speeding up the initial map load. Style validation is not needed with AWS
map styles, because they are pre-validated.

Example

```

const map = new maplibregl.Map({
    container: 'map', // ID of the div where the map will render
    style: `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`, // Map style URL
    center: [0, 0], // Starting position [lng, lat]
    zoom: 2, // Starting zoom
    validateStyle: false, // Disable style validation for faster map load
});

```

Explanation

- `validateStyle: true`: This enables
  validation of the map style against the MapLibre GL
  style specification. If there are any issues in the
  style, they'll be logged in the console.
- If you set this to `false`, the map will
  skip the style validation process, which might result in
  faster loading, but without error checking.

#### Pre-warm the map

For single-page applications (SPAs) that may create and destroy the map
many times as the user navigates through the app, the pre-warm function can
reduce delays in re-creating the map after it has been destroyed.

This feature is only recommended for SPAs.

## Static maps

### Bounds, bounding box (box)

When working with maps and geographical data, defining the bounding box
(`bbox`) and bounds parameters accurately is crucial, as they
determine the geographic area of interest. Any inaccuracies can lead to
undesirable results.

**Ensure precise bounds**

Ensure the specified bounds precisely represent the region you
want to display. Even slight inaccuracies can crop or exclude
portions of the desired area, defeating the visualization's
purpose.

**Verify appropriate zoom level**

The map's zoom level is automatically calculated based on the
specified bounds or bbox. Verify that the resulting zoom level
provides appropriate detail and visibility for the entire area of
interest. If the zoom is too high or low, the map may fail to convey
the desired information effectively.

**Check for custom overlay visibility**

When using bbox or bounds with custom overlays like GeoJSON
features, make sure the features' extent falls within the resulting
map image. Features extending beyond the bounds may be clipped or
omitted, leading to incomplete or misleading visualizations.

**Use padding with bbox**

Use the bbox along with the padding parameter to ensure map
features near the edges are fully visible and not cut off.

By accurately defining the bbox and bounds parameters, you can ensure your
maps represent the desired geographic area correctly, provide an appropriate
level of detail, and effectively incorporate custom overlays or data
layers.

## GeoJSON

When using GeoJSON data, optimizing the query string by minifying the GeoJSON can
help you stay within query string limits, especially for large datasets.
