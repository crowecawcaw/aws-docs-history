Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeomFromEWKB

ST_GeomFromEWKB constructs a geometry object from the extended well-known binary (EWKB) representation of an input geometry.

ST_GeomFromEWKB accepts 3DZ, 3DM, and 4D geometries written in WKB and EWKB hexadecimal format.

## Syntax

```
ST_GeomFromEWKB(*ewkb\_string*)
```

## Arguments

_ewkb_string_

A value of data type `VARCHAR` that is a hexadecimal EWKB representation of a geometry.

## Return type

`GEOMETRY`

If _ewkb_string_ is null, then null is returned.

If _ewkb_string_ is not valid, then an error is returned.

## Examples

The following SQL constructs a polygon from an EWKB value and returns the EWKT representation of a polygon.

```
SELECT ST_AsEWKT(ST_GeomFromEWKB('0103000020E61000000100000005000000000000000000000000000000000000000000000000000000000000000000F03F000000000000F03F000000000000F03F000000000000F03F000000000000000000000000000000000000000000000000'));
```

```

 st_asewkt
--------------------------------
 SRID=4326;POLYGON((0 0,0 1,1 1,1 0,0 0))

```
