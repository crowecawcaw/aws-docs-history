Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_VARCHAR function

Checks whether a variable is a `VARCHAR`. The IS_VARCHAR function returns `true` for all
strings. The function returns `false` for any other values.

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

## Examples

To check if `abc` is a `VARCHAR` using the IS_VARCHAR function, use the following example.

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
