# IS_BIGINT function

Checks whether a value is a `BIGINT`. The IS_BIGINT function returns
`true` for numbers of scale 0 in the 64-bit range. Otherwise, the
function returns `false` for all other values, including null and floating
point numbers.

The IS_BIGINT function is a superset of IS_INTEGER.

## Syntax

```
IS_BIGINT(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `5` is a `BIGINT` using the IS_BIGINT function,
use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_BIGINT(s) FROM t;`

`+---+-----------+
| s | is_bigint |
+---+-----------+
| 5 | true |
+---+-----------+`
```
