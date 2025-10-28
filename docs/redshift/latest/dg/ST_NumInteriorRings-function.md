Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_NumInteriorRings

ST_NumInteriorRings returns the number of rings in an input polygon geometry.

## Syntax

```
ST_NumInteriorRings(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER`

If _geom_ is null, then null is returned.

If _geom_ is not a polygon, then null is returned.

## Examples

The following SQL returns the number of interior rings in the input polygon.

```
SELECT ST_NumInteriorRings(ST_GeomFromText('POLYGON((0 0,100 0,100 100,0 100,0 0),(1 1,1 5,5 1,1 1),(7 7,7 8,8 7,7 7))'));
```

```

 st_numinteriorrings
-------------
 2

```
