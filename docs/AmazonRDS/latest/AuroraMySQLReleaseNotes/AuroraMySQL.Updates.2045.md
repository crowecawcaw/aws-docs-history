

# Aurora MySQL database engine updates 2019-07-08 (version 2.04.5) (Deprecated)
<a name="AuroraMySQL.Updates.2045"></a>

**Version:** 2.04.5

Aurora MySQL 2.04.5 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7 and Aurora MySQL 1.x versions are compatible with MySQL 5.6.

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*. 

 You have the option to upgrade existing Aurora MySQL 2.\* database clusters to Aurora MySQL 2.04.5. We do not allow in-place upgrade of Aurora MySQL 1.\* clusters. This restriction will be lifted in a later Aurora MySQL 2.\* release. You can restore snapshots of Aurora MySQL 1.14.\*, 1.15.\*, 1.16.\*, 1.17.\*, 1.18.\*, 1.19.\*, 2.01.\*, 2.02.\*, 2.03.\* and 2.04.\* into Aurora MySQL 2.04.5. 

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2045.Improvements"></a>

 **Security fixes:** 
+ [CVE-2016-3518](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3518)

 **General fixes:** 
+  Fixed a race condition during storage volume growth that caused the database to restart. 
+  Fixed an internal communication failure during volume open that caused the database to restart. 
+  Added DDL recovery support for `ALTER TABLE ALGORITHM=INPLACE` on partitioned tables. 
+  Fixed an issue with DDL recovery of `ALTER TABLE ALGORITHM=COPY` that caused the database to restart. 
+  Improved Aurora Replica stability under heavy delete workload on the writer. 
+  Fixed a database restart caused by a deadlatch between the thread performing full-text search index sync and the thread performing eviction of full-text search table from dictionary cache. 
+  Fixed a stability issue on the binlog worker during DDL replication while the connection to the binlog master is unstable. 
+  Fixed an out-of-memory issue in the full-text search code that caused the database to restart. 
+  Fixed an issue on the Aurora Writer that caused it to restart when the entire 64 tebibyte (TiB) volume is used. 
+  Fixed a race condition in the Performance Schema feature that caused the database to restart. 
+  Fixed an issue that caused aborted connections when handling an error in network protocol management. 

## Comparison with Aurora MySQL version 1
<a name="AuroraMySQL.Updates.2045.Compare56"></a>

The following Amazon Aurora MySQL features are supported in Aurora MySQL Version 1 (compatible with MySQL 5.6), but these features are currently not supported in Aurora MySQL Version 2 (compatible with MySQL 5.7).
+ Asynchronous key prefetch (AKP). For more information, see [ Optimizing Aurora indexed join queries with asynchronous key prefetch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.AKP) in the *Amazon Aurora User Guide*. 
+ Hash joins. For more information, see [ Optimizing large Aurora MySQL join queries with hash joins](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.HashJoin) in the *Amazon Aurora User Guide*.
+ Native functions for synchronously invoking AWS Lambda functions. For more information, see [ Invoking a Lambda function with an Aurora MySQL native function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html#AuroraMySQL.Integrating.NativeLambda) in the *Amazon Aurora User Guide*.
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).
+ Migrating data from MySQL using an Amazon S3 bucket. For more information, see [ Migrating data from MySQL by using an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3) in the *Amazon Aurora User Guide*.

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2045.Compatibility"></a>

Aurora MySQL 2.04.5 is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes, and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver >20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

Aurora MySQL 2.04.5 does not currently support the following MySQL 5.7 features:
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