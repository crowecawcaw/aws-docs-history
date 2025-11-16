# Aurora MySQL database engine updates 2025-05-05 (version 3.04.4, compatible with MySQL 8.0.28)

**Version:** 3.04.4

Aurora MySQL 3.04.4 is generally available. Aurora MySQL 3.04 versions are compatible with MySQL 8.0.28. For more information on the
community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.md "../AuroraUserGuide/AuroraMySQL.md"). For
differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparison of Aurora MySQL version 2 and Aurora MySQL version
3](../AuroraUserGuide/AuroraMySQL.md "../AuroraUserGuide/AuroraMySQL.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparison of Aurora MySQL version 3 and MySQL 8.0 Community
Edition](../AuroraUserGuide/AuroraMySQL.md "../AuroraUserGuide/AuroraMySQL.md") in the _Amazon Aurora User Guide_.

###### Note

This version is designated as a long-term support (LTS) release. For more information, see [Aurora MySQL long-term support (LTS)
releases](../AuroraUserGuide/AuroraMySQL.Update.md#AuroraMySQL.Updates.LTS "../AuroraUserGuide/AuroraMySQL.Update.md#AuroraMySQL.Updates.LTS") in the _Amazon Aurora User Guide_.

We recommend that you don't set the `AutoMinorVersionUpgrade` parameter to
`true` (or enable **Auto minor version upgrade** in the AWS Management Console) for LTS versions. Doing so could lead
to your DB cluster being upgraded to the next target version for Automatic Minor Version Upgrade campaign, which may not be an LTS version.

You can perform an in-place upgrade that leverages a [zero-downtime-patch](../AuroraUserGuide/AuroraMySQL.Updates.md "../AuroraUserGuide/AuroraMySQL.Updates.md"), restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.04.4 cluster.

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

**Security fixes**

Critical CVEs:

- [CVE-2024-11053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11053 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11053")
- [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371")

**Availability improvements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish connection with the writer.
- Fixed an issue that can cause a restart on a binary log (binlog) replica when processing a large number of relay log files during [relay log recovery](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-unexpected-replica-halt.html "https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-unexpected-replica-halt.html").
- Fixed an issue that causes a database reader instance restart when executing a query using the Parallel Query feature.
- Fixed an issue that, in rare conditions, can disable binary logging when an error occurs during commit of a large transaction.
- Fixed an issue that can cause Aurora read replicas to restart in the event of certain rare transaction commit orders on the writer DB instance.
- Fixed an issue that can lead to a database restart when [scheduled events](https://dev.mysql.com/doc/refman/8.0/en/events-overview.html "https://dev.mysql.com/doc/refman/8.0/en/events-overview.html") are aborted during execution on instances that have Enhanced Binlog enabled.
- Fixed an issue where database instances using multi TB Aurora cluster volumes, may experience increased downtime during restart due to InnoDB bufferpool validation failures.

**General improvements**

- The following privileges have been added to the `rds_superuser_role`: `FLUSH_OPTIMIZER_COSTS`, `FLUSH_STATUS`, `FLUSH_TABLES`, and `FLUSH_USER_RESOURCES`. For information about the `rds_superuser_role`, see [Amazon Master User Accounts with Amazon Aurora](../AuroraUserGuide/UsingWithRDS.md "../AuroraUserGuide/UsingWithRDS.md") in the _Amazon Aurora User Guide_. For more information on these dynamic privileges, please see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/flush.html "https://dev.mysql.com/doc/refman/8.0/en/flush.html").
- Fixed an issue where a preserved connection is handled incorrectly during Zero-downtime patching (ZDP)/Zero-downtime restart (ZDR) that can lead to the client waiting indefinitely for a query to complete.
- Fixed an issue where the row becomes unreadable through the spatial index during an update.
- Fixed an issue where a query containing an optimizer hint that was aborted during a Zero-downtime restart or Zero-downtime patching operation may be incorrectly handled.
- Fixed an issue where the commit latency is not measured when `innodb_flush_log_at_trx_commit` is set to `0`.
- Introduced optimizations to reduce memory usage during logical [data dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary.html") recovery when there are a large number of tables.
- Fixed an issue that caused the `SHOW BINARY LOGS` command to take longer to execute on a cluster where Enhanced Binlog is enabled or was previously enabled. This issue could also cause increased commit latency if multiple `SHOW BINARY LOGS` commands were running concurrently.
- Fixed a memory issue associated with the default roles of the view definer.
- Fixed an issue that can cause failure in completing the process of disabling the write forwarding feature.
- Fixed an issue that can prevent new client connections from being established to the database when write forwarding is enabled.
- Fixed an issue that can cause a writer database instance to restart when a reader instance using write forwarding executes a DML statement that contains a `timestamp` value and the `time_zone` database parameter is set to "UTC".
- Fixed an issue that caused intermittent unavailability of an Aurora Read Replica or table definition inconsistencies with error `'Table does not exist'` on the replica due to concurrent read queries on the replica and DDL operations on the writer.
- Fixed an issue that may cause an incomplete result set when executing queries involving `LEFT-` or `RIGHT-JOIN` operations using the hash-join algorithm with Parallel Query.
- Starting with
  this Aurora MySQL version, fast insert optimization is no longer enabled. For more
  information, see [Amazon Aurora MySQL performance enhancements](../AuroraUserGuide/Aurora.AuroraMySQL.md#Aurora.AuroraMySQL.Performance "../AuroraUserGuide/Aurora.AuroraMySQL.md#Aurora.AuroraMySQL.Performance") in the _Amazon Aurora User Guide_.

**Upgrades and migrations**

- Removed the default roles that were unnecessarily created during the upgrade from AMS2 to AMS3.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.28. For more
information, see [MySQL bugs fixed by Aurora MySQL 3.x database
engine updates](AuroraMySQL.Updates.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.md#AuroraMySQL.Updates.MySQLBugs.v3")
.

- Fixed an issue that resolves the deadlock when `FLUSH STATUS`, `COM_CHANGE_USER`, and `SHOW PROCESS LIST` are executed concurrently. (Bug#35218030)
