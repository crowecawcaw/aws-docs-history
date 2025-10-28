Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_SCALAR function

Checks whether a variable is a scalar. The IS_SCALAR function returns `true` for any
value that is not an array or an object. The function returns `false` for any other
values, including null.

The set of IS_ARRAY, IS_OBJECT, and IS_SCALAR cover all values except nulls.

## Syntax

```
IS_SCALAR(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `{"name": "Joe"}` is a scalar using the IS_SCALAR function, use the following example.

````
`CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (JSON_PARSE('{"name": "Joe"}'));

SELECT s, IS_SCALAR(s.name) FROM t;`

`+----------------+-----------+
| s | is_scalar | +----------------+-----------+
| {"name":"Joe"} | true | +----------------+-----------+` ```
````
