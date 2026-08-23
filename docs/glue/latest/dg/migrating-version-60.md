# Migrating AWS Glue for Spark jobs to AWS Glue version 6.0

This topic describes the changes between AWS Glue version 5.1 and 6.0
to allow you to migrate your Spark applications and ETL jobs to AWS Glue
6.0. It also describes the features in AWS Glue 6.0 and the advantages of using
it.

To use this feature with your AWS Glue ETL jobs, choose
`6.0` for the `Glue version` when creating your
jobs.

###### Topics

- [New features](#migrating-version-60-features "#migrating-version-60-features")
- [Actions to migrate to AWS Glue 6.0](#migrating-version-60-actions "#migrating-version-60-actions")
- [Migration checklist](#migrating-version-60-checklist "#migrating-version-60-checklist")
- [Migrating from AWS Glue 5.1 to AWS Glue 6.0](#migrating-version-60-from-51 "#migrating-version-60-from-51")
- [Migrating from older AWS Glue versions to AWS Glue 6.0](#migrating-older-versions-to-60 "#migrating-older-versions-to-60")
- [Connector and JDBC driver migration for AWS Glue 6.0](#migrating-version-60-connector-driver-migration "#migrating-version-60-connector-driver-migration")
- [Known limitations](#migrating-version-60-known-limitations "#migrating-version-60-known-limitations")
- [Appendix A: Notable dependency upgrades](#migrating-version-60-appendix-dependencies "#migrating-version-60-appendix-dependencies")
- [Appendix B: JDBC driver upgrades](#migrating-version-60-appendix-jdbc-driver "#migrating-version-60-appendix-jdbc-driver")
- [Appendix C: Connector upgrades](#migrating-version-60-appendix-connector "#migrating-version-60-appendix-connector")
- [Appendix D: Open table format upgrades](#migrating-version-60-appendix-open-table-formats "#migrating-version-60-appendix-open-table-formats")

## New features

This section describes new features and advantages of AWS Glue version
6.0.

- Apache Spark upgrade from 3.5.6 in AWS Glue 5.1 to 4.1.1 in AWS Glue 6.0.
- Scala upgrade from 2.12.18 to 2.13.17.
- Python upgrade from 3.11 to 3.13.
- Open Table Formats (OTF) updated to Hudi 1.1.1, Iceberg 1.11.0, and Delta Lake 4.2.0.
- **Iceberg format version 3** — Extends data types and existing
  metadata structures to add new capabilities including:

  - VARIANT data type with variant shredding for simplified semi-structured data management and faster reads.
  - Nanosecond-precision timestamps.
  - Geospatial data types (Geometry and Geography).

- **Spark Declarative Pipelines (SDP)** — A new declarative framework
  for defining end-to-end data pipelines using SQL or DataFrame API, with support for
  streaming tables and materialized views. For more information, see
  [Spark Declarative Pipelines](spark-declarative-pipelines.md "spark-declarative-pipelines.md").
- **Spark Connect for Interactive Sessions** — Enables thin-client
  connectivity to AWS Glue Interactive Sessions through Spark Connect protocol, supporting
  remote development workflows.
- **Arrow-native Python UDFs/UDTFs** — Improved performance for Python
  user-defined functions using Apache Arrow columnar format natively.
- **Customer-managed or service-generated Python virtual environment**
  (`--python-virtual-env`) — You can build and provide your own Python venv
  that AWS Glue attaches to Spark drivers and executors at runtime, providing full control
  over dependency management. When existing jobs are migrated to AWS Glue 6.0, AWS Glue
  automatically generates this virtual environment if required.
- **Streaming enhancements** — Real-time mode for stateless streaming
  with millisecond-level latency. For more information, see
  [Enabling real-time mode for streaming jobs](streaming-chapter.md#glue-streaming-real-time-mode "streaming-chapter.md#glue-streaming-real-time-mode").
- **Connector upgrades** — Updated Amazon Redshift, MongoDB, Snowflake, and
  other connectors. See
  [Appendix C: Connector upgrades](#migrating-version-60-appendix-connector "#migrating-version-60-appendix-connector")
  for full version details.

###### Known issues and limitations

Note the following known issues and limitations:

- **ANSI mode is enabled by default** in Spark 4.1. Operations that
  previously returned NULL on overflow (for example, integer arithmetic, cast operations) now
  throw exceptions. Set `spark.sql.ansi.enabled=false` to restore previous
  behavior.
- **Spark Declarative Pipelines (SDP)** is a new feature with limited
  support for certain SQL constructs. Refer to the
  [Spark Declarative Pipelines](spark-declarative-pipelines.md "spark-declarative-pipelines.md")
  documentation for current limitations.
- **Iceberg v3 tables** created in AWS Glue 6.0 cannot be read by Athena SQL
  (error: `Cannot read unsupported version 3`). Use Iceberg v2 for cross-engine
  compatibility with Athena.
- **Python 3.13** removes several deprecated modules and changes behavior
  for some standard library functions. Review the Python 3.13 migration guide for
  compatibility.
- **AWS SDK for Java 2.x compatibility with `--user-jars-first`**
  — AWS Glue 6.0 includes AWS SDK for Java 2.x version 2.44.6. If you use the
  `--user-jars-first` job parameter with a custom JAR that bundles an older
  version of the AWS SDK for Java 2.x, your job might fail with a
  `java.lang.NoSuchFieldError` or similar error. These failures occur when the
  SDK bundled in your custom JAR is missing classes, fields, or methods that the AWS Glue
  runtime depends on. To avoid this issue, ensure that any custom JAR you supply with
  `--user-jars-first` uses AWS SDK for Java 2.x version 2.44.6 or
  later.

###### Breaking changes

Note the following breaking changes:

- **EMRFS has been removed.** S3A is the only S3 filesystem in AWS Glue 6.0.
  The `com.amazon.ws.emr.hadoop.fs.EmrFileSystem` class is no longer available. Jobs
  using `s3://` paths use S3A automatically. If you previously set EMRFS-specific
  configurations (for example, `fs.s3.consistent.*`), remove them.
- **AWS SDK for Java v1 has been removed.** Only AWS SDK v2 (2.44.6) is
  available. Jobs importing `com.amazonaws.services.*` packages must migrate to
  `software.amazon.awssdk.services.*`.
- **Scala upgraded from 2.12 to 2.13.** Custom JARs compiled against Scala
  2.12 don't work. Recompile against Scala 2.13.17. Key changes:
  `JavaConversions` removed (use `CollectionConverters`),
  `MutableList` removed (use `ListBuffer`), parallel collections
  require separate import.
- **Spark 4.1 API changes:**

  - `SQLContext` removed — use `SparkSession` directly.
  - ANSI mode enabled by default — implicit type conversions and overflows behave differently.
  - Several deprecated APIs removed. Refer to the [Spark 4.1 Migration Guide](https://spark.apache.org/docs/4.1.1/migration-guide.html "https://spark.apache.org/docs/4.1.1/migration-guide.html") on the Apache Spark website.

- **CreateSession API validation** — Additional validation on session
  parameters for Interactive Sessions. Invalid configurations that were previously silently
  accepted might now return errors.
- **`getResolvedOptions` behavior change** —
  Argument prefix matching is disabled by default (`allow_abbrev=False`).
  Use the full argument name, or pass `allow_abbrev=True` to
  `getResolvedOptions()` to restore the old behavior.

## Actions to migrate to AWS Glue 6.0

For existing jobs, change the `Glue version` from the previous version to
`Glue 6.0` in the job configuration.

- In AWS Glue Studio, choose `Glue 6.0 - Supports Spark 4.1.1,
 Scala 2, Python 3` in `Glue version`.
- In the API, choose `6.0` in the `GlueVersion`
  parameter in the [UpdateJob](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob") API operation.

For new jobs, choose `Glue 6.0` when you create a job.

- In the console, choose `Spark 4.1.1, Python 3 (Glue Version 6.0) or Spark
 4.1.1, Scala 2 (Glue Version 6.0)` in `Glue version`.
- In AWS Glue Studio, choose `Glue 6.0 - Supports Spark 4.1.1,
 Scala 2, Python 3` in `Glue version`.
- In the API, choose `6.0` in the `GlueVersion`
  parameter in the [CreateJob](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob") API operation.

To help migrate your jobs, you can use [Generative AI upgrades for
Apache Spark](upgrade-analysis.md "upgrade-analysis.md") to upgrade your AWS Glue ETL jobs
from older AWS Glue versions (2.0 and later) to the latest AWS Glue version.

###### Troubleshooting

You can use the [Spark Troubleshooting Agent](../../../emr/latest/ReleaseGuide/spark-troubleshoot.md "../../../emr/latest/ReleaseGuide/spark-troubleshoot.md") to troubleshoot your
AWS Glue ETL jobs.

## Migration checklist

Review this checklist for migration:

- [Scala] Recompile custom JARs against Scala 2.13.17. Replace
  `JavaConversions` with `CollectionConverters`.
- [Python] Update code for Python 3.13 compatibility. Remove usage of deprecated
  modules (for example, `imp`, `cgi`, `cgitb`).
- [Python] Update boto3 references from 1.40 to 1.42.
- [Spark SQL] Review queries for ANSI mode impact. Add
  `spark.sql.ansi.enabled=false` if needed.
- [SDK] Replace any AWS SDK v1 imports (`com.amazonaws.*`) with SDK v2
  (`software.amazon.awssdk.*`).
- [S3] Remove EMRFS-specific configurations. S3A is now the default and only S3
  connector.
- [Dependencies] Update `--extra-jars` to versions compiled for Scala 2.13
  and Spark 4.1.

## Migrating from AWS Glue 5.1 to AWS Glue 6.0

All existing job parameters and major features that exist in
AWS Glue 5.1 will exist in AWS Glue 6.0. Note the following changes when migrating:

- **S3 filesystem:** EMRFS is no longer available. S3A is the sole S3
  connector. If you previously set `spark.hadoop.fs.s3a.endpoint.region`, continue
  using it. If not set, ensure your VPC endpoint or network configuration allows S3A to resolve
  the correct region.
- **Scala binary compatibility:** AWS Glue 6.0 uses Scala 2.13. Any
  `--extra-jars` compiled with Scala 2.12 fail with
  `NoSuchMethodError` or `ClassNotFoundException`. Recompile all custom
  Scala/Java JARs.
- **Spark SQL behavior changes:**

  - ANSI mode is ON by default. Integer overflow, invalid casts, and array index
    out-of-bounds throw exceptions instead of returning NULL.
  - `spark.sql.legacy.timeParserPolicy` default changed. Date/time
    parsing might behave differently.
  - Implicit string-to-numeric conversions in SQL might fail under ANSI
    mode.

- **Python version:** Python 3.13 is the runtime. The
  `--additional-python-modules` feature continues to work but is deprecated.
  Consider migrating to `--python-virtual-env` for full dependency control.
- **AWS SDK:** Only SDK v2 is available. If your scripts use boto3
  (Python), no change is needed — boto3 continues to work. For Scala/Java jobs using the
  AWS SDK directly, migrate to v2 APIs.

Refer to the Spark migration documentation:

- [Migration Guide: Spark Core](https://spark.apache.org/docs/4.1.1/core-migration-guide.html "https://spark.apache.org/docs/4.1.1/core-migration-guide.html") on the Apache Spark website
- [Migration Guide: SQL, Datasets and DataFrame](https://spark.apache.org/docs/4.1.1/sql-migration-guide.html "https://spark.apache.org/docs/4.1.1/sql-migration-guide.html") on the Apache Spark website
- [Migration Guide: Structured Streaming](https://spark.apache.org/docs/4.1.1/ss-migration-guide.html "https://spark.apache.org/docs/4.1.1/ss-migration-guide.html") on the Apache Spark website
- [Upgrading PySpark](https://spark.apache.org/docs/4.1.1/api/python/migration_guide/pyspark_upgrade.html "https://spark.apache.org/docs/4.1.1/api/python/migration_guide/pyspark_upgrade.html") on the Apache Spark website

## Migrating from older AWS Glue versions to AWS Glue 6.0

- For migration steps related to AWS Glue 5.0 to AWS Glue 5.1, see
  [Migrating from AWS Glue 5.0 to AWS Glue 5.1](migrating-version-51.md#migrating-version-51-from-50 "migrating-version-51.md#migrating-version-51-from-50").
- For migration steps related to AWS Glue 4.0 to AWS Glue 5.0, see
  [Migrating from AWS Glue 4.0 to AWS Glue 5.0](migrating-version-50.md#migrating-version-50-from-40 "migrating-version-50.md#migrating-version-50-from-40").
- For migration steps related to AWS Glue 3.0 to AWS Glue 5.0, see
  [Migrating from AWS Glue 3.0 to AWS Glue 5.0](migrating-version-50.md#migrating-version-50-from-30 "migrating-version-50.md#migrating-version-50-from-30").
- For migration steps related to AWS Glue 2.0 to AWS Glue 5.0, see
  [Migrating from AWS Glue 2.0 to AWS Glue 5.0](migrating-version-50.md#migrating-version-50-from-20 "migrating-version-50.md#migrating-version-50-from-20").
- After completing the steps above, finish migrating to AWS Glue 6.0 by following
  [Migrating from AWS Glue 5.1 to AWS Glue 6.0](#migrating-version-60-from-51 "#migrating-version-60-from-51").

## Connector and JDBC driver migration for AWS Glue 6.0

For the versions of JDBC and data lake connectors that were upgraded, see:

- [Appendix B: JDBC driver upgrades](#migrating-version-60-appendix-jdbc-driver "#migrating-version-60-appendix-jdbc-driver")
- [Appendix C: Connector upgrades](#migrating-version-60-appendix-connector "#migrating-version-60-appendix-connector")
- [Appendix D: Open table format upgrades](#migrating-version-60-appendix-open-table-formats "#migrating-version-60-appendix-open-table-formats")

The following changes apply to the OTF version upgrades identified in
[Appendix D: Open table format upgrades](#migrating-version-60-appendix-open-table-formats "#migrating-version-60-appendix-open-table-formats") for AWS Glue 6.0.

###### Apache Iceberg

Note the following changes:

- Iceberg upgraded to 1.11.0 with full support for Apache Iceberg version 3 specifications.
- VARIANT data type with variant shredding for optimized semi-structured data queries.
- Nanosecond-precision timestamps.
- Geospatial data types (Geometry and Geography).

The following Iceberg features are already supported by AWS Glue ETL since AWS Glue 5.1:
deletion vectors (merge-on-read using Roaring Bitmaps stored in Puffin files) and
row lineage tracking through `first-row-id` metadata.

###### Apache Hudi

Note the following changes:

- Hudi upgraded to 1.1.1.
- Continued support for FTA read and write access on AWS Lake Formation registered tables.

###### Delta Lake

Note the following changes:

- Delta Lake upgraded to 4.2.0.
- Continued support for FTA read and write access on AWS Lake Formation registered tables.

## Known limitations

The following limitations apply to AWS Glue 6.0:

- Iceberg native table encryption keys are not supported.
- Iceberg multi-argument transforms are not supported.
- The new Iceberg v3 data types are only supported with Spark DataFrames. These features will not work with DynamicFrames.
- Visual ETL in AWS Glue Studio does not support the new Iceberg v3 data types. If you want to use these new features with Visual ETL, we recommend migrating your ETL jobs to Amazon SageMaker Unified Studio.
- Fine-grained access control (FGAC) is not supported with VARIANT columns.
- Iceberg tables created with `'format-version'='3'` cannot be read by Athena SQL
  (error: `Cannot read unsupported version 3`). Use Iceberg v2 for cross-engine
  compatibility with Athena.

## Appendix A: Notable dependency upgrades

The following are dependency upgrades:

| Dependency                   | Version in AWS Glue 6.0 | Version in AWS Glue 5.1 | Version in AWS Glue 5.0 | Version in AWS Glue 4.0 |
| ---------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Java                         | 17                      | 17                      | 17                      | 8                       |
| Spark                        | 4.1.1                   | 3.5.6                   | 3.5.4                   | 3.3.0-amzn-1            |
| Hadoop                       | 3.4.2                   | 3.4.1                   | 3.4.1                   | 3.3.3-amzn-0            |
| Scala                        | 2.13.17                 | 2.12.18                 | 2.12.18                 | 2.12                    |
| Jackson                      | 2.20.0                  | 2.15.2                  | 2.15.2                  | 2.12                    |
| Hive                         | 2.3.10-amzn-1           | 2.3.9-amzn-4            | 2.3.9-amzn-4            | 2.3.9-amzn-2            |
| Arrow                        | 18.3.0                  | 12.0.1                  | 12.0.1                  | 7.0.0                   |
| AWS Glue Data Catalog client | 4.11.0                  | 4.9.0                   | 4.5.0                   | 3.7.0                   |
| AWS SDK for Java             | 2.44.6 (v2 only)        | 2.35.5                  | 2.29.52                 | 1.12                    |
| Python                       | 3.13                    | 3.11                    | 3.11                    | 3.10                    |
| Boto3                        | 1.42.84                 | 1.40.61                 | 1.34.131                | 1.26                    |
| Json4s                       | 3.7.0-M11               | 3.7.0-M11               | 3.7.0-M11               | 3.7.0-M11               |
| EMR DynamoDB connector       | 6.1.0                   | 5.7.0                   | 5.6.0                   | 4.16.0                  |
| Netty                        | 4.2.7                   | N/A                     | N/A                     | N/A                     |
| Parquet                      | 1.16.0                  | N/A                     | N/A                     | N/A                     |
| NumPy                        | 2.4.4                   | N/A                     | N/A                     | N/A                     |
| Pandas                       | 2.3.3                   | N/A                     | N/A                     | N/A                     |

## Appendix B: JDBC driver upgrades

The following are JDBC driver upgrades:

| Driver               | JDBC driver version in AWS Glue 6.0 | JDBC driver version in AWS Glue 5.1 | JDBC driver version in AWS Glue 5.0 |
| -------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| MySQL                | 8.0.33                              | 8.0.33                              | 8.0.33                              |
| Microsoft SQL Server | 10.2.0                              | 10.2.0                              | 10.2.0                              |
| Oracle Databases     | 23.4.0.24.05                        | 23.3.0.23.09                        | 23.3.0.23.09                        |
| PostgreSQL           | 42.7.3                              | 42.7.3                              | 42.7.3                              |
| Amazon Redshift      | redshift-jdbc42-2.2.7               | redshift-jdbc42-2.1.0.29            | redshift-jdbc42-2.1.0.29            |
| MariaDB              | 3.5.7                               | N/A                                 | N/A                                 |

## Appendix C: Connector upgrades

The following are connector upgrades:

| Connector              | Version in AWS Glue 6.0 | Version in AWS Glue 5.1 | Version in AWS Glue 5.0 |
| ---------------------- | ----------------------- | ----------------------- | ----------------------- |
| Spark Redshift         | 6.7.0                   | 6.4.2                   | 6.4.0                   |
| Spark SQL Kinesis      | 2.1.0                   | N/A                     | N/A                     |
| MongoDB                | 11.0.1                  | 10.3.0                  | 10.3.0                  |
| Snowflake              | 3.17.0                  | 3.1.1                   | 3.0.0                   |
| OpenSearch             | 2.0.0                   | 1.2.0                   | 1.2.0                   |
| EMR DynamoDB connector | 6.1.0                   | 5.7.0                   | 5.6.0                   |

## Appendix D: Open table format upgrades

The following are open table format upgrades:

| OTF        | Version in AWS Glue 6.0 | Version in AWS Glue 5.1 | Version in AWS Glue 5.0 | Version in AWS Glue 4.0 |
| ---------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Hudi       | 1.1.1                   | 1.0.2                   | 0.15.0                  | 0.12.1                  |
| Delta Lake | 4.2.0                   | 3.3.2                   | 3.3.0                   | 2.1.0                   |
| Iceberg    | 1.11.0                  | 1.10.0                  | 1.7.1                   | 1.0.0                   |
