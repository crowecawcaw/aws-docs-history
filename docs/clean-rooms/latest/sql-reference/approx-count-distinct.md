# APPROX COUNT_DISTINCT function

APPROX COUNT_DISTINCT provides an efficient way to estimate the number of unique values in a
column or dataset.

## Syntax

```
approx_count_distinct(expr[, relativeSD])
```

## Arguments

_expr_

The expression or column for which you want to estimate the number of unique
values.

It can be a single column, a complex expression, or a combination of columns.

_relativeSD_

An optional parameter that specifies the desired relative standard deviation of the
estimate.

It is a value between 0 and 1, representing the maximum acceptable relative error of the
estimate. A smaller relativeSD value will result in a more accurate but slower estimation.

If this parameter isn't provided, a default value (usually around 0.05 or 5%) is
used.

## Returns

Returns the estimated cardinality by HyperLogLog++. relativeSD defines the maximum relative
standard deviation allowed.

## Example

The following query estimates the number of unique values in the `col1` column,
with a relative standard deviation of 1% (0.01).

```
SELECT approx_count_distinct(col1, 0.01)
```

The following query estimates that there are 3 unique values in the `col1`
column (the values 1, 2, and 3).

```
SELECT approx_count_distinct(col1) FROM VALUES (1), (1), (2), (2), (3) tab(col1)
```
