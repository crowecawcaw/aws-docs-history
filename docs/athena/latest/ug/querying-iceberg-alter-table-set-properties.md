# ALTER TABLE SET TBLPROPERTIES

Adds properties to an Iceberg table and sets their assigned values.

In accordance with [Iceberg
specifications](https://iceberg.apache.org/#spec/#table-metadata-fields "https://iceberg.apache.org/#spec/#table-metadata-fields"), table properties are stored in the Iceberg table
metadata file rather than in AWS Glue. Athena does not accept custom table properties.
Refer to the [Specify table properties](querying-iceberg-creating-tables.md#querying-iceberg-table-properties "querying-iceberg-creating-tables.md#querying-iceberg-table-properties") section for allowed
key-value pairs. If you would like Athena to support a specific open source table
configuration property, send feedback to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com "mailto:athena-feedback@amazon.com").

## Synopsis

```
ALTER TABLE [`db_name`.]`table_name` SET TBLPROPERTIES ('`property_name`' = '`property_value`' [ , ... ])
```

## Example

```
ALTER TABLE iceberg_table SET TBLPROPERTIES (
  'format'='parquet',
  'write_compression'='snappy',
  'optimize_rewrite_delete_file_threshold'='10'
)
```
