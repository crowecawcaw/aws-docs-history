Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# H3_Polyfill

H3_Polyfill returns the corresponding H3 cell IDs that correspond to the hexagons and pentagons that are contained in the input polygon of the given resolution.
For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_Polyfill(*geom*, *resolution*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The _geom_ must be a `POLYGON`.

_resolution_

A value of data type `INTEGER` or an expression that
evaluates to an `INTEGER` type.
The value represents the resolution of the H3 grid system.
The value must be an integer between 0–15, inclusive.
With `0` being the coarsest and `15` being the finest.

## Return type

`SUPER` – represents a list of H3 cell IDs.

If _geom_ is not a `POLYGON`, then an error is returned.

If _resolution_ is out of bounds, then an error is returned.

If _geom_ is empty, then NULL is returned.

## Examples

The following SQL returns a SUPER data type array of H3 cell IDs from a polygon and resolution `4`.

```
SELECT H3_Polyfill(ST_GeomFromText('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))'), 4);
```

```

 h3_polyfill
----------------------------------------------------------------------------------------------------------------------------------------------------------
 [596538848238895103,596538805289222143,596538856828829695,596538813879156735,596537920525959167,596538685030137855,596538693620072447,596538839648960511]

```
