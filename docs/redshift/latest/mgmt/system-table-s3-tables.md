Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# System table integration with S3 Tables

Use system table integration with [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/ "https://aws.amazon.com/s3/features/tables/") to retain your Amazon Redshift [system table](../dg/serverless_views-monitoring.md "../dg/serverless_views-monitoring.md") data beyond the 7-day in-cluster
retention period. This helps you meet compliance, auditing, and observability requirements. When you enable this feature, Redshift
writes system table logs to S3 Tables in [Apache Iceberg](https://aws.amazon.com/what-is/apache-iceberg/ "https://aws.amazon.com/what-is/apache-iceberg/") format and manages
partitioning, compaction, and snapshot maintenance. You can keep this data for as
long as you need for analysis and auditing. Because the data is stored in open
Iceberg format, you can query it with Redshift, [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"), or any other
Iceberg-compatible engine. You can also use AI agent skills for natural-language
queries (see [System table skills for AWS Agent Toolkit](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/system-table-skills "https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/system-table-skills") on the GitHub website).

When you enable this feature through the console, the Redshift CLI, or SDK, Redshift begins
writing new rows from the system tables you select to S3 Tables
shortly thereafter at a fixed frequency. You choose which system tables to
publish; S3 Tables enforces the retention duration that you configure.

This supports the following use cases:

- **Meet compliance and audit requirements**. Retain query, connection, and
  change history for months or years.
- **Monitor your fleet from one place**. Consolidate monitoring data from
  multiple data warehouses in your account and Region and analyze activity
  across your fleet.
- **Remove the need for custom extract, transform, and load (ETL) pipelines**. Stop
  building and maintaining jobs that export system table data to S3 for longer
  retention.
- **Investigate past incidents**. Query historical data beyond the 7-day
  in-cluster window for root cause analysis, post-incident review, and
  monitoring workload evolution and performance trends over time.
  This feature is available for Amazon Redshift Provisioned [RA3](https://aws.amazon.com/redshift/features/ra3/ "https://aws.amazon.com/redshift/features/ra3/") and [RG](https://aws.amazon.com/redshift/features/rg/ "https://aws.amazon.com/redshift/features/rg/") instances
  and [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/ "https://aws.amazon.com/redshift/redshift-serverless/") in all AWS commercial Regions where Redshift and
  S3 Tables are supported. In this topic, _data warehouse_ refers to either a
  provisioned cluster or a Redshift Serverless workgroup.

###### Topics

- [How it works](#system-table-s3-tables-how-it-works "#system-table-s3-tables-how-it-works")
- [Enabling system table integration with S3 Tables](#system-table-s3-tables-enabling "#system-table-s3-tables-enabling")
- [Supported system tables](#system-table-s3-tables-supported-tables "#system-table-s3-tables-supported-tables")
- [Metadata columns added to each table](#system-table-s3-tables-metadata-columns "#system-table-s3-tables-metadata-columns")
- [Configuring retention](#system-table-s3-tables-retention "#system-table-s3-tables-retention")
- [Data governance](#system-table-s3-tables-data-governance "#system-table-s3-tables-data-governance")
- [Delivery and lifecycle behavior](#system-table-s3-tables-lifecycle "#system-table-s3-tables-lifecycle")
- [Best practices](#system-table-s3-tables-best-practices "#system-table-s3-tables-best-practices")
- [Billing](#system-table-s3-tables-billing "#system-table-s3-tables-billing")
- [Considerations and limitations](#system-table-s3-tables-considerations "#system-table-s3-tables-considerations")

## How it works

After you enable the feature and select one or more supported system tables,
Redshift writes newly completed records from those system tables to S3 Tables. Data is delivered in batches at a fixed frequency.

The system tables live in your AWS account but are _service-managed_: AWS owns
and operates the data delivery and table management, including the following:

- Creating the S3 table bucket, namespace, and S3 tables in your account.
- Defining and evolving the table schemas.
- Writing data in Apache Iceberg format to S3 tables.
- Compacting data and maintaining snapshots (handled automatically by S3 Tables).

There is no infrastructure to build or maintain and no impact to your workloads.

You configure how long to retain the data through S3 Tables record expiration.
For more information, see [Configuring retention](#system-table-s3-tables-retention "#system-table-s3-tables-retention").

Because the tables are managed by AWS, you cannot modify or delete the rows that
Redshift delivers. The delivered data is immutable. You only control read access to
the tables. For more information, see [Data governance](#system-table-s3-tables-data-governance "#system-table-s3-tables-data-governance").

Only completed activity is delivered to S3 Tables. The system tables in your data warehouse can show in-flight activity, but only records that have reached a final state are copied. For example, a completed, aborted, or canceled query is delivered, but a query that is still running is not delivered until it reaches a final state.

## Enabling system table integration with S3 Tables

To enable system table integration with S3 Tables, use the
existing Redshift APIs with a new log destination type of `s3table`. When
enabled, Redshift creates an S3 table bucket named `aws-redshift` in your
account. You manage the feature with the same operations you use for other log
destinations: for provisioned clusters, `enable-logging`, `disable-logging`, and
`describe-logging-status`; for Redshift Serverless, `update-namespace` and
`get-namespace`.

### Permissions

The principal that enables, modifies, or disables the feature must have the
following permissions:

- `redshift:EnableLogging` (for provisioned clusters) or
  `redshift-serverless:UpdateNamespace` (for Redshift Serverless).
- Permission to create and configure the S3 table bucket. The enabling principal
  needs the following S3 Tables permissions:

  - `s3tables:CreateTableBucket`
  - `s3tables:PutTableBucketEncryption`
  - `s3tables:PutTableBucketPolicy`
    When you enable the feature, Redshift creates and configures the S3 table
    bucket using the identity of the principal who triggers the operation.

After the bucket is created, Redshift creates namespaces and tables within it
using a service trust relationship between Redshift and S3 Tables. The enabling
principal does not need permissions to create namespaces or tables.

### Deployment options

You can configure delivery in one of two patterns. A given data warehouse uses
one pattern at a time.

| Deployment Option | Description                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Per-warehouse** | Redshift writes each data warehouse's system table data to its own set of S3 tables. Every row in a table comes from a single data warehouse. Use this for physical isolation between warehouses.                                                                                                      |
| **Consolidated**  | Redshift writes system table data from multiple data warehouses within the same account and Region into a shared set of S3 tables. Rows from different warehouses are distinguished by the `warehouse_namespace_arn` and `warehouse_name` columns. Use this for centralized, cross-warehouse analysis. |

The deployment model determines how data is organized in S3 Tables. In the
per-warehouse model, the S3 Tables namespace name contains a unique identifier
for the data warehouse, so each warehouse's data is physically separated into its
own namespace. In the consolidated model, the S3 Tables namespace name contains
the AWS account number, and data from all warehouses in that account and Region is
stored together in the same namespace and tables.

Both options are supported within a **single AWS account and a single AWS
Region**. To analyze data across Regions or accounts, combine results from each
Region's or account's tables at query time. For cross-account access, you can use AWS Glue Data Catalog
sharing. For more information, see
[Granting cross-account access](../../../glue/latest/dg/cross-account-access.md "../../../glue/latest/dg/cross-account-access.md")
in the _AWS Glue Developer Guide_.

###### Note

If you switch a data warehouse from one deployment pattern to another, previously
delivered data remains in its existing table and is retained according to its
configured retention. Redshift begins delivering new data to the new target and
does not backfill historical data.

### Using the console

###### To configure system table integration with S3 Tables

1. Open the Redshift console and in the navigation pane, under **Amazon Redshift**
   or **Amazon Redshift Serverless**, choose **System table integrations**. You
   can also configure from the cluster or namespace detail page by choosing the
   **Integrations** tab, or by choosing **Actions**, **Integrations**,
   **Configure system table integration**.
2. Choose **Create System table integration**.
3. Select your provisioned cluster or Redshift Serverless workgroup.
4. Choose the system tables to publish. Select individual `SYS_*` views, or choose **Select all supported system tables** to publish all current and future supported views. If you select all, new views added in the future are automatically included without requiring a configuration change.
5. Select the deployment model:

   - **Individual S3 table per system table per data warehouse** to keep this warehouse's data in its own set of tables.
   - **Shared S3 table per system table across data warehouses** to consolidate data from multiple warehouses in the account into a shared set of tables.

6. Optionally, choose an encryption key. By default the data is encrypted with Amazon S3-managed keys (SSE-S3). To use your own AWS KMS key, select it here. If you use your own AWS KMS key, the key policy must grant Redshift and S3 Tables access to the key. For more information, see [Configuring encryption](#system-table-s3-tables-configuring-encryption "#system-table-s3-tables-configuring-encryption").
7. Save your changes. Redshift begins publishing the selected system tables to S3 Tables and continues to add new records on a recurring basis.

To stop publishing a system table, return to the settings and remove it. Data already published is retained until you configure expiration through S3 Tables.

You can review the status of the integration from the cluster or namespace detail page. Expand **View S3 table mapping** to see the mapping between each system table and its corresponding S3 table name and namespace. You can also view the published data from the S3 Tables console.

### Using the AWS CLI

The following parameters configure S3 Tables publishing:

| Parameter                | Applies to  | Description                                                                                                 |
| ------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------- |
| `--log-destination-type` | Both        | Set to `s3table` to publish to S3 Tables. Other values are `s3` and `cloudwatch`.                           |
| `--log-exports`          | Provisioned | The system tables to publish, as a list of `SYS_*` view names, or `all`.                                    |
| `--s3-table-names`       | Serverless  | The system tables to publish, as a list of `SYS_*` view names, or `all`.                                    |
| `--s3-table-action`      | Serverless  | `Enable` or `Disable` S3 Tables publishing.                                                                 |
| `--s3-table-granularity` | Both        | Table scope. Provisioned: `cluster` (default) or `account`. Serverless: `namespace` (default) or `account`. |
| `--s3-table-kms-key-id`  | Both        | Optional AWS KMS key ARN or ID for encryption. Defaults to Amazon S3-managed keys (SSE-S3).                 |

#### Provisioned clusters

**Enable delivery.** `--log-exports` accepts `all` or a space-separated list of
supported system tables, and `--s3-table-granularity` accepts `cluster` (per-warehouse) or
`account` (consolidated).

```
aws redshift enable-logging \
    --cluster-identifier my-redshift-cluster \
    --log-destination-type s3table \
    --log-exports all \
    --s3-table-granularity account
```

To enable delivery for specific system tables only:

```
aws redshift enable-logging \
    --cluster-identifier my-redshift-cluster \
    --log-destination-type s3table \
    --log-exports sys_query_history sys_query_text sys_userlog \
    --s3-table-granularity cluster
```

**Check delivery status.**

```
aws redshift describe-logging-status \
    --cluster-identifier my-redshift-cluster
```

**Disable delivery** for all system tables, or for specific tables with `--log-exports`:

```
aws redshift disable-logging \
    --cluster-identifier my-redshift-cluster \
    --log-destination-type s3table \
    --log-exports sys_stream_scan_states
```

#### Redshift Serverless

In Redshift Serverless, you configure the feature per namespace with
`update-namespace`. System table names are passed on `--s3-table-names` (not
`--log-exports`).

**Enable delivery.**

```
aws redshift-serverless update-namespace \
    --namespace-name my-namespace \
    --log-destination-type s3table \
    --s3-table-action Enable \
    --s3-table-names all \
    --s3-table-granularity namespace
```

**Disable delivery** for specific system tables (or `all`):

```
aws redshift-serverless update-namespace \
    --namespace-name my-namespace \
    --log-destination-type s3table \
    --s3-table-action Disable \
    --s3-table-names sys_stream_scan_states
```

**Check delivery status.**

```
aws redshift-serverless get-namespace \
    --namespace-name my-namespace
```

To resume delivery after the S3 table bucket or a table was dropped, run the
enable command again.

### Registering with AWS Glue Data Catalog

Before you can query the retained data with Redshift, Athena, or other
analytics services, the service-managed S3 table bucket must be integrated with
AWS Glue Data Catalog. This is a one-time step per account and Region. If you
have already integrated S3 Tables with AWS Glue Data Catalog, no additional
action is required.

For integration instructions, see
[Integrating Amazon S3 Tables with AWS Glue Data Catalog](../../../glue/latest/dg/glue-federation-s3tables.md "../../../glue/latest/dg/glue-federation-s3tables.md")
in the _AWS Glue Developer Guide_.

### Configuring encryption

By default, data delivered to S3 Tables is encrypted with Amazon S3-managed keys
(SSE-S3). To use an AWS KMS customer managed key instead, specify its ARN with
`--s3-table-kms-key-id` when you enable delivery:

```
aws redshift enable-logging \
    --cluster-identifier my-redshift-cluster \
    --log-destination-type s3table \
    --log-exports all \
    --s3-table-granularity account \
    --s3-table-kms-key-id arn:aws:kms:us-west-2:111122223333:key/`key-id`
```

If you use a customer managed key, its key policy must allow the Redshift system
table integration service principal to generate data keys when it writes your
system tables, and the S3 Tables maintenance service principal to use the
key during table maintenance (such as compaction). Add the following statements to
the key policy, replacing `REGION`, `ACCOUNT`, and `KEY_ID` with your own
values.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnableRedshiftSystemTableKeyUsage",
      "Effect": "Allow",
      "Principal": {
        "Service": "systemtables.redshift.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:`REGION`:`ACCOUNT`:key/`KEY_ID`",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`ACCOUNT`"
        }
      }
    },
    {
      "Sid": "EnableS3TableMaintenanceKeyUsage",
      "Effect": "Allow",
      "Principal": {
        "Service": "maintenance.s3tables.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:`REGION`:`ACCOUNT`:key/`KEY_ID`",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:`REGION`:`ACCOUNT`:bucket/aws-redshift/*"
        }
      }
    }
  ]
}
```

If the key policy does not grant these permissions, Redshift cannot write to the
encrypted S3 Tables and delivery fails.

## Supported system tables

You can select any of the following `SYS_*` monitoring views to integrate with S3
Tables. For a description of the columns in each view, choose the view name.

- [SYS\_ANALYZE\_COMPRESSION\_HISTORY](../dg/r_SYS_ANALYZE_COMPRESSION_HISTORY.md "../dg/r_SYS_ANALYZE_COMPRESSION_HISTORY.md")
- [SYS\_ANALYZE\_HISTORY](../dg/SYS_ANALYZE_HISTORY.md "../dg/SYS_ANALYZE_HISTORY.md")
- [SYS\_AUTOMATIC\_OPTIMIZATION](../dg/SYS_AUTOMATIC_OPTIMIZATION.md "../dg/SYS_AUTOMATIC_OPTIMIZATION.md")
- [SYS\_AUTO\_TABLE\_OPTIMIZATION](../dg/r_SYS_AUTO_TABLE_OPTIMIZATION.md "../dg/r_SYS_AUTO_TABLE_OPTIMIZATION.md")
- [SYS\_CHILD\_QUERY\_TEXT](../dg/SYS_CHILD_QUERY_TEXT.md "../dg/SYS_CHILD_QUERY_TEXT.md")
- [SYS\_CONNECTION\_LOG](../dg/SYS_CONNECTION_LOG.md "../dg/SYS_CONNECTION_LOG.md")
- [SYS\_COPY\_JOB\_INFO](../dg/SYS_COPY_JOB_INFO.md "../dg/SYS_COPY_JOB_INFO.md")
- [SYS\_COPY\_REPLACEMENTS](../dg/SYS_COPY_REPLACEMENTS.md "../dg/SYS_COPY_REPLACEMENTS.md")
- [SYS\_DATASHARE\_CHANGE\_LOG](../dg/SYS_DATASHARE_CHANGE_LOG.md "../dg/SYS_DATASHARE_CHANGE_LOG.md")
- [SYS\_DATASHARE\_USAGE\_CONSUMER](../dg/SYS_DATASHARE_USAGE_CONSUMER.md "../dg/SYS_DATASHARE_USAGE_CONSUMER.md")
- [SYS\_DATASHARE\_USAGE\_PRODUCER](../dg/SYS_DATASHARE_USAGE_PRODUCER.md "../dg/SYS_DATASHARE_USAGE_PRODUCER.md")
- SYS\_DATASHARE\_WRITE\_HISTORY
- [SYS\_EXTERNAL\_QUERY\_ERROR](../dg/SYS_EXTERNAL_QUERY_ERROR.md "../dg/SYS_EXTERNAL_QUERY_ERROR.md")
- [SYS\_INTEGRATION\_ACTIVITY](../dg/r_SYS_INTEGRATION_ACTIVITY.md "../dg/r_SYS_INTEGRATION_ACTIVITY.md")
- [SYS\_MV\_STATE](../dg/SYS_MV_STATE.md "../dg/SYS_MV_STATE.md")
- [SYS\_PROCEDURE\_MESSAGES](../dg/SYS_PROCEDURE_MESSAGES.md "../dg/SYS_PROCEDURE_MESSAGES.md")
- [SYS\_QUERY\_DETAIL](../dg/SYS_QUERY_DETAIL.md "../dg/SYS_QUERY_DETAIL.md")
- [SYS\_QUERY\_EXPLAIN](../dg/SYS_QUERY_EXPLAIN.md "../dg/SYS_QUERY_EXPLAIN.md")
- [SYS\_QUERY\_HISTORY](../dg/SYS_QUERY_HISTORY.md "../dg/SYS_QUERY_HISTORY.md")
- [SYS\_QUERY\_TEXT](../dg/SYS_QUERY_TEXT.md "../dg/SYS_QUERY_TEXT.md")
- [SYS\_SCHEMA\_QUOTA\_VIOLATIONS](../dg/r_SYS_SCHEMA_QUOTA_VIOLATIONS.md "../dg/r_SYS_SCHEMA_QUOTA_VIOLATIONS.md")
- [SYS\_SESSION\_HISTORY](../dg/SYS_SESSION_HISTORY.md "../dg/SYS_SESSION_HISTORY.md")
- [SYS\_SPATIAL\_SIMPLIFY](../dg/SYS_SPATIAL_SIMPLIFY.md "../dg/SYS_SPATIAL_SIMPLIFY.md")
- [SYS\_STREAM\_SCAN\_ERRORS](../dg/r_SYS_STREAM_SCAN_ERRORS.md "../dg/r_SYS_STREAM_SCAN_ERRORS.md")
- [SYS\_STREAM\_SCAN\_STATES](../dg/r_SYS_STREAM_SCAN_STATES.md "../dg/r_SYS_STREAM_SCAN_STATES.md")
- [SYS\_UNLOAD\_DETAIL](../dg/SYS_UNLOAD_DETAIL.md "../dg/SYS_UNLOAD_DETAIL.md")
- [SYS\_USERLOG](../dg/SYS_USERLOG.md "../dg/SYS_USERLOG.md")
- [SYS\_VACUUM\_HISTORY](../dg/SYS_VACUUM_HISTORY.md "../dg/SYS_VACUUM_HISTORY.md")

###### Note

The following views require [patch P203](cluster-versions.md#cluster-version-203 "cluster-versions.md#cluster-version-203") or later: SYS\_CHILD\_QUERY\_TEXT,
SYS\_COPY\_REPLACEMENTS, SYS\_EXTERNAL\_QUERY\_ERROR, SYS\_PROCEDURE\_MESSAGES,
SYS\_QUERY\_DETAIL, SYS\_QUERY\_EXPLAIN, SYS\_SPATIAL\_SIMPLIFY, and SYS\_UNLOAD\_DETAIL.
If you enable these views on a data warehouse running a patch earlier than P203, the
tables are created with the correct schema but contain no data until the data warehouse
is updated to P203 or later.

## Metadata columns added to each table

Each S3 table contains all of the columns from the source `SYS_*` view, plus
the following five metadata columns that Redshift adds to identify the
source of each row and when it was delivered.

| Column                     | Type              | Description                                                                                                                                  |
| -------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `warehouse_account_id`     | string            | The AWS account that owns the source data warehouse.                                                                                         |
| `warehouse_region_name`    | string            | The AWS Region in which the source data warehouse runs.                                                                                      |
| `warehouse_namespace_arn`  | string            | The ARN of the namespace for the source data warehouse. This is a stable, unique identifier that is immutable across renames and recreation. |
| `warehouse_name`           | string            | The human-readable name of the source data warehouse (cluster name or workgroup name).                                                       |
| `s3_tables_ingestion_time` | timestamp(6), UTC | The time at which Redshift committed the row to S3 Tables. This is the delivery time, not the time the underlying event occurred.            |

## Configuring retention

Redshift does not define a retention policy for the data it delivers to S3
Tables. You configure how long to keep the data by setting a record expiration
policy through S3 Tables. You specify the number of days (for example, 5
days, 100 days, or 365 days), and S3 Tables automatically removes data that ages
past the configured duration.

If you do not configure an expiration policy, data is kept indefinitely.

When you disable the integration or remove a system table, Redshift stops writing
new data but previously delivered data remains in S3 Tables and continues to be
subject to whatever expiration policy you have configured.

For more information, see
[Configuring record expiration for S3 table buckets](../../../AmazonS3/latest/userguide/s3-tables-record-expiration.md "../../../AmazonS3/latest/userguide/s3-tables-record-expiration.md")
in the _Amazon S3 User Guide_.

## Data governance

You govern access to the retained system table data; Redshift does not
apply read permissions on your behalf and does not mask data.

- **Access control**. After you integrate the S3 table bucket with AWS Glue Data Catalog, you can govern read access using [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM) or [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/"). In a
  consolidated deployment, you can scope read access per warehouse.
- **Cataloging and discovery**. The AWS Glue Data Catalog integration provides a
  central place to discover the retained tables and apply fine-grained
  permissions (for example, table-, column-, or row-level access with Lake Formation).

## Delivery and lifecycle behavior

- **Delivery frequency**. Data is delivered in batches at a fixed frequency.
- **Exactly-once delivery**. Each record is delivered once; re-enabling or
  re-adding a system table does not create duplicates.
- **Enable, disable, re-enable**. While the feature (or a specific system table) is
  disabled, no data is captured for that period. Disabling stops writes but does
  not remove the S3 Tables or previously delivered data. Re-enabling resumes
  delivery going forward and does not backfill the gap.
- **Removing a system table from your selection**. Redshift stops delivering new
  data for that system table. Previously delivered data remains in S3 Tables and is
  subject to any record expiration policy you have configured. Re-adding the system table
  resumes delivery without duplicating data.
- **Data warehouse deletion with in-flight data**. If you delete a data warehouse
  while delivery is in progress and the data warehouse's encryption key differs
  from the key used for S3 Tables, Redshift might continue to use the AWS KMS grant on
  the data warehouse's key for a short period after deletion to complete delivery
  of any remaining data.

### Checking delivery status

You can review the current configuration and the most recent delivery time per
system table at any time:

- **Provisioned clusters**. `describe-logging-status` (or `describe-cluster`)
  returns the active system tables, the S3 Tables namespace, the granularity, and the
  last ingestion time for each system table.
- **Redshift Serverless**. `get-namespace` returns the same information
  in the namespace's S3 Tables publish status.

### Redshift Serverless

Delivery does not keep a workgroup awake or consume your compute. Before the
workgroup pauses, Redshift ensures any pending batch is delivered.

## Best practices

1. **Assess your data sensitivity.** Understand what kind of data is stored within your data warehouse and whether the system tables contain sensitive information. Some system tables (such as SYS\_QUERY\_TEXT and SYS\_PROCEDURE\_MESSAGES) can capture literal values from your queries and stored procedures.
2. **Choose a deployment model.** If your data warehouse stores sensitive information, consider using the per-warehouse deployment model to keep each data warehouse's system table data physically isolated. If your data is not sensitive and you want to run cross-warehouse queries without combining results from multiple tables, use the consolidated deployment model.
3. **Select the system tables you need.** Review the list of supported system tables and choose the ones that match your compliance, audit, or observability requirements. You do not need to enable all system tables.
4. **Configure encryption before you enable the feature.** If you want to use a customer managed AWS KMS key, specify it when you first enable the feature. You cannot change the key after S3 Tables are created. To change the key, disable the feature, drop the S3 Tables using the S3 Tables API (this permanently deletes retained data), and then re-enable the feature with the new key.
5. **Set retention based on business requirements.** Configure the record expiration policy directly in S3 Tables at a table level, based on your compliance, audit, or operational needs. Different tables can have different retention durations. If you do not configure an expiration policy, data is kept indefinitely. To monitor storage usage for your system tables, see [Amazon S3 Tables CloudWatch metrics](../../../AmazonS3/latest/userguide/s3-tables-cloudwatch-metrics.md "../../../AmazonS3/latest/userguide/s3-tables-cloudwatch-metrics.md") in the _Amazon S3 User Guide_.

## Billing

Writing system table data to S3 Tables is free. You are charged for standard
S3 Tables storage and maintenance for the retained data, and for the query
engine you use to read the data, according to that engine's pricing. For more
information, see [Amazon S3 Tables pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Considerations and limitations

- Supported within a single AWS account and a single AWS Region. To analyze data
  across accounts or Regions, combine results at query time.
- A data warehouse uses one deployment pattern (per-warehouse or consolidated) at
  a time.
- Switching deployment patterns, disabling and re-enabling, or removing and
  re-adding a system table does not backfill historical data.
- Delivered data is immutable. You cannot modify or delete individual rows
  through Redshift.
- You can drop the S3 Tables created by this feature, but doing so permanently
  removes all retained data in those tables and stops delivery. Redshift
  does not automatically recreate dropped tables. To resume delivery, you must
  re-enable the feature, which creates new tables and begins delivering new data
  going forward. Previously delivered data is not restored. For more information,
  see [Deleting S3 tables](../../../AmazonS3/latest/userguide/s3-tables-delete.md "../../../AmazonS3/latest/userguide/s3-tables-delete.md")
  in the _Amazon S3 User Guide_.
- Delivery is batch-based (data is written at a fixed frequency).
- Querying from Redshift requires the S3 table bucket to be integrated with
  AWS Glue Data Catalog.
