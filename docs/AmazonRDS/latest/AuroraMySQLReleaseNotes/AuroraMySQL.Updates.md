# Aurora MySQL database engine updates 2022-01-06 (version 2.08.4) (Deprecated)

**Version:** 2.08.4

Aurora MySQL 2.08.4 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7
and Aurora MySQL 1.x versions are compatible with MySQL 5.6.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.10.0. For clusters running
Aurora MySQL version 1, you can upgrade an existing Aurora MySQL 1.23 or higher cluster directly to 2.10.0. You can
also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.10.0.

To create a cluster with an older version of Aurora MySQL, specify the engine version through the AWS Management Console, the
AWS CLI, or the Amazon RDS API.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.md "../AuroraUserGuide/USER_UpgradeDBInstance.md") in the _Amazon Aurora User Guide_.

###### Note

For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](../AuroraUserGuide/AuroraMySQL.Updates.md "../AuroraUserGuide/AuroraMySQL.Updates.md") in the
_Amazon Aurora User Guide_.

## Improvements

**Security fixes and general improvements:**

- Fixed security issues related to Aurora MySQL integration
  with other AWS Services such as Amazon S3, Amazon ML, and AWS Lambda.
- Fixed an issue where the value of a TIMESTAMP column of an existing row
  is updated to the latest timestamp when all of the following conditions are satisfied:

1.  a trigger exists for the table; 2. an INSERT is performed on the table that has an
    ON DUPLICATE KEY UPDATE clause; 3. the inserted row can cause a duplicate value violation
    in a UNIQUE index or PRIMARY KEY; and 4. one or more columns are of TIMESTAMP data type
    and have a default value of CURRENT_TIMESTAMP.

- Fixed an issue which, in rare conditions, causes a writer instance to restart when an
  in-memory data-integrity check fails.
- Fixed an issue with parallel query which could cause the database to restart when
  executing SQL statements with a LIMIT clause.

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
- Scan batching. For more information, see [Aurora MySQL database engine updates
  2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md").
- Migrating data from MySQL using an Amazon S3 bucket. For more information, see [Migrating data from MySQL by using an Amazon S3 bucket](../AuroraUserGuide/AuroraMySQL.Migrating.md#AuroraMySQL.Migrating.ExtMySQL.S3 "../AuroraUserGuide/AuroraMySQL.Migrating.md#AuroraMySQL.Migrating.ExtMySQL.S3") in the
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
