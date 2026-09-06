

# Aurora MySQL database engine updates 2023-05-11 (version 3.03.1) (Deprecated)
<a name="AuroraMySQL.Updates.3031"></a><a name="3.03.1"></a><a name="3.03.1"></a>

 **Version:** 3.03.1 

 Aurora MySQL 3.03.1 is generally available. Aurora MySQL 3.03 versions are compatible with MySQL 8.0.26, and Aurora MySQL 3.02 versions are compatible with MySQL 8.0.23. For more information on community changes that have occurred from 8.0.23 to 8.0.26, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

 For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html). 

 Currently supported Aurora MySQL releases are 2.07.9, 2.11.1, 2.11.2, 3.01.\*, 3.02.\* and 3.03.\*. 

You can perform an in-place upgrade or restore a snapshot from any currently supported Aurora MySQL version 2 cluster into Aurora MySQL 3.03.1.

 For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3031.Improvements"></a>

 **New features:** 
+ Aurora Optimized I/O storage configuration is available starting from version 3.03.1. For more information, see [Storage configurations for Amazon Aurora DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html#aurora-storage-type). 
+ Added a new system variable, `innodb_aurora_max_partitions_for_range`. In some cases where persisted stats are not available, this parameter can be used to improve the execution time of row count estimations on partitioned tables. More information can be found in the documentation, [Aurora MySQL configuration parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html). 

**Availability improvements:**
+ Fixed an issue which can cause the database instance to restart due to incorrectly accessing invalid memory when a connection is closed immediately after committing a transaction.
+ Fixed an issue with Aurora Advanced Auditing that causes excess logging of informational messages to the Aurora MySQL error log when the server variable `server_audit_events` is set to ALL or QUERY. This issue may cause a database instance restart.
+ Fixed an issue which, in certain situations, can cause Aurora reader instances to restart when attempting to read a page which is no longer accessible during a range estimation. 
+ Fixed an issue which can cause an Aurora MySQL reader instance to restart while executing a query which utilizes an Aurora parallel query execution plan.
+ Fixed an issue where database instances using binary log replication may experience an increase in CPU utilization and connection failures when multiple binary log replication consumers are attached.
+ Fixed an issue where unsupported index scan access methods were considered for common table expressions (CTE) while materializing intermediate temporary tables, which can lead to undesired behavior including database restarts or incorrect query results. We fix this issue by avoiding the use of such unsupported index scan access methods on tables using the TempTable storage engine.
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

 **General improvements:** 
+ Fixed an issue which can cause higher than expected execution times for the SHOW BINARY LOGS statement. This could lead to a drop in commit throughput of the database.
+ Fixed an issue which can cause parallel export for user tables that have columns added using the Instant ADD COLUMN functionality to fail.
+ Fixed an issue where events that were reported while processing audit log rotations might not be written to the audit log.
+ Fixed an issue which may cause depletion of available memory when executing queries against the INFORMATION\_SCHEMA INNODB\_TABLESPACES table.
+ Fixed an issue which incorrectly allows customers to set ROW\_FORMAT as COMPRESSED when creating partitioned tables. Tables will be implicitly converted to COMPACT format with a warning to inform that Aurora MySQL doesn’t support compressed tables.

 **Upgrades and migrations:** 
+ To perform a minor version upgrade for an Aurora global database from Aurora MySQL version 3.01 or 3.02 to Aurora MySQL version 3.03 or higher, refer to [Upgrading Aurora MySQL by modifying the engine version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html#AuroraMySQL.Updates.Patching.ModifyEngineVersion). 
+ Fixed an issue that can cause upgrade precheck failures due to schema inconsistency errors reported for the `mysql.general_log_backup`, `mysql.general_log`, `mysql.slow_log_backup` and `mysql.slow_log` tables when upgrading from Aurora MySQL 2 to Aurora MySQL 3. For more information about upgrade troubleshooting, see [Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting).

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3031.Patches"></a>

This release includes all community bug fixes up to and including 8.0.26, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+  Fixed an issue where a buffer block containing intrinsic temporary table page was relocated during page traversal, causing an assertion failure. (Bug \#33715694) 