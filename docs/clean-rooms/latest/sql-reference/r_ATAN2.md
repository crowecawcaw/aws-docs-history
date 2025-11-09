# ATAN2 function

ATAN2 is a trigonometric function that returns the arc tangent of one number divided by
another number. The return value is in radians and is between `PI/2` and
`-PI/2`.

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

To return the arc tangent of `2/2` and multiply it by 4, use the following
example.

```
`SELECT ATAN2(2,2) * 4 AS PI;`

`+-------------------+
| pi |
+-------------------+
| 3.141592653589793 |
+-------------------+`
```
