# Aurora MySQL database engine updates 2024-06-26 (version 3.06.1) (Deprecated)

**Version:** 3.06.1

Aurora MySQL 3.06.1 is generally available. Aurora MySQL 3.06 versions are compatible with
MySQL 8.0.34. For more information on the community changes that have occurred, see [MySQL 8.0 Release
Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/ "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/").

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](../AuroraUserGuide/AuroraMySQL.MySQL80.md "../AuroraUserGuide/AuroraMySQL.MySQL80.md"). For
differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version
3](../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-v2-v3.md"). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community
Edition](../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md "../AuroraUserGuide/AuroraMySQL.Compare-80-v3.md") in the _Amazon Aurora User Guide_.

Currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

You can perform an in-place upgrade, restore a snapshot, or initiate a managed blue/green upgrade using [Amazon RDS Blue/Green
Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") from any currently supported Aurora MySQL version 2 cluster into an Aurora MySQL version 3.06.1 cluster.

For information on planning an upgrade to Aurora MySQL version 3, see
[Planning
a major version upgrade for an Aurora MySQL DB cluster](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning"). For general information about Aurora MySQL upgrades, see
[Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the
_Amazon Aurora User Guide_.

For troubleshooting information, see
[Troubleshooting
for Aurora MySQL in-place upgrade](../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Troubleshooting "../AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Troubleshooting") in the _Amazon Aurora User Guide_.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see [Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in
the _Amazon Aurora User Guide_.

## Improvements

**Fixed security issues and CVEs:**

This release includes all community CVE fixes up to and including MySQL 8.0.34. The
following CVE fixes are included:

- [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487")
- [CVE-2024-0853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0853 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0853")

**Availability improvements:**

- Fixed an issue that causes an Aurora MySQL DB instance to restart when running a parallel query.
- Fixed an issue that can cause a reader DB instance to restart when reading a
  table that is being altered or dropped on the writer DB instance.
- Fixed an issue that caused a memory access violation leading to releasing a
  mutex object no longer owned by the thread.
- Fixed an issue that can cause an Aurora MySQL writer DB instance to restart when a write forwarding session is closed while running a forwarded query.
- Fixed an issue that causes a DB instance restart when handling large GTID sets on a binary log–enabled instance.
- Fixed an issue that, in rare conditions, can cause a reader instance to restart when performing `SELECT` queries on tables with a
  foreign key constraint.
- Fixed an issue that causes a DB instance to restart when attempting to recover
  the InnoDB data dictionary during database recovery.
- Fixed an issue in Aurora Serverless v2 that can lead to a database restart while scaling up.

**General improvements:**

- Fixed an issue in metrics publishing code where memory might be used after
  being freed.
- Fixed an issue that caused repeated DB engine restarts due to a nonexistent
  undo tablespace object.
- Fixed an issue with automatic truncation of undo tablespaces when they're
  larger than the threshold [innodb\_max\_undo\_log\_size](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html#sysvar_innodb_max_undo_log_size "https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html#sysvar_innodb_max_undo_log_size") in upgrade scenarios.
- Fixed an issue that provided an incorrect value for the
  `threads_running` status variable when using Aurora Global
  Database.
- Fixed an issue where an Aurora MySQL binary log (binlog) read replica with
  [parallel secondary index optimization](../AuroraUserGuide/AuroraMySQL.Replication.MySQL.md#binlog-optimization "../AuroraUserGuide/AuroraMySQL.Replication.MySQL.md#binlog-optimization") enabled would experience a
  restart when applying replication changes on tables with foreign keys.
- [Aurora MySQL version 3.06.0](AuroraMySQL.Updates.3060.md "AuroraMySQL.Updates.3060.md")
  added support for Amazon Bedrock integration. As part of this, new reserved keywords
  (`accept`, `aws_bedrock_invoke_model`,
  `aws_sagemaker_invoke_endpoint`, `content_type`, and
  `timeout_ms`) were added. In Aurora MySQL version 3.06.1, these
  keywords have been changed to nonreserved keywords, which are permitted as
  identifiers without quoting. For more information on how MySQL handles reserved
  and nonreserved keywords, see [Keywords and
  reserved words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html "https://dev.mysql.com/doc/refman/8.0/en/keywords.html") in the MySQL documentation.
- Fixed an issue that didn't clearly return an error message to the client when
  invoking the Amazon Bedrock service from an Aurora MySQL DB cluster in an AWS Region where
  Amazon Bedrock isn't yet available.
- Fixed an issue that causes a DB instance to restart because of inaccurate lock
  holder information in `rw_lock` when using parallel reads.
- Fixed an issue that can cause a DB instance to restart when `SHOW VOLUME STATUS` is run.
- Fixed a memory management issue that led to a decrease in freeable memory over time when running `SELECT ... INTO OUTFILE ...` queries.
- Added support for the `connection_memory_limit` and
  `connection_memory_chunk_size` parameters to be set at the
  session level to behave similar to corresponding functionality in MySQL
  Community Edition. The `connection_memory_limit` parameter sets the
  maximum amount of memory that can be used by a single user connection. The
  `connection_memory_chunk_size` parameter sets the chunking size
  for updates to the [global memory usage counter](https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html#statvar_Global_connection_memory "https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html#statvar_Global_connection_memory").
- Fixed an issue that can cause a DB instance to restart when the local storage
  on the DB instance reaches full capacity.
- Fixed an issue where the Performance Schema wasn't enabled when Performance Insights automated
  management was turned on for db.t4g.medium and db.t4g.large DB instances.
- Fixed an issue that can cause a writer DB instance to restart when a reader DB instance using write forwarding runs a Data Manipulation Language (DML)
  statement that contains a timestamp value and the `time_zone` database parameter is set to `UTC`.
- Fixed an issue during zero-downtime patching (ZDP) that prevents a DB instance from closing client connections upon reaching the
  customer-configured minimum value of either `wait_timeout` or `interactive_timeout`.

**Upgrades and migrations:**

- Fixed an issue that causes upgrades or migrations to fail when the target
  Aurora MySQL DB engine version is 3.04.0 or higher. This occurs when the
  `lower_case_table_names` DB cluster parameter is set to
  `1`, and MySQL database collation is incompatible with lowercase
  table names.

## Integration of MySQL Community Edition bug fixes

This release includes all community bug fixes up to and including 8.0.34. For more
information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3 "AuroraMySQL.Updates.MySQLBugs.md#AuroraMySQL.Updates.MySQLBugs.v3").
