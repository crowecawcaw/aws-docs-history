Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_EndPoint

ST_EndPoint returns the last point of an input linestring.
The spatial reference system identifier (SRID) value of the result is the same as that of the input geometry.
The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_EndPoint(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `LINESTRING`.

## Return type

`GEOMETRY`

If _geom_ is null, then null is returned.

If _geom_ is empty, then null is returned.

If _geom_ isn't a `LINESTRING`, then null is returned.

## Examples

The following SQL returns an extended well-known text (EWKT) representation of a four-point
`LINESTRING` to a `GEOMETRY` object and returns the end point of the linestring.

```
SELECT ST_AsEWKT(ST_EndPoint(ST_GeomFromText('LINESTRING(0 0,10 0,10 10,5 5,0 5)',4326)));
```

```

st_asewkt
-------------
 SRID=4326;POINT(0 5)

```
