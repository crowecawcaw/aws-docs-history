Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_BOOLEAN function

Checks whether a value is a `BOOLEAN`. The IS_BOOLEAN function returns `true` for
constant JSON Booleans. The function returns `false` for any other values, including
null.

## Syntax

```
IS_BOOLEAN(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `TRUE` is a `BOOLEAN` using the IS_BOOLEAN function, use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (TRUE);

SELECT s, IS_BOOLEAN(s) FROM t;`

`+------+------------+
| s | is_boolean |
+------+------------+
| true | true |
+------+------------+`
```
