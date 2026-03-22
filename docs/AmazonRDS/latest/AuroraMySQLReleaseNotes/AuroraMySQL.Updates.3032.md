# Aurora MySQL database engine updates 2023-08-29 (version 3.03.2) (Deprecated)

**Version:** 3.03.2

Aurora MySQL 3.03.2 is generally available. Aurora MySQL 3.04 versions are compatible with MySQL 8.0.28, Aurora MySQL 3.03 versions are compatible with MySQL 8.0.26, and Aurora MySQL 3.02 versions
are compatible with MySQL 8.0.23. For more information on community changes that have occurred from 8.0.23 to 8.0.28, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.MySQL80.md "../AuroraUserGuide/AuroraMySQL.MySQL80.md").
For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0
Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md").

Currently available Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 3.01.\*, 3.02.\*, 3.03.\*, and 3.04.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md")
from any currently available Aurora MySQL version 2 cluster into an Aurora MySQL version 3.03.2 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Upgrade planning for Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-planning "../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-planning") in the _Amazon Aurora User Guide_. For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting upgrade issues with Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting "../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting").

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## Improvements

**Fixed security issues and CVEs:**

- Fixed an issue that might cause the audit log to miss events during audit log file rotation.

The following CVE fixes are included in this release:

- [CVE-2023-21963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21963 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21963")
- [CVE-2023-21912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21912 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21912")
- [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215")
- [CVE-2022-43551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43551 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43551")
- [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434")

**Availability improvements:**

- Fixed an issue that can cause database restarts during long transaction recovery.
- Fixed an issue that can cause the database cluster to become unavailable when the writer instance restarts while the database
  was creating or dropping triggers on internal system tables.
- Fixed an issue that can cause a database instance to restart while executing a query which references an aggregate
  function.
- Fixed an issue that can cause a database restart during the rollback of an `INSERT` statement when parallel query
  is enabled.
- Fast insert is enabled only for regular InnoDB tables in Aurora MySQL version 3.03.2 and higher. This optimization doesn’t
  work for InnoDB temporary tables. For more information on the fast insert optimization, see
  [Amazon Aurora MySQL
  performance enhancements](../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance "../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance").

**General improvements:**

- Fixed an issue where the reader instance is unable to open a table, with `ERROR 1146`.
  This issue occurs when executing certain types of online Data Definition Language (DDL) while the `INPLACE` algorithm is being used on the writer instance.
- Introduced file management performance optimizations on binlog replicas to help reduce contention when writing to relay log files.
- Fixed an issue when parallel query is enabled that causes the query plan optimizer to pick an inefficient execution plan for certain `SELECT` queries that benefit from a primary or secondary index.
- Added logical replication support for the following Data Control Language (DCL) statements: `GRANT/REVOKE` and `CREATE/DROP/ALTER/RENAME USER`.
- Parallel query for Amazon Aurora MySQL is not supported when choosing the Aurora I/O-Optimized cluster configuration. See [Limitations of parallel query for Aurora MySQL](../AuroraUserGuide/aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-limitations "../AuroraUserGuide/aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-limitations") for more information.

**Upgrades and migrations:**

- To perform a minor version upgrade for an Aurora global database from Aurora MySQL version 3.01 or 3.02 to Aurora MySQL version 3.03 or higher, refer to
  [Upgrading Aurora MySQL by modifying the engine version](../AuroraUserGuide/AuroraMySQL.Updates.Patching.md#AuroraMySQL.Updates.Patching.ModifyEngineVersion "../AuroraUserGuide/AuroraMySQL.Updates.Patching.md#AuroraMySQL.Updates.Patching.ModifyEngineVersion").
- Fixed an issue which can cause major version upgrade failures when upgrading to Aurora MySQL version 3 when a trigger definition contains a reserved keyword that is not enclosed in quotation marks.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.26, in addition to the below. For more information, see
[MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3").

- Fixed an issue which can sometimes produce incorrect query results while processing complex SQL statements consisting of multiple nested
  Common Table Expressions (CTEs). (Bug #34572040, Bug #34634469, Bug #33856374)
- InnoDB: A race condition between threads attempting to deinitialize and initialize statistics for the same table raised an assertion failure. (Bug #33135425)
- InnoDB: Prevent online DDL operations from accessing out-of-bounds memory. (Bug #34750489, Bug #108925)
