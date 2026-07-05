Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_StartPoint

ST\_StartPoint returns the first point of an input linestring. The spatial reference
system identifier (SRID) value of the result is the same as that of the input geometry.
The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_StartPoint(*geom*)
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
`LINESTRING` to a `GEOMETRY` object and returns the start point of the linestring.

```
SELECT ST_AsEWKT(ST_StartPoint(ST_GeomFromText('LINESTRING(0 0,10 0,10 10,5 5,0 5)',4326)));
```

```

st_asewkt
-------------
 SRID=4326;POINT(0 0)

```
