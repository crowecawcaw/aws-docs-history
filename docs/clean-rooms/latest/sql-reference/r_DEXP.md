# DEXP function

The DEXP function returns the exponential value in scientific notation for a double
precision number. The only difference between the DEXP and EXP functions is that the
parameter for DEXP must be a `DOUBLE PRECISION`.

## Syntax

```
DEXP(*number*)
```

## Argument

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Example

```
`SELECT (SELECT SUM(qtysold)
FROM sales, date
WHERE sales.dateid=date.dateid
AND year=2008) * DEXP((7::FLOAT/100)*10) qty2010;`

`+-------------------+
| qty2010 |
+-------------------+
| 695447.4837722216 |
+-------------------+`
```
