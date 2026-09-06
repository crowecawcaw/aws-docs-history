

# Aurora MySQL database engine updates 2026-02-17 (version 3.12.0, compatible with MySQL 8.0.44)
<a name="AuroraMySQL.Updates.3120"></a><a name="3.12.0"></a>

**Version:** 3.12.0

Aurora MySQL 3.12.0 is generally available. Aurora MySQL 3.12 versions are compatible with MySQL 8.0.44. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can perform an in-place upgrade [leveraging Zero Downtime Patching (ZDP)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.12.0 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3120.Improvements"></a>

**Security fixes**
+ Fixed an issue which can cause some SQL statements to not get logged in the audit log.
+ Fixed caching\_sha2\_password plugin to ensure Aurora MySQL reader and writer instances validate updated passwords consistently.

**Medium CVEs:**
+ [CVE-2025-53040](https://www.cve.org/CVERecord?id=CVE-2025-53040)
+ [CVE-2025-53042](https://www.cve.org/CVERecord?id=CVE-2025-53042)
+ [CVE-2025-53044](https://www.cve.org/CVERecord?id=CVE-2025-53044)
+ [CVE-2025-53045](https://www.cve.org/CVERecord?id=CVE-2025-53045)
+ [CVE-2025-53053](https://www.cve.org/CVERecord?id=CVE-2025-53053)
+ [CVE-2025-53054](https://www.cve.org/CVERecord?id=CVE-2025-53054)
+ [CVE-2025-53062](https://www.cve.org/CVERecord?id=CVE-2025-53062)
+ [CVE-2025-53069](https://www.cve.org/CVERecord?id=CVE-2025-53069)

**Availability improvements:**
+ Fixed an issue which can cause a database instance restart when the lock table is full during semi-consistent read.
+ Fixed an issue in binlog recovery that could cause binlog replica instance to restart when using `aurora_in_memory_relaylog` with multi-threaded replication.
+ Fixed an issue which could cause the writer instance to restart when global write forwarding or local write forwarding is being disabled.
+ Fixed an issue where excessively large thread\_stack configurations could prevent Aurora MySQL server bootup during restarts or upgrades. Aurora MySQL server now automatically resets thread\_stack to the engine default value(1 MB) when it exceeds system memory, preventing startup failures.
+ Fixed an issue which, could cause an engine restart when running `KILL` after running `EXPLAIN FOR CONNECTION` on a running parallel query.
+ Fixed issue that can force parallel query on a random query and causes engine restart if this query is forcibly terminated.
+ Fixed an issue which prevented users with CONNECTION\_ADMIN or SUPER privileges from performing an additional connection beyond max\_connections limit, as supported in MySQL Community Edition.
+ Fixed an issue that can cause a restart on a binary log (binlog) replica when processing a large number of relay log files during [relay log recovery](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-unexpected-replica-halt.html).
+ Fixed an issue that causes the writer DB instance to restart when running a parallel query on a reader DB instance.
+ Fixed an issue that, in rare conditions, can disable binary logging when an error occurs during commit of a large transaction.
+ Fixed an issue that can cause read replicas to restart in the event of certain rare transaction commit orders on the writer DB instance.
+ Fixed an issue that can lead to a database restart when [scheduled events](https://dev.mysql.com/doc/refman/8.4/en/events-overview.html) are aborted during execution on instances that have enhanced binlog enabled.
+ Fixed an issue where database instances using multi TiB storage sizes, may experience increased downtime during restart due to InnoDB bufferpool validation failures.

**General improvements:**
+ Excluded a community change introduced in MySQL 8.0.44 where failed connection attempts unexpectedly added rows to performance\_schema tables causing excessive memory consumption. Ref community [Bug\#119766](https://bugs.mysql.com/bug.php?id=119766)
+ Fixed an issue affecting Aurora specific replication stored procedures when configuring binlog replication on instances with custom collation settings.
+ Fixed an issue to reduce CPU overhead while establishing Encryption in Transit between the database engine and the storage layer.
+ Improved write IOPS performance when system variable innodb\_flush\_log\_at\_trx\_commit is set to 0.
+ Automatically disable aurora\_oom\_response actions (except print, if configured) when aurora\_oom\_response fails to resolve memory pressure after a threshold time (in the order of few mins).
+ Resolved a race condition that could cause incorrect page reads from the buffer pool during Aurora Serverless scale-down operations or during page eviction from the buffer pool. Ref community [Bug\#116305](https://bugs.mysql.com/bug.php?id=116305).
+ Fixed an out-of-memory (OOM) issue that could cause reader restarts when executing privilege-related commands on the writer.
+ The following privileges have been added to the `rds_superuser_role`: `FLUSH_OPTIMIZER_COSTS, FLUSH_STATUS, FLUSH_TABLES, FLUSH_USER_RESOURCES`. For information about the `rds_superuser_role`, please see the [Amazon Master User Accounts with Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html) documentation. For more information on these dynamic privileges, please see the [MySQL](https://dev.mysql.com/doc/refman/8.0/en/flush.html) documentation.
+ Fixed an issue causing inaccurate tracking of parallel query requests while running `EXPLAIN ANALYZE` statements where `Aurora_pq_request_in_progress` counter was not updated accurately.
+ Fixed an issue where a preserved connection is handled incorrectly during zero-downtime patching (ZDP)/zero-downtime restart (ZDR) which can lead to the client waiting indefinitely for a query to complete.
+ Fix the issue where the row becomes unreadable through the spatial index during an update.
+ Fixed an issue where a query containing an optimizer hint which was aborted during a zero-downtime restart (ZDR) or zero-downtime patching (ZDP) operation may be incorrectly handled.
+ Fix the issue where the commit latency is not measured when innodb\_flush\_log\_at\_trx\_commit is set to 0.
+ Introduced optimizations to reduce memory usage during logical [data dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary.html) recovery when there are a large number of tables.
+ Fixed an issue that caused the `SHOW BINARY LOGS` command to take longer to execute on a cluster where Enhanced Binlog is enabled or was previously enabled. This issue could also cause increased commit latency if multiple `SHOW BINARY LOGS` commands were running concurrently.
+ Fix the memory issue associated with the default roles of the view definer.
+ Fixed an issue that can cause failure in completing the process of disabling the "write forwarding" feature.
+ Fixed an issue which can cause a writer database instance to restart when a reader instance using write forwarding executes a DML statement that contains a timestamp value and the time\_zone database parameter is set to "UTC".
+ Fixed an issue, which in rare cases, caused intermittent unavailability of an Aurora Read Replica or table definition inconsistencies with error 'Table does not exist' on the replica due to concurrent read queries on the replica and DDL operations on the writer.
+ Fixed an issue which may cause an incomplete result set when executing queries involving LEFT- or RIGHT-JOIN operations using the hash-join algorithm with parallel query.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3120.Patches"></a>

This release includes all community bug fixes up to and including 8.0.44. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed an issue where a query of the form `SELECT 1 FROM t WHERE CAST(a AS UNSIGNED INTEGER) = 1 AND a = (SELECT 1 FROM t)` leads to an assertion failure in `item_func.cc`. (Community Bug Fix \#36128964)
+ Fixed an issue that resolves the deadlock when FLUSH STATUS, COM\_CHANGE\_USER and SHOW PROCESS LIST are executed concurrently. (Bug\#35218030)