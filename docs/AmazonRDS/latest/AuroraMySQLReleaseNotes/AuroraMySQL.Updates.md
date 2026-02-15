# Aurora MySQL database engine updates 2024-07-23 (version 3.07.1) (Deprecated)

**Version:** 3.07.1

Aurora MySQL 3.07.1 is generally available. Aurora MySQL 3.07 versions are compatible with MySQL 8.0.36. For more information on the
community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.md "../AuroraUserGuide/AuroraMySQL.md"). For
differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version
3](../AuroraUserGuide/AuroraMySQL.md "../AuroraUserGuide/AuroraMySQL.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community
Edition](../AuroraUserGuide/AuroraMySQL.md "../AuroraUserGuide/AuroraMySQL.md") in the _Amazon Aurora User Guide_.

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using
[Amazon RDS Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md")
from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.07.1 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see
[Planning
a major version upgrade for an Aurora MySQL cluster](../AuroraUserGuide/AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning "../AuroraUserGuide/AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning"). For general information about Aurora MySQL upgrades, see
[Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.md "../AuroraUserGuide/AuroraMySQL.Updates.md")
in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting for Aurora MySQL
in-place upgrade](../AuroraUserGuide/AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Troubleshooting "../AuroraUserGuide/AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Troubleshooting") in the _Amazon Aurora User Guide_.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.md "../AuroraUserGuide/USER_UpgradeDBInstance.md") in
the _Amazon Aurora User Guide_.

## Improvements

**Fixed security issues and CVEs:**

- Introduced a new user for binary log (binlog) replication, `rdsrepladmin_priv_checks_user`. For more information, see
  [Privilege
  checks user for binary log replication](../AuroraUserGuide/AuroraMySQL.md#AuroraMySQL.privilege-model.binlog "../AuroraUserGuide/AuroraMySQL.md#AuroraMySQL.privilege-model.binlog") in the _Amazon Aurora User Guide_.

This release includes all community CVE fixes up to and including MySQL 8.0.36.

**Availability improvements:**

- Fixed an issue that can cause a reader DB instance to restart when freeing memory used for log application.
- Fixed an issue in computing internal metrics for full-text search (FTS) indexes that can cause database restarts.
- Fixed an issue that can disable binary logging when an error occurs while committing a large transaction.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.36. For more information, see
[MySQL bugs fixed by Aurora MySQL 3.x database
engine updates](AuroraMySQL.Updates.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.md#AuroraMySQL.Updates.MySQLBugs.v3").
