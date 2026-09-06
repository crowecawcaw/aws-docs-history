

# Aurora MySQL database engine updates 2024-07-09 (version 2.12.3, compatible with MySQL 5.7.44) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2123"></a><a name="2123"></a><a name="2.12.3"></a>

**Version:** 2.12.3

Aurora MySQL 2.12.3 is generally available. Aurora MySQL 2.12 versions are compatible up to MySQL 5.7.44. For more information on community changes, see [Changes in MySQL 5.7.44 (2022-10-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-44.html).

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.3. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.3.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2123.Improvements"></a>

**Fixed security issues and CVEs:**
+ Fixed a security issue for MySQL stored procedures.

This release includes all community CVE fixes up to and including MySQL 5.7.44. The following CVE fixes are included:
+ [CVE-2023-21912](https://nvd.nist.gov/vuln/detail/CVE-2023-21912)
+ [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)
+ [CVE-2024-0853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0853)
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
+ Fixed an issue that causes an Aurora MySQL DB instance to restart when running a parallel query.
+ Fixed an issue that can cause a database server to restart due to the concurrent access of connection resources during seamless scaling, zero downtime restart (ZDR), and zero downtime patching (ZDP).
+ Fixed an issue that can cause a reader DB instance to restart when freeing memory used for log application.
+ Fixed an issue in a background process that caused prolonged or failed running of queries while the background operation drops temporary indexes.
+ Fixed an issue with startup routines that can cause writer DB instances to restart due to metadata inconsistency.
+ Added an indicator for transaction recovery progress. This avoids potential unavailability, in rare situations, when transaction recovery takes a long time to complete.
+ Fixed an issue that can cause a reader DB instance to restart when reading a table that is being altered or dropped on the writer DB instance.
+ Fixed an issue where a low `thread_stack` parameter value caused the database to restart repeatedly. The minimum allowed `thread_stack` value has been increased from 131,072 to 136,192 to ensure successful booting and prevent startup issues.
+ Fixed an issue that causes a reader DB instance to restart when running a parallel query.
+ Fixed an issue that can cause Aurora read replicas to restart in the event of certain rare transaction commit orders on the writer DB instance.
+ Fixed an issue that, in rare cases, can cause a DB instance to restart when a read-only transaction obtains shared locks.
+ Fixed an issue that can cause a reader DB instance that uses write forwarding to restart when a forwarded [implicit commit statement](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html) encounters an error.

**General improvements:**
+ Fixed an issue that can cause SQL statements to experience unexpected primary key violation errors or warnings on some rows when performing concurrent `INSERT` statements on a table that has an `AUTO_INCREMENT` primary key column and a unique key column, and when an `INSERT` statement has unique key violations on different rows.
+ Fixed an issue that can lead to incorrect query results when ZDR incorrectly restores session variables set as hints in queries.
+ Fixed an issue in parallel query that causes an incomplete result set to be returned when using the built-in `LPAD` and `RPAD` string functions.
+ Fixed an issue that causes missing foreign key indexes on reader DB instances when an `ALTER TABLE RENAME COLUMN` statement is run on the writer DB instance against a table with a foreign key.
+ Fixed an issue that can cause failure in completing the process of disabling write forwarding.
+ Fixed an issue during Aurora Serverless v1 scaling that causes the DB instance to restart due to incorrect access to an internal data structure while finding a scaling point.
+ Fixed an issue where the Performance Schema wasn't enabled when Performance Insights automated management was turned on for db.t4g.medium and db.t4g.large DB instances.
+ The request timeout for [Aurora machine learning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-ml.html) operations to Amazon SageMaker AI has been increased from 3 to 30 seconds. This helps resolve an issue where customers might see an increased number of retries or failures for requests to Amazon SageMaker AI from Aurora machine learning when using larger batch sizes.
+ Fixed an issue where slow `INSERT`, `DELETE`, and `UPDATE` queries run by the MySQL [Event Scheduler](https://dev.mysql.com/doc/refman/8.0/en/event-scheduler.html) weren't recorded in the slow query log unless preceded by a slow `SELECT` query.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2123.Patches"></a>

This release includes all community bug fixes up to and including 5.7.44. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v2).
+ Fixed an issue where temporary tables bound to triggers while running statements could cause an unexpected DB engine restart.
+ Fixed a defect that can cause the server to exit when single-table `UPDATE` and `DELETE` statements using indexed expressions are run as prepared statements. ([Bug \#29257254](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-17.html))

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2123.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2123.Compatibility"></a>

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