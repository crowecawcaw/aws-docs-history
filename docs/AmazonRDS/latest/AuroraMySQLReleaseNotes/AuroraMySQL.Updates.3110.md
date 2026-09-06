

# Aurora MySQL database engine updates 2025-11-13 (version 3.11.0, compatible with MySQL 8.0.43)
<a name="AuroraMySQL.Updates.3110"></a><a name="3110"></a><a name="3.11.0"></a>

**Version:** 3.11.0

Aurora MySQL 3.11.0 is generally available. Aurora MySQL 3.11 versions are compatible with MySQL 8.0.43. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can perform an in-place upgrade leveraging zero-downtime patching (ZDP), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.11.0 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, Support is available on the community forums and through [Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3110.Improvements"></a>

**Fixed security issues and CVEs**

**Medium CVEs:**
+ [CVE-2025-50077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50077)
+ [CVE-2025-50078](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50078)
+ [CVE-2025-50079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50079)
+ [CVE-2025-50080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50080)
+ [CVE-2025-50082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50082)
+ [CVE-2025-50083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50083)
+ [CVE-2025-50084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50084)
+ [CVE-2025-50085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50085)
+ [CVE-2025-50086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50086)
+ [CVE-2025-50087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50087)
+ [CVE-2025-50088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50088)
+ [CVE-2025-50091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50091)
+ [CVE-2025-50092](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50092)
+ [CVE-2025-50093](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50093)
+ [CVE-2025-50094](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50094)
+ [CVE-2025-50096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50096)
+ [CVE-2025-50097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50097)
+ [CVE-2025-50099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50099)
+ [CVE-2025-50101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50101)
+ [CVE-2025-50102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50102)
+ [CVE-2025-53023](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-53023)

**Low CVEs:**
+ [CVE-2025-50098](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50098)
+ [CVE-2025-50100](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50100)
+ [CVE-2025-50104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50104)

**Availability improvements**
+ Fixed an issue in logical recovery with `aurora_enhanced_binlog` enabled that could prevent database restarts in case of aborted transactions.
+ Fixed an issue that could cause the writer instance to restart when global write forwarding or local write forwarding is being disabled.
+ Fixed an issue that could cause writer to become unresponsive when write forwarding is being disabled while two or more replicas are forwarding requests.
+ Fixed an issue that could cause an engine restart when running `KILL <query-id>` after running `EXPLAIN FOR CONNECTION <query-id>` on a running parallel query.
+ Fixed an issue where out-of-memory (OOM) avoidance wasn't persisting the configured `aurora_oom_response` DB parameter value after database restart.
+ Fixed an issue that prevented users with `CONNECTION_ADMIN` or `SUPER` privileges from performing an additional connection beyond `max_connections` limit, as supported in MySQL Community Edition.
+ Fixed an issue with Aurora serverless scaling that resulted in DB instance restarts by preventing critical memory pages from being swapped out.
+ Fixed an issue that could cause Aurora MySQL serverless instances to restart when the `innodb_purge_threads` parameter was manually configured to a value different from the default. The `innodb_purge_threads` parameter is now automatically managed for Aurora serverless instances and can't be modified.
+ Fixed an issue that could cause a reader instance's restart to fail when the writer is running a large number of DDL operations.
+ Fixed an issue that could cause the writer instance to become unresponsive if reader instances restart while using Global Write Forwarding or Local Write Forwarding.
+ Fixed an issue that could cause engine restart during zero-downtime patching (ZDP)/zero-downtime restart (ZDR), when preserving SSL/TLS connections with active transactions.
+ Fixed an issue that, under rare conditions, could cause changes on the writer instance to be sent to the reader instance in an order that's incompatible with the query-processing threads. This can lead to a deadlock between query-processing thread and replication-apply thread, which in turn can cause the reader instance to restart.
+ Fixed an issue to prevent unnecessary database server restarts that were occurring due to the monitoring agent's incorrect health assessment.

**General improvements**
+ Fixed an issue where writes to the database may stall while executing a long running transaction leading to a database restart or a major version upgrade to fail.
+ Fixed an issue with replicas incorrectly being restarted when joining the writer.
+ Optimized database performance for database instances with large Aurora Storage volumes.
+ Fixed an issue in the range optimizer where constant expressions weren't recognized when calculating range bounds. (Community Bug \#112737)
+ Fixed an issue where exporting a DB snapshot to Amazon S3 performs slower when exporting tables containing JSON columns with null values.
+ Fixed an issue where temporary binary log files weren't being properly cleaned up after transaction rollbacks when using binary logging. This fix prevents storage consumption from retained temporary files and in certain cases can also prevent anomalies in the binary log files.
+ Improved write IOPS performance when system variable `innodb_flush_log_at_trx_commit` is set to `0`.
+ Fixed an issue where zero downtime patching (ZDP) / zero downtime restart (ZDR) could result in DB instance restart while restoring warnings with invalid error codes.
+ Automatically disable `aurora_oom_response` actions (except print, if configured) when `aurora_oom_response` fails to resolve memory pressure after a threshold time (in the order of few mins).
+ Fixed an issue where a column with partial JSON updates fails parallel export causing internal fallback to a much slower Amazon RDS export.
+ Fixed an issue that can cause memory management issues when parallel query operations on the table with the blob fields.
+ Fixed an issue that could cause the `Previous_gtids` binlog event to exclude certain GTIDs with Enhanced Binlog enabled and `gtid_mode` set to `ON` or `ON_PERMISSIVE`.
+ Fixed an issue that causes unexpected "Internal write forwarding error" on reader instances when write forwarding is enabled.
+ Resolved a race condition that could cause incorrect page reads from the buffer pool during Aurora serverless scale-down operations or during page eviction from the buffer pool. Ref community [Bug\#116305](https://bugs.mysql.com/bug.php?id=116305).
+ Fixed an issue where exporting a DB snapshot to Amazon S3 will be slower when exporting tables containing secondary indices with generated expressions.
+ Fixed an issue causing inaccurate `AbortedClients` metrics when multiple connections terminate unexpectedly.
+ Added a new global variable `aurora_lambda_request_timeout` to allow users configure AWS Lambda request timeouts (default: 10 seconds). For more information on invoking a Lambda function from an Aurora MySQL DB cluster see [Invoking a Lambda function from an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html).
+ Fixed an issue where local write forwarding stops working after the database instance restarted with zero-downtime restart.
+ Fixed an issue that could cause a database instance restart operation to fail if `max_user_connections` is set to a low value.
+ Improved parallel export performance by optimizing the bootstrap process for large volumes (>64 TB), reducing overall export operation time.
+ Fixed an issue that could cause the writer instance to restart when performing `ALTER TABLE` in parallel with read queries.
+ Fixed an issue that can cause DB cluster exports to take significantly longer than expected when there are tables larger than 14 TB.
+ Fixed an issue that caused inaccurate tracking of parallel query requests while running `EXPLAIN ANALYZE` statements where `Aurora_pq_request_in_progress` counter wasn't updated accurately.
+ Fixed an issue that, under uncommon conditions, can cause the database instance to restart when the database volume is close to its maximum allowed size.
+ Fixed an issue that can cause a database instance restart when restoring connections during zero-downtime restart and zero-downtime patching.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3110.Patches"></a>

This release includes all community bug fixes up to and including 8.0.43. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed an issue where a query of the form `SELECT 1 FROM t WHERE CAST(a AS UNSIGNED INTEGER) = 1 AND a = (SELECT 1 FROM t)` leads to an assertion failure in `item_func.cc`. (Community Bug Fix \#36128964)
+ A query of the form `SELECT 1 FROM t WHERE CAST(a AS UNSIGNED INTEGER) = 1 AND a = (SELECT 1 FROM t)` led to an assertion in `item_func.cc`. (Bug \#36128964)

For more information on community changes, see [MySQL 8.0.43 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-43.html).