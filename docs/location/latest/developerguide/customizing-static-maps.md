# Customize static maps

###### Note

Static maps only support the Satellite style. For more information, see [AWS map styles and features](map-styles.md "map-styles.md").

This section provides an overview of how to customize static maps generated using
Amazon Location Service. It covers various features, such as adjusting the map's position, size,
language, scale, overlays, and attribution, enabling you to tailor the map to your
specific requirements.

For more information, see [GetStaticMap](../APIReference/API_geomaps_GetStaticMap.md "../APIReference/API_geomaps_GetStaticMap.md") in the
_Amazon Location Service API Reference_.

## Position

The position allows you to define the center and boundaries of the map. You can
control the map's focus by setting the center coordinates, a bounding box, or using
a zoom level to determine how much area to display. To learn how it works, see [How to get a static map of a specific position](get-static-map-specific-position.md "get-static-map-specific-position.md").

- `Center`: Defines the center point of the map using longitude
  and latitude coordinates.
- `Radius`: Specifies the radius (distance from the center) that
  will be displayed on the static map.
- `Bounding Box`: Defines a rectangular area of the map, set by
  providing the coordinates of the top-left and bottom-right corners.
- `Zoom`: Controls the zoom level of the map. Higher zoom levels
  show more detail in a smaller area, while lower zoom levels show less detail
  over a larger area.

## Dimension and

quality

You can customize the size and visual quality of the static map by defining its
dimensions (height and width) and adding padding for better presentation of markers
and other elements. To learn how it works, see [How to get a static map of a specific dimension](get-static-map-specific-dimension.md "get-static-map-specific-dimension.md").

- `Height and Width`: Specifies the size of the static map image
  by defining its height and width in pixels.
- `Padding`: Adds extra space around the edges of the map,
  allowing for better visualization when placing markers, lines, or
  shapes.

## Scale

The scale provides control over the scale of the map and defines the units
(kilometers, miles) to measure distances. This is useful for accurately representing
the map's size and distance relationships. To learn how it works, see [How to add scale for a static map](add-scale-static-map.md "add-scale-static-map.md").

- `Scale Unit`: Defines the units for the map's scale bar (for
  example, kilometers or miles), allowing users to accurately gauge distances
  on the map.

## Overlay

You can add markers, lines to show routes, polygons to show areas, and more. To
learn how it works, see [How to add a marker to a static map](add-marker-static-map.md "add-marker-static-map.md"), [How to add a line to a static map](how-to-add-line-static.md "how-to-add-line-static.md"), or [How to add a route to a static map](how-to-add-route.md "how-to-add-route.md").
