# Limitations

Consider the following limitations before you use data lake frameworks with AWS Glue.

- The following AWS Glue `GlueContext` methods for DynamicFrame don't support reading and writing data lake framework
  tables. Use the `GlueContext` methods for DataFrame or Spark DataFrame API instead.
  - `create_dynamic_frame.from_catalog`
  - `write_dynamic_frame.from_catalog`
  - `getDynamicFrame`
  - `writeDynamicFrame`

- The following `GlueContext` methods for DataFrame are supported with Lake Formation permission control:
  - `create_data_frame.from_catalog`
  - `write_data_frame.from_catalog`
  - `getDataFrame`
  - `writeDataFrame`

- [Grouping small files](grouping-input-files.md "grouping-input-files.md") is not
  supported.
- [Job bookmarks](monitor-continuations.md "monitor-continuations.md") are not
  supported.
- Apache Hudi 0.10.1 for AWS Glue 3.0 doesn't support Hudi Merge on Read (MoR)
  tables.
- `ALTER TABLE … RENAME TO` is not available for Apache Iceberg 0.13.1
  for AWS Glue 3.0.

## Limitations for data lake format tables managed by Lake Formation permissions

The data lake formats are integrated with AWS Glue ETL via Lake Formation permissions. Creating a DynamicFrame using `create_dynamic_frame` is not supported. For more information, see the following examples:

- [Example: Read and write Iceberg table with Lake Formation permission control](aws-glue-programming-etl-format-iceberg.md#aws-glue-programming-etl-format-iceberg-read-write-lake-formation-tables "aws-glue-programming-etl-format-iceberg.md#aws-glue-programming-etl-format-iceberg-read-write-lake-formation-tables")
- [Example: Read and write Hudi table with Lake Formation permission control](aws-glue-programming-etl-format-hudi.md#aws-glue-programming-etl-format-hudi-read-write-lake-formation-tables "aws-glue-programming-etl-format-hudi.md#aws-glue-programming-etl-format-hudi-read-write-lake-formation-tables")
- [Example: Read and write Delta Lake table with Lake Formation permission control](aws-glue-programming-etl-format-delta-lake.md#aws-glue-programming-etl-format-delta-lake-read-write-lake-formation-tables "aws-glue-programming-etl-format-delta-lake.md#aws-glue-programming-etl-format-delta-lake-read-write-lake-formation-tables")

###### Note

The integration with AWS Glue ETL via Lake Formation permissions for Apache Hudi, Apache Iceberg, and Delta Lake is supported only in AWS Glue version 4.0.

Apache Iceberg has the best integration with AWS Glue ETL via Lake Formation permissions. It supports almost all operations and includes SQL support.

Hudi supports most basic operations with the exception of administrative operations. This is because these options generally are done via writing of dataframes and specified via `additional_options`. You need to use AWS Glue APIs to create DataFrames for your operations as SparkSQL is not supported.

Delta Lake only supports the reading and appending and overwriting of table data. Delta Lake requires the use of their own libraries to be able to perform various tasks such as updates.

The following features are not available for Iceberg tables managed by Lake Formation permissions.

- Compaction using AWS Glue ETL
- Spark SQL support via AWS Glue ETL

The following are limitations of Hudi tables managed by Lake Formation permissions:

- Removal of orphaned files

The following are limitations of Delta Lake tables managed by Lake Formation permissions:

- All features other than inserting and reading from Delta Lake tables.
