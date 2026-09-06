

# Aurora MySQL database engine updates 2025-05-14 (version 3.09.0, compatible with MySQL 8.0.40)
<a name="AuroraMySQL.Updates.3090"></a><a name="3.09.0"></a><a name="3.09.0"></a>

**Version:** 3.09.0

Aurora MySQL 3.09.0 is generally available. Aurora MySQL 3.09 versions are compatible with MySQL 8.0.40. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can perform an in-place upgrade that leverages a [zero-downtime-patch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.09.0 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the * Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Release highlights
<a name="AuroraMySQL.Updates.3090.Highlights"></a>
+ Enhanced Aurora MySQL global databases to allow secondary reader instances to complete startup and serve read requests during unplanned events (hardware failures, network disruptions). Previously, secondary reader instances could not restart during such events. For more information, see [Cross-Region resiliency for Global Database secondary clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-secondary-availability.html) in the *Amazon Aurora User Guide*.
+ Reduced writer downtime during Aurora MySQL Global Database cross-region switchovers to typically under one minute, minimizing downtime during planned regional switches.

## Improvements
<a name="AuroraMySQL.Updates.3090.Improvements"></a>

**Security fixes**

Critical CVEs:
+ [CVE-2024-11053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11053)
+ [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)

Medium CVEs:
+ [CVE-2024-7264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7264)
+ [CVE-2024-21193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21193)
+ [CVE-2024-21194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21194)
+ [CVE-2024-21196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21196)
+ [CVE-2024-21197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21197)
+ [CVE-2024-21198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21198)
+ [CVE-2024-21199](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21199)
+ [CVE-2024-21201](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21201)
+ [CVE-2024-21203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21203)
+ [CVE-2024-21207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21207)
+ [CVE-2024-21212](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21212)
+ [CVE-2024-21213](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21213)
+ [CVE-2024-21218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21218)
+ [CVE-2024-21219](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21219)
+ [CVE-2024-21230](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21230)
+ [CVE-2024-21236](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21236)
+ [CVE-2024-21238](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21238)
+ [CVE-2024-21239](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21239)
+ [CVE-2024-21241](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21241)
+ [CVE-2025-21494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21494)
+ [CVE-2025-21504](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21504)
+ [CVE-2025-21525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21525)
+ [CVE-2025-21534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21534)
+ [CVE-2025-21536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21536)

**Availability improvements:**
+ Fixed an issue where multi-statement queries forwarded from reader to writer instances could hang when `innodb_flush_log_at_trx_commit` is set to `0` on the writer and non-zero on the reader, preventing potential write forwarding failures.
+ Fixed a deadlock issue with Enhanced Binlog enabled that could cause database reboots when running `SHOW BINARY LOGS` concurrent with either committing transactions to [BLACKHOLE](https://dev.mysql.com/doc/refman/8.0/en/blackhole-storage-engine.html) engines or executing `XA PREPARE` statements, preventing potential stuck writes and instance availability issues.
+ Fixed race conditions in write forwarding that could cause Aurora writer instance restarts by preventing new requests from being accepted before previous requests are fully completed, improving the stability of write forwarding operations.
+ Fixed an issue on the replica where a network interruption may not correctly re-establish connection with the writer causing replication to be stuck and potential instance restarts.
+ Aurora MySQL Out of Memory (OOM) response now implements phased buffer pool resizing that gradually reduces memory usage based on system memory state (LOW/RESERVED) when enabled through `aurora_oom_response` DB parameter, providing better memory management during memory pressure situations.
+ Improved the Binlog file recovery time during database restarts by optimizing the recovery process to take constant time regardless of Binlog file size. Previously, in some cases, recovery time would be proportional to the size of the last Binlog file.
+ Fixed an issue that could cause unexpected MySQL server restarts when executing concurrent InnoDB table truncation operations while querying `performance_schema.data_lock_waits`.
+ Fixed an issue that can cause a database instance to restart when committing large binlog events during low storage conditions.
+ Fixed an issue where buffer pool resize operations triggered during Out of Memory (OOM) avoidance could become unresponsive during high-workload scenarios, leading to a possible database restart.
+ Fixed an issue that can cause a database restart loop when creating a trigger. The issue can also occur when a new Binlog or a Relaylog file is added or these files rotate.
+ Fixed an issue that could cause Aurora reader instance restarts when using write forwarding with multi-statement or implicit commit queries.

**General improvements:**
+ Fixed an issue where `ALTER TABLE ... REBUILD / OPTIMIZE TABLE` operations could consume excessive memory by allocating `innodb_ddl_buffer_size` bytes per DDL thread instead of dividing the buffer size among threads, preventing potential memory over utilization during DDL operations.
+ Changed the default value for `aurora_oom_response`, on all DB instance classes that have more than 4 GiB of memory, from print to print,decline,kill\_connect. For more information, see [Amazon Aurora MySQL out-of-memory issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting-workload.html#AuroraMySQLOOM) in the *Amazon Aurora User Guide*.
+ The following privileges have been added to the `rds_superuser_role`: `FLUSH_OPTIMIZER_COSTS`, `FLUSH_STATUS`, `FLUSH_TABLES`, `FLUSH_USER_RESOURCES`. For information about the `rds_superuser_role`, see the [Amazon Master User Accounts with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html) documentation. For more information on these dynamic privileges, please see the [MySQL](https://dev.mysql.com/doc/refman/8.0/en/flush.html) documentation.
+ Starting with this Aurora MySQL version, fast insert optimization is no longer enabled. For more information, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance) in the *Amazon Aurora User Guide*.
+ Fixed an issue with an incorrect breach of the `max_user_connections` threshold, resulting in connection errors for some users. This occurs in some edge cases, such as when connections are created and killed almost immediately.
+ Fixed an audit logging issue that caused high CPU utilization, leading to an unresponsive database server instance.
+ Fixed a memory management issue when using XA transactions, preventing possible instance restarts when Enhanced Binlog is enabled.
+ Fixed an issue where query performance would degrade when the optimizer made incorrect cost estimations due to the Bufferpool Index Statistics being updated incorrectly post database server restart.
+ Fixed an issue that prevented customers from turning off local write-forwarding functionality because of a stuck worker thread.
+ Fixed an issue that caused the `SHOW BINARY LOGS` command to take longer to execute on a cluster where Enhanced Binlog is enabled or was previously enabled. This issue could also cause increased commit latency if multiple `SHOW BINARY LOGS` commands were running concurrently.

**Upgrades and migrations:**
+ Fixed an issue where Zero Downtime Patching (ZDP) could be unsuccessful while attempting to preserve connection, belonging to a user which had been dropped. More information on the `DROP USER` command, and its affect on active connections can be found in the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/flush.html).

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3090.Patches"></a>

This release includes all community bug fixes up to and including 8.0.40. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).
+ While large transactions were being received and applied, and a request to stop the replication channel was made using `STOP REPLICA`, MySQL did not do so properly, and subsequently did not process any channel commands. In addition, the server shutdown process did not complete gracefully, and required either the MySQL process to be killed or the host system to be restarted. (Bug \#115966, Bug \#37008345)