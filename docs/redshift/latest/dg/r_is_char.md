Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# IS\_CHAR function

Checks whether a value is a `CHAR`. The IS\_CHAR function returns `true` for strings that
have only ASCII characters, because the CHAR type can store only characters that are in the
ASCII format. The function returns `false` for any other values.

## Syntax

```
IS_CHAR(*super\_expression*)

```

## Arguments

_super\_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `t` is a `CHAR` using the IS\_CHAR function, use the following example.

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
