Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ATAN2 function

ATAN2 is a trigonometric function that returns the arc tangent of one number
divided by another number. The return value is in radians and is between `PI/2` and `-PI/2`.

## Syntax

```
ATAN2(*number1*, *number2*)
```

## Arguments

_number1_

A `DOUBLE PRECISION` number.

_number2_

A `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the arc tangent of `2/2` and multiply it by 4, use the following example.

```
`SELECT ATAN2(2,2) * 4 AS PI;`

`+-------------------+
| pi |
+-------------------+
| 3.141592653589793 |
+-------------------+`
```

To convert the arc tangent of `1/0` (which evaluates to 0) to the equivalent
number of degrees, use the following example.

```
`SELECT (ATAN2(1,0) * 180/(SELECT PI())) AS degrees;`

`+---------+
| degrees |
+---------+
| 90 |
+---------+`
```
