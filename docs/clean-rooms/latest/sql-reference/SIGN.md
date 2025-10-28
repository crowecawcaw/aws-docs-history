# SIGN function

The SIGN function returns the sign (positive or negative) of a number. The result of
the SIGN function is `1`, `-1`, or `0` indicating the sign
of the argument.

## Syntax

```
SIGN (*number*)
```

## Argument

_number_

Number or expression that evaluates to a number. It can be the DECIMALor
FLOAT8 type. AWS Clean Rooms can convert other data types per the implicit conversion
rules.

## Return type

SIGN returns the same numeric data type as the input argument(s). If the input is
DECIMAL, the output is DECIMAL(1,0).

## Examples

To determine the sign of the commission paid for a given transaction from the SALES
table, use the following example.

````
SELECT commission, SIGN(commission)
FROM sales WHERE salesid=10000;

+------------+------+
| commission | sign | +------------+------+
|      28.05 |    1 | +------------+------+ ```
````
