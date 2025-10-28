Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# RADIANS function

The RADIANS function converts an angle in degrees to its equivalent in radians.

## Syntax

```
RADIANS(*number*)
```

## Argument

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the radian equivalent of 180 degrees, use the following example.

````
`SELECT RADIANS(180);`

`+-------------------+
| radians | +-------------------+
| 3.141592653589793 | +-------------------+` ```
````
