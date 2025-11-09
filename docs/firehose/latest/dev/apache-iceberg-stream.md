# Set up the Firehose stream

To create a Firehose stream with Apache Iceberg Tables as your destination you must
configure the following.

###### Note

The setup of a Firehose stream for delivering to tables in S3 table buckets is the same
as Apache Iceberg Tables in Amazon S3.

## Configure source and

destination

To deliver data to Apache Iceberg Tables, choose the source for your stream.

To configure your source for your stream, see [Configure source settings](configure-source.md "configure-source.md").

Next, choose **Apache Iceberg Tables** as the destination and
provide a Firehose stream name.

## Configure data

transformation

To perform custom transformations on your data, such as adding or modifying
records in your incoming stream, you can add a Lambda function to your Firehose stream.
For more information on data transformation using Lambda in a Firehose stream, see [Transform source data in Amazon Data Firehose](data-transformation.md "data-transformation.md").

For Apache Iceberg Tables, you must specify how you want to route incoming records
to different destination tables and the operations that you want to perform. One of
the ways to provide the required routing information to Firehose is using a Lambda
function.

For more information, see [Route
records to different Iceberg tables](apache-iceberg-format-input-record.md "apache-iceberg-format-input-record.md").

## Connect data catalog

Apache Iceberg requires a data catalog to write to Apache Iceberg Tables. Firehose
integrates with AWS Glue Data Catalog for Apache Iceberg Tables.

You can use AWS Glue Data Catalog in the same account as your Firehose stream or in a
cross-account and in the same Region as your Firehose stream (default), or in a different
Region.

