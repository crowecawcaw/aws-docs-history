Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# JSON_SERIALIZE_TO_VARBYTE function

The JSON_SERIALIZE_TO_VARBYTE function converts a `SUPER` value to a JSON string
similar to JSON_SERIALIZE(), but stored in a `VARBYTE` value instead.

## Syntax

```
JSON_SERIALIZE_TO_VARBYTE(*super\_expression*)
```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`VARBYTE`

## Examples

To serialize a `SUPER` value and returns the result in `VARBYTE` format, use the following example.

````
`SELECT JSON_SERIALIZE_TO_VARBYTE(JSON_PARSE('[10001,10002,"abc"]'));`

`+----------------------------------------+
| json_serialize_to_varbyte | +----------------------------------------+
| 5b31303030312c31303030322c22616263225d | +----------------------------------------+` ``` To serialize a `SUPER` value and casts the result to `VARCHAR` format, use the following example. For more information, see [CAST function](r_CAST_function.md "r_CAST_function.md"). ``` `SELECT CAST((JSON_SERIALIZE_TO_VARBYTE(JSON_PARSE('[10001,10002,"abc"]'))) AS VARCHAR);` `+---------------------------+
| json_serialize_to_varbyte | +---------------------------+
| [10001,10002,"abc"] | +---------------------------+` ```
````
