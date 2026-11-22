

# Aurora MySQL 8.4.12
<a name="8412"></a><a name="8.4.12"></a>

**Version:** 8.4.12

This release of Aurora MySQL is compatible with MySQL 8.4.12. For more information on the community changes that have occurred, see [MySQL 8.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/) on the MySQL website.

For details of the new features in Aurora MySQL version 8.4, see [Aurora MySQL version 8.4 compatible with MySQL 8.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL84.html). For differences between Aurora MySQL version 8.4 and version 3, see [Comparison of Aurora MySQL version 3 and Aurora MySQL version 8.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v3-v84.html). For a comparison with MySQL 8.4 Community Edition, see [Comparison of Aurora MySQL version 8.4 and MySQL 8.4 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v84-community.html) in the *Amazon Aurora User Guide*.

You can perform an in-place major version upgrade, restore a snapshot with upgrade, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html). You can upgrade from any currently supported Aurora MySQL version 3 cluster to Aurora MySQL version 8.4.12.

For information on planning an upgrade to Aurora MySQL version 8.4, see [Planning a major version upgrade for an Aurora MySQL cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Planning). For more information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*.

For troubleshooting information, see [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html#AuroraMySQL.Upgrading.Troubleshooting) in the *Amazon Aurora User Guide*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

For more information about patch releases and how to apply them, see [About patch releases](AuroraMySQL.Updates.84Updates.md#AuroraMySQL.Updates.84Updates.PatchReleases).

**Topics**
+ [Aurora MySQL 8.4.12, November 20, 2026](#AuroraMySQL.Updates.8412.GA)

## Aurora MySQL 8.4.12, November 20, 2026
<a name="AuroraMySQL.Updates.8412.GA"></a>

### Improvements
<a name="AuroraMySQL.Updates.8412.Improvements"></a>

Below are the improvements made compared to Aurora MySQL 8.4.10, see [Aurora MySQL 8.4.10 Release Notes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.8410.html).

#### Security fixes
<a name="AuroraMySQL.Updates.8412.SecurityFixes"></a>

This release includes fixes for the following high severity CVEs. Each CVE ID links to its record on the CVE website:
+ [CVE-2026-101775](https://www.cve.org/CVERecord?id=CVE-2026-101775)
+ [CVE-2026-101785](https://www.cve.org/CVERecord?id=CVE-2026-101785)
+ [CVE-2026-101796](https://www.cve.org/CVERecord?id=CVE-2026-101796)

#### Availability improvements
<a name="AuroraMySQL.Updates.8412.AvailabilityImprovements"></a>
+ Fixed an issue that can cause premature undo tablespace truncation, leading to a writer restart when purge processes undo records for a secondary index on a virtually generated column.
+ Fixed an issue that, in rare cases, can cause a binlog replica DB instance with `aurora_in_memory_relaylog` enabled to restart during transaction retries.
+ Fixed an issue that can cause reader instances to restart during read queries using a backward index scan.
+ Fixed an issue on DB clusters with Enhanced Binlog enabled that could cause the writer DB instance to restart repeatedly when a transaction used `ROLLBACK TO SAVEPOINT`.

#### General improvements
<a name="AuroraMySQL.Updates.8412.GeneralImprovements"></a>
+ Upgraded the time zone definitions to the IANA 2026f version.
+ Fixed a collation mismatch error (`ERROR 1267 HY000: Illegal mix of collations`) that caused replication stored procedures to fail on DB clusters with a non-default `collation_server` parameter.
+ Fixed an issue which could cause the writer instance to become unresponsive when a large number of concurrent write requests are forwarded to it. If this condition persists, the writer instance can restart.
+ Fixed an issue that can cause an Aurora machine learning query to fail when an earlier query aborts with pending requests to Amazon SageMaker AI or Amazon Comprehend.