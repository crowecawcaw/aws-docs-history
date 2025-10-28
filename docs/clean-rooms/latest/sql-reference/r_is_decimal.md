# IS_DECIMAL function

Checks whether a value is a `DECIMAL`. The IS_DECIMAL function returns
`true` for numbers that are not floating points. The function returns
`false` for any other values, including null.

The IS_DECIMAL function is a superset of IS_BIGINT.

## Syntax

```
IS_DECIMAL(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `1.22` is a `DECIMAL` using the IS_DECIMAL
function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (1.22);

SELECT s, IS_DECIMAL(s) FROM t;`

`+------+------------+
| s | is_decimal | +------+------------+
| 1.22 | true | +------+------------+` ```
````
