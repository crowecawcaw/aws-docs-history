# Considerations and

limitations

Consider the following considerations and limitations when you use Lake Formation with
EMR Serverless.

###### Note

When you enable Lake Formation for a Spark job on EMR Serverless, the job launches a system
driver and a user driver. If you specified pre-initialized capacity at launch, the
drivers provision from the pre-initialized capacity, and the number of system drivers
is equal to the number of user drivers that you specify. If you choose On Demand
capacity, EMR Serverless launches a system driver in addition to a user driver. To
estimate the costs associated with your EMR Serverless with Lake Formation job, use the
[AWS Pricing Calculator](https://calculator.aws/#/addService/EMR "https://calculator.aws/#/addService/EMR").

Amazon EMR Serverless with Lake Formation is available in all supported [EMR Serverless Regions](considerations.md "considerations.md").

- Amazon EMR Serverless supports fine-grained access control via Lake Formation for read operations with Apache Hive, Apache Iceberg, Delta Lake and Hudi tables. Apache Hive
  formats include Parquet, ORC, and xSV.
- Lake Formation-enabled applications don’t support usage of [customized EMR Serverless images](application-custom-image.md "application-custom-image.md").
- You can't turn off `DynamicResourceAllocation` for Lake Formation jobs.
- You can only use Lake Formation with Spark jobs.
- EMR Serverless with Lake Formation only supports a single Spark session throughout a
  job.
- EMR Serverless with Lake Formation only supports cross-account table
  queries shared through resource links.
- The following aren't supported:
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Write with Lake Formation granted permissions
  - Access control for nested columns

- EMR Serverless blocks functionalities that might undermine the complete
  isolation of system driver, including the following:
  - UDTs, HiveUDFs, and any user-defined function that involves custom
    classes
  - Custom data sources
  - Supply of additional jars for Spark extension, connector, or
    metastore
  - `ANALYZE TABLE` command

- To enforce access controls, `EXPLAIN PLAN` and DDL operations such as `DESCRIBE TABLE` don't expose restricted information.
- EMR Serverless restricts access to system driver Spark logs on Lake Formation-enabled applications.
  Since the system driver runs with elevated permissions, events and logs that the system driver
  generates can include sensitive information. To prevent unauthorized users or code
  from accessing this sensitive data, EMR Serverless disables access to system driver logs.

System profile logs are always persisted in managed storage – this is a mandatory setting that cannot be disabled. These logs are stored securely and
encrypted using either a Customer Managed KMS key or an AWS Managed KMS key.

If your EMR Serverless application
is in a private subnet with VPC endpoints for Amazon S3 and you attach an endpoint policy to control access, before your
jobs can send log data to AWS Managed Amazon S3, include the permissions detailed in [Managed storage](logging.md#jobs-log-storage-managed-storage "logging.md#jobs-log-storage-managed-storage")
in your VPC policy to S3 gateway endpoint. For troubleshooting requests, contact AWS support.

- If you registered a table location with Lake Formation, the data access path goes
  through the Lake Formation stored credentials regardless of the IAM permission for the
  EMR Serverless job runtime role. If you misconfigure the role registered with
  table location, jobs submitted that use the role with S3 IAM permission to the
  table location will fail.
- Writing to a Lake Formation table uses IAM permission rather than Lake Formation granted
  permissions. If your job runtime role has the necessary S3 permissions, you can
  use it to run write operations.
- Starting with Amazon EMR 7.9.0, Spark FGAC supports S3AFileSystem when used with the s3a:// scheme.
  The following are considerations and limitations when using Apache Iceberg:

- You can only use Apache Iceberg with session catalog and not arbitrarily named catalogs.
- Iceberg tables that are registered in Lake Formation only support the metadata tables `history`,
  `metadata_log_entries`, `snapshots`, `files`, `manifests`, and `refs`. Amazon EMR
  hides the columns that might have sensitive data, such as `partitions`, `path`, and `summaries`.
  This limitation doesn't apply to Iceberg tables that aren't registered in Lake Formation.
- Tables that you don't register in Lake Formation support all Iceberg stored procedures. The `register_table`
  and `migrate` procedures aren't supported for any tables.
- We suggest that you use Iceberg DataFrameWriterV2 instead of V1.
