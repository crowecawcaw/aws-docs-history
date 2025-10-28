Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_MakePolygon

ST_MakePolygon has two variants that return a polygon. One takes a single geometry,
and another takes two geometries.

- The input of the first variant is a linestring that defines the outer ring of the output polygon.
- The input of the second variant is a linestring and a multilinestring. Both of these are empty
  or closed.

The boundary of the exterior ring of the output polygon is the input
linestring, and the boundaries of the interior rings of the polygon are the
linestrings in the input multilinestring. If the input linestring is empty, an empty
polygon is returned. Empty linestrings in the multilinestring are disregarded. The
spatial reference system identifier (SRID) of the resulting geometry is the common
SRID of the two input geometries.
The dimension of the returned geometry is the same as that of the input geometries.
The exterior ring and interior rings must of the same dimension.

## Syntax

```
ST_MakePolygon(*geom1*)
```

```
ST_MakePolygon(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`LINESTRING`. The _linestring_ value must be
closed or empty.

_geom2_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`MULTILINESTRING`.

## Return type

`GEOMETRY` of subtype `POLYGON`.

The spatial reference system identifier (SRID) of the returned geometry is equal
to the SRID of the inputs.

If _geom1_, or _geom2_ is null, then null is returned.

If _geom1_ is not a linestring, then an error is returned.

If _geom2_ is not a multilinestring, then an error is returned.

If _geom1_ is not closed, then an error is returned.

If _geom1_ is a single point or is not closed, then an error is returned.

If _geom2_ contains at least one linestring that has a single point or is not closed, then an error is returned.

If _geom1_ and _geom2_ have different SRID values, then an error is returned.

If _geom1_ and _geom2_ have different dimensions, then an error is returned.

## Examples

The following SQL returns a polygon from an input linestring.

```
SELECT ST_AsText(ST_MakePolygon(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)')));
```

```

 st_astext
---------------
POLYGON((77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07))

```

The following SQL creates a polygon from a closed linestring and a closed
multilinestring. The linestring is used for the exterior ring of the polygon. The
linestrings in the multilinestrings are used for the interior rings of the polygon.

```
SELECT ST_AsEWKT(ST_MakePolygon(ST_GeomFromText('LINESTRING(0 0,10 0,10 10,0 10,0 0)'), ST_GeomFromText('MULTILINESTRING((1 1,1 2,2 1,1 1),(3 3,3 4,4 3,3 3))')));
```

```

 st_astext
----------------------------------
POLYGON((0 0,10 0,10 10,0 10,0 0),(1 1,1 2,2 1,1 1),(3 3,3 4,4 3,3 3))

```
