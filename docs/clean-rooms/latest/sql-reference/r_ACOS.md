# ACOS function

ACOS is a trigonometric function that returns the arc cosine of a number. The return
value is in radians and is between `0` and `PI`.

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

````
`SELECT ACOS(-1);`

`+-------------------+
| acos | +-------------------+
| 3.141592653589793 | +-------------------+` ```
````
