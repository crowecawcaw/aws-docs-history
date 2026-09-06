

# Aurora MySQL database engine updates 2024-07-19 (version 2.11.6, compatible with MySQL 5.7.12) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2116"></a><a name="2116"></a><a name="2.11.6"></a>

**Version:** 2.11.6

Aurora MySQL 2.11.6 is generally available. Aurora MySQL 2.11 versions are compatible with MySQL 5.7.12. For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html).

The currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.11.6. You can also restore a snapshot from any currently supported lower Aurora MySQL version 2 release into Aurora MySQL 2.11.6.

If you upgrade an Aurora MySQL global database to version 2.11.\*, you must upgrade your primary and secondary DB clusters to the exact same version, including the patch level. For more information on upgrading the minor version of an Aurora global database, see [Minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.html#aurora-global-database-upgrade.minor). 

Immediately after an in-place engine version upgrade to Aurora MySQL 2.11.\* is performed, an operating system upgrade is applied automatically to all affected instances on the db.r4, db.r5, db.t2, and db.t3 DB instance classes, if the instances are running an old operating system version. In a Multi-AZ DB cluster, all of the reader instances apply the operating system upgrade first. When the operating system upgrade on the first reader instance is finished, a failover occurs and the previous writer instance is upgraded.

**Note**  
The operating system upgrade isn't applied automatically to Aurora global databases during major version upgrades.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2116.Improvements"></a>

**Fixed security issues and CVEs:**
+ Fixed a security issue in MySQL stored procedures.

This release includes all community CVE fixes up to and including MySQL 5.7.12. The following CVE fixes are included in this release:
+ [CVE-2023-21912](https://nvd.nist.gov/vuln/detail/CVE-2023-21912)
+ [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545)
+ [CVE-2023-39975](https://nvd.nist.gov/vuln/detail/CVE-2023-39975)
+ [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)
+ [CVE-2024-0853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0853)
+ [CVE-2024-20963](https://nvd.nist.gov/vuln/detail/CVE-2024-20963)
+ [CVE-2024-20993](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20993)
+ [CVE-2024-20998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20998)
+ [CVE-2024-21008](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21008)
+ [CVE-2024-21009](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21009)
+ [CVE-2024-21013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21013)
+ [CVE-2024-21047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21047)
+ [CVE-2024-21054](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21054)
+ [CVE-2024-21055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21055)
+ [CVE-2024-21057](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21057)
+ [CVE-2024-21062](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21062)
+ [CVE-2024-21069](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21069)
+ [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096)
+ [CVE-2024-21097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21097)

**Availability improvements:**
+ Fixed an issue that can cause a database server to restart due to the concurrent access of connection resources during seamless scaling, zero-downtime restart (ZDR), and zero-downtime patching (ZDP).
+ Fixed an issue that can cause a reader DB instance to restart when freeing memory used for log application.
+ Fixed an issue that causes a reader DB instance to restart when running a parallel query.
+ Fixed an issue that can cause a reader DB instance that uses write forwarding to restart when a forwarded [implicit commit statement](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html) encounters an error.

**General improvements:**
+ Fixed an issue that can cause SQL statements to experience unexpected primary key violation errors or warnings on some rows when performing concurrent `INSERT` statements on a table that has an `AUTO_INCREMENT` primary key column and a unique key column, and when an `INSERT` statement has unique key violations on different rows.
+ Fixed an issue that can lead to incorrect query results when ZDR incorrectly restores session variables set as hints in queries.
+ Fixed an issue during Aurora Serverless v1 scaling that causes the DB instance to restart due to incorrect access to an internal data structure while finding a scaling point.
+ Fixed an issue where slow `INSERT`, `DELETE`, and `UPDATE` queries run by the MySQL [Event Scheduler](https://dev.mysql.com/doc/refman/8.0/en/event-scheduler.html) weren't recorded in the slow query log unless preceded by a slow `SELECT` query.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2116.Patches"></a>

This release includes all community bug fixes up to and including 5.7.12. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v2).

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2116.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2116.Compatibility"></a>

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