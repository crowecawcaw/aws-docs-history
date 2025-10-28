# IS_SCALAR function

Checks whether a variable is a scalar. The IS_SCALAR function returns
`true` for any value that is not an array or an object. The function
returns `false` for any other values, including null.

The set of IS_ARRAY, IS_OBJECT, and IS_SCALAR cover all values except nulls.

## Syntax

```
IS_SCALAR(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `{"name": "Joe"}` is a scalar using the IS_SCALAR function,
use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (JSON_PARSE('{"name": "Joe"}'));

SELECT s, IS_SCALAR(s.name) FROM t;`

`+----------------+-----------+
| s | is_scalar | +----------------+-----------+
| {"name":"Joe"} | true | +----------------+-----------+` ```
````
