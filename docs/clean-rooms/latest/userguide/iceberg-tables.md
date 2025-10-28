# Apache Iceberg tables in AWS Clean Rooms

Apache Iceberg is an open source table format for data lakes. AWS Clean Rooms can use the statistics
stored in Apache Iceberg metadata to optimize query plans and reduce file scans during clean room
query processing. For more information, see the [Apache
Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/") documentation.

Consider the following when using AWS Clean Rooms with Iceberg tables:

- **Apache
  Iceberg tables for S3** – Apache Iceberg
  tables must be defined in the AWS Glue Data Catalog based on the [open source glue catalog
  implementation](https://iceberg.apache.org/docs/latest/aws/#glue-catalog "https://iceberg.apache.org/docs/latest/aws/#glue-catalog").
- **Apache Iceberg tables for Athena** – For more
  information, see [https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html](../../../athena/latest/ug/querying-iceberg.md "../../../athena/latest/ug/querying-iceberg.md")
- **Apache Iceberg tables for Snowflake** – For more
  information, see [https://docs.snowflake.com/en/user-guide/tables-iceberg](https://docs.snowflake.com/en/user-guide/tables-iceberg "https://docs.snowflake.com/en/user-guide/tables-iceberg")
- **Parquet file format** – AWS Clean Rooms only supports Iceberg
  tables in the Parquet data file format.
- **GZIP and Snappy compression** – AWS Clean Rooms supports
  Parquet with GZIP and Snappy compression.
- **Iceberg versions** – AWS Clean Rooms supports running queries
  against version 1 and version 2 Iceberg tables.
- **Partitions** – You don't need to manually add
  partitions for your Apache Iceberg tables in AWS Glue. AWS Clean Rooms detects new partitions
  in Apache Iceberg tables automatically and no manual operation is needed to
  update partitions in the table definition. Iceberg partitions appear as regular columns in the
  AWS Clean Rooms table schema and not separately as a partition key in the configured table schema.
- **Limitations**
  - **New Iceberg tables only**

  Apache Iceberg tables converted from Apache Parquet tables
  are not supported.
  - **Time travel queries**

  AWS Clean Rooms does not support time travel queries with Apache Iceberg
  tables.
  - **Athena engine version 2**

  Iceberg tables created with Athena engine version 2 are not
  supported.
  - **File formats**

  Avro and Optimized Row Columnar (ORC) file formats are not
  supported.
  - **Compression**

  Zstandard (Zstd) compression for Parquet is not
  supported.

## Supported data types for Iceberg tables

AWS Clean Rooms can query Iceberg tables that contain the following data types:

- BOOLEAN
- DATE
- DECIMAL
- DOUBLE
- FLOAT
- INT
- LIST
- LONG
- MAP
- STRING
- STRUCT
- TIMESTAMP WITHOUT TIME ZONE

For more information about Iceberg data types, see the [Schemas for Iceberg](https://iceberg.apache.org/docs/latest/schemas/ "https://iceberg.apache.org/docs/latest/schemas/") in the Apache
Iceberg documentation.
