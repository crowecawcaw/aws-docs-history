

# Aurora MySQL database engine updates 2023-10-25 (version 3.05.0) (Deprecated)
<a name="AuroraMySQL.Updates.3050"></a><a name="3.05.0"></a><a name="3.05.0"></a>

 **Version:** 3.05.0 

 Aurora MySQL 3.05.0 is generally available. Aurora MySQL 3.05 versions are compatible with MySQL 8.0.32. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

 For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html). 

 Currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, and 3.05.\*. 

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.05.0 cluster. 

 For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3050.Improvements"></a>

 **New features:** 
+ Added support for saving data from an Aurora MySQL database cluster into text files in an Amazon S3 bucket encrypted with a KMS key (SSE-KMS). For more information, see [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.SaveIntoS3.html). 
+ Introduced a new global status variable `aurora_tmz_version` to denote the current version of the time zone (TZ) information used by the engine. The values follow the IANA time zone database version and are formatted as "YYYYsuffix", for example, 2022a and 2023c. For more information, see [Aurora MySQL global status variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html#AuroraMySQL.Reference.GlobalStatusVars). 

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes are below:
+ [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)

 **Availability improvements:** 
+ Fixed an issue where Aurora MySQL database instances using parallel query may experience a database restart when running a high number of concurrent parallel queries. 
+  Fixed an issue with lock contention caused by an audit logging thread eventually leading to high CPU utilization and client application timeouts. 
+ Fixed an issue which can cause the executed GTID set to be recovered incorrectly on a binary log (binlog) replica cluster with enhanced binlog enabled when any binlog source has `gtid_mode` set to `ON` or `ON_PERMISSIVE`. This issue may cause the replica cluster's writer instance to restart an additional time during recovery, or lead to incorrect results when querying the executed GTID set. 
+ Fixed a memory management issue that can cause an Aurora MySQL database instance restart or a failover due to a decrease in freeable memory when enhanced binary log is enabled. 
+ Fixed an issue which can cause a database instance restart when attempting to read a database page that belongs to a dropped table. 
+ Fixed an issue which can cause the reader instance to restart when the writer instance grows the database volume to a multiple of 160GB. 
+ Fixed an issue where an Aurora MySQL database instance with the enhanced binary log feature enabled might get stuck during the database instance startup as the binary log recovery process is being executed. 
+ Fixed an issue where an Aurora MySQL database instance may experience multiple restarts during instance startup while large rollback segments are initialized. 
+ Fixed an issue during zero downtime patching which causes an instance restart that leads to database connections being unexpectedly closed. 
+ Fixed an issue which can cause a database instance restart due to a deadlatch when running [SHOW STATUS](https://dev.mysql.com/doc/refman/8.0/en/show-status.html) and [PURGE BINARY LOGS](https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html) statements concurrently. The purge binary logs is a managed statement that is executed to honor the user configured binlog retention period. 
+ Fixed an issue which can cause database cluster unavailability if the writer instance restarts while the database is creating or dropping triggers on internal system tables. 
+ Fixed an issue which can cause a database instance restart due to a long semaphore wait when using the enhanced binlog feature on a cluster with an Aurora replica. 
+ Fixed an issue which can cause a database instance to restart while executing a query which references an aggregate function. 
+ Fixed an issue which, in rare conditions, can cause the database instance to restart when Aurora serverless incorrectly attempts to update the table cache while scaling. 
+ Fixed an issue where unsupported index scan access methods were considered for common table expressions (CTE) while materializing intermediate temporary tables, which can lead to undesired behavior including database restarts or incorrect query results. We fixed this issue by avoiding the use of such unsupported index scan access methods on tables using the TempTable storage engine.

 **General improvements:** 
+ Fixed an issue which can cause database unavailability when enhanced binlog is enabled on an Aurora serverless database cluster running on Aurora MySQL 3.04.0.
+ Removed unused storage metadata before writing to Aurora storage when the enhanced binlog feature is enabled. This avoids certain scenarios when a database restart or failover may occur because of increased write latency due to increased bytes transmitted over the network. 
+ With the addition of the `malloc_stats` and `malloc_stats_totals` tables in the `performance_schema`, three advanced system variables were added to control the behavior of Jemalloc, an internal memory allocator:
  + `aurora_jemalloc_background_thread`.
  + `aurora_jemalloc_dirty_decay_ms`.
  + `aurora_jemalloc_tcache_enabled`.
+ Fixed an issue where Aurora specific performance schema tables were not created upon an upgrade or migration. 
+ Added a new system variable, `aurora_use_vector_instructions`. When this parameter is enabled, Aurora MySQL uses optimized vector processing instructions to improve performance on I/O heavy workloads. This setting is turned `ON` by default in Aurora MySQL 3.05 and higher. For more details, see [Aurora MySQL configuration parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html#AuroraMySQL.Reference.Parameters.Instance).
+ Fixed an issue which can cause the `NumBinaryLogFiles` metrics on CloudWatch to display incorrect results when enhanced binlog is enabled. 
+ The request timeout for [Aurora MySQL Machine Learning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-ml.html) operations to Amazon Sagemaker has been increased from 3 to 30 seconds. This helps resolve an issue where customers may see an increased number of retries or failures for requests to Amazon Sagemaker from Aurora MySQL Machine Learning when using larger batch sizes. 
+ Added support for `malloc_stats` and `malloc_stats_totals` tables in the performance\_schema database. 
+ Updated the `FROM` keyword in the `LOAD DATA FROM S3` command to be optional. For more information, see [Loading data into an Amazon Aurora MySQL DB cluster from text files in an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.LoadFromS3.html). 
+ Added support for the parameter `innodb_aurora_instant_alter_column_allowed`, which controls whether the `INSTANT` algorithm can be used for `ALTER COLUMN` operations. For more information see [Cluster-level parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html#AuroraMySQL.Reference.Parameters.Cluster). 
+ Fixed an issue which can prevent new client connections from being established to the database when write forwarding is enabled. 
+ Fixed an issue which can cause the modification of the `table_open_cache` database parameter to not take effect until the database instance is restarted. 
+ Fixed an issue which can cause duplicate key errors for `AUTO_INCREMENT` columns using descending indices after a snapshot restore, backtrack, or database clone operation. 
+ Fixed an issue involving index scans where an inaccurate result might be returned when executing a `SELECT` query with the `GROUP BY` clause and the `aurora_parallel_query`parameter turned `ON`. 
+ Fixed an issue which may cause the depletion of available memory when executing queries against the `INFORMATION_SCHEMA INNODB_TABLESPACES` table. 
+ Fixed an issue where the reader instance is unable to open a table, with ERROR 1146. This issue occurs when executing certain types of online Data Definition Language (DDL) while the `INPLACE` algorithm is being used on the writer instance. 
+ Fixed an issue to avoid an instance restart during Aurora serverless scaling when the internal monitoring process erroneously submits duplicate scaling requests. 
+ Fixed an issue which can cause a database restart when connected binary log (binlog) consumers are using duplicate binlog replication server IDs. 
+ Introduced an in-memory [relay log](https://dev.mysql.com/doc/refman/8.0/en/replica-logs-relaylog.html) cache for Aurora MySQL managed binary log replicas. This improvement can help achieve up to a 40% increase in binary log replication throughput. This enhancement is enabled automatically when using single-threaded binary log replication or when using multi-threaded replication with [GTID auto-positioning](https://dev.mysql.com/doc/refman/8.0/en/replication-gtids-auto-positioning.html) enabled.

 **Upgrades and migrations:** 
+ Upgrading from MySQL 5.7 to MySQL 8.0 with a very large number of tables in a single database caused the server to consume excessive memory. It was found that, during the process of checking whether tables could be upgraded, we fetched all the data dictionary `Table` objects upfront, processing each and fetching its name, then performed [Checking Version Compatibility](https://dev.mysql.com/doc/refman/8.0/en/check-table.html#check-table-version-compatibility) on the list. Fetching all objects beforehand was not necessary in this case, and contributed greatly to memory consumption. To correct this problem, we now fetch one `Table` object at a time in such cases, performing any required checks, fetching its name, and releasing the object, before proceeding with the next one. (Bug \#34526001) 
+ Improved the performance of major version upgrades from Aurora MySQL version 2 to version 3 by executing tablespace checks in parallel using all available vCPUs on the database instance.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3050.Patches"></a>

This release includes all community bug fixes up to and including 8.0.32, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+  Fixed an issue which can cause higher CPU utilization due to background TLS certificate rotation. (Community Bug Fix \#34284186) 