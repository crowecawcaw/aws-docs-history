Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

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
