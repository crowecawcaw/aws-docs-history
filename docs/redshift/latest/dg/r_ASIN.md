Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ASIN function

ASIN is a trigonometric function that returns the arc sine of a number. The return
value is in radians and is between `PI/2` and `-PI/2`.

## Syntax

```
ASIN(*number*)
```

## Arguments

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the arc sine of `1`, use the following example.

```
`SELECT ASIN(1) AS halfpi;`

`+--------------------+
| halfpi |
+--------------------+
| 1.5707963267948966 |
+--------------------+`
```

To convert the arc sine of `.5` to the equivalent number of
degrees, use the following example.

```
`SELECT (ASIN(.5) * 180/(SELECT PI())) AS degrees;`

`+--------------------+
| degrees |
+--------------------+
| 30.000000000000004 |
+--------------------+`
```
