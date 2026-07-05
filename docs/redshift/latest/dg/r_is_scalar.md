Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# IS\_SCALAR function

Checks whether a variable is a scalar. The IS\_SCALAR function returns `true` for any
value that is not an array or an object. The function returns `false` for any other
values, including null.

The set of IS\_ARRAY, IS\_OBJECT, and IS\_SCALAR cover all values except nulls.

## Syntax

```
IS_SCALAR(*super\_expression*)

```

## Arguments

_super\_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `{"name": "Joe"}` is a scalar using the IS\_SCALAR function, use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (JSON_PARSE('{"name": "Joe"}'));

SELECT s, IS_SCALAR(s.name) FROM t;`

`+----------------+-----------+
| s | is_scalar |
+----------------+-----------+
| {"name":"Joe"} | true |
+----------------+-----------+`
```
