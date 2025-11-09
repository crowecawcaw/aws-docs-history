# IS_CHAR function

Checks whether a value is a `CHAR`. The IS_CHAR function returns
`true` for strings that have only ASCII characters, because the CHAR type
can store only characters that are in the ASCII format. The function returns
`false` for any other values.

## Syntax

```
IS_CHAR(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `t` is a `CHAR` using the IS_CHAR function, use
the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES ('t');

SELECT s, IS_CHAR(s) FROM t;`

`+-----+---------+
| s | is_char |
+-----+---------+
| "t" | true |
+-----+---------+`
```
