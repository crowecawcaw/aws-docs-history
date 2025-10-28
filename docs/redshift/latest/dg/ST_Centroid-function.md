Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Centroid

ST_Centroid returns a point that represents a centroid of a geometry as follows:

- For `POINT` geometries, it returns the point whose coordinates are the average of the coordinates of the points in the geometry.
- For `LINESTRING` geometries, it returns the point whose coordinates are the weighted average of the midpoints
  of the segments of the geometry, where the weights are the lengths of the segments of the geometry.
- For `POLYGON` geometries, it returns the point whose coordinates are the weighted average of the centroids of a triangulation of the areal geometry where the weights are the areas of the triangles in the triangulation.
- For geometry collections, it returns the weighted average of the centroids of the geometries of maximum topological dimension in the geometry collection.

## Syntax

```
ST_Centroid(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

If _geom_ is null, then null is returned.

If _geom_ is empty, then null is returned.

## Examples

The following SQL returns central point of an input linestring.

```
SELECT ST_AsEWKT(ST_Centroid(ST_GeomFromText('LINESTRING(110 40, 2 3, -10 80, -7 9, -22 -33)', 4326)))
```

```

                     st_asewkt
----------------------------------------------------
 SRID=4326;POINT(15.6965103455214 27.0206782881905)

```
