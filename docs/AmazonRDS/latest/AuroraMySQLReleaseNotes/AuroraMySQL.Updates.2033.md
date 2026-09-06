

# Aurora MySQL database engine updates 2019-01-18 (version 2.03.3) (Deprecated)
<a name="AuroraMySQL.Updates.2033"></a>

**Version:** 2.03.3

Aurora MySQL 2.03.3 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7 and Aurora MySQL 1.x versions are compatible with MySQL 5.6.

When creating a new Aurora MySQL DB cluster (including restoring a snapshot), you can choose compatibility with either MySQL 5.7 or MySQL 5.6.

We don't allow in-place upgrade of Aurora MySQL 1.\* clusters into Aurora MySQL 2.03.3 or restore to Aurora MySQL 2.03.3 from an Amazon S3 backup. We plan to remove these restrictions in a later Aurora MySQL 2.\* release.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

**Note**  
 This version is currently not available in the AWS GovCloud (US-West) [us-gov-west-1] and China (Beijing) [cn-north-1] regions. There will be a separate announcement once it is made available. 

**Note**  
The procedure to upgrade your DB cluster has changed. For more information, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.2033.Improvements"></a>

 **CVE fixes** 
+ [CVE-2016-5436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-5436)

 **Critical fixes:** 
+  Fixed an issue where an Aurora Replica might become dead-latched when running a backward scan on an index. 
+  Fixed an issue where an Aurora Replica might restart when the Aurora primary instance runs in-place DDL operations on partitioned tables. 
+  Fixed an issue where an Aurora Replica might restart during query cache invalidation after a DDL operation on the Aurora primary instance. 
+  Fixed an issue where an Aurora Replica might restart during a `SELECT` query on a table while the Aurora primary instance runs truncation on that table. 
+  Fixed a wrong result issue with MyISAM temporary tables where only indexed columns are accessed. 
+  Fixed an issue in slow logs that generated incorrect large values for `query_time` and `lock_time` periodically after approximately 40,000 queries. 
+  Fixed an issue where a schema named "tmp" could cause migration from RDS for MySQL to Aurora MySQL to become stuck. 
+  Fixed an issue where the audit log might have missing events during log rotation. 
+  Fixed an issue where the Aurora primary instance restored from an Aurora 5.6 snapshot might restart when the Fast DDL feature in the lab mode is enabled. 
+  Fixed an issue where the CPU usage is 100% caused by the dictionary stats thread. 
+  Fixed an issue where an Aurora Replica might restart when running a `CHECK TABLE` statement. 

## Integration of MySQL bug fixes
<a name="AuroraMySQL.Updates.2033.BugFixes"></a>
+  Bug \#25361251: INCORRECT BEHAVIOR WITH INSERT ON DUPLICATE KEY IN SP 
+  Bug \#26734162: INCORRECT BEHAVIOR WITH INSERT OF BLOB \+ ON DUPLICATE KEY UPDATE 
+  Bug \#27460607: INCORRECT BEHAVIOR OF IODKU WHEN INSERT SELECT's SOURCE TABLE IS EMPTY 
+  A query using a `DISTINCT` or `GROUP BY` clause could return incorrect results. (MySQL 5.7 Bug \#79591, Bug \#22343910) 
+  A `DELETE` from joined tables using a derived table in the `WHERE` clause fails with error 1093 (Bug \#23074801). 
+  GCOLS: INCORRECT BEHAVIOR WITH CHARSET CHANGES (Bug \#25287633). 

## Comparison with Aurora MySQL version 1
<a name="AuroraMySQL.Updates.2033.Compare56"></a>

The following Amazon Aurora MySQL features are supported in Aurora MySQL version 1 (compatible with MySQL 5.6), but these features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Asynchronous key prefetch (AKP). For more information, see [ Optimizing Aurora indexed join queries with asynchronous key prefetch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.AKP) in the *Amazon Aurora User Guide*. 
+ Hash joins. For more information, see [ Optimizing large Aurora MySQL join queries with hash joins](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.HashJoin) in the *Amazon Aurora User Guide*.
+ Native functions for synchronously invoking AWS Lambda functions. For more information, see [ Invoking a Lambda function with an Aurora MySQL native function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html#AuroraMySQL.Integrating.NativeLambda) in the *Amazon Aurora User Guide*.
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).
+ Migrating data from MySQL using an Amazon S3 bucket. For more information, see [ Migrating data from MySQL by using an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3) in the *Amazon Aurora User Guide*.

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2033.Compatibility"></a>

Aurora MySQL 2.03.3 is wire-compatible with MySQL 5.7 and includes features such as JSON support, spatial indexes, and generated columns. Aurora MySQL uses a native implementation of spatial indexing using z-order curves to deliver >20x better write performance and >10x better read performance than MySQL 5.7 for spatial datasets.

Aurora MySQL 2.03.3 does not currently support the following MySQL 5.7 features:
+ Global transaction identifiers (GTIDs). Aurora MySQL supports GTIDs in version 2.04 and higher.
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
+ X Protocol