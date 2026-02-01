Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# H3_FromLongLat

H3_FromLongLat returns the corresponding H3 cell ID from an input longitude, latitude, and resolution.
For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_FromLongLat(*longitude*, *latitude*, *resolution*)
```

## Arguments

_longitude_

A value of data type `DOUBLE PRECISION` or an expression that
evaluates to a `DOUBLE PRECISION` type.

_latitude_

A value of data type `DOUBLE PRECISION` or an expression that
evaluates to a `DOUBLE PRECISION` type.

_resolution_

A value of data type `INTEGER` or an expression that
evaluates to an `INTEGER` type.
The value represents the resolution of the H3 grid system.
The value must be an integer between 0–15, inclusive.
With `0` being the coarsest and `15` being the finest.

## Return type

`BIGINT` – represents the H3 cell ID.

If _resolution_ is out of bounds, then an error is returned.

## Examples

The following SQL returns the H3 cell ID from longitude `0`, latitude `0`, and resolution `10`.

```
SELECT H3_FromLongLat(0, 0, 10);
```

```

 h3_fromlonglat
-------------------
 623560421467684863

```
