# SKEWNESS function

The SKEWNESS function returns the skewness value calculated from values of a group.

Skewness is a statistical measure that describes the asymmetry or lack of symmetry in a
dataset. It provides information about the shape of the data distribution.

This function can be useful in understanding the statistical properties of a dataset and
informing further analysis or decision-making.

## Syntax

```
skewness(expr)
```

## Arguments

_expr_

An expression that evaluates to a numeric.

## Returns

Returns DOUBLE.

If DISTINCT is specified, the function operates only on a unique set of _expr_ values.

## Examples

The following query calculates the skewness of the values in the `col` column.
In this example, the `VALUES` clause is used to create an inline table with four
rows, where each row has a single column `col` with the values -10, -20, 100, and 1000. The `skewness()` function is then used to calculate the skewness of the values
in the `col` column. The result, 1.1135657469022011, represents the degree and
direction of skewness in the data. A positive skewness value indicates that the data is skewed
to the right, with the bulk of the values concentrated on the left side of the distribution. A
negative skewness value indicates that the data is skewed to the left, with the bulk of the
values concentrated on the right side of the distribution.

```
SELECT skewness(col) FROM VALUES (-10), (-20), (100), (1000) AS tab(col);
 1.1135657469022011
```

The following query calculates the skewness of the values in the col column. Similar to the
previous example, the `VALUES` clause is used to create an inline table with four
rows, where each row has a single column `col` with the values -1000, -100, 10, and 20. The `skewness()` function is then used to calculate the skewness of the values in
the `col` column. The result, -1.1135657469022011, represents the degree and
direction of skewness in the data. In this case, the negative skewness value indicates that the
data is skewed to the left, with the bulk of the values concentrated on the right side of the
distribution.

```
SELECT skewness(col) FROM VALUES (-1000), (-100), (10), (20) AS tab(col);
 -1.1135657469022011
```
