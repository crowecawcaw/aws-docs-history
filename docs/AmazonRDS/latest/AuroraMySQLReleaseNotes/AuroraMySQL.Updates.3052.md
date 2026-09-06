

# Aurora MySQL database engine updates 2024-01-31 (version 3.05.2) (Deprecated)
<a name="AuroraMySQL.Updates.3052"></a><a name="3.05.2"></a>

**Version:** 3.05.2

Aurora MySQL 3.05.2 is generally available. Aurora MySQL 3.05 versions are compatible with MySQL 8.0.32. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

Currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, and 3.05.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.05.2 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3052.Improvements"></a>

**Fixed security issues and CVEs:**

The following CVE fixes are included in this release:
+ [CVE-2020-11104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11104)
+ [CVE-2020-11105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11105)
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)
+ [CVE-2023-39975](https://nvd.nist.gov/vuln/detail/CVE-2023-39975)

**Availability improvements:**
+ Fixed an issue where processing `INSERT` queries on InnoDB partitioned tables can cause a gradual decline of free memory in the instance.
+ Fixed an issue that can cause a database instance restart when running [SHOW STATUS](https://dev.mysql.com/doc/refman/8.0/en/show-status.html) and [PURGE BINARY LOGS](https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html) statements concurrently. `PURGE BINARY LOGS` is a managed statement that is run to honor the user-configured binlog retention period.
+ Fixed an issue that can cause the server to unexpectedly close after running Data Manipulation Language (DML) statements on a table whose nonvirtual columns were reordered with a `MODIFY COLUMN` or `CHANGE COLUMN` statement.
+ Fixed an issue that, during the restart of a database instance, can cause an additional restart.

**General improvements:**
+ Fixed an issue where the user is unable to interrupt any query or set session timeouts for `performance_schema` queries.
+ Fixed an issue where binary log (binlog) replication setup using custom SSL certificates ([mysql.rds\_import\_binlog\_ssl\_material](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html#mysql_rds_import_binlog_ssl_material)) could fail when the replication instance is undergoing a host replacement.
+ Fixed an issue related to audit log file management that can cause log files to be inaccessible for download or rotation, and in some cases increase CPU usage.
+ In Aurora MySQL versions lower than 3.05.2, users are unable to retrieve the output of `SHOW ENGINE INNODB STATUS` on Aurora MySQL reader DB instances. This is due to the [default InnoDB behavior](https://dev.mysql.com/doc/refman/8.0/en/innodb-read-only-instance.html) when `innodb_read_only` is enabled.

  In Aurora MySQL version 3.05.2 and higher, when `SHOW ENGINE INNODB STATUS` is run on a reader instance, the output is written to the MySQL error log, allowing for easier troubleshooting.

  For more information on working with MySQL error logs, see [Aurora MySQL error logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.MySQL.LogFileSize.html#USER_LogAccess.MySQL.Errorlog). For more information on `SHOW ENGINE INNODB STATUS`, see [SHOW ENGINE statement](https://dev.mysql.com/doc/refman/8.0/en/show-engine.html) in the MySQL documentation.

**Upgrades and migrations:**
+ Fixed an issue that can cause upgrade failures from Aurora MySQL version 2 to Aurora MySQL version 3 when there is a user-defined `FTS_DOC_ID` column present in the table schema.
+ Fixed an issue that can cause upgrade failures from Aurora MySQL version 2 to Aurora MySQL version 3 due to a synchronization issue while processing InnoDB tablespaces.
+ Fixed an issue that can cause major version upgrades to Aurora MySQL version 3 to fail due to the presence of orphaned entries for already deleted tablespaces in InnoDB system tables in Aurora MySQL version 2.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3052.Patches"></a>

This release includes all community bug fixes up to and including 8.0.32, in addition to the following. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed an issue where `records_in_range` performed an excessive number of disk reads for `INSERT` operations, leading to a gradual decline in performance. (Community Bug Fix \#34976138)