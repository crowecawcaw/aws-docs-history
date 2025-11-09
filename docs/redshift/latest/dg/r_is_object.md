Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_OBJECT function

Checks whether a variable is an object. The IS_OBJECT function returns `true` for
objects, including empty objects. The function returns `false` for any other values,
including null.

## Syntax

```
IS_OBJECT(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `{"name": "Joe"}` is an object using the IS_OBJECT function, use the following example.

```
`CREATE TABLE t(s super);

INSERT INTO t VALUES (JSON_PARSE('{"name": "Joe"}'));

SELECT s, IS_OBJECT(s) FROM t;`

`+----------------+-----------+
| s | is_object |
+----------------+-----------+
| {"name":"Joe"} | true |
+----------------+-----------+`
```
