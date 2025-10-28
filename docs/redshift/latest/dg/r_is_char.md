Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_CHAR function

Checks whether a value is a `CHAR`. The IS_CHAR function returns `true` for strings that
have only ASCII characters, because the CHAR type can store only characters that are in the
ASCII format. The function returns `false` for any other values.

## Syntax

```
IS_CHAR(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `t` is a `CHAR` using the IS_CHAR function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES ('t');

SELECT s, IS_CHAR(s) FROM t;`

`+-----+---------+
| s | is_char | +-----+---------+
| "t" | true | +-----+---------+` ```
````
