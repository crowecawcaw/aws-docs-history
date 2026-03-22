# Aurora MySQL database engine updates 2019-11-14 (version 2.04.7) (Deprecated)

**Version:** 2.04.7

Aurora MySQL 2.04.7 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7
and Aurora MySQL 1.x versions are compatible with MySQL 5.6.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can restore a snapshot from a currently supported Aurora MySQL release into Aurora MySQL 2.04.7. You also have the option to upgrade
existing Aurora MySQL 2.\* database clusters to Aurora MySQL 2.04.7. You can't upgrade an existing Aurora MySQL 1.\* cluster directly to
2.04.7; however, you can restore its snapshot to Aurora MySQL 2.04.7.

To create a cluster with an older version of Aurora MySQL, please specify the engine version through the AWS Management Console,
the AWS CLI, or the RDS API.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

###### Note

This version is currently not available in the following AWS Regions:
AWS GovCloud (US-East) [us-gov-east-1], AWS GovCloud (US-West) [us-gov-west-1],
Asia Pacific (Hong Kong) [ap-east-1], and Middle East (Bahrain) [me-south-1]. There will
be a separate announcement once it is made available.

###### Note

For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](../AuroraUserGuide/AuroraMySQL.Updates.Patching.md "../AuroraUserGuide/AuroraMySQL.Updates.Patching.md") in the
_Amazon Aurora User Guide_.

## Improvements

**High-priority fixes:**

**Connection Handling**

- Database availability has been improved to better service a surge
  in client connections while executing one or more DDLs. It is
  handled by temporarily creating additional threads when needed.
  You are advised to upgrade if the database becomes unresponsive
  following a surge in connections while processing DDL.
- Fixed an issue that resulted in an incorrect value for the
  `Threads_running` global status variable.

**Engine Restart**

- Fixed an issue of prolonged unavailability while restarting the
  engine. This addresses an issue in the buffer pool initialization.
  This issue occurs rarely but can potentially impact any supported
  release.

**General stability fixes:**

- Made improvements where queries accessing uncached data could be
  slower than usual. Customers experiencing unexplained elevated
  read latencies while accessing uncached data are encouraged to
  upgrade as they may be experiencing this issue.

## Comparison with Aurora MySQL version 1

The following Amazon Aurora MySQL features are supported in Aurora MySQL Version 1 (compatible with
MySQL 5.6), but these features are currently not supported in Aurora MySQL Version 2 (compatible
with MySQL 5.7).

- Asynchronous key prefetch (AKP). For more
  information, see [Optimizing Aurora indexed join queries with asynchronous key prefetch](../AuroraUserGuide/AuroraMySQL.BestPractices.md#Aurora.BestPractices.AKP "../AuroraUserGuide/AuroraMySQL.BestPractices.md#Aurora.BestPractices.AKP") in the
  _Amazon Aurora User Guide_.
- Hash joins. For more information, see [Optimizing large Aurora MySQL join queries with hash joins](../AuroraUserGuide/AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin "../AuroraUserGuide/AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin") in the
  _Amazon Aurora User Guide_.
- Native functions for synchronously invoking AWS Lambda functions. For more
  information, see [Invoking a Lambda function with an Aurora MySQL native function](../AuroraUserGuide/AuroraMySQL.Integrating.Lambda.md#AuroraMySQL.Integrating.NativeLambda "../AuroraUserGuide/AuroraMySQL.Integrating.Lambda.md#AuroraMySQL.Integrating.NativeLambda") in the
  _Amazon Aurora User Guide_.
- Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md "AuroraMySQL.Updates.20171211.md").
- Migrating data from MySQL using an Amazon S3 bucket. For more information, see [Migrating data from MySQL by using an Amazon S3 bucket](../AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.md#AuroraMySQL.Migrating.ExtMySQL.S3 "../AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.md#AuroraMySQL.Migrating.ExtMySQL.S3") in the
  _Amazon Aurora User Guide_.

## MySQL 5.7 compatibility

Aurora MySQL 2.04.7 is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes,
and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver

> 20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

Aurora MySQL 2.04.7 does not currently support the following MySQL 5.7 features:

- Group replication plugin
- Increased page size
- InnoDB buffer pool loading at startup
- InnoDB full-text parser plugin
- Multisource replication
- Online buffer pool resizing
- Password validation plugin
- Query rewrite plugins
- Replication filtering
- The `CREATE TABLESPACE` SQL statement
