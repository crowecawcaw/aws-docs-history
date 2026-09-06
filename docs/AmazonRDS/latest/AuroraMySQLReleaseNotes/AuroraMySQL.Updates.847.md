

# Aurora MySQL 8.4.7, May 21, 2026
<a name="AuroraMySQL.Updates.847"></a><a name="8.4.7"></a>

**Version:** 8.4.7

This release of Aurora MySQL is compatible with MySQL 8.4.7. For more information on the community changes that have occurred, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/).

For details of the new features in Aurora MySQL version 8.4, see [Aurora MySQL version 8.4 compatible with MySQL 8.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL84.html). For differences between Aurora MySQL version 8.4 and version 3, see [Comparison of Aurora MySQL version 3 and Aurora MySQL version 8.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v3-v84.html). For a comparison with MySQL 8.4 Community Edition, see [Comparison of Aurora MySQL version 8.4 and MySQL 8.4 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v84-community.html) in the *Amazon Aurora User Guide*.

You can perform an in-place major version upgrade, restore a snapshot with upgrade, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html). You can upgrade from any currently supported Aurora MySQL version 3 cluster to Aurora MySQL version 8.4.7.

For information on planning an upgrade to Aurora MySQL version 8.4, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## New features
<a name="AuroraMySQL.Updates.847.NewFeatures"></a>
+ Added support for password management capabilities in Aurora MySQL 8.4, configurable using the cluster parameter group settings. For a full description of MySQL password management capabilities and configuration options, refer to the [MySQL 8.4 Reference Manual, Section 8.2.15 – Password Management](https://dev.mysql.com/doc/refman/8.4/en/password-management.html).
+ Added support for the `validate_password` component for enforcing password strength policies, enabled via the `aurora_enable_validate_password_component` parameter and configured through the cluster parameter group.
+ Introduced automatic memory management for Aurora MySQL 8.4 with the new `aurora_enable_memory_management` parameter. When set to `ON` (the default), Aurora automatically manages memory recovery actions to prevent out-of-memory (OOM) database restarts, and the `aurora_oom_response` parameter is ignored. Set `aurora_enable_memory_management` to `OFF` to control recovery actions manually through `aurora_oom_response`. For more information, see [Amazon Aurora MySQL out-of-memory issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQLOOM.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.847.Improvements"></a>

Below are the improvements made compared to Aurora MySQL 3.12.0, see [Aurora MySQL 3.12.0 Release Notes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.3120.html).

**Availability improvements:**
+ Fixed an issue that can cause the writer instance to repeatedly restart. This occurs when the writer restarts while purging an undo record for a table with indexes on virtual columns.
+ Fixed an issue that could cause new database cluster creation to fail, requiring the cluster to be deleted and recreated.
+ Fixed an issue where the database writer instance could restart unexpectedly during a global database switchover operation. The restart occurred while cleaning up temporary tables after SQL statement processing. This could result in longer switchover completion time.
+ Improved the performance of Aurora physical replication by applying changes from the writer instance on reader instances using multiple threads.
+ Fixed an issue which could cause read replicas to restart when the writer instance commits a large transaction with binlog enabled. This issue could also cause errors when reading the binlog file containing the large transaction.
+ Fixed an issue where a delay in InnoDB buffer pool resizing during Aurora serverless scaling operations could cause the database instance to become unresponsive and restart.
+ Fixed an issue in the out-of-memory (OOM) avoidance mechanism that could cause a database instance restart while attempting to recover memory under critical memory pressure.
+ Fixed an issue where a reader instance could restart repeatedly after being restarted while the writer instance was performing a forceful purge of undo logs.
+ Fixed an issue which can cause an unexpected database restart on reader instances when subqueries using Parallel Query requests were not correctly closed on completion.

**General improvements:**
+ Fixed commit ordering on binlog replicas with Enhanced Binlog enabled to correctly honor the `replica_preserve_commit_order` setting. This ordering behavior did not affect data integrity or cause conflicts between transactions, as it applied only to the sequencing of non-dependent transactions.
+ Fixed an issue which can cause query results to be returned in ascending order instead of the requested descending order. This occurs when using `ORDER BY DESC` with a range comparison and `LIMIT`.
+ Fixed an issue where the reader reports "ERROR 1146" (table not found) during certain online DDL operations on the writer when using INPLACE algorithm. This can occur when the reader has not previously opened the table before the DDL begins. It can also occur when the reader restarts or a new reader is created while the DDL is in progress.
+ Fixed an issue that can cause replication errors when processing binlog events larger than `aurora_in_memory_relaylog` fixed cache size (128MB).
+ Fixed an infrequent issue that could cause the database instance to restart when ongoing SQL statements read from temporary tables during buffer pool resize or page eviction operations.
+ Fixed performance issue where optimizer picks sub optimal query execution plan with Prepared Statements using IN and parameterized values.
+ Fixed a cluster availability issue that could occur during database server upgrades when DML operations on system tables referenced stale auto-increment values.
+ Fixed an issue that can cause queries using hash joins to return incorrect results when parallel query is enabled and the hash join memory requirement exceeds the limit.
+ Fixed an issue which can, in some cases, cause delayed instance availability during zero-downtime patching or zero-downtime restart operations.
+ Fixed issue which could cause engine restart when a spatial GIS query uses a Z-order spatial index on a column declared with an explicit SRID annotation.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.847.Patches"></a>

This version is based on MySQL 8.4.7. For more information, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/).