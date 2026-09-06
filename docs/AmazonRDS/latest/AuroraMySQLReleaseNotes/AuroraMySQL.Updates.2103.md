

# Aurora MySQL database engine updates 2022-11-01 (version 2.10.3) (Deprecated)
<a name="AuroraMySQL.Updates.2103"></a><a name="2103"></a><a name="2.10.3"></a>

 **Version:** 2.10.3 

 Aurora MySQL 2.10.3 is generally available. Aurora MySQL 2.x versions are compatible with MySQL 5.7, and Aurora MySQL 1.x versions are compatible with MySQL 5.6. 

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 2.11.\*, 3.01.\* and 3.02.\*. 

 You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.10.3. For clusters running Aurora MySQL version 1, you can upgrade an existing Aurora MySQL 1.23 or higher cluster directly to 2.10.3. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.10.3. 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

**Note**  
 For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2103.Improvements"></a>

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below:
+ [CVE-2022-21444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21444)
+ [CVE-2022-21344](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21344)
+ [CVE-2022-21304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21304)
+ [CVE-2022-21245](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21245)
+ [CVE-2021-36222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222)
+ [CVE-2021-22926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22926)

 **General improvements:** 
+ Fixed an issue which, in rare conditions, causes the database server to restart due to a long semaphore wait when the [deadlock detector thread](https://dev.mysql.com/doc/refman/5.7/en/innodb-deadlocks.html) gets stuck.
+ Fixed an issue which can cause the freeable memory on the database instance to reduce when certain Data Control Language (DCL) SQL statements such as GRANT, FLUSH PRIVILEGES etc. are run on that instance. Frequent use of such statements can cause the freeable memory to keep reducing and may cause the database instance to restart because of out-of-memory issues. Use of such statements on the writer instance can also cause the freeable memory on the reader instances to reduce.
+ Fixed an issue where queries against the "performance\_schema.events\_waits\_summary\_global\_by\_event\_name" table may become slow when a database instance is under heavy load with the "wait/io/aurora\_respond\_to\_client" performance\_schema wait event enabled.
+ Fixed an issue which, in rare conditions, can cause the database server to stall and restart when transactions partially roll back due to a constraint violation on the secondary indexes.
+ Fixed an issue which, in rare conditions, can cause the writer instance to restart or failover when a transaction accesses a row being deleted by another transaction.
+ Fixed an issue which, in rare conditions, can cause the database to restart due to a long semaphore wait when I/O threads become deadlocked.
+ Fixed an issue which can cause the read replica to restart during failover in rare conditions when the Unix socket lock file is in use.
+ Fixed an issue where excessive query cache invalidation causes higher than expected CPU usage and latencies on the read replica due to the read replica having to read the data from the disk instead of from the query cache.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.2103.Patches"></a>

This release includes all community bug fixes up to and including 5.7, in addition to the below. For more information, see [MySQL bugs fixed by Aurora MySQL 2.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v2).
+ Fixed an issue where the code for reading character set information from Performance Schema statement events tables (for example, events\_statements\_current) did not prevent simultaneous writing to that character set information. As a result, the SQL query text character set could be invalid, which could result in a server exit. With this fix, an invalid character set causes SQL\_TEXT column truncation and prevents server exits. (Bug \#23540008)
+ Fixed an issue when an UPDATE required a temporary table having a primary key larger than 1024 bytes and that table was created using InnoDB, the server could exit. (Bug \#25153670)
+ Fixed an issue where two sessions concurrently executing an INSERT ... ON DUPLICATE KEY UPDATE operation generated a deadlock. During partial rollback of a tuple, another session could update it. The fix for this bug reverts the fixes for Bug \#11758237, Bug \#17604730, and Bug \#20040791. (Bug \#25966845)

## Comparison with Aurora MySQL version 1
<a name="AuroraMySQL.Updates.2103.Compare56"></a>

The following Amazon Aurora MySQL features are supported in Aurora MySQL version 1 (compatible with MySQL 5.6), but these features are currently not supported in Aurora MySQL version 2 (compatible with MySQL 5.7).
+ Hash joins. For more information, see [ Optimizing large Aurora MySQL join queries with hash joins](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#Aurora.BestPractices.HashJoin) in the *Amazon Aurora User Guide*.
+ Native functions for synchronously invoking AWS Lambda functions. For more information, see [ Invoking a Lambda function with an Aurora MySQL native function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html#AuroraMySQL.Integrating.NativeLambda) in the *Amazon Aurora User Guide*.
+ Scan batching. For more information, see [Aurora MySQL database engine updates 2017-12-11 (version 1.16) (Deprecated)](AuroraMySQL.Updates.20171211.md).
+ Migrating data from MySQL using an Amazon S3 bucket. For more information, see [ Migrating data from MySQL by using an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3) in the *Amazon Aurora User Guide*.

## MySQL 5.7 compatibility
<a name="AuroraMySQL.Updates.2103.Compatibility"></a>

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