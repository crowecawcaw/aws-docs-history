Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_IsClosed

ST_IsClosed returns true if the 2D projection of the input geometry is closed. The following rules define
a closed geometry:

- The input geometry is a point or a multipoint.
- The input geometry is a linestring, and the start and end points of the linestring coincide.
- The input geometry is a nonempty multilinestring and all its linestrings are closed.
- The input geometry is a nonempty polygon, all polygon's rings are nonempty, and the start and
  end points of all its rings coincide.
- The input geometry is a nonempty multipolygon and all its polygons are closed.
- The input geometry is a nonempty geometry collection and all its components are closed.

## Syntax

```
ST_IsClosed(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom_ is an empty point, then false is returned.

If _geom_ is null, then null is returned.

## Examples

The following SQL checks if the polygon is closed.

```
SELECT ST_IsClosed(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'));
```

```

st_isclosed
-----------
 true

```
