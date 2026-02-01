Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# JSON_PARSE function

The JSON_PARSE function parses data in JSON format and converts it into the `SUPER`
representation.

To ingest into `SUPER` data type using the INSERT or UPDATE command, use the JSON_PARSE
function. When you use JSON_PARSE() to parse JSON strings into `SUPER` values, certain
restrictions apply. For additional information, see [Parsing options for SUPER](super-configurations.md#parsing-options-super "super-configurations.md#parsing-options-super").

## Syntax

```
JSON_PARSE( {*json\_string* | *binary\_value*} )
```

## Arguments

_json_string_

An expression that returns serialized JSON as a `VARBYTE` or `VARCHAR` type.

_binary_value_

A VARBYTE type binary value.

## Return type

`SUPER`

## Examples

To convert the JSON array `[10001,10002,"abc"]` into the `SUPER` data type, use the following example.

```
`SELECT JSON_PARSE('[10001,10002,"abc"]');`

`+---------------------+
| json_parse |
+---------------------+
| [10001,10002,"abc"] |
+---------------------+`
```

To make sure that the function converted the JSON array into the `SUPER` data type, use the following example. For more information, see [JSON_TYPEOF function](r_json_typeof.md "r_json_typeof.md")

```
`SELECT JSON_TYPEOF(JSON_PARSE('[10001,10002,"abc"]'));`

`+-------------+
| json_typeof |
+-------------+
| array |
+-------------+`
```
