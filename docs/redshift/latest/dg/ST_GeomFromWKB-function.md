Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeomFromWKB

ST_GeomFromWKB constructs a geometry object from a hexadecimal well-known binary (WKB) representation of an input geometry.

ST_GeomFromWKB accepts 3DZ, 3DM, and 4D geometries written in WKB hexadecimal format.

## Syntax

```
ST_GeomFromWKB(*wkb\_string*)
```

```
ST_GeomFromWKB(*wkb\_string*, *srid*)
```

## Arguments

_wkb_string_

A value of data type `VARCHAR` that is a hexadecimal WKB representation of a geometry.

_srid_

A value of data type `INTEGER` that is a spatial reference identifier (SRID).
If an SRID value is provided, the returned geometry has this SRID value.
Otherwise, the SRID value of the returned geometry is set to 0.

## Return type

`GEOMETRY`

If _wkb_string_ or _srid_ is null, then null is returned.

If _srid_ is negative, then null is returned.

If _wkb_string_ is not valid, then an error is returned.

If _srid_ is not valid, then an error is returned.

## Examples

The following SQL constructs a polygon from a WKB value and returns the WKT representation of a polygon.

```
SELECT ST_AsText(ST_GeomFromWKB('01030000000100000005000000000000000000000000000000000000000000000000000000000000000000F03F000000000000F03F000000000000F03F000000000000F03F000000000000000000000000000000000000000000000000'));

```

```

 st_astext
--------------------------------
 POLYGON((0 0,0 1,1 1,1 0,0 0))

```
