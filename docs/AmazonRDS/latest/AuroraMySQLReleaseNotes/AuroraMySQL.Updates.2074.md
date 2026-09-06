

# Aurora MySQL database engine updates 2021-03-04 (version 2.07.4) (Deprecated)
<a name="AuroraMySQL.Updates.2074"></a>

**Version:** 2.07.4

Aurora MySQL 2.07.4 is generally available. Aurora MySQL 2.\* versions are compatible with MySQL 5.7 and Aurora MySQL 1.\* versions are compatible with MySQL 5.6.

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*. 

 You can restore a snapshot from a currently supported Aurora MySQL release into Aurora MySQL 2.07.4. You also have the option to upgrade existing Aurora MySQL 2.\* database clusters to Aurora MySQL 2.07.4. You can't upgrade an existing Aurora MySQL 1.\* cluster directly to 2.07.4; however, you can restore its snapshot to Aurora MySQL 2.07.4. 

 To create a cluster with an older version of Aurora MySQL, please specify the engine version through the AWS Management Console, the AWS CLI, or the RDS API. 

**Note**  <a name="lts_notice_2074"></a>
 This version is designated as a long-term support (LTS) release. For more information, see [ Aurora MySQL long-term support (LTS) releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Versions.html#AuroraMySQL.Updates.LTS) in the *Amazon Aurora User Guide*. 

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2074.Improvements"></a>

 **Security fixes:** 
+ [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812)
+ [CVE-2020-14793](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14793)
+ [CVE-2020-14790](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14790)
+ [CVE-2020-14775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14775)
+ [CVE-2020-14769](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14769)
+ [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765)
+ [CVE-2020-14760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14760)
+ [CVE-2020-14672](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14672)
+ [CVE-2020-1971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1971)

 **Availability improvements:** 
+  Fixed an issue that could cause a client to hang in case of a network error while reading or writing a network packet. 
+  Improved engine restart times in some cases after interrupted DDL. 
+  Fixed an issue where a DDL or DML could cause engine restart during a page prefetch request. 
+  Fixed an issue where a replica could restart while performing a reverse scan of a table/index on an Aurora Read Replica. 
+  Fixed an issue in clone cluster operation that could cause the clone to take longer. 
+  Fixed an issue that could cause a restart of a database when using parallel query optimization for geospatial columns. 
+  Fixed an issue that caused a binlog replica to stop with an `HA_ERR_KEY_NOT_FOUND` error. 

## Integration of MySQL community edition bug fixes
<a name="AuroraMySQL.Updates.2074.Patches"></a>
+  Fixed an issue in the Full-text ngram parser when dealing with tokens containing ' ' (space), '%', or ','. Customers should rebuild their FTS indexes if using ngram parser. (Bug \#25873310) 
+  Fixed an issue that could cause engine restart during query execution with nested SQL views. (Bug \#27214153, Bug \#26864199) 

## Comparison with Aurora MySQL version 1
<a name="AuroraMySQL.Updates.2074.Compare56"></a>

The following Amazon Aurora MySQL features are supported in Aurora MySQL Version 1 (compatible with MySQL 5.6), but these features are currently not supported in Aurora MySQL Version 2 (compatible with MySQL 5.7).
+ Asynchronous key prefetch (AKP). For more information, see [ Optimizing Aurora indexed join queries with asynchronous key prefetch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.AKP) in the *Amazon Aurora User Guide*. 
+ Hash joins. For more information, see [ Optimizing large Aurora MySQL join queries with hash joins](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.HashJoin) in the *Amazon Aurora User Guide*.
+ Native functions for synchronously invoking AWS Lambda functions. For more information, see [ Invoking a Lambda function with an Aurora MySQL native function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html#AuroraMySQL.Integrating.NativeLambda) in the *Amazon Aurora User Guide*.
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).
+ Migrating data from MySQL using an Amazon S3 bucket. For more information, see [ Migrating data from MySQL by using an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3) in the *Amazon Aurora User Guide*.

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2074.Compatibility"></a>

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