Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_INTEGER function

Returns `true` for numbers of scale 0 in the 32-bit range, and `false` for anything else
(including null and floating point numbers).

The IS_INTEGER function is a superset of the IS_SMALLINT function.

## Syntax

```
IS_INTEGER(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `5` is an `INTEGER` using the IS_INTEGER function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_INTEGER(s) FROM t;`

`+---+------------+
| s | is_integer | +---+------------+
| 5 | true | +---+------------+` ```
````
