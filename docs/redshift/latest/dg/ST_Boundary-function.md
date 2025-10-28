Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Boundary

ST_Boundary returns the boundary of an input geometry as follows:

- If the input geometry is empty (that is, it contains no points) it is returned as is.
- If the input geometry is a point or nonempty multipoint, an empty geometry collection is
  returned.
- If the input is a linestring or a multilinestring, then a multipoint containing all the points
  on the boundary is returned. The multipoint might be empty).
- If the input is a polygon that does not have any interior rings, then a closed linestring representing its boundary is returned.
- If the input is a polygon that has interior rings, or is a multipolygon, then a multilinestring is returned.
  The multilinestring contains all the boundaries of all the rings in the areal geometry as closed linestrings.
  To determine point equality, ST_Boundary operates on the 2D projection of the input geometry.
  If the input geometry is empty, a copy of it is returned in the same dimension as the input.
  For nonempty 3DM and 4D geometries, their `m` coordinates are dropped.
  In the special case of 3DZ and 4D multilinestrings, the `z` coordinates of the multilinestring's boundary points
  are computed as the averages of the distinct z-values of the linestring boundary points with the same 2D projection.

## Syntax

```
ST_Boundary(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

If _geom_ is null, then null is returned.

If _geom_ is a `GEOMETRYCOLLECTION`, then an error is returned.

## Examples

The following SQL returns the boundary of the input polygon as a multilinestring.

```
SELECT ST_AsEWKT(ST_Boundary(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0),(1 1,1 2,2 1,1 1))')));
```

```

st_asewkt
--------------------
 MULTILINESTRING((0 0,10 0,10 10,0 10,0 0),(1 1,1 2,2 1,1 1))

```
