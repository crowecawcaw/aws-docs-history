Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

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
