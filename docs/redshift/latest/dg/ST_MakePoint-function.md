Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_MakePoint

ST_MakePoint returns a point geometry whose coordinate values are the input values.

## Syntax

```
ST_MakePoint(*x*, *y*)
```

```
ST_MakePoint(*x*, *y*, *z*)
```

```
ST_MakePoint(*x*, *y*, *z*, *m*)
```

## Arguments

_x_

A value of data type `DOUBLE PRECISION` representing the first coordinate.

_y_

A value of data type `DOUBLE PRECISION` representing the second coordinate.

_z_

A value of data type `DOUBLE PRECISION` representing the third coordinate.

_m_

A value of data type `DOUBLE PRECISION` representing the fourth coordinate.

## Return type

`GEOMETRY` of subtype `POINT`.

The spatial reference system identifier (SRID) value of the returned geometry is
set to 0.

If _x_, _y_, _z_, or _m_ is null, then null is returned.

## Examples

The following SQL returns a `GEOMETRY` type of subtype
`POINT` with the provided coordinates.

```
SELECT ST_AsText(ST_MakePoint(1,3));
```

```

st_astext
-----------
 POINT(1 3)

```

The following SQL returns a `GEOMETRY` type of subtype
`POINT` with the provided coordinates.

```
SELECT ST_AsEWKT(ST_MakePoint(1, 2, 3));
```

```

st_asewkt
----------------
 POINT Z (1 2 3)

```

The following SQL returns a `GEOMETRY` type of subtype
`POINT` with the provided coordinates.

```
SELECT ST_AsEWKT(ST_MakePoint(1, 2, 3, 4));
```

```

st_asewkt
-------------------
 POINT ZM (1 2 3 4)

```
