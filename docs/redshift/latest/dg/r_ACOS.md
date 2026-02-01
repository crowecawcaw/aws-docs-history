Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ACOS function

ACOS is a trigonometric function that returns the arc cosine of a number.

The return value is in radians and is between `0` and `PI`.

## Syntax

```
ACOS(*number*)
```

## Arguments

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the arc cosine of `-1`, use the following example.

```
`SELECT ACOS(-1);`

`+-------------------+
| acos |
+-------------------+
| 3.141592653589793 |
+-------------------+`
```

To convert the arc cosine of `.5` to the equivalent number of
degrees, use the following example.

```
`SELECT (ACOS(.5) * 180/(SELECT PI())) AS degrees;`

`+-------------------+
| degrees |
+-------------------+
| 60.00000000000001 |
+-------------------+`
```
