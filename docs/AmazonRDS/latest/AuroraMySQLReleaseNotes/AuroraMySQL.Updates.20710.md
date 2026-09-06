

# Aurora MySQL database engine updates 2023-08-15 (version 2.07.10) (Deprecated)
<a name="AuroraMySQL.Updates.20710"></a>

**Version:** 2.07.10

Aurora MySQL 2.07.10 is generally available. Aurora MySQL 2.07 versions are compatible with MySQL 5.7.12. For more information on community changes, see [Changes in MySQL 5.7.12 (2016-04-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-12.html).

 Currently supported Aurora MySQL releases are 2.07.\*, 2.11.\*, 3.01.\*, 3.02.\*, 3.03.\*, and 3.04.\*. 

 You can restore a snapshot from a currently supported Aurora MySQL release into Aurora MySQL 2.07.10. You also have the option to upgrade existing Aurora MySQL 2.\* database clusters to Aurora MySQL 2.07.10. In-place upgrade is available for Aurora MySQL 1.\* clusters to Aurora MySQL 2.\* (see [ Upgrading from Aurora MySQL 1.x to 2.x](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Updates.MajorVersionUpgrade.1to2)). It's also available for Aurora MySQL 2.\* clusters to Aurora MySQL 3.\* (see [ Upgrading from Aurora MySQL 2.x to 3.x](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Updates.MajorVersionUpgrade.2to3)). 

Immediately after an in-place engine version upgrade to Aurora MySQL 2.07.10 is performed, an operating system upgrade is applied automatically to all of the affected instances on the db.r4, db.r5, db.t2, and db.t3 DB instance classes, if the instances are running an old operating system version. In a Multi-AZ DB cluster, all of the reader instances apply the operating system upgrade first. When the operating system upgrade on the first reader instance is finished, a failover occurs and the previous writer instance is upgraded.

**Note**  
The operating system upgrade isn't applied automatically to Aurora global databases during major version upgrades.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.20710.Improvements"></a>

 **Fixed security issues and CVEs listed below:** 

 Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below: 
+ [CVE-2023-21963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21963)
+ [CVE-2023-21912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21912)
+ [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
+ [CVE-2022-43551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43551)
+ [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)
+ Fixed an issue where events that were reported while processing audit log rotations might not be written to the audit log.
+ Updated the default SSL ciphers used by Aurora MySQL to exclude the less secure DES-CBC3-SHA values from the [SSL\_CIPHER](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_ssl_cipher) database parameter. If you encounter SSL connection issues due to the removal of the DES-CBC3-SHA cipher, please use an applicable secure cipher from the following information, [Configuring cipher suites for connections to Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html#AuroraMySQL.Security.SSL.ConfiguringCipherSuites).
+ OpenSSL was upgraded to version 1.0.2zh.

 **General improvements:** 
+ Added support for ECDHE-RSA SSL ciphers that use smaller key sizes for encryption.
+ Fixed a memory management issue when executing queries with hash joins.

## Features not supported in Aurora MySQL version 2
<a name="AuroraMySQL.Updates.20710.Compare56"></a>

The following features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Asynchronous key prefetch (AKP).
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.20710.Compatibility"></a>

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