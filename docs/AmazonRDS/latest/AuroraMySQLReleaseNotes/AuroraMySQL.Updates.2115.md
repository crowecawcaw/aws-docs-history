

# Aurora MySQL database engine updates 2024-03-26 (version 2.11.5, compatible with MySQL 5.7.12) - RDS Extended Support version (Default)
<a name="AuroraMySQL.Updates.2115"></a><a name="2115"></a><a name="2.11.5"></a>

**Version:** 2.11.5

Aurora MySQL 2.11.5 is generally available. Aurora MySQL 2.11 versions are compatible with MySQL 5.7.12. For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html).

Version 2.11.5 is the current default version for Aurora MySQL version 2 when you create a DB cluster. For more information, see [Default Amazon Aurora versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.html#Aurora.VersionPolicy.DefaultVersions).

The currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, 3.04.\*, 3.05.\*, and 3.06.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.11.5. You can also restore a snapshot from any currently supported lower Aurora MySQL version 2 release into Aurora MySQL 2.11.5.

If you upgrade an Aurora MySQL global database to version 2.11.\*, you must upgrade your primary and secondary DB clusters to the exact same version, including the patch level. For more information on upgrading the minor version of an Aurora global database, see [Minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.html#aurora-global-database-upgrade.minor). 

Immediately after an in-place engine version upgrade to Aurora MySQL 2.11.\* is performed, an operating system upgrade is applied automatically to all affected instances on the db.r4, db.r5, db.t2, and db.t3 DB instance classes, if the instances are running an old operating system version. In a Multi-AZ DB cluster, all of the reader instances apply the operating system upgrade first. When the operating system upgrade on the first reader instance is finished, a failover occurs and the previous writer instance is upgraded.

**Note**  
The operating system upgrade isn't applied automatically to Aurora global databases during major version upgrades.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2115.Improvements"></a>

**Fixed security issues and CVEs:**

The following CVE fixes are included in this release:
+ [CVE-2020-11104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11104)
+ [CVE-2020-11105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11105)
+ [CVE-2023-22015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22015)
+ [CVE-2023-22026](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22026)
+ [CVE-2023-22028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22028)
+ [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084)
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)
+ [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)
+ [CVE-2024-20963](https://nvd.nist.gov/vuln/detail/CVE-2024-20963)

**Availability improvements:**
+ Fixed an issue where an Aurora MySQL writer DB instance can fail over due to a defect in the component that communicates with Aurora storage. The defect occurs as a result of a breakdown in the communication between the DB instance and underlying storage following a software update.
+ Fixed an issue that, in rare conditions, can cause the reader DB instances to restart.
+ Fixed an issue with lock contention caused by an audit logging thread that can lead to high CPU utilization and client application timeouts.

**General improvements:**
+ Fixed an issue that can cause a parallel query to fail due to transient network issues while reading data from the Aurora DB cluster volume.
+ Fixed an issue related to audit log file management that can cause log files to be inaccessible for download or rotation, and in some cases increase CPU usage.
+ Fixed an issue that can produce an incorrect value of the `Threads_running` variable in the `information_schema` and `performance_schema` global status tables when using write forwarding.

**Upgrades and migrations:**
+ Fixed an issue that prevented initiation of binary log replication on Aurora MySQL DB clusters migrated from RDS for MySQL 5.7.
+ Disabled the database event scheduler during major version upgrades to Aurora MySQL version 3. This helps avoid any changes to the database by event execution while the major version upgrade is in progress.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2115.Patches"></a>

This release includes all community bug fixes up to and including 5.7.12, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v2).

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2115.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2115.Compatibility"></a>

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