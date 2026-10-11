

# Aurora MySQL database engine updates 2026-10-05 (version 3.10.6, compatible with MySQL 8.0.42)
<a name="AuroraMySQL.Updates.3106"></a><a name="3106"></a><a name="3.10.6"></a>

**Version:** 3.10.6

Aurora MySQL 3.10.6 is generally available. Aurora MySQL 3.10 versions are compatible with MySQL 8.0.42. For more information about the community changes, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/) on the MySQL website.

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can perform an in-place upgrade using [Zero Downtime Patching (ZDP)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.10.6 cluster.

For information about planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general upgrade information, see [Upgrading Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, Support is available on the community forums and through [Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3106.Improvements"></a>

### Security fixes
<a name="AuroraMySQL.Updates.3106.SecurityFixes"></a>
+ Fixed an issue which can cause a database instance to restart when setting up Kerberos Service Principal Name.
+ Fixed an issue where queries run through prepared statements could generate duplicate entries in the advanced audit log.
+ Fixed an issue where the Advanced Audit log recorded an incorrect user and host for SQL statements executed inside a SQL SECURITY DEFINER routine (stored procedure, function, or trigger). These records showed the routine's definer user and host (for example, 'user'@'%') instead of the SQL client that invoked the routine. After this fix, the records show the user and host of the invoking SQL client.

This release includes fixes for the following high severity CVEs:
+ [CVE-2026-61094](https://www.cve.org/CVERecord?id=CVE-2026-61094)

### Availability improvements
<a name="AuroraMySQL.Updates.3106.AvailabilityImprovements"></a>
+ Fixed an issue that could cause an additional restart during Zero-downtime patching (ZDP) impacting the overall patching time and ability to preserve connections.
+ Fixed an issue where excessively large thread\_stack configurations could prevent the Aurora MySQL server from starting during a restart or upgrade. Aurora MySQL server now automatically resets thread\_stack to the engine default value (1 MB) when it exceeds system memory, preventing startup failures.
+ Fixed a memory management issue that could cause a reader instance to restart when processing write workloads through write forwarding.
+ Fixed an issue that could cause write forwarding on a reader DB instance to stop working, requiring a reboot of the reader to restore write forwarding. This could occur when a forwarded query was cancelled or timed out while using global write forwarding or local write forwarding.
+ Fixed an issue that could make the replica briefly disconnect and reconnect to the primary, causing a temporary spike in replication lag (AuroraReplicaLag).
+ Fixed an issue which can cause the writer instance to restart while processing `ALTER TABLE ... REORGANIZE PARTITION` SQL statement that changes sub-partition order.

### General improvements
<a name="AuroraMySQL.Updates.3106.GeneralImprovements"></a>
+ Fixed an issue where, during write forwarding, a reader instance restart could leave an orphan forwarding session on the writer instance, and killing that session could cause the writer to restart.
+ Fixed an issue where graceful reader disconnections could incorrectly increment `Aborted_clients` on the writer instance when write forwarding is enabled.
+ Fixed an issue where, with write forwarding enabled, a reader session with aurora\_replica\_read\_consistency set to global could fail to read the latest committed changes.
+ Fixed an issue that can cause the AuroraReplicaLag metric to report values higher than the true replica lag on DB clusters that have enhanced binlog enabled and little to no write workload.

### Integration of MySQL community edition bug fixes
<a name="AuroraMySQL.Updates.3106.CommunityBugFixes"></a>
+ Events created within stored programs were not always handled correctly. (Bug\#36402968)
+ Fixed an issue where renaming a column using ALTER TABLE ... CHANGE COLUMN, on a table with prior instant DDL changes, could result in incorrect internal column-position metadata. (Bug\#38935534)