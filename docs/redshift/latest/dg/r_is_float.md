Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS\_FLOAT function

Checks whether a value is a floating point number. The IS\_FLOAT function returns `true`
for floating point numbers (`FLOAT4` and `FLOAT8`). The function returns `false` for any other
values.

The set of IS\_DECIMAL the set of IS\_FLOAT are disjoint.

## Syntax

```
IS_FLOAT(*super\_expression*)

```

## Arguments

_super\_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `2.22::FLOAT` is a `FLOAT` using the IS\_FLOAT function, use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES(2.22::FLOAT);

SELECT s, IS_FLOAT(s) FROM t;`

`+---------+----------+
| s | is_float |
+---------+----------+
| 2.22e+0 | true |
+---------+----------+`
```
