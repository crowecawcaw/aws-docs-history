

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# json\_serialization\_enable
<a name="r_json_serialization_enable"></a>

## Values (default in bold)
<a name="r_json_serialization_enable-values"></a>

**false**, true

## Description
<a name="description"></a>

A session configuration that modifies the JSON serialization behavior of ORC, JSON, Ion, and Parquet formatted data. If `json_serialization_enable` is `true`, all top-level collections are automatically serialized to JSON and returned as VARCHAR(65535). Noncomplex columns are not affected or serialized. Because collection columns are serialized as VARCHAR(65535), their nested subfields can no longer be accessed directly as part of the query syntax (that is, in the filter clause). If `json_serialization_enable` is `false`, top-level collections are not serialized to JSON. For more information about nested JSON serialization, see [Serializing complex nested JSON](serializing-complex-JSON.md). 