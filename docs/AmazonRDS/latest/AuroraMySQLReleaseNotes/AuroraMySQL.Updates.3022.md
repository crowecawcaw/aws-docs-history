# Aurora MySQL database engine updates 2022-11-18 (version 3.02.2) (Deprecated)

**Version:** 3.02.2

Aurora MySQL 3.02.2 is generally available. Aurora MySQL 3.02 versions are compatible with MySQL 8.0.23, Aurora MySQL
2.x versions are compatible with MySQL 5.7, and Aurora MySQL 1.x versions are compatible with MySQL 5.6.

For details of new features in Aurora MySQL version 3 and differences between Aurora MySQL version 3 and Aurora MySQL
version 2 or community MySQL 8.0, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.Compare-v2-v3 "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.Compare-v2-v3") in the _Amazon Aurora User Guide_.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can restore a snapshot from any currently supported Aurora MySQL version 2 cluster into Aurora MySQL 3.02.2.

For information on planning an upgrade to Aurora MySQL version 3, see
[Upgrade planning for Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-planning "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-planning") in the _Amazon Aurora User Guide_.
For the upgrade procedure itself, see
[Upgrading to Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-procedure "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-procedure") in the _Amazon Aurora User Guide_.
For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting upgrade issues with Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-troubleshooting "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-troubleshooting").

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## Improvements

Aurora MySQL version 3.02.2 is generally available and generally compatible with community MySQL 8.0.23.

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below:

- [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451")
- [CVE-2021-36222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222")
- [CVE-2021-22926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22926 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22926")

- [CVE-2022-21444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451")

**Availability improvements:**

- Fixed an issue which can cause the database instance to restart due to incorrectly accessing the invalid memory when a
  connection to the database instance is closed explicitly or implicitly.
- Fixed an issue which can cause the database startup to be interrupted repeatedly on larger instance classes due to buffer pool
  initialization taking longer than expected.
- Fixed an issue which, in rare conditions, can cause the database instance to restart when Aurora Serverless v2 incorrectly
  attempts to update the table cache while scaling.
- Fixed an issue which, in rare conditions, could cause the database to restart when processing a query with a GROUP BY clause
  that truncates a decimal column to zero decimal places.
- Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running
  queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast
  insert optimization, see [Amazon Aurora MySQL performance enhancements](../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance "../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance").

**General improvements:**

- Fixed an issue that can cause upgrade failures from Aurora MySQL version 2 (compatible with MySQL 5.7) to Aurora MySQL version 3
  (compatible with MySQL 8.0) due to a metadata inconsistency in the mysql.host table.
- Added performance improvements to reduce the upgrade time from Aurora MySQL version 2 (compatible with MySQL 5.7) to Aurora MySQL
  version 3 (compatible with MySQL 8.0). By parallelizing certain upgrade steps, the time is further shortened when using
  larger instance classes, such as db.r6g.16xlarge or db.r5.24xlarge.
- Added support for displaying all errors when upgrading from Aurora MySQL version 2 (compatible with MySQL 5.7) to Aurora MySQL
  version 3 (compatible with MySQL 8.0) when previous versions were limited to displaying only 50 errors.
- Fixed an issue, which in rare conditions, can cause the auto-increment counters to be incorrect after a major version upgrade
  from Aurora MySQL version 2 (compatible with MySQL 5.7) to Aurora MySQL version 3 (compatible with MySQL 8.0).
- Fixed an issue that can cause major version upgrades from Aurora MySQL version 2 to Aurora MySQL version 3 to fail because
  migrating the `mysql.innodb\_table\_stats` and `mysql.innodb\_index\_stats` tables took longer than expected. This issue
  mainly affected database clusters with a large numbers of tables (>1.5 million).
- Fixed an issue that can cause major version upgrades from Aurora MySQL version 2 to Aurora MySQL version 3 to fail due to a defect
  in AMS 8.0 engine upgrade workflow, which causes the log records to be accumulated on the Aurora storage cluster volume
  and stops normal write operations. This issue mainly affected database clusters with large numbers of tables,
  approximately >750k.
- Fixed an issue that prevents Aurora MySQL Serverless v2 idle instances from scaling down to 0.5 ACUs because the MySQL purge
  threads were incorrectly kept active.
- Fixed an issue where applications may experience increased latency while connecting to a database instance when the instance
  is experiencing a sudden increase in incoming connections.
- Introduced two new Amazon CloudWatch metrics to help troubleshoot connection establishment delays for Aurora MySQL database instances.
  More information on AuroraSlowHandshakeCount and AuroraSlowConnectionHandleCount metrics can be found in the [Aurora
  CloudWatch metrics definitions](../AuroraUserGuide/Aurora.AuroraMySQL.Monitoring.Metrics.md "../AuroraUserGuide/Aurora.AuroraMySQL.Monitoring.Metrics.md").

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.23, in addition to the below. For more information, see
[MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3").

- Fixed an issue which, in certain conditions, may return incorrect results due to an inaccurate calculation of the nullability
  property when executing a query with an OR condition. (Bug #34060289)
- Fixed an issue which, in certain conditions, may return incorrect results when the following two conditions are met:

  - A derived table is merged into the outer query block.
  - The query includes a left join and an IN subquery. (Bug #34060289)

- Fixed an issue where it was not possible to revoke the DROP privilege on the Performance Schema. (Bug #33578113)
- Fixed an issue where a stored procedure containing an IF statement using EXISTS, which acted on one or more tables that were
  deleted and recreated between executions, did not execute correctly for subsequent invocations following the first one.
  (MySQL Bug #32855634).
- Incorrect AUTO_INCREMENT values were generated when the maximum integer column value was exceeded. The error was due to the
  maximum column value not being considered. The previous valid AUTO_INCREMENT value should have been returned in this
  case, causing a duplicate key error. (Bug #87926, Bug #26906787)
- Fixed an issue which can lead to a failure while upgrading an Aurora MySQL version 1 (Compatible with MySQL 5.6) database
  cluster containing user-created table with certain table IDs. Assignment of these table IDs may result in conflicting
  data dictionary table IDs while upgrading from Aurora MySQL version 2 (Compatible with MySQL 5.7) to Aurora MySQL
  version 3 (Compatible with MySQL 8.0) (Bug #33919635)
