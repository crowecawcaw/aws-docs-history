# Creating point maps

You can create point maps in Quick Suite to show the difference between data
values for each location by size. Each point on this type of map corresponds to a
geographic location in your data, such as a country, state or province, or city. The
size of the points on the map represents the magnitude of the field in the
**Size** field well, in relation to other values in the same
field. The color of the points represents the values in the
**Color** field well. The field values in the
**Color** field well display in the legend, if you choose a
field for color.

Use the following procedure to create a point map in Quick Suite.

To create point maps in Quick Suite, make sure that you have the
following:

- One geospatial field (such as country, state or region, county or
  district, city, or ZIP code or postal code). Or you can use one latitude
  field and one longitude field.
- One numeric field (measure) for size.
- (Optional) A categorical field (dimension) for color.
  For information on formatting geospatial maps, see [Map and geospatial chart
  formatting options](../../../quicksight/latest/user/geospatial-formatting.md "../../../quicksight/latest/user/geospatial-formatting.md").

## Creating point maps

###### To create a point map

1. Add a new visual to your analysis. For more information about starting
   analyses, see [Starting an analysis in Quick Sight](creating-an-analysis.md "creating-an-analysis.md"). For more information about
   adding visuals to analyses, see [Adding a visual](creating-a-visual.md#create-a-visual "creating-a-visual.md#create-a-visual").
2. For **Visual type**, choose the **Points on
   map** icon. It looks like a globe with a point on
   it.
3. Drag a geographic field from the **Fields list** pane
   to the **Geospatial** field well, for example
   `Country`. You can also choose a latitude or longitude
   field.

A point map appears with a point for each location in your
data.

If the field is part of a geographic hierarchy, the hierarchy displays
in the field well. 4. Drag a measure from the **Fields list** pane to the
**Size** field well.

The points on the map update to show the magnitude of values for each
location. 5. (Optional) Drag a dimension from the **Fields list**
pane to the **Color** field well.

Each point updates to show a point for each categorical value in the
dimension.
