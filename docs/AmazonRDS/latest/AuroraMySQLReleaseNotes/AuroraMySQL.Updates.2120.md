

# Aurora MySQL database engine updates 2023-07-25 (version 2.12.0, compatible with MySQL 5.7.40) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2120"></a><a name="2120"></a><a name="2.12.0"></a>

**Version:** 2.12.0

Aurora MySQL 2.12.0 is generally available. Aurora MySQL 2.12 versions are compatible up to MySQL 5.7.40. For more information on community changes, see [Changes in MySQL 5.7.40 (2022-10-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-40.html).

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\* and 3.03.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.0. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.0.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2120.Improvements"></a>

**Fixed security issues and CVEs listed below:**

This release includes all community CVEs fixes up to and including MySQL 5.7.40.
+ Default SSL ciphers used by Aurora MySQL have been updated to exclude the less secure DES-CBC3-SHA values from the [SSL\_CIPHER](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_ssl_cipher) database parameter. If you encounter SSL connection issues due to the removal of the DES-CBC3-SHA cipher, please use an applicable secure cipher from the following list, [Configuring cipher suites for connections to Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html#AuroraMySQL.Security.SSL.ConfiguringCipherSuites). More information on MySQL client [Connection Cipher Configuration](https://dev.mysql.com/doc/refman/5.7/en/encrypted-connection-protocols-ciphers.html#encrypted-connection-cipher-configuration) can be found in the MySQL documentation. 
+ [CVE-2023-21963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21963)
+ [CVE-2023-21912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21912)
+ [CVE-2023-21840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21840)
+ [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
+ [CVE-2022-43551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43551)
+ [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)
+ [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
+ [CVE-2021-36222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222)
+ [CVE-2021-22926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22926)
+ [CVE-2021-2169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2169)

**Availability improvements:**
+ Fixed an issue in the database activity streams event encryption which may cause database restarts
+ Fixed two issues which can cause a database restart to fail if it occurred while executing a Data Definition Language (DDL) query
+ Fixed an issue where connection surges can cause increased query latency or a database instance restart
+ Fixed an issue which, in rare cases, can cause an Aurora replica to restart during simultaneous execution of large update operations or Data Definition Language (DDL) workloads on the writer instance and read operations on the same set of tables on the Aurora replica
+ Fixed an issue where connection surges could cause the connection establishment process to take longer to complete or to fail with timeout errors
+ Fixed an issue where the Advanced Auditing log rotation may reduce the freeable memory, which could lead to the database instance restarting
+ Fixed an issue which can cause an Aurora MySQL reader instance to restart while executing a query which utilizes an Aurora parallel query execution plan
+ Fixed an issue that can cause the writer instance to restart while executing the `OPTIMIZE TABLE` query on a table with a Full Text Search (FTS) index
+ Fixed an issue which can cause the writer instance in an Aurora global database primary AWS Region to restart when a `SELECT FOR UPDATE` query is executed using global write forwarding from an Aurora global database secondary Region
+ Fixed an issue which can cause an Aurora global database secondary AWS Region reader instance using global write forwarding to restart when a forwarded [implicit commit statement](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html) encounters an error
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

**General improvements:**
+ Introduced file management performance optimizations on binlog replicas to help reduce contention when writing to relay log files
+ Fixed an issue that can cause the `buffer_pool_read_requests` counter to be reported incorrectly in the `information_schema` metrics
+ Fixed an issue that can cause the local storage to fill up when performing `LOAD FROM S3` or `SELECT INTO S3` operations. The issue can also lead to higher CPU utilization, database restarts due to low memory, and increased latency for these queries.
+ Fixed an issue where DB instances using binary log replication may experience an increase in CPU utilization and connection failures when multiple binary log replication consumers are attached
+ Fixed an issue where the SSL server status variables weren't being populated
+ Fixed an issue where the Data Manipulation Language (DML) statements executing duplicate writes could lead to excessive error logging and increased query latencies
+ Upgraded the time zone definitions to the IANA 2023c version
+ Added support for enabling and disabling session-level binary logging. See [Stored Procedures - Replicating](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html#mysql_rds_enable_session_binlog) in the Amazon Aurora User Guide
+ Added support for setting the session-level binary log format. See [Stored Procedures - Replicating](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html#mysql_rds_set_session_binlog_format) in the Amazon Aurora User Guide
+ Fixed an issue where setting the `aurora_disable_hash_join` parameter to `1` or `ON` might not prevent the optimizer from using a hash join
+ Fixed an issue involving index scans where an inaccurate result might be returned when executing a `SELECT` query with the `GROUP BY` clause and the `aurora_parallel_query` parameter turned `ON`
+ Fixed an issue which, in rare cases, can cause an Amazon Aurora reader instance to restart when accessing a table which has large update or Data Definition Language (DDL) operations running concurrently on the writer instance
+ Fixed an issue that can cause the `buffer_pool_read_requests` counter to be reported incorrectly in the `information_schema` metrics
+ Fixed an issue that can cause a binlog replica to restart if the system variable [server uuid](https://dev.mysql.com/doc/refman/5.7/en/replication-options.html#sysvar_server_uuid) of the source is missing or has an invalid value
+ Fixed an issue to prevent InnoDB statistics from getting stale, which can sometimes generate a sub-optimal query execution plan that may lead to an increase in the query execution time
+ Fixed an issue wherein the `AuroraGlobalDBRPOLag` CloudWatch metrics always displayed zero regardless of the user workload

 **Upgrades and migrations:** 
+ To perform a minor version upgrade for an Aurora global database from Aurora MySQL version 2.07 or 2.11 to Aurora MySQL version 2.12 or higher, refer to [Upgrading Aurora MySQL by modifying the engine version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html#AuroraMySQL.Updates.Patching.ModifyEngineVersion).

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2120.Patches"></a>

This release includes all community bug fixes up to and including 5.7.40 in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v2).
+ Fixed an issue which can cause higher CPU utilization due to background TLS certificate rotation (Community Bug Fix \#34284186)

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2120.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching.

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2120.Compatibility"></a>

This Aurora MySQL version is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes, and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver >20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

This Aurora MySQL version does not currently support the following MySQL 5.7 features:
+ The `CREATE TABLESPACE` SQL statement
+ Group replication plugin
+ Increased page size
+ InnoDB buffer pool loading at startup
+ InnoDB full-text parser plugin
+ Multisource replication
+ Online buffer pool resizing
+ Password validation plugin
+ Query rewrite plugins
+ Replication filtering
+ X Protocol