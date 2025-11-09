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

## Example

To return the radian equivalent of 180 degrees, use the following example.

```
`SELECT RADIANS(180);`

`+-------------------+
| radians |
+-------------------+
| 3.141592653589793 |
+-------------------+`
```
