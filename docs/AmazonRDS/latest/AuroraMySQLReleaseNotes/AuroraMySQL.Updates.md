# Aurora MySQL database engine updates 2023-10-17 (version 2.11.4, compatible with MySQL 5.7.12) - RDS Extended Support version

**Version:** 2.11.4

Aurora MySQL 2.11.4 is generally available. Aurora MySQL 2.11 versions are compatible with MySQL 5.7.12.
For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html "https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html").

The currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, and 3.04.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.11.4. You can
also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.11.4.

If you upgrade an Aurora MySQL global database to version 2.11.\*, you must upgrade your primary and secondary DB clusters to the exact same version, including the patch level.
For more information on upgrading the minor version of an Aurora global database, see [Minor version upgrades](../AuroraUserGuide/aurora-global-database-upgrade.md#aurora-global-database-upgrade.minor "../AuroraUserGuide/aurora-global-database-upgrade.md#aurora-global-database-upgrade.minor").

Immediately after an in-place engine version upgrade to Aurora MySQL 2.11.\* is performed, an operating system upgrade is applied
automatically to all affected instances on the db.r4, db.r5, db.t2, and db.t3 DB instance classes, if the instances are running an
old operating system version. In a Multi-AZ DB cluster, all of the reader instances apply the operating system upgrade first. When
the operating system upgrade on the first reader instance is finished, a failover occurs and the previous writer instance is
upgraded.

###### Note

The operating system upgrade isn't applied automatically to Aurora global databases during major version upgrades.

###### Note

For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](../AuroraUserGuide/AuroraMySQL.Updates.md "../AuroraUserGuide/AuroraMySQL.Updates.md") in the
_Amazon Aurora User Guide_.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.md "../AuroraUserGuide/USER_UpgradeDBInstance.md") in the _Amazon Aurora User Guide_.

## Improvements

**Fixed security issues and CVEs listed below:**

- Fixed an issue where the events that were reported while processing audit log rotations might not be written to the audit log.
- [CVE-2022-24407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407")

**Availability improvements:**

- Fixed an issue where Aurora MySQL database instances using parallel query may experience a database restart when running a high number of concurrent parallel queries.
- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads.
- Fixed an issue which can cause a database instance restart when attempting to read a database page that belongs to a dropped table.
- Fixed an issue which can cause the reader instance to restart when the writer instance grows the database volume to a multiple of 160GB.
- Fixed an issue which can cause database cluster unavailability if the writer instance restarts while the database is creating or dropping triggers on internal system tables.
- Fixed an issue which can cause a reader instance to restart when executing Data Manipulation Language (DML) queries on a table containing a full-text index.
- Fixed an issue which can cause a reader instance to restart while executing a query which utilizes an Aurora parallel query execution plan.
- Fixed an issue that can cause the writer instance to restart while executing the `OPTIMIZE TABLE` query on a table with a Full Text Search (FTS) index.
- Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running
  queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast
  insert optimization, see [Amazon Aurora MySQL performance enhancements](../AuroraUserGuide/Aurora.AuroraMySQL.md#Aurora.AuroraMySQL.Performance "../AuroraUserGuide/Aurora.AuroraMySQL.md#Aurora.AuroraMySQL.Performance").

**General improvements:**

- Fixed an issue where small read replica instances may experience increased replication lag after upgrading from versions below 2.11.\*.
- Fixed an issue that can cause excessive log messages when consulting the [procs_priv grant table](https://dev.mysql.com/doc/refman/8.0/en/grant-tables.html#grant-tables-procs-priv "https://dev.mysql.com/doc/refman/8.0/en/grant-tables.html#grant-tables-procs-priv") for verification of requests that involve stored routines.
- Fixed a memory management issue which can cause the database instance to use excessive memory while executing queries using the hash join optimization.
- Fixed an issue that caused a restart of the database when executing `SELECT` statements with partitioned tables (created in a version of MySQL supporting the old `ha_partition` partition handler) and parallel query is chosen by the query planner.
- Fixed an issue which can prevent new client connections from being established to the database when write forwarding is enabled.
- Reduced binary log (binlog) replication lag when an Aurora MySQL binlog replica is executing `QUERY` events written to the source's binlog file without a default database defined by the `USE` command.
- Fixed an issue involving index scans where an inaccurate result might be returned when executing a `SELECT` query with the `GROUP BY` clause and the `aurora_parallel_query` parameter turned `ON`.
- Added support for enabling and disabling session-level binary logging. See [Stored Procedures - Replicating](../AuroraUserGuide/mysql-stored-proc-replicating.md#mysql_rds_enable_session_binlog "../AuroraUserGuide/mysql-stored-proc-replicating.md#mysql_rds_enable_session_binlog") in the _Amazon Aurora User Guide_.
- Fixed an issue that can cause a binlog replica to restart if the system variable [server_uuid](https://dev.mysql.com/doc/refman/5.7/en/replication-options.html#sysvar_server_uuid "https://dev.mysql.com/doc/refman/5.7/en/replication-options.html#sysvar_server_uuid") of the source is missing or has an invalid value.
- Added support for setting session-level binary log format. See [Stored Procedures - Replicating](../AuroraUserGuide/mysql-stored-proc-replicating.md#mysql_rds_set_session_binlog_format "../AuroraUserGuide/mysql-stored-proc-replicating.md#mysql_rds_set_session_binlog_format") in the _Amazon Aurora User Guide_.
- Fixed an issue which can cause the `CommitLatency` CloudWatch metric to be incorrectly reported when the `innodb_flush_log_at_trx_commit` parameter is not set to 1.
- Fixed an issue to prevent InnoDB statistics from getting stale, which can sometimes generate a sub-optimal query execution plan that may lead to an increase in query execution time.
- Fixed an issue which can cause a database restart when connected binary log (binlog) consumers are using duplicate binlog replication server IDs.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 5.7.12, in addition to the below. For more information, see
[MySQL bugs fixed by Aurora MySQL 2.x database engine updates](AuroraMySQL.Updates.md#AuroraMySQL.Updates.MySQLBugs.v2 "AuroraMySQL.Updates.md#AuroraMySQL.Updates.MySQLBugs.v2").

- Replication: Some binary log events were not always handled correctly. (Bug #34617506)
- Fixed an issue which can cause higher CPU utilization due to background TLS certificate rotation (Community Bug Fix #34284186).
- In prepared statements, some types of subqueries could cause a server exit. (Bug #33100586)

## Features not supported in Aurora MySQL version 2

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).

- Scan batching. For more information, see [Aurora MySQL database engine updates
  2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md").

## MySQL 5.7 compatibility

This Aurora MySQL version is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes,
and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver

> 20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

This Aurora MySQL version does not currently support the following MySQL 5.7 features:

- Group replication plugin
- Increased page size
- InnoDB buffer pool loading at startup
- InnoDB full-text parser plugin
- Multisource replication
- Online buffer pool resizing
- Password validation plugin
- Query rewrite plugins
- Replication filtering
- The `CREATE TABLESPACE` SQL statement
