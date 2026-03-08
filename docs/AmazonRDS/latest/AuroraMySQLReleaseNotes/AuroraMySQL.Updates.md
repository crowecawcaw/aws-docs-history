# Aurora MySQL database engine updates 2019-05-09 (version 2.04.3) (Deprecated)

**Version:** 2.04.3

Aurora MySQL 2.04.3 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7
and Aurora MySQL 1.x versions are compatible with MySQL 5.6.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

When creating a new Aurora MySQL DB cluster (including restoring a snapshot), you have the
option of choosing compatibility with either MySQL 5.7 or MySQL 5.6. We do not allow in-place
upgrade of Aurora MySQL 1.\* clusters or restore of Aurora MySQL 1.\* clusters from an Amazon S3 backup into Aurora MySQL 2.04.3.
We plan to remove these restrictions in a later Aurora MySQL 2.\* release.

You can restore snapshots of Aurora MySQL 1.14.\*, 1.15.\*, 1.16.\*, 1.17.\*, 1.18.\*, 1.19.\*,
2.01.\*, 2.02.\*, 2.03.\*, and 2.04.\* into Aurora MySQL 2.04.3.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.md "../AuroraUserGuide/USER_UpgradeDBInstance.md") in the _Amazon Aurora User Guide_.

###### Note

This version is currently not available in the AWS GovCloud (US-West) [us-gov-west-1]
and China (Ningxia) [cn-northwest-1] AWS Regions. There will be a separate announcement once
it is made available.

###### Note

For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](../AuroraUserGuide/AuroraMySQL.Updates.md "../AuroraUserGuide/AuroraMySQL.Updates.md") in the
_Amazon Aurora User Guide_.

## Improvements

- Fixed a bug in binlog replication that can cause an issue on Aurora instances configured
  as binlog worker.
- Fixed an out-of-memory condition when handling large stored routines.
- Fixed an error in handling certain kinds of `ALTER TABLE` commands.
- Fixed an issue with aborted connections because of an error in network protocol
  management.

## Comparison with Aurora MySQL version 1

The following Amazon Aurora MySQL features are supported in Aurora MySQL Version 1 (compatible with
MySQL 5.6), but these features are currently not supported in Aurora MySQL Version 2 (compatible
with MySQL 5.7).

- Asynchronous key prefetch (AKP). For more
  information, see [Optimizing Aurora indexed join queries with asynchronous key prefetch](../AuroraUserGuide/AuroraMySQL.md#Aurora.BestPractices.AKP "../AuroraUserGuide/AuroraMySQL.md#Aurora.BestPractices.AKP") in the
  _Amazon Aurora User Guide_.
- Hash joins. For more information, see [Optimizing large Aurora MySQL join queries with hash joins](../AuroraUserGuide/AuroraMySQL.md#Aurora.BestPractices.HashJoin "../AuroraUserGuide/AuroraMySQL.md#Aurora.BestPractices.HashJoin") in the
  _Amazon Aurora User Guide_.
- Native functions for synchronously invoking AWS Lambda functions. For more
  information, see [Invoking a Lambda function with an Aurora MySQL native function](../AuroraUserGuide/AuroraMySQL.Integrating.md#AuroraMySQL.Integrating.NativeLambda "../AuroraUserGuide/AuroraMySQL.Integrating.md#AuroraMySQL.Integrating.NativeLambda") in the
  _Amazon Aurora User Guide_.
- Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md").
- Migrating data from MySQL using an Amazon S3 bucket. For more information, see [Migrating data from MySQL by using an Amazon S3 bucket](../AuroraUserGuide/AuroraMySQL.Migrating.md#AuroraMySQL.Migrating.ExtMySQL.S3 "../AuroraUserGuide/AuroraMySQL.Migrating.md#AuroraMySQL.Migrating.ExtMySQL.S3") in the
  _Amazon Aurora User Guide_.

## MySQL 5.7 compatibility

Aurora MySQL 2.04.3 is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes,
and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver

> 20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

Aurora MySQL 2.04.3 does not currently support the following MySQL 5.7 features:

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
