Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_MemSize

ST_MemSize returns the amount of memory space (in bytes) used by the input geometry.
This size depends on the Amazon Redshift internal representation of the geometry and thus can change if the internal
representation changes. You can use this size as an indication of the relative size of geometry objects in Amazon Redshift.

## Syntax

```
ST_MemSize(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER` representing the inherent dimension of _geom_.

If _geom_ is null, then null is returned.

## Examples

The following SQL returns the memory size of a geometry collection.

```
SELECT ST_MemSize(ST_GeomFromText('GEOMETRYCOLLECTION(POLYGON((0 0,10 0,0 10,0 0)),LINESTRING(20 10,20 0,10 0))'))::varchar + ' bytes';
```

```

 ?column?
-----------
 172 bytes

```
