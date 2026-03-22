# Aurora MySQL database engine updates 2023-07-31 (version 3.04.0) , compatible with MySQL 8.0.28)

**Version:** 3.04.0

Aurora MySQL 3.04.0 is generally available. Aurora MySQL 3.04 versions are compatible with MySQL 8.0.28, Aurora MySQL 3.03 versions are compatible with MySQL 8.0.26, and Aurora MySQL 3.02 versions
are compatible with MySQL 8.0.23. For more information on community changes that have occurred from 8.0.23 to 8.0.28, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

###### Note

This version is designated as a long-term support (LTS) release. For more information, see [Aurora MySQL long-term support (LTS)
releases](../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md#AuroraMySQL.Updates.LTS "../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md#AuroraMySQL.Updates.LTS") in the _Amazon Aurora User Guide_.

We recommend that you don't set the `AutoMinorVersionUpgrade` parameter to
`true` (or enable **Auto minor version upgrade** in the AWS Management Console) for LTS versions. Doing so could lead
to your DB cluster being upgraded to the next target version for Automatic Minor Version Upgrade campaign, which may not be an LTS version.

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.MySQL80.md "../AuroraUserGuide/AuroraMySQL.MySQL80.md").
For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](../AuroraUserGuide/Aurora.AuroraMySQL.Compare-v2-v3.md "../AuroraUserGuide/Aurora.AuroraMySQL.Compare-v2-v3.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0
Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md").

Currently supported Aurora MySQL releases are 2.07.9, 2.11.1, 2.11.2, 3.01.\*, 3.02.\*, 3.03.\*, and 3.04.0.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS
Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.04.0 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Upgrade planning for Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-planning "../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-planning") in the _Amazon Aurora User Guide_. For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting upgrade issues with Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting "../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting").

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

###### Note

Aurora MySQL enhanced binary log (binlog) is currently not supported for the Aurora Serverless v2 database instance on Aurora MySQL version 3.04.0.
Enabling this feature may lead to database unavailability. If you require the use of enhanced binary log on Aurora MySQL version 3.04.0, we recommend
using a [non-serverless database instance class](../AuroraUserGuide/Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.Types "../AuroraUserGuide/Concepts.DBInstanceClass.md#Concepts.DBInstanceClass.Types")
or setting the minimum and maximum ACU of the Serverless v2 database instance to the same value.

