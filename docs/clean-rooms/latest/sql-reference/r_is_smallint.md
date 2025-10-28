# IS_SMALLINT function

Checks whether a variable is a `SMALLINT`. The IS_SMALLINT function returns
`true` for numbers of scale 0 in the 16-bit range. The function returns
`false` for any other values, including null and floating point
numbers.

## Syntax

```
IS_SMALLINT(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return

`BOOLEAN`

## Example

To check if `5` is a `SMALLINT` using the IS_SMALLINT
function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_SMALLINT(s) FROM t;`

`+---+-------------+
| s | is_smallint | +---+-------------+
| 5 | true | +---+-------------+` ```
````
