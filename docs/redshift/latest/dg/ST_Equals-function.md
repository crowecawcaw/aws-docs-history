Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Equals

ST_Equals returns true if the 2D projections of the input geometries are geometrically equal. Geometries
are considered geometrically equal if they have equal point sets and their interiors have a
nonempty intersection.

## Syntax

```
ST_Equals(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type. This value is compared with _geom1_ to determine if it is equal to _geom1_.

## Return type

`BOOLEAN`

If _geom1_ or _geom2_ is null, then an error is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geom1_ or _geom2_ is a geometry collection, then an error is returned.

## Examples

The following SQL checks if the two polygons are geometrically equal.

```
SELECT ST_Equals(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'), ST_GeomFromText('POLYGON((-1 3,2 1,0 -3,-1 3))'));
```

```

st_equals
-----------
 false


```

The following SQL checks if the two linestrings are geometrically equal.

```
SELECT ST_Equals(ST_GeomFromText('LINESTRING(1 0,10 0)'), ST_GeomFromText('LINESTRING(1 0,5 0,10 0)'));
```

```

st_equals
-----------
 true


```
