# Create Iceberg tables

To create an Iceberg table for use in Athena, you can use a `CREATE TABLE`
statement as documented on this page, or you can use an AWS Glue crawler.

## Use a CREATE TABLE

statement

Athena creates Iceberg v2 tables. For the difference between v1 and v2 tables, see
[Format version changes](https://iceberg.apache.org/spec/#appendix-e-format-version-changes "https://iceberg.apache.org/spec/#appendix-e-format-version-changes") in the Apache Iceberg documentation.

Athena `CREATE TABLE` creates an Iceberg table with no data. You can
query a table from external systems such as Apache Spark directly if the table uses
the [Iceberg
open source glue catalog](https://iceberg.apache.org/docs/latest/aws/#glue-catalog "https://iceberg.apache.org/docs/latest/aws/#glue-catalog"). You do not have to create an external
table.

###### Warning

Running `CREATE EXTERNAL TABLE` results in the error message
**`External keyword not supported for table type
 ICEBERG`**.

To create an Iceberg table from Athena, set the `'table_type'` table
property to `'ICEBERG'` in the `TBLPROPERTIES` clause, as in
the following syntax summary.

```
CREATE TABLE
  [db_name.]table_name (col_name data_type [COMMENT col_comment] [, ...] )
  [PARTITIONED BY (col_name | transform, ... )]
  LOCATION 's3://amzn-s3-demo-bucket/`your-folder`/'
  TBLPROPERTIES ( 'table_type' ='ICEBERG' [, `property_name`=`property_value`] )
```

For information about the data types that you can query in Iceberg tables, see
[Supported data types for Iceberg
tables in Athena](querying-iceberg-supported-data-types.md "querying-iceberg-supported-data-types.md").

### Use partitions

To create Iceberg tables with partitions, use `PARTITIONED BY`
syntax. Columns used for partitioning must be specified in the columns
declarations first. Within the `PARTITIONED BY` clause, the column
type must not be included. You can also define [partition
transforms](https://iceberg.apache.org/spec/#partition-transforms "https://iceberg.apache.org/spec/#partition-transforms") in `CREATE TABLE` syntax. To specify multiple
columns for partitioning, separate the columns with the comma (`,`)
character, as in the following example.

```
CREATE TABLE iceberg_table (id bigint, data string, category string)
  PARTITIONED BY (category, bucket(16, id))
  LOCATION 's3://amzn-s3-demo-bucket/`your-folder`/'
  TBLPROPERTIES ( 'table_type' = 'ICEBERG' )
```

The following table shows the available partition transform functions.

| Function                | Description                                                                                                  | Supported types                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| `year(ts)`              | Partition by year                                                                                            | `date`, `timestamp`                                                     |
| `month(ts)`             | Partition by month                                                                                           | `date`, `timestamp`                                                     |
| `day(ts)`               | Partition by day                                                                                             | `date`, `timestamp`                                                     |
| `hour(ts)`              | Partition by hour                                                                                            | `timestamp`                                                             |
| `bucket(`N`,<br>col)`   | Partition by hashed value mod `N`<br>buckets. This is the same concept as hash bucketing for Hive<br>tables. | `int`, `long`, `decimal`,<br>`date`, `timestamp`,<br>`string`, `binary` |
| `truncate(`L`,<br>col)` | Partition by value truncated to<br>`L`                                                                       | `int`, `long`, `decimal`,<br>`string`                                   |

Athena supports Iceberg's hidden partitioning. For more information, see [Iceberg's hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning "https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning") in the Apache Iceberg
documentation.

This section describes table properties that you can specify as key-value
pairs in the `TBLPROPERTIES` clause of the `CREATE
 TABLE` statement. Athena allows only a predefined list of key-value
pairs in the table properties for creating or altering Iceberg tables. The
following tables show the table properties that you can specify. For more
information about the compaction options, see [Optimize Iceberg tables](querying-iceberg-data-optimization.md "querying-iceberg-data-optimization.md") in this
documentation. If you would like Athena to support a specific open source
table configuration property, send feedback to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com "mailto:athena-feedback@amazon.com").

_format_

|                                |                                                                                                                                                                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**                | File data format                                                                                                                                                                                                 |
| **Allowed property<br>values** | Supported file format and compression combinations vary<br>by Athena engine version. For more information, see [Use Iceberg table compression](compression-support-iceberg.md "compression-support-iceberg.md"). |
| **Default value**              | parquet                                                                                                                                                                                                          |

_write_compression_

|                                |                                                                                                                                                                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**                | File compression codec                                                                                                                                                                                           |
| **Allowed property<br>values** | Supported file format and compression combinations vary<br>by Athena engine version. For more information, see [Use Iceberg table compression](compression-support-iceberg.md "compression-support-iceberg.md"). |
| **Default value**              | Default write compression varies by Athena engine<br>version. For more information, see [Use Iceberg table compression](compression-support-iceberg.md "compression-support-iceberg.md").                        |

_optimize_rewrite_data_file_threshold_

|                                |                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**                | Data optimization specific configuration. If there are<br>fewer data files that require optimization than the given<br>threshold, the files are not rewritten. This allows the<br>accumulation of more data files to produce files closer to<br>the target size and skip unnecessary computation for cost<br>saving. |
| **Allowed property<br>values** | A positive number. Must be less than 50.                                                                                                                                                                                                                                                                             |
| **Default value**              | 5                                                                                                                                                                                                                                                                                                                    |

_optimize_rewrite_delete_file_threshold_

|                                |                                                                                                                                                                                                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**                | Data optimization specific configuration. If there are<br>fewer delete files associated with a data file than the<br>threshold, the data file is not rewritten. This allows the<br>accumulation of more delete files for each data file for<br>cost saving. |
| **Allowed property<br>values** | A positive number. Must be less than 50.                                                                                                                                                                                                                    |
| **Default value**              | 2                                                                                                                                                                                                                                                           |

_vacuum_min_snapshots_to_keep_

|                                |                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**                | Minimum number of snapshots to retain on a table's<br>main branch.<br>This value takes precedence over the<br>`vacuum_max_snapshot_age_seconds`<br>property. If the minimum remaining snapshots are older<br>than the age specified by<br>`vacuum_max_snapshot_age_seconds`, the<br>snapshots are kept, and the value of<br>`vacuum_max_snapshot_age_seconds` is<br>ignored. |
| **Allowed property<br>values** | A positive number.                                                                                                                                                                                                                                                                                                                                                           |
| **Default value**              | 1                                                                                                                                                                                                                                                                                                                                                                            |

_vacuum_max_snapshot_age_seconds_

|                                |                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**                | Maximum age of the snapshots to retain on the main<br>branch. This value is ignored if the remaining minimum of<br>snapshots specified by<br>`vacuum_min_snapshots_to_keep` are older than<br>the age specified. This table behavior property corresponds<br>to the `history.expire.max-snapshot-age-ms`<br>property in Apache Iceberg configuration. |
| **Allowed property<br>values** | A positive number.                                                                                                                                                                                                                                                                                                                                    |
| **Default value**              | 432000 seconds (5 days)                                                                                                                                                                                                                                                                                                                               |

_vacuum_max_metadata_files_to_keep_

|                                |                                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| **Description**                | The maximum number of previous metadata files to retain<br>on the table's main branch. |
| **Allowed property<br>values** | A positive number.                                                                     |
| **Default value**              | 100                                                                                    |

### Example CREATE

TABLE statement

The following example creates an Iceberg table that has three columns.

```
CREATE TABLE iceberg_table (
  id int,
  data string,
  category string)
PARTITIONED BY (category, bucket(16,id))
LOCATION 's3://amzn-s3-demo-bucket/`iceberg-folder`'
TBLPROPERTIES (
  'table_type'='ICEBERG',
  'format'='parquet',
  'write_compression'='snappy',
  'optimize_rewrite_delete_file_threshold'='10'
)
```

## Use CREATE TABLE AS SELECT

(CTAS)

For information about creating an Iceberg table using the `CREATE TABLE
 AS` statement, see [CREATE TABLE AS](create-table-as.md "create-table-as.md"), with particular attention to the [CTAS table properties](create-table-as.md#ctas-table-properties "create-table-as.md#ctas-table-properties")
section.

## Use an AWS Glue

crawler

You can use an AWS Glue crawler to automatically register your Iceberg tables into
the AWS Glue Data Catalog. If you want to migrate from another Iceberg catalog, you can create
and schedule an AWS Glue crawler and provide the Amazon S3 paths where the Iceberg tables
are located. You can specify the maximum depth of the Amazon S3 paths that the AWS Glue
crawler can traverse. After you schedule an AWS Glue crawler, the crawler extracts
schema information and updates the AWS Glue Data Catalog with the schema changes every time it
runs. The AWS Glue crawler supports schema merging across snapshots and updates the
latest metadata file location in the AWS Glue Data Catalog. For more information, see [Data Catalog
and crawlers in AWS Glue](../../../glue/latest/dg/catalog-and-crawler.md "../../../glue/latest/dg/catalog-and-crawler.md").
