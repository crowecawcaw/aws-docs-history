# IS_FLOAT function

Checks whether a value is a floating point number. The IS_FLOAT function returns
`true` for floating point numbers (`FLOAT4` and
`FLOAT8`). The function returns `false` for any other
values.

The set of IS_DECIMAL the set of IS_FLOAT are disjoint.

## Syntax

```
IS_FLOAT(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `2.22::FLOAT` is a `FLOAT` using the IS_FLOAT
function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES(2.22::FLOAT);

SELECT s, IS_FLOAT(s) FROM t;`

`+---------+----------+
| s | is_float | +---------+----------+
| 2.22e+0 | true | +---------+----------+` ```
````
