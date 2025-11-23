# Considerations and

limitations

## General

Review the following limitations when using Lake Formation with EMR Serverless.

###### Note

When you enable Lake Formation for a Spark job on EMR Serverless, the job launches a system
driver and a user driver. If you specified pre-initialized capacity at launch, the
drivers provision from the pre-initialized capacity, and the number of system drivers
is equal to the number of user drivers that you specify. If you choose On Demand
capacity, EMR Serverless launches a system driver in addition to a user driver. To
estimate the costs associated with your EMR Serverless with Lake Formation job, use the
[AWS Pricing Calculator](https://calculator.aws/#/addService/EMR "https://calculator.aws/#/addService/EMR").

- Amazon EMR Serverless with Lake Formation is available in all supported [EMR Serverless
  Regions](considerations.md "considerations.md").

- Lake Formation-enabled applications don’t support usage of [customized EMR Serverless images](application-custom-image.md "application-custom-image.md").
- You can't turn off `DynamicResourceAllocation` for Lake Formation
  jobs.
- You can only use Lake Formation with Spark jobs.
- EMR Serverless with Lake Formation only supports a single Spark session throughout a
  job.
- EMR Serverless with Lake Formation only supports cross-account table queries shared
  through resource links.
- The following aren't supported:
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Access control for nested columns

- EMR Serverless blocks functionalities that might undermine the complete
  isolation of system driver, including the following:
  - UDTs, HiveUDFs, and any user-defined function that involves custom
    classes
  - Custom data sources
  - Supply of additional jars for Spark extension, connector, or
    metastore
  - `ANALYZE TABLE` command

- If your EMR Serverless application is in a private subnet with VPC endpoints
  for Amazon S3 and you attach an endpoint policy to control access, before your jobs
  can send log data to AWS Managed Amazon S3, include the permissions detailed in
  [Managed
  storage](logging.md#jobs-log-storage-managed-storage "logging.md#jobs-log-storage-managed-storage") in your VPC policy to S3 gateway endpoint. For
  troubleshooting requests, contact AWS support.
- Starting with Amazon EMR 7.9.0, Spark FGAC supports S3AFileSystem when used
  with the s3a:// scheme.
- Amazon EMR 7.11 supports creating managed tables using CTAS.
- Amazon EMR 7.12 supports creating managed and external tables using
  CTAS.

## Permissions

- To enforce access controls, EXPLAIN PLAN and DDL operations such as DESCRIBE
  TABLE don't expose restricted information.
- When you register a table location with Lake Formation, data access uses Lake
  Formation stored credentials instead of the EMR Serverless job runtime role's
  IAM permissions. Jobs will fail if the registered role for table location is
  misconfigured, even when the runtime role has S3 IAM permissions for that
  location.
- Starting with Amazon EMR 7.12, you can write to existing Hive and Iceberg
  tables using DataFrameWriter (V2) with Lake Formation credentials in append
  mode. For overwrite operations or when creating new tables, EMR uses the runtime
  role credentials to modify table data.
- The following limitations apply when using views or cached tables as source
  data (these limitations do not apply to AWS Glue Data Catalog views):
  - For MERGE, DELETE, and UPDATE operations
    - Supported: Using views and cached tables as source
      tables.
    - Not supported: Using views and cached tables in assignment and
      condition clauses.

  - For CREATE OR REPLACE and REPLACE TABLE AS SELECT operations:
    - Not supported: Using views and cached tables as source
      tables.

- Delta Lake tables with UDFs in source data support MERGE, DELETE, and UPDATE
  operations only when deletion vector is enabled.

## Logs and debugging

- EMR Serverless restricts access to system driver Spark logs on Lake Formation-enabled
  applications. Since the system driver runs with elevated permissions, events and
  logs that the system driver generates can include sensitive information. To
  prevent unauthorized users or code from accessing this sensitive data,
  EMR Serverless disables access to system driver logs.
- System profile logs are always persisted in managed storage – this is a
  mandatory setting that cannot be disabled. These logs are stored securely and
  encrypted using either a Customer Managed KMS key or an AWS Managed KMS
  keys.

## Iceberg

Review the following considerations when using Apache Iceberg:

- You can only use Apache Iceberg with session catalog and not arbitrarily named catalogs.
- Iceberg tables that are registered in Lake Formation only support the metadata tables `history`,
  `metadata_log_entries`, `snapshots`, `files`, `manifests`, and `refs`. Amazon EMR
  hides the columns that might have sensitive data, such as `partitions`, `path`, and `summaries`.
  This limitation doesn't apply to Iceberg tables that aren't registered in Lake Formation.
- Tables that not registered in Lake Formation support all Iceberg stored procedures. The
  `register_table` and `migrate` procedures aren't
  supported for any tables.
- We suggest that you use Iceberg DataFrameWriterV2 instead of V1.
