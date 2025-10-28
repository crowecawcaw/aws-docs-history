Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_ConvexHull

ST_ConvexHull returns a geometry that represents the convex hull of the nonempty
points contained in the input geometry.

For empty input, the resulting geometry is the same as the input geometry.
For all nonempty input, the function operates on the 2D projection of the input geometry.
However, the dimension of the output geometry depends on the dimension of the input geometry.
More specifically, when the input geometry is a nonempty 3DM or 3D geometry, `m` coordinates are dropped.
That is, the dimension of the returned geometry is 2D or 3DZ, respectively.
If the input is a nonempty 2D or 3DZ geometry, the resulting geometry has the same dimension.

## Syntax

```
ST_ConvexHull(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

The spatial reference system identifier (SRID) value of the returned geometry is the SRID value of the input geometry.

If _geom_ is null, then null is returned.

The values returned are as follows.

| Number of points on the convex hull | Geometry subtype                                                                                                                                                                         |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                                   | A copy of _geom_ is returned.                                                                                                                                                            |
| 1                                   | A `POINT` subtype is returned.                                                                                                                                                           |
| 2                                   | A `LINESTRING` subtype is returned. The two points of the returned linestring are lexicographically ordered.                                                                             |
| 3 or greater                        | A `POLYGON` subtype with no interior rings is returned. The polygon is clockwise oriented, and the first point of the exterior ring is the lexicographically smallest point of the ring. | ## Examples The following SQL returns the extended well-known text (EWKT) representation of a linestring. In this case, the convex hull returned is a polygon. `SELECT ST_AsEWKT(ST_ConvexHull(ST_GeomFromText('LINESTRING(0 0,1 0,0 1,1 1,0.5 0.5)'))) as output;` `output ------------- POLYGON((0 0,0 1,1 1,1 0,0 0))` The following SQL returns the EWKT representation of a linestring. In this case, the convex hull returned is a linestring. `SELECT ST_AsEWKT(ST_ConvexHull(ST_GeomFromText('LINESTRING(0 0,1 1,0.2 0.2,0.6 0.6,0.5 0.5)'))) as output;` `output ------------- LINESTRING(0 0,1 1)` The following SQL returns the EWKT representation of a multipoint. In this case, the convex hull returned is a point. `SELECT ST_AsEWKT(ST_ConvexHull(ST_GeomFromText('MULTIPOINT(0 0,0 0,0 0)'))) as output;` `output ------------- POINT(0 0)` |
