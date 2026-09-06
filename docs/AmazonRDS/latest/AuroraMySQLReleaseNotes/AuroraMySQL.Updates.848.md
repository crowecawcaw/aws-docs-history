# Aurora MySQL 8.4.8, September 3, 2026

**Version:** 8.4.8

This release of Aurora MySQL is compatible with MySQL 8.4.8. For more information on the community changes that have occurred, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.4/en/") on the MySQL website.

For details of the new features in Aurora MySQL version 8.4, see [Aurora MySQL version 8.4 compatible with MySQL 8.4](../AuroraUserGuide/AuroraMySQL.MySQL84.md "../AuroraUserGuide/AuroraMySQL.MySQL84.md"). For differences between Aurora MySQL version 8.4 and version 3, see [Comparison of Aurora MySQL version 3 and Aurora MySQL version 8.4](../AuroraUserGuide/AuroraMySQL.Compare-v3-v84.md "../AuroraUserGuide/AuroraMySQL.Compare-v3-v84.md"). For a comparison with MySQL 8.4 Community Edition, see [Comparison of Aurora MySQL version 8.4 and MySQL 8.4 Community Edition](../AuroraUserGuide/AuroraMySQL.Compare-v84-community.md "../AuroraUserGuide/AuroraMySQL.Compare-v84-community.md") in the _Amazon Aurora User Guide_.

You can perform an in-place major version upgrade, restore a snapshot with upgrade, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md"). You can upgrade from any currently supported Aurora MySQL version 3 cluster to Aurora MySQL version 8.4.8.

