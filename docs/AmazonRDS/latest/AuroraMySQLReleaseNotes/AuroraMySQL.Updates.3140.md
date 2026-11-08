

# Aurora MySQL database engine updates 2026-10-26 (version 3.14.0, compatible with MySQL 8.0.46)
<a name="AuroraMySQL.Updates.3140"></a><a name="3140"></a><a name="3.14.0"></a>

**Version:** 3.14.0

Aurora MySQL 3.14.0 is now generally available and is compatible with MySQL 8.0.46. For more information about the community changes, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/) on the MySQL website.

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html).

For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html).

For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can upgrade from any currently supported Aurora MySQL version 2 cluster to an Aurora MySQL version 3.14.0 cluster in one of three ways: perform an in-place upgrade using [Zero Downtime Patching (ZDP)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html).

For information about planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For more information about upgrades, see [Upgrading Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, Support is available on the community forums and through [Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## New features
<a name="AuroraMySQL.Updates.3140.NewFeatures"></a>
+ Aurora MySQL minor version upgrades to this release from version 3.08 or higher now complete faster, allowing your writer instance to return to service sooner. No configuration changes or opt-in are required; the improvement is applied automatically.
+ Aurora MySQL introduces the hybrid key exchange groups `X25519MLKEM768` and `SecP256r1MLKEM768` alongside the classical elliptic-curve groups for TLS 1.3 connections. Clients that support post-quantum key exchange automatically negotiate a quantum-resistant shared secret; those that do not continue using classical groups. To verify which group a session negotiated, query the new `Aurora_ssl_named_group` status variable: `SHOW STATUS LIKE 'Aurora_ssl_named_group';`

## Improvements
<a name="AuroraMySQL.Updates.3140.Improvements"></a>

### Security fixes
<a name="AuroraMySQL.Updates.3140.SecurityFixes"></a>
+ Fixed an issue where the Advanced Audit log recorded an incorrect user and host for SQL statements executed inside a `SQL SECURITY DEFINER` routine (stored procedure, function, or trigger). These records showed the routine's definer user and host (for example, `'user'@'%'`) instead of the SQL client that invoked the routine. After this fix, the records show the user and host of the invoking SQL client.
+ Fixed an issue where queries run through prepared statements could generate duplicate entries in the advanced audit log.
+ Fixed an issue where `SET ROLE NONE` would not correctly clear the privileges of a previously active role in sessions using Write Forwarding, potentially allowing operations that should have been denied after role deactivation.

This release includes fixes for the following high severity CVEs. Each CVE ID links to its record on the CVE website:
+ [CVE-2026-60163](https://www.cve.org/CVERecord?id=CVE-2026-60163)
+ [CVE-2026-61094](https://www.cve.org/CVERecord?id=CVE-2026-61094)

This release includes fixes for the following medium severity CVEs. Each CVE ID links to its record on the CVE website:
+ [CVE-2026-21998](https://www.cve.org/CVERecord?id=CVE-2026-21998)
+ [CVE-2026-22002](https://www.cve.org/CVERecord?id=CVE-2026-22002)
+ [CVE-2026-22004](https://www.cve.org/CVERecord?id=CVE-2026-22004)
+ [CVE-2026-22005](https://www.cve.org/CVERecord?id=CVE-2026-22005)
+ [CVE-2026-22009](https://www.cve.org/CVERecord?id=CVE-2026-22009)
+ [CVE-2026-22015](https://www.cve.org/CVERecord?id=CVE-2026-22015)
+ [CVE-2026-22017](https://www.cve.org/CVERecord?id=CVE-2026-22017)
+ [CVE-2026-34267](https://www.cve.org/CVERecord?id=CVE-2026-34267)
+ [CVE-2026-34278](https://www.cve.org/CVERecord?id=CVE-2026-34278)
+ [CVE-2026-34293](https://www.cve.org/CVERecord?id=CVE-2026-34293)
+ [CVE-2026-34303](https://www.cve.org/CVERecord?id=CVE-2026-34303)
+ [CVE-2026-34304](https://www.cve.org/CVERecord?id=CVE-2026-34304)
+ [CVE-2026-34308](https://www.cve.org/CVERecord?id=CVE-2026-34308)
+ [CVE-2026-35236](https://www.cve.org/CVERecord?id=CVE-2026-35236)
+ [CVE-2026-35237](https://www.cve.org/CVERecord?id=CVE-2026-35237)
+ [CVE-2026-35238](https://www.cve.org/CVERecord?id=CVE-2026-35238)
+ [CVE-2026-35239](https://www.cve.org/CVERecord?id=CVE-2026-35239)
+ [CVE-2026-35240](https://www.cve.org/CVERecord?id=CVE-2026-35240)
+ [CVE-2026-60585](https://www.cve.org/CVERecord?id=CVE-2026-60585)
+ [CVE-2026-60332](https://www.cve.org/CVERecord?id=CVE-2026-60332)
+ [CVE-2026-60331](https://www.cve.org/CVERecord?id=CVE-2026-60331)
+ [CVE-2026-60747](https://www.cve.org/CVERecord?id=CVE-2026-60747)
+ [CVE-2026-47023](https://www.cve.org/CVERecord?id=CVE-2026-47023)
+ [CVE-2026-60186](https://www.cve.org/CVERecord?id=CVE-2026-60186)
+ [CVE-2026-60184](https://www.cve.org/CVERecord?id=CVE-2026-60184)
+ [CVE-2026-60185](https://www.cve.org/CVERecord?id=CVE-2026-60185)
+ [CVE-2026-60187](https://www.cve.org/CVERecord?id=CVE-2026-60187)
+ [CVE-2026-60188](https://www.cve.org/CVERecord?id=CVE-2026-60188)
+ [CVE-2026-60189](https://www.cve.org/CVERecord?id=CVE-2026-60189)
+ [CVE-2026-60191](https://www.cve.org/CVERecord?id=CVE-2026-60191)

This release includes fixes for the following low severity CVEs. Each CVE ID links to its record on the CVE website:
+ [CVE-2026-22001](https://www.cve.org/CVERecord?id=CVE-2026-22001)
+ [CVE-2026-60190](https://www.cve.org/CVERecord?id=CVE-2026-60190)

### Availability improvements
<a name="AuroraMySQL.Updates.3140.AvailabilityImprovements"></a>
+ Fixed an issue that could cause write forwarding on a reader DB instance to stop working, requiring a reboot of the reader to restore write forwarding. This could occur when a forwarded query was cancelled or timed out while using global write forwarding or local write forwarding.
+ Fixed an issue with improper handling of empty responses during connection loss with storage nodes.
+ Fixed an intermittent issue that could cause an Aurora reader instance to restart during an Aurora Global Database switchover, when the reader was sending replication-progress updates to the storage layer while its storage connections were being re-established.
+ Fixed an issue where a failed in-place `ALTER TABLE` requiring a table rebuild could restart the database instance if the secondary index build hit an error. An unreleased lock during cleanup triggered a restart instead of the `ALTER TABLE` simply failing. The lock is now released correctly, so the database instance remains available.

### General improvements
<a name="AuroraMySQL.Updates.3140.GeneralImprovements"></a>
+ Fixed an issue in Enhanced Binlog that reported incorrect binary log coordinates after a snapshot restore. Previously, this could result in an invalid binlog replication setup when Enhanced Binlog was running on the source cluster and some transactions were rolled back.
+ Optimized zero downtime patching (ZDP) by reducing the communication overhead between the database instance and the storage layer.
+ Fixed an issue where write forwarding throughput and latency metrics incorrectly reported 0 after a failover event on clusters with write forwarding enabled. These metrics now accurately reflect write forwarding activity following a failover: `ForwardingReplicaDMLLatency`, `ForwardingReplicaDMLThroughput`, `ForwardingReplicaSelectLatency`, and `ForwardingReplicaSelectThroughput`.
+ Fixed an issue with Aurora MySQL memory management where OOM response actions were not reliably disabled after an internal timeout period, if there was a concurrent change to `aurora_oom_response` DB parameter value.
+ Fixed an issue in the auto-increment recovery feature where auto-increment values for partitioned tables were not recovered correctly, which could lead to potential `DUPLICATE KEY` errors.
+ *New CloudWatch Metric: `AuroraTempTableVolumeTotalBytes`* — Aurora MySQL now publishes a new CloudWatch metric, `AuroraTempTableVolumeTotalBytes`, that reports the total cluster volume bytes used by both internal and external InnoDB temporary tablespaces on writer instances. This metric gives you real-time visibility into temporary tablespace storage consumption across all active sessions, enabling you to monitor growth trends, identify storage-heavy workloads, and set CloudWatch alarms before usage becomes critical. For more information, see [Amazon CloudWatch metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html), [external temporary tables](https://dev.mysql.com/doc/refman/8.4/en/create-temporary-table.html), and [internal temporary tables](https://dev.mysql.com/doc/refman/8.4/en/internal-temporary-tables.html).
+ Fixed an issue that can cause queries using hash joins to return incorrect results when parallel query is enabled and the memory required for a hash join exceeds the limit.
+ Fixed an issue that can cause a temporary spike in read I/O, DML latency, and query latency on reader instances after an online, non-rebuilding index DDL statement (such as `CREATE INDEX`, `DROP INDEX`, or `ALTER TABLE ... ALTER INDEX ... INVISIBLE`) is run on the writer instance.
+ Fixed an issue that can cause the `AuroraReplicaLag` metric to report values higher than the true replica lag on DB clusters that have enhanced binlog enabled and little to no write workload.
+ Fixed an issue where Performance Schema could not be disabled through the database instance parameter group while Performance Insights was enabled.
+ Fixed an issue which can cause a new value for the `table_open_cache` or `table_definition_cache` DB parameter to not be retained, reverting to the previous value.
+ Fixed an issue introduced in community MySQL 8.0.46 where the `CREATE TABLE` row-size estimate counted medium-length `VARCHAR` columns at their full declared size instead of capping them. On community MySQL 8.0.46, creating a table with many such columns fails with `ERROR 1118` ("Row size too large"), even though the same statement succeeded on earlier MySQL 8.0 releases. Aurora MySQL 3.14.0 retains the pre-8.0.46 behavior, so these statements continue to succeed as they did in Aurora MySQL 3.13.0 and earlier. For more information, see the following bugs on the MySQL Bugs website: [Bug\#120323](https://bugs.mysql.com/bug.php?id=120323), [Bug\#120356](https://bugs.mysql.com/bug.php?id=120356), and [Bug\#120370](https://bugs.mysql.com/bug.php?id=120370).
+ Added a new CloudWatch metric `FTSCacheMemoryUsed` that you can use to identify the total memory used by the InnoDB Full-Text Search (FTS) cache across all tables on a DB instance. For more information, see [Amazon CloudWatch metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*.
+ Added `RETURNING` clause support for single-table `DELETE` statements. You can now return values from deleted rows directly in the `DELETE` statement, eliminating the need for a separate `SELECT` query. Because `RETURNING` is now a reserved keyword, identifiers named `returning` must be quoted with backticks.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3140.Patches"></a>

This release includes all community bug fixes up to and including 8.0.46. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).
+ Bug\#38132549: If the server closed during transaction commit, transactions in an already committed state could remain in the undo log. If the transaction is already committed, it is cleared from `trx_sys->rw_trx_list` during recovery, but is not cleared from `active_rw_trxs` of the `trx_sys->shards`. This invalid transaction stored in the `trx_sys->shards` could cause errors or assertions in the execution of the later queries.