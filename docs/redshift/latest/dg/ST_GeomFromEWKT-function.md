Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeomFromEWKT

ST_GeomFromEWKT constructs a geometry object from the extended well-known text (EWKT) representation of an input geometry.

ST_GeomFromEWKT accepts 3DZ, 3DM, and 4D where the geometry type is prefixed with Z, M, or ZM, respectively.

## Syntax

```
ST_GeomFromEWKT(*ewkt\_string*)
```

## Arguments

_ewkt_string_

A value of data type `VARCHAR` or an expression that evaluates to a `VARCHAR` type,
that is an EWKT representation of a geometry.

You can use the WKT keyword `EMPTY` to designate an empty
point, a multipoint with an empty point, or a geometry collection with an empty
point. The following example creates an empty point.

```
ST_GeomFromEWKT('SRID=4326;POINT EMPTY');
```

## Return type

`GEOMETRY`

If _ewkt_string_ is null, then null is returned.

If _ewkt_string_ is not valid, then an error is returned.

## Examples

The following SQL constructs a multilinestring from an EWKT value and returns a geometry.
It also returns the ST_AsEWKT result of the geometry.

```
SELECT ST_GeomFromEWKT('SRID=4326;MULTILINESTRING((1 0,1 0),(2 0,3 0),(4 0,5 0,6 0))') as geom, ST_AsEWKT(geom);
```

```

                                                                                                                                                       geom                                                                                                                                                       |                          st_asewkt
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------
 0105000020E610000003000000010200000002000000000000000000F03F0000000000000000000000000000F03F00000000000000000102000000020000000000000000000040000000000000000000000000000008400000000000000000010200000003000000000000000000104000000000000000000000000000001440000000000000000000000000000018400000000000000000 | SRID=4326;MULTILINESTRING((1 0,1 0),(2 0,3 0),(4 0,5 0,6 0))

```
