Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeomFromText

ST_GeomFromText constructs a geometry object from a well-known text (WKT) representation of an input geometry.

ST_GeomFromText accepts 3DZ, 3DM, and 4D where the geometry type is prefixed with Z, M, or ZM, respectively.

## Syntax

```
ST_GeomFromText(*wkt\_string*)
```

```
ST_GeomFromText(*wkt\_string*, *srid*)
```

## Arguments

_wkt_string_

A value of data type `VARCHAR` that is a WKT representation of a geometry.

You can use the WKT keyword `EMPTY` to designate an empty
point, a multipoint with an empty point, or a geometry collection with an empty
point. The following example creates a multipoint with one empty and one
nonempty point.

```
ST_GeomFromEWKT('MULTIPOINT(1 0,EMPTY)');
```

_srid_

A value of data type `INTEGER` that is a spatial reference
identifier (SRID). If an SRID value is provided, the returned geometry has this
SRID value. Otherwise, the SRID value of the returned geometry is set to zero
(0).

## Return type

`GEOMETRY`

If _wkt_string_ or _srid_ is null, then null is returned.

If _srid_ is negative, then null is returned.

If _wkt_string_ is not valid, then an error is returned.

If _srid_ is not valid, then an error is returned.

## Examples

The following SQL constructs a geometry object from the WKT representation and SRID value.

```
SELECT ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))',4326);
```

```

st_geomfromtext
--------------------------------
0103000020E61000000100000005000000000000000000000000000000000000000000000000000000000000000000F03F000000000000F03F000000000000F03F000000000000F03F000000000000000000000000000000000000000000000000

```
