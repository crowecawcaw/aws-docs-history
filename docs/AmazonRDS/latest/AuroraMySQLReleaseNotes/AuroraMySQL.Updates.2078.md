# Aurora MySQL database engine updates 2022-06-16 (version 2.07.8) (Deprecated)

**Version:** 2.07.8

Aurora MySQL 2.07.8 is generally available. Aurora MySQL 2.\* versions are compatible with MySQL 5.7
and Aurora MySQL 1.\* versions are compatible with MySQL 5.6.

###### Note

This version is designated as a long-term support (LTS) release.
For more information, see [Aurora MySQL long-term support (LTS) releases](../AuroraUserGuide/AuroraMySQL.Updates.Versions.md#AuroraMySQL.Updates.LTS "../AuroraUserGuide/AuroraMySQL.Updates.Versions.md#AuroraMySQL.Updates.LTS") in the _Amazon Aurora User Guide_.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can restore a snapshot from a currently supported Aurora MySQL release into Aurora MySQL 2.07.8. You also have the option to upgrade
existing Aurora MySQL 2.\* database clusters to Aurora MySQL 2.07.8. In-place upgrade is available for Aurora MySQL 1.\* clusters to Aurora MySQL 2.\*
(see [Upgrading from Aurora MySQL 1.x to 2.x](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Updates.MajorVersionUpgrade.1to2 "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Updates.MajorVersionUpgrade.1to2")). It's also available for Aurora MySQL 2.\* clusters to Aurora MySQL 3.\*
(see [Upgrading from Aurora MySQL 2.x to 3.x](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Updates.MajorVersionUpgrade.2to3 "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Updates.MajorVersionUpgrade.2to3")).

To create a cluster with an older version of Aurora MySQL, specify the engine version through the AWS Management Console, the AWS CLI, or the RDS API.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

###### Note

For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](../AuroraUserGuide/AuroraMySQL.Updates.Patching.md "../AuroraUserGuide/AuroraMySQL.Updates.Patching.md") in the
_Amazon Aurora User Guide_.

## Improvements

**Security fixes:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below:

- [CVE-2022-21245](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21245 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21245")
- [CVE-2021-36222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222")
- [CVE-2021-22926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22926 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22926")

**General improvements:**

- Fixed an issue which, in rare cases, causes the database server to restart when the deadlock detector thread gets stuck because of a race condition.

## Integration of MySQL community edition bug fixes

- When an UPDATE required a temporary table having a primary key larger than 1024 bytes and that table was created using InnoDB, the server could exit. (Bug #25153670)

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
