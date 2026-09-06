

# Aurora MySQL database engine updates 2025-07-31 (version 3.10.0, compatible with MySQL 8.0.42)
<a name="AuroraMySQL.Updates.3100"></a><a name="3.10.0"></a><a name="3.10.0"></a>

**Version:** 3.10.0

Aurora MySQL 3.10.0 is generally available. Aurora MySQL 3.10 versions are compatible with MySQL 8.0.42. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

**Note**  <a name="lts_notice_3100"></a>
This version is designated as a long-term support (LTS) release. For more information, see [Aurora MySQL long-term support (LTS) releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.html#AuroraMySQL.Updates.LTS) in the *Amazon Aurora User Guide*.  
We recommend that you don't set the `AutoMinorVersionUpgrade` parameter to `true` (or enable **Auto minor version upgrade** in the AWS Management Console) for LTS versions. Doing so could lead to your DB cluster being upgraded to the next target version for Automatic Minor Version Upgrade campaign, which may not be an LTS version.

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

You can perform an in-place upgrade [leveraging Zero Downtime Patching (ZDP)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.10.0 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## New features
<a name="AuroraMySQL.Updates.3100.NewFeatures"></a>
+ Aurora MySQL version 3.10 extends the in-memory relay log cache support for binary log replicas. This feature, first introduced in [version 3.05](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.3050.html), can improve binary log replication throughput by up to 40%. The in-memory relay log cache is turned off by default. To turn it on, set the `aurora_in_memory_relaylog` parameter to `ON` in the DB cluster parameter group or DB instance parameter group. For more information about this parameter, see [Aurora MySQL parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html). The feature supports single-threaded binary log replication and multi-threaded replication with [GTID auto-positioning](https://dev.mysql.com/doc/refman/8.0/en/replication-gtids-auto-positioning.html). Starting with version 3.10, the feature also supports multi-threaded replication with [replica\_preserve\_commit\_order = ON](https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html#sysvar_replica_preserve_commit_order), even without GTIDs. For more information, see [Binary log optimizations in Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/binlog-optimization.html).
+ Amazon Aurora has doubled its maximum storage capacity from 128 TiB to 256 TiB, enabling larger workloads in a single database cluster. To use the increased storage limit with Aurora MySQL, upgrade your cluster to version 3.10 (compatible with MySQL 8.0.42) or higher. After upgrade, Aurora storage automatically scales up to 256 TiB based on the amount of data in your cluster volume.

## Improvements
<a name="AuroraMySQL.Updates.3100.Improvements"></a>

**Security fixes**

Medium CVEs:
+ [CVE-2025-21501](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21501)
+ [CVE-2025-21500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21500)
+ [CVE-2025-21543](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21543)
+ [CVE-2025-21540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21540)
+ [CVE-2025-21491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21491)
+ [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490)
+ [CVE-2025-21559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21559)
+ [CVE-2025-21555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21555)
+ [CVE-2025-21497](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21497)
+ [CVE-2025-21519](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21519)
+ [CVE-2025-21529](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21529)
+ [CVE-2025-21505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21505)
+ [CVE-2025-21531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21531)
+ [CVE-2025-21523](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21523)
+ [CVE-2025-21503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21503)
+ [CVE-2025-21522](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21522)
+ [CVE-2025-21518](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21518)
+ [CVE-2025-21577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21577)
+ [CVE-2025-30682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30682)
+ [CVE-2025-30687](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30687)
+ [CVE-2025-30688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30688)
+ [CVE-2025-21574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21574)
+ [CVE-2025-21575](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21575)
+ [CVE-2025-30693](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30693)
+ [CVE-2025-30695](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30695)
+ [CVE-2025-30715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30715)
+ [CVE-2025-21584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21584)
+ [CVE-2025-21580](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21580)
+ [CVE-2025-21581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21581)
+ [CVE-2025-21585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21585)
+ [CVE-2025-30689](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30689)
+ [CVE-2025-21579](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21579)
+ [CVE-2025-30696](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30696)
+ [CVE-2025-30705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30705)
+ [CVE-2025-30683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30683)
+ [CVE-2025-30684](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30684)
+ [CVE-2025-30685](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30685)
+ [CVE-2025-30699](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30699)
+ [CVE-2025-30704](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30704)
+ [CVE-2025-30721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30721)

Low CVEs:
+ [CVE-2025-21520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21520)
+ [CVE-2025-21546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21546)
+ [CVE-2025-30703](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30703)
+ [CVE-2025-30681](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30681)

**Availability improvements:**
+ Fixed an issue that causes unnecessary database server restarts that were occurring because of an incorrect assessment of recovery progress.

**General improvements:**
+ Reduced commit latency when I/O optimized is enabled.
+ Fixed an issue that causes reader instances to not generate error logs when write forwarding is enabled and parameter `aurora_replica_read_consistency` is modified.
+ Fixed an issue that can cause a reader instance to restart due to the interaction between the replication thread and a query accessing tables that are not present in the buffer cache.
+ Fixed an issue where local write forwarding stops working after the database instance restarted with zero-downtime restart.
+ Fixed an issue in write forwarding where forwarded queries may behave incorrectly for statements containing set options.
+ Fixed a stability issue where inserting metadata for an undo tablespace would trigger an unexpected database restart.
+ Fixed an issue which can cause DB cluster exports to take significantly longer than expected when there are tables larger than 14 TB.
+ Fixed an issue which can cause incorrect reporting of `Innodb_buffer_pool_pages_misc` status variable.
+ Added support for preserving `LAST_INSERT_ID` during zero-downtime patching (ZDP) or zero-downtime restart (ZDR).
+ Aurora MySQL uses 8-bit values for virtual index IDs to prevent MySQL undo format issues, as exceeding this limit could cause cluster unavailability. When approaching this limit, the system now writes warning messages to the MySQL error log. If the limit is reached, attempts to add a new index return an error. For more information about virtual index best practices, see [Virtual index ID overflow errors](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.Performance.html#AuroraMySQL.BestPractices.Performance.VirtualIndexIDOverflow) in the Aurora MySQL documentation.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3100.Patches"></a>

This release includes all community bug fixes up to and including 8.0.42. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).
+ A server exit could result from simultaneous attempts by multiple threads to register and deregister metadata Performance Schema objects, or to acquire and release metadata locks. (Bug \#26502135)