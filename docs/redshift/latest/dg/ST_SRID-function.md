Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_SRID

ST_SRID returns the spatial reference system identifier (SRID) of an input geometry.

For more information about an SRID, see
[Querying spatial data in Amazon Redshift](geospatial-overview.md "geospatial-overview.md").

## Syntax

```
ST_SRID(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER` representing the SRID value of _geom_.

If _geom_ is null, then null is returned.

## Examples

The following SQL returns an SRID value of a linestring that is set to SRID `4326`.

```
SELECT ST_SRID(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)',4326));
```

```

st_srid
-------------
 4326

```

The following SQL returns an SRID value of a linestring that is not set when constructed. This results in `0` for the SRID value.

```
SELECT ST_SRID(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
```

```

st_srid
-------------
 0

```
