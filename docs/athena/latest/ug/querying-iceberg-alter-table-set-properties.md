

# ALTER TABLE SET TBLPROPERTIES
<a name="querying-iceberg-alter-table-set-properties"></a>

Adds properties to an Iceberg table and sets their assigned values.

In accordance with [Iceberg specifications](https://iceberg.apache.org/#spec/#table-metadata-fields), table properties are stored in the Iceberg table metadata file rather than in AWS Glue. Athena does not accept custom table properties. Refer to the [Specify table properties](querying-iceberg-creating-tables.md#querying-iceberg-table-properties) section for allowed key-value pairs. You can also use `ALTER TABLE SET TBLPROPERTIES` and `ALTER TABLE UNSET TBLPROPERTIES` to set or remove the `write.data.path` and `write.object-storage.path` Iceberg table properties. If you would like Athena to support a specific open source table configuration property, send feedback to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com).

## Synopsis
<a name="querying-iceberg-alter-table-set-properties-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}} SET TBLPROPERTIES ('{{property_name}}' = '{{property_value}}' [ , ... ])
```

## Example
<a name="querying-iceberg-alter-table-set-properties-example"></a>

```
ALTER TABLE iceberg_table SET TBLPROPERTIES (
  'format'='parquet',
  'write_compression'='snappy',
  'optimize_rewrite_delete_file_threshold'='10'
)
```

The following example sets the `write.data.path` property on an existing Iceberg table.

```
ALTER TABLE iceberg_table SET TBLPROPERTIES (
  'write.data.path'='s3://amzn-s3-demo-bucket/{{your-folder}}/data'
)
```