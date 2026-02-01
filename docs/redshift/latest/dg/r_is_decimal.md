Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_DECIMAL function

Checks whether a value is a `DECIMAL`. The IS_DECIMAL function returns `true` for numbers
that are not floating points. The function returns `false` for any other values, including
null.

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

## Examples

To check if `1.22` is a `DECIMAL` using the IS_DECIMAL function, use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (1.22);

SELECT s, IS_DECIMAL(s) FROM t;`

`+------+------------+
| s | is_decimal |
+------+------------+
| 1.22 | true |
+------+------------+`
```
