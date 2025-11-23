# Considerations for Amazon EMR with Lake Formation

Amazon EMR with Lake Formation is available in all [available
regions](emr-plan-region.md "emr-plan-region.md").

## Considerations for Amazon EMR with Lake Formation

for version 7.9 and earlier

Consider the following when using AWS Lake Formation on EMR 7.9 and earlier
versions.

- [Fine-grained access control](emr-lf-enable.md#emr-lf-fgac-perms "emr-lf-enable.md#emr-lf-fgac-perms")
  at row, column, and cell level is available on clusters with Amazon EMR
  releases 6.15 and higher.
- Users with access to a table can access all the properties of that
  table. If you have Lake Formation based access control on a table, review the
  table to make sure that the properties don't contain any sensitive data
  or information.
- Amazon EMR clusters with Lake Formation don't support Spark's fallback to HDFS when
  Spark collects table statistics. This ordinarily helps optimize query
  performance.
- Operations that support access controls based on Lake Formation with
  non-governed Apache Spark tables include `INSERT INTO` and
  `INSERT OVERWRITE`.
- Operations that support access controls based on Lake Formation with Apache
  Spark and Apache Hive include `SELECT`,
  `DESCRIBE`, `SHOW DATABASE`, `SHOW
TABLE`, `SHOW COLUMN`, and `SHOW
PARTITION`.
- Amazon EMR doesn't support access control to the following Lake Formation based
  operations:
  - Writes to governed tables
  - Amazon EMR doesn't support `CREATE TABLE`. Amazon EMR 6.10.0
    and higher supports `ALTER TABLE`.
  - DML statements other than `INSERT` commands.

- There are performance differences between the same query with and
  without Lake Formation based access control.
- You can only use Amazon EMR with Lake Formation for Spark jobs.
- Trusted Identity propagation is not supported with multi-catalog
  hierarchy in Glue Data Catalog. For more information, see [Working with a
  multi-catalog hierarchy in AWS Glue Data Catalog](../ReleaseGuide/emr-multi-catalog.md "../ReleaseGuide/emr-multi-catalog.md").

## Considerations for Amazon EMR with Lake Formation for

version 7.10 and later

Consider the following when using Amazon EMR with AWS Lake Formation on EMR 7.10 and later
versions.

- Amazon EMR supports fine-grained access control via Lake Formation only for Apache
  Hive, Apache Iceberg, Apache Delta and Apache Hudi tables. Apache Hive
  formats include Parquet, ORC, and xSV CSV.
- For Lake Formation–enabled applications, Spark logs are written to Amazon S3 in two
  groups: system space logs and user space logs. System space logs may
  contain sensitive information such as the full table schema. To
  safeguard this data, Amazon EMR stores system space logs in a separate
  location from user space logs. It is strongly recommended that account
  administrators do not grant users access to system space logs.
- If you register a table location with Lake Formation, data access will be
  controlled exclusively by the permissions of the role used for
  registration, rather than by the Amazon EMR job runtime role. If the
  registration role is misconfigured, jobs that attempt to access the
  table will fail.
- You can't turn off `DynamicResourceAllocation` for Lake Formation
  jobs.
- You can only use Lake Formation with Spark jobs.
- Amazon EMR with Lake Formation only supports a single Spark session throughout a
  job.
- Amazon EMR with Lake Formation only supports cross-account table queries shared
  through resource links.
- The following aren't supported:
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Write with Lake Formation granted permissions
  - Access control for nested columns

- Amazon EMR blocks functionalities that might undermine the complete
  isolation of system driver, including the following:
  - UDTs, HiveUDFs, and any user-defined function that involves
    custom classes
  - Custom data sources
  - Supply of additional jars for Spark extension, connector, or
    metastore
  - `ANALYZE TABLE` command

- To enforce access controls, `EXPLAIN PLAN` and DDL
  operations such as `DESCRIBE TABLE` don't expose restricted
  information.
- Amazon EMR restricts access to system driver Spark logs on Lake Formation-enabled
  applications. Since the system driver runs with elevated permissions,
  events and logs that the system driver generates can include sensitive
  information. To prevent unauthorized users or code from accessing this
  sensitive data, Amazon EMR disables access to system driver logs.

System profile logs are always persisted in managed storage –
this is a mandatory setting that cannot be disabled. These logs are
stored securely and encrypted using either a Customer Managed KMS key or
an AWS Managed KMS key.

If your Amazon EMR application is in a private subnet with VPC endpoints
for Amazon S3 and you attach an endpoint policy to control access, before
your jobs can send log data to AWS Managed Amazon S3, you must include the
permissions detailed in [Managed
storage](logging.md#jobs-log-storage-managed-storage "logging.md#jobs-log-storage-managed-storage") in your VPC policy to S3 gateway endpoint. For
troubleshooting requests, contact AWS support.

- If you registered a table location with Lake Formation, the data access path
  goes through the Lake Formation stored credentials regardless of the IAM
  permission for the Amazon EMR job runtime role. If you misconfigure the role
  registered with table location, jobs submitted that use the role with S3
  IAM permission to the table location will fail.
- Writing to a Lake Formation table uses IAM permission rather than Lake Formation granted
  permissions. If your job runtime role has the necessary S3 permissions,
  you can use it to run write operations.

The following are considerations and limitations when using Apache
Iceberg:

- You can only use Apache Iceberg with session catalog and not
  arbitrarily named catalogs.
- Iceberg tables that are registered in Lake Formation only support the metadata
  tables `history`, `metadata_log_entries`,
  `snapshots`, `files`, `manifests`,
  and `refs`. Amazon EMR hides the columns that might have sensitive
  data, such as `partitions`, `path`, and
  `summaries`. This limitation doesn't apply to Iceberg
  tables that aren't registered in Lake Formation.
- Tables that you don't register in Lake Formation support all Iceberg stored
  procedures. The `register_table` and `migrate`
  procedures aren't supported for any tables.
- We recommend that you use Iceberg DataFrameWriterV2 instead of
  V1.

## Considerations for Amazon EMR with Lake Formation for version 7.12

and later

### General

Review the following limitations when using Lake Formation with Amazon EMR .

- You can't turn off `DynamicResourceAllocation` for Lake Formation
  jobs.
- You can only use Lake Formation with Spark jobs.
- Amazon EMR with Lake Formation only supports a single Spark session throughout a
  job.
- Amazon EMR with Lake Formation only supports cross-account table queries shared
  through resource links.
- The following aren't supported:
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Access control for nested columns

- Amazon EMR blocks functionalities that might undermine the complete
  isolation of system driver, including the following:
  - UDTs, HiveUDFs, and any user-defined function that involves
    custom classes
  - Custom data sources
  - Supply of additional jars for Spark extension, connector, or
    metastore
  - `ANALYZE TABLE` command

- If your Amazon EMR application is in a private subnet with VPC endpoints for Amazon S3 and you
  attach an endpoint policy to control access, before your jobs can send
  log data to AWS Managed Amazon S3, you must include the permissions
  detailed in [Managed storage](logging.md#jobs-log-storage-managed-storage "logging.md#jobs-log-storage-managed-storage") in your VPC policy to S3 gateway endpoint.
  For troubleshooting requests, contact AWS support.
- Starting with Amazon EMR 7.9.0, Spark FGAC supports S3AFileSystem when
  used with the s3a:// scheme.
- Amazon EMR 7.11 supports creating managed tables using CTAS.
- Amazon EMR 7.12 supports creating managed and external tables using
  CTAS.

## Permissions

- To enforce access controls, EXPLAIN PLAN and DDL operations such as
  DESCRIBE TABLE don't expose restricted information.
- When you register a table location with Lake Formation, data access
  uses Lake Formation stored credentials instead of the EMR Serverless job
  runtime role's IAM permissions. Jobs will fail if the registered role
  for table location is misconfigured, even when the runtime role has S3
  IAM permissions for that location.
- Starting with Amazon EMR 7.12, you can write to existing Hive and
  Iceberg tables using DataFrameWriter (V2) with Lake Formation
  credentials in append mode. For overwrite operations or when creating
  new tables, EMR uses the runtime role credentials to modify table
  data.
- The following limitations apply when using views or cached tables as
  source data (these limitations do not apply to AWS Glue Data Catalog
  views):
  - For MERGE, DELETE, and UPDATE operations
    - Supported: Using views and cached tables as source
      tables.
    - Not supported: Using views and cached tables in
      assignment and condition clauses.

  - For CREATE OR REPLACE and REPLACE TABLE AS SELECT
    operations:
    - Not supported: Using views and cached tables as source
      tables.

- Delta Lake tables with UDFs in source data support MERGE, DELETE, and
  UPDATE operations only when deletion vector is enabled.

## Logs and debugging

- Amazon EMR restricts access to system driver Spark logs on Lake Formation-enabled
  applications. Since the system driver runs with elevated permissions,
  events and logs that the system driver generates can include sensitive
  information. To prevent unauthorized users or code from accessing this
  sensitive data, Amazon EMR disables access to system driver logs.

System profile logs are always persisted in managed storage –
this is a mandatory setting that cannot be disabled. These logs are
stored securely and encrypted using either a Customer Managed KMS key or
an AWS Managed KMS key.

## Iceberg

Review the following considerations when using Apache Iceberg:

- You can only use Apache Iceberg with session catalog and not
  arbitrarily named catalogs.
- Iceberg tables that are registered in Lake Formation only support the metadata
  tables `history`, `metadata_log_entries`,
  `snapshots`, `files`, `manifests`,
  and `refs`. Amazon EMR hides the columns that might have sensitive
  data, such as `partitions`, `path`, and
  `summaries`. This limitation doesn't apply to Iceberg
  tables that aren't registered in Lake Formation.
- Tables that not registered in Lake Formation support all Iceberg stored
  procedures. The `register_table` and `migrate`
  procedures aren't supported for any tables.
- We suggest that you use Iceberg DataFrameWriterV2 instead of
  V1.
