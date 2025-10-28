Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# H3_FromPoint

H3_FromPoint returns the corresponding H3 cell ID from an input geometry point and resolution.
For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_FromPoint(*geom*, *resolution*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The _geom_ must be a `POINT`.

_resolution_

A value of data type `INTEGER` or an expression that
evaluates to an `INTEGER` type.
The value represents the resolution of the H3 grid system.
The value must be an integer between 0–15, inclusive.
With `0` being the coarsest and `15` being the finest.

## Return type

`BIGINT` – represents the H3 cell ID.

If _geom_ is not a `POINT`, then an error is returned.

If _resolution_ is out of bounds, then an error is returned.

If _geom_ is empty, then NULL is returned.

## Examples

The following SQL returns the H3 cell ID from point `0,0`, and resolution `10`.

```
SELECT H3_FromPoint(ST_GeomFromText('POINT(0 0)'), 10);
```

```

 h3_frompoint
-------------------
 623560421467684863

```
