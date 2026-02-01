Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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
