Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_NumGeometries

ST_NumGeometries returns the number of geometries in an input geometry.

## Syntax

```
ST_NumGeometries(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER` representing the number of geometries in _geom_.

If _geom_ is null, then null is returned.

If _geom_ is a single empty geometry, then `0` is returned.

If _geom_ is a single nonempty geometry, then `1` is returned.

If _geom_ is a `GEOMETRYCOLLECTION` or a `MULTI` subtype,
then the number of geometries is returned.

## Examples

The following SQL returns the number of geometries in the input multilinestring.

```
SELECT ST_NumGeometries(ST_GeomFromText('MULTILINESTRING((0 0,1 0,0 5),(3 4,13 26))'));
```

```

st_numgeometries
-------------
 2

```
