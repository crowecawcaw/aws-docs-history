Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# json_serialization_enable

## Values (default in bold)

**false**, true

## Description

A session configuration that modifies the JSON serialization behavior of ORC, JSON,
Ion, and Parquet formatted data. If `json_serialization_enable` is
`true`, all top-level collections are automatically serialized to JSON and
returned as VARCHAR(65535). Noncomplex columns are not affected or serialized. Because
collection columns are serialized as VARCHAR(65535), their nested subfields can no
longer be accessed directly as part of the query syntax (that is, in the filter clause).
If `json_serialization_enable` is `false`, top-level collections
are not serialized to JSON. For more information about nested JSON serialization, see
[Serializing complex nested JSON](serializing-complex-JSON.md "serializing-complex-JSON.md").
