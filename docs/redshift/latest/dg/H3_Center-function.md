Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# H3\_Center

H3\_Center returns the centroid of an H3 cell ID from an input index.
For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_Center(*index*)
```

## Arguments

_index_

A value of data type `BIGINT` or `VARCHAR` that represents the index of an H3 cell. Or, an expression that
evaluates to one of these data types.

## Return type

`POINT` – represents the centroid of the H3 cell with spatial reference system identifier (SRID) of `0`.

If _index_ is not valid, then an error is returned.

## Examples

The following SQL inputs a `VARCHAR` that represents the index of an H3 cell, and returns a POINT with SRID of 0 that represents the centroid of the input H3 cell.

```
SELECT H3_Center('8025fffffffffff');
```

```

 h3_center
--------------------------------------------
 010100000070707A550B605940AEE9D70B327E4640

```

The following SQL inputs a `BIGINT` that represents the index of an H3 cell, and returns a POINT with SRID 0 that represents the centroid of the input H3 cell.

```
SELECT H3_Center(577129255373111295);
```

```

 h3_center
--------------------------------------------
 010100000070707A550B605940AEE9D70B327E4640

```

The following SQL inputs a `VARCHAR` that represents the index of an H3 cell, and returns a POINT with SRID 0 that represents the centroid of the input H3 cell.
The output of H3\_Center is input to ST\_AwEWKT to display in extended well-known text (EWKT) representation.

```
SELECT ST_AsEWKT(H3_Center('8075fffffffffff'));
```

```

 st_asewkt
-----------------------------------------
POINT(-5.24539029677733 2.30088211162675)

```
