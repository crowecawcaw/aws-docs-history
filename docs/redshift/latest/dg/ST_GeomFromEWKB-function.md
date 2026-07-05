Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_GeomFromEWKB

ST\_GeomFromEWKB constructs a geometry object from the extended well-known binary (EWKB) representation of an input geometry.

ST\_GeomFromEWKB accepts 3DZ, 3DM, and 4D geometries written in WKB and EWKB hexadecimal format.

## Syntax

```
ST_GeomFromEWKB(*ewkb\_string*)
```

## Arguments

_ewkb\_string_

A value of data type `VARCHAR` that is a hexadecimal EWKB representation of a geometry.

## Return type

`GEOMETRY`

If _ewkb\_string_ is null, then null is returned.

If _ewkb\_string_ is not valid, then an error is returned.

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
