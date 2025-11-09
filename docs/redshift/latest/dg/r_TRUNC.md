Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TRUNC function

The TRUNC function truncates numbers to the previous integer or decimal.

The TRUNC function can optionally include a second argument as an `INTEGER` to indicate
the number of decimal places for rounding, in either direction. When you don't
provide the second argument, the function rounds to the nearest whole number. When the
second argument _integer_ is specified, the function rounds to the nearest
number with _integer_ decimal places of precision.

This function can also truncate a `TIMESTAMP` and return a `DATE`. For more information, see [TRUNC function](r_TRUNC_date.md "r_TRUNC_date.md").

## Syntax

```
TRUNC(*number* [ , *integer* ])
```

## Arguments

_number_

A number or an expression that evaluates to a number. It can be the `DECIMAL`,
`FLOAT8` or `SUPER` type. Amazon Redshift can convert other data types per the implicit
conversion rules.

_integer_

(Optional) An `INTEGER` that indicates the number of decimal places of precision, in
either direction. If no _integer_ is provided, the number is truncated as a
whole number; if an _integer_ is specified, the number is truncated to the
specified decimal place. This isn't supported for the `SUPER` data type.

## Return type

TRUNC returns the same data type as the input _number_.

When the input is of the `SUPER` type, the output retains the same dynamic type as the input while the static type remains the `SUPER` type. When the dynamic type of `SUPER` isn't a number, Amazon Redshift returns `NULL`.

## Examples

Some of the following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To truncate the commission paid for a given sales transaction, use the following example.

```
`SELECT commission, TRUNC(commission)
FROM sales WHERE salesid=784;`

`+------------+-------+
| commission | trunc |
+------------+-------+
| 111.15 | 111 |
+------------+-------+`
```

To truncate the same commission value to the first decimal place, use the following example.

```
`SELECT commission, TRUNC(commission,1)
FROM sales WHERE salesid=784;`

`+------------+-------+
| commission | trunc |
+------------+-------+
| 111.15 | 111.1 |
+------------+-------+`
```

To truncate the commission with a negative value for the second argument, use the following example.
Note that `111.15` is rounded down to `110`.

```
`SELECT commission, TRUNC(commission,-1)
FROM sales WHERE salesid=784;`

`+------------+-------+
| commission | trunc |
+------------+-------+
| 111.15 | 110 |
+------------+-------+`
```
