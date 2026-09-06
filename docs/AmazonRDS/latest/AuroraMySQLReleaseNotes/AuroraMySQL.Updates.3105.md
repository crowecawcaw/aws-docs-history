

# Aurora MySQL database engine updates 2026-07-30 (version 3.10.5, compatible with MySQL 8.0.42)
<a name="AuroraMySQL.Updates.3105"></a><a name="3105"></a><a name="3.10.5"></a>

**Version:** 3.10.5

Aurora MySQL 3.10.5 is generally available. Aurora MySQL 3.10 versions are compatible with MySQL 8.0.42. For more information about the community changes, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/) on the MySQL website.

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can perform an in-place upgrade using [Zero Downtime Patching (ZDP)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.10.5 cluster.

For information about planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general upgrade information, see [Upgrading Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, Support is available on the community forums and through [Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3105.Improvements"></a>

### Security fixes
<a name="AuroraMySQL.Updates.3105.SecurityFixes"></a>

This release includes fixes for the following high severity CVEs:
+ [CVE-2026-46863](https://www.cve.org/CVERecord?id=CVE-2026-46863)

### Availability improvements
<a name="AuroraMySQL.Updates.3105.AvailabilityImprovements"></a>
+ Fixed an issue where a replica instance might restart when executing binary protocol prepared statements that are forwarded to the writer through write forwarding.
+ Fixed an issue where a reader instance could restart repeatedly after being restarted while the writer instance was performing a forceful purge of undo logs.
+ Fixed an issue in the out-of-memory (OOM) avoidance mechanism that could cause a database instance restart while attempting to recover memory under critical memory pressure.
+ Fixed an issue where a delay in InnoDB buffer pool resizing during Aurora serverless scaling operations could cause the database instance to become unresponsive and restart.
+ Fixed an issue that might cause read replicas to restart when the writer instance commits a large transaction with binlog enabled. This issue might also cause errors when reading the binlog file containing the large transaction.
+ Fixed an issue that could cause a writer DB instance to restart when a reader DB instance restarts while local or global write forwarding is enabled.
+ Fixed an issue where the database writer instance could restart unexpectedly during a global database switchover operation while cleaning up temporary tables after SQL statement processing. This restart could result in longer switchover completion time.
+ Fixed an issue that can cause the writer instance to repeatedly restart when the writer instance restarts while purging an undo record for a table with indexes on virtual columns.
+ Fixed a rare issue that can cause the writer instance to restart due to an internal timing conflict during highly concurrent write operations.
+ Fixed an issue that can cause the database to restart when a storage configuration change occurs while a metadata synchronization operation is still in progress.
+ Fixed an issue that could cause a database instance to restart when enhanced binlog is enabled.

### General improvements
<a name="AuroraMySQL.Updates.3105.GeneralImprovements"></a>
+ Fixed an issue that could cause engine restart when a spatial GIS query uses a Z-order spatial index on a column declared with an explicit SRID annotation.
+ Fixed an out-of-memory (OOM) issue that could cause reader restarts when executing privilege-related commands on the writer.
+ Fixed an issue that can, in some cases, cause delayed instance availability during zero-downtime patching (ZDP) or zero-downtime restart (ZDR) operations.
+ Fixed a cluster availability issue that could occur during database server upgrades when DML operations on system tables referenced stale auto-increment values.
+ Fixed an issue where the reader reports `ERROR 1146` (table not found) during certain online DDL operations on the writer when using the `INPLACE` algorithm. This can occur when either the reader has not previously opened the table before the DDL begins, or the reader restarts or a new reader is created while the DDL is in progress.
+ Fixed an issue that can cause query results to be returned in ascending order instead of the requested descending order when using `ORDER BY DESC` with a range comparison and `LIMIT`.
+ Fixed commit ordering on binlog replicas with Enhanced Binlog enabled to correctly honor the `replica_preserve_commit_order` setting. This ordering behavior did not affect data integrity or cause conflicts between transactions, as it applied only to the sequencing of non-dependent transactions.
+ Fixed an issue that could cause database instance restarts during Aurora Serverless scale-down operations or during periods of high buffer pool pressure.
+ Fixed an issue that could cause database cluster clone operations to take an extended time to complete.
+ Fixed an issue where in some cases connection state is not preserved following a zero-downtime upgrade, which could result in unexpected behavior.