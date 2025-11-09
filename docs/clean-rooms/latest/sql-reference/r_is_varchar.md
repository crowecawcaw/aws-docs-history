# IS_VARCHAR function

Checks whether a variable is a `VARCHAR`. The IS_VARCHAR function returns
`true` for all strings. The function returns `false` for any
other values.

The IS_VARCHAR function is a superset of the IS_CHAR function.

## Syntax

```
IS_VARCHAR(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `abc` is a `VARCHAR` using the IS_VARCHAR
function, use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES ('abc');

SELECT s, IS_VARCHAR(s) FROM t;`

`+-------+------------+
| s | is_varchar |
+-------+------------+
| "abc" | true |
+-------+------------+`
```
