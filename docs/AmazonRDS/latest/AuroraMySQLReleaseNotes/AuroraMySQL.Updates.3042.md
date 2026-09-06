

# Aurora MySQL database engine updates 2024-03-15 (version 3.04.2, compatible with MySQL 8.0.28)
<a name="AuroraMySQL.Updates.3042"></a><a name="3.04.2"></a><a name="3.04.2"></a>

**Version:** 3.04.2

Aurora MySQL 3.04.2 is generally available. Aurora MySQL 3.04 versions are compatible with MySQL 8.0.28. For more information on community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Compare-80-v3.html).

**Note**  <a name="lts_notice_3042"></a>
This version is designated as a long-term support (LTS) release. For more information, see [Aurora MySQL long-term support (LTS) releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.html#AuroraMySQL.Updates.LTS) in the *Amazon Aurora User Guide*.  
We recommend that you don't set the `AutoMinorVersionUpgrade` parameter to `true` (or enable **Auto minor version upgrade** in the AWS Management Console) for LTS versions. Doing so could lead to your DB cluster being upgraded to the next target version for Automatic Minor Version Upgrade campaign, which may not be an LTS version.

Currently supported Aurora MySQL releases are 2.07.9, 2.7.10, 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, and 3.06.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently available Aurora MySQL version 2 cluster into an Aurora MySQL version 3.04.2 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html#AuroraMySQL.mysql80-upgrade-troubleshooting).

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3042.Improvements"></a>

**Fixed security issues and CVEs:**

The following CVE fixes are included in this release:
+ [CVE-2020-11104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11104)
+ [CVE-2020-11105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11105)
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)
+ [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)
+ [CVE-2023-39975](https://nvd.nist.gov/vuln/detail/CVE-2023-39975)

**Availability improvements:**
+ Fixed an issue where a read replica DB instance can't be launched successfully when there's high workload in the writer DB instance.
+ Fixed an issue where an Aurora MySQL writer DB instance can fail over due to a defect in the component that communicates with Aurora storage. The defect occurs as a result of a breakdown in the communication between the DB instance and underlying storage following a software update.
+ Fixed an issue that can cause a database instance restart when running [SHOW STATUS](https://dev.mysql.com/doc/refman/8.0/en/show-status.html) and [PURGE BINARY LOGS](https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html) statements concurrently. `PURGE BINARY LOGS` is a managed statement that is run to honor the user-configured binlog retention period.
+ Fixed an issue that, during the restart of a database instance, can cause an additional restart.
+ Fixed an issue with lock contention caused by an audit logging thread that can lead to high CPU utilization and client application timeouts.
+ Fixed an issue where an Aurora MySQL database instance can experience multiple restarts during instance startup while large rollback segments are initialized.
+ Fixed an issue that can cause a DB instance to restart while running a query that references an aggregate function.

**General improvements:**
+ Fixed an issue that can cause a parallel query to fail due to transient network issues while reading data from the Aurora DB cluster volume 
+ Fixed an issue where the user is unable to interrupt any query or set session timeouts for `performance_schema` queries.
+ Fixed an issue where binary log (binlog) replication configured to use custom SSL certificates ([mysql.rds\_import\_binlog\_ssl\_material](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html#mysql_rds_import_binlog_ssl_material)) could fail when the replication instance is undergoing a host replacement.
+ Fixed an issue related to audit log file management that can cause log files to be inaccessible for download or rotation, and in some cases increase CPU usage.
+ Optimized `AUTO_INCREMENT` key recovery to reduce the completion time for restoring snapshots, performing point-in-time recovery, and cloning DB clusters with large numbers of tables in the database.
+ Fixed an issue where SQL statements referring to some `performance_schema` tables can return an error due to these tables being missing after migrating from Community MySQL to Aurora MySQL versions 3.04.0 and 3.04.1.
+ Fixed an issue where small read replica instances can experience increased replication lag after upgrading from Aurora MySQL versions lower than 2.11.\*.
+ Fixed an issue that can cause duplicate key errors for `AUTO_INCREMENT` columns using descending indices after a snapshot restore, backtrack, or database cloning operation.
+ Fixed an issue that can cause modifications of the `table_open_cache` database parameter not to take effect until the DB instance is restarted.
+ Fixed an issue where the reader DB instance is unable to open a table, with ERROR 1146. This issue occurs when running certain types of online Data Definition Language (DDL) statements while the `INPLACE` algorithm is being used on the writer DB instance.
+ Fixed an issue to avoid an instance restart during Aurora serverless scaling when the internal monitoring process erroneously submits duplicate scaling requests.
+ Fixed an issue that can cause a database restart when connected binary log (binlog) consumers are using duplicate binlog replication server IDs.

**Upgrades and migrations:**
+ Fixed an issue that can cause major version upgrades to Aurora MySQL version 3 to fail due to the presence of orphaned entries for already deleted tablespaces in InnoDB system tables in Aurora MySQL version 2.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3042.Patches"></a>

This release includes all community bug fixes up to and including 8.0.28, in addition to the following. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed an issue where cache line value can be calculated incorrectly, causing a failure during database restart on Graviton-based instances. (Community Bug Fix \#35479763)
+ Repeated running of a stored routine, having as a subquery a SELECT statement containing multiple `AND`, `OR`, or `XOR` conditions, led to excessive consumption and possibly eventual exhaustion of virtual memory. (Community Bug Fix \#33852530)