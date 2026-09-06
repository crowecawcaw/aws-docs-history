

# Aurora MySQL database engine updates 2024-10-23 (version 2.12.4, compatible with MySQL 5.7.44) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2124"></a><a name="2124"></a><a name="2.12.4"></a>

**Version:** 2.12.4

Aurora MySQL 2.12.4 is generally available. Aurora MySQL 2.12 versions are compatible up to MySQL 5.7.44. For more information on community changes, see [Changes in MySQL 5.7.44 (2022-10-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-44.html).

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.4. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.4.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2124.Improvements"></a>

**Fixed security issues and CVEs:**

This release includes all community CVE fixes up to and including MySQL 5.7.44. The following CVE fixes are included:
+ [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)
+ [CVE-2024-21142](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21142)
+ [CVE-2024-21177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21177)
+ [CVE-2024-25062](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25062)

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2124.Patches"></a>

This release includes all community bug fixes up to and including 5.7.44. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v2).

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2124.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2124.Compatibility"></a>

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