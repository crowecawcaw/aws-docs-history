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

## Example

To return the degree equivalent of .5 radians, use the following example.

````
`SELECT DEGREES(.5);`

`+-------------------+
| degrees | +-------------------+
| 28.64788975654116 | +-------------------+` ``` To convert PI radians to degrees, use the following example. ``` `SELECT DEGREES(pi());` `+---------+
| degrees | +---------+
| 180 | +---------+` ```
````
