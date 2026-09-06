

# Aurora MySQL database engine updates 2024-03-07 (version 3.06.0) (Deprecated)
<a name="AuroraMySQL.Updates.3060"></a><a name="3.06.0"></a><a name="3.06.0"></a>

**Version:** 3.06.0

Aurora MySQL 3.06.0 is generally available. Aurora MySQL 3.06 versions are compatible with MySQL 8.0.34. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

Currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, and 3.06.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.06.0 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## New features
<a name="AuroraMySQL.Updates.3060.New"></a>
+ Aurora MySQL version 3.06.0 supports Amazon Bedrock integration and introduces the new reserved keywords `accept`, `aws_bedrock_invoke_model`, `aws_sagemaker_invoke_endpoint`, `content_type`, and `timeout_ms`. Check the object definitions for the usage of the new reserved keywords before upgrading to version 3.06.0. To mitigate the conflict with the new reserved keywords, quote the reserved keywords used in the object definitions. For more information on the Amazon Bedrock integration and handling the reserved keywords, see [What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) in the *Amazon Aurora User Guide*. For additional information, see [Keywords and Reserved Words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html), [The INFORMATION\_SCHEMA KEYWORDS Table](https://dev.mysql.com/doc/refman/8.0/en/information-schema-keywords-table.html), and [Schema Object Names](https://dev.mysql.com/doc/refman/8.0/en/identifiers.html) in the MySQL documentation.
+ Improved performance for binary log replicas when replicating transactions for large tables with more than one secondary index. This feature introduces a thread pool to apply secondary index changes in parallel on a binlog replica. The feature is controlled by the `aurora_binlog_replication_sec_index_parallel_workers` DB cluster parameter, which controls the total number of parallel threads available to apply the secondary index changes. For more information, see [Optimizing binary log replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.html#binlog-optimization) in the *Amazon Aurora User Guide*.
+ Added a new stored procedure `mysql.rds_set_read_only` that allows changing the value of the global system variable `read_only` on database instances in your Aurora MySQL cluster. For more information, see [Replicating](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html) in the *Amazon Aurora User Guide*.
+ Added a new stored procedure `mysql.rds_set_binlog_source_ssl` that allows setting the encryption on a binary log replica by specifying a value for `SOURCE_SSL`. For more information, see [Replicating](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html) in the *Amazon Aurora User Guide*.
+ [Amazon Aurora Machine Learning](https://aws.amazon.com/rds/aurora/machine-learning) is an optimized integration between the Aurora MySQL database and AWS machine learning (ML) services. [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is now supported, allowing you to invoke machine learning models in Amazon Bedrock directly from your Aurora MySQL DB cluster using SQL. For more information on using Amazon Bedrock with your Aurora MySQL DB cluster, see [Using Amazon Aurora machine learning with Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-ml.html) in the *Amazon Aurora User Guide*.
+ Aurora MySQL version 3.06 adds support for [automated undo tablespace truncation](https://dev.mysql.com/doc/refman/8.0/en/innodb-undo-tablespaces.html#truncate-undo-tablespace). This optimization allows you to reclaim unused space in undo tablespaces after the undo logs have been purged.

## Improvements
<a name="AuroraMySQL.Updates.3060.Improvements"></a>

**Fixed security issues and CVEs:**

The following CVE fixes are included in this release:
+ [CVE-2020-11104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11104)
+ [CVE-2020-11105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11105)
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)
+ [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)
+ [CVE-2023-39975](https://nvd.nist.gov/vuln/detail/CVE-2023-39975)

**Availability improvements:**
+ Fixed an issue where a read replica DB instance can't be launched successfully when there's high workload in the writer DB instance.
+ Fixed an issue where an Aurora MySQL writer DB instance can fail over due to a defect in communication with Aurora storage. The defect occurs as a result of a breakdown in the communication between the DB instance and underlying storage following a software update of the Aurora storage instance.
+ Fixed an issue when processing `INSERT` queries on InnoDB partitioned tables that can cause a gradual decline of free memory in the instance.
+ Fixed an issue that can cause an Aurora MySQL DB instance to restart or fail over due to a decrease in freeable memory when hash join is used while running queries.
+ Fixed an issue that can cause a database instance restart when running [SHOW STATUS](https://dev.mysql.com/doc/refman/8.0/en/show-status.html) and [PURGE BINARY LOGS](https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html) statements concurrently. `PURGE BINARY LOGS` is a managed statement that is run to honor the user-configured binlog retention period.
+ Fixed an issue that can cause the server to unexpectedly close after running Data Manipulation Language (DML) statements on a table whose nonvirtual columns were reordered with a `MODIFY COLUMN` or `CHANGE COLUMN` statement.
+ Fixed an issue that, during the restart of a database instance, can cause an additional restart.
+ Fixed an issue that can cause a database restart when a cascading `UPDATE` or `DELETE` foreign key constraint is defined on a table where a virtual column is involved either as a column in the foreign key constraint, or as a member of the referenced table.
+ In Aurora MySQL 2.10, we added support for rebooting an Aurora DB cluster with read availability. This feature allows reader DB instances to stay online while a writer DB instance is rebooted. This feature is now supported on secondary AWS Regions in Aurora MySQL global databases, ensuring that you can still serve read requests during a writer instance restart on the primary cluster. Previously, when a writer instance restarted, all reader instances in an Aurora MySQL secondary cluster also restarted. With this release, secondary cluster reader instances continue to serve read requests during a writer instance restart, improving read availability in the cluster. For more information, see [Rebooting an Aurora cluster with read availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_RebootCluster.html#aurora-mysql-survivable-replicas).
+ Fixed an issue that can interrupt database recovery during startup if the restart occurred while running heavy insert operations involving `AUTO_INCREMENT` columns.

**General improvements:**
+ Fixed an issue that can cause a parallel query to fail due to transient network issues while reading data from the Aurora cluster volume.
+ Fixed an issue where the user is unable to interrupt any query or set session timeouts for `performance_schema` queries.
+ Fixed an issue where binary log (binlog) replication configured to use custom SSL certificates ([mysql.rds\_import\_binlog\_ssl\_material](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html#mysql_rds_import_binlog_ssl_material)) could fail when the replication instance is undergoing a host replacement.
+ Small DB instances with less than or equal to 4 GiB of memory now close the top memory-consuming connections when the DB instance is under memory pressure. You can also tune the buffer pool to decrease its size. For more information, see [Amazon Aurora MySQL out-of-memory issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting-workload.html#AuroraMySQLOOM) in the *Amazon Aurora User Guide*.
+ Changed the default response for `aurora_oom_response`, on all DB instance classes that have more than 4 GiB of memory, from empty to `print`. For more information, see [Amazon Aurora MySQL out-of-memory issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting-workload.html#AuroraMySQLOOM) in the *Amazon Aurora User Guide*.
+ Fixed an issue related to audit log file management that can cause log files to be inaccessible for download or rotation, and in some cases increase CPU usage.
+ Optimized `AUTO_INCREMENT` key recovery to reduce the completion time for restoring snapshots, performing point-in-time recovery, and cloning DB clusters with large numbers of tables in the database.
+ Fixed an issue where the [wait/io/redo\_log\_flush](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.io-auredologflush.html) event wasn't shown in the Performance Schema [wait event summary tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-wait-summary-tables.html).
+ Added the `Aurora_lockmgr_memory_used` and `Aurora_lockmgr_buffer_pool_memory_used` metrics to track the lock manager's memory usage. For more information, see [Aurora MySQL global status variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html#AuroraMySQL.Reference.GlobalStatusVars) in the *Amazon Aurora User Guide*.
+ Fixed an issue where small read replica instances can experience increased replication lag after upgrading from Aurora MySQL versions lower than 2.11.\*.
+ Fixed an issue that can cause duplicate key errors for `AUTO_INCREMENT` columns using descending indices after a snapshot restore, backtrack, or database cloning operation.
+ Fixed an issue where a `SELECT` query on an Aurora reader instance might fail with the error table doesn't exist when the table has at least one full-text search (FTS) index and a `TRUNCATE` statement is being run on the Aurora writer DB instance.
+ Fixed an issue that can cause an incomplete result set when running queries involving `LEFT JOIN` or `RIGHT JOIN` operations using the hash join algorithm with parallel query.

**Upgrades and migrations:**
+ Fixed an issue that can cause major version upgrades to fail if there is a user-defined `FTS_DOC_ID` column present in the table schema.
+ Fixed an issue that can cause upgrade failures from Aurora MySQLversion 2 to Aurora MySQL version 3 due to a synchronization issue while processing InnoDB tablespaces.
+ Fixed an issue that can cause major version upgrades to Aurora MySQL version 3 to fail due to the presence of orphaned entries for already deleted tablespaces in InnoDB system tables in Aurora MySQL version 2.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3060.Patches"></a>

This release includes all community bug fixes up to and including 8.0.34, in addition to the following. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed an issue where cache line value can be calculated incorrectly, causing a failure during database restart on Graviton-based instances. (Community Bug Fix \#35479763)
+ Fixed an issue where some instances of subqueries within stored routines were not always handled correctly. (Community Bug Fix \#35377192)
+ Fixed an issue that can cause higher CPU usage due to background TLS certificate rotation (Community Bug Fix \#34284186).
+ Fixed an issue where InnoDB allowed the addition of `INSTANT` columns to tables in the MySQL system schema in Aurora MySQL versions lower than 3.05, which could lead to the server unexpectedly closing (database instance restarting) after upgrading to Aurora MySQL version 3.05.0. (Community Bug Fix \#35625510).