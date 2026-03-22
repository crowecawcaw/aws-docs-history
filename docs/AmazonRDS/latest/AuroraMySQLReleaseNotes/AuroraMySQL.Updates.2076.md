# Aurora MySQL database engine updates 2021-09-02 (version 2.07.6) (Deprecated)

**Version:** 2.07.6

Aurora MySQL 2.07.6 is generally available. Aurora MySQL 2.\* versions are compatible with MySQL 5.7
and Aurora MySQL 1.\* versions are compatible with MySQL 5.6.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can restore a snapshot from a currently supported Aurora MySQL release into Aurora MySQL 2.07.6. You also have the option to upgrade
existing Aurora MySQL 2.\* database clusters to Aurora MySQL 2.07.6. You can't upgrade an existing Aurora MySQL 1.\* cluster directly to
2.07.6; however, you can restore its snapshot to Aurora MySQL 2.07.6.

To create a cluster with an older version of Aurora MySQL, please specify the engine version through the AWS Management Console, the AWS CLI, or the RDS API.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## Integration of MySQL community edition bug fixes

- INSERTING 64K SIZE RECORDS TAKE TOO MUCH TIME. ([Bug#23031146](https://github.com/mysql/mysql-server/commit/a2f9ea422e4bdfd65da6dd0c497dc233629ec52e "https://github.com/mysql/mysql-server/commit/a2f9ea422e4bdfd65da6dd0c497dc233629ec52e"))

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

This Aurora MySQL version is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes,
and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver

> 20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

This Aurora MySQL version does not currently support the following MySQL 5.7 features:

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
