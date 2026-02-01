Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ATAN function

ATAN is a trigonometric function that returns the arc tangent of a number.

The return value is in radians and is between `-PI` and `PI`.

## Syntax

```
ATAN(*number*)
```

## Arguments

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the arc tangent of `1` and multiply it by 4, use the following example.

```
`SELECT ATAN(1) * 4 AS pi;`

`+-------------------+
| pi |
+-------------------+
| 3.141592653589793 |
+-------------------+`
```

To convert the arc tangent of `1` to the equivalent number of
degrees, use the following example.

```
`SELECT (ATAN(1) * 180/(SELECT PI())) AS degrees;`

`+---------+
| degrees |
+---------+
| 45 |
+---------+`
```
