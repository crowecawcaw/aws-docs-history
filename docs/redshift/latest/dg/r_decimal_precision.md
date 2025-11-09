Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DECIMAL_PRECISION function

Checks the precision of the maximum total number of decimal digits to be stored. This
number includes both the left and right digits of the decimal point. The range of the
precision is from 1 to 38, with a default of 38.

## Syntax

```
DECIMAL_PRECISION(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`INTEGER`

## Examples

To apply the DECIMAL_PRECISION function to the table t, use the following example.

```
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (3.14159);

SELECT DECIMAL_PRECISION(s) FROM t;`

`+-------------------+
| decimal_precision |
+-------------------+
| 6 |
+-------------------+`
```
