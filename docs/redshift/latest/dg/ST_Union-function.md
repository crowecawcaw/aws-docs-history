Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Union

ST_Union returns a geometry representing the union of two geometries.
That is, it merges the input geometries to produce a resulting geometry with no overlaps.

## Syntax

```
ST_Union(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

The spatial reference system identifier (SRID) value of the returned geometry is the SRID value of the input geometries.

If _geom1_ or _geom2_ is null, then null is returned.

If _geom1_ or _geom2_ are empty, then an empty geometry is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geom1_ or _geom2_ is a geometry collection, linestring, or multilinestring, then an error is returned.

If _geom1_ or _geom2_ is not a two-dimensional (2D) geometry, then an error is returned.

## Examples

The following SQL returns the non-empty geometry representing the union of two input geometries.

```
SELECT ST_AsEWKT(ST_Union(ST_GeomFromText('POLYGON((0 0,100 100,0 200,0 0))'), ST_GeomFromText('POLYGON((0 0,10 0,0 10,0 0))')));
```

```

        st_asewkt
-------------------------
 POLYGON((0 0,0 200,100 100,5 5,10 0,0 0))

```
