# ASIN function

ASIN is a trigonometric function that returns the arc sine of a number. The return value
is in radians and is between `PI/2` and `-PI/2`.

## Syntax

```
ASIN(*number*)
```

## Arguments

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the arc sine of `1`, use the following example.

````
`SELECT ASIN(1) AS halfpi;`

`+--------------------+
| halfpi | +--------------------+
| 1.5707963267948966 | +--------------------+` ```
````
