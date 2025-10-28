Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DECIMAL_SCALE function

Checks the number of decimal digits to be stored to the right of the decimal point. The range of the scale is from 0 to the precision point, with a default of 0.

## Syntax

```
DECIMAL_SCALE(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`INTEGER`

## Examples

To apply the DECIMAL_SCALE function to the table t, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (3.14159);

SELECT DECIMAL_SCALE(s) FROM t;`

`+---------------+
| decimal_scale | +---------------+
| 5 | +---------------+` ```
````
