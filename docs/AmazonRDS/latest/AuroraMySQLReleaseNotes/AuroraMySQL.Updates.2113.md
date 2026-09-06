

# Aurora MySQL database engine updates 2023-06-09 (version 2.11.3, compatible with MySQL 5.7.12) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2113"></a><a name="2113"></a><a name="2.11.3"></a>

 **Version:** 2.11.3 

 Aurora MySQL 2.11.3 is generally available. Aurora MySQL 2.11 versions are compatible with MySQL 5.7.12. For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html). 

 The currently supported Aurora MySQL releases are 2.07.\*, 2.11.\*, 3.01.\*, 3.02.\* and 3.03.\*. 

 You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.11.3. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.11.3. 

 If you upgrade an Aurora MySQL global database to version 2.11.\*, you must upgrade your primary and secondary DB clusters to the exact same version, including the patch level. For more information on upgrading the minor version of an Aurora global database, see [Minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.html#aurora-global-database-upgrade.minor). 

Immediately after an in-place engine version upgrade to Aurora MySQL 2.11.\* is performed, an operating system upgrade is applied automatically to all affected instances on the db.r4, db.r5, db.t2, and db.t3 DB instance classes, if the instances are running an old operating system version. In a Multi-AZ DB cluster, all of the reader instances apply the operating system upgrade first. When the operating system upgrade on the first reader instance is finished, a failover occurs and the previous writer instance is upgraded.

**Note**  
The operating system upgrade isn't applied automatically to Aurora global databases during major version upgrades.

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

**Note**  
 For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2113.Improvements"></a>

**Fixed security issues and CVEs listed below:**
+ Updated the default SSL ciphers used by Aurora MySQL to exclude the less secure `DES-CBC3-SHA` values from the [SSL\_CIPHER](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_ssl_cipher) database parameter. If you encounter SSL connection issues due to the removal of the `DES-CBC3-SHA` cipher, please use an applicable secure cipher from this list, [ConfiguringCipherSuites](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html#AuroraMySQL.Security.SSL.ConfiguringCipherSuites). More information on the MySQL client [Connection Cipher Configuration](https://dev.mysql.com/doc/refman/5.7/en/encrypted-connection-protocols-ciphers.html#encrypted-connection-cipher-configuration) can be found in the MySQL documentation.
+ [CVE-2023-21963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21963)
+ [CVE-2023-21912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21912)
+ [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
+ [CVE-2022-43551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43551)
+ [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)

**Availability improvements:**
+ Fixed an issue in database activity streams (DAS) event encryption which may cause database restarts.
+ Fixed two issues which can cause a database restart to fail if it occurred while executing a Data Definition Language (DDL) query.
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

**General improvements:**
+ Introduced file management performance optimizations on binlog replicas to help reduce contention when writing to relay log files.
+ Fixed an issue where setting the `aurora_disable_hash_join` parameter to 1 or ON might not prevent the optimizer from using a hash join.
+ Fixed an issue that can cause the `buffer_pool_read_requests` counter to be reported incorrectly in the `information_schema` metrics.
+ Fixed an issue that can cause the local storage to fill up when performing `LOAD FROM S3` or `SELECT INTO S3` operations. The issue can also lead to higher CPU utilization, database restarts due to low memory, and increased latency for these queries.

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.2113.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2113.Compatibility"></a>

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