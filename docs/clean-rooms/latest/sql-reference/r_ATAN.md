# ATAN function

ATAN is a trigonometric function that returns the arc tangent of a number. The return
value is in radians and is between `-PI` and `PI`.

## Syntax

```
ATAN(*number*)
```

## Arguments

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the arc tangent of `1` and multiply it by 4, use the following
example.

````
`SELECT ATAN(1) * 4 AS pi;`

`+-------------------+
| pi | +-------------------+
| 3.141592653589793 | +-------------------+` ```
````
