

# Aurora MySQL database engine updates 2022-04-20 (version 3.02.0) (Deprecated)
<a name="AuroraMySQL.Updates.3020"></a><a name="3.02.0"></a><a name="3.02.0"></a>

 **Version:** 3.02.0 

 Aurora MySQL 3.02.0 is generally available. Aurora MySQL 3.02 versions are compatible with MySQL 8.0.23, Aurora MySQL 2.x versions are compatible with MySQL 5.7, and Aurora MySQL 1.x versions are compatible with MySQL 5.6. 

 For details of new features in Aurora MySQL version 3 and differences between Aurora MySQL version 3 and Aurora MySQL version 2 or community MySQL 8.0, see [ Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.Compare-v2-v3) in the *Amazon Aurora User Guide*. 

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*. 

 You can restore a snapshot from any currently supported Aurora MySQL version 2 cluster into Aurora MySQL 3.02.0. 

 For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For the upgrade procedure itself, see [ Upgrading to Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-upgrade-procedure) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-upgrade-troubleshooting). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3020.Improvements"></a>

 Aurora MySQL version 3.02.0 is generally available and generally compatible with community MySQL 8.0.23. 

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below:
+ [CVE-2021-22946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22946)

 **New features:** 
+ Amazon Aurora serverless is generally available. For more information, see the [Amazon Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/) overview, [blog](https://aws.amazon.com/blogs/aws/amazon-aurora-serverless-v2-is-generally-available-instant-scaling-for-demanding-workloads/), and [Using Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) documentation. Get started today by creating an Aurora serverless database using only a few steps in the AWS Management Console.

**Availability improvements:**
+ Fixed an issue that can cause the server to potentially go into a restart loop and cause unavailability while deleting a record or dropping a table containing two or more variable-length columns (VARCHAR, VARBINARY, BLOB, and TEXT types). For more details about column types, see [innodb-row-format](https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html).
+ Fixed an issue where existing connections timeout and new connections could not be established on a cluster with Binary Log turned on and has at least one Binary Log consumer attached that results in resource contention between the application and the consumer(s).
+ Freeable memory is indicated by the `FreeableMemory` CloudWatch metric. For more information, see [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Monitoring.Metrics.html).
  + Fixed an issue that can cause a DB instance restart or a failover due to a decrease in freeable memory when binary log replication is enabled.
  + Fixed an issue that can cause a DB instance restart or a failover due to a decrease in freeable memory when setting session variables.
  + Fixed an issue that can cause a DB instance restart or a failover due to a decrease in freeable memory when the database process opens an existing file.
+ Fixed an issue which, in rare conditions, can cause a duplicate entry error when inserting new rows into a table containing an `AUTO_INCREMENT` column on a cluster restored from snapshot.
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

**General improvements:**
+ Fixed an issue where the volume status was not shown when using the `SHOW VOLUME STATUS` command. For more information, see [AuroraMySQL.Managing.VolumeStatus](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.VolumeStatus.html).
+ Fixed an issue that caused calls to [mysql\_rds\_import\_binlog\_ssl\_material](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_import_binlog_ssl_material.html) to fail with [MySQL server ERROR 3512](https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html#error_er_sp_load_failed).
+ Fixed an issue where Aurora replica lag is incorrectly reported for deleted Aurora reader instances.

**Upgrades/Migration:**
+ Fixed an issue that can cause migration failures of MySQL 8.0.x databases to Aurora MySQL version 3 due to an issue in copying ibdata files and tablespaces to Aurora storage.
+ Fixed an issue which can cause upgrades of clusters from Aurora MySQL version 2 to Aurora MySQL version 3 to fail when database tables contained a large amount of data.
+ Fixed an issue that can cause failures when restoring clusters from Aurora MySQL version 2 to Aurora MySQL version 3 due to a failure in creating [serialized data dictionary information](https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_serialized_dictionary_information) (SDI) for a table.
+ Fixed an issue that can cause upgrade failures from Aurora MySQL version 2 to Aurora MySQL version 3 due to schema inconsistency errors reported by upgrade prechecks for RDS system tables.
+ Fixed an issue that can cause failures when migrating or restoring from RDS for MySQL 8.0 or Aurora MySQL version 2 to Aurora MySQL version 3 databases due to invalid syntax in an RDS managed stored procedure.
+ Fixed an issue that can cause upgrade failures from Aurora MySQL 2 to Aurora MySQL 3 due to schema inconsistency errors reported by upgrade prechecks for the [general log](https://dev.mysql.com/doc/refman/5.7/en/query-log.html) and [slow log](https://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html) tables.

## Integration of MySQL community edition bug fixes
<a name="AuroraMySQL.Updates.3020.Patches"></a>

This release includes all community bug fixes up to and including 8.0.23, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed the improper handling of temporary tables used for cursors within stored procedures that could result in unexpected server behavior, [mysqld-8-0-24-bug](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-24.html#mysqld-8-0-24-bug). (Bug \#32416811) 