Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_BIGINT function

Checks whether a value is a `BIGINT`. The IS_BIGINT function returns `true` for numbers
of scale 0 in the 64-bit range. Otherwise, the function returns `false` for all other
values, including null and floating point numbers.

The IS_BIGINT function is a superset of IS_INTEGER.

## Syntax

```
IS_BIGINT(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `5` is a `BIGINT` using the IS_BIGINT function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_BIGINT(s) FROM t;`

`+---+-----------+
| s | is_bigint | +---+-----------+
| 5 | true | +---+-----------+` ```
````
