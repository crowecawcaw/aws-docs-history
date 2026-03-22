# Aurora MySQL database engine updates 2023-11-13 (version 3.04.1, compatible with MySQL 8.0.28)

**Version:** 3.04.1

Aurora MySQL 3.04.1 is generally available. Aurora MySQL 3.04 versions are compatible with MySQL 8.0.28. For more information on community changes that have occurred, see
[MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

###### Note

This version is designated as a long-term support (LTS) release. For more information, see [Aurora MySQL long-term support (LTS)
releases](../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md#AuroraMySQL.Updates.LTS "../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md#AuroraMySQL.Updates.LTS") in the _Amazon Aurora User Guide_.

We recommend that you don't set the `AutoMinorVersionUpgrade` parameter to
`true` (or enable **Auto minor version upgrade** in the AWS Management Console) for LTS versions. Doing so could lead
to your DB cluster being upgraded to the next target version for Automatic Minor Version Upgrade campaign, which may not be an LTS version.

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.MySQL80.md "../AuroraUserGuide/AuroraMySQL.MySQL80.md").
For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see
[Comparing Aurora MySQL version 2 and Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md").
For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see
[Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md").

Currently supported Aurora MySQL releases are 2.07.9, 2.7.10, 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, 3.04.\*, and 3.05.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS
Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") from any currently available Aurora MySQL version 2 cluster into an Aurora MySQL version 3.04.1 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Upgrade planning for Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-planning "../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-planning") in the _Amazon Aurora User Guide_. For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting upgrade issues with Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting "../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting").

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## Improvements

**Availability improvements:**

- Fixed an issue where Aurora MySQL database instances using parallel query may experience a database restart when running a high number of concurrent parallel queries.
- Fixed an issue which can cause the executed GTID set to be recovered incorrectly on a binary log (binlog) replica cluster with enhanced binlog enabled when any binlog
  source has set `gtid_mode` to `ON` or `ON_PERMISSIVE`. This issue may cause the replica cluster's writer instance to restart an additional
  time during recovery, or lead to incorrect results when querying the executed GTID set.
- Fixed a memory management issue that can cause an Aurora MySQL database instance restart or a failover due to a decrease in freeable memory when enhanced binary log is enabled.
- Fixed an issue which can cause the reader instance to restart when the writer instance grows the database volume to a multiple of 160GB.
- Fixed an issue where an Aurora MySQL database instance with the enhanced binary log feature enabled might get stuck during the database instance startup as the binary log
  recovery process is being executed.
- Fixed an issue which can cause a database instance restart due to a deadlatch when running [`SHOW STATUS`](https://dev.mysql.com/doc/refman/8.0/en/show-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-status.html")
  and [`PURGE BINARY LOGS`](https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html "https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html") statements concurrently. The purge binary logs is a managed
  statement that is executed to honor the user configured binlog retention period.
- Fixed an issue which can cause database cluster unavailability if the writer instance restarts while the database is creating or dropping triggers on internal system tables.
- Fixed an issue which can cause a database instance restart due to a long semaphore wait when using the enhanced binlog feature on a cluster with an Aurora replica.

**General improvements:**

- Fixed an issue which can cause database unavailability when enhanced binlog is enabled on an Aurora Serverless v2 database cluster running on Aurora MySQL 3.04.0.
- Removed unused storage metadata before writing to Aurora Storage when the enhanced binlog feature is enabled. This avoids certain scenarios when a database
  restart or failover may occur because of increased write latency due to increased bytes transmitted over the network.
- Fixed an issue where Aurora specific performance schema tables were not created upon an upgrade or migration.
- Fixed an issue which can cause the `NumBinaryLogFiles` metrics on CloudWatch to display incorrect results when enhanced binlog is enabled.

**Upgrades and migrations:**

- Upgrading from MySQL 5.7 to MySQL 8.0 with a very large number of tables in a single database caused the server to consume excessive memory.
  It was found that, during the process of checking whether tables could be upgraded, we fetched all the data dictionary `Table` objects upfront,
  processing each and fetching its name, then performed [`CHECK TABLE ... FOR UPGRADE`](https://dev.mysql.com/doc/refman/8.0/en/check-table.html#check-table-version-compatibility "https://dev.mysql.com/doc/refman/8.0/en/check-table.html#check-table-version-compatibility") on the list. Fetching all objects beforehand was not necessary in this case, and contributed
  greatly to memory consumption. To correct this problem, we now fetch one `Table` object at a time in such cases, performing any required checks,
  fetching its name, and releasing the object, before proceeding with the next one. (Bug #34526001)

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.28, in addition to the below. For more information, see
[MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3").

- Fixed an issue which can cause higher CPU utilization due to background TLS certificate rotation (Community Bug Fix #34284186)
