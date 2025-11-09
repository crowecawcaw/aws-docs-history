# Migrating AWS Glue for Spark jobs to

AWS Glue version 4.0

This topic describes the changes between AWS Glue versions 0.9, 1.0, 2.0, and
3.0 to allow you to migrate your Spark applications and ETL jobs to AWS Glue
4.0. It also describes the features in AWS Glue 4.0 and the advantages of using
it.

To use this feature with your AWS Glue ETL jobs, choose
`4.0` for the `Glue version` when creating your
jobs.

###### Topics

- [New features supported](#migrating-version-40-features "#migrating-version-40-features")
- [Actions to migrate to
  AWS Glue 4.0](#migrating-version-40-actions "#migrating-version-40-actions")
- [Migration checklist](#migrating-version-40-checklist "#migrating-version-40-checklist")
- [Migrating from AWS Glue 3.0
  to AWS Glue 4.0](#migrating-version-40-from-30 "#migrating-version-40-from-30")
- [Migrating from AWS Glue 2.0
  to AWS Glue 4.0](#migrating-version-40-from-20 "#migrating-version-40-from-20")
- [Migrating from AWS Glue 1.0
  to AWS Glue 4.0](#migrating-version-40-from-10 "#migrating-version-40-from-10")
- [Migrating from AWS Glue 0.9
  to AWS Glue 4.0](#migrating-version-40-from-09 "#migrating-version-40-from-09")
- [Connector and JDBC
  driver migration for AWS Glue 4.0](#migrating-version-40-connector-driver-migration "#migrating-version-40-connector-driver-migration")
- [Appendix A: Notable
  dependency upgrades](#migrating-version-40-appendix-dependencies "#migrating-version-40-appendix-dependencies")
- [Appendix B: JDBC driver
  upgrades](#migrating-version-40-appendix-jdbc-driver "#migrating-version-40-appendix-jdbc-driver")
- [Appendix C: Connector
  upgrades](#migrating-version-40-appendix-connector "#migrating-version-40-appendix-connector")

## New features supported

This section describes new features and advantages of AWS Glue version
4.0.

- It is based on Apache Spark 3.3.0, but includes optimizations in
  AWS Glue, and Amazon EMR, such as adaptive query runs, vectorized
  readers, and optimized shuffles and partition coalescing.
- Upgraded JDBC drivers for all AWS Glue native sources including
  MySQL, Microsoft SQL Server, Oracle, PostgreSQL, MongoDB, and upgraded Spark
  libraries and dependencies brought in by Spark 3.3.0.
- Updated with a new Amazon Redshift connector and JDBC driver.
- Optimized Amazon S3 access with upgraded EMR File System (EMRFS) and enabled
  Amazon S3-optimized output committers, by default.
- Optimized Data Catalog access with partition indexes, pushdown predicates,
  partition listing, and an upgraded Hive metastore client.
- Integration with Lake Formation for governed catalog tables with cell-level filtering
  and data lake transactions.
- Reduced startup latency to improve overall job completion times and
  interactivity.
- Spark jobs are billed in 1-second increments with a 10x lower minimum billing
  duration—from a 10-minute minimum to a 1-minute minimum.
- Native support for open-data lake frameworks with Apache Hudi, Delta Lake, and
  Apache Iceberg.
- Native support for the Amazon S3-based Cloud Shuffle Storage Plugin (an Apache
  Spark plugin) to use Amazon S3 for shuffling and elastic storage capacity.

###### Major enhancements from Spark 3.1.1 to Spark 3.3.0

Note the following enhancements:

- Row-level runtime filtering ([SPARK-32268](https://issues.apache.org/jira/browse/SPARK-32268 "https://issues.apache.org/jira/browse/SPARK-32268")).
- ANSI enhancements ([SPARK-38860](https://issues.apache.org/jira/browse/SPARK-38860 "https://issues.apache.org/jira/browse/SPARK-38860")).
- Error message improvements ([SPARK-38781](https://issues.apache.org/jira/browse/SPARK-38781 "https://issues.apache.org/jira/browse/SPARK-38781")).
- Support complex types for Parquet vectorized reader ([SPARK-34863](https://issues.apache.org/jira/browse/SPARK-34863 "https://issues.apache.org/jira/browse/SPARK-34863")).
- Hidden file metadata support for Spark SQL ([SPARK-37273](https://issues.apache.org/jira/browse/SPARK-37273 "https://issues.apache.org/jira/browse/SPARK-37273")).
- Provide a profiler for Python/Pandas UDFs ([SPARK-37443](https://issues.apache.org/jira/browse/SPARK-37443 "https://issues.apache.org/jira/browse/SPARK-37443")).
- Introduce Trigger.AvailableNow for running streaming queries like Trigger.Once
  in multiple batches ([SPARK-36533](https://issues.apache.org/jira/browse/SPARK-36533 "https://issues.apache.org/jira/browse/SPARK-36533")).
- More comprehensive Datasource V2 pushdown capabilities ([SPARK-38788](https://issues.apache.org/jira/browse/SPARK-38788 "https://issues.apache.org/jira/browse/SPARK-38788")).
- Migrating from log4j 1 to log4j 2 ([SPARK-37814](https://issues.apache.org/jira/browse/SPARK-37814 "https://issues.apache.org/jira/browse/SPARK-37814")).

###### Other notable changes

Note the following changes:

- Breaking changes
  - Drop references to Python 3.6 support in docs and Python/docs ([SPARK-36977](https://issues.apache.org/jira/browse/SPARK-36977 "https://issues.apache.org/jira/browse/SPARK-36977")).
  - Remove named tuple hack by replacing built-in pickle to cloudpickle
    ([SPARK-32079](https://issues.apache.org/jira/browse/SPARK-32079 "https://issues.apache.org/jira/browse/SPARK-32079")).
  - Bump minimum pandas version to 1.0.5 ([SPARK-37465](https://issues.apache.org/jira/browse/SPARK-37465 "https://issues.apache.org/jira/browse/SPARK-37465")).

## Actions to migrate to

AWS Glue 4.0

For existing jobs, change the `Glue version` from the previous version to
`Glue 4.0` in the job configuration.

- In AWS Glue Studio, choose `Glue 4.0 - Supports Spark 3.3,
Scala 2, Python 3` in `Glue version`.
- In the API, choose `4.0` in the `GlueVersion`
  parameter in the [`UpdateJob`](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob") API operation.

For new jobs, choose `Glue 4.0` when you create a job.

- In the console, choose `Spark 3.3, Python 3 (Glue Version 4.0) or Spark
3.3, Scala 2 (Glue Version 3.0)` in `Glue version`.
- In AWS Glue Studio, choose `Glue 4.0 - Supports Spark 3.3,
Scala 2, Python 3` in `Glue version`.
- In the API, choose `4.0` in the `GlueVersion`
  parameter in the [`CreateJob`](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob") API operation.

To view Spark event logs of AWS Glue 4.0 coming from AWS Glue
2.0 or earlier, [launch an
upgraded Spark history server for AWS Glue 4.0 using AWS CloudFormation or
Docker](monitor-spark-ui-history.md "monitor-spark-ui-history.md").

## Migration checklist

- Do your job's external Python libraries depend on Python 2.7/3.6?
  - Update the dependent libraries from Python 2.7/3.6 to Python 3.10 as
    Spark 3.3.0 completely removed Python 2.7 and 3.6 support.

## Migrating from AWS Glue 3.0

to AWS Glue 4.0

Note the following changes when migrating:

- All existing job parameters and major features that exist in
  AWS Glue 3.0 will exist in AWS Glue 4.0.
- AWS Glue 3.0 uses Amazon EMR-optimized Spark 3.1.1, and
  AWS Glue 4.0 uses Amazon EMR-optimized Spark 3.3.0.

Several Spark changes alone might require revision of your scripts to ensure
that removed features are not being referenced.

- AWS Glue 4.0 also features an update to EMRFS and Hadoop. For the
  specific version, see [Appendix A: Notable
  dependency upgrades](#migrating-version-40-appendix-dependencies "#migrating-version-40-appendix-dependencies").
- The AWS SDK provided in ETL jobs is now upgraded from 1.11 to 1.12.
- All Python jobs will be using Python version 3.10. Previously, Python 3.7 was
  used in AWS Glue 3.0.

As a result, some pymodules brought out-of-the-box by AWS Glue are
upgraded.

- Log4j has been upgraded to Log4j2.
  - For information on the Log4j2 migration path, see the [Log4j documentation](https://logging.apache.org/log4j/2.x/manual/migration.html#Log4j2API "https://logging.apache.org/log4j/2.x/manual/migration.html#Log4j2API").
  - You must rename any custom log4j.properties file as a
    log4j2.properties file instead, with the appropriate log4j2
    properties.

- For migrating certain connectors, see [Connector and JDBC
  driver migration for AWS Glue 4.0](#migrating-version-40-connector-driver-migration "#migrating-version-40-connector-driver-migration").
- The AWS Encryption SDK is upgraded from 1.x to 2.x. AWS Glue
  jobs using AWS Glue security configurations and jobs dependent on
  the AWS Encryption SDK dependency provided in runtime are affected. See the
  instructions for AWS Glue job migration.

You can safely upgrade an AWS Glue 2.0/3.0 job to an
AWS Glue 4.0 job because AWS Glue 2.0/3.0 already
contains the AWS Encryption SDK bridge version.

Refer to the Spark migration documentation:

- [Upgrading from Spark SQL 3.1 to 3.2](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32")
- [Upgrading from Spark SQL 3.2 to 3.3](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33")

## Migrating from AWS Glue 2.0

to AWS Glue 4.0

Note the following changes when migrating:

###### Note

For migration steps related to AWS Glue 3.0, see [Migrating from AWS Glue 3.0
to AWS Glue 4.0](#migrating-version-40-from-30 "#migrating-version-40-from-30").

- All existing job parameters and major features that exist in
  AWS Glue 2.0 will exist in AWS Glue 4.0.
- The EMRFS S3-optimized committer for writing Parquet data into Amazon S3 is enabled
  by default since AWS Glue 3.0. However, you can still disable it by setting
  `--enable-s3-parquet-optimized-committer` to
  `false`.
- AWS Glue 2.0 uses open-source Spark 2.4 and AWS Glue
  4.0 uses Amazon EMR-optimized Spark 3.3.0.
  - Several Spark changes alone may require revision of your scripts to
    ensure that removed features are not being referenced.
  - For example, Spark 3.3.0 does not enable Scala-untyped UDFs, but Spark
    2.4 does allow them.

- The AWS SDK provided in ETL jobs is now upgraded from 1.11 to 1.12.
- AWS Glue 4.0 also features an update to EMRFS, updated JDBC
  drivers, and inclusions of additional optimizations onto Spark itself provided
  by AWS Glue.
- Scala is updated to 2.12 from 2.11, and Scala 2.12 is not backward compatible
  with Scala 2.11.
- Python 3.10 is the default version used for Python scripts, as
  AWS Glue 2.0 was only using Python 3.7 and 2.7.
  - Python 2.7 is not supported with Spark 3.3.0. Any job requesting
    Python 2 in the job configuration will fail with an
    IllegalArgumentException.
  - A new mechanism of installing additional Python modules is available
    since AWS Glue 2.0.

- Several dependency updates, highlighted in [Appendix A: Notable
  dependency upgrades](#migrating-version-40-appendix-dependencies "#migrating-version-40-appendix-dependencies").
- Any extra JAR files supplied in existing AWS Glue 2.0 jobs might
  bring in conflicting dependencies because there were upgrades in several
  dependencies in 4.0 from 2.0. You can avoid classpath conflicts in AWS Glue 4.0 with the `--user-jars-first` AWS Glue job parameter.
- AWS Glue 4.0 uses Spark 3.3. Starting with Spark 3.1, there was a change in the behavior of loading/saving of timestamps from/to parquet files. For more details, see [Upgrading from Spark SQL 3.0 to 3.1](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-30-to-31 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-30-to-31").

We recommend to set the following parameters when reading/writing parquet data that contains timestamp columns. Setting those parameters can resolve the calendar incompatibility issue that occurs during the Spark 2 to Spark 3 upgrade, for both the AWS Glue Dynamic Frame and Spark Data Frame. Use the CORRECTED option to read the datetime value as it is; and the LEGACY option to rebase the datetime values with regard to the calendar difference during reading.

```
- Key: --conf
- Value: spark.sql.legacy.parquet.int96RebaseModeInRead=[CORRECTED|LEGACY] --conf spark.sql.legacy.parquet.int96RebaseModeInWrite=[CORRECTED|LEGACY] --conf spark.sql.legacy.parquet.datetimeRebaseModeInRead=[CORRECTED|LEGACY]
```

- For migrating certain connectors, see [Connector and JDBC
  driver migration for AWS Glue 4.0](#migrating-version-40-connector-driver-migration "#migrating-version-40-connector-driver-migration").
- The AWS Encryption SDK is upgraded from 1.x to 2.x. AWS Glue
  jobs using AWS Glue security configurations and jobs dependent on
  the AWS Encryption SDK dependency provided in runtime are affected. See these
  instructions for AWS Glue job migration:
  - You can safely upgrade an AWS Glue 2.0 job to an
    AWS Glue 4.0 job because AWS Glue 2.0
    already contains the AWS Encryption SDK bridge version.

Refer to the Spark migration documentation:

- [Upgrading from Spark SQL 2.4 to 3.0](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-24-to-30 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-24-to-30")
- [Upgrading from Spark SQL 3.1 to 3.2](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32")
- [Upgrading from Spark SQL 3.2 to 3.3](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33")
- [Changes in
  Datetime behavior to be expected since Spark 3.0.](https://issues.apache.org/jira/browse/SPARK-31408 "https://issues.apache.org/jira/browse/SPARK-31408")

## Migrating from AWS Glue 1.0

to AWS Glue 4.0

Note the following changes when migrating:

- AWS Glue 1.0 uses open-source Spark 2.4 and AWS Glue
  4.0 uses Amazon EMR-optimized Spark 3.3.0.
  - Several Spark changes alone may require revision of your scripts to
    ensure that removed features are not being referenced.
  - For example, Spark 3.3.0 does not enable Scala-untyped UDFs, but Spark
    2.4 does allow them.

- All jobs in AWS Glue 4.0 will be run with significantly improved
  startup times. Spark jobs will be billed in 1-second increments with a 10x lower
  minimum billing duration since startup latency will go from 10 minutes maximum
  to 1 minute maximum.
- Logging behavior has changed significantly in AWS Glue 4.0, Spark
  3.3.0 has a minimum requirement of Log4j2.
- Several dependency updates, highlighted in the appendix.
- Scala is also updated to 2.12 from 2.11, and Scala 2.12 is not backward
  compatible with Scala 2.11.
- Python 3.10 is also the default version used for Python scripts, as
  AWS Glue 0.9 was only using Python 2.

Python 2.7 is not supported with Spark 3.3.0. Any job requesting Python 2 in
the job configuration will fail with an IllegalArgumentException.

- A new mechanism of installing additional Python modules through pip is
  available since AWS Glue 2.0. For more information, see [Installing additional Python modules with pip in AWS Glue
  2.0+](aws-glue-programming-python-libraries.md#addl-python-modules-support "aws-glue-programming-python-libraries.md#addl-python-modules-support").
- AWS Glue 4.0 does not run on Apache YARN, so YARN settings do not
  apply.
- AWS Glue 4.0 does not have a Hadoop Distributed File System
  (HDFS).
- Any extra JAR files supplied in existing AWS Glue 1.0 jobs might
  bring in conflicting dependencies because there were upgrades in several
  dependencies in 4.0 from 1.0. We enable AWS Glue 4.0 with the
  `--user-jars-first`
  AWS Glue job parameter by default, to avoid this problem.
- AWS Glue 4.0 supports auto scaling. Therefore, the
  ExecutorAllocationManager metric will be available when auto scaling is
  enabled.
- In AWS Glue version 4.0 jobs, you specify the number of workers
  and worker type, but do not specify a `maxCapacity`.
- AWS Glue 4.0 does not yet support machine learning
  transforms.
- For migrating certain connectors, see [Connector and JDBC
  driver migration for AWS Glue 4.0](#migrating-version-40-connector-driver-migration "#migrating-version-40-connector-driver-migration").
- The AWS Encryption SDK is upgraded from 1.x to 2.x. AWS Glue
  jobs using AWS Glue security configurations and jobs dependent on
  the AWS Encryption SDK dependency provided in runtime are affected. See these
  instructions for AWS Glue job migration.
  - You cannot migrate an AWS Glue 0.9/1.0 job to an
    AWS Glue 4.0 job directly. This is because when
    upgrading directly to version 2.x or later and enabling all new features
    immediately, the AWS Encryption SDK won't be able to decrypt the
    ciphertext encrypted under earlier versions of the AWS Encryption SDK.
  - To safely upgrade, we first recommend that you migrate to an
    AWS Glue 2.0/3.0 job that contains the AWS Encryption
    SDK bridge version. Run the job once to utilize the AWS Encryption SDK
    bridge version.
  - Upon completion, you can safely migrate the AWS Glue
    2.0/3.0 job to AWS Glue 4.0.

Refer to the Spark migration documentation:

- [Upgrading from Spark SQL 2.4 to 3.0](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-24-to-30 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-24-to-30")
- [Upgrading from Spark SQL 3.0 to 3.1](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-30-to-31 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-30-to-31")
- [Upgrading from Spark SQL 3.1 to 3.2](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32")
- [Upgrading from Spark SQL 3.2 to 3.3](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33")
- [Changes in
  Datetime behavior to be expected since Spark 3.0.](https://issues.apache.org/jira/browse/SPARK-31408 "https://issues.apache.org/jira/browse/SPARK-31408")

## Migrating from AWS Glue 0.9

to AWS Glue 4.0

Note the following changes when migrating:

- AWS Glue 0.9 uses open-source Spark 2.2.1 and AWS Glue
  4.0 uses Amazon EMR-optimized Spark 3.3.0.
  - Several Spark changes alone might require revision of your scripts to
    ensure that removed features are not being referenced.
  - For example, Spark 3.3.0 does not enable Scala-untyped UDFs, but Spark
    2.2 does allow them.

- All jobs in AWS Glue 4.0 will be run with significantly improved
  startup times. Spark jobs will be billed in 1-second increments with a 10x lower
  minimum billing duration because startup latency will go from 10 minutes maximum
  to 1 minute maximum.
- Logging behavior has changed significantly since AWS Glue 4.0,
  Spark 3.3.0 has a minimum requirement of Log4j2 as mentioned here
  (https://spark.apache.org/docs/latest/core-migration-guide.html#upgrading-from-core-32-to-33).
- Several dependency updates, highlighted in the appendix.
- Scala is also updated to 2.12 from 2.11, and Scala 2.12 is not backward
  compatible with Scala 2.11.
- Python 3.10 is also the default version used for Python scripts, as
  AWS Glue 0.9 was only using Python 2.
  - Python 2.7 is not supported with Spark 3.3.0. Any job requesting
    Python 2 in the job configuration will fail with an
    IllegalArgumentException.
  - A new mechanism of installing additional Python modules through pip is
    available.

- AWS Glue 4.0 does not run on Apache YARN, so YARN settings do not
  apply.
- AWS Glue 4.0 does not have a Hadoop Distributed File System
  (HDFS).
- Any extra JAR files supplied in existing AWS Glue 0.9 jobs might
  bring in conflicting dependencies because there were upgrades in several
  dependencies in 3.0 from 0.9. You can avoid classpath conflicts in
  AWS Glue 3.0 with the `--user-jars-first`
  AWS Glue job parameter.
- AWS Glue 4.0 supports auto scaling. Therefore, the
  ExecutorAllocationManager metric will be available when auto scaling is
  enabled.
- In AWS Glue version 4.0 jobs, you specify the number of workers
  and worker type, but do not specify a `maxCapacity`.
- AWS Glue 4.0 does not yet support machine learning
  transforms.
- For migrating certain connectors, see [Connector and JDBC
  driver migration for AWS Glue 4.0](#migrating-version-40-connector-driver-migration "#migrating-version-40-connector-driver-migration").
- The AWS Encryption SDK is upgraded from 1.x to 2.x. AWS Glue
  jobs using AWS Glue security configurations and jobs dependent on
  the AWS Encryption SDK dependency provided in runtime are affected. See these
  instructions for AWS Glue job migration.
  - You cannot migrate an AWS Glue 0.9/1.0 job to an
    AWS Glue 4.0 job directly. This is because when
    upgrading directly to version 2.x or later and enabling all new features
    immediately, the AWS Encryption SDK won't be able to decrypt the
    ciphertext encrypted under earlier versions of the AWS Encryption SDK.
  - To safely upgrade, we first recommend that you migrate to an
    AWS Glue 2.0/3.0 job that contains the AWS Encryption
    SDK bridge version. Run the job once to utilize the AWS Encryption SDK
    bridge version.
  - Upon completion, you can safely migrate the AWS Glue
    2.0/3.0 job to AWS Glue 4.0.

Refer to the Spark migration documentation:

- [Upgrading from Spark SQL 2.2 to 2.3](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-22-to-23 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-22-to-23")
- [Upgrading from Spark SQL 2.3 to 2.4](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-23-to-24 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-23-to-24")
- [Upgrading from Spark SQL 2.4 to 3.0](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-24-to-30 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-24-to-30")
- [Upgrading from Spark SQL 3.0 to 3.1](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-30-to-31 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-30-to-31")
- [Upgrading from Spark SQL 3.1 to 3.2](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-31-to-32")
- [Upgrading from Spark SQL 3.2 to 3.3](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33 "https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-32-to-33")
- [Changes in
  Datetime behavior to be expected since Spark 3.0](https://issues.apache.org/jira/browse/SPARK-31408 "https://issues.apache.org/jira/browse/SPARK-31408").

## Connector and JDBC

driver migration for AWS Glue 4.0

For the versions of JDBC and data lake connectors that were upgraded, see:

- [Appendix B: JDBC driver
  upgrades](#migrating-version-40-appendix-jdbc-driver "#migrating-version-40-appendix-jdbc-driver")
- [Appendix C: Connector
  upgrades](#migrating-version-40-appendix-connector "#migrating-version-40-appendix-connector")

### Hudi

- Spark SQL support improvements:
  - Through the `Call Procedure` command, there is added
    support for upgrade, downgrade, bootstrap, clean, and repair.
    `Create/Drop/Show/Refresh Index` syntax is possible
    in Spark SQL.
  - A performance gap has been closed between usage through a Spark
    DataSource as opposed to Spark SQL. Datasource writes in the past
    used to be faster than SQL.
  - All built-in key generators implement more performant
    Spark-specific API operations.
  - Replaced UDF transformation in the bulk `insert`
    operation with RDD transformations to cut down on costs of using
    SerDe.
  - Spark SQL with Hudi requires a `primaryKey` to be
    specified by `tblproperites` or options in the SQL
    statement. For update and delete operations, the
    `preCombineField` is required as well.

- Any Hudi table created before version 0.10.0 without a
  `primaryKey` needs to be recreated with a
  `primaryKey` field since version 0.10.0.

### PostgreSQL

- Several vulnerabilities (CVEs) were addressed.
- Java 8 is natively supported.
- If the job is using Arrays of Arrays, with the exception of byte arrays,
  this scenario can be treated as multidimensional arrays.

### MongoDB

- The current MongoDB connector supports Spark version 3.1 or later and
  MongoDB version 4.0 or later.
- Due to the connector upgrade, a few property names changed. For example,
  the URI property name changed to `connection.uri`. For more
  information on the current options, see the [MongoDB Spark Connector blog](https://www.mongodb.com/docs/spark-connector/current/configuration/ "https://www.mongodb.com/docs/spark-connector/current/configuration/").
- Using MongoDB 4.0 hosted by Amazon DocumentDB has some functional differences. For
  more information, see these topics:
  - [Functional Differences: Amazon DocumentDB and MongoDB](../../../documentdb/latest/developerguide/functional-differences.md "../../../documentdb/latest/developerguide/functional-differences.md")
  - [Supported MongoDB APIs, Operations, and Data Types](../../../documentdb/latest/developerguide/mongo-apis.md "../../../documentdb/latest/developerguide/mongo-apis.md").

- The "partitioner" option is restricted to `ShardedPartitioner`,
  `PaginateIntoPartitionsPartitioner`, and
  `SinglePartitionPartitioner`. It cannot use default
  `SamplePartitioner` and
  `PaginateBySizePartitioner` for Amazon DocumentDB because the stage
  operator does not support the MongoDB API. For more information, see [Supported MongoDB APIs, Operations, and Data Types](../../../documentdb/latest/developerguide/mongo-apis.md "../../../documentdb/latest/developerguide/mongo-apis.md").

### Delta

Lake

- Delta Lake now supports [time travel in SQL](https://docs.delta.io/2.1.0/delta-batch.html#query-an-older-snapshot-of-a-table-time-travel "https://docs.delta.io/2.1.0/delta-batch.html#query-an-older-snapshot-of-a-table-time-travel") to query older data easily. With this
  update, time travel is now available both in Spark SQL and through the
  DataFrame API. Support has been added for the current version of TIMESTAMP
  in SQL.
- Spark 3.3 introduces [Trigger.AvailableNow](https://issues.apache.org/jira/browse/SPARK-36533 "https://issues.apache.org/jira/browse/SPARK-36533") for running streaming queries as an
  equivalent to `Trigger.Once` for batch queries. This support is
  also available when using Delta tables as a streaming source.
- Support for SHOW COLUMNS to return the list of columns in a table.
- Support for [DESCRIBE DETAIL](https://docs.delta.io/2.1.0/delta-utility.html#retrieve-delta-table-details "https://docs.delta.io/2.1.0/delta-utility.html#retrieve-delta-table-details") in the Scala and Python DeltaTable API. It
  retrieves detailed information about a Delta table using either the
  DeltaTable API or Spark SQL.
- Support for returning operation metrics from SQL [Delete](https://github.com/delta-io/delta/pull/1328 "https://github.com/delta-io/delta/pull/1328"), [Merge](https://github.com/delta-io/delta/pull/1327 "https://github.com/delta-io/delta/pull/1327"), and
  [Update](https://github.com/delta-io/delta/pull/1331 "https://github.com/delta-io/delta/pull/1331")
  commands. Previously these SQL commands returned an empty DataFrame, now
  they return a DataFrame with useful metrics about the operation
  performed.
- Optimize performance improvements:
  - Set the configuration option
    `spark.databricks.delta.optimize.repartition.enabled=true`
    to use `repartition(1)` instead of
    `coalesce(1)` in the Optimize command for better
    performance when compacting many small files.
  - [Improved
    performance](https://github.com/delta-io/delta/pull/1315 "https://github.com/delta-io/delta/pull/1315") by using a queue-based approach to
    parallelize compaction jobs.

- Other notable changes:
  - [Support
    for using variables](https://github.com/delta-io/delta/issues/1267 "https://github.com/delta-io/delta/issues/1267") in the VACUUM and OPTIMIZE SQL
    commands.
  - Improvements for CONVERT TO DELTA with catalog tables
    including:
    - [Autofill the partition schema](https://github.com/delta-io/delta/commit/18d4d12ed06f973006501f6c39c8785db51e2b1f "https://github.com/delta-io/delta/commit/18d4d12ed06f973006501f6c39c8785db51e2b1f") from the catalog
      when it's not provided.
    - [Use partition information](https://github.com/delta-io/delta/commit/ebff29904f3ababb889897343f8f8f7a010a1f71 "https://github.com/delta-io/delta/commit/ebff29904f3ababb889897343f8f8f7a010a1f71") from the catalog to
      find the data files to commit instead of doing a full
      directory scan. Instead of committing all data files in the
      table directory, only data files under the directories of
      active partitions will be committed.

  - [Support
    for Change Data Feed (CDF) batch reads](https://github.com/delta-io/delta/issues/1349 "https://github.com/delta-io/delta/issues/1349") on column mapping
    enabled tables when DROP COLUMN and RENAME COLUMN have not been
    used. For more information, see the [Delta Lake documentation](https://docs.delta.io/2.1.0/delta-change-data-feed.html#known-limitations "https://docs.delta.io/2.1.0/delta-change-data-feed.html#known-limitations").
  - [Improve
    Update command performance](https://github.com/delta-io/delta/pull/1202 "https://github.com/delta-io/delta/pull/1202") by enabling schema pruning in
    the first pass.

### Apache

Iceberg

- Added several [performance improvements](https://iceberg.apache.org/releases/#performance-improvements "https://iceberg.apache.org/releases/#performance-improvements") for scan planning and Spark
  queries.
- Added a common REST catalog client that uses change-based commits to
  resolve commit conflicts on the service side.
- `AS OF` syntax for SQL time travel queries is supported.
- Added merge-on-read support for MERGE and UPDATE queries.
- Added support to rewrite partitions using Z-order.
- Added a spec and implementation for Puffin, a format for large stats and
  index blobs, like [Theta sketches](https://datasketches.apache.org/docs/Theta/InverseEstimate.html "https://datasketches.apache.org/docs/Theta/InverseEstimate.html") or bloom filters.
- Added new interfaces for consuming data incrementally (both append and
  changelog scans).
- Added support for bulk operations and ranged reads to FileIO
  interfaces.
- Added more metadata tables to show delete files in the metadata
  tree.
- The drop table behavior changed. In Iceberg 0.13.1, running `DROP
TABLE` removes the table from the catalog and deletes the table
  contents as well. In Iceberg 1.0.0, `DROP TABLE` only removes the
  table from the catalog. To delete the table contents use `DROP TABLE
PURGE`.
- Parquet vectorized reads are enabled by default in Iceberg 1.0.0. If you
  want to disable vectorized reads, set
  `read.parquet.vectorization.enabled` to
  `false`.

### Oracle

Changes are minor.

### MySQL

Changes are minor.

### Amazon Redshift

AWS Glue 4.0 features a new Amazon Redshift connector with a new JDBC driver. For information about
the enhancements and how to migrate from previous AWS Glue versions, see [Redshift connections](aws-glue-programming-etl-connect-redshift-home.md "aws-glue-programming-etl-connect-redshift-home.md").

## Appendix A: Notable

dependency upgrades

The following are dependency upgrades:

| Dependency                   | Version in AWS Glue 4.0 | Version in AWS Glue 3.0 | Version in AWS Glue 2.0 | Version in AWS Glue 1.0 |
| ---------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Spark                        | 3.3.0-amzn-1            | 3.1.1-amzn-0            | 2.4.3                   | 2.4.3                   |
| Hadoop                       | 3.3.3-amzn-0            | 3.2.1-amzn-3            | 2.8.5-amzn-5            | 2.8.5-amzn-1            |
| Scala                        | 2.12                    | 2.12                    | 2.11                    | 2.11                    |
| Jackson                      | 2.13.3                  | 2.10.x                  | 2.7.x                   | 2.7.x                   |
| Hive                         | 2.3.9-amzn-2            | 2.3.7-amzn-4            | 1.2                     | 1.2                     |
| EMRFS                        | 2.54.0                  | 2.46.0                  | 2.38.0                  | 2.30.0                  |
| Json4s                       | 3.7.0-M11               | 3.6.6                   | 3.5.x                   | 3.5.x                   |
| Arrow                        | 7.0.0                   | 2.0.0                   | 0.10.0                  | 0.10.0                  |
| AWS Glue Data Catalog client | 3.7.0                   | 3.0.0                   | 1.10.0                  | N/A                     |
| Python                       | 3.10                    | 3.7                     | 2.7 & 3.6               | 2.7 & 3.6               |
| Boto                         | 1.26                    | 1.18                    | 1.12                    | N/A                     |

## Appendix B: JDBC driver

upgrades

The following are JDBC driver upgrades:

| Driver               | JDBC driver version in past AWS Glue versions | JDBC driver version in AWS Glue 3.0 | JDBC driver version in AWS Glue 4.0 |
| -------------------- | --------------------------------------------- | ----------------------------------- | ----------------------------------- |
| MySQL                | 5.1                                           | 8.0.23                              | 8.0.23                              |
| Microsoft SQL Server | 6.1.0                                         | 7.0.0                               | 9.4.0                               |
| Oracle Databases     | 11.2                                          | 21.1                                | 21.7                                |
| PostgreSQL           | 42.1.0                                        | 42.2.18                             | 42.3.6                              |
| MongoDB              | 2.0.0                                         | 4.0.0                               | 4.7.2                               |
| Amazon Redshift      | redshift-jdbc41-1.2.12.1017                   | redshift-jdbc41-1.2.12.1017         | redshift-jdbc42-2.1.0.16            |

## Appendix C: Connector

upgrades

The following are connector upgrades:

| Driver     | Connector version in AWS Glue 3.0 | Connector version in AWS Glue 4.0 |
| ---------- | --------------------------------- | --------------------------------- |
| MongoDB    | 3.0.0                             | 10.0.4                            |
| Hudi       | 0.10.1                            | 0.12.1                            |
| Delta Lake | 1.0.0                             | 2.1.0                             |
| Iceberg    | 0.13.1                            | 1.0.0                             |
| DynamoDB   | 1.11                              | 1.12                              |
