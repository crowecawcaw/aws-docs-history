# Migrating AWS Glue for Spark jobs to

AWS Glue version 5.1

This topic describes the changes between AWS Glue versions 0.9, 1.0, 2.0, 3.0, 4.0 and
5.0 to allow you to migrate your Spark applications and ETL jobs to AWS Glue
5.1. It also describes the features in AWS Glue 5.1 and the advantages of using
it.

To use this feature with your AWS Glue ETL jobs, choose
`5.1` for the `Glue version` when creating your
jobs.

###### Topics

- [New features](#migrating-version-51-features "#migrating-version-51-features")
- [Actions to migrate to
  AWS Glue 5.1](#migrating-version-51-actions "#migrating-version-51-actions")
- [Migration checklist](#migrating-version-51-checklist "#migrating-version-51-checklist")
- [Migrating from AWS Glue 5.0
  to AWS Glue 5.1](#migrating-version-51-from-50 "#migrating-version-51-from-50")
- [Migrating from Older AWS Glue Versions to AWS Glue 5.1](#migrating-older-versions-to-51 "#migrating-older-versions-to-51")
- [Connector and JDBC driver migration for AWS Glue 5.1](#migrating-version-51-connector-driver-migration "#migrating-version-51-connector-driver-migration")

## New features

This section describes new features and advantages of AWS Glue version
5.1.

- Apache Spark update from 3.5.4 in AWS Glue 5.0 to 3.5.6 in AWS Glue 5.1.
- Open Table Formats (OTF) updated to Hudi 1.0.2, Iceberg 1.10.0, and Delta Lake 3.3.2
- **Iceberg Materialized Views** - Create and manage Iceberg Materialized Views (MV). For more information, see
  [blog post](https://aws.amazon.com/blogs/big-data/introducing-apache-iceberg-materialized-views-in-aws-glue-data-catalog/ "https://aws.amazon.com/blogs/big-data/introducing-apache-iceberg-materialized-views-in-aws-glue-data-catalog/")
- **Iceberg format version 3.0** - Extends data types and existing metadata structures to add new capabilities. For more information, see the
  [Iceberg Table Spec](https://iceberg.apache.org/spec/ "https://iceberg.apache.org/spec/").
- **Hudi Full Table Access** - Full Table Access (FTA) control for Apache Hudi in Apache Spark based on your policies defined in .
  This feature enables read and write operations from your AWS Glue ETL jobs on registered tables when the job role has full table access.
- **Spark native fine-grained access control (FGAC) support using** - DDL/DML operations (like CREATE, ALTER, DELETE, DROP) with fine grained access control for
  Apache Hive, Apache Iceberg and Delta Lake tables registered in .
- **Audit context for Spark jobs** - Audit context for AWS Glue ETL jobs with enabled jobs will be available
  for AWS Glue and AWS Lake Formation API calls in log

###### Known Issues and Limitations

Note the following known issues and limitations:

- Limited support for view SQL clause for creation of materialized views, query rewrite and incremental refresh.
  More details can be found in the
  [Iceberg Materialized Views feature documentation page](../../../lake-formation/latest/dg/materialized-views.md#materialized-views-considerations-limitations "../../../lake-formation/latest/dg/materialized-views.md#materialized-views-considerations-limitations")
- **Hudi FTA writes** require using HoodieCredentialedHadoopStorage for credential vending during job execution.
  Set the following configuration when running Hudi jobs:

`hoodie.storage.class=org.apache.spark.sql.hudi.storage.HoodieCredentialedHadoopStorage`

- Hudi FTA write support works only with the default Hudi configurations. Custom or non-default Hudi settings may not be fully supported and could result in unexpected behavior.
  Clustering for Hudi Merge-On-Read (MOR) tables is also not supported under FTA write mode.

###### Breaking changes

Note the following breaking changes:

- S3A filesystem has replaced EMRFS as the default S3 connector.
  For information on how to migrate, see
  [Migrating from AWS Glue 5.0
  to AWS Glue 5.1](#migrating-version-51-from-50 "#migrating-version-51-from-50").

## Actions to migrate to

AWS Glue 5.1

For existing jobs, change the `Glue version` from the previous version to
`Glue 5.1` in the job configuration.

- In AWS Glue Studio, choose `Glue 5.1 - Supports Spark 3.5.6,
Scala 2, Python 3` in `Glue version`.
- In the API, choose `5.1` in the `GlueVersion`
  parameter in the [`UpdateJob`](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob") API operation.

For new jobs, choose `Glue 5.1` when you create a job.

- In the console, choose `Spark 3.5.6, Python 3 (Glue Version 5.1) or Spark
3.5.6, Scala 2 (Glue Version 5.1)` in `Glue version`.
- In AWS Glue Studio, choose `Glue 5.1 - Supports Spark 3.5.6,
Scala 2, Python 3` in `Glue version`.
- In the API, choose `5.1` in the `GlueVersion`
  parameter in the [`CreateJob`](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob") API operation.

To view Spark event logs of AWS Glue 5.1 coming from AWS Glue
2.0 or earlier, [launch an
upgraded Spark history server for AWS Glue 5.1 using CloudFormation or
Docker](monitor-spark-ui-history.md "monitor-spark-ui-history.md").

## Migration checklist

Review this checklist for migration:

- [Python] Update boto references from 1.34 to 1.40.

## Migrating from AWS Glue 5.0

to AWS Glue 5.1

All existing job parameters and major features that exist in
AWS Glue 5.0 will exist in AWS Glue 5.1. Note the following changes when migrating:

- In AWS Glue 5.1, S3A filesystem has replaced EMRFS as the default S3 connector.
  If both `spark.hadoop.fs.s3a.endpoint` and `spark.hadoop.fs.s3a.endpoint.region` are not set,
  the default region used by S3A is `us-east-2`.
  This can cause issues, such as S3 upload timeout errors, especially for VPC jobs.
  To mitigate the issues caused by this change, set the `spark.hadoop.fs.s3a.endpoint.region`
  Spark configuration when using the S3A file system in AWS Glue 5.1.
- To continue using EMRFS instead of S3A, set the following spark configurations:

```
    --conf spark.hadoop.fs.s3.impl=com.amazon.ws.emr.hadoop.fs.EmrFileSystem
    --conf spark.hadoop.fs.s3n.impl=com.amazon.ws.emr.hadoop.fs.EmrFileSystem
    --conf spark.hadoop.fs.AbstractFileSystem.s3.impl=org.apache.hadoop.fs.s3.EMRFSDelegate

```

Refer to the Spark migration documentation:

- [Migration Guide: Spark Core](https://spark.apache.org/docs/3.5.6/core-migration-guide.html "https://spark.apache.org/docs/3.5.6/core-migration-guide.html")
- [Migration Guide: SQL, Datasets and DataFrame](https://spark.apache.org/docs/3.5.6/sql-migration-guide.html "https://spark.apache.org/docs/3.5.6/sql-migration-guide.html")
- [Migration Guide: Structured Streaming](https://spark.apache.org/docs/3.5.6/ss-migration-guide.html "https://spark.apache.org/docs/3.5.6/ss-migration-guide.html")
- [Upgrading PySpark](https://spark.apache.org/docs/3.5.6/api/python/migration_guide/pyspark_upgrade.html "https://spark.apache.org/docs/3.5.6/api/python/migration_guide/pyspark_upgrade.html")

## Migrating from Older AWS Glue Versions to AWS Glue 5.1

- For migration steps related to AWS Glue 4.0 to AWS Glue 5.0, see
  [Migrating from AWS Glue 4.0 to AWS Glue 5.0](migrating-version-50.md#migrating-version-50-from-40 "migrating-version-50.md#migrating-version-50-from-40").
- For migration steps related to AWS Glue 3.0 to AWS Glue 5.0, see
  [Migrating from AWS Glue 3.0 to AWS Glue 5.0](migrating-version-50.md#migrating-version-50-from-30 "migrating-version-50.md#migrating-version-50-from-30").
- For migration steps related to AWS Glue 2.0 to AWS Glue 5.0 and a list of migration differences between AWS Glue version 2.0 and 4.0, see
  [Migrating from AWS Glue 2.0 to AWS Glue 5.0](migrating-version-50.md#migrating-version-50-from-20 "migrating-version-50.md#migrating-version-50-from-20").

## Connector and JDBC driver migration for AWS Glue 5.1

For the versions of JDBC and data lake connectors that were upgraded, see:

- [Appendix B: JDBC driver
  upgrades](#migrating-version-51-appendix-jdbc-driver "#migrating-version-51-appendix-jdbc-driver")
- [Appendix C: Connector
  upgrades](#migrating-version-51-appendix-connector "#migrating-version-51-appendix-connector")
- [Appendix D: Open table format
  upgrades](#migrating-version-51-appendix-open-table-formats "#migrating-version-51-appendix-open-table-formats")

The following changes apply to the OTF version upgrades identified in
[Appendix D: Open table format
upgrades](#migrating-version-51-appendix-open-table-formats "#migrating-version-51-appendix-open-table-formats") for AWS Glue 5.1.

###### Apache Hudi

Note the following changes:

- Support FTA read and write access on Lake Formation registered tables.

###### Apache Iceberg

Note the following changes:

- Support Iceberg format version 3. The following features are supported:
  - Multi-argument transforms for partitioning and sorting.
  - Row Lineage tracking.
  - Deletion vectors. Learn more in
    [blog post](https://aws.amazon.com/blogs/big-data/unlock-the-power-of-apache-iceberg-v3-deletion-vectors-on-amazon-emr/ "https://aws.amazon.com/blogs/big-data/unlock-the-power-of-apache-iceberg-v3-deletion-vectors-on-amazon-emr/")
  - Table encryption keys.

- Support Spark-native FGAC writes on registered tables.
- Athena SQL compatibility - Cannot read Iceberg V3 tables created by EMR Spark due to
  error: `GENERIC_INTERNAL_ERROR: Cannot read unsupported version 3`

###### Delta Lake

Note the following changes:

- Support FTA read and write access on Lake Formation registered tables.

### Appendix A: Notable

dependency upgrades

The following are dependency upgrades:

| Dependency                   | Version in AWS Glue 5.1 | Version in AWS Glue 5.0 | Version in AWS Glue 4.0 | Version in AWS Glue 3.0 | Version in AWS Glue 2.0 | Version in AWS Glue 1.0 |
| ---------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Java                         | 17                      | 17                      | 8                       | 8                       | 8                       | 8                       |
| Spark                        | 3.5.6                   | 3.5.4                   | 3.3.0-amzn-1            | 3.1.1-amzn-0            | 2.4.3                   | 2.4.3                   |
| Hadoop                       | 3.4.1                   | 3.4.1                   | 3.3.3-amzn-0            | 3.2.1-amzn-3            | 2.8.5-amzn-5            | 2.8.5-amzn-1            |
| Scala                        | 2.12.18                 | 2.12.18                 | 2.12                    | 2.12                    | 2.11                    | 2.11                    |
| Jackson                      | 2.15.2                  | 2.15.2                  | 2.12                    | 2.12                    | 2.11                    | 2.11                    |
| Hive                         | 2.3.9-amzn-4            | 2.3.9-amzn-4            | 2.3.9-amzn-2            | 2.3.7-amzn-4            | 1.2                     | 1.2                     |
| EMRFS                        | 2.73.0                  | 2.69.0                  | 2.54.0                  | 2.46.0                  | 2.38.0                  | 2.30.0                  |
| Json4s                       | 3.7.0-M11               | 3.7.0-M11               | 3.7.0-M11               | 3.6.6                   | 3.5.x                   | 3.5.x                   |
| Arrow                        | 12.0.1                  | 12.0.1                  | 7.0.0                   | 2.0.0                   | 0.10.0                  | 0.10.0                  |
| AWS Glue Data Catalog client | 4.9.0                   | 4.5.0                   | 3.7.0                   | 3.0.0                   | 1.10.0                  | N/A                     |
| AWS SDK for Java             | 2.35.5                  | 2.29.52                 | 1.12                    | 1.12                    |                         |                         |
| Python                       | 3.11                    | 3.11                    | 3.10                    | 3.7                     | 2.7 & 3.6               | 2.7 & 3.6               |
| Boto                         | 1.40.61                 | 1.34.131                | 1.26                    | 1.18                    | 1.12                    | N/A                     |
| EMR DynamoDB connector       | 5.7.0                   | 5.6.0                   | 4.16.0                  |                         |                         |                         |

### Appendix B: JDBC driver

upgrades

The following are JDBC driver upgrades:

| Driver               | JDBC driver version in AWS Glue 5.1 | JDBC driver version in AWS Glue 5.0 | JDBC driver version in AWS Glue 4.0 | JDBC driver version in AWS Glue 3.0 | JDBC driver version in past AWS Glue versions |
| -------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | --------------------------------------------- |
| MySQL                | 8.0.33                              | 8.0.33                              | 8.0.23                              | 8.0.23                              | 5.1                                           |
| Microsoft SQL Server | 10.2.0                              | 10.2.0                              | 9.4.0                               | 7.0.0                               | 6.1.0                                         |
| Oracle Databases     | 23.3.0.23.09                        | 23.3.0.23.09                        | 21.7                                | 21.1                                | 11.2                                          |
| PostgreSQL           | 42.7.3                              | 42.7.3                              | 42.3.6                              | 42.2.18                             | 42.1.0                                        |
| Amazon Redshift      | redshift-jdbc42-2.1.0.29            | redshift-jdbc42-2.1.0.29            | redshift-jdbc42-2.1.0.16            | redshift-jdbc41-1.2.12.1017         | redshift-jdbc41-1.2.12.1017                   |
| SAP Hana             | 2.20.17                             | 2.20.17                             | 2.17.12                             |                                     |                                               |
| Teradata             | 20.00.00.33                         | 20.00.00.33                         | 20.00.00.06                         |                                     |                                               |

### Appendix C: Connector

upgrades

The following are connector upgrades:

| Driver                 | Connector version in AWS Glue 5.1 | Connector version in AWS Glue 5.0 | Connector version in AWS Glue 4.0 | Connector version in AWS Glue 3.0 |
| ---------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| EMR DynamoDB connector | 5.7.0                             | 5.6.0                             | 4.16.0                            |                                   |
| Amazon Redshift        | 6.4.2                             | 6.4.0                             | 6.1.3                             |                                   |
| OpenSearch             | 1.2.0                             | 1.2.0                             | 1.0.1                             |                                   |
| MongoDB                | 10.3.0                            | 10.3.0                            | 10.0.4                            | 3.0.0                             |
| Snowflake              | 3.1.1                             | 3.0.0                             | 2.12.0                            |                                   |
| Google BigQuery        | 0.32.2                            | 0.32.2                            | 0.32.2                            |                                   |
| AzureCosmos            | 4.33.0                            | 4.33.0                            | 4.22.0                            |                                   |
| AzureSQL               | 1.3.0                             | 1.3.0                             | 1.3.0                             |                                   |
| Vertica                | 3.3.5                             | 3.3.5                             | 3.3.5                             |                                   |

### Appendix D: Open table format

upgrades

The following are open table format upgrades:

| OTF        | Connector version in AWS Glue 5.1 | Connector version in AWS Glue 5.0 | Connector version in AWS Glue 4.0 | Connector version in AWS Glue 3.0 |
| ---------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| Hudi       | 1.0.2                             | 0.15.0                            | 0.12.1                            | 0.10.1                            |
| Delta Lake | 3.3.2                             | 3.3.0                             | 2.1.0                             | 1.0.0                             |
| Iceberg    | 1.10.0                            | 1.7.1                             | 1.0.0                             | 0.13.1                            |
