Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# IS\_SMALLINT function

Checks whether a variable is a `SMALLINT`. The IS\_SMALLINT function returns `true` for
numbers of scale 0 in the 16-bit range. The function returns `false` for any other values,
including null and floating point numbers.

## Syntax

```
IS_SMALLINT(*super\_expression*)

```

## Arguments

_super\_expression_

A `SUPER` expression or column.

## Return

`BOOLEAN`

## Examples

To check if `5` is a `SMALLINT` using the IS\_SMALLINT function, use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_SMALLINT(s) FROM t;`

`+---+-------------+
| s | is_smallint |
+---+-------------+
| 5 | true |
+---+-------------+`
```
