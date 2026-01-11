# Major version upgrades for RDS for MySQL

Amazon RDS supports the following in-place upgrades for major versions of the MySQL database engine:

- MySQL 5.7 to MySQL 8.0
- MySQL 8.0 to MySQL 8.4

###### Note

You can only create MySQL version 5.7, 8.0, and 8.4 DB instances with
latest-generation and current-generation DB instance classes.

In some cases, you want to upgrade a DB instance running on a previous-generation
DB instance class to a DB instance with a higher MySQL engine version. In these
cases, first modify the DB instance to use a latest-generation or current-generation
DB instance class. After you do this, you can then modify the DB instance to use the
higher MySQL database engine version. For information on Amazon RDS DB instance classes,
see [DB instance classes](Concepts.md "Concepts.md").

###### Topics

- [Overview of MySQL
  major version upgrades](#USER_UpgradeDBInstance.MySQL.Major.Overview "#USER_UpgradeDBInstance.MySQL.Major.Overview")
- [Prechecks for
  upgrades](#USER_UpgradeDBInstance.MySQL.Prechecks "#USER_UpgradeDBInstance.MySQL.Prechecks")
- [Rollback after failure to upgrade](#USER_UpgradeDBInstance.MySQL.Major.RollbackAfterFailure "#USER_UpgradeDBInstance.MySQL.Major.RollbackAfterFailure")

## Overview of MySQL

major version upgrades

Major version upgrades can contain database changes that are not
backward-compatible with existing applications. As a result, Amazon RDS doesn't apply
major version upgrades automatically; you must manually modify your DB instance. We
recommend that you thoroughly test any upgrade before applying it to your production
instances.

To perform a major version upgrade, first perform any available OS updates. After
OS updates are complete, upgrade to each major version, for example, 5.7 to 8.0 and
then 8.0 to 8.4. For information about upgrading an RDS for MySQL Multi-AZ DB cluster, see [Upgrading the engine version of a Multi-AZ DB cluster for Amazon RDS](multi-az-db-clusters-upgrading.md "multi-az-db-clusters-upgrading.md"). MySQL DB instances created
before April 24, 2014, show an available OS update until the update has been
applied. For more information on OS updates, see [Applying updates to a DB instance](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.OSUpgrades "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.OSUpgrades").

During a major version upgrade of MySQL, Amazon RDS runs the MySQL binary
`mysql_upgrade` to upgrade tables, if necessary. Also, Amazon RDS empties
the `slow_log` and `general_log` tables during a major version
upgrade. To preserve log information, save the log contents before the major version
upgrade.

MySQL major version upgrades typically complete in about 10 minutes. Some upgrades
might take longer because of the DB instance class size or because the instance
doesn't follow certain operational guidelines in [Best practices for Amazon RDS](CHAP_BestPractices.md "CHAP_BestPractices.md"). If you upgrade a DB instance from the
Amazon RDS console, the status of the DB instance indicates when the upgrade is complete.
If you upgrade using the AWS Command Line Interface (AWS CLI), use the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
command and check the `Status` value.

## Prechecks for

upgrades

Amazon RDS runs prechecks before upgrading to check for incompatibilities. These
incompatibilities vary based on the MySQL version being upgraded to.

The prechecks include some that are included with MySQL and some that were created
specifically by the Amazon RDS team. For information about the prechecks provided by
MySQL, see [Upgrade checker utility](https://dev.mysql.com/doc/mysql-shell/8.4/en/mysql-shell-utilities-upgrade.html "https://dev.mysql.com/doc/mysql-shell/8.4/en/mysql-shell-utilities-upgrade.html").

The prechecks run before the DB instance is stopped for the upgrade, meaning that
they don't cause any downtime when they run. If the prechecks find an
incompatibility, Amazon RDS automatically cancels the upgrade before the DB instance is
stopped. Amazon RDS also generates an event for the incompatibility. For more information
about Amazon RDS events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").

Amazon RDS records detailed information about each incompatibility in the log file
`PrePatchCompatibility.log`. In most cases, the log entry includes a
link to the MySQL documentation for correcting the incompatibility. For more
information about viewing log files, see [Viewing and listing database log files](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md").

Because of the nature of the prechecks, they analyze the objects in your database.
This analysis results in resource consumption and increases the time for the upgrade
to complete.

###### Topics

- [Prechecks for
  upgrades from MySQL 8.0 to 8.4](#USER_UpgradeDBInstance.MySQL.80to84Prechecks "#USER_UpgradeDBInstance.MySQL.80to84Prechecks")
- [Prechecks for upgrades from MySQL 5.7 to 8.0](#USER_UpgradeDBInstance.MySQL.57to80Prechecks "#USER_UpgradeDBInstance.MySQL.57to80Prechecks")

### Prechecks for

upgrades from MySQL 8.0 to 8.4

MySQL 8.4 includes a number of incompatibilities with MySQL 8.0. These
incompatibilities can cause problems during an upgrade from MySQL 8.0 to MySQL 8.4.
So, some preparation might be required on your database for the upgrade to be
successful. The following is a general list of these incompatibilities:

- There must be no tables that use obsolete data types or functions.
- Triggers must not have a missing or empty definer or an invalid creation context.
- There must be no keyword or reserved word violations. Some keywords might
  be reserved in MySQL 8.4 that were not reserved previously.

For more information, see [Keywords
and reserved words](https://dev.mysql.com/doc/refman/8.4/en/keywords.html "https://dev.mysql.com/doc/refman/8.4/en/keywords.html") in the MySQL documentation.

- There must be no tables in the MySQL 8.0 `mysql` system
  database that have the same name as a table used by the MySQL 8.4 data
  dictionary.
- There must be no obsolete SQL modes defined in your `sql_mode` system variable setting.
- There must be no tables or stored procedures with individual `ENUM` or `SET` column elements
  that exceed 255 characters or 1020 bytes in length.
- Your MySQL 8.0 installation must not use features that are not supported
  in MySQL 8.4.

For more information, see [Features removed in MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html#mysql-nutshell-removals "https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html#mysql-nutshell-removals") in the MySQL documentation.

- There must be no foreign key constraint names longer than 64 characters.
- For improved Unicode support, review the following information:

      + Consider converting objects that use the `utf8mb3`
       charset to use the `utf8mb4` charset. The
       `utf8mb3` character set is deprecated.
      + Consider using `utf8mb4` for character set
       references instead of `utf8`, because currently
       `utf8` is an alias for the `utf8mb3`
       charset. If possible, change `utf8` to
       `utf8mb4` first, and then upgrade your database.
      + Because older clients can receive an unknown character set
       error for `utf8mb3`, upgrade your database clients
       before upgrading your database.

  For more information, see [The utf8mb3 character set (3-byte UTF-8 unicode encoding)](https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-utf8mb3.html "https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-utf8mb3.html")
  in the MySQL documentation.

To change the character sets, you can manually perform a backup,
restore, and replication of your database. Or you can use Amazon RDS
Blue/Green Deployments. For more information, see [Using Amazon RDS Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

When you start an upgrade from MySQL 8.0 to 8.4, Amazon RDS runs prechecks
automatically to detect these incompatibilities. For information about upgrading to
MySQL 8.4, see [Upgrading MySQL](https://dev.mysql.com/doc/refman/8.4/en/upgrading.html "https://dev.mysql.com/doc/refman/8.4/en/upgrading.html") in the MySQL documentation.

These prechecks are mandatory. You can't choose to skip them. The prechecks provide the following benefits:

- They enable you to avoid unplanned downtime during the upgrade.
- If there are incompatibilities, Amazon RDS prevents the upgrade and provides a
  log for you to learn about them. You can then use the log to prepare your
  database for the upgrade to MySQL 8.4 by reducing the incompatibilities. For
  detailed information about removing incompatibilities, see [Preparing your installation for upgrade](https://dev.mysql.com/doc/refman/8.4/en/upgrade-prerequisites.html "https://dev.mysql.com/doc/refman/8.4/en/upgrade-prerequisites.html") in the MySQL
  documentation.

### Prechecks for upgrades from MySQL 5.7 to 8.0

MySQL 8.0 includes a number of incompatibilities with MySQL 5.7. These incompatibilities can cause problems during an upgrade from
MySQL 5.7 to MySQL 8.0. So, some preparation might be required on your database for the upgrade to be successful. The following is
a general list of these incompatibilities:

- There must be no tables that use obsolete data types or functions.
- There must be no orphan \*.frm files.
- Triggers must not have a missing or empty definer or an invalid creation context.
- There must be no partitioned table that uses a storage engine that does not have native partitioning support.
- There must be no keyword or reserved word violations. Some keywords might be reserved in MySQL 8.0
  that were not reserved previously.

For more information, see [Keywords
and reserved words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html "https://dev.mysql.com/doc/refman/8.0/en/keywords.html") in the MySQL documentation.

- There must be no tables in the MySQL 5.7 `mysql` system database that have the same name as a
  table used by the MySQL 8.0 data dictionary.
- There must be no obsolete SQL modes defined in your `sql_mode` system variable setting.
- There must be no tables or stored procedures with individual `ENUM` or `SET` column elements
  that exceed 255 characters or 1020 bytes in length.
- Before upgrading to MySQL 8.0.13 or higher, there must be no table partitions that reside in shared InnoDB tablespaces.
- There must be no queries and stored program definitions from MySQL 8.0.12 or lower that use `ASC` or `DESC`
  qualifiers for `GROUP BY` clauses.
- Your MySQL 5.7 installation must not use features that are not supported in MySQL 8.0.

For more information, see [Features removed in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals") in the MySQL documentation.

- There must be no foreign key constraint names longer than 64 characters.
- For improved Unicode support, review the following information:

      + Consider converting objects that use the `utf8mb3`
       charset to use the `utf8mb4` charset. The
       `utf8mb3` character set is deprecated.
      + Consider using `utf8mb4` for character set
       references instead of `utf8`, because currently
       `utf8` is an alias for the `utf8mb3`
       charset. If possible, change `utf8` to
       `utf8mb4` first, and then upgrade your database.
      + Because older clients can receive an unknown character set
       error for `utf8mb3`, upgrade your database clients
       before upgrading your database.

  For more information, see [The utf8mb3 character set (3-byte UTF-8 unicode encoding)](https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-utf8mb3.html "https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-utf8mb3.html")
  in the MySQL documentation.

To change the character sets, you can manually perform a backup,
restore, and replication of your database. Or you can use Amazon RDS
Blue/Green Deployments. For more information, see [Using Amazon RDS Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

When you start an upgrade from MySQL 5.7 to 8.0, Amazon RDS runs prechecks automatically to detect these incompatibilities. For information
about upgrading to MySQL 8.0, see [Upgrading MySQL](https://dev.mysql.com/doc/refman/8.0/en/upgrading.html "https://dev.mysql.com/doc/refman/8.0/en/upgrading.html")
in the MySQL documentation.

These prechecks are mandatory. You can't choose to skip them. The prechecks provide the following benefits:

- They enable you to avoid unplanned downtime during the upgrade.
- If there are incompatibilities, Amazon RDS prevents the upgrade and provides a
  log for you to learn about them. You can then use the log to prepare your
  database for the upgrade to MySQL 8.0 by reducing the incompatibilities. For
  detailed information about removing incompatibilities, see [Preparing your installation for upgrade](https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html "https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html") in the MySQL
  documentation and [Upgrading to MySQL 8.0? Here is what you need to know...](https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/ "https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/") on
  the MySQL Server Blog.

## Rollback after failure to upgrade

When you upgrade a DB instance from MySQL version 5.7 to MySQL version 8.0 or from
MySQL version 8.0 to 8.4, the upgrade can fail. In particular, it can fail if the
data dictionary contains incompatibilities that weren't captured by the
prechecks. In this case, the database fails to start up successfully in the new
MySQL 8.0 or 8.4 version. At this point, Amazon RDS rolls back the changes performed for
the upgrade. After the rollback, the MySQL DB instance is running the original
version:

- MySQL version 8.0 (for a rollback from MySQL 8.4)
- MySQL version 5.7 (for a rollback from MySQL 8.0)

When an upgrade fails and is rolled
back, Amazon RDS generates an event with the event ID RDS-EVENT-0188.

Typically, an upgrade fails because there are incompatibilities in the metadata
between the databases in your DB instance and the target MySQL version. When an
upgrade fails, you can view the details about these incompatibilities in the
`upgradeFailure.log` file. Resolve the incompatibilities
before attempting to upgrade again.

During an unsuccessful upgrade attempt and rollback, your DB instance is
restarted. Any pending parameter changes are applied during the restart and persist
after the rollback.

For more information about upgrading to MySQL 8.0, see the following topics in the MySQL documentation:

- [Preparing Your Installation for Upgrade](https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html "https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html")
- [Upgrading to MySQL 8.0? Here is what you need to know…](https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/ "https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/")

For more information about upgrading to MySQL 8.4, see [Preparing Your Installation for Upgrade](https://dev.mysql.com/doc/refman/8.4/en/upgrade-prerequisites.html "https://dev.mysql.com/doc/refman/8.4/en/upgrade-prerequisites.html") in the MySQL
documentation.
