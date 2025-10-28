# IS_INTEGER function

Returns `true` for numbers of scale 0 in the 32-bit range, and
`false` for anything else (including null and floating point
numbers).

The IS_INTEGER function is a superset of the IS_SMALLINT function.

## Syntax

```
IS_INTEGER(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `5` is an `INTEGER` using the IS_INTEGER
function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_INTEGER(s) FROM t;`

`+---+------------+
| s | is_integer | +---+------------+
| 5 | true | +---+------------+` ```
````
