Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

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
