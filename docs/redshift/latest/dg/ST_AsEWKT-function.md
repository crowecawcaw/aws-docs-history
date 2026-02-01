Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_AsEWKT

ST_AsEWKT returns the extended well-known text (EWKT) representation of an input geometry or geography.
For 3DZ, 3DM, and 4D geometries, ST_AsEWKT appends Z, M, or ZM to the WKT value for the geometry type.

## Syntax

```
ST_AsEWKT(*geo*)
```

```
ST_AsEWKT(*geo*, *precision*)
```

## Arguments

_geo_

A value of data type `GEOMETRY` or `GEOGRAPHY`, or an expression that evaluates to a `GEOMETRY` or `GEOGRAPHY` type.

_precision_

A value of data type `INTEGER`. For geometries, the coordinates of _geo_
are displayed using the specified precision 1–20. If
_precision_ is not specified, the default is 15.
For geographies, the coordinates of _geo_
are displayed using the specified precision. If
_precision_ is not specified, the default is 15.

## Return type

`VARCHAR`

If _geo_ is null, then null is returned.

If _precision_ is null, then null is returned.

If the result is larger than a 64-KB `VARCHAR`, then an error is
returned.

## Examples

The following SQL returns the EWKT representation of a linestring.

```
SELECT ST_AsEWKT(ST_GeomFromText('LINESTRING(3.141592653589793 -6.283185307179586,2.718281828459045 -1.414213562373095)', 4326));
```

```

st_asewkt
--------------------------------
 SRID=4326;LINESTRING(3.14159265358979 -6.28318530717959,2.71828182845905 -1.41421356237309)

```

The following SQL returns the EWKT representation of a linestring. The coordinates of the geometries are displayed with six digits of precision.

```
SELECT ST_AsEWKT(ST_GeomFromText('LINESTRING(3.141592653589793 -6.283185307179586,2.718281828459045 -1.414213562373095)', 4326), 6);
```

```

st_asewkt
--------------------------------
 SRID=4326;LINESTRING(3.14159 -6.28319,2.71828 -1.41421)

```

The following SQL returns the EWKT representation of a geography.

```
SELECT ST_AsEWKT(ST_GeogFromText('LINESTRING(110 40, 2 3, -10 80, -7 9)'));
```

```

                  st_asewkt
----------------------------------------------
 SRID=4326;LINESTRING(110 40,2 3,-10 80,-7 9)

```
