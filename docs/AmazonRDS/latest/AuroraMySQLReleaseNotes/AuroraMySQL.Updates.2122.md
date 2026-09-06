

# Aurora MySQL database engine updates 2024-03-19 (version 2.12.2, compatible with MySQL 5.7.44) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2122"></a><a name="2122"></a><a name="2.12.2"></a>

**Version:** 2.12.2

Aurora MySQL 2.12.2 is generally available. Aurora MySQL 2.12 versions are compatible up to MySQL 5.7.44. For more information on community changes, see [Changes in MySQL 5.7.44 (2022-10-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-44.html).

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\* and 3.06.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.2. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.2.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2122.Improvements"></a>

**Fixed security issues and CVEs listed below:**

This release includes all community CVE fixes up to and including MySQL 5.7.44. The following CVE fixes are included:
+ [CVE-2024-20963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-CVE-2024-20963)
+ [CVE-2023-39975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39975)
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)

Security issues:
+ Added a fix that ensures binary log replicas default to using SSL/TLS if the source supports encrypted connections, irrespective of the `MASTER_SSL` setting.

**Availability improvements:**
+ Fixed an issue that can prevent a read replica instance from launching successfully if there is a high workload on the writer instance.
+ Fixed an issue which can cause an Aurora MySQL database writer instance to failover due to a defect in the component that communicates with Aurora storage. The defect occurs as a result of a breakdown in the communication between the database instance and the underlying storage following a software update of the Aurora storage instance.
+ Fixed an issue which, in rare conditions, can cause the reader instances to restart.
+ Fixed an issue in which a privileged user can modify the [resource limits](https://dev.mysql.com/doc/refman/5.7/en/user-resources.html) associated with the user, [rdsadmin](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html). When set incorrectly, these resource limits can impede the RDS monitoring agent's ability to monitor the health of the database instance leading to database unavailability.

**Upgrades and migrations:**
+ Fixed an issue that occurred when attempting to start the binary log replication for Aurora MySQL clusters that had migrated from Amazon RDS MySQL 5.7 and that contained unsupported stored procedures.
+ Disabled the database event scheduler during a major version upgrade to Aurora MySQL version 3. This update helps avoid any changes to the database by the event execution while the major version upgrade is in progress.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2122.Patches"></a>

This release includes all community bug fixes up to and including 5.7.44. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v2).

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2122.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2122.Compatibility"></a>

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