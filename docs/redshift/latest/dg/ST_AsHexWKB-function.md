Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_AsHexWKB

ST_AsHexWKB returns the hexadecimal well-known binary (WKB) representation of an input geometry or geography using ASCII hexadecimal characters (0–9, A–F).
For 3DZ, 3DM, and 4D geometries or geographies, ST_AsHexWKB uses the Open Geospatial Consortium (OGC) standard value for the geometry or geography type.

## Syntax

```
ST_AsHexWKB(*geo*)
```

## Arguments

_geo_

A value of data type `GEOMETRY` or `GEOGRAPHY`, or an expression that
evaluates to a `GEOMETRY` or `GEOGRAPHY` type.

## Return type

`VARCHAR`

If _geo_ is null, then null is returned.

If the result is larger than a 64-KB `VARCHAR`, then an error is
returned.

## Examples

The following SQL returns the hexadecimal WKB representation of a polygon in a geometry.

```
SELECT ST_AsHexWKB(ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))',4326));
```

```

st_ashexwkb
--------------------------------
01030000000100000005000000000000000000000000000000000000000000000000000000000000000000F03F000000000000F03F000000000000F03F000000000000F03F000000000000000000000000000000000000000000000000

```

The following SQL returns the hexadecimal WKB representation of a polygon in a geography.

```
SELECT ST_AsHexWKB(ST_GeogFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))'));
```

```

st_ashexwkb
--------------------------------
01030000000100000005000000000000000000000000000000000000000000000000000000000000000000F03F000000000000F03F000000000000F03F000000000000F03F000000000000000000000000000000000000000000000000

```
