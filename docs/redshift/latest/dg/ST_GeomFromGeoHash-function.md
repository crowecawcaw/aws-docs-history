Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeomFromGeoHash

ST_GeomFromGeoHash constructs a geometry object from the geohash representation of an input geometry.
ST_GeomFromGeoHash returns a two-dimensional (2D) geometry with the spatial reference identifier (SRID) of zero (0).
For more information about the geohash format, see [Geohash](https://en.wikipedia.org/wiki/Geohash "https://en.wikipedia.org/wiki/Geohash") in Wikipedia.

## Syntax

```
ST_GeomFromGeoHash(*geohash\_string*)
```

```
ST_GeomFromGeoHash(*geohash\_string*, *precision*)
```

## Arguments

_geohash_string_

A value of data type `VARCHAR` or an expression that evaluates to a `VARCHAR` type,
that is a geohash representation of a geometry.

_precision_

A value of data type `INTEGER` that represents the precision of the geohash.
The value is the number of characters of the geohash to be used as precision. If the value is not specified, less than zero,
or greater than the _geohash_string_ length. then the _geohash_string_ length is used.

## Return type

`GEOMETRY`

If _geohash_string_ is null, then null is returned.

If _geohash_string_ is not valid, then an error is returned.

## Examples

The following SQL returns a polygon with high precision.

```
SELECT ST_AsText(ST_GeomFromGeoHash('9qqj7nmxncgyy4d0dbxqz0'));
```

```

 st_asewkt
-----------------------
 POLYGON((-115.172816 36.114646,-115.172816 36.114646,-115.172816 36.114646,-115.172816 36.114646,-115.172816 36.114646))

```

The following SQL returns a point with high precision.

```
SELECT ST_AsText(ST_GeomFromGeoHash('9qqj7nmxncgyy4d0dbxqz00'));
```

```

 st_asewkt
-----------------------
 POINT(-115.172816 36.114646)

```

The following SQL returns a polygon with low precision.

```
SELECT ST_AsText(ST_GeomFromGeoHash('9qq'));
```

```

 st_asewkt
-----------------------
 POLYGON((-115.3125 35.15625,-115.3125 36.5625,-113.90625 36.5625,-113.90625 35.15625,-115.3125 35.15625))

```

The following SQL returns a polygon with precision 3.

```
SELECT ST_AsText(ST_GeomFromGeoHash('9qqj7nmxncgyy4d0dbxqz0', 3));
```

```

 st_asewkt
-----------------------
 POLYGON((-115.3125 35.15625,-115.3125 36.5625,-113.90625 36.5625,-113.90625 35.15625,-115.3125 35.15625))

```
