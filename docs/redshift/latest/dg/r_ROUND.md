Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ROUND function

The ROUND function rounds numbers to the nearest integer or decimal.

The ROUND function can optionally include a second argument as an `INTEGER` to indicate
the number of decimal places for rounding, in either direction. When you don't
provide the second argument, the function rounds to the nearest whole number. When the
second argument _integer_ is specified, the function rounds to the nearest
number with _integer_ decimal places of precision.

## Syntax

```
ROUND(*number* [ , *integer* ] )
```

## Arguments

_number_

A number or expression that evaluates to a number. It can be the `DECIMAL`,
`FLOAT8` or `SUPER` type. Amazon Redshift can implicitly convert other numeric data types.

_integer_
(Optional) An `INTEGER` that indicates the number of decimal places for rounding in either
direction. The `SUPER` data type isn't supported for this argument.

## Return type

ROUND returns the same numeric data type as the input _number_.

When the input is of the `SUPER` type, the output retains the same dynamic type as the input while the static type remains the `SUPER` type. When the dynamic type of `SUPER` isn't a number, Amazon Redshift returns `NULL`.

## Examples

The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To round the commission paid for a given transaction to the nearest whole number, use the following example.

```
`SELECT commission, ROUND(commission)
FROM sales WHERE salesid=10000;`

`+------------+-------+
| commission | round |
+------------+-------+
| 28.05 | 28 |
+------------+-------+`
```

To round the commission paid for a given transaction to the first decimal place, use the following example.

```
`SELECT commission, ROUND(commission, 1)
FROM sales WHERE salesid=10000;`

`+------------+-------+
| commission | round |
+------------+-------+
| 28.05 | 28.1 |
+------------+-------+`
```

To extend the precision in the opposite direction as the previous example, use the following example.

```
`SELECT commission, ROUND(commission, -1)
FROM sales WHERE salesid=10000;`

`+------------+-------+
| commission | round |
+------------+-------+
| 28.05 | 30 |
+------------+-------+`
```
