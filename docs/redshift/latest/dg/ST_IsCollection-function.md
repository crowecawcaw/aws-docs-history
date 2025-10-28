Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_IsCollection

ST_IsCollection returns true if the input geometry is one of the following subtypes: `GEOMETRYCOLLECTION`, `MULTIPOINT`, `MULTILINESTRING`, or `MULTIPOLYGON`.

## Syntax

```
ST_IsCollection(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom_ is null, then null is returned.

## Examples

The following SQL checks if the polygon is a collection.

```
SELECT ST_IsCollection(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'));
```

```

st_iscollection
-----------
 false

```
