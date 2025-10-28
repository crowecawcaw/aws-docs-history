Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# COPY parameter reference

COPY has many parameters that can be used in many situations.
However, not all parameters are supported in each situation.
For example, to load from ORC or PARQUET files there is a limited number of supported parameters.
For more information, see
[COPY from columnar data
formats](copy-usage_notes-copy-from-columnar.md "copy-usage_notes-copy-from-columnar.md").

###### Topics

- [Data sources](copy-parameters-data-source.md "copy-parameters-data-source.md")
- [Authorization parameters](copy-parameters-authorization.md "copy-parameters-authorization.md")
- [Column mapping options](copy-parameters-column-mapping.md "copy-parameters-column-mapping.md")
- [Data format parameters](copy-parameters-data-format.md "copy-parameters-data-format.md")
- [File compression
  parameters](copy-parameters-file-compression.md "copy-parameters-file-compression.md")
- [Data conversion parameters](copy-parameters-data-conversion.md "copy-parameters-data-conversion.md")
- [Data load operations](copy-parameters-data-load.md "copy-parameters-data-load.md")
- [Alphabetical parameter list](r_COPY-alphabetical-parm-list.md "r_COPY-alphabetical-parm-list.md")
