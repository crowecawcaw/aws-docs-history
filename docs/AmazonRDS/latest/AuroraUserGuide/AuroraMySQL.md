# Major version upgrade prechecks for Aurora MySQL

Upgrading MySQL from one major version to another, such as going from MySQL 5.7 to MySQL 8.0, involves some significant architectural changes that
require careful planning and preparation. Unlike minor version upgrades where the focus is mainly on updating the database engine software and in some
cases system tables, major MySQL upgrades often introduce fundamental changes to how the database stores and manages its metadata.

To assist you in identifying such incompatibilities, when upgrading from Aurora MySQL version 2 to version 3, Aurora runs upgrade compatibility checks
(prechecks) automatically to examine objects in your database cluster and identify known incompatibilities that can block the upgrade from proceeding. For
details about the Aurora MySQL prechecks, see [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md"). The Aurora prechecks run in addition to those run by the Community MySQL [upgrade checker utility](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-utilities-upgrade.html "https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-utilities-upgrade.html").

These prechecks are mandatory. You can't choose to skip them. The prechecks provide the following benefits:

- They can reduce the possibility of running into upgrade failures that can lead to extended downtime.
- If there are incompatibilities, Amazon Aurora prevents the upgrade from proceeding and provides a log for you to learn about them. You can
  then use the log to prepare your database for the upgrade to version 3 by resolving the incompatibilities. For detailed information about resolving
  incompatibilities, see [Preparing your installation for
  upgrade](https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html "https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html") in the MySQL documentation and [Upgrading to MySQL 8.0? Here is what you need to know...](https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/ "https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/") on the MySQL Server Blog.

For more information about upgrading to MySQL 8.0, see [Upgrading MySQL](https://dev.mysql.com/doc/refman/8.0/en/upgrading.html "https://dev.mysql.com/doc/refman/8.0/en/upgrading.html") in the MySQL
documentation.
The prechecks run before your DB cluster is taken offline for the major version upgrade. If the prechecks find an incompatibility, Aurora
automatically cancels the upgrade before the DB instance is stopped. Aurora also generates an event for the incompatibility. For more information about
Amazon Aurora events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").

After the prechecks are completed, Aurora records detailed information about each incompatibility in the `upgrade-prechecks.log`
file. In most cases, the log entry includes a link to the MySQL documentation for correcting the incompatibility. For more information about viewing log
files, see [Viewing and listing database log files](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md").

###### Note

Due to the nature of the prechecks, they analyze the objects in your database. This analysis results in resource consumption and increases the time
for the upgrade to complete. For more information on precheck performance considerations, see [Precheck process for Aurora MySQL](#AuroraMySQL.upgrade-prechecks.process "#AuroraMySQL.upgrade-prechecks.process").

###### Contents

- [Precheck process for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.process "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.process")
- [Precheck log format for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-format "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-format")
- [Precheck log output examples for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-examples "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-examples")
- [Precheck performance for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.performance "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.performance")
- [Summary of Community MySQL upgrade prechecks](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.community "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.community")
- [Summary of Aurora MySQL upgrade prechecks](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.ams "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.ams")
- [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md")
  - [Errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors")
    - [MySQL prechecks that report errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.mysql "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.mysql")
    - [Aurora MySQL prechecks that report errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.aurora "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.aurora")

  - [Warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings")
    - [MySQL prechecks that report warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.mysql "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.mysql")
    - [Aurora MySQL prechecks that report warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.aurora "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.aurora")

  - [Notices](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-notices "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-notices")
  - [Errors, warnings, or notices](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-all "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-all")

## Precheck process for Aurora MySQL

As described previously, the Aurora MySQL upgrade process involves running compatibility checks (prechecks) on your database before the major version
upgrade can proceed.

For in-place upgrades, the prechecks run on your writer DB instance while it's online. If the precheck succeeds, the upgrade proceeds. If errors are
found, they're logged in the `upgrade-prechecks.log` file and the upgrade is canceled. Before attempting the upgrade again, resolve
any errors returned in the `upgrade-prechecks.log` file.

For snapshot-restore upgrades, the precheck runs during the restore process. If it succeeds, your database will upgrade to the new Aurora MySQL
version. If errors are found, they're logged in the `upgrade-prechecks.log` file and the upgrade is canceled. Before attempting the
upgrade again, resolve any errors returned in the `upgrade-prechecks.log` file.

For more information, see [Finding the reasons for Aurora MySQL major version upgrade failures](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md") and [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md").

To monitor precheck status, you can view the following events on your DB cluster.

| Precheck status | Event message                                                                                                                                                                                                                                                                                                                                                                                 | Action                                                                                                  |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Started         | Upgrade preparation in progress: Starting online upgrade prechecks.                                                                                                                                                                                                                                                                                                                           | None                                                                                                    |
| Failed          | Database cluster is in a state that cannot be upgraded: Upgrade prechecks failed. For more details, see the upgrade-prechecks.log<br>file.<br>For more information on troubleshooting the cause of the upgrade failure, see<br>[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Upgrading.Troubleshooting.html](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md") | Review `upgrade-prechecks.log` for errors.<br>Remediate errors.<br>Retry the upgrade.                   |
| Succeeded       | Upgrade preparation in progress: Completed online upgrade prechecks.                                                                                                                                                                                                                                                                                                                          | Precheck succeeded with no errors returned.<br>Review `upgrade-prechecks.log` for warnings and notices. |

For more information on viewing events, see [Viewing Amazon RDS events](USER_ListEvents.md "USER_ListEvents.md").

## Precheck log format for Aurora MySQL

After the upgrade compatibility checks (prechecks) are complete, you can review the `upgrade-prechecks.log` file. The log file
contains the results, affected objects, and remediation information for each precheck.

Errors block the upgrade. You must resolve them before retrying the upgrade.

Warnings and notices are less critical, but we still recommend that you review them carefully to make sure that there are no compatibility issues
with the application workload. Address any identified issues soon.

The log file has the following format:

- `targetVersion` – The MySQL-compatible version of the Aurora MySQL upgrade.
- `auroraServerVersion` – The Aurora MySQL version on which the precheck was run.
- `auroraTargetVersion` – The Aurora MySQL version to which you're upgrading.
- `checksPerformed` – Contains the list of prechecks performed.
- `id` – The name of the precheck being run.
- `title` – A description of the precheck being run.
- `status` – This doesn't indicate whether the precheck succeeded or failed, but shows the status of the precheck query:
  - `OK` – The precheck query ran and completed successfully.
  - `ERROR` – The precheck query failed to run. This can occur because of issues such as resource constraints, unexpected
    instance restarts, or the compatibility precheck query being interrupted.

  For more information, see [this example](#precheck-query-failed "#precheck-query-failed").

- `description` – A general description of the incompatibility, and how to remediate the issue.
- `documentationLink` – Where applicable, a link to relevant Aurora MySQL or MySQL documentation is noted here. For more
  information, see [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md").
- `detectedProblems` – If the precheck returns an error, warning, or notice, this shows details of the incompatibility, and
  incompatible objects where applicable:
  - `level` – The level of the incompatibility detected by the precheck. Valid levels are the following:
    - `Error` – The upgrade can't proceed until you resolve the incompatibility.
    - `Warning` – The upgrade can proceed, but a deprecated object, syntax, or configuration was detected. Review warnings
      carefully, and resolve them soon to avoid issues in future releases.
    - `Notice` – The upgrade can proceed, but a deprecated object, syntax, or configuration was detected. Review notices
      carefully, and resolve them soon to avoid issues in future releases.

  - `dbObject` – The name of the database object in which the incompatibility was detected.
  - `description` – A detailed description of the incompatibility, and how to remediate the issue.

- `errorCount` – The number of incompatibility errors detected. These block the upgrade.
- `warningCount` – The number of incompatibility warnings detected. These don't block the upgrade, but address them soon to
  avoid problems in future releases.
- `noticeCount` – The number of incompatibility notices detected. These don't block the upgrade, address them soon to avoid
  problems in future releases.
- `Summary` – A summary of the precheck compatibility error, warning, and notice counts.

## Precheck log output examples for Aurora MySQL

The following examples show the precheck log output that you might see. For details of the prechecks that are run, see [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md").

**Precheck status OK, no incompatibility detected**

The precheck query completed successfully. No incompatibilities were detected.

```
{
  "id": "auroraUpgradeCheckIndexLengthLimitOnTinytext",
  "title": "Check for the tables with indexes defined with prefix length greater than 255 bytes on tiny text columns",
  "status": "OK",
  "detectedProblems": []
},
```

**Precheck status OK, error detected**

The precheck query completed successfully. One error was detected.

```
{
  "id": "auroraUpgradeCheckForPrefixIndexOnGeometryColumns",
  "title": "Check for geometry columns on prefix indexes",
  "status": "OK",
  "description": "Consider dropping the prefix indexes of geometry columns and restart the upgrade.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test25.sbtest1",
        "description": "Table `test25`.`sbtest1` has an index `idx_t1` on geometry column/s. Mysql 8.0 does not support this type of index on a geometry column https://dev.mysql.com/worklog/task/?id=11808. To upgrade to MySQL 8.0, Run 'DROP INDEX `idx_t1` ON `test25`.`sbtest1`;"
      },
 }
```

**Precheck status OK, warning detected**

Warnings can be returned when a precheck is successful or unsuccessful.

Here the precheck query completed successfully. Two warnings were detected.

```
{
  "id": "zeroDatesCheck",
  "title": "Zero Date, Datetime, and Timestamp values",
  "status": "OK",
  "description": "Warning: By default zero date/datetime/timestamp values are no longer allowed in MySQL, as of 5.7.8 NO_ZERO_IN_DATE and NO_ZERO_DATE are included in SQL_MODE by default. These modes should be used with strict mode as they will be merged with strict mode in a future release. If you do not include these modes in your SQL_MODE setting, you are able to insert date/datetime/timestamp values that contain zeros. It is strongly advised to replace zero values with valid ones, as they may not work correctly in the future.",
  "documentationLink": "https://lefred.be/content/mysql-8-0-and-wrong-dates/",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "global.sql_mode",
        "description": "does not contain either NO_ZERO_DATE or NO_ZERO_IN_DATE which allows insertion of zero dates"
      },
      {
        "level": "Warning",
        "dbObject": "session.sql_mode",
        "description": " of 10 session(s) does not contain either NO_ZERO_DATE or NO_ZERO_IN_DATE which allows insertion of zero dates"
      }
    ]
}
```

**Precheck status ERROR, no incompatibilities reported**

The precheck query failed with an error, so incompatibilities couldn't be verified.

```
{
  "id": "auroraUpgradeCheckForDatafilePathInconsistency",
  "title": "Check for inconsistency related to ibd file path.",
  "status": "ERROR",
  "description": "Can't connect to MySQL server on 'localhost:3306' (111) at 13/08/2024 12:22:20 UTC. This failure can occur due to low memory available on the instance for executing upgrade prechecks. Please check 'FreeableMemory' Cloudwatch metric to verify the available memory on the instance while executing prechecks. If instance ran out of memory, we recommend to retry the upgrade on a higher instance class."
}
```

This failure can occur because of an unexpected instance restart or a compatibility precheck query being interrupted on the database while
running. For example, on smaller DB instance classes, you might experience this when the available memory on the instance runs low.

You can use the `FreeableMemory` Amazon CloudWatch metric to verify the available memory on the instance while running prechecks. If the
instance ran out of memory, we recommend retrying the upgrade on a larger DB instance class. In some cases, you can use a [Blue/Green deployment](blue-green-deployments-overview.md "blue-green-deployments-overview.md") This allows prechecks and upgrades to run on the “green” DB cluster
independent of the production workload, which also consumes system resources.

For more information, see [Troubleshooting memory usage issues for Aurora MySQL databases](ams-workload-memory.md "ams-workload-memory.md").

**Precheck summary, one error and three warnings detected**

The compatibility prechecks also contain information on the source and target Aurora MySQL versions, and a summary of error, warning, and notice
counts at the end of the precheck output.

For example, the following output shows that an attempt was made to upgrade from Aurora MySQL 2.11.6 to Aurora MySQL 3.07.1. The upgrade returned
one error, three warnings, and no notices. Because upgrades can't proceed when an error is returned, you must resolve the [routineSyntaxCheck](AuroraMySQL.upgrade-prechecks.md#routineSyntaxCheck "AuroraMySQL.upgrade-prechecks.md#routineSyntaxCheck") compatibility issue and retry the upgrade.

```
{
  "serverAddress": "/tmp%2Fmysql.sock",
  "serverVersion": "5.7.12 - MySQL Community Server (GPL)",
  "targetVersion": "8.0.36",
  "auroraServerVersion": "2.11.6",
  "auroraTargetVersion": "3.07.1",
  "outfilePath": "/rdsdbdata/tmp/PreChecker.log",
  "checksPerformed": [{
      ... output for each individual precheck ...
      .
      .
      {
        "id": "oldTemporalCheck",
        "title": "Usage of old temporal type",
        "status": "OK",
          "detectedProblems": []
      },
      {
        "id": "routinesSyntaxCheck",
        "title": "MySQL 8.0 syntax check for routine-like objects",
        "status": "OK",
        "description": "The following objects did not pass a syntax check with the latest MySQL 8.0 grammar. A common reason is that they reference names that conflict with new reserved keywords. You must update these routine definitions and `quote` any such references before upgrading.",
        "documentationLink": "https://dev.mysql.com/doc/refman/en/keywords.html",
        "detectedProblems": [{
            "level": "Error",
            "dbObject": "test.select_res_word",
            "description": "at line 2,18: unexpected token 'except'"
        }]
      },
      .
      .
      .
      {
        "id": "zeroDatesCheck",
        "title": "Zero Date, Datetime, and Timestamp values",
        "status": "OK",
        "description": "Warning: By default zero date/datetime/timestamp values are no longer allowed in MySQL, as of 5.7.8 NO_ZERO_IN_DATE and NO_ZERO_DATE are included in SQL_MODE by default. These modes should be used with strict mode as they will be merged with strict mode in a future release. If you do not include these modes in your SQL_MODE setting, you are able to insert date/datetime/timestamp values that contain zeros. It is strongly advised to replace zero values with valid ones, as they may not work correctly in the future.",
        "documentationLink": "https://lefred.be/content/mysql-8-0-and-wrong-dates/",
        "detectedProblems": [{
            "level": "Warning",
            "dbObject": "global.sql_mode",
            "description": "does not contain either NO_ZERO_DATE or NO_ZERO_IN_DATE which allows insertion of zero dates"
            },
            {
            "level": "Warning",
            "dbObject": "session.sql_mode",
            "description": " of 8 session(s) does not contain either NO_ZERO_DATE or NO_ZERO_IN_DATE which allows insertion of zero dates"
            }
          ]
       },
       .
       .
       .
  }],
  "errorCount": 1,
  "warningCount": 3,
  "noticeCount": 0,
  "Summary": "1 errors were found. Please correct these issues before upgrading to avoid compatibility issues."
}
```

## Precheck performance for Aurora MySQL

The compatibility prechecks run before the DB instance is taken offline for the upgrade, so under regular circumstances they don't cause DB instance
downtime while running. However, they can impact application workload running on the writer DB instance. The prechecks access the data dictionary through
[information_schema](https://dev.mysql.com/doc/mysql-infoschema-excerpt/5.7/en/information-schema-introduction.html "https://dev.mysql.com/doc/mysql-infoschema-excerpt/5.7/en/information-schema-introduction.html") tables, which
can be slow if there are many database objects. Consider the following factors:

- Precheck duration varies with the number of database objects such as tables, columns, routines, and constraints. DB clusters with a large number
  of objects can take longer to run.

For example, the [removedFunctionsCheck](AuroraMySQL.upgrade-prechecks.md#removedFunctionsCheck "AuroraMySQL.upgrade-prechecks.md#removedFunctionsCheck") can take longer and use more resources based on the number
of [stored objects](https://dev.mysql.com/doc/refman/5.7/en/stored-objects.html "https://dev.mysql.com/doc/refman/5.7/en/stored-objects.html").

- For in-place upgrades, using a larger DB instance class (for example, db.r5.24xlarge or db.r6g.16xlarge) can help the upgrade complete faster by
  using more CPU. You can downsize after the upgrade.
- Queries on the `information_schema` across multiple databases can be slow, especially with many objects and on smaller DB instances.
  In such cases, consider using cloning, snapshot restore, or a [Blue/Green deployment](blue-green-deployments-overview.md "blue-green-deployments-overview.md") for
  upgrades.
- Precheck resource usage (CPU, memory) can increase with more objects, leading to longer run times on smaller DB instances. In such cases,
  consider testing using cloning, snapshot restore, or a Blue/Green deployment for upgrades.

If the prechecks fail due to lack of resources, you can detect this in the precheck log using the status output:

```
"status": "ERROR",
```

For more information, see [How the Aurora MySQL in-place major version upgrade works](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence") and [Planning a major version upgrade for an Aurora MySQL cluster](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning").

## Summary of Community MySQL upgrade prechecks

The following is a general list of incompatibilities between MySQL 5.7 and 8.0:

- Your MySQL 5.7–compatible DB cluster must not use features that aren't supported in MySQL 8.0.

For more information, see [Features removed in
MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals") in the MySQL documentation.

- There must be no keyword or reserved word violations. Some keywords might be reserved in MySQL 8.0 that were not reserved previously.

For more information, see [Keywords and reserved words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html "https://dev.mysql.com/doc/refman/8.0/en/keywords.html") in the MySQL
documentation.

- For improved Unicode support, consider converting objects that use the `utf8mb3` charset to use the `utf8mb4` charset. The
  `utf8mb3` character set is deprecated. Also, consider using `utf8mb4` for character set references instead of
  `utf8`, because currently `utf8` is an alias for the `utf8mb3` charset.

For more information, see [The utf8mb3 character set (3-byte
UTF-8 unicode encoding)](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb3.html "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb3.html") in the MySQL documentation.

- There must be no InnoDB tables with a nondefault row format.
- There must be no `ZEROFILL` or `display` length type attributes.
- There must be no partitioned table that uses a storage engine that does not have native partitioning support.
- There must be no tables in the MySQL 5.7 `mysql` system database that have the same name as a table used by the MySQL 8.0 data
  dictionary.
- There must be no tables that use obsolete data types or functions.
- There must be no foreign key constraint names longer than 64 characters.
- There must be no obsolete SQL modes defined in your `sql_mode` system variable setting.
- There must be no tables or stored procedures with individual `ENUM` or `SET` column elements that exceed 255 characters in
  length.
- There must be no table partitions that reside in shared InnoDB tablespaces.
- There must be no circular references in tablespace data file paths.
- There must be no queries and stored program definitions that use `ASC` or `DESC` qualifiers for `GROUP BY`
  clauses.
- There must be no removed system variables, and system variables must use the new default values for MySQL 8.0.
- There must be no zero (`0`) date, datetime, or timestamp values.
- There must be no schema inconsistencies resulting from file removal or corruption.
- There must be no table names that contain the `FTS` character string.
- There must be no InnoDB tables that belong to a different engine.
- There must be no table or schema names that are invalid for MySQL 5.7.

For details of the prechecks that are run, see [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md").

For more information about upgrading to MySQL 8.0, see [Upgrading MySQL](https://dev.mysql.com/doc/refman/8.0/en/upgrading.html "https://dev.mysql.com/doc/refman/8.0/en/upgrading.html")
in the MySQL documentation. For a general description of changes in MySQL 8.0, see [What is new in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html") in the MySQL documentation.

## Summary of Aurora MySQL upgrade prechecks

Aurora MySQL has its own specific requirements when upgrading from version 2 to version 3, including the following:

- There must be no deprecated SQL syntax, such as `SQL_CACHE`, `SQL_NO_CACHE`, and `QUERY_CACHE`, in views,
  routines, triggers, and events.
- There must be no `FTS_DOC_ID` column present on any table without the `FTS` index.
- There must be no column definition mismatch between the InnoDB data dictionary and the actual table definition.
- All database and table names must be lowercase when the `lower_case_table_names` parameter is set to `1`.
- Events and triggers must not have a missing or empty definer or an invalid creation context.
- All trigger names in a database must be unique.
- DDL recovery and Fast DDL aren't supported in Aurora MySQL version 3. There must be no artifacts in databases related to these features.
- Tables with the `REDUNDANT` or `COMPACT` row format can't have indexes larger than 767 bytes.
- The prefix length of indexes defined on `tiny` text columns can't exceed 255 bytes. With the `utf8mb4` character set, this
  limits the prefix length supported to 63 characters.

A larger prefix length was allowed in MySQL 5.7 using the `innodb_large_prefix` parameter. This parameter is deprecated in MySQL
8.0.

- There must be no InnoDB metadata inconsistency in the `mysql.host` table.
- There must be no column data type mismatch in system tables.
- There must be no XA transactions in the `prepared` state.
- Column names in views can't be longer than 64 characters.
- Special characters in stored procedures can't be inconsistent.
- Tables can't have data file path inconsistency.

For details of the prechecks that are run, see [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md").
