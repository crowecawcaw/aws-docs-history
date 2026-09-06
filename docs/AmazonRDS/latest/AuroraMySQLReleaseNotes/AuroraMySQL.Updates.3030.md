

# Aurora MySQL database engine updates 2023-03-01 (version 3.03.0) (Deprecated)
<a name="AuroraMySQL.Updates.3030"></a><a name="3.03.0"></a><a name="3.03.0"></a>

 **Version:** 3.03.0 

 Aurora MySQL 3.03.0 is generally available. Aurora MySQL 3.03 versions are compatible with MySQL 8.0.26, and Aurora MySQL 3.02 versions are compatible with MySQL 8.0.23. For more information on community changes that have occurred from 8.0.23 to 8.0.26, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

 For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see the [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html). 

 Currently supported Aurora MySQL releases are 2.07.\*, 2.11.\*, 3.01.\*, 3.02.\* and 3.03.\*. 

You can perform an in-place upgrade or restore a snapshot from any currently supported Aurora MySQL version 2 cluster into Aurora MySQL 3.03.0.

 For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3030.Improvements"></a>

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below:
+ [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
+ [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451)
+ [CVE-2022-21444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21444)

**Availability improvements:**
+ Fixed an issue where larger DB instance classes may experience issues during restart due to the buffer pool initialization taking longer than expected.
+ Fixed an issue where the DB instance may restart during the database recovery process when binary logging is enabled.
+ Fixed an issue that can cause connection failures on reader instances while executing Data Control Language (DCL) statements, for example `GRANT` and `REVOKE`, or while establishing new connections on the writer instance.
+ Fixed an issue where parallel query was incorrectly used for Data Manipulation Language (DML) operations, such as the `DELETE` and `UPDATE` statements, which aren't currently supported, that led to a DB instance restart. For more information on operations supported in parallel query, see [Aurora MySQL parallel query limitations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query.html#aurora-mysql-parallel-query-limitations).
+ Fixed an issue which, in rare cases, can cause Aurora replicas to restart during the simultaneous execution of large update operations or Data Definition Language (DDL) workloads on the writer instance and read operations on the same set of tables on the Aurora replica.
+ Fixed an issue with the Aurora serverless reader instance scale down operation that can cause that reader instance to restart, and in some rare cases, cause data inconsistency.
+ Fixed an issue which can cause the DB instance to restart due to incorrectly accessing an invalid memory location when a connection to the DB instance is closed.
+ Fixed an issue which, in rare conditions, can cause the DB instance to restart while processing a query with a `GROUP BY` clause that truncates a decimal column to zero decimal places.
+ Fixed an issue that can cause a DB instance restart due to incorrectly accessing a record when executing a range query using spatial index.
+ Fixed an issue that can cause a DB instance restart on Aurora MySQL replica instances when internal temporary tables exceed the default or customer-configured memory or mmap values.
+ Fixed an issue where the Advanced Audit log rotation may cause memory management issues.
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

**General improvements:**
+ Improved the read query latency of global database write forwarding sessions using the GLOBAL read consistency setting.
+ Fixed an issue where the `wait_timeout` parameter value wasn't being honored after a client session executed the `reset_connection` or `change_user` commands.
+ Fixed an issue where applications may experience increased latency while connecting to a DB instance when the instance is experiencing a sudden increase in incoming connections. Two new CloudWatch metrics, `AuroraSlowHandshakeCount` and `AuroraSlowConnectionHandleCount`, were introduced to help troubleshoot connection establishment delays for Aurora MySQL DB instances. More information on these metrics can be found in the Aurora CloudWatch metrics definitions documentation, [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Monitoring.Metrics.html).
+  The `temptable_use_mmap` parameter has been deprecated, and support for it is expected to be removed in a future MySQL release. For more information, see [Storage engine for internal (implicit) temporary tables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams3-temptable-behavior.html#ams3-temptable-behavior-engine).
+ Fixed an issue which can cause higher than expected execution times for the `SHOW BINARY LOGS` statement. This could lead to a drop in the commit throughput of the database.

 **Upgrades and migrations:** 
+ To perform a minor version upgrade for an Aurora global database from Aurora MySQL version 3.01 or 3.02 to Aurora MySQL version 3.03 or higher, refer to [Upgrading Aurora MySQL by modifying the engine version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html#AuroraMySQL.Updates.Patching.ModifyEngineVersion).
+ Fixed an issue that can cause major version upgrades from Aurora MySQL version 2 to Aurora MySQL version 3 to fail when there are a large number of tables (over 750K) in the cluster.
+ Fixed an issue that can cause major version upgrades from Aurora MySQL version 2 to Aurora MySQL version 3 to fail because migrating the `mysql.innodb_table_stats` and `mysql.innodb_index_stats` tables took longer than expected. This issue mainly affected DB clusters with millions of tables.
+ Fixed an issue that can cause failures while upgrading from Aurora MySQL version 2 to Aurora MySQL version 3 due to schema inconsistency errors. These errors are reported by the upgrade pre-checker for the `mysql.general_log_template` and `mysql.slow_log_template` tables. For more information about upgrade troubleshooting, see [Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting).
+ Fixed an issue that can cause upgrade failures from Aurora MySQL version 2 to Aurora MySQL version 3 due to the `schemaInconsistencyCheck` error. This error is caused by schema inconsistencies within the `mysql.table_migration_index_info` table, as reported by the `upgrade-prechecks.log`. For more information about troubleshooting upgrades to Aurora MySQL version 3, see [Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting).

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2102.Patches"></a>

This release includes all community bug fixes up to and including 8.0.26, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+  Fixed an issue where sorts of some column types, including `JSON` and `TEXT`, sometimes exhausted the sort buffer if its size wasn't at least 15 times that of the largest row in the sort. Now the sort buffer need only be 15 times as large as the largest sort key. (Bug \#103325, Bug \#105532, Bug \#32738705, Bug \#33501541) 
+  Fixed an issue where InnoDB did't always handle some legal names for table partitions correctly. (Bug \#32208630) 
+  Fixed an issue which, in certain conditions, may return incorrect results due to an inaccurate calculation of the nullability property when executing a query with an `OR` condition. (Bug \#34060289) 
+  Fixed an issue which, in certain conditions, may return incorrect results when the following two conditions are met: 
  + a derived table is merged into the outer query block 
  + the query includes a left join and an `IN` subquery 

  (Bug \#34060289) 
+  Fixed an issue where incorrect `AUTO_INCREMENT` values were generated when the maximum integer column value was exceeded. The error was due to the maximum column value not being considered. The previous valid `AUTO_INCREMENT` value should have been returned in this case, causing a duplicate key error. (Bug \#87926, Bug \#26906787) 
+  Fixed an issue where it wasn't possible to revoke the `DROP` privilege on the Performance Schema. (Bug \#33578113) 
+  Fixed an issue where a stored procedure containing an `IF` statement using `EXISTS`, which acted on one or more tables that were deleted and recreated between executions, didn't execute correctly for the subsequent invocations following the first one. (Bug \#32855634). 
+  Fixed an issue where a query that references a view in a subquery and an outer query block can cause an unexpected restart. (Bug\#32324234) 