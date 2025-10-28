Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeoHash

ST_GeoHash returns the `geohash` representation of the input point with the specified precision.
The default precision value is 20.
For more information about the definition of geohash, see [Geohash](https://en.wikipedia.org/wiki/Geohash "https://en.wikipedia.org/wiki/Geohash") in Wikipedia.

## Syntax

```
ST_GeoHash(*geom*)
```

```
ST_GeoHash(*geom*, *precision*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

_precision_

A value of data type `INTEGER`.
The default is 20.

## Return type

`GEOMETRY`

The function returns the `geohash` representation of the input point.

If the input point is empty, the function returns null.

If the input geometry is not a point, the function returns an error.

## Examples

The following SQL returns the geohash representation of the input point.

```
SELECT ST_GeoHash(ST_GeomFromText('POINT(45 -45)'), 25) AS geohash;
```

```
          geohash
---------------------------
 m000000000000000000000gzz


```

The following SQL returns null because the input point is empty.

```
SELECT ST_GeoHash(ST_GeomFromText('POINT EMPTY'), 10) IS NULL AS result;
```

```
 result
---------
 true


```
