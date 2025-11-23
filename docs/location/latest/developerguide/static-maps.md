# Static maps

###### Note

Static maps only support Standard and Satellite styles. For more information, see [AWS map styles and features](map-styles.md "map-styles.md").

Static maps offer a pre-rendered representation of geographic data with the option to
overlay markers (or pins), routes, and polygon areas, as needed for your application. The
Static Map lets you generate static (non-interactive) map images based on customizable
parameters and data inputs. By customizing overlays, shapes, or applying custom styles,
Static Map enables you to create map visualizations that meet specific needs, enhancing the
end-user experience and effectively communicating geographical information. The server
customizes the requested map images and delivers them to the client as JPEG files. You can
programmatically request and generate map images tailored to your specific
requirements.

The _GetStaticMap API_ generates a static image of a map based on
specified parameters like center coordinates, bounding boxes, or overlays. The API allows
customization of map features and style, enabling use in web or mobile applications without
interactive map functionality.

For more information, see [GetStaticMap](../../../latest/APIReference/API_geomaps_GetStaticMap.md "../../../latest/APIReference/API_geomaps_GetStaticMap.md") in the
_Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Static maps](static-maps-how-to.md "static-maps-how-to.md").

## Common use cases

- **Embedded maps in web or mobile application:**
  Static map images can be efficiently embedded in websites or mobile applications
  to provide visualizations of locations, routes, or points of interest with
  non-interactive maps, reducing load times and data usage. Examples include
  search engines (such as Yahoo) showing map images with search results for
  POIs.
- **Location details in e-mails:** Static map
  images can be used to share location information via email to help your end
  users understand the context of the email. For example, food delivery or
  ride-sharing apps use static map images to display pickup/drop-off locations,
  routes, or surrounding areas in post-trip or delivery emails containing bill and
  summary.
- **Marketing materials and printed documents:**
  Customized static map images can be incorporated into brochures, flyers, or
  other printed materials, providing visually appealing representations of
  geographical information relevant to the content.

## Understand the request

The request includes optional URI parameters, like `BoundedPositions`,
`BoundingBox`, and `Center`, among others, to define the
visible area and overlays of the map. The parameters `Height` and
`Width` are required for defining the image size. To learn more, see
[Customize static maps](customizing-static-maps.md "customizing-static-maps.md") and [Overlay on the static map](overlaying-static-map.md "overlaying-static-map.md").

- `BoundedPositions`: Coordinates to encompass in the image.
- `BoundingBox`: Coordinates defining the south-west and north-east
  edges of the map.
- `Height`: Specifies the height of the image.
- `Width`: Specifies the width of the image.
- `GeoJsonOverlay`: A valid GeoJSON object for adding
  overlays.

## Understand the response

The response contains headers like `CacheControl`,
`ContentType`, and `ETag`, and returns the static map as a binary
blob in either JPEG or PNG format. The headers provide metadata like cache control,
content type, and version for static images.

- `CacheControl`: Specifies caching configurations for the map
  image.
- `ContentType`: Indicates the format of the map image (JPEG or
  PNG).
- `ETag`: An identifier for the version of the static map
  image.
- `Blob`: Represents the map image in either JPEG or PNG
  format.
