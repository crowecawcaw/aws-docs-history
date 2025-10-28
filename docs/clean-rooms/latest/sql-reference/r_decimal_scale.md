# DECIMAL_SCALE function

Checks the number of decimal digits to be stored to the right of the decimal point.
The range of the scale is from 0 to the precision point, with a default of 0.

## Syntax

```
DECIMAL_SCALE(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`INTEGER`

## Example

To apply the DECIMAL_SCALE function to the table t, use the following
example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (3.14159);

SELECT DECIMAL_SCALE(s) FROM t;`

`+---------------+
| decimal_scale | +---------------+
| 5 | +---------------+` ```
````
