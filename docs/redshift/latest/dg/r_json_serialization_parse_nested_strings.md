Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# json_serialization_parse_nested_strings

## Values (default in bold)

**false**, true

## Description

A session configuration that modifies the JSON serialization behavior of ORC, JSON,
Ion, and Parquet formatted data. When both
`json_serialization_parse_nested_strings` and
`json_serialization_enable` are true, string values that are stored in
complex types (such as, maps, structures, or arrays) are parsed and written inline
directly into the result if they are valid JSON. If
`json_serialization_parse_nested_strings` is false, strings within nested
complex types are serialized as escaped JSON strings. For more information, see [Serializing complex types containing JSON strings](serializing-complex-JSON.md#serializing-complex-JSON-strings "serializing-complex-JSON.md#serializing-complex-JSON-strings").
