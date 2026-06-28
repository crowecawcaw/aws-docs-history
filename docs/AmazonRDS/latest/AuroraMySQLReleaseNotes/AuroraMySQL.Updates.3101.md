# Aurora MySQL database engine updates 2025-09-30 (version 3.10.1, compatible with MySQL 8.0.42)

**Version:** 3.10.1

Aurora MySQL 3.10.1 is generally available. Aurora MySQL 3.10 versions are compatible with MySQL 8.0.42. For more information on the
community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.MySQL80.md "../AuroraUserGuide/AuroraMySQL.MySQL80.md"). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md") in the _Amazon Aurora User Guide_.

You can perform an in-place upgrade [leveraging Zero Downtime Patching (ZDP)](../AuroraUserGuide/AuroraMySQL.Updates.ZDP.md "../AuroraUserGuide/AuroraMySQL.Updates.ZDP.md"), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.10.1 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning"). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](../AuroraUserGuide/AuroraMySQL.Upgrading.Troubleshooting.md "../AuroraUserGuide/AuroraMySQL.Upgrading.Troubleshooting.md") in the _Amazon Aurora User Guide_.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see [Maintaining an Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## Improvements

**Availability improvements:**

- Fixed an issue with the page latching order sent to reader instances. It can cause the reader instance to restart due to a deadlatch when running SELECT queries over tables being updated by its writer.
- Fixed an issue that could cause a reader instance's restart to fail when the writer is running a large number of DDL operations.
- Fixed an issue which could cause Aurora MySQL Serverless v2 instances to restart when the innodb\_purge\_threads parameter was manually configured to a value different from the default. The innodb\_purge\_threads parameter is now automatically managed for Aurora Serverless v2 instances and cannot be modified.
- Fixed an issue with Aurora Serverless V2 scaling that resulted in DB instance restarts by preventing critical memory pages from being swapped out.
- Fixed an issue where Aurora out of memory (OOM) avoidance wasn't persisting the configured aurora\_oom\_response DB parameter value after database restart.
- Fixed a race condition which could cause availability issue after a failover in Multi-AZ clusters.
- Fixed an issue in logical recovery with aurora\_enhanced\_binlog enabled that could prevent database restarts in case of aborted transactions.
- Resolved an issue where database instances could become unresponsive during Parallel Query (PQ) workloads.
- Fixed an issue which prevented users with CONNECTION\_ADMIN or SUPER privileges from performing an additional connection beyond max\_connections limit, as supported in MySQL Community Edition.

**General improvements:**

- Fixed an issue that can cause continuous database server restarts when the volume was allowed to grow to its maximum size due to certain types of queries being mistakenly allowed after the volume was greater than a certain threshold.
- Fixed an issue that can cause the writer instance to become irresponsive if reader instances restart while using Global Write Forwarding or Local Write Forwarding.
- Fixed an issue that could cause the writer instance to restart when performing ALTER TABLE in parallel with read queries.
- Fixed an issue to improve availability with large volume (> 64 TB) bootstrapping during the parallel export operation.
- Fixed an issue that could cause a database instance restart operation to fail if max\_user\_connections is set to a low value.
- Fixed an issue causing inaccurate AbortedClients metrics when multiple connections terminate unexpectedly.
- Resolved a race condition that could cause incorrect page reads from the buffer pool during Aurora Serverless scale-down operations or during page eviction from the buffer pool.
  Ref [community Bug#116305](https://bugs.mysql.com/bug.php?id=116305 "https://bugs.mysql.com/bug.php?id=116305").
- Fixed an issue that causes unexpected "Internal write forwarding error" on reader instances when write forwarding is enabled.
- Fixed an issue which could cause the Previous\_gtids binlog event to exclude certain GTIDs with Enhanced Binlog enabled and gtid\_mode set to ON or ON\_PERMISSIVE.
- Fixed an issue which can cause memory management issue when parallel query operations on the table with the blob fields.
- Fixed issue where a column with partial JSON updates will fail Parallel Export causing internal fallback to a much slower RDS Export.
- Fixed an issue that can cause unexpected instance restarts when there is high concurrent write forwarding workload.
- Fixed an issue where Zero Downtime Patching (ZDP) / Zero Downtime Restart (ZDR) could result in DB instance restart while restoring warnings with invalid error codes.
- Fixed an issue where temporary binary log files were not being properly cleaned up after transaction rollbacks when using binary logging. This fix prevents unnecessary storage consumption from retained temporary files and in certain cases could also prevent anomalies in the binary log files.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.42.
For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3").

- A query of the form SELECT 1 FROM t WHERE CAST(a AS UNSIGNED INTEGER) = 1 AND a = (SELECT 1 FROM t) led to an assertion in item\_func.cc. (Bug #36128964)
