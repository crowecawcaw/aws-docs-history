Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TAN function

TAN is a trigonometric function that returns the tangent of a number. The input
argument is a number (in radians).

## Syntax

```
TAN(*number*)
```

## Argument

_number_

A `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the tangent of zero, use the following example.

```
`SELECT TAN(0);`

`+-----+
| tan |
+-----+
| 0 |
+-----+`
```
