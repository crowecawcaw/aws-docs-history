

# Aurora MySQL database engine updates 2024-11-18 (version 3.08.0, compatible with MySQL 8.0.39)
<a name="AuroraMySQL.Updates.3080"></a><a name="3.08.0"></a><a name="3.08.0"></a>

 **Version:** 3.08.0

Aurora MySQL 3.08.0 is generally available. Aurora MySQL 3.08 versions are compatible with MySQL 8.0.39. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/). 

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*. 

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.04.\*, 3.05.\*, 3.06.\*, 3.07.\*, and 3.08.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.08.0 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*. 

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## New features
<a name="AuroraMySQL.Updates.3080.New"></a>
+ Added three new Amazon CloudWatch metrics to allow users to monitor the InnoDB purge process:
  +  `PurgeBoundary` 
  +  `PurgeFinishedPoint` 
  +  `TruncateFinishedPoint` 

  For more information, see [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*. 
+ Added a new CloudWatch metric `TransactionAgeMaximum` to allow users to identify long-running transactions that might be holding back the purge boundary. For more information, see [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*. 
+ Added three new CloudWatch metrics for out-of-memory (OOM) avoidance:
  +  `AuroraMillisecondsSpentInOomRecovery` 
  +  `AuroraNumOomRecoverySuccessful` 
  +  `AuroraNumOomRecoveryTriggered` 

  For more information, see [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*. 
+ Changed three CloudWatch metrics for out-of-memory (OOM) avoidance from running totals to incremental counters:
  +  `AuroraMemoryNumDeclinedSqlTotal` 
  +  `AuroraMemoryNumKillConnTotal` 
  +  `AuroraMemoryNumKillQueryTotal` 

  For more information, see [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*. 
+ Added two global status variables to show the amount of memory used by [internal temporary tables](https://dev.mysql.com/doc/refman/8.0/en/internal-temporary-tables.html): `aurora_temptable_ram_allocation` and `aurora_temptable_max_ram_allocation`. These global status variables increase observability and help diagnose issues related to internal temporary table memory usage.

  For more information, see [Aurora MySQL global status variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html#AuroraMySQL.Reference.GlobalStatusVars) in the *Amazon Aurora User Guide*. 
+ Introduced the new system variable `aurora_optimizer_trace_print_before_purge` to print [optimizer traces](https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_OPT_TRACE.html) to the error log before the server purges the traces from memory. A purge can be triggered based on the thresholds set by the system variables [optimizer\_trace\_offset](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_optimizer_trace_offset) and [optimizer\_trace\_limit](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_optimizer_trace_limit). 
+ Added support for the following DB instance classes:
  + db.r7i
  + db.r8g

  For more information, see [Supported DB engines for DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.SupportAurora.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3080.Improvements"></a>

 **Fixed security issues and CVEs:** 
+ Introduced a new user for binary log (binlog) replication, `rdsrepladmin_priv_checks_user`. For more information, see [Privilege checks user for binary log replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html#AuroraMySQL.privilege-model.binlog) in the *Amazon Aurora User Guide*. 
+ Fixed an issue where input parameters to [Aurora MySQL stored procedures](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.StoredProcs.html) might be handled incorrectly.

This release includes all community CVE fixes up to and including MySQL 8.0.39. The following CVE fixes are included:
+  [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487) 
+  [CVE-2024-0853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0853) 
+  [CVE-2024-20996](https://nvd.nist.gov/vuln/detail/CVE-2024-20996) 
+  [CVE-2024-21000](https://nvd.nist.gov/vuln/detail/CVE-2024-21000) 
+  [CVE-2024-21013](https://nvd.nist.gov/vuln/detail/CVE-2024-21013) 
+  [CVE-2024-21125](https://nvd.nist.gov/vuln/detail/CVE-2024-21125) 
+  [CVE-2024-21127](https://nvd.nist.gov/vuln/detail/CVE-2024-21127) 
+  [CVE-2024-21129](https://nvd.nist.gov/vuln/detail/CVE-2024-21129) 
+  [CVE-2024-21130](https://nvd.nist.gov/vuln/detail/CVE-2024-21130) 
+  [CVE-2024-21134](https://nvd.nist.gov/vuln/detail/CVE-2024-21134) 
+  [CVE-2024-21135](https://nvd.nist.gov/vuln/detail/CVE-2024-21135) 
+  [CVE-2024-21137](https://nvd.nist.gov/vuln/detail/CVE-2024-21137) 
+  [CVE-2024-21142](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21142) 
+  [CVE-2024-21157](https://nvd.nist.gov/vuln/detail/CVE-2024-21157) 
+  [CVE-2024-21159](https://nvd.nist.gov/vuln/detail/CVE-2024-21159) 
+  [CVE-2024-21160](https://nvd.nist.gov/vuln/detail/CVE-2024-21160) 
+  [CVE-2024-21162](https://nvd.nist.gov/vuln/detail/CVE-2024-21162) 
+  [CVE-2024-21163](https://nvd.nist.gov/vuln/detail/CVE-2024-21163) 
+  [CVE-2024-21165](https://nvd.nist.gov/vuln/detail/CVE-2024-21165) 
+  [CVE-2024-21166](https://nvd.nist.gov/vuln/detail/CVE-2024-21166) 
+  [CVE-2024-21173](https://nvd.nist.gov/vuln/detail/CVE-2024-21173) 
+  [CVE-2024-21177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21177) 
+  [CVE-2024-21179](https://nvd.nist.gov/vuln/detail/CVE-2024-21179) 
+  [CVE-2024-21185](https://nvd.nist.gov/vuln/detail/CVE-2024-21185) 
+  [CVE-2024-25062](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25062) 
+  [CVE-2024-37371](https://nvd.nist.gov/vuln/detail/cve-2024-37371) 
+  [CVE-2025-21492](https://nvd.nist.gov/vuln/detail/CVE-2025-21492) 

 **Availability improvements:** 
+ Fixed a defect that can cause the server to restart unexpectedly after running Data Manipulation Language (DML) commands on a table that already has instantly dropped columns, such that the count of dropped and nondropped columns is greater than 1017.
+ Fixed an issue that can lead to database log files not being rotated correctly, resulting in increased [local storage space usage](https://aws.amazon.com/blogs/database/understanding-amazon-aurora-mysql-storage-space-utilization) on a DB instance.
+ Fixed an issue that could cause the DB instance to stop closing connections under low-memory conditions when [aurora\_oom\_response](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting-workload.html#AuroraMySQLOOM) is enabled, leading to an out-of-memory reboot that could otherwise be avoided.
+ Fixed an issue that can cause a reader DB instance to restart when freeing memory used for log application.
+ Fixed an issue in computing internal metrics for full-text search (FTS) indexes that can cause database restarts.
+ Fixed a community issue that can sometimes produce incorrect query results when a `LIMIT` clause is used in subqueries along with index condition pushdown.
+ Fixed an issue that caused a memory access violation leading to releasing a mutex object no longer owned by the thread.
+ Fixed an issue that can cause a restart on a binary log (binlog) replica when processing a large number of relay log files during [relay log recovery](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-unexpected-replica-halt.html). 
+ Fixed an issue that can cause an Aurora reader DB instance to restart when write forwarding is enabled.
+ Fixed an issue where a query containing multiple `UNION` clauses could allocate a large amount of memory, leading to a DB instance restart.
+ Fixed an issue that causes the writer DB instance to restart when running a parallel query on a reader DB instance.
+ Fixed an issue where binlog replication would stall on the replica due to a deadlock encountered on the replica's I/O thread when the `FLUSH RELAY LOGS` command was run.
+ Fixed an issue that causes a DB instance restart when handling large GTID sets on a DB cluster with enhanced binlog enabled.
+ Fixed an issue that can cause a restart on a binlog replica when the in-memory relay log cache is enabled. The in-memory relay log cache is enabled on Aurora MySQL managed binlog replicas when using either single-threaded binary log replication, or multithreaded replication with [GTID auto-positioning](https://dev.mysql.com/doc/refman/8.0/en/replication-gtids-auto-positioning.html) enabled.
+ Fixed an issue that can cause a binlog replica instance to restart when applying Data Control Language (DCL) statements during database engine startup.
+ Fixed an issue that, in rare conditions, can cause a reader DB instance to restart due to a deadlatch when running `SELECT` queries on tables being updated by its writer DB instance.
+ Fixed an issue that can cause an Aurora Global Database reader instance to restart with an active write forwarding session.
+ Fixed an issue that can cause Aurora read replicas to restart in the event of certain rare transaction commit orders on the writer DB instance.
+ Fixed an issue that can cause a database to restart when [scheduled events](https://dev.mysql.com/doc/refman/8.0/en/events-overview.html) are canceled while running on DB instances that have enhanced binlog enabled.

 **General improvements:** 
+ Fixed an issue where a client connection can become stuck during zero-downtime patching (ZDP) or zero-downtime restart (ZDR).
+ Fixed an issue that, in rare cases, cause a database instance restart due to a memory management issue that can occur while handling an open table failure.
+ Fixed an issue that can cause SQL statements to experience unexpected primary key violation errors or warnings on some rows when performing concurrent `INSERT` statements on a table that has an `AUTO_INCREMENT` primary key column and a unique key column, and when an `INSERT` statement has unique key violations on different rows.
+ The Performance Schema instrument `memory/sql/sp_head::main_mem_root` is now a controlled instrument. Consequently, memory allocated for parsing and representation of stored programs now contributes toward per-connection memory limits.
+ Fixed an issue where a row becomes unreadable through the spatial index during an update.
+  Fixed an issue that prevented users from disabling local write forwarding.
+ Fixed an issue where a `SELECT COUNT` query can return the wrong result while using write forwarding.
+ Fixed an issue that can lead to incorrect query results when ZDP incorrectly restores session variables set as hints in queries.
+ Fixed an issue with automatic truncation of undo tablespaces when they're larger than the threshold [innodb\_max\_undo\_log\_size](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_max_undo_log_size) in upgrade scenarios.
+ Fixed an issue where the commit latency and commit throughput aren't measured when `innodb_flush_log_at_trx_commit` is set to `0`. 
+ Fixed an issue that can cause Aurora replica lag to be reported incorrectly .
+ Fixed an issue that provided an incorrect value for the `threads_running` variable when using Aurora Global Database.
+ Fixed an issue where an Aurora MySQL binlog replica with [parallel secondary index optimization](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.html#binlog-optimization) enabled would experience a restart when applying replication changes on tables with foreign keys.
+ Fixed a restart issue caused by prolonged resizing of the lock hash table during scaling up or scaling down events.
+ Fixed an issue that can cause a DB instance restart after disabling binary logging, when enhanced binlog was previously enabled.
+ Introduced optimizations to reduce memory usage during logical [data dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary.html) recovery when there is a large number of tables.
+ Fixed an issue where a user might experience an `ERROR 1377 (HY000): Fatal error during log purge` error while running the [mysql.rds\_set\_external\_source](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html#mysql_rds_set_external_source) stored procedure on a binlog replica, when binary log replication is already configured.
+ Fixed a defect that prevented the persistence of user role privileges after [ZDR](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.Availability.html). 
+ Fixed a memory issue associated with the default roles of the view definer.
+ Fixed an issue that can cause a DB instance to restart when `SHOW VOLUME STATUS` is run.
+ Fixed a restart issue caused by prolonged buffer pool resizing during scaling up or scaling down events.
+ Fixed a restart issue caused by logical read ahead (LRA) accessing freed pages due to buffer resizing during a scaling down event.
+ Fixed an issue that addresses `SELECT` queries returning incorrect results when the query uses `LEFT OUTER JOIN` with [semijoin transformation](https://dev.mysql.com/doc/refman/8.0/en/semijoins.html) that uses materialization as a strategy.
+ Fixed an issue that can cause failure in completing the process of disabling write forwarding.
+ Fixed an issue where the `ActiveTransactions` and `BlockedTransactions` CloudWatch metrics were reporting lower values than expected.
+ Fixed an issue where binlog replication breaks when the replica processes a multitable `DELETE` statement that explicitly deletes from both a parent and a child table.
+ Fixed an issue that can lead to a DB instance restart when processing a trigger with user-defined functions that return an `enum` type.
+ Fixed an issue where the `DMLLatency` CloudWatch metric would show incorrect values for a binary log replica instance when replicating using `binlog_format` set to `row`. 
+ Fixed an issue where slow `INSERT`, `DELETE`, and `UPDATE` queries run by the MySQL [Event Scheduler](https://dev.mysql.com/doc/refman/8.0/en/event-scheduler.html) weren't recorded in the slow query log unless preceded by a slow `SELECT` query.
+  Fixed an issue that, in rare cases, caused either intermittent unavailability of an Aurora read replica or table definition inconsistencies, sometimes with the error `Table does not exist`, on the replica. This is due to concurrent read queries on the replica and Data Definition Language (DDL) operations on the writer DB instance.
+ Fixed an issue that caused the `SHOW BINARY LOGS` command to take longer to run on a DB cluster where enhanced binlog is enabled or was previously enabled. This issue could also cause increased commit latency if multiple `SHOW BINARY LOGS` commands were running concurrently.

 **Upgrades and migrations:** 
+ Improved the performance of major version upgrade from Aurora MySQL version 2 to version 3 for DB clusters with large numbers of database objects (such as tables, triggers, and routines).

  For larger DB instance classes, the database upgrade process upgrades traditional MySQL object metadata to the new, atomic MySQL 8.0 data dictionary in parallel using multiple threads.
+ Fixed an issue that causes upgrades or migrations to fail when the target Aurora MySQL DB engine version is 3.04.0 or higher. This occurs when the `lower_case_table_names` DB cluster parameter is set to `1`, and MySQL database collation is incompatible with lowercase table names.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3080.Patches"></a>

This release includes all community bug fixes up to and including 8.0.39, in addition to the following. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3). 
+ Fixed an issue that caused `NULL` values to be incorrectly omitted from the result set for certain queries that have both `JOIN` and `UNION` operations. (Community Bug Fix \#114301)