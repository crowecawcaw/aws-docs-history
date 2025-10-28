# SIN function

SIN is a trigonometric function that returns the sine of a number. The return value is
between `-1` and `1`.

## Syntax

```
SIN(*number*)
```

## Argument

_number_

A `DOUBLE PRECISION` number in radians.

## Return type

`DOUBLE PRECISION`

## Example

To return the sine of `-PI`, use the following example.

````
`SELECT SIN(-PI());`

`+-------------------------+
| sin | +-------------------------+
| -0.00000000000000012246 | +-------------------------+` ```
````
