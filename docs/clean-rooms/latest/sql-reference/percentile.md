# PERCENTILE function

The PERCENTILE function is used to calculates the exact percentile value by first sorting
the values in the `col` column and then finding the value at the specified
`percentage`.

The PERCENTILE function is useful when you need to calculate the exact percentile value and
the computational cost is acceptable for your use case. It provides more accurate results than
the APPROX_PERCENTILE function, but may be slower, especially for large datasets.

In contrast, the APPROX_PERCENTILE function is a more efficient alternative that can provide
an estimate of the percentile value with a specified error tolerance, making it more suitable for
scenarios where speed is a higher priority than absolute precision.

## Syntax

```
percentile(col, percentage [, frequency])
```

## Arguments

_col_

The expression or column for which you want to calculate the percentile value.

_percentage_

The percentile value you want to calculate, expressed as a value between 0 and 1.

For example, 0.5 would correspond to the 50th percentile (median).

_frequency_

An optional parameter that specifies the frequency or weight of each value in the
`col` column. If provided, the function will calculate the percentile based on
the frequency of each value.

## Returns

Returns the exact percentile value of numeric or ANSI interval column col at the given
percentage.

The value of percentage must be between 0.0 and 1.0.

The value of frequency should be positive integral

## Example

The following query finds the value that is greater than or equal to 30% of the values in
the `col` column. Since the values are 0 and 10, the 30th percentile is 3.0, because
it is the value that is greater than or equal to 30% of the data.

```
SELECT percentile(col, 0.3) FROM VALUES (0), (10) AS tab(col);
 3.0
```
