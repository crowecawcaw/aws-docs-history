Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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
