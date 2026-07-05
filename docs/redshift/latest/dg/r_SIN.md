Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SIN function

SIN is a trigonometric function that returns the sine of a number. The return value
is between `-1` and `1`.

## Syntax

```
SIN(*number*)
```

## Argument

_number_

A `DOUBLE PRECISION` number in radians.

## Return type

`DOUBLE PRECISION`

## Examples

To return the sine of `-PI`, use the following example.

```
`SELECT SIN(-PI());`

`+-------------------------+
| sin |
+-------------------------+
| -0.00000000000000012246 |
+-------------------------+`
```
