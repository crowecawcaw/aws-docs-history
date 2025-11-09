# DECIMAL_PRECISION function

Checks the precision of the maximum total number of decimal digits to be stored. This
number includes both the left and right digits of the decimal point. The range of the
precision is from 1 to 38, with a default of 38.

## Syntax

```
DECIMAL_PRECISION(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`INTEGER`

## Example

To apply the DECIMAL_PRECISION function to the table t, use the following
example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (3.14159);

SELECT DECIMAL_PRECISION(s) FROM t;`

`+-------------------+
| decimal_precision |
+-------------------+
| 6 |
+-------------------+`
```