For information on planning an upgrade to Aurora MySQL version 8.4, see [Planning a major version upgrade for an Aurora MySQL cluster](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning"). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Troubleshooting "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Troubleshooting") in the _Amazon Aurora User Guide_.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see [Maintaining an Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## New features

- Added support for multi-source binary log (binlog) replication. This feature enables an Aurora MySQL DB cluster to replicate data from multiple MySQL-compatible source databases at the same time. Each source connection is managed through a dedicated replication channel with its own receiver thread, applier threads, and relay log. You can configure and manage channels using new per-channel stored procedures. For more information, see [Using multi-source replication with Aurora MySQL](../AuroraUserGuide/AuroraMySQL.Replication.MultiSource.md "../AuroraUserGuide/AuroraMySQL.Replication.MultiSource.md") in the _Amazon Aurora User Guide_.
- Added support for delayed binary log (binlog) replication, where an Aurora MySQL DB cluster acting as a binlog replica can be configured to wait a specified number of seconds before applying transactions received from the source. Delayed replication can be used to protect against accidental data modifications such as unintended `DROP TABLE` or `DELETE` statements, giving you a recovery window to identify and correct errors before they propagate to the replica. For more information, see [Configuring the replication delay interval](../AuroraUserGuide/AuroraMySQL.Replication.Delayed.md "../AuroraUserGuide/AuroraMySQL.Replication.Delayed.md") in the _Amazon Aurora User Guide_.
- Introduced the `aurora_transaction_timeout` parameter. This parameter sets the maximum duration, in seconds, for an InnoDB transaction. You can use this parameter to help prevent long-running transactions (active or idle) from blocking InnoDB purge, which can lead to performance issues. For more information, see [Aurora MySQL transaction timeout](../AuroraUserGuide/AuroraMySQL.TransactionTimeout.md "../AuroraUserGuide/AuroraMySQL.TransactionTimeout.md") in the _Amazon Aurora User Guide_.
- Added support for post-quantum hybrid key exchange (X25519MLKEM768 and SecP256r1MLKEM768) for TLS 1.3 connections. Clients that support post-quantum key exchange negotiate a quantum-resistant shared secret automatically. To confirm which group the current session negotiated, query the `Ssl_named_group` status variable. For example: `SHOW STATUS LIKE 'Ssl_named_group';`.

## Improvements

Below are the improvements made compared to Aurora MySQL 8.4.7, see [Aurora MySQL 8.4.7 Release Notes](AuroraMySQL.Updates.847.md "AuroraMySQL.Updates.847.md").

### Security fixes

- Fixed an issue where the Advanced Audit log recorded an incorrect user and host for SQL statements executed inside a SQL SECURITY DEFINER routine (stored procedure, function, or trigger). These records showed the routine's definer user and host (for example, `'user'@'%'`) instead of the SQL client that invoked the routine. After this fix, the records show the user and host of the invoking SQL client.
- Fixed an issue where queries run through prepared statements could generate duplicate entries in the Advanced Audit log.
- Fixed an issue where `SET ROLE NONE` would not correctly clear the privileges of a previously active role in sessions using write forwarding, which could allow operations that should have been denied after role deactivation.

This release includes fixes for the following high severity CVEs:

- [CVE-2026-46863](https://www.cve.org/CVERecord?id=CVE-2026-46863 "https://www.cve.org/CVERecord?id=CVE-2026-46863")
- [CVE-2026-60163](https://www.cve.org/CVERecord?id=CVE-2026-60163 "https://www.cve.org/CVERecord?id=CVE-2026-60163")
- [CVE-2026-61094](https://www.cve.org/CVERecord?id=CVE-2026-61094 "https://www.cve.org/CVERecord?id=CVE-2026-61094")

This release includes fixes for the following medium severity CVEs:

- [CVE-2026-21936](https://www.cve.org/CVERecord?id=CVE-2026-21936 "https://www.cve.org/CVERecord?id=CVE-2026-21936")
- [CVE-2026-21937](https://www.cve.org/CVERecord?id=CVE-2026-21937 "https://www.cve.org/CVERecord?id=CVE-2026-21937")
- [CVE-2026-21941](https://www.cve.org/CVERecord?id=CVE-2026-21941 "https://www.cve.org/CVERecord?id=CVE-2026-21941")
- [CVE-2026-21948](https://www.cve.org/CVERecord?id=CVE-2026-21948 "https://www.cve.org/CVERecord?id=CVE-2026-21948")
- [CVE-2026-21968](https://www.cve.org/CVERecord?id=CVE-2026-21968 "https://www.cve.org/CVERecord?id=CVE-2026-21968")
- [CVE-2026-60585](https://www.cve.org/CVERecord?id=CVE-2026-60585 "https://www.cve.org/CVERecord?id=CVE-2026-60585")
- [CVE-2026-60332](https://www.cve.org/CVERecord?id=CVE-2026-60332 "https://www.cve.org/CVERecord?id=CVE-2026-60332")
- [CVE-2026-60331](https://www.cve.org/CVERecord?id=CVE-2026-60331 "https://www.cve.org/CVERecord?id=CVE-2026-60331")
- [CVE-2026-60747](https://www.cve.org/CVERecord?id=CVE-2026-60747 "https://www.cve.org/CVERecord?id=CVE-2026-60747")
- [CVE-2026-47023](https://www.cve.org/CVERecord?id=CVE-2026-47023 "https://www.cve.org/CVERecord?id=CVE-2026-47023")
- [CVE-2026-60186](https://www.cve.org/CVERecord?id=CVE-2026-60186 "https://www.cve.org/CVERecord?id=CVE-2026-60186")
- [CVE-2026-60184](https://www.cve.org/CVERecord?id=CVE-2026-60184 "https://www.cve.org/CVERecord?id=CVE-2026-60184")
- [CVE-2026-60185](https://www.cve.org/CVERecord?id=CVE-2026-60185 "https://www.cve.org/CVERecord?id=CVE-2026-60185")
- [CVE-2026-60187](https://www.cve.org/CVERecord?id=CVE-2026-60187 "https://www.cve.org/CVERecord?id=CVE-2026-60187")
- [CVE-2026-60188](https://www.cve.org/CVERecord?id=CVE-2026-60188 "https://www.cve.org/CVERecord?id=CVE-2026-60188")
- [CVE-2026-60189](https://www.cve.org/CVERecord?id=CVE-2026-60189 "https://www.cve.org/CVERecord?id=CVE-2026-60189")
- [CVE-2026-60191](https://www.cve.org/CVERecord?id=CVE-2026-60191 "https://www.cve.org/CVERecord?id=CVE-2026-60191")

This release includes fixes for the following low severity CVEs:

- [CVE-2026-60190](https://www.cve.org/CVERecord?id=CVE-2026-60190 "https://www.cve.org/CVERecord?id=CVE-2026-60190")

### Availability improvements

- Fixed an issue which can cause a database instance restart when executing `ALTER TABLE ... REORGANIZE PARTITION`, `DROP PARTITION`, or `ADD PARTITION` while concurrent operations (such as performance schema queries, full-text search optimization, or statistics collection) are accessing the same table.
- Fixed an issue which can cause a database instance restart when queries on `performance_schema.data_lock_waits` or `performance_schema.data_locks` run concurrently with `ALTER TABLE ... REORGANIZE PARTITION` on tables that have columns added using `ALGORITHM=INSTANT`.
- Fixed an issue which can cause the writer instance to restart while processing an `ALTER TABLE ... REORGANIZE PARTITION` SQL statement that changes sub-partition order.
- Fixed an issue where DDL operations on the writer instance could block or kill certain SQL statements on reader instances. Affected statements included write operations such as `UPDATE` or `TRUNCATE` on `performance_schema` tables, and write operations on temporary tables and `JOIN` operations.
- Fixed an issue where the database writer instance could restart unexpectedly during a global database switchover operation while cleaning up temporary tables after SQL statement processing. This restart could result in longer switchover completion time.
- Fixed an issue that could cause write forwarding on a reader DB instance to stop working, requiring a reboot of the reader to restore write forwarding. This could occur when a forwarded query was cancelled or timed out while using global write forwarding or local write forwarding.
- Fixed an issue where a delay in critical data structure resizing during Aurora serverless scaling operations could cause RDS health monitoring to restart the database instance.
- Fixed an issue which can cause the writer instance to restart due to an internal timing conflict during highly concurrent write operations.
- Fixed an issue that could cause a database instance to restart when enhanced binlog is enabled.
- Fixed a bug that could make the replica briefly disconnect and reconnect to the writer, causing a temporary spike in replication lag (`AuroraReplicaLag`).
- Fixed an issue in the Aurora Storage Daemon that in rare cases could result in an unexpected database restart.

### General improvements

- Fixed an issue where, with write forwarding enabled, a reader session with `aurora_replica_read_consistency` set to `global` could fail to read the latest committed changes.
- Fixed an issue which could cause engine restart when a spatial GIS query uses a Z-order spatial index on a column declared with an explicit SRID annotation.
- Fixed an issue where graceful reader disconnections could incorrectly increment `Aborted_clients` on the writer instance when write forwarding is enabled.
- Fixed an issue where in some cases connection state is not preserved following a zero-downtime upgrade, which could result in unexpected behavior.
- Fixed an issue where, during write forwarding, a reader instance restart could leave an orphan forwarding session on the writer instance, and killing that session could cause the writer to restart.
- Reduced the downtime during zero-downtime patching (ZDP) by optimizing the communication between the database instance and the storage layer after patching.
- Fixed an issue with Aurora MySQL memory management where out-of-memory (OOM) response actions were not reliably disabled after an internal timeout period, if there was a concurrent change to the `aurora_oom_response` DB parameter value.
- Fixed an issue in Enhanced Binlog that reported incorrect binary log coordinates after a snapshot restore. Previously, this could result in an invalid binlog replication setup when Enhanced Binlog was running on the source cluster and some transactions were rolled back.
- Fixed an issue in the auto-increment recovery feature where auto-increment values for partitioned tables were not recovered correctly, which could lead to potential DUPLICATE KEY errors.
- Added a new CloudWatch metric, `AuroraTempTableVolumeTotalBytes`, that reports the total cluster volume bytes used by both internal and external InnoDB temporary tablespaces on writer instances. This metric reports temporary tablespace storage consumption across all active sessions. You can use it to monitor growth trends, identify storage-heavy workloads, and set CloudWatch alarms. For more information about this metric, see [Amazon CloudWatch metrics for Amazon Aurora](../AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.md "../AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.md") in the _Amazon Aurora User Guide_. For more information about temporary tables, see [external temporary tables](https://dev.mysql.com/doc/refman/8.4/en/create-temporary-table.html "https://dev.mysql.com/doc/refman/8.4/en/create-temporary-table.html") and [internal temporary tables](https://dev.mysql.com/doc/refman/8.4/en/internal-temporary-tables.html "https://dev.mysql.com/doc/refman/8.4/en/internal-temporary-tables.html") on the MySQL website.
- Fixed an issue where write forwarding throughput and latency metrics incorrectly reported 0 after a failover event on clusters with write forwarding enabled. These metrics now accurately reflect write forwarding activity following a failover: `ForwardingReplicaDMLLatency`, `ForwardingReplicaDMLThroughput`, `ForwardingReplicaSelectLatency`, and `ForwardingReplicaSelectThroughput`.
- Fixed a performance issue where the optimizer picks a suboptimal query execution plan with prepared statements using `IN` and parameterized values.
- Fixed an issue that can cause queries using hash joins to return incorrect results when parallel query is enabled and the memory required for a hash join exceeds the limit.

### Upgrades and migrations

- Fixed an issue that could cause database cluster clone operations to take an extended time to complete.

## Integration of MySQL Community Edition bug fixes

This version is based on MySQL 8.4.8. For more information, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.4/en/") on the MySQL website.

- Fixed a regression introduced in MySQL 8.0.42 where inserting into a partitioned table using a prepared statement or stored procedure could fail with `ERROR 1748` ("Found a row not matching the given partition set"). This occurred when the partition key column uses `DEFAULT CURRENT_TIMESTAMP`. Partition pruning at prepare time locked a partition based on the current timestamp, but on subsequent re-execution the timestamp could map to a different partition. For more information about this fix, see MySQL upstream [Bug#119784](https://bugs.mysql.com/bug.php?id=119784 "https://bugs.mysql.com/bug.php?id=119784") on the MySQL Bugs website.