More information on enhanced binary logging in Aurora MySQL is available in the [Aurora User Guide](../AuroraUserGuide/AuroraMySQL.Replication.MySQL.md#AuroraMySQL.Enhanced.binlog "../AuroraUserGuide/AuroraMySQL.Replication.MySQL.md#AuroraMySQL.Enhanced.binlog").

## Improvements

**New features:**

- Improved the performance of queries using InnoDB full-text indices to search phrases in [natural language mode](https://dev.mysql.com/doc/refman/8.0/en/fulltext-natural-language.html "https://dev.mysql.com/doc/refman/8.0/en/fulltext-natural-language.html").
  For more information on full text searches in MySQL, refer to [Full-Text Search Functions](https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html "https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html").
- Amazon Aurora MySQL supports local (in-cluster) write forwarding. You can now forward write operations from a reader DB instance to a writer DB instance within an Aurora MySQL DB cluster.
  For more information, see [Using local write forwarding in an Aurora MySQL DB cluster](../AuroraUserGuide/aurora-mysql-write-forwarding.md "../AuroraUserGuide/aurora-mysql-write-forwarding.md").
- Added the capability to change the value of the `aurora_replica_read_consistency` parameter for the [Using write forwarding in an Amazon Aurora global database](../AuroraUserGuide/aurora-global-database-write-forwarding.md "../AuroraUserGuide/aurora-global-database-write-forwarding.md") feature in sessions which have `autocommit` disabled.
  For more information, see [Configuration parameters for write forwarding](../AuroraUserGuide/aurora-global-database-write-forwarding.md#aurora-global-database-write-forwarding-params "../AuroraUserGuide/aurora-global-database-write-forwarding.md#aurora-global-database-write-forwarding-params").
- Starting with Aurora MySQL 3.04, for the [global database write forwarding](../AuroraUserGuide/aurora-global-database-write-forwarding.md#aurora-global-database-write-forwarding-params "../AuroraUserGuide/aurora-global-database-write-forwarding.md#aurora-global-database-write-forwarding-params")
  feature, you can now set the value of the `aurora_replica_read_consistency` parameter via the database cluster and database instance parameter groups. Prior to Aurora MySQL version 3.04, this parameter's value could only be configured at the session level.

**Fixed security issues and CVEs:**

- Changed the SSL/TLS provider from OpenSSL to [AWS-LC](https://github.com/aws/aws-lc "https://github.com/aws/aws-lc"). This brings
  a number of changes including, but not limited to the following:

      + Database connections using SSL can now be restored by Zero Downtime Restart and Zero Downtime Patching when
       upgrading from Aurora MySQL version 3.04.0 to a higher version.
      + Support for TLSv1.3 which includes support for TLS\_AES\_128\_GCM\_SHA256, TLS\_AES\_256\_GCM\_SHA384 and
       TLS\_CHACHA20\_POLY1305\_SHA256 SSL ciphers.
      + Removal of support for less secure DHE-RSA-\* ciphers.

  For more information, see [Using TLS with Aurora MySQL
  DB clusters](../AuroraUserGuide/AuroraMySQL.Security.md#AuroraMySQL.Security.SSL "../AuroraUserGuide/AuroraMySQL.Security.md#AuroraMySQL.Security.SSL")

- Added the dynamic privilege `SHOW_ROUTINE` to the `rds_superuser_role` which enables access to
  definitions and properties of all stored routines, such as stored procedures and functions. For more details, see [SHOW_ROUTINE](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine "https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine").
- Fixed an issue which may cause the audit log to miss events during audit log file rotation.
- Enabled support for secure and performant Transport Layer Security (TLS) 1.3 protocol while maintaining compatibility
  with TLS 1.2 version.
- TLS versions TLSv1 and TLSv1.1 were deprecated in community MySQL 8.0.26 and correspondingly in Aurora MySQL 3.03. These
  protocols have now been removed in community MySQL 8.0.28 and correspondingly in Aurora MySQL 3.04. By default, any secure
  client that cannot communicate over TLS 1.2 or higher will be rejected. For more information on connecting to your
  database instances using TLS, please see [Security with Amazon Aurora MySQL](../AuroraUserGuide/AuroraMySQL.Security.md "../AuroraUserGuide/AuroraMySQL.Security.md").

The following CVE fixes are included in this release:

- [CVE-2023-21963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21963 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21963")
- [CVE-2023-21912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21912 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21912")
- [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215")
- [CVE-2022-43551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43551 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43551")
- [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434")
- [CVE-2022-21635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21635 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21635")
- [CVE-2022-21556](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21556 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21556")
- [CVE-2022-21352](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21352 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21352")
- [CVE-2021-35630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35630 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35630")
- [CVE-2021-35624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35624 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35624")

**Availability improvements:**

- Fixed an issue that can cause database restarts during long transaction recovery.
- Fixed an issue within database activity streams event encryption that can cause database restarts.
- Fixed a memory management issue due to out of memory errors when the InnoDB buffer pool is being initialized during startup or
  while scaling in Aurora Serverless v2. This issue might have caused database instance restarts or performance degradation
  including throughput reduction or increased latency.
- Fixed an issue that can cause an Aurora MySQL reader instance to restart while executing a query which utilizes an Aurora MySQL
  parallel query execution plan.
- Fixed an issue that, in certain situations, can cause Aurora reader instances to restart during a range estimation.
- Fixed an issue that can interrupt database recovery during startup if the restart occurred while executing heavy insert
  operations involving auto-increment columns.
- Fixed an issue with Aurora advanced auditing that causes excess logging of informational messages to the Aurora MySQL error log
  when the server variable `server_audit_events` is set to `ALL` or `QUERY`. This issue
  might cause a database instance restart.
- Fixed an issue that can cause a database restart during the rollback of an `INSERT` statement when parallel query
  is enabled.
- Fixed an issue that can cause the database instance to restart when running the `EXPLAIN ANALYZE` profiling tool on
  a query which returned the output `all select tables were optimized away` within the `EXTRA`
  information column. For more information, see the MySQL documentation on [`EXPLAIN` Output Format](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html "https://dev.mysql.com/doc/refman/8.0/en/explain-output.html").
- Fixed an issue that can cause an Aurora global database secondary Region reader instance using global write forwarding to
  restart when a forwarded [implicit commit
  statement](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html "https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html") encounters an error.
- Fixed an issue that can cause the writer instance in an Aurora global database primary Region to restart when a `SELECT
FOR UPDATE` query is executed using global write forwarding from an Aurora global database secondary
  Region.

**General improvements:**

- Added a new stored procedure, `mysql.rds_gtid_purged`, to allow customers to set the `GTID_PURGED` system variable.
  For more information, see [mysql.rds_gtid_purged](../AuroraUserGuide/mysql-stored-proc-replicating.md#mysql_rds_gtid_purged "../AuroraUserGuide/mysql-stored-proc-replicating.md#mysql_rds_gtid_purged").
- Added two new stored procedures, `mysql.rds_start_replication_until` and `mysql.rds_start_replication_until_gtid`, which
  allow customers to configure a location to stop binary log replication. For more information on configuring a stop location for binary log
  replication in Aurora MySQL, see [mysql.rds_start_replication_until](../UserGuide/mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "../UserGuide/mysql-stored-proc-replicating.md#mysql_rds_start_replication_until").
- Fixed an issue that would prevent [Aurora MySQL replication control stored procedures](../AuroraUserGuide/mysql-stored-proc-replicating.md "../AuroraUserGuide/mysql-stored-proc-replicating.md")
  from modifying the [`sql_log_bin`](https://dev.mysql.com/doc/refman/8.0/en/set-sql-log-bin.html "https://dev.mysql.com/doc/refman/8.0/en/set-sql-log-bin.html")
  variable, when called from a session with autocommit mode disabled.
- Added logical replication support for the following Data Control Language (DCL) statements: `GRANT/REVOKE` and
  `CREATE/DROP/ALTER/RENAME USER`.
- Fixed an issue to prevent InnoDB statistics from getting stale, which can sometimes generate a sub-optimal query execution plan that may lead to
  an increase in the query execution time.
- Added two new system views, `information_schema.aurora_global_db_instance_status` and `information_schema.aurora_global_db_status`.
  These views can be used to display the status and topology of primary and secondary resources in an Aurora MySQL global database cluster. The details of the two
  system views can be found here, [Aurora MySQL–specific information_schema tables](../AuroraUserGuide/AuroraMySQL.Reference.ISTables.md "../AuroraUserGuide/AuroraMySQL.Reference.ISTables.md").
- Fixed an issue where a user is unable to access the database with a wildcard character in the database name after executing the `SET ROLE` statement with an escaped wildcard character.
- Fixed an issue where events that were reported while processing audit log rotations might not be written to the audit log.
- Fixed an issue where creating an internal temporary table, via a `TRIGGER` execution, can cause a writer database instance to restart.
- Added a new system variable, `innodb_aurora_max_partitions_for_range`. In some cases where persisted stats are not available, this
  parameter can be used to improve the execution time of row count estimations on partitioned tables. More information can be found in the documentation,
  [Aurora MySQL configuration parameters](../AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.md "../AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.md").
- Fixed an issue which incorrectly allows customers to set `ROW_FORMAT` as `COMPRESSED` when creating partitioned tables.
  Tables will be implicitly converted to `COMPACT` format with a warning to inform that Aurora MySQL doesn't support compressed tables.
- Fixed an issue that can cause multithreaded binary log replication to stop when the `replica_parallel_type` variable is set to
  `LOGICAL_CLOCK` and the `replica_preserve_commit_order` variable is turned `ON`. This issue can occur when a
  transaction larger than 500 MB is run on the source.
- Fixed an issue when the [global database write forwarding](../AuroraUserGuide/aurora-global-database-write-forwarding.md "../AuroraUserGuide/aurora-global-database-write-forwarding.md")
  feature is enabled that can cause changes to the `performance_schema` configuration on the reader instances in the secondary Regions to be
  unintentionally forwarded to the writer instance in the primary Region.
- Fixed an issue where the server status variable `innodb_buffer_pool_reads` may not be updated after a data page is read from the Aurora storage file system.
- Aurora MySQL parallel query is not supported when choosing the Aurora I/O-Optimized cluster configuration. For more information, see [Amazon Aurora MySQL parallel query
  limitations](../AuroraUserGuide/aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-limitations "../AuroraUserGuide/aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-limitations").
- Fixed an issue, when parallel query is enabled, that causes the query plan optimizer to pick an inefficient execution plan for certain `SELECT`
  queries that benefit from a primary or secondary index.
- Upgraded the time zone definitions to the IANA 2023c version.
- Introduced file management performance optimizations on binlog replicas to help reduce contention when writing to relay log files.
- Fixed an issue where the `RPO_LAG_IN_MILLISECONDS` column in the `information_schema.aurora_global_db_status` table and
  `AuroraGlobalDBRPOLag` CloudWatch metric always displayed zero regardless of the user workload.
- Introduced a new parameter `aurora_tmptable_enable_per_table_limit`. When this parameter is enabled, the `tmp_table_size`
  variable defines the maximum size of the individual in-memory internal temporary table created by the TempTable storage engine. For additional details,
  see [Storage engine for internal (implicit) temporary tables](../AuroraUserGuide/ams3-temptable-behavior.md#ams3-temptable-behavior-engine "../AuroraUserGuide/ams3-temptable-behavior.md#ams3-temptable-behavior-engine").
- Fixed an issue where an additional connection is created when the [global database write forwarding](../AuroraUserGuide/aurora-global-database-write-forwarding.md "../AuroraUserGuide/aurora-global-database-write-forwarding.md")
  feature is enabled. The issue occurs when read-only transactions on a reader instance incorrectly forward an implicit commit to the writer.
- Fixed an issue where the `PROCESSLIST_USER` and `PROCESSLIST_HOST` fields in the `performance_schema.threads` table were not
  populated on the writer in the primary Region for connections using the [global database write forwarding](../AuroraUserGuide/aurora-global-database-write-forwarding.md "../AuroraUserGuide/aurora-global-database-write-forwarding.md") feature.
  More information about this table and Performance Schema can be found in the MySQL Reference Manual, [The threads Table](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-threads-table.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-threads-table.html"),
  and the Amazon Aurora User Guide [Overview of the Performance Schema](../AuroraUserGuide/USER_PerfInsights.EnableMySQL.md#USER_PerfInsights.EnableMySQL.overview "../AuroraUserGuide/USER_PerfInsights.EnableMySQL.md#USER_PerfInsights.EnableMySQL.overview").
- Fixed an issue where the `CommitLatency` Cloudwatch metric displayed incorrect values for reader instances in secondary Regions when the
  [global database write forwarding](../AuroraUserGuide/aurora-global-database-write-forwarding.md "../AuroraUserGuide/aurora-global-database-write-forwarding.md") feature is used.
  To monitor the forwarded DML statement latency on secondary database clusters, it is recommended to use the `ForwardingReplicaDMLLatency` and
  `ForwardingWriterDMLLatency` metrics. Commit latency can also be observed using the `CommitLatency` metric on the primary Region's
  writer instance. More information is available in the Aurora User Guide, [Amazon CloudWatch metrics for write forwarding](../AuroraUserGuide/aurora-global-database-write-forwarding.md#aurora-global-database-write-forwarding-cloudwatch "../AuroraUserGuide/aurora-global-database-write-forwarding.md#aurora-global-database-write-forwarding-cloudwatch").
- Fixed an issue where the [Aurora MySQL replication control stored procedures](../AuroraUserGuide/mysql-stored-proc-replicating.md "../AuroraUserGuide/mysql-stored-proc-replicating.md") used to manage and configure binary log replication
  incorrectly report errors when multi-threaded binary log replication is configured by setting the [`replica_parallel_workers`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html#sysvar_replica_parallel_workers "https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html#sysvar_replica_parallel_workers") variable's value greater than 0.
- Fixed an issue that can cause high CPU consumption when multiple sessions are trying
  to access a page that doesn't exist in memory.

**Upgrades and migrations:**

- To perform a minor version upgrade for an Aurora global database from Aurora MySQL version 3.01, 3.02 or 3.03 to Aurora MySQL version 3.04 or higher, refer to
  [Upgrading Aurora MySQL by modifying the engine version](../AuroraUserGuide/AuroraMySQL.Updates.Patching.md#AuroraMySQL.Updates.Patching.ModifyEngineVersion "../AuroraUserGuide/AuroraMySQL.Updates.Patching.md#AuroraMySQL.Updates.Patching.ModifyEngineVersion").
- Fixed an issue that can cause upgrade precheck failures due to schema inconsistency errors reported for the `mysql.general_log_backup`, `mysql.general_log`,
  `mysql.slow_log_backup` and `mysql.slow_log` tables when upgrading from Aurora MySQL 2 to Aurora MySQL 3. For more information about upgrade troubleshooting,
  see [Troubleshooting upgrade issues with Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting "../AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.md#AuroraMySQL.mysql80-upgrade-troubleshooting").
- Fixed an issue which can cause major version upgrade failures when upgrading to Aurora MySQL 3 when a trigger definition contains a reserved keyword that is not within quotes.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.28, in addition to the below. For more information, see
[MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3").

- Fixed an issue where a buffer block containing intrinsic temporary table page was relocated during page traversal, causing an assertion failure (Bug# 33715694)
- InnoDB: Prevent online DDL operations from accessing out-of-bounds memory (Bug# 34750489, Bug# 108925)
- Fixed an issue which can sometimes produce incorrect query results while processing complex SQL statements consisting of multiple nested Common Table Expressions (CTEs) (Bug# 34572040, Bug# 34634469, Bug# 33856374)
