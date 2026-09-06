

# Aurora MySQL database engine updates 2023-05-04 (version 2.07.9) (Deprecated)
<a name="AuroraMySQL.Updates.2079"></a>

**Version:** 2.07.9

Aurora MySQL 2.07.9 is generally available. Aurora MySQL 2.07 versions are compatible with MySQL 5.7.12. For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html).

 Currently supported Aurora MySQL releases are 2.07.\*, 2.11.\*, 3.01.\*, 3.02.\* and 3.03.\*. 

 You can restore a snapshot from a currently supported Aurora MySQL release into Aurora MySQL 2.07.9. You also have the option to upgrade existing Aurora MySQL 2.\* database clusters to Aurora MySQL 2.07.9. In-place upgrade is available for Aurora MySQL 1.\* clusters to Aurora MySQL 2.\* (see [ Upgrading from Aurora MySQL 1.x to 2.x](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Updates.MajorVersionUpgrade.1to2)). It's also available for Aurora MySQL 2.\* clusters to Aurora MySQL 3.\* (see [ Upgrading from Aurora MySQL 2.x to 3.x](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Updates.MajorVersionUpgrade.2to3)). 

Immediately after an in-place engine version upgrade to Aurora MySQL 2.07.9 is performed, an operating system upgrade is applied automatically to all of the affected instances on the db.r4, db.r5, db.t2, and db.t3 DB instance classes, if the instances are running an old operating system version. In a Multi-AZ DB cluster, all of the reader instances apply the operating system upgrade first. When the operating system upgrade on the first reader instance is finished, a failover occurs and the previous writer instance is upgraded.

**Note**  
The operating system upgrade isn't applied automatically to Aurora global databases during major version upgrades.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2079.Improvements"></a>

 **Fixed security issues and CVEs listed below:** 

 Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below: 
+ [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)

 **Availability improvements:** 
+ Fixed an issue where the Advanced Audit log rotation may reduce the freeable memory, which could lead to the DB instance restarting.
+ Fixed an issue which can occur during database restarts and results in the database not starting up successfully for an extended duration.

 **General improvements:** 
+ Fixed an issue which, in rare conditions, can cause the instances to restart when the database volume grows to a multiple of 160GB.

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2079.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Asynchronous key prefetch (AKP).
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2079.Compatibility"></a>

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