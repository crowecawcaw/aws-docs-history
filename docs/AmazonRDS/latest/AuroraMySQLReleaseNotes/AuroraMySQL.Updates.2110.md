

# Aurora MySQL database engine updates 2022-10-25 (version 2.11.0, compatible with MySQL 5.7.12) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2110"></a><a name="2110"></a><a name="2.11.0"></a>

 **Version:** 2.11.0 

 Aurora MySQL 2.11.0 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7.12. For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html). 

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 2.11.\*, 3.01.\* and 3.02.\*. 

 You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.11.0. For clusters running Aurora MySQL version 1, you can upgrade an existing Aurora MySQL 1.23 or higher cluster directly to 2.11.0. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.11.0. 

 If you upgrade an Aurora MySQL global database to version 2.11.\* and you have write forwarding turned on, you must upgrade your primary and secondary DB clusters to the exact same version, including the patch level, to continue using write forwarding. For more information on upgrading the minor version of an Aurora global database, see [Minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.html#aurora-global-database-upgrade.minor). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

**Note**  
 For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2110.Improvements"></a>

**Fixed security issues and CVEs:**
+ Changed the SSL/TLS provider from OpenSSL to [AWS-LC](https://github.com/aws/aws-lc).

  This brings a number of changes including, but not limited to, the removal of support for less secure DHE-RSA-\* ciphers.

  For more information, see [Using TLS with Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html#AuroraMySQL.Security.SSL)

The following CVE fixes are included in this release:
+ [CVE-2022-21460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21460)
+ [CVE-2022-21451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21451)
+ [CVE-2022-21444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21444)
+ [CVE-2022-21417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21417)
+ [CVE-2022-21304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21304)
+ [CVE-2022-21303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21303)
+ [CVE-2022-21245](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21245)
+ [CVE-2021-36222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222)
+ [CVE-2021-28196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28196)
+ [CVE-2021-23841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23841)
+ [CVE-2021-22926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22926)
+ [CVE-2021-3449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3449)
+ [CVE-2021-2307](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2307)
+ [CVE-2021-2226](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2226)
+ [CVE-2021-2202](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2202)
+ [CVE-2021-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2194)
+ [CVE-2021-2179](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2179)
+ [CVE-2021-2178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2178)
+ [CVE-2021-2174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2174)
+ [CVE-2021-2171](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2171)
+ [CVE-2021-2169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2169)
+ [CVE-2021-2166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166)
+ [CVE-2021-2160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2160)
+ [CVE-2021-2154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154)

 **New features:** 
+ With the release of Aurora MySQL version 2.11, a new operating system upgrade is available. We recommend that you apply this pending OS update to all your Aurora MySQL database instances after upgrading to version 2.11. For more information, see [Working with operating system updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#OS_Updates).
+ A new dynamic configuration option, innodb\_deadlock\_detect, may be used to disable deadlock detection. On high concurrency systems, deadlock detection can cause a slowdown when numerous threads wait for the same lock. At times, it may be more efficient to disable deadlock detection and rely on the innodb\_lock\_wait\_timeout setting for transaction rollback when a deadlock occurs. (Bug \#23477773) More information on Innodb deadlock detection can be found in the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/innodb-deadlock-detection.html).
+ The `UUID_TO_BIN`, `BIN_TO_UUID` and `IS_UUID` functions from MySQL 8.0 have been added. More information on using these functions can be found in [MySQL Miscellaneous function](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html).
+ Added support for optimizer hints allowing the user to enable or disable Aurora MySQL parallel query on a per-table or per-query basis.
  + [Working with parallel query for Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query.html)
  + [Aurora MySQL hints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.html#AuroraMySQL.Reference.Hints)
+ Removed R3 instance type support.
+ Added support for R6i instances.

**Availability improvements:**
+ Fixed an issue which can prevent cross region logical replication in a database cluster due to incorrect binlog file and position written to the error logs. This issue may occur when the engine is restarted after running a DDL statement.
+ Fixed an issue which, in rare conditions, can cause Aurora reader instances to restart when running Access-Control List (ACL) statements such as GRANT and FLUSH on the writer instance. This issue is more likely to affect reader instances with a large number of users and ACL operations (e.g., permission changes).
+ Fixed an issue which, in rare conditions, can cause the writer instance to restart or failover when a transaction accesses a row being deleted by another transaction.
+ Improved the Fulltext phrase search performance to significantly reduce the time taken to search phrases in a table with fulltext indexes.
+ Fixed an issue where, after a writer instance restarts, it would get stuck in slow recovery and subsequently restart again. This issue occurs when there are a large number of uncommitted rows in the database at the time of the initial restart.
+ Fixed an issue which, in rare cases, causes the database server to restart due to a long semaphore wait when the [deadlock detector thread](https://dev.mysql.com/doc/refman/5.7/en/innodb-deadlocks.html) gets stuck.
+ Fixed an issue which, in rare cases, can cause the database to restart due to a long semaphore wait when I/O threads become deadlocked.
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

 **General improvements:** 
+ Fixed an issue which can cause the database server to restart when all of the following conditions are true: 
  + ALLOW\_INVALID\_DATES is disabled in SQL MODE.
  + The database server is processing an INSERT, UPDATE, DELETE or SELECT statement with an invalid value of DATETIME type such that the month is not between 1 and 12.
+ Fixed an issue where the binary log retention period was not honored when log-bin was set to OFF, leading to higher than expected storage utilization. After this fix, the binary logs will be purged based on your retention period. More information on how to configure your binary log retention period can be found in the [Aurora MySQL User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.html#AuroraMySQL.Replication.MySQL.RetainBinlogs).
+ Fixed an issue which can cause the freeable memory on the database instance to reduce when certain Data Control Language (DCL) SQL statements such as GRANT, FLUSH PRIVILEGES etc. are run on that instance. Frequent use of such statements can cause the freeable memory to keep reducing and may cause the database instance to restart because of out-of-memory issues. Use of such statements on the writer instance can also cause the freeable memory on the reader instances to reduce.
+ Introduced a larger read buffer size for reads performed from the relay logs to minimize the number of read I/O operations, which reduces contention between the I/O and SQL threads.
+ Fixed an issue that can cause the mysql.rds\_rotate\_slow\_log stored procedure to fail with the error message "Table 'mysql.slow\_log\_backup' doesn't exist".
+ Fixed an issue where excessive query cache invalidation causes higher than expected CPU usage and latencies on the read replica due to the read replica having to read the data from the disk instead of from the query cache. 
+ Fixed an issue which allowed users to run the INSTALL PLUGIN and UNINSTALL PLUGIN commands on a reader instance, which can cause deadlock on LOCK\_plugin, LOCK\_system\_variables\_hash, LOCK\_global\_system\_variables. These statements can now only be executed on the writer instance in a database cluster.
+ Fixed an issue where clusters may experience higher than expected commit latency when binary logging is enabled. This affects all transactions that generate large binlog events (over 500MB in size).
+ Fixed an issue that can cause the trx\_active\_transactions metric in the INFORMATION\_SCHEMA.INNODB\_METRICS table to have an incorrect value.
+ Fixed an issue which can stop logical replication due to the binlog file becoming inconsistent while executing a rollback to savepoint for a large transaction.
+ Masked credential hashes in general-log, slow-query-log, and audit-log by default using a consistent mask secret. This is configurable via the aurora\_mask\_password\_hashes\_type parameter.
+ Fixed an issue where the Zero-Downtime-Restart (ZDR) duration is incorrectly reported in the customer observed events.
+ Fixed an issue which can cause calls to [ mysql\_rds\_import\_binlog\_ssl\_material](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_import_binlog_ssl_material.html) to fail with [ MySQL server ERROR 1457](https://dev.mysql.com/doc/mysql-errors/5.7/en/server-error-reference.html#error_er_sp_proc_table_corrupt).
+ Fixed an issue where dump thread initialization could get deadlocked with the thread for purging binary logs. This can stop the active binlog file from rotating and instead continue growing or cause issues with new binlog replica connections.
+ Fixed an issue where the query cache can return stale result on an Aurora read replica.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2110.Patches"></a>

This release includes all community bug fixes up to and including 5.7, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v2).
+ Fixed an issue where the code for reading character set information from Performance Schema statement events tables (for example, events\_statements\_current) did not prevent simultaneous writing to that character set information. As a result, the SQL query text character set could be invalid, which could result in a server exit. With this fix, an invalid character set causes SQL\_TEXT column truncation and prevents server exits. (Bug \#23540008)
+ InnoDB: Backport of a fix for Community Bug \#25189192, Bug \#84038. Fixed an issue where after a RENAME TABLE operation that moved a table to a different schema, InnoDB failed to update INNODB\_SYS\_DATAFILES data dictionary table. This resulted in an error on restart indicating that it could not locate the tablespace data file. 
+ InnoDB: Fixed an issue where the server dropped an internally defined foreign key index when adding a new index and attempted to use a secondary index defined on a virtual generated column as the foreign key index, causing a server exit. InnoDB now permits a foreign key constraint to reference a secondary index defined on a virtual generated column. (Bug \#23533396)
+ Fixed an issue where two sessions concurrently executing an INSERT ... ON DUPLICATE KEY UPDATE operation generated a deadlock. During partial rollback of a tuple, another session could update it. The fix for this bug reverts the fixes for Bug \#11758237, Bug \#17604730, and Bug \#20040791. (Bug \#25966845)
+ Backport of a fix for Community Bug \#27407480: Fixed an issue where the EXECUTE and ALTER ROUTINE privileges weren't correctly granted to routine creators even with automatic\_sp\_privileges enabled.
+ Backport of fix for Community Bug\#24671968: Fixed an issue where a query could produce incorrect results if the WHERE clause contained a dependent subquery, the table had a secondary index on the columns in the select list followed by the columns in the subquery, and `GROUP BY` or `DISTINCT` permitted the query to use a Loose Index Scan.
+ Fixed an issue where replication breaks if a multi-table delete statement is issued against multiple tables with foreign keys. (Bug \#80821)
+ Fixed an issue where in special cases certain slave errors are not ignored even with [slave\_skip\_errors](https://dev.mysql.com/doc/refman/5.6/en/replication-options-replica.html#sysvar_slave_skip_errors) enabled. In cases when opening and locking a table failed or when field conversions failed on a server running row-based replication, the error is considered critical and the state of [slave\_skip\_errors](https://dev.mysql.com/doc/refman/5.6/en/replication-options-replica.html#sysvar_slave_skip_errors) is ignored. The fix ensures that with [slave\_skip\_errors](https://dev.mysql.com/doc/refman/5.6/en/replication-options-replica.html#sysvar_slave_skip_errors)) enabled, all errors reported during applying a transaction are correctly handled. (Bug \#70640, Bug \#17653275)
+ Fixed an issue where a [`SET PASSWORD`](https://dev.mysql.com/doc/refman/5.7/en/set-password.html) statement was replicated from a MySQL 5.6 master to a MySQL 5.7 slave, or from a MySQL 5.7 master with the [log\_builtin\_as\_identified\_by\_password](https://dev.mysql.com/doc/refman/5.7/en/replication-options-binary-log.html#sysvar_log_builtin_as_identified_by_password) system variable set to ON to a MySQL 5.7 slave, the password hash was itself also hashed before being stored on the slave. The issue has now been fixed and the replicated password hash is stored as originally passed to the slave. (Bug\#24687073)
+ Fixed an issue where serialization of a JSON value consisting of a large sub-document wrapped in many levels of JSON arrays, objects, or both, sometimes required an excessive amount time to complete. (Bug \#23031146)
+  Statements that cannot be parsed (due, for example, to syntax errors) are no longer written to the slow query log. (Bug \#33732907) 

## Comparison with Aurora MySQL version 1
<a name="AuroraMySQL.Updates.2110.Compare56"></a>

The following Amazon Aurora MySQL features are supported in Aurora MySQL version 1 (compatible with MySQL 5.6), but these features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Hash joins. For more information, see [ Optimizing large Aurora MySQL join queries with hash joins](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.HashJoin) in the *Amazon Aurora User Guide*.
+ Native functions for synchronously invoking AWS Lambda functions. For more information, see [ Invoking a Lambda function with an Aurora MySQL native function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html#AuroraMySQL.Integrating.NativeLambda) in the *Amazon Aurora User Guide*.
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).
+ Migrating data from MySQL using an Amazon S3 bucket. For more information, see [ Migrating data from MySQL by using an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3) in the *Amazon Aurora User Guide*.

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2110.Compatibility"></a>

This Aurora MySQL version is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes, and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver >20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

This Aurora MySQL version does not currently support the following MySQL 5.7 features:
+ Group replication plugin
+ Increased page size
+ InnoDB buffer pool loading at startup
+ InnoDB full-text parser plugin
+ Multisource replication
+ Online buffer pool resizing
+ Password validation plugin
+ Query rewrite plugins
+ Replication filtering
+ The `CREATE TABLESPACE` SQL statement