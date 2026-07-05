Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# IS\_VARCHAR function

Checks whether a variable is a `VARCHAR`. The IS\_VARCHAR function returns `true` for all
strings. The function returns `false` for any other values.

The IS\_VARCHAR function is a superset of the IS\_CHAR function.

## Syntax

```
IS_VARCHAR(*super\_expression*)

```

## Arguments

_super\_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `abc` is a `VARCHAR` using the IS\_VARCHAR function, use the following example.

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
