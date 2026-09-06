

# Aurora MySQL database engine updates 2024-07-23 (version 3.07.1) (Deprecated)
<a name="AuroraMySQL.Updates.3071"></a><a name="3.07.1"></a><a name="3.07.1"></a>

**Version:** 3.07.1

Aurora MySQL 3.07.1 is generally available. Aurora MySQL 3.07 versions are compatible with MySQL 8.0.36. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.07.1 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3071.Improvements"></a>

**Fixed security issues and CVEs:**
+ Introduced a new user for binary log (binlog) replication, `rdsrepladmin_priv_checks_user`. For more information, see [Privilege checks user for binary log replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html#AuroraMySQL.privilege-model.binlog) in the *Amazon Aurora User Guide*.

This release includes all community CVE fixes up to and including MySQL 8.0.36.

**Availability improvements:**
+ Fixed an issue that can cause a reader DB instance to restart when freeing memory used for log application.
+ Fixed an issue in computing internal metrics for full-text search (FTS) indexes that can cause database restarts.
+ Fixed an issue that can disable binary logging when an error occurs while committing a large transaction.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3071.Patches"></a>

This release includes all community bug fixes up to and including 8.0.36. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).