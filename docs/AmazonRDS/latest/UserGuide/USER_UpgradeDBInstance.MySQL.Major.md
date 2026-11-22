

# Major version upgrades for RDS for MySQL

Amazon RDS supports the following in-place upgrades for major versions of the MySQL database engine:
+ MySQL 5.7 to MySQL 8.0
+ MySQL 8.0 to MySQL 8.4
+ MySQL 8.4 to MySQL 9.7

**Note**  
You can only create MySQL version 5.7, 8.0, 8.4, and 9.7 DB instances with latest-generation and current-generation DB instance classes.   
In some cases, you want to upgrade a DB instance running on a previous-generation DB instance class to a DB instance with a higher MySQL engine version. In these cases, first modify the DB instance to use a latest-generation or current-generation DB instance class. After you do this, you can then modify the DB instance to use the higher MySQL database engine version. For information on Amazon RDS DB instance classes, see [DB instance classes](Concepts.DBInstanceClass.md).

**Topics**
+ [Overview of MySQL major version upgrades](#USER_UpgradeDBInstance.MySQL.Major.Overview)
+ [Upgrading to MySQL 9.7](#USER_UpgradeDBInstance.MySQL.Major.97)
+ [Prechecks for upgrades](#USER_UpgradeDBInstance.MySQL.Prechecks)
+ [Rollback after failure to upgrade](#USER_UpgradeDBInstance.MySQL.Major.RollbackAfterFailure)

## Overview of MySQL major version upgrades
<a name="USER_UpgradeDBInstance.MySQL.Major.Overview"></a>

Major version upgrades can contain database changes that are not backward-compatible with existing applications. As a result, Amazon RDS doesn't apply major version upgrades automatically; you must manually modify your DB instance. We recommend that you thoroughly test any upgrade before applying it to your production instances. 

To perform a major version upgrade, first perform any available OS updates. After OS updates are complete, upgrade to each major version, for example, 5.7 to 8.0, then 8.0 to 8.4, and then 8.4 to 9.7. For information about upgrading an RDS for MySQL Multi-AZ DB cluster, see [Upgrading the engine version of a Multi-AZ DB cluster for Amazon RDS](multi-az-db-clusters-upgrading.md). MySQL DB instances created before April 24, 2014, show an available OS update until the update has been applied. For more information on OS updates, see [Applying updates to a DB instance ](USER_UpgradeDBInstance.Maintenance.md#USER_UpgradeDBInstance.OSUpgrades). 

During a major version upgrade of MySQL, Amazon RDS runs the MySQL binary `mysql_upgrade` to upgrade tables, if necessary. Also, Amazon RDS empties the `slow_log` and `general_log` tables during a major version upgrade. To preserve log information, save the log contents before the major version upgrade. 

MySQL major version upgrades typically complete in about 10 minutes. Some upgrades might take longer because of the DB instance class size or because the instance doesn't follow certain operational guidelines in [Best practices for Amazon RDS](CHAP_BestPractices.md). If you upgrade a DB instance from the Amazon RDS console, the status of the DB instance indicates when the upgrade is complete. If you upgrade using the AWS Command Line Interface (AWS CLI), use the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command and check the `Status` value. 

## Upgrading to MySQL 9.7
<a name="USER_UpgradeDBInstance.MySQL.Major.97"></a>

MySQL 9.7 is a long-term support (LTS) release. It includes changes that aren't compatible with MySQL 8.4. Before you upgrade, review the following considerations.

Supported upgrade path  
You can upgrade to MySQL 9.7 only from MySQL 8.4. You can upgrade from any MySQL 8.4 minor version. If your DB instance runs MySQL 8.0, first upgrade it to MySQL 8.4. If your DB instance runs MySQL 5.7, upgrade one major version at a time: 5.7 to 8.0, 8.0 to 8.4, and then 8.4 to 9.7. Replication from a MySQL 5.7 source to a MySQL 9.7 replica isn't supported.  
MySQL 9.7 is available for Single-AZ DB instance deployments and Multi-AZ DB instance deployments. Multi-AZ DB clusters don't support MySQL 9.7.

Prechecks  
When you start an upgrade from MySQL 8.4 to 9.7, Amazon RDS runs prechecks to find incompatibilities. If a precheck finds an incompatibility, Amazon RDS cancels the upgrade before it stops the DB instance, and records the details in the `PrePatchCompatibility.log` file. Incompatibilities that block the upgrade include the following:  
+ A database account uses the `mysql_native_password` authentication plugin. MySQL 9.7 removes this plugin. On RDS for MySQL 8.4, the plugin is enabled by default. Before you upgrade, change these accounts to use `caching_sha2_password`, and make sure that your client drivers support `caching_sha2_password`. To find accounts that use `mysql_native_password`, run the following query:

  ```sql
  SELECT user, host FROM mysql.user WHERE plugin = 'mysql_native_password';
  ```

  To change an account, run a statement such as the following:

  ```sql
  ALTER USER '{{user}}'@'{{host}}' IDENTIFIED WITH caching_sha2_password BY '{{password}}';
  ```
+ Views, stored routines, triggers, events, generated columns, column defaults, `CHECK` constraints, or functional indexes use the `MD5()`, `SHA1()`, or `SHA()` functions. These functions aren't available on RDS for MySQL 9.7. Replace them with `SHA2()` or with hashing in your application. Also update any application SQL that calls these functions.
+ The SSL/TLS server certificate of the DB instance has expired. We recommend that you rotate the certificate authority (CA) of your DB instance before you upgrade. For more information, see [Rotating your SSL/TLS certificate](UsingWithRDS.SSL-certificate-rotation.md).
+ `CHECK TABLE ... FOR UPGRADE` reports errors for tables or views. For example, a view that references a table or column that no longer exists is reported as an error. Fix or drop these objects before you upgrade.
The precheck also reports warnings that don't block the upgrade. For example, it reports warnings for accounts that use the `sha256_password` authentication plugin, for foreign keys that reference a non-unique key or only part of a key, for the `validate_password` plugin, and for system variables whose default values change in MySQL 9.7.  
MySQL 9.7 adds the reserved keywords `EXTERNAL` and `LIBRARY`. If a stored procedure, stored function, trigger, or event uses either word as an unquoted identifier in its body, the precheck reports an error and the upgrade doesn't proceed. Quote the identifier with backticks, for example ``library``, and then retry the upgrade. Databases, tables, columns, views, and stored programs that are only named `EXTERNAL` or `LIBRARY` don't block the upgrade, and the precheck doesn't report them. However, after the upgrade, SQL statements that refer to them without backticks or a qualifier fail with a syntax error, so review your application queries before you upgrade. For more information, see [Keywords and Reserved Words](https://dev.mysql.com/doc/refman/9.7/en/keywords.html) in the MySQL documentation.  
For more information, see [Prechecks for upgrades from MySQL 8.4 to 9.7](#USER_UpgradeDBInstance.MySQL.84to97Prechecks).

TLS connections required by default  
In MySQL 9.7, `require_secure_transport` defaults to `1` (ON). In MySQL 8.4, the default is `0` (OFF). After the upgrade, clients must connect with SSL/TLS unless you set `require_secure_transport` to `0`. Before you upgrade, make sure that all of your clients connect with SSL/TLS. Or, use a custom DB parameter group in the `mysql9.7` family and set `require_secure_transport` to `0`. For more information, see [Encrypting client connections with SSL/TLS to MySQL DB instances on Amazon RDS](mysql-ssl-connections.md). For other parameter default changes, see [MySQL 9.7 support on Amazon RDS](MySQL.Concepts.FeatureSupport.md#MySQL.Concepts.FeatureSupport.9-7).

Spatial indexes  
If you upgrade from a MySQL version lower than 8.4.4 and your tables have spatial indexes, drop the spatial indexes before you upgrade, and recreate them after the upgrade completes. If you upgrade from MySQL 8.4.4 or higher, you don't need to do this.

Blue/Green Deployments  
We recommend that you use Amazon RDS Blue/Green Deployments to upgrade from MySQL 8.4 to 9.7. Create a blue/green deployment with a green environment that runs MySQL 9.7 and uses a DB parameter group in the `mysql9.7` family. Then test your applications against the green environment. When your tests pass, switch over to the green environment. The blue environment stays on MySQL 8.4 until you switch over, so you can test the upgrade without affecting production. For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](blue-green-deployments.md).  
Whether you use a blue/green deployment or an in-place upgrade, test the upgrade before you upgrade your production DB instance. For more information, see [Testing an RDS for MySQL upgrade](USER_UpgradeDBInstance.MySQL.UpgradeTesting.md).

Active-active clusters  
If you use active-active clusters, see [Synchronizing local GTIDs before a DB instance joins an active-active cluster (MySQL 9.7)](mysql-active-active-clusters-sync-gtids.md). For the default values of the TLS parameters for Group Replication, see [Required parameter settings for active-active clusters](mysql-active-active-clusters-parameters.md).

Reserved user `rdsproxyadmin`  
In MySQL 9.7, `rdsproxyadmin` is a reserved user. If you created a user named `rdsproxyadmin` yourself, not through RDS Proxy, drop or rename it before you upgrade. If RDS Proxy created the user, leave it in place.

Other behavior changes  
+ The default output format of `EXPLAIN` is now `TREE` instead of `TRADITIONAL`. If your tools parse `EXPLAIN` output, use `EXPLAIN FORMAT=TRADITIONAL`, or run `SET SESSION explain_format='TRADITIONAL'`.
+ Statements that use `IGNORE` now fail if a scalar subquery returns more than one row.
+ If you set `sql_require_primary_key` to `1`, a table that has a `UNIQUE NOT NULL` key is treated as having a primary key.
+ Review the Incompatible Change entries in the [MySQL 9.7 release notes](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/) and in the release notes for MySQL 9.0 through 9.6.

For information about the changes in MySQL 9.7, see [What is new in MySQL 9.7](https://dev.mysql.com/doc/refman/9.7/en/mysql-nutshell.html) and [Upgrading MySQL](https://dev.mysql.com/doc/refman/9.7/en/upgrading.html) in the MySQL documentation.

## Prechecks for upgrades
<a name="USER_UpgradeDBInstance.MySQL.Prechecks"></a>

Amazon RDS runs prechecks before upgrading to check for incompatibilities. These incompatibilities vary based on the MySQL version being upgraded to. 

The prechecks include some that are included with MySQL and some that were created specifically by the Amazon RDS team. For information about the prechecks provided by MySQL, see [Upgrade checker utility](https://dev.mysql.com/doc/mysql-shell/en/mysql-shell-utilities-upgrade.html). Amazon RDS runs its own build of the upgrade checker, so the results can differ from the results of the community version of MySQL Shell.

The prechecks run before the DB instance is stopped for the upgrade, meaning that they don't cause any downtime when they run. If the prechecks find an incompatibility, Amazon RDS automatically cancels the upgrade before the DB instance is stopped. Amazon RDS also generates an event for the incompatibility. For more information about Amazon RDS events, see [Working with Amazon RDS event notification](USER_Events.md).

Amazon RDS records detailed information about each incompatibility in the log file `PrePatchCompatibility.log`. In most cases, the log entry includes a link to the MySQL documentation for correcting the incompatibility. For more information about viewing log files, see [Viewing and listing database log files](USER_LogAccess.Procedural.Viewing.md).

Because of the nature of the prechecks, they analyze the objects in your database. This analysis results in resource consumption and increases the time for the upgrade to complete.

**Topics**
+ [Prechecks for upgrades from MySQL 8.4 to 9.7](#USER_UpgradeDBInstance.MySQL.84to97Prechecks)
+ [Prechecks for upgrades from MySQL 8.0 to 8.4](#USER_UpgradeDBInstance.MySQL.80to84Prechecks)
+ [Prechecks for upgrades from MySQL 5.7 to 8.0](#USER_UpgradeDBInstance.MySQL.57to80Prechecks)

### Prechecks for upgrades from MySQL 8.4 to 9.7
<a name="USER_UpgradeDBInstance.MySQL.84to97Prechecks"></a>

MySQL 9.7 has some incompatibilities with MySQL 8.4 that can cause an upgrade to fail. Before you upgrade, check your database for issues, including the following:
+ There must be no database accounts that use the `mysql_native_password` authentication plugin. MySQL 9.7 removes this plugin. Change these accounts to use `caching_sha2_password` before you upgrade.

  This check applies only to the accounts that you create. Amazon RDS migrates the accounts that it manages, such as `rdsadmin`, `rds_superuser_role`, `rdsrepladmin` (when you use read replicas), `rdsproxyadmin` (when RDS Proxy created it), and `rdszeroetladmin` (when you use zero-ETL integrations). You don't need to change these accounts.
+ There must be no views, stored routines, triggers, events, generated columns, column defaults, `CHECK` constraints, or functional indexes that use the `MD5()`, `SHA1()`, or `SHA()` functions. These functions aren't available on RDS for MySQL 9.7.
+ Stored procedures, stored functions, triggers, and events must not use `EXTERNAL` or `LIBRARY`, which are newly reserved in MySQL 9.7, as unquoted identifiers in their bodies. The precheck reports an error for these objects and blocks the upgrade. Objects that are only named `EXTERNAL` or `LIBRARY` aren't reported, but SQL that refers to them without backticks fails after the upgrade.

  For more information, see [Keywords and Reserved Words](https://dev.mysql.com/doc/refman/9.7/en/keywords.html) in the MySQL documentation.
+ The SSL/TLS server certificate of the DB instance must not be expired. We recommend that you rotate the certificate authority (CA) of your DB instance before you upgrade. For more information, see [Rotating your SSL/TLS certificate](UsingWithRDS.SSL-certificate-rotation.md).
+ There must be no tables or views that `CHECK TABLE ... FOR UPGRADE` reports as having errors. For example, a view that references a table or column that no longer exists is reported as an error. Fix or drop these objects before you upgrade.
+ We recommend that you change database accounts that use the deprecated `sha256_password` authentication plugin to use `caching_sha2_password`. The precheck reports a warning for these accounts. A warning doesn't block the upgrade.
+ We recommend that no foreign keys reference a non-unique key or only part of a unique key. The precheck reports a warning for these foreign keys. A warning doesn't block the upgrade. Before you upgrade, make the referenced key unique, or change the foreign key so that it references a primary key or a full unique key.
+ If the `validate_password` plugin is installed, the precheck reports a warning. A warning doesn't block the upgrade. The upgrade removes the plugin. To use password validation on MySQL 9.7, set the `rds.validate_password` parameter. For more information, see [Using password validation for MySQL 9.7](MySQL.Concepts.PasswordValidationPlugin.md#MySQL.Concepts.PasswordValidationPlugin.9-7).

The `PrePatchCompatibility.log` file also lists warnings for system variables whose default values change in MySQL 9.7. Some of these variables don't apply to RDS for MySQL. These warnings don't block the upgrade. For the default values that Amazon RDS uses, see [MySQL 9.7 support on Amazon RDS](MySQL.Concepts.FeatureSupport.md#MySQL.Concepts.FeatureSupport.9-7).

When you start an upgrade from MySQL 8.4 to 9.7, Amazon RDS runs prechecks automatically to detect these incompatibilities. For information about upgrading to MySQL 9.7, see [Upgrading to MySQL 9.7](#USER_UpgradeDBInstance.MySQL.Major.97) and [Upgrading MySQL](https://dev.mysql.com/doc/refman/9.7/en/upgrading.html) in the MySQL documentation.

These prechecks are mandatory. You can't choose to skip them. The prechecks provide the following benefits:
+ They help you avoid unplanned downtime during the upgrade.
+ If there are incompatibilities, Amazon RDS prevents the upgrade and provides a log for you to learn about them. You can then use the log to prepare your database for the upgrade to MySQL 9.7 by reducing the incompatibilities.

### Prechecks for upgrades from MySQL 8.0 to 8.4
<a name="USER_UpgradeDBInstance.MySQL.80to84Prechecks"></a>

MySQL 8.4 includes a number of incompatibilities with MySQL 8.0. These incompatibilities can cause problems during an upgrade from MySQL 8.0 to MySQL 8.4. So, some preparation might be required on your database for the upgrade to be successful. The following is a general list of these incompatibilities:
+ There must be no tables that use obsolete data types or functions.
+ Triggers must not have a missing or empty definer or an invalid creation context.
+ There must be no keyword or reserved word violations. Some keywords might be reserved in MySQL 8.4 that were not reserved previously.

  For more information, see [Keywords and reserved words](https://dev.mysql.com/doc/refman/8.4/en/keywords.html) in the MySQL documentation.
+ There must be no tables in the MySQL 8.0 `mysql` system database that have the same name as a table used by the MySQL 8.4 data dictionary.
+ There must be no obsolete SQL modes defined in your `sql_mode` system variable setting.
+ There must be no tables or stored procedures with individual `ENUM` or `SET` column elements that exceed 255 characters or 1020 bytes in length.
+ Your MySQL 8.0 installation must not use features that are not supported in MySQL 8.4.

  For more information, see [ Features removed in MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html#mysql-nutshell-removals) in the MySQL documentation.
+ There must be no foreign key constraint names longer than 64 characters.
+ For improved Unicode support, review the following information:
  + Consider converting objects that use the `utf8mb3` charset to use the `utf8mb4` charset. The `utf8mb3` character set is deprecated.
  + Consider using `utf8mb4` for character set references instead of `utf8`, because currently `utf8` is an alias for the `utf8mb3` charset. If possible, change `utf8` to `utf8mb4` first, and then upgrade your database. 
  + Because older clients can receive an unknown character set error for `utf8mb3`, upgrade your database clients before upgrading your database. 

  For more information, see [ The utf8mb3 character set (3-byte UTF-8 unicode encoding)](https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-utf8mb3.html) in the MySQL documentation.

  To change the character sets, you can manually perform a backup, restore, and replication of your database. Or you can use Amazon RDS Blue/Green Deployments. For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](blue-green-deployments.md).

When you start an upgrade from MySQL 8.0 to 8.4, Amazon RDS runs prechecks automatically to detect these incompatibilities. For information about upgrading to MySQL 8.4, see [Upgrading MySQL](https://dev.mysql.com/doc/refman/8.4/en/upgrading.html) in the MySQL documentation.

These prechecks are mandatory. You can't choose to skip them. The prechecks provide the following benefits:
+ They enable you to avoid unplanned downtime during the upgrade.
+ If there are incompatibilities, Amazon RDS prevents the upgrade and provides a log for you to learn about them. You can then use the log to prepare your database for the upgrade to MySQL 8.4 by reducing the incompatibilities. For detailed information about removing incompatibilities, see [ Preparing your installation for upgrade](https://dev.mysql.com/doc/refman/8.4/en/upgrade-prerequisites.html) in the MySQL documentation.

### Prechecks for upgrades from MySQL 5.7 to 8.0
<a name="USER_UpgradeDBInstance.MySQL.57to80Prechecks"></a>

MySQL 8.0 includes a number of incompatibilities with MySQL 5.7. These incompatibilities can cause problems during an upgrade from MySQL 5.7 to MySQL 8.0. So, some preparation might be required on your database for the upgrade to be successful. The following is a general list of these incompatibilities:
+ There must be no tables that use obsolete data types or functions.
+ There must be no orphan \*.frm files.
+ Triggers must not have a missing or empty definer or an invalid creation context.
+ There must be no partitioned table that uses a storage engine that does not have native partitioning support.
+ There must be no keyword or reserved word violations. Some keywords might be reserved in MySQL 8.0 that were not reserved previously.

  For more information, see [Keywords and reserved words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html) in the MySQL documentation.
+ There must be no tables in the MySQL 5.7 `mysql` system database that have the same name as a table used by the MySQL 8.0 data dictionary.
+ There must be no obsolete SQL modes defined in your `sql_mode` system variable setting.
+ There must be no tables or stored procedures with individual `ENUM` or `SET` column elements that exceed 255 characters or 1020 bytes in length.
+ Before upgrading to MySQL 8.0.13 or higher, there must be no table partitions that reside in shared InnoDB tablespaces.
+ There must be no queries and stored program definitions from MySQL 8.0.12 or lower that use `ASC` or `DESC` qualifiers for `GROUP BY` clauses.
+ Your MySQL 5.7 installation must not use features that are not supported in MySQL 8.0.

  For more information, see [ Features removed in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals) in the MySQL documentation.
+ There must be no foreign key constraint names longer than 64 characters.
+ For improved Unicode support, review the following information:
  + Consider converting objects that use the `utf8mb3` charset to use the `utf8mb4` charset. The `utf8mb3` character set is deprecated.
  + Consider using `utf8mb4` for character set references instead of `utf8`, because currently `utf8` is an alias for the `utf8mb3` charset. If possible, change `utf8` to `utf8mb4` first, and then upgrade your database. 
  + Because older clients can receive an unknown character set error for `utf8mb3`, upgrade your database clients before upgrading your database. 

  For more information, see [ The utf8mb3 character set (3-byte UTF-8 unicode encoding)](https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-utf8mb3.html) in the MySQL documentation.

  To change the character sets, you can manually perform a backup, restore, and replication of your database. Or you can use Amazon RDS Blue/Green Deployments. For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](blue-green-deployments.md).

When you start an upgrade from MySQL 5.7 to 8.0, Amazon RDS runs prechecks automatically to detect these incompatibilities. For information about upgrading to MySQL 8.0, see [Upgrading MySQL](https://dev.mysql.com/doc/refman/8.0/en/upgrading.html) in the MySQL documentation.

These prechecks are mandatory. You can't choose to skip them. The prechecks provide the following benefits:
+ They enable you to avoid unplanned downtime during the upgrade.
+ If there are incompatibilities, Amazon RDS prevents the upgrade and provides a log for you to learn about them. You can then use the log to prepare your database for the upgrade to MySQL 8.0 by reducing the incompatibilities. For detailed information about removing incompatibilities, see [ Preparing your installation for upgrade](https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html) in the MySQL documentation and [ Upgrading to MySQL 8.0? Here is what you need to know...](https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/) on the MySQL Server Blog.

## Rollback after failure to upgrade
<a name="USER_UpgradeDBInstance.MySQL.Major.RollbackAfterFailure"></a>

When you upgrade a DB instance from MySQL version 5.7 to MySQL version 8.0, from MySQL version 8.0 to 8.4, or from MySQL version 8.4 to 9.7, the upgrade can fail. In particular, it can fail if the data dictionary contains incompatibilities that weren't captured by the prechecks. In this case, the database fails to start up successfully in the new MySQL 8.0, 8.4, or 9.7 version. At this point, Amazon RDS rolls back the changes performed for the upgrade. After the rollback, the MySQL DB instance is running the original version:
+ MySQL version 8.4 (for a rollback from MySQL 9.7)
+ MySQL version 8.0 (for a rollback from MySQL 8.4)
+ MySQL version 5.7 (for a rollback from MySQL 8.0)

When an upgrade fails and is rolled back, Amazon RDS generates an event with the event ID RDS-EVENT-0188.

Typically, an upgrade fails because there are incompatibilities in the metadata between the databases in your DB instance and the target MySQL version. When an upgrade fails, you can view the details about these incompatibilities in the `upgradeFailure.log` file. Resolve the incompatibilities before attempting to upgrade again.

During an unsuccessful upgrade attempt and rollback, your DB instance is restarted. Any pending parameter changes are applied during the restart and persist after the rollback.

For more information about upgrading to MySQL 8.0, see the following topics in the MySQL documentation:
+ [ Preparing Your Installation for Upgrade](https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html)
+ [ Upgrading to MySQL 8.0? Here is what you need to know…](https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/)

For more information about upgrading to MySQL 8.4, see [ Preparing Your Installation for Upgrade](https://dev.mysql.com/doc/refman/8.4/en/upgrade-prerequisites.html) in the MySQL documentation.

For more information about upgrading to MySQL 9.7, see [ Preparing Your Installation for Upgrade](https://dev.mysql.com/doc/refman/9.7/en/upgrade-prerequisites.html) in the MySQL documentation.