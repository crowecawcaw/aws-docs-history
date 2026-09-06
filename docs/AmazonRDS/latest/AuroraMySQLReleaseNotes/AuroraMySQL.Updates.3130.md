

# Aurora MySQL database engine updates 2026-08-27 (version 3.13.0, compatible with MySQL 8.0.45)
<a name="AuroraMySQL.Updates.3130"></a><a name="3130"></a><a name="3.13.0"></a>

**Version:** 3.13.0

Aurora MySQL 3.13.0 is now generally available and is compatible with MySQL 8.0.45. For more information about the community changes, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/) on the MySQL website.

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html).

For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html).

For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can upgrade from any currently supported Aurora MySQL version 2 cluster to an Aurora MySQL version 3.13.0 cluster in one of three ways: perform an in-place upgrade using [Zero Downtime Patching (ZDP)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html).

For information about planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general upgrade information, see [Upgrading Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, Support is available on the community forums and through [Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3130.Improvements"></a>

### Security fixes
<a name="AuroraMySQL.Updates.3130.SecurityFixes"></a>

This release includes fixes for the following high severity CVEs:
+ [CVE-2026-46863](https://www.cve.org/CVERecord?id=CVE-2026-46863)

This release includes fixes for the following medium severity CVEs:
+ [CVE-2026-21936](https://www.cve.org/CVERecord?id=CVE-2026-21936)
+ [CVE-2026-21937](https://www.cve.org/CVERecord?id=CVE-2026-21937)
+ [CVE-2026-21941](https://www.cve.org/CVERecord?id=CVE-2026-21941)
+ [CVE-2026-21948](https://www.cve.org/CVERecord?id=CVE-2026-21948)
+ [CVE-2026-21968](https://www.cve.org/CVERecord?id=CVE-2026-21968)

### Availability improvements
<a name="AuroraMySQL.Updates.3130.AvailabilityImprovements"></a>
+ Fixed an issue which can cause a database instance restart when executing `ALTER TABLE ... REORGANIZE PARTITION`, `DROP PARTITION`, or `ADD PARTITION` while concurrent operations (such as performance schema queries, full-text search optimization or statistics collection) are accessing the same table.
+ Fixed an issue which can cause a database instance restart when queries on `performance_schema.data_lock_waits` or `performance_schema.data_locks` run concurrently with `ALTER TABLE ... REORGANIZE PARTITION` on tables that have columns added using `ALGORITHM=INSTANT`.
+ Fixed an issue which can cause the writer instance to restart while processing an `ALTER TABLE ... REORGANIZE PARTITION` SQL statement that changes sub-partition order.
+ Fixed an issue where DDL operations on the writer instance could block or kill certain SQL statements on reader instances. Affected statements included write operations such as `UPDATE` or `TRUNCATE` on `performance_schema` tables, and write operations on temporary tables and `JOIN` operations.
+ Fixed an issue where the database writer instance could restart unexpectedly during a global database switchover operation while cleaning up temporary tables after SQL statement processing. This restart could result in longer switchover completion time.
+ Fixed an issue that could cause new database cluster creation to fail, requiring the cluster to be deleted and recreated.
+ Fixed an issue in the out-of-memory (OOM) avoidance mechanism that could cause a database instance restart while attempting to recover memory under critical memory pressure.
+ Fixed an issue which could cause the writer instance to repeatedly restart when the writer instance restarts while purging an undo record for a table with indexes on virtual columns.
+ Fixed an issue which could cause read replicas to restart when the writer instance commits a large transaction with binlog enabled. This issue could also cause errors when reading the binlog file containing the large transaction.
+ Fixed an issue where a delay in InnoDB buffer pool resizing during Aurora serverless scaling operations could cause the database instance to become unresponsive and restart.
+ Fixed an issue where a reader instance could restart repeatedly after being restarted while the writer instance was performing a forceful purge of undo logs.
+ Fixed an issue that could cause a writer DB instance to restart when a reader DB instance restarts while local or global write forwarding is enabled.
+ Fixed an issue which can cause an unexpected database restart on reader instances when subqueries utilizing Parallel Query requests were not correctly closed on completion.
+ Fixed an issue where a replica instance might restart when executing binary protocol prepared statements that are forwarded to the writer through write forwarding.
+ Fixed an issue which can cause the writer instance to restart due to an internal timing conflict during highly concurrent write operations.
+ Fixed an issue that could cause a database instance to restart when enhanced binlog is enabled.
+ Fixed a bug that could make the replica briefly disconnect and reconnect to the writer, causing a temporary spike in replication lag (`AuroraReplicaLag`).
+ Fixed an issue in the Aurora Storage Daemon that in rare cases could result in an unexpected database restart.
+ Improved the performance of Aurora physical replication by applying changes from the writer instance on reader instances using multiple threads.

### General improvements
<a name="AuroraMySQL.Updates.3130.GeneralImprovements"></a>
+ Fixed an issue where, with write forwarding enabled, a reader session with `aurora_replica_read_consistency` set to `global` could fail to read the latest committed changes.
+ Fixed an issue which could cause engine restart when a spatial GIS query uses a Z-order spatial index on a column declared with an explicit SRID annotation.
+ Fixed an issue where graceful reader disconnections could incorrectly increment `Aborted_clients` on the writer instance when write forwarding is enabled.
+ Fixed an infrequent issue that could cause the database instance to restart when ongoing SQL statements read from temporary tables during buffer pool resize or page eviction operations.
+ Fixed commit ordering on binlog replicas with Enhanced Binlog enabled to correctly honor the `replica_preserve_commit_order` setting. This ordering behavior did not affect data integrity or cause conflicts between transactions, as it applied only to the sequencing of non-dependent transactions.
+ Fixed an issue which can cause query results to be returned in ascending order instead of the requested descending order when using `ORDER BY DESC` with a range comparison and `LIMIT`.
+ Fixed a cluster availability issue that could occur during database server upgrades when DML operations on system tables referenced stale auto-increment values.
+ Fixed an issue which could cause replication errors when processing binlog events larger than the `aurora_in_memory_relaylog` fixed cache size (128 MB).
+ Fixed an issue where the reader reports `ERROR 1146` (table not found) during certain online DDL operations on the writer when using the `INPLACE` algorithm.
+ Fixed an issue which can cause delayed instance availability during zero-downtime patching (ZDP) or zero-downtime restart (ZDR) operations.
+ Fixed an issue where in some cases connection state is not preserved following a zero-downtime upgrade, which could result in unexpected behavior.
+ Fixed an issue where, during write forwarding, a reader instance restart could leave an orphan forwarding session on the writer instance, and killing that session could cause the writer to restart.

### Upgrades and migrations
<a name="AuroraMySQL.Updates.3130.UpgradesMigration"></a>
+ Fixed an issue that could cause database cluster clone operations to take an extended time to complete.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3130.Patches"></a>

This release includes all community bug fixes up to and including 8.0.45. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed a regression introduced in MySQL 8.0.42 where inserting into a partitioned table using a prepared statement or stored procedure could fail with `ERROR 1748` ("Found a row not matching the given partition set"). This occurred when the partition key column uses `DEFAULT CURRENT_TIMESTAMP`. Partition pruning at prepare time locked a partition based on the current timestamp, but on subsequent re-execution the timestamp could map to a different partition. Reference: MySQL upstream [Bug\#119784](https://bugs.mysql.com/bug.php?id=119784).