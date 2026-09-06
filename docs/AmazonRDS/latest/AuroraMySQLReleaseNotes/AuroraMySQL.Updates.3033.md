

# Aurora MySQL database engine updates 2023-12-08 (version 3.03.3) (Deprecated)
<a name="AuroraMySQL.Updates.3033"></a><a name="3.03.3"></a><a name="3.03.3"></a>

 **Version:** 3.03.3 

 Aurora MySQL 3.03.3 is generally available. Aurora MySQL 3.03 versions are compatible with MySQL 8.0.26. For more information on community changes that have occurred from 8.0.23 to 8.0.28, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

 For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html). 

 Currently available Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, 3.04.\*, and 3.05.\*. 

 You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently available Aurora MySQL version 2 cluster into an Aurora MySQL version 3.03.3 cluster. 

 For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3033.Improvements"></a>

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes are below:
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)

 **Availability improvements:** 
+ Fixed an issue where Aurora MySQL database instances using parallel query may experience a database restart when running a high number of concurrent parallel queries.
+ Fixed an issue which can cause the executed GTID set to be recovered incorrectly on a binary log (binlog) replica cluster with enhanced binlog enabled when any binlog source has `gtid_mode` set to `ON` or `ON_PERMISSIVE`. This issue may cause the replica cluster's writer instance to restart an additional time during recovery, or lead to incorrect results when querying the executed GTID set.
+ Fixed a memory management issue that can cause an Aurora MySQL database instance restart or a failover due to a decrease in the freeable memory when enhanced binary log is enabled.
+ Fixed an issue which can cause the reader instance to restart when the writer instance grows the database volume to a multiple of 160GB.
+ Fixed an issue where an Aurora MySQL database instance with the enhanced binary log feature enabled might get stuck during the database instance startup as the binary log recovery process is being executed.
+ Fixed an issue during zero downtime patching which causes an instance restart that leads to the database connections being unexpectedly closed.
+ Fixed an issue which can cause a database instance restart due to a deadlatch when running [`SHOW STATUS`](https://dev.mysql.com/doc/refman/8.0/en/show-status.html) and [`PURGE BINARY LOGS`](https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html) statements concurrently. The purge binary logs is a managed statement that is executed to honor the user configured binlog retention period.
+ Fixed an issue which can cause a database instance restart due to a long semaphore wait when using the enhanced binlog feature on a cluster with an Aurora replica.

 **General improvements:** 
+ Removed unused storage metadata before writing to Aurora storage when the enhanced binlog feature is enabled. This avoids certain scenarios when a database restart or failover may occur because of increased write latency due to increased bytes transmitted over the network.
+ Fixed an issue which can cause the `NumBinaryLogFiles` metrics on CloudWatch to display incorrect results when enhanced binlog is enabled.
+ Fixed an issue which can cause the modification of the `table_open_cache` database parameter to not take effect until the database instance is restarted.
+ Fixed an issue which can cause a database restart when connected binary log (binlog) consumers are using duplicate binlog replication server IDs.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3033.Patches"></a>

This release includes all community bug fixes up to and including 8.0.26, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+  Fixed an issue which can cause higher CPU utilization due to background TLS certificate rotation (Community Bug Fix \#34284186) 