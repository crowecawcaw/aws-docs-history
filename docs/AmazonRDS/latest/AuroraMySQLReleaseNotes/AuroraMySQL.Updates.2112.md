

# Aurora MySQL database engine updates 2023-03-24 (version 2.11.2, compatible with MySQL 5.7.12) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2112"></a><a name="2112"></a><a name="2.11.2"></a>

 **Version:** 2.11.2 

 Aurora MySQL 2.11.2 is generally available. Aurora MySQL 2.11 versions are compatible with MySQL 5.7.12. For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html). 

 The currently supported Aurora MySQL releases are 2.07.\*, 2.11.\*, 3.01.\*, 3.02.\* and 3.03.\*. 

 You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.11.2. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.11.2. 

 If you upgrade an Aurora MySQL global database to version 2.11.\*, you must upgrade your primary and secondary DB clusters to the exact same version, including the patch level. For more information on upgrading the minor version of an Aurora global database, see [Minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.html#aurora-global-database-upgrade.minor). 

Immediately after an in-place engine version upgrade to Aurora MySQL 2.11.\* is performed, an operating system upgrade is applied automatically to all affected instances on the db.r4, db.r5, db.t2, and db.t3 DB instance classes, if the instances are running an old operating system version. In a Multi-AZ DB cluster, all of the reader instances apply the operating system upgrade first. When the operating system upgrade on the first reader instance is finished, a failover occurs and the previous writer instance is upgraded.

**Note**  
The operating system upgrade isn't applied automatically to Aurora global databases during major version upgrades.

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

**Note**  
 For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2112.Improvements"></a>

**General improvements:**
+ Fixed an issue where DB instances using binary log replication may experience an increase in CPU utilization and connection failures when multiple binary log replication consumers are attached.
+ Fixed an issue that can cause a reader instance in a global database secondary Region to become out of sync after upgrading to Aurora MySQL version 2.11 if the primary database writer is on Aurora MySQL version 2.10.

**Availability improvements:**
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2112.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2112.Compatibility"></a>

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