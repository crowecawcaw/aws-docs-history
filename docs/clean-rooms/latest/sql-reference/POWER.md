# POWER function

The POWER function is an exponential function that raises a numeric expression to the
power of a second numeric expression. For example, 2 to the third power is calculated as
`POWER(2,3)`, with a result of `8`.

## Syntax

```
{POWER(*expression1*, *expression2*)
```

## Arguments

_expression1_

Numeric expression to be raised. Must be an `INTEGER`,
`DECIMAL`, or `FLOAT` data type.

_expression2_

Power to raise _expression1_. Must be an
`INTEGER`, `DECIMAL`, or `FLOAT` data type.

## Return type

`DOUBLE PRECISION`

## Example

```
`SELECT (SELECT SUM(qtysold) FROM sales, date
WHERE sales.dateid=date.dateid
AND year=2008) * POW((1+7::FLOAT/100),10) qty2010;`

`+-------------------+
| qty2010 |
+-------------------+
| 679353.7540885945 |
+-------------------+`
```
