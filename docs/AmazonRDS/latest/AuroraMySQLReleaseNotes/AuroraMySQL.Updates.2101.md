# Aurora MySQL database engine updates 2021-10-21 (version 2.10.1) (Deprecated)

**Version:** 2.10.1

Aurora MySQL 2.10.1 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7, and Aurora MySQL
1.x versions are compatible with MySQL 5.6.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.10.0. For clusters running
Aurora MySQL version 1, you can upgrade an existing Aurora MySQL 1.23 or higher cluster directly to 2.10.0. You can
also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.10.0.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

###### Note

For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](../AuroraUserGuide/AuroraMySQL.Updates.Patching.md "../AuroraUserGuide/AuroraMySQL.Updates.Patching.md") in the
_Amazon Aurora User Guide_.

## Improvements

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below:

- [CVE-2021-2307](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2307 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2307")
- [CVE-2021-2226](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2226 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2226")
- [CVE-2021-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2194 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2194")
- [CVE-2021-2174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2174 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2174")
- [CVE-2021-2171](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2171 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2171")
- [CVE-2021-2169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2169 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2169")
- [CVE-2021-2166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166")
- [CVE-2021-2160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2160 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2160")
- [CVE-2021-2154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154")
- [CVE-2021-2032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2032 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2032")
- [CVE-2021-2001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2001 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2001")

**Availability improvements:**

- Added the ability to cleanly shut down the cluster for future major version upgrades.

**General improvements:**

- Fixed an issue that can cause high CPU consumption on the reader instances due to excessive logging
  of informational messages in internal diagnostic log files.
- Fixed an issue where the value of a TIMESTAMP column of an existing row is updated to the latest timestamp
  when all of the following conditions are satisfied:

  1.  A trigger exists for the table.
  2.  An INSERT is performed on the table that has an ON DUPLICATE KEY UPDATE clause.
  3.  The inserted row causes a duplicate value violation in a UNIQUE index or PRIMARY KEY.
  4.  One or more columns are of TIMESTAMP data type and have a default value of CURRENT_TIMESTAMP.

- Fixed an issue introduced in version 2.10.0 which causes use of json_merge function to raise an error code in
  certain cases. In particular, when json_merge function is used in a DDL containing generated columns,
  it can return error code 1305.
- Fixed an issue where, in rare conditions, read replicas restarts when a large object's update history is
  being validated for a transaction's read view on the read replica.
- Fixed an issue which, in rare conditions, causes a writer instance to restart when an in-memory data- integrity check fails.

## Integration of MySQL community edition bug fixes

- CURRENT_TIMESTAMP PRODUCES ZEROS IN TRIGGER. (Bug #25209512)

## Comparison with Aurora MySQL version 1

The following Amazon Aurora MySQL features are supported in Aurora MySQL version 1 (compatible with
MySQL 5.6), but these features are currently not supported in Aurora MySQL version 2 (compatible
with MySQL 5.7).

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
