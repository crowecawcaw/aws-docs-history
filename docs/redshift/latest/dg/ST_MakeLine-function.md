Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_MakeLine

ST_MakeLine creates a linestring from the input geometries.

The dimension of the returned geometry is the same as that of the input geometries. Both input geometries must of the same dimension.

## Syntax

```
ST_MakeLine(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`POINT`, `LINESTRING`, or `MULTIPOINT`.

_geom2_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`POINT`, `LINESTRING`, or `MULTIPOINT`.

## Return type

`GEOMETRY` of subtype `LINESTRING`.

If _geom1_ or _geom2_ is null, then null is returned.

If _geom1_ and _geom2_ is the empty point or contains empty points,
then these empty points are ignored.

If _geom1_ and _geom2_ are empty,
then the empty `LINESTRING` is returned.

The spatial reference system identifier (SRID) value of the returned geometry is
the SRID value of the input geometries.

If _geom1_ and _geom2_ have different SRID
values, then an error is returned.

If _geom1_ or _geom2_ is not a `POINT`, `LINESTRING`, or `MULTIPOINT`, then an error is returned.

If _geom1_ and _geom2_ have different dimensions, then an error is returned.

## Examples

The following SQL constructs a linestring from two input linestrings.

```
SELECT ST_MakeLine(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'), ST_GeomFromText('LINESTRING(88.29 39.07,88.42 39.26,88.27 39.31,88.29 39.07)'));
```

```

st_makeline
-----------
 010200000008000000C3F5285C8F52534052B81E85EB113D407B14AE47E15A5340C3F5285C8F423D40E17A14AE475153408FC2F5285C4F3D40C3F5285C8F52534052B81E85EB113D40C3F5285C8F125640295C8FC2F58843407B14AE47E11A5640E17A14AE47A14340E17A14AE4711564048E17A14AEA74340C3F5285C8F125640295C8FC2F5884340

```
