# Aurora MySQL database engine updates 2025-04-07 (version 3.08.2, compatible with MySQL 8.0.39)

**Version:** 3.08.2

Aurora MySQL 3.08.2 is generally available. Aurora MySQL 3.08 versions are compatible with MySQL 8.0.39. For more information on the
community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.MySQL80.md "../AuroraUserGuide/AuroraMySQL.MySQL80.md"). For
differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version
3](../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community
Edition](../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md") in the _Amazon Aurora User Guide_.

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.04.\*, 3.05.\*, 3.06.\*, 3.07.\*, and 3.08.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using
[Amazon RDS Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") from any currently
supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.08.2 cluster.

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

**Security fixes:**

- [CVE-2024-11053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11053 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11053")

**Availability improvements:**

- Fixed an issue on the replica where a network interruption may not correctly re-establish connection with the writer.
- Fixed an issue where a forwarded multi-statement query can fail if `innodb_flush_log_at_trx_commit` is set to `0` at writer instance.
- Fixed an issue that can cause an Aurora writer DB instance to restart when write forwarding is enabled.
- Fixed an issue that can cause an Aurora reader DB instance to restart when using write forwarding with multi-statement or implicit commit queries.

**General improvements**

- Starting with
  this Aurora MySQL version, fast insert optimization is no longer enabled. For more
  information, see [Amazon Aurora MySQL performance enhancements](../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance "../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance") in the _Amazon Aurora User Guide_.
- Fixed an issue with an incorrect breach of the `max_user_connections` threshold, resulting in connection errors for some users. This occurs in some edge cases, such as when connections are created and killed almost immediately.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.39, in addition to the following. For more information, see
[MySQL
bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3").

- While large transactions were being received and applied, and a request to stop the replication channel was made using `STOP REPLICA`, MySQL did not do so properly, and subsequently did not process any channel commands. In addition, the server shutdown process did not complete gracefully, and required either the MySQL process to be killed or the host system to be restarted. (Community Bug Fix #115966 and #37008345)
