# Aurora MySQL database engine updates 2026-01-02 (version 3.04.6, compatible with MySQL 8.0.28)

**Version:** 3.04.6

Aurora MySQL 3.04.6 is generally available. Aurora MySQL 3.04 versions are compatible with MySQL 8.0.28. For more information on the
community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.Updates.30Updates.md "../AuroraUserGuide/AuroraMySQL.Updates.30Updates.md"). For
differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version
3](../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community
Edition](../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md") in the _Amazon Aurora User Guide_.

You can perform an in-place upgrade that leverages a [zero-downtime-patch](../AuroraUserGuide/AuroraMySQL.Updates.ZDP.md "../AuroraUserGuide/AuroraMySQL.Updates.ZDP.md"), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.04.6 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see
[Planning
a major version upgrade for an Aurora MySQL cluster](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning"). For general information about Aurora MySQL upgrades, see
[Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md")
in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting for Aurora MySQL
in-place upgrade](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Troubleshooting "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Troubleshooting") in the _Amazon Aurora User Guide_.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in
the _Amazon Aurora User Guide_.

## Improvements

**Availability improvements**

- Fixed an issue which, could cause an engine restart when running `KILL <query-id>` after running `EXPLAIN FOR CONNECTION <query-id>` on a running parallel query.
- Fixed issues that could cause the writer instance to become unavailable if write forwarding is disabled or reader instances are restarted when using Global Write Forwarding or Local Write Forwarding

**General improvements**

- Fixed an issue that causes reader instances to not generate error logs when write forwarding is enabled and parameter "aurora_replica_read_consistency" is modified.
- Fixed an issue which can cause some SQL statements to not get logged in the audit log.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.28. For more
information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3")
.
