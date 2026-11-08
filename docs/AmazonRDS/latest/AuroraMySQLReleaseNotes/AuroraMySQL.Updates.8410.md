

# Aurora MySQL 8.4.10
<a name="AuroraMySQL.Updates.8410"></a><a name="8410"></a><a name="8.4.10"></a>

**Version:** 8.4.10

This release of Aurora MySQL is compatible with MySQL 8.4.10. For more information on the community changes that have occurred, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/) on the MySQL website.

For details of the new features in Aurora MySQL version 8.4, see [Aurora MySQL version 8.4 compatible with MySQL 8.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL84.html). For differences between Aurora MySQL version 8.4 and version 3, see [Comparison of Aurora MySQL version 3 and Aurora MySQL version 8.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v3-v84.html). For a comparison with MySQL 8.4 Community Edition, see [Comparison of Aurora MySQL version 8.4 and MySQL 8.4 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v84-community.html) in the *Amazon Aurora User Guide*.

You can perform an in-place major version upgrade, restore a snapshot with upgrade, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html). You can upgrade from any currently supported Aurora MySQL version 3 cluster to Aurora MySQL version 8.4.10.

For information on planning an upgrade to Aurora MySQL version 8.4, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For more information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

For more information about patch releases and how to apply them, see [About patch releases](AuroraMySQL.Updates.84Updates.md#AuroraMySQL.Updates.84Updates.PatchReleases).

**Topics**
+ [Aurora MySQL 8.4.10, October 26, 2026](#AuroraMySQL.Updates.8410.GA)

## Aurora MySQL 8.4.10, October 26, 2026
<a name="AuroraMySQL.Updates.8410.GA"></a>

### New features
<a name="AuroraMySQL.Updates.8410.NewFeatures"></a>
+ Aurora MySQL minor version upgrades to this release from version 8.4.7 or 8.4.8 now complete faster, allowing your writer instance to return to service sooner. No configuration changes or opt-in are required; the improvement is applied automatically.
+ Added support for tagged global transaction identifiers (GTIDs). This feature extends the GTID format to include a user-defined tag, so that transactions sharing the same source server UUID can be grouped and identified separately. A tagged GTID has the format UUID:TAG:NUMBER, where TAG is an alphanumeric label that you assign to a set of transactions. Use tagged GTIDs to distinguish transactions from different workloads or sources within complex replication topologies. For more information, see [Using GTID tags with an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-replication-gtid.tags.html) in the *Amazon Aurora User Guide*.

### Improvements
<a name="AuroraMySQL.Updates.8410.Improvements"></a>

Below are the improvements made compared to Aurora MySQL 8.4.8, see [Aurora MySQL 8.4.8 Release Notes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.848.html).

#### Availability improvements
<a name="AuroraMySQL.Updates.8410.AvailabilityImprovements"></a>
+ Fixed an issue with improper handling of empty responses during connection loss with storage nodes.

#### General improvements
<a name="AuroraMySQL.Updates.8410.GeneralImprovements"></a>
+ Added three new CloudWatch metrics `UndoTablespaceTruncationPagesRemaining`, `UndoTablespaceTruncationPoint`, `UndoTablespaceTruncationActiveTransactions` to help track writer instance undo tablespace truncation. Please see [Amazon CloudWatch metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) for additional details. Added a new global status variable `Aurora_undo_tablespace_truncation_pending_id`, that reports the ID of the undo tablespace currently pending truncation, or 0 when there is none. Please see [Aurora MySQL global status variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.GlobalStatusVars.html) for additional details.
+ Added new metrics `AuroraUndoTablespaceBytesUsed`, `AuroraUndoTablespaceUtilization` to help track writer instance undo usage. Please see the [Amazon CloudWatch metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) for additional details.
+ Fixed an issue where undo tablespace truncation could cause the `RollbackSegmentHistoryListLength` CloudWatch metric to report a value higher than the actual history list length.
+ Fixed an issue that can cause a temporary spike in read I/O, DML latency, and query latency on reader instances after an online, non-rebuilding index DDL statement (such as `CREATE INDEX`, `DROP INDEX`, or `ALTER TABLE ... ALTER INDEX ... INVISIBLE`) is run on the writer instance.
+ Fixed an issue where the engine rolls back an `XA PREPARE` transaction during recovery when binary log is enabled but the session variable `sql_log_bin` is set to `OFF`.
+ Improved Enhanced Binlog recovery time to sub-seconds for XA transactions.
+ Added a new CloudWatch metric, `FTSCacheMemoryUsed`, to allow users to identify the total memory used by the InnoDB Full-Text Search (FTS) cache across all tables on a DB instance. For more information, see [Amazon CloudWatch metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*.
+ Enabled support for higher `max_connections` limit, increased the highest allowed value from 16000 to 50000.
+ Added `RETURNING` clause support for single-table `DELETE` statements. You can now return values from deleted rows directly in the `DELETE` statement, eliminating the need for a separate `SELECT` query. Because `RETURNING` is now a reserved keyword, identifiers named `returning` must be quoted with backticks.

#### Upgrades and migrations
<a name="AuroraMySQL.Updates.8410.UpgradesMigration"></a>
+ Optimized minor version upgrade performance through parallel processing of Performance Schema updates, reducing upgrade duration when Performance Schema modifications are required.

### Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.8410.Patches"></a>

This version is based on MySQL 8.4.10. For more information, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/) on the MySQL website.
+ Bug\#38132549: If the server closed during transaction commit, transactions in an already committed state could remain in the undo log. If the transaction is already committed, it is cleared from `trx_sys->rw_trx_list` during recovery, but is not cleared from `active_rw_trxs` of the `trx_sys->shards`. This invalid transaction stored in the `trx_sys->shards` could cause errors or assertions in the execution of the later queries.