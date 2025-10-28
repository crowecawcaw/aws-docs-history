# Considerations and

limitations

Consider the following considerations and limitations when you use Lake Formation with
AWS Glue.

AWS Glue with Lake Formation is available in all supported Regions except AWS GovCloud (US-East) and AWS GovCloud (US-West).

- AWS Glue supports fine-grained access control via Lake Formation only for Apache Hive and Apache Iceberg tables. Apache Hive
  formats include Parquet, ORC, and CSV.
- You can only use Lake Formation with Spark jobs.
- AWS Glue with Lake Formation only supports a single Spark session throughout a job.
- When Lake Formation is enabled,AWS Glue requires a greater number of workers because it requires one system driver, system executors, one user driver, and optionally user executors (required when your job has UDFs or `spark.createDataFrame`).
- AWS Glue with Lake Formation only supports cross-account table
  queries shared through resource links. The resource-link needs to be named identically to the source account's resource.
- To enable fine-grained access control for AWS Glue jobs, pass the `--enable-lakeformation-fine-grained-access` job parameter.
- You can configure your AWS Glue jobs to work with the AWS Glue multi-catalog hierarchy. For information on the configuration parameters to use with the AWS Glue `StartJobRun` API, see [Working with AWS Glue multi-catalog hierarchy on EMR Serverless](../../../emr/latest/EMR-Serverless-UserGuide/external-metastore-glue-multi.md "../../../emr/latest/EMR-Serverless-UserGuide/external-metastore-glue-multi.md").
- The following aren't supported:
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Write with Lake Formation granted permissions
  - Access control for nested columns

- AWS Glue blocks functionalities that might undermine the complete
  isolation of system driver, including the following:
  - UDTs, HiveUDFs, and any user-defined function that involves custom
    classes
  - Custom data sources
  - Supply of additional jars for Spark extension, connector, or
    metastore
  - `ANALYZE TABLE` command

- To enforce access controls, `EXPLAIN PLAN` and DDL operations such as `DESCRIBE TABLE` don't expose restricted information.
- AWS Glue restricts access to system driver Spark logs on Lake Formation-enabled applications.
  Since the system driver runs with more access, events and logs that the system driver
  generates can include sensitive information. To prevent unauthorized users or code
  from accessing this sensitive data, AWS Glue disabled access to system driver logs. For
  troubleshooting, contact AWS support.
- If you registered a table location with Lake Formation, the data access path goes
  through the Lake Formation stored credentials regardless of the IAM permission for the
  AWS Glue job runtime role. If you misconfigure the role registered with
  table location, jobs submitted that use the role with S3 IAM permission to the
  table location will fail.
- Writing to a Lake Formation table uses IAM permission rather than Lake Formation granted
  permissions. If your job runtime role has the necessary S3 permissions, you can
  use it to run write operations.
  The following are considerations and limitations when using Apache Iceberg:

- You can only use Apache Iceberg with session catalog and not arbitrarily named catalogs.
- Iceberg tables that are registered in Lake Formation only support the metadata tables `history`,
  `metadata_log_entries`, `snapshots`, `files`, `manifests`, and `refs`. AWS Glue
  hides the columns that might have sensitive data, such as `partitions`, `path`, and `summaries`.
  This limitation doesn't apply to Iceberg tables that aren't registered in Lake Formation.
- Tables that you don't register in Lake Formation support all Iceberg stored procedures. The `register_table`
  and `migrate` procedures aren't supported for any tables.
- We recommend that you use Iceberg DataFrameWriterV2 instead of V1.

## Example worker allocation

For a job configured with the following parameters:

```
--enable-lakeformation-fine-grained-access=true
--number-of-workers=20

```

The worker allocation would be:

- One worker for the user driver.
- One worker for the system driver.
- 10% of the remaining 18 workers (that is, 2 workers) reserved for the user executors.
- Up to 16 workers allocated for system executors.

With auto-scaling enabled, the user executors can utilize any of the unallocated capacity from the system executors if needed.

## Controlling user executor allocation

You can adjust the reservation percentage for user executors using the following configuration:

```
--conf spark.dynamicAllocation.maxExecutorsRatio=<value between 0 and 1>
```

This configuration allows fine-tuned control over how many user executors are reserved relative to the total available capacity.
