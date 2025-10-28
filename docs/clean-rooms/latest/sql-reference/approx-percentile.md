# APPROX PERCENTILE function

APPROX PERCENTILE is used to estimate the percentile value of a given expression or column
without having to sort the entire dataset. This function is useful in scenarios where you need to
quickly understand the distribution of a large dataset or track percentile-based metrics, without
the computational overhead of performing an exact percentile calculation. However, it's important
to understand the trade-offs between speed and accuracy, and to choose the appropriate error
tolerance based on the specific requirements of your use case.

## Syntax

```
APPROX_PERCENTILE(expr, percentile [, accuracy])

```

## Arguments

_expr_

The expression or column for which you want to estimate the percentile value.

It can be a single column, a complex expression, or a combination of columns.

_percentile_

The percentile value you want to estimate, expressed as a value between 0 and 1.

For example, 0.5 would correspond to the 50th percentile (median).

_accuracy_

An optional parameter that specifies the desired accuracy of the percentile estimate. It
is a value between 0 and 1, representing the maximum acceptable relative error of the
estimate. A smaller `accuracy` value will result in a more precise but slower
estimation. If this parameter isn't provided, a default value (usually around 0.05 or 5%) is
used.

## Returns

Returns the approximate percentile of the numeric or ANSI interval column col which is the
smallest value in the ordered col values (sorted from least to greatest) such that no more than
percentage of col values is less than the value or equal to that value.

The value of percentage must be between 0.0 and 1.0. The accuracy parameter (default: 10000) is a positive numeric literal which controls approximation accuracy at the cost of
memory.

Higher value of accuracy yields better accuracy, `1.0/accuracy` is the relative
error of the approximation.

When percentage is an array, each value of the percentage array must be between 0.0 and
1.0. In this case, returns the approximate percentile array of column col at the given
percentage array.

## Examples

The following query estimates the 95th percentile of the `response_time` column,
with a maximum relative error of 1% (0.01).

```
SELECT APPROX_PERCENTILE(response_time, 0.95, 0.01) AS p95_response_time
FROM my_table;
```

The following query estimates the 50th, 40th, and 10th percentile values of the
`col` column in the `tab` table.

```
SELECT approx_percentile(col, array(0.5, 0.4, 0.1), 100) FROM VALUES (0), (1), (2), (10) AS tab(col)
```

The following query estimates the 50th percentile (median) of the values in the col
column.

```
SELECT approx_percentile(col, 0.5, 100) FROM VALUES (0), (6), (7), (9), (10) AS tab(col)
```