If you are delivering to an Amazon S3 Table and you are using the console to
set up your Firehose stream, then select the catalog that corresponds to your
Amazon S3 Table catalog. If you are using the CLI to set up your Firehose stream,
then in the `CatalogConfiguration` input, use `CatalogARN`
with the format:
`arn:aws:glue:<region>:<account-id>:catalog/s3tablescatalog/<s3
 table bucket name>`. For more information, see [Setting up a Firehose stream to Amazon S3 tables](../../../AmazonS3/latest/userguide/s3-tables-integrating-firehose.md#firehose-stream-tables "../../../AmazonS3/latest/userguide/s3-tables-integrating-firehose.md#firehose-stream-tables").

###### Note

Firehose supports three operations for Iceberg tables: insert, update, and
delete. Without a specified operation, Firehosedefaults to insert, adding each
incoming record as a new row, and preserving duplicates. To modify existing
records instead, specify the "update" operation, which uses primary keys to
locate, and change existing rows.

Example:

- Default (insert): Multiple identical customer records create duplicate rows.
- Specified update: New customer address updates the existing record.

## Configure JQ expressions

For Apache Iceberg Tables, you must specify how you want to route incoming records
to different destination tables and the operations such as insert, update, and
delete that you want to perform. You can do this by configuring JQ expressions for
Firehose to parse and get the required information. For more information, see [Provide routing information to Firehose with
JSONQuery expression](apache-iceberg-format-input-record-different.md#apache-iceberg-route-jq "apache-iceberg-format-input-record-different.md#apache-iceberg-route-jq").

## Configure unique keys

**Updates and Deletes with more than one table**
– Unique keys are one or more fields in your source record that uniquely
identify a row in Apache Iceberg Tables. If you have insert only scenario with more
than one table, then you do not have to configure unique keys. If you want to do
updates and deletes on certain tables, then you must configure unique keys for those
required tables. Note that update will automatically insert the row if the row in
the tables is missing. If you have only a single table, then you can configure
unique keys. For an update operation, Firehose puts a delete file followed by an
insert.

You can either configure unique keys per table as a part of Firehose stream creation or
you can set [identifier-field-ids](https://iceberg.apache.org/spec/#identifier-field-ids "https://iceberg.apache.org/spec/#identifier-field-ids") natively in Iceberg during [create
table](https://iceberg.apache.org/docs/1.5.1/spark-ddl/#create-table "https://iceberg.apache.org/docs/1.5.1/spark-ddl/#create-table") or [alter table](https://iceberg.apache.org/docs/1.5.1/spark-ddl/#alter-table-set-identifier-fields "https://iceberg.apache.org/docs/1.5.1/spark-ddl/#alter-table-set-identifier-fields") operation. Configuring unique keys per table during stream
creation is optional. If you don’t configure unique keys per table during stream
creation, Firehose checks for `identifier-field-ids` for required tables and
will use them as unique keys. If both are not configured, then delivery of data with
update and delete operations fails.

To configure this section, provide the database name, table name, and unique keys
for the tables where you want to update or delete data. You can have only entry for
each table in the configuration. You don’t need to configure this section for append-only scenarios. Optionally, you can also choose to provide an error
bucket prefix if data from the table fails to deliver as shown in the following
example.

```
[
  {
    "DestinationDatabaseName": "MySampleDatabase",
    "DestinationTableName": "MySampleTable",
    "UniqueKeys": [
      "COLUMN_PLACEHOLDER"
    ],
    "S3ErrorOutputPrefix": "OPTIONAL_PREFIX_PLACEHOLDER"
  }
]
```

Firehose supports the configuration of unique keys if the supplied column name is unique across the entire table. However, it does not support fully qualified column names as unique keys. For instance, a key named `top._id` is not considered a unique key if the column name `_id` is also present at the top-level. If `_id` is unique across the entire table, then it is utilized regardless of its location within the table structure. This is whether it's a top-level column or a nested column. In the following example, `_id` is a valid unique key for the schema because the column name is unique across the schema.

```
[
 "schema": {
  "type": "struct",
  "fields": [
    {
      "name": "top",
      "type": {
        "type": "struct",
        "fields": [
          { "name": "_id", "type": "string" },
          { "name": "name", "type": "string" }
        ]
      }
    },
    { "name": "user", "type": "string" }
  ]
}
]
```

In the following example, `_id` is not a valid unique key for the schema because it is used in both the top-level column, and the nested struct.

```
[
"schema": {
  "type": "struct",
  "fields": [
    {
      "name": "top",
      "type": {
        "type": "struct",
        "fields": [
          { "name": "_id", "type": "string" },
          { "name": "name", "type": "string" }
        ]
      }
    },
    { "name": "_id", "type": "string" }
  ]
}
]
```

## Specify retry

duration

You can use this configuration to specify the duration in seconds for which Firehose
should attempt to retry, if it encounters failures in writing to Apache Iceberg
Tables in Amazon S3. You can set any value from 0 to 7200 seconds for performing retries.
By default, Firehose retries for 300 seconds.

## Handle failed delivery or

processing

You must configure Firehose to deliver records to an S3 backup bucket in case it
encounters failures in processing or delivering a stream after expiry of retry
duration. For this, configure the **S3 backup bucket** and
**S3 backup bucket error output prefix** from **Backup
settings** in console.

## Handle errors

Firehose sends all delivery errors to CloudWatch Logs, and Amazon S3 error buckets.

List of errors:

| **Error Message**          | \***\*Description\*\***                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `Iceberg.NoSuchTable`      | Firehose is writing to a table that doesn't exist, or the table<br>is not in V2 format. Firehose doesn't support tables in V1 format. |
| `Iceberg.InvalidTableName` | A null or empty table name is passed, or the table is not in<br>V2 format. Firehosedoesn't support tables in V1 format.               |
| `S3.AccessDenied`          | Ensure that the IAM role created in the prerequisites step has<br>the required permissions, and trust policy.                         |
| `Glue.AccessDenied`        | Ensure that the IAM role created in the prerequisites step has<br>the required permissions, and trust policy.                         |

## Configure buffer hints

Firehose buffers incoming streaming data in memory to a certain size
(**Buffering size**) and for a certain period of time
(**Buffering interval**) before delivering it to Apache Iceberg
Tables. You can choose a buffer size of 1–128 MiBs and a buffer interval of 0–900
seconds. Higher buffer hints results in a lower number of S3 writes, less cost of
compaction due to larger data files, and faster query runtime, but with a higher
latency. Lower buffer hint values deliver the data with lower latency.

## Configure advanced

settings

You can configure server-side encryption, error logging, permissions, and tags for
your Apache Iceberg Tables. For more information, see [Configure advanced settings](create-configure-advanced.md "create-configure-advanced.md").
You must add the IAM role that you created as part of the [Prerequisites to use Apache Iceberg Tables as a
destination](apache-iceberg-prereq.md "apache-iceberg-prereq.md"). Firehose will assume the role to access AWS Glue
tables and write to Amazon S3 buckets.

Firehose stream creation can take several minutes to complete. After you successfully
create the Firehose stream, you can start ingesting data into it and can view the data in
Apache Iceberg tables.
