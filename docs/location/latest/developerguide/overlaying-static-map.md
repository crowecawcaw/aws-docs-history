# Overlay on the static map

This section explains how to overlay additional information onto static maps using
Amazon Location Service. You can customize your static maps by adding various geographical features,
such as points, lines, and polygons, to enhance the map's visual representation.
Amazon Location Service supports multiple formats, including GeoJSON and a compact overlay format, to
provide flexible and efficient ways of adding overlays.

For more information, see [GetStaticMap](../../../latest/APIReference/API_geomaps_GetStaticMap.md "../../../latest/APIReference/API_geomaps_GetStaticMap.md") in the
_Amazon Location Service API Reference_.

## With GeoJSON

GeoJSON is a versatile format that allows you to overlay custom data on static
maps. By defining geographical features such as points, lines, and polygons, you can
enhance the visual representation of your maps, providing valuable context for
users. GeoJSON is widely supported and offers flexibility when it comes to styling
and customizing map overlays, making it an ideal format for displaying regions,
plotting routes, or showing spatial relationships.

With Amazon Location Service, you can leverage GeoJSON to add dynamic, location-based features
directly onto your static maps. This enables you to create highly customizable
overlays that can be tailored to meet your specific business needs. GeoJSON supports
several geometry types, including `Point`, `LineString`,
`Polygon`, and `MultiPolygon`, allowing you to display a
wide range of features, from markers and routes to complex area
representations.

## Colors

When styling GeoJSON features, you have flexibility in defining colors. You can
specify colors using different formats, such as hexadecimal values (like #ff0000 for
red) or with alpha transparency (like #ff000080 for semi-transparent red). This
ensures your overlays can be visually consistent with the map style. If no color is
specified, the default color for the selected map style will be applied.

## Drawing order

Custom overlays are drawn in a specific order to maintain clarity and avoid visual
clutter. In Amazon Location Service, overlay features like polygons, lines, and points will appear
above the base map, but below map labels. The drawing order prioritizes polygons
first, followed by lines, and then points or markers.

## Measurement units

For properties like `width` and `outline-width`, you can use
different measurement units to specify size, including pixels (px), meters (m),
kilometers (km), miles (mi), and percentages (%). The percentage unit adjusts the
property relative to a default value, providing more flexibility in styling your
overlays.

## Geometry types

Amazon Location Service supports multiple GeoJSON geometry types, such as `Point`,
`LineString`, `Polygon`, and `MultiPolygon`.
Each geometry type can be styled and adjusted using the properties object in
GeoJSON, allowing for extensive customization of markers, routes, and areas on your
map.

## With compact overlay

###### Note

Compact overlay supports the following geometry types: point, line, and
polygon. It doesn't support `multiPoint`, `multiLine`, or
`multiPolgyon`.

The compact overlay option allows you to efficiently display multiple geometries
on a static map by using a single query parameter. This streamlined approach
simplifies the request format and reduces the size of the request, making it easier
to transmit overlay data. Customers can input various geometry types and their
corresponding style properties in one query parameter, and Amazon Location Service will handle the
heavy lifting by parsing and rendering the overlay as specified.

While using the compact overlay format, keep in mind that there are limits on the
size of the request URL. Although Amazon Location Service optimizes the query, ensure that your
request stays within reasonable limits, especially when dealing with multiple
geometries and their associated properties.

## Format

The compact overlay format is structured as follows:
`geometry_type:geometry;property_1=value_1;property_2=value_2|geometry_type:geometry;property_1=value_1...`

Each geometry type is defined along with its style properties. Multiple geometries
are separated by a pipe operator (|), and properties for each geometry are separated
using a semicolon.

## Supported geometry

types

Amazon Location Service supports several geometry types, including `Point`,
`MultiPoint`, `LineString`, `Polygon`, and
`MultiPolygon`. These geometry types can be combined and styled
within the same query parameter using the compact overlay format.

## Styling

properties

Each geometry can be customized using various style properties, such as color,
outline color, size, and more. These properties allow you to control the appearance
of each geometry on the map, ensuring that the overlay aligns with your business
requirements.
