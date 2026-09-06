

# Aurora MySQL database engine updates 2024-06-26 (version 3.04.3, compatible with MySQL 8.0.28)
<a name="AuroraMySQL.Updates.3043"></a><a name="3.04.3"></a><a name="3.04.3"></a>

**Version:** 3.04.3

Aurora MySQL 3.04.3 is generally available. Aurora MySQL 3.04 versions are compatible with MySQL 8.0.28. For more information on community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html).

**Note**  <a name="lts_notice_3043"></a>
This version is designated as a long-term support (LTS) release. For more information, see [Aurora MySQL long-term support (LTS) releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.html#AuroraMySQL.Updates.LTS) in the *Amazon Aurora User Guide*.  
We recommend that you don't set the `AutoMinorVersionUpgrade` parameter to `true` (or enable **Auto minor version upgrade** in the AWS Management Console) for LTS versions. Doing so could lead to your DB cluster being upgraded to the next target version for Automatic Minor Version Upgrade campaign, which may not be an LTS version.

Currently supported Aurora MySQL releases are 2.07.9, 2.7.10, 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html) from any currently available Aurora MySQL version 2 cluster into an Aurora MySQL version 3.04.3 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3043.Improvements"></a>

**Fixed security issues and CVEs:**

This release includes all community CVE fixes up to and including MySQL 8.0.28. The following CVE fixes are included:
+ [CVE-2024-0853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0853)

**Availability improvements:**
+ Fixed an issue that causes an Aurora MySQL DB instance to restart when running a parallel query.
+ Fixed an issue that can cause a reader DB instance to restart when reading a table that is being altered or dropped on the writer DB instance.
+ Fixed an issue that caused a memory access violation leading to releasing a mutex object no longer owned by the thread.
+ Fixed an issue that can cause an Aurora MySQL writer DB instance to restart when a write forwarding session is closed while running a forwarded query.
+ Fixed an issue that causes a DB instance to restart when handling large GTID sets on a binary log–enabled instance.
+ Fixed an issue when processing `INSERT` queries on InnoDB partitioned tables that can cause a gradual decline of free memory in the DB instance.
+ Fixed an issue that, in rare conditions, can cause a reader instance to restart when performing `SELECT` queries on tables with a foreign key constraint.
+ Fixed an issue that can cause a database to restart when InnoDB data dictionary recovery takes a long time during database recovery.
+ Fixed an issue that can cause a database to restart when a cascading `UPDATE` or `DELETE` foreign key constraint is defined on a table where a virtual column is involved either as a column in the foreign key constraint, or as a member of the referenced table.
+ Fixed an issue in Aurora serverless that can lead to a database restart while scaling up.

**General improvements:**
+ Fixed an issue that provided an incorrect value for the `threads_running` status variable when using Aurora Global Database.
+ Fixed an issue that causes a DB instance to restart because of inaccurate lock holder information in `rw_lock` when using parallel reads.
+ Fixed a memory management issue that led to a decrease in freeable memory over time when running `SELECT ... INTO OUTFILE ...` queries.
+ Fixed an issue that can cause a DB instance to restart when the local storage on the DB instance reaches full capacity.
+ Fixed an issue where the Performance Schema wasn't enabled when Performance Insights automated management was turned on for db.t4g.medium and db.t4g.large DB instances.
+ Fixed an issue during zero-downtime patching (ZDP) that prevents a DB instance from closing client connections upon reaching the customer-configured of either `wait_timeout` or `interactive_timeout`.
+ Fixed an issue where a `SELECT` query on an Aurora reader instance might fail with the error table doesn't exist when the table has at least one full-text search (FTS) index and a `TRUNCATE` statement is being run on the Aurora writer DB instance.

**Upgrades and migrations:**
+ Fixed an issue that causes upgrades or migrations to fail when the target Aurora MySQL DB engine version is 3.04.0 or higher. This occurs when the `lower_case_table_names` DB cluster parameter is set to `1`, and MySQL database collation is incompatible with lowercase table names.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3043.Patches"></a>

This release includes all community bug fixes up to and including 8.0.28. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3).