Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# DEGREES function

Converts an angle in radians to its equivalent in degrees.

## Syntax

```
DEGREES(*number*)
```

## Argument

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the degree equivalent of .5 radians, use the following example.

```
`SELECT DEGREES(.5);`

`+-------------------+
| degrees |
+-------------------+
| 28.64788975654116 |
+-------------------+`
```

To convert PI radians to degrees, use the following example.

```
`SELECT DEGREES(pi());`

`+---------+
| degrees |
+---------+
| 180 |
+---------+`
```
