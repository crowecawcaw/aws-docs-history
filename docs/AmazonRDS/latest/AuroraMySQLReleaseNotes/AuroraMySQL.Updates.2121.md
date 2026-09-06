

# Aurora MySQL database engine updates 2023-12-28 (version 2.12.1, compatible with MySQL 5.7.40) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2121"></a><a name="2121"></a><a name="2.12.1"></a>

**Version:** 2.12.1

Aurora MySQL 2.12.1 is generally available. Aurora MySQL 2.12 versions are compatible up to MySQL 5.7.40. For more information on community changes, see [Changes in MySQL 5.7.40 (2022-10-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-40.html).

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, 3.04.\*, and 3.05.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.1. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.1.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2121.Improvements"></a>

**Fixed security issues and CVEs listed below:**

This release includes all community CVEs fixes up to and including MySQL 5.7.44.

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes are below:
+ [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)
+ [CVE-2023-22053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22053)
+ [CVE-2023-22028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22028)
+ [CVE-2023-22026](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22026)
+ [CVE-2023-22015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22015)
+ [CVE-2022-24407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407)
+ [CVE-2020-11105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11105)
+ [CVE-2020-11104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11104)
+ Fixed processing of single character tokens by a Full-Text Search (FTS) parser plugin (Bug \#35432973)
+ Fixed an issue where events that were reported while processing the audit log rotations might not be written to the audit log

**New features:**
+ Added support for multi-threaded binary log (binlog) replication, where the SQL thread on the binlog replica would apply binary log events in parallel when possible. Learn more about the configuration options to help fine-tune your multithreaded replication in the [Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.html).

**Availability improvements:**
+ Fixed an issue where Aurora MySQL database instances using parallel query may experience a database restart when running a high number of concurrent parallel queries.
+ Fixed an issue with lock contention caused by an audit logging thread that can lead to high CPU utilization and client application timeouts.
+ Fixed an issue which can cause a database instance restart when attempting to read a database page that belongs to a dropped table.
+ Fixed an issue which can cause the reader instance to restart when the writer instance grows the database volume to a multiple of 160GB.
+ Fixed an issue in the lock manager that could cause a restart or failover, when handling two-phase commits with the isolation level set to `READ_COMMITED` or `READ_UNCOMMITED` and either XA transactions are used or binary log (binlog) is enabled.
+ Fixed an issue which can cause database cluster unavailability if the writer instance restarts while the database is creating or dropping triggers on internal system tables.
+ Fixed an issue that may cause the database instance to restart when the number of database connections approaches the value set by the `max_connections` parameter.
+ Fixed an issue which can cause an Aurora reader instance to restart when executing Data Manipulation Language (DML) queries on a table containing a full-text index.
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

**General improvements:**
+ Fixed an issue which can cause a parallel query to fail due to transient network issues while reading data from the Aurora cluster volume.
+ Fixed an issue related to audit log file management which can cause log files to be inaccessible for download or rotation, and in some cases increase CPU utilization.
+ Fixed an issue where small read replica instances may experience increased replication lag after upgrading from versions below 2.11.\*
+ Fixed an issue that can cause excessive log messages when consulting the [`procs_priv` grant table](https://dev.mysql.com/doc/refman/8.0/en/grant-tables.html#grant-tables-procs-priv) for verification of requests that involve stored routines.
+ Fixed a memory management issue which can cause the database instance to use excessive memory while executing queries using the hash join optimization.
+ Fixed an issue which can produce an incorrect value of the variable `Threads_running` in the `information_schema` and `performance_schema` global status tables when using write forwarding.
+ Fixed an issue that caused a restart of the database when executing `SELECT` statements with partitioned tables (created in a version of MySQL supporting the old `ha_partition` partition handler) and parallel query is chosen by the query planner.
+ Fixed an issue which can prevent new client connections from being established to the database when write forwarding is enabled.
+ Reduced binary log (binlog) replication lag when an Aurora MySQL binlog replica is executing `QUERY` events written to the source's binlog file without a default database defined by the `USE` command.
+ Fixed an issue which can cause the `CommitLatency` CloudWatch metric to be incorrectly reported when the `innodb_flush_log_at_trx_commit` parameter is not set to 1.
+ Fixed an issue which can cause database connections to be closed before being established. This issue is more likely to affect database instances which open and close connections at a high rate.
+ Fixed an issue which can cause a database restart when connected binary log (binlog) consumers are using duplicate binlog replication server IDs.
+ Fixed an issue that can cause multithreaded binary log replication to stop when the `replica_parallel_type` variable is set to `LOGICAL_CLOCK` and the `replica_preserve_commit_order` variable is turned `ON`. This issue can occur when a transaction larger than 500 MB is run on the source.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2121.Patches"></a>

This release includes all community bug fixes up to and including 5.7.40 in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v2).
+ Fixed an issue which can cause existing and new remote connections to stall when run concurrently with `SHOW PROCESSLIST` statement (Community Bug \#34857411)
+ Replication: Some binary log events were not always handled correctly (Bug \#34617506)

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2121.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2121.Compatibility"></a>

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