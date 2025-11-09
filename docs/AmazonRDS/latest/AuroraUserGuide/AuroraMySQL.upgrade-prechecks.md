# Precheck descriptions reference for Aurora MySQL

The upgrade prechecks for Aurora MySQL are described here in detail.

###### Contents

- [Errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors")
  - [MySQL prechecks that report errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.mysql "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.mysql")
  - [Aurora MySQL prechecks that report errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.aurora "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.aurora")

- [Warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings")
  - [MySQL prechecks that report warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.mysql "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.mysql")
  - [Aurora MySQL prechecks that report warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.aurora "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.aurora")

- [Notices](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-notices "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-notices")
- [Errors, warnings, or notices](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-all "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-all")

## Errors

The following prechecks generate errors when the precheck fails, and the upgrade can't proceed.

###### Topics

- [MySQL prechecks that report errors](#precheck-descriptions-errors.mysql "#precheck-descriptions-errors.mysql")
- [Aurora MySQL prechecks that report errors](#precheck-descriptions-errors.aurora "#precheck-descriptions-errors.aurora")

### MySQL prechecks that report errors

The following prechecks are from Community MySQL:

- [checkTableMysqlSchema](#checkTableMysqlSchema "#checkTableMysqlSchema")
- [circularDirectoryCheck](#circularDirectoryCheck "#circularDirectoryCheck")
- [columnsWhichCannotHaveDefaultsCheck](#columnsWhichCannotHaveDefaultsCheck "#columnsWhichCannotHaveDefaultsCheck")
- [depreciatedSyntaxCheck](#depreciatedSyntaxCheck "#depreciatedSyntaxCheck")
- [engineMixupCheck](#engineMixupCheck "#engineMixupCheck")
- [enumSetElementLengthCheck](#enumSetElementLengthCheck "#enumSetElementLengthCheck")
- [foreignKeyLengthCheck](#foreignKeyLengthCheck "#foreignKeyLengthCheck")
- [getDuplicateTriggers](#getDuplicateTriggers "#getDuplicateTriggers")
- [getEventsWithNullDefiner](#getEventsWithNullDefiner "#getEventsWithNullDefiner")
- [getMismatchedMetadata](#getMismatchedMetadata "#getMismatchedMetadata")
- [getTriggersWithNullDefiner](#getTriggersWithNullDefiner "#getTriggersWithNullDefiner")
- [getValueOfVariablelower_case_table_names](#getValueOfVariable "#getValueOfVariable")
- [groupByAscSyntaxCheck](#groupByAscSyntaxCheck "#groupByAscSyntaxCheck")
- [mysqlEmptyDotTableSyntaxCheck](#mysqlEmptyDotTableSyntaxCheck "#mysqlEmptyDotTableSyntaxCheck")
- [mysqlIndexTooLargeCheck](#mysqlIndexTooLargeCheck "#mysqlIndexTooLargeCheck")
- [mysqlInvalid57NamesCheck](#mysqlInvalid57NamesCheck "#mysqlInvalid57NamesCheck")
- [mysqlOrphanedRoutinesCheck](#mysqlOrphanedRoutinesCheck "#mysqlOrphanedRoutinesCheck")
- [mysqlSchemaCheck](#mysqlSchemaCheck "#mysqlSchemaCheck")
- [nonNativePartitioningCheck](#nonNativePartitioningCheck "#nonNativePartitioningCheck")
- [oldTemporalCheck](#oldTemporalCheck "#oldTemporalCheck")
- [partitionedTablesInSharedTablespaceCheck](#partitionedTablesInSharedTablespace "#partitionedTablesInSharedTablespace")
- [removedFunctionsCheck](#removedFunctionsCheck "#removedFunctionsCheck")
- [routineSyntaxCheck](#routineSyntaxCheck "#routineSyntaxCheck")
- [schemaInconsistencyCheck](#schemaInconsistencyCheck "#schemaInconsistencyCheck")

**checkTableMysqlSchema**

**Precheck level: Error**

**Issues reported by the `check table x for upgrade` command for the `mysql`
schema**

Before starting the upgrade to Aurora MySQL version 3, `check table for upgrade` is run on each table in the
`mysql` schema on the DB instance. The `check table for upgrade` command examines tables for any potential
issues that might arise during an upgrade to a newer version of MySQL. Running this command before attempting an upgrade can help
identify and resolve any incompatibilities ahead of time, making the actual upgrade process smoother.

This command performs various checks on each table, such as the following:

- Verifying that the table structure and metadata are compatible with the target MySQL version
- Checking for any deprecated or removed features used by the table
- Ensuring that the table can be properly upgraded without data loss

For more information, see [CHECK TABLE statement](https://dev.mysql.com/doc/refman/5.7/en/check-table.html "https://dev.mysql.com/doc/refman/5.7/en/check-table.html") in
the MySQL documentation.

**Example output:**

```
{
  "id": "checkTableMysqlSchema",
  "title": "Issues reported by 'check table x for upgrade' command for mysql schema.",
  "status": "OK",
  "detectedProblems": []
}
```

The output for this precheck depends on the error encountered, and when it's encountered, because `check table for
 upgrade` performs multiple checks.

If you encounter any errors with this precheck, open a case with [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support")
to request that the metadata inconsistency be resolved. Alternatively, you can retry the upgrade by performing a logical dump, then
restoring to a new Aurora MySQL version 3 DB cluster.

**circularDirectoryCheck**

**Precheck level: Error**

**Circular directory references in tablespace data file paths**

As of [MySQL 8.0.17](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-17.html "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-17.html"), the `CREATE
 TABLESPACE ... ADD DATAFILE` clause no longer permits circular directory references. To avoid upgrade issues, remove any
circular directory references from tablespace data file paths before upgrading to Aurora MySQL version 3.

**Example output:**

```
{
  "id": "circularDirectory",
  "title": "Circular directory references in tablespace data file paths",
  "status": "OK",
  "description": "Error: Following tablespaces contain circular directory references (e.g. the reference '/../') in data file paths which as of MySQL 8.0.17 are not permitted by the CREATE TABLESPACE ... ADD DATAFILE clause. An exception to the restriction exists on Linux, where a circular directory reference is permitted if the preceding directory is a symbolic link. To avoid upgrade issues, remove any circular directory references from tablespace data file paths before upgrading.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-innodb-changes",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "ts2",
        "description": "circular reference in datafile path: '/home/ec2-user/dbdata/mysql_5_7_44/../ts2.ibd'",
        "dbObjectType": "Tablespace"
      }
  ]
}
```

If you receive this error, rebuild your tables using a [file-per-table tablespace](https://dev.mysql.com/doc/refman/8.0/en/innodb-file-per-table-tablespaces.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-file-per-table-tablespaces.html"). Use
default file paths for all tablespace and table definitions.

###### Note

Aurora MySQL doesn't support general tablespaces or `CREATE TABLESPACE` commands.

Before rebuilding tablespaces, see [Online DDL operations](https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html") in the MySQL documentation to understand the effects of locking and data movement on
foreground transactions.

After rebuilding, the precheck passes, allowing the upgrade to proceed.

```
{
  "id": "circularDirectoryCheck",
  "title": "Circular directory references in tablespace data file paths",
  "status": "OK",
  "detectedProblems": []
},
```

**columnsWhichCannotHaveDefaultsCheck**

**Precheck level: Error**

**Columns that can't have default values**

Before MySQL 8.0.13, `BLOB`, `TEXT`, `GEOMETRY`, and `JSON` columns can't have [default values](https://dev.mysql.com/doc/refman/5.7/en/data-type-defaults.html "https://dev.mysql.com/doc/refman/5.7/en/data-type-defaults.html"). Remove any default clauses on
these columns before upgrading to Aurora MySQL version 3. For more information on changes to the default handling for these data
types, see the [Data type default values](https://dev.mysql.com/doc/refman/8.0/en/data-type-defaults.html "https://dev.mysql.com/doc/refman/8.0/en/data-type-defaults.html") in the
MySQL documentation.

**Example output:**

```
{
  "id": "columnsWhichCannotHaveDefaultsCheck",
  "title": "Columns which cannot have default values",
  "status": "OK",
  "description": "Error: The following columns are defined as either BLOB, TEXT, GEOMETRY or JSON and have a default value set. These data types cannot have default values in MySQL versions prior to 8.0.13, while starting with 8.0.13, the default value must be specified as an expression. In order to fix this issue, please use the ALTER TABLE ... ALTER COLUMN ... DROP DEFAULT statement.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/data-type-defaults.html#data-type-defaults-explicit",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.test_blob_default.geo_col",
        "description": "geometry"
      }
  ]
},
```

The precheck returns an error because the `geo_col` column in the `test.test_blob_default` table is using a
`BLOB`, `TEXT`, `GEOMETRY`, or `JSON` data type with a default value
specified.

Looking at the table definition, we can see that the `geo_col` column is defined as `geo_col geometry NOT NULL
 default ''`.

```
mysql> show create table test_blob_default\G
*************************** 1. row ***************************
       Table: test_blob_default
Create Table: CREATE TABLE `test_blob_default` (
  `geo_col` geometry NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

Removing this default clause to allow the precheck to pass.

###### Note

Before running `ALTER TABLE` statements or rebuilding tablespaces, see [Online DDL operations](https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html") in the MySQL
documentation to understand the effects of locking and data movement on foreground transactions.

```
mysql> ALTER TABLE test_blob_default modify COLUMN geo_col geometry NOT NULL;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show create table test_blob_default\G
*************************** 1. row ***************************
       Table: test_blob_default
Create Table: CREATE TABLE `test_blob_default` (
  `geo_col` geometry NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
1 row in set (0.00 sec)
```

The precheck passes, and you can retry the upgrade.

```
{
  "id": "columnsWhichCannotHaveDefaultsCheck",
  "title": "Columns which cannot have default values",
  "status": "OK",
  "detectedProblems": []
},
```

**depreciatedSyntaxCheck**

**Precheck level: Error**

**Usage of depreciated keywords in definition**

MySQL 8.0 has removed the [query cache](https://dev.mysql.com/doc/refman/5.7/en/query-cache.html "https://dev.mysql.com/doc/refman/5.7/en/query-cache.html"). As a result,
some query cache–specific SQL syntax has been removed. If any of your database objects contain the `QUERY CACHE`,
`SQL_CACHE`, or `SQL_NO_CACHE` keywords, a precheck error is returned. To resolve this issue, re-create
these objects, removing the mentioned keywords.

**Example output:**

```
{
  "id": "depreciatedSyntaxCheck",
  "title": "Usage of depreciated keywords in definition",
  "status": "OK",
  "description": "Error: The following DB objects contain keywords like 'QUERY CACHE', 'SQL_CACHE', 'SQL_NO_CACHE' which are not supported in major version 8.0. It is recommended to drop these DB objects or rebuild without any of the above keywords before upgrade.",
  "detectedProblems": [
      {
"level": "Error",
"dbObject": "test.no_query_cache_check",
"description": "PROCEDURE uses depreciated words in definition"
      }
  ]
}
```

The precheck reports that the `test.no_query_cache_check` stored procedure is using one of the removed keywords.
Looking at the procedure definition, we can see that it uses `SQL_NO_CACHE`.

```
mysql> show create procedure test.no_query_cache_check\G
*************************** 1. row ***************************
           Procedure: no_query_cache_check
            sql_mode:
    Create Procedure: CREATE DEFINER=`reinvent`@`%` PROCEDURE `no_query_cache_check`()
BEGIN
    SELECT SQL_NO_CACHE k from sbtest1 where id > 10 and id < 20 group by k asc;
END
character_set_client: utf8mb4
collation_connection: utf8mb4_0900_ai_ci
  Database Collation: latin1_swedish_ci
1 row in set (0.00 sec)
```

Remove the keyword.

```
mysql> drop procedure test.no_query_cache_check;
Query OK, 0 rows affected (0.01 sec)

mysql> delimiter //

mysql> CREATE DEFINER=`reinvent`@`%` PROCEDURE `no_query_cache_check`() BEGIN     SELECT k from sbtest1 where id > 10 and id < 20 group by k asc; END//
Query OK, 0 rows affected (0.00 sec)

mysql> delimiter ;
```

After removing the keyword, the precheck completes successfully.

```
{
  "id": "depreciatedSyntaxCheck",
  "title": "Usage of depreciated keywords in definition",
  "status": "OK",
  "detectedProblems": []
}
```

**engineMixupCheck**

**Precheck level: Error**

**Tables recognized by InnoDB that belong to a different engine**

Similar to [schemaInconsistencyCheck](#schemaInconsistencyCheck "#schemaInconsistencyCheck"), this precheck verifies that table metadata in
MySQL is consistent before proceeding with the upgrade.

If you encounter any errors with this precheck, open a case with [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support")
to request that the metadata inconsistency be resolved. Alternatively, you can retry the upgrade by performing a logical dump, then
restoring to a new Aurora MySQL version 3 DB cluster.

**Example output:**

```
{
  "id": "engineMixupCheck",
  "title": "Tables recognized by InnoDB that belong to a different engine",
  "status": "OK",
  "description": "Error: Following tables are recognized by InnoDB engine while the SQL layer believes they belong to a different engine. Such situation may happen when one removes InnoDB table files manually from the disk and creates e.g. a MyISAM table with the same name.\n\nA possible way to solve this situation is to e.g. in case of MyISAM table:\n\n1. Rename the MyISAM table to a temporary name (RENAME TABLE).\n2. Create some dummy InnoDB table (its definition does not need to match), then copy (copy, not move) and rename the dummy .frm and .ibd files to the orphan name using OS file commands.\n3. The orphan table can be then dropped (DROP TABLE), as well as the dummy table.\n4. Finally the MyISAM table can be renamed back to its original name.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "mysql.general_log_backup",
        "description": "recognized by the InnoDB engine but belongs to CSV"
      }
  ]
}
```

**enumSetElementLengthCheck**

**Precheck level: Error**

**`ENUM` and `SET` column definitions containing elements longer than 255
characters**

Tables and stored procedures must not have `ENUM` or `SET` column elements exceeding 255 characters or 1020
bytes. Before MySQL 8.0, the maximum combined length was 64K, but 8.0 limits individual elements to 255 characters or 1020 bytes
(supporting multibyte). If you get a precheck failure for `enumSetElementLengthCheck`, modify any elements exceeding
these new limits before retrying the upgrade.

**Example output:**

```
{
  "id": "enumSetElementLengthCheck",
  "title": "ENUM/SET column definitions containing elements longer than 255 characters",
  "status": "OK",
  "description": "Error: The following columns are defined as either ENUM or SET and contain at least one element longer that 255 characters. They need to be altered so that all elements fit into the 255 characters limit.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/string-type-overview.html",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.large_set.s",
        "description": "SET contains element longer than 255 characters"
      }
  ]
},
```

The precheck reports an error because the column `s` in the `test.large_set` table contains a
`SET` element larger than 255 characters.

After reducing the `SET` size for this column, the precheck passes, allowing the upgrade to proceed.

```
{
  "id": "enumSetElementLenghtCheck",
  "title": "ENUM/SET column definitions containing elements longer than 255 characters",
  "status": "OK",
  "detectedProblems": []
},
```

**foreignKeyLengthCheck**

**Precheck level: Error**

**Foreign key constraint names longer than 64 characters**

In MySQL, the length of identifiers is limited to 64 characters, as outlined in the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/identifier-length.html "https://dev.mysql.com/doc/refman/8.0/en/identifier-length.html"). Due to [issues](https://bugs.mysql.com/bug.php?id=88118 "https://bugs.mysql.com/bug.php?id=88118") identified where foreign key lengths could equal or exceed this
value, leading to upgrade failures, this precheck was implemented. If you encounter errors with this precheck you should [alter or rename](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html "https://dev.mysql.com/doc/refman/8.0/en/alter-table.html") your constraint so that it is less than
64 characters before retrying the upgrade.

**Example output:**

```
{
  "id": "foreignKeyLength",
  "title": "Foreign key constraint names longer than 64 characters",
  "status": "OK",
  "detectedProblems": []
}
```

**getDuplicateTriggers**

**Precheck level: Error**

**All trigger names in a database must be unique.**

Due to changes in the data dictionary implementation, MySQL 8.0 doesn't support case-sensitive triggers within a database. This
precheck validates that your DB cluster doesn’t have one or more databases containing duplicate triggers. For more information, see
[Identifier case sensitivity](https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html "https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html") in the
MySQL documentation.

**Example output:**

```
{
  "id": "getDuplicateTriggers",
  "title": "MySQL pre-checks that all trigger names in a database are unique or not.",
  "status": "OK",
  "description": "Error: You have one or more database containing duplicate triggers. Mysql 8.0 does not support case sensitive triggers within a database https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html. To upgrade to MySQL 8.0, drop the triggers with case-insensitive duplicate names and recreate with distinct names.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test",
        "description": "before_insert_product"
      },
      {
        "level": "Error",
        "dbObject": "test",
        "description": "before_insert_PRODUCT"
      }
  ]
}
```

The precheck reports an error that the database cluster has two triggers with the same name, but using different cases:
`test.before_insert_product` and `test.before_insert_PRODUCT`.

Before upgrading, rename the triggers or drop and re-create them with a new name.

After renaming `test.before_insert_PRODUCT` to `test.before_insert_product_2`, the precheck
succeeds.

```
{
  "id": "getDuplicateTriggers",
  "title": "MySQL pre-checks that all trigger names in a database are unique or not.",
  "status": "OK",
  "detectedProblems": []
}
```

**getEventsWithNullDefiner**

**Precheck level: Error**

**The definer column for `mysql.event` can't be null or blank.**

The `DEFINER` attribute specifies the MySQL account that owns a stored object definition, such as a trigger, stored
procedure, or event. This attribute is particularly useful in situations where you want to control the security context under which
the stored object runs. When creating a stored object, if a `DEFINER` isn't specified, the default is the user who
created the object.

When upgrading to MySQL 8.0, you can't have any stored objects that have a `null` or blank definer in the MySQL data
dictionary. If you have such stored objects, a precheck error is raised. You must fix it before the upgrade can proceed.

Example error:

```
{
  "id": "getEventsWithNullDefiner",
  "title": "The definer column for mysql.event cannot be null or blank.",
  "status": "OK",
  "description": "Error: Set definer column in mysql.event to a valid non-null definer.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.get_version",
        "description": "Set definer for event get_version in Schema test"
      }
  ]
}
```

The precheck returns an error for the `test.get_version`
[event](https://dev.mysql.com/doc/refman/5.7/en/events-overview.html "https://dev.mysql.com/doc/refman/5.7/en/events-overview.html") because it has a `null`
definer.

To resolve this you can check the event definition. As you can see, the definer is `null` or blank.

```
mysql> select db,name,definer from mysql.event where name='get_version';
+------+-------------+---------+
| db   | name        | definer |
+------+-------------+---------+
| test | get_version |         |
+------+-------------+---------+
1 row in set (0.00 sec)
```

Drop or re-create the event with a valid definer.

###### Note

Before dropping or redefining a `DEFINER`, carefully review and check your application and privilege requirements.
For more information, see [Stored object access
control](https://dev.mysql.com/doc/refman/5.7/en/stored-objects-security.html "https://dev.mysql.com/doc/refman/5.7/en/stored-objects-security.html") in the MySQL documentation.

```
mysql> drop event test.get_version;
Query OK, 0 rows affected (0.00 sec)

mysql> DELIMITER ;
mysql> delimiter $$
mysql> CREATE EVENT get_version
    ->     ON SCHEDULE
    ->       EVERY 1 DAY
    ->     DO
    ->      ///DO SOMETHING //
    -> $$
Query OK, 0 rows affected (0.01 sec)

mysql> DELIMITER ;

mysql> select db,name,definer from mysql.event where name='get_version';
+------+-------------+------------+
| db   | name        | definer    |
+------+-------------+------------+
| test | get_version | reinvent@% |
+------+-------------+------------+
1 row in set (0.00 sec)
```

Now the precheck passes.

```
{
  "id": "getEventsWithNullDefiner",
  "title": "The definer column for mysql.event cannot be null or blank.",
  "status": "OK",
  "detectedProblems": []},
```

**getMismatchedMetadata**

**Precheck level: Error**

**Column definition mismatch between InnoDB data dictionary and actual table definition**

Similar to [schemaInconsistencyCheck](#schemaInconsistencyCheck "#schemaInconsistencyCheck"), this precheck verifies that table metadata in
MySQL is consistent before proceeding with the upgrade. In this case, the precheck verifies that the column definitions match
between the InnoDB data dictionary and the MySQL table definition. If a mismatch if detected, the upgrade doesn't proceed.

If you encounter any errors with this precheck, open a case with [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support")
to request that the metadata inconsistency be resolved. Alternatively, you can retry the upgrade by performing a logical dump, then
restoring to a new Aurora MySQL version 3 DB cluster.

**Example output:**

```
{
  "id": "getMismatchedMetadata",
  "title": "Column definition mismatch between InnoDB Data Dictionary and actual table definition.",
  "status": "OK",
  "description": "Error: Your database has mismatched metadata. The upgrade to mysql 8.0 will not succeed until this is fixed.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.mismatchTable",
        "description": "Table `test/mismatchTable` column names mismatch with InnoDb dictionary column names: iD <> id"
      }
  ]
}
```

The precheck reports a mismatch in the metadata for the `id` column in the `test.mismatchTable` table.
Specifically, the MySQL metadata has the column name as `iD`, while InnoDB has it as `id`.

**getTriggersWithNullDefiner**

**Precheck level: Error**

**The definer column for `information_schema.triggers` can't be `null` or
blank.**

The precheck validates that your database has no triggers defined with `null` or blank definers. For more information
on definer requirements for stored objects, see [getEventsWithNullDefiner](#getEventsWithNullDefiner "#getEventsWithNullDefiner").

**Example output:**

```
{
  "id": "getTriggersWithNullDefiner",
  "title": "The definer column for information_schema.triggers cannot be null or blank.",
  "status": "OK",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.example_trigger",
        "description": "Set definer for trigger example_trigger in Schema test"
      }
  ]
}
```

The precheck returns an error because the `example_trigger` trigger in the `test` schema has a
`null` definer. To correct this issue, fix the definer by re-creating the trigger with a valid user, or drop the
trigger. For more information, see the example in [getEventsWithNullDefiner](#getEventsWithNullDefiner "#getEventsWithNullDefiner").

###### Note

Before dropping or redefining a `DEFINER`, carefully review and check your application and privilege requirements.
For more information, see [Stored object access
control](https://dev.mysql.com/doc/refman/5.7/en/stored-objects-security.html "https://dev.mysql.com/doc/refman/5.7/en/stored-objects-security.html") in the MySQL documentation.

**getValueOfVariablelower_case_table_names**

**Precheck level: Error**

**All database or table names must be lowercase when the `lower_case_table_names` parameter is set to
`1`.**

Before MySQL 8.0, database names, table names and other objects corresponded to files in the data directory, such as file-based
metadata (.frm). The [lower_case_table_names](https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html "https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html") system variable allows users to control how the server handles identifier case sensitivity for
database objects, and the storage of such metadata objects. This parameter could be changed on an already initialized server
following a reboot.

However, in MySQL 8.0, while this parameter still controls how the server handles identifier case sensitivity, it can't be changed
after the data dictionary is initialized. When upgrading or creating a MySQL 8.0 database, the value set for
`lower_case_table_names` the first time the data dictionary is started on MySQL, is used for the lifetime of that
database. This restriction was put in place as part of the implementation of the [Atomic Data Dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html") implementation,
where database objects are migrated from file-based metadata to internal InnoDB tables in the `mysql` schema.

For more information, see [Data
dictionary changes](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-data-dictionary-changes "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-data-dictionary-changes") in the MySQL documentation.

To avoid issues during upgrade when updating file-based metadata to the new Atomic Data Dictionary, this precheck validates that
when `lower_case_table_names = 1`, all tables are stored on disk in lower case. If they aren’t, a precheck error is
returned, and you must correct the metadata before proceeding with the upgrade.

**Example output:**

```
{
  "id": "getValueOfVariablelower_case_table_names",
  "title": "MySQL pre-checks that all database or table names are lowercase when the lower_case_table_names parameter is set to 1.",
  "status": "OK",
  "description": "Error: You have one or more databases or tables with uppercase letters in the names, but the lower_case_table_names parameter is set to 1. To upgrade to MySQL 8.0, either change all database or table names to lowercase, or set the parameter to 0.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.TEST",
        "description": "Table test.TEST contains one or more capital letters in name while lower_case_table_names = 1"
      }
  ]
}
```

An error is returned because the table `test.TEST` contains uppercase letters, but `lower_case_table_names`
is set to `1`.

To resolve this issue, you can rename the table to use lowercase, or modify the `lower_case_table_names` parameter on
the DB cluster before starting the upgrade.

###### Note

Carefully test and review the documentation on [case sensitivity](https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html "https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html") in MySQL, and how
any such changes might affect your application.

Also review the MySQL 8.0 documentation on how [lower_case_table_names](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_lower_case_table_names "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_lower_case_table_names") are handled differently in MySQL 8.0.

**groupByAscSyntaxCheck**

**Precheck level: Error**

**Usage of removed `GROUP BY ASC/DESC` syntax**

As of MySQL 8.0.13, the deprecated `ASC` or `DESC` syntax for `GROUP BY` clauses has been
removed. Queries relying on `GROUP BY` sorting might now produce different results. To get a specific sort order, use an
`ORDER BY` clause instead. If any objects exist in your database using this syntax, you must re-create them using an
`ORDER BY` clause before retrying the upgrade. For more information, see [SQL changes](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-sql-changes "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-sql-changes") in the
MySQL documentation.

**Example output:**

```
{
  "id": "groupbyAscSyntaxCheck",
  "title": "Usage of removed GROUP BY ASC/DESC syntax",
  "status": "OK",
  "description": "Error: The following DB objects use removed GROUP BY ASC/DESC syntax. They need to be altered so that ASC/DESC keyword is removed from GROUP BY clause and placed in appropriate ORDER BY clause.",
  "documentationLink": "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-13.html#mysqld-8-0-13-sql-syntax",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.groupbyasc",
        "description": "PROCEDURE uses removed GROUP BY ASC syntax",
        "dbObjectType": "Routine"
      }
  ]
}
```

**mysqlEmptyDotTableSyntaxCheck**

**Precheck level: Error**

**Check for deprecated `.<table>` syntax used in routines.**

In MySQL 8.0, routines can no longer contain the deprecated identifier syntax (`\".<table>\"`). If any stored
routines or triggers contain such identifiers, the upgrade fails. For example, the following `.dot_table` reference is no
longer permitted:

```
mysql> show create procedure incorrect_procedure\G
*************************** 1. row ***************************
           Procedure: incorrect_procedure
            sql_mode:
    Create Procedure: CREATE DEFINER=`reinvent`@`%` PROCEDURE `incorrect_procedure`()
BEGIN delete FROM .dot_table; select * from .dot_table where 1=1; END
character_set_client: utf8mb4
collation_connection: utf8mb4_0900_ai_ci
  Database Collation: latin1_swedish_ci
1 row in set (0.00 sec)
```

After you re-create the routines and triggers to use the correct identifier syntax and escaping, the precheck passes, and the
upgrade can proceed. For more information on identifiers, see [Schema object names](https://dev.mysql.com/doc/refman/8.0/en/identifiers.html "https://dev.mysql.com/doc/refman/8.0/en/identifiers.html") in the MySQL documentation.

**Example output:**

```
{
  "id": "mysqlEmptyDotTableSyntaxCheck",
  "title": "Check for deprecated '.<table>' syntax used in routines.",
  "status": "OK",
  "description": "Error: The following routines contain identifiers in deprecated identifier syntax (\".<table>\"), and should be corrected before upgrade:\n",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.incorrect_procedure",
        "description": " routine body contains deprecated identifiers."
      }
  ]
}
```

The precheck returns an error for the `incorrect_procedure` routine in the `test` database because it
contains deprecated syntax.

After you correct the routine, the precheck succeeds, and you can retry the upgrade.

**mysqlIndexTooLargeCheck**

**Precheck level: Error**

**Check for indexes that are too large to work on MySQL versions higher than 5.7**

For compact or redundant row formats, it shouldn't be possible to create an index with a prefix larger than 767 bytes. However,
before MySQL version 5.7.35 this was possible. For more information, see the [MySQL 5.7.35 release notes](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-35.html "https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-35.html").

Any indexes that were affected by this bug will become inaccessible after upgrading to MySQL 8.0. This precheck identifies
offending indexes that have to be rebuilt before the upgrade is allowed to proceed.

```
 {
  "id": "mysqlIndexTooLargeCheck",
  "title": "Check for indexes that are too large to work on higher versions of MySQL Server than 5.7",
  "status": "OK",
  "description": "Error: The following indexes ware made too large for their format in an older version of MySQL (older than 5.7.34). Normally those indexes within tables with compact or redundant row formats shouldn't be larger than 767 bytes. To fix this problem those indexes should be dropped before upgrading or those tables will be inaccessible.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.table_with_large_idx",
        "description": "IDX_2"
      }
  ]
}
```

The precheck returns an error because the `test.table_with_large_idx` table contains an index on a table using a
compact or redundant row format that's larger than 767 bytes. These tables would become unaccessible after upgrading to MySQL 8.0.
Before proceeding with the upgrade, do one of the following:

- Drop the index mentioned in the precheck.
- Add an index mentioned in the precheck.
- Change the row format used by the table.

Here we rebuild the table to resolve the precheck failure. Before rebuilding the table, make sure that the [innodb_file_format](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_file_format "https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_file_format") is set
to `Barracuda`, and the [innodb_default_row_format](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_default_row_format "https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_default_row_format") is set to `dynamic`. These are the defaults in MySQL 5.7. For more information,
see [InnoDB row formats](https://dev.mysql.com/doc/refman/5.7/en/innodb-row-format.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-row-format.html") and [InnoDB file-format management](https://dev.mysql.com/doc/refman/5.7/en/innodb-file-format.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-file-format.html") in the MySQL
documentation.

###### Note

Before rebuilding tablespaces, see [Online DDL operations](https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html") in the MySQL documentation to understand the effects of locking and data movement on
foreground transactions.

```
mysql > select @@innodb_file_format,@@innodb_default_row_format;
+----------------------+-----------------------------+
| @@innodb_file_format | @@innodb_default_row_format |
+----------------------+-----------------------------+
| Barracuda            | dynamic                     |
+----------------------+-----------------------------+
1 row in set (0.00 sec)

mysql> optimize table table_with_large_idx;
+---------------------------+----------+----------+-------------------------------------------------------------------+
| Table                     | Op       | Msg_type | Msg_text                                                          |
+---------------------------+----------+----------+-------------------------------------------------------------------+
| test.table_with_large_idx | optimize | note     | Table does not support optimize, doing recreate + analyze instead |
| test.table_with_large_idx | optimize | status   | OK                                                                |
+---------------------------+----------+----------+-------------------------------------------------------------------+
2 rows in set (0.02 sec)

# Verify FILE_FORMAT and ROW_FORMAT
mysql>  select * from information_schema.innodb_sys_tables where name like 'test/table_with_large_idx';
+----------+---------------------------+------+--------+-------+-------------+------------+---------------+------------+
| TABLE_ID | NAME                      | FLAG | N_COLS | SPACE | FILE_FORMAT | ROW_FORMAT | ZIP_PAGE_SIZE | SPACE_TYPE |
+----------+---------------------------+------+--------+-------+-------------+------------+---------------+------------+
|       43 | test/table_with_large_idx |   33 |      4 |    26 | Barracuda   | Dynamic    |             0 | Single     |
+----------+---------------------------+------+--------+-------+-------------+------------+---------------+------------+
1 row in set (0.00 sec)
```

After rebuilding the table, the precheck passes, and the upgrade can proceed.

```
{
  "id": "mysqlIndexTooLargeCheck",
  "title": "Check for indexes that are too large to work on higher versions of MySQL Server than 5.7",
  "status": "OK",
  "detectedProblems": []
},
```

**mysqlInvalid57NamesCheck**

**Precheck level: Error**

**Check for invalid table and schema names used in MySQL 5.7**

When migrating to the new data dictionary in MySQL 8.0, your database instance can't contain schemas or tables prefixed with
`#mysql50#`. If any such objects exist, the upgrade fails. To resolve this issue, run [mysqlcheck](https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html "https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html") against the returned schemas and tables.

###### Note

Make sure that you use a [MySQL 5.7 version](https://downloads.mysql.com/archives/community/ "https://downloads.mysql.com/archives/community/") of
`mysqlcheck` , because [--fix-db-names](https://dev.mysql.com/doc/refman/5.7/en/mysqlcheck.html#option_mysqlcheck_fix-db-names "https://dev.mysql.com/doc/refman/5.7/en/mysqlcheck.html#option_mysqlcheck_fix-db-names") and
[--fix-table-names](https://dev.mysql.com/doc/refman/5.7/en/mysqlcheck.html#option_mysqlcheck_fix-table-names "https://dev.mysql.com/doc/refman/5.7/en/mysqlcheck.html#option_mysqlcheck_fix-table-names") have been removed from [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html").

**Example output:**

```
{
  "id": "mysqlInvalid57NamesCheck",
  "title": "Check for invalid table names and schema names used in 5.7",
  "status": "OK",
  "description": "The following tables and/or schemas have invalid names. In order to fix them use the mysqlcheck utility as follows:\n\n  $ mysqlcheck --check-upgrade --all-databases\n  $ mysqlcheck --fix-db-names --fix-table-names --all-databases\n\nOR via mysql client, for eg:\n\n  ALTER DATABASE `#mysql50#lost+found` UPGRADE DATA DIRECTORY NAME;",
  "documentationLink": "https://dev.mysql.com/doc/refman/5.7/en/identifier-mapping.html https://dev.mysql.com/doc/refman/5.7/en/alter-database.html https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "#mysql50#fix_db_names",
        "description": "Schema name"
      }
  ]
}
```

The precheck reports that the schema `#mysql50#fix_db_names` has an invalid name.

After fixing the schema name, the precheck passes, allowing the upgrade to proceed.

```
{
  "id": "mysqlInvalid57NamesCheck",
  "title": "Check for invalid table names and schema names used in 5.7",
  "status": "OK",
  "detectedProblems": []
},
```

**mysqlOrphanedRoutinesCheck**

**Precheck level: Error**

**Check for orphaned routines in 5.7**

When migrating to the new data dictionary in MySQL 8.0, if there are any stored procedures in the database where the schema no
longer exists, the upgrade fails. This precheck verifies that all schemas referenced in stored procedures on your DB instance still
exist. To allow the upgrade to proceed, drop these stored procedures.

**Example output:**

```
{
  "id": "mysqlOrphanedRoutinesCheck",
  "title": "Check for orphaned routines in 5.7",
  "status": "OK",
  "description": "Error: The following routines have been orphaned. Schemas that they are referencing no longer exists.\nThey have to be cleaned up or the upgrade will fail.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "dropped_db.get_version",
        "description": "is orphaned"
      }
  ]
},
```

The precheck reports that the `get_version` stored procedure in the `dropped_db` database is
orphaned.

To clean up this procedure, you can re-create the missing schema.

```
mysql> create database dropped_db;
Query OK, 1 row affected (0.01 sec)
```

After the schema is re-created, you can drop the procedure to allow the upgrade to proceed.

```
{
  "id": "mysqlOrphanedRoutinesCheck",
  "title": "Check for orphaned routines in 5.7",
  "status": "OK",
  "detectedProblems": []
},
```

**mysqlSchemaCheck**

**Precheck level: Error**

**Table names in the `mysql` schema conflicting with new tables in MySQL 8.0**

The new [Atomic Data Dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html")
introduced in MySQL 8.0 stores all metadata in a set of internal InnoDB tables in the `mysql` schema. During the upgrade,
the new [internal data dictionary tables](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-schema.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-schema.html") are
created in the `mysql` schema. To avoid naming collisions, which would result in upgrade failures, the precheck examines
all table names in the `mysql` schema to ensure that none of the new table names are already in use. If they are, an
error is returned, and the upgrade isn't allowed to proceed.

**Example output:**

```
{
  "id": "mysqlSchema",
  "title": "Table names in the mysql schema conflicting with new tables in the latest MySQL.",
  "status": "OK",
  "description": "Error: The following tables in mysql schema have names that will conflict with the ones introduced in the latest version. They must be renamed or removed before upgrading (use RENAME TABLE command). This may also entail changes to applications that use the affected tables.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/upgrade-before-you-begin.html",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "mysql.tablespaces",
        "description": "Table name used in mysql schema.",
        "dbObjectType": "Table"
      }
  ]
}
```

An error is returned because there is a table named `tablespaces` in the `mysql` schema. This is one of the
new internal data dictionary table names in MySQL 8.0. You must rename or remove any such tables before upgrading, by using the
`RENAME TABLE` command.

**nonNativePartitioningCheck**

**Precheck level: Error**

**Partitioned tables using engines with non-native partitioning**

According to the [MySQL 8.0 documentation](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html"), two
storage engines currently provide native partitioning support: [InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html") and [NDB](https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster.html"). Of these, only InnoDB is supported in Aurora MySQL
version 3, compatible with MySQL 8.0. Any attempt to create partitioned tables in MySQL 8.0 using any other storage engine fails.
This precheck looks for tables in your DB cluster that are using non-native partitioning. If any are returned, you must remove the
partitioning or convert the storage engine to InnoDB.

**Example output:**

```
{
  "id": "nonNativePartitioning",
  "title": "Partitioned tables using engines with non native partitioning",
  "status": "OK",
  "description": "Error: In the latest MySQL storage engine is responsible for providing its own partitioning handler, and the MySQL server no longer provides generic partitioning support. InnoDB and NDB are the only storage engines that provide a native partitioning handler that is supported in the latest MySQL. A partitioned table using any other storage engine must be altered—either to convert it to InnoDB or NDB, or to remove its partitioning—before upgrading the server, else it cannot be used afterwards.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-configuration-changes",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.partMyisamTable",
         "description": "MyISAM engine does not support native partitioning",
         "dbObjectType": "Table"
      }
  ]
}
```

Here a MyISAM table is using partitioning, which requires action before the upgrade can proceed.

**oldTemporalCheck**

**Precheck level: Error**

**Usage of old temporal type**

"Old temporals" refer to the temporal type columns (such as `TIMESTAMP` and `DATETIME`) created in MySQL
versions 5.5 and lower. In MySQL 8.0, support for these old temporal data types is removed, meaning that in-place upgrades from
MySQL 5.7 to 8.0 aren't possible if the database contains these old temporal types. To fix this, you must [rebuild](https://dev.mysql.com/doc/refman/5.7/en/rebuilding-tables.html "https://dev.mysql.com/doc/refman/5.7/en/rebuilding-tables.html") any tables containing such old temporal
date types, before proceeding with the upgrade.

For more information on the deprecation of old temporal data types in MySQL 5.7, see this [blog](https://dev.mysql.com/blog-archive/how-to-easily-identify-tables-with-temporal-types-in-old-format/ "https://dev.mysql.com/blog-archive/how-to-easily-identify-tables-with-temporal-types-in-old-format/"). For more
information on the removal of old temporal data types in MySQL 8.0, see this [blog](https://dev.mysql.com/blog-archive/mysql-8-0-removing-support-for-old-temporal-datatypes/ "https://dev.mysql.com/blog-archive/mysql-8-0-removing-support-for-old-temporal-datatypes/").

###### Note

Before rebuilding tablespaces, see [Online DDL operations](https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html") in the MySQL documentation to understand the effects of locking and data movement on
foreground transactions.

**Example output:**

```
{
  "id": "oldTemporalCheck",
  "title": "Usage of old temporal type",
  "status": "OK",
  "description": "Error: Following table columns use a deprecated and no longer supported temporal disk storage format. They must be converted to the new format before upgrading. It can by done by rebuilding the table using 'ALTER TABLE <table_name> FORCE' command",
  "documentationLink": "https://dev.mysql.com/blog-archive/mysql-8-0-removing-support-for-old-temporal-datatypes/",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.55_temporal_table.timestamp_column",
        "description": "timestamp /* 5.5 binary format */",
        "dbObjectType": "Column"
      }
  ]
},
```

An error is reported for the column `timestamp_column` in the table `test.55_temporal_table`, because it
uses an old temporal disk storage format that's no longer supported.

To resolve this issue and allow the upgrade to proceed, rebuild the table to convert the old temporal disk storage format to the
new one introduced in MySQL 5.6. For more information and prerequisites before doing so, see [Converting between 3-byte and 4-byte Unicode
character sets](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-conversion.html "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-conversion.html") in the MySQL documentation.

Running the following command to rebuild the tables mentioned in this precheck converts the old temporal types to the newer format
with fractional-second precision.

```
ALTER TABLE ... ENGINE=InnoDB;
```

For more information on rebuilding tables, see [ALTER TABLE
statement](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html "https://dev.mysql.com/doc/refman/8.0/en/alter-table.html") in the MySQL documentation.

After rebuilding the table in question and restarting the upgrade, the compatibility check passes, allowing the upgrade to
proceed.

```
{
  "id": "oldTemporalCheck",
  "title": "Usage of old temporal type",
  "status": "OK",
  "detectedProblems": []
}
```

**partitionedTablesInSharedTablespaceCheck**

**Precheck level: Error**

**Usage of partitioned tables in shared tablespaces**

As of [MySQL 8.0.13](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-13.html "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-13.html"), support for placing
table partitions in shared tablespaces is removed. Before upgrading, move any such tables from shared tablespaces to file-per-table
tablespaces.

###### Note

Before rebuilding tablespaces, see [Partitioning
operations](https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html#online-ddl-partitioning "https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html#online-ddl-partitioning") in the MySQL documentation to understand the effects of locking and data movement on foreground
transactions.

**Example output:**

```
{
  "id": "partitionedTablesInSharedTablespaceCheck",
  "title": "Usage of partitioned tables in shared tablespaces",
  "status": "OK",
  "description": "Error: The following tables have partitions in shared tablespaces. They need to be moved to file-per-table tablespace before upgrading. You can do this by running query like 'ALTER TABLE table_name REORGANIZE PARTITION X INTO (PARTITION X VALUES LESS THAN (30) TABLESPACE=innodb_file_per_table);'",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.partInnoDBTable",
        "description": "Partition p1 is in shared tablespace innodb",
        "dbObjectType": "Table"
      }
  ]
}
```

The precheck fails because partition `p1` from table `test.partInnoDBTable` is in the system
tablespace.

To resolve this issue, rebuild the `test.partInnodbTable` table, placing the offending partition `p1` in a
file-per-table tablespace.

```
mysql > ALTER TABLE partInnodbTable REORGANIZE PARTITION p1
    ->   INTO (PARTITION p1 VALUES LESS THAN ('2014-01-01') TABLESPACE=innodb_file_per_table);
Query OK, 0 rows affected, 1 warning (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

After doing so, the precheck passes.

```
{
  "id": "partitionedTablesInSharedTablespaceCheck",
  "title": "Usage of partitioned tables in shared tablespaces",
  "status": "OK",
  "detectedProblems": []
}
```

**removedFunctionsCheck**

**Precheck level: Error**

**Usage of functions that were removed from the latest MySQL version**

In MySQL 8.0, a number of built-in functions have been removed. This precheck examines your database for objects that might use
these functions. If they're found, an error is returned. You must resolve the issues before retrying the upgrade.

The majority of functions removed are [spatial
functions](https://dev.mysql.com/doc/refman/5.7/en/gis-wkt-functions.html "https://dev.mysql.com/doc/refman/5.7/en/gis-wkt-functions.html"), which have been replaced with equivalent `ST_*` functions. In these cases, you modify the database
objects to use the new procedure naming. For more information, see [Features removed in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals")
in the MySQL documentation.

**Example output:**

```
{
  "id": "removedFunctionsCheck",
  "title": "Usage of removed functions",
  "status": "OK",
  "description": "Error: The following DB objects use functions that were removed in the latest MySQL version. Please make sure to update them to use supported alternatives before upgrade.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.GetLocationsInPolygon",
        "description": "PROCEDURE uses removed function POLYGONFROMTEXT (consider using ST_POLYGONFROMTEXT instead)",
        "dbObjectType": "Routine"
      },
      {
        "level": "Error",
        "dbObject": "test.InsertLocation",
        "description": "PROCEDURE uses removed function POINTFROMTEXT (consider using ST_POINTFROMTEXT instead)",
        "dbObjectType": "Routine"
      }
  ]
},
```

The precheck reports that the `test.GetLocationsInPolygon` stored procedure is using two removed functions: [POLYGONFROMTEXT](https://dev.mysql.com/doc/refman/5.7/en/gis-wkt-functions.html#function_polyfromtext "https://dev.mysql.com/doc/refman/5.7/en/gis-wkt-functions.html#function_polyfromtext") and [POINTFROMTEXT](https://dev.mysql.com/doc/refman/5.7/en/gis-wkt-functions.html#function_st-mpointfromtext "https://dev.mysql.com/doc/refman/5.7/en/gis-wkt-functions.html#function_st-mpointfromtext"). It also
suggests that you use the new [ST_POLYGONFROMTEXT](https://dev.mysql.com/doc/refman/8.0/en/gis-wkt-functions.html#function_st-polyfromtext "https://dev.mysql.com/doc/refman/8.0/en/gis-wkt-functions.html#function_st-polyfromtext") and [ST_POINTFROMTEXT](https://dev.mysql.com/doc/refman/8.0/en/gis-wkt-functions.html#function_st-mpointfromtext "https://dev.mysql.com/doc/refman/8.0/en/gis-wkt-functions.html#function_st-mpointfromtext") as
replacements. After re-creating the procedure using the suggestions, the precheck completes successfully.

```
{
  "id": "removedFunctionsCheck",
  "title": "Usage of removed functions",
  "status": "OK",
  "detectedProblems": []
},
```

###### Note

While in most cases the deprecated functions have direct replacements, make sure that you test your application and review the
documentation for any changes in behavior as a result of the change.

**routineSyntaxCheck**

**Precheck level: Error**

**MySQL syntax check for routine-like objects**

MySQL 8.0 introduced [reserved keywords](https://dev.mysql.com/doc/mysqld-version-reference/en/keywords-8-0.html#keywords-new-in-8-0 "https://dev.mysql.com/doc/mysqld-version-reference/en/keywords-8-0.html#keywords-new-in-8-0") that were not reserved previously. The upgrade prechecker evaluates the usage of reserved keywords in
the names of database objects and in their definitions and body. If it detects reserved keywords being used in database objects,
such as stored procedures, functions, events, and triggers, the upgrade fails and an error is published to the
`upgrade-prechecks.log` file. To resolve the issue, you must update these object definitions and enclose any
such references in single quotes (') before upgrading. For more information on escaping reserved words in MySQL, see [String literals](https://dev.mysql.com/doc/refman/8.0/en/string-literals.html "https://dev.mysql.com/doc/refman/8.0/en/string-literals.html") in the MySQL documentation.

Alternatively, you can change the name to a different name, which may require application changes.

**Example output:**

```
{
  "id": "routineSyntaxCheck",
  "title": "MySQL syntax check for routine-like objects",
  "status": "OK",
  "description": "The following objects did not pass a syntax check with the latest MySQL grammar. A common reason is that they reference names that conflict with new reserved keywords. You must update these routine definitions and `quote` any such references before upgrading.",
  "documentationLink": "https://dev.mysql.com/doc/refman/en/keywords.html",
  "detectedProblems": [
      {
         "level": "Error",
         "dbObject": "test.select_res_word",
         "description": "at line 2,18: unexpected token 'except'",
         "dbObjectType": "Routine"
      }
  ]
}
```

To fix this issue, check the routine definition.

```
SHOW CREATE PROCEDURE test.select_res_word\G

*************************** 1. row ***************************
           Procedure: select_res_word
            sql_mode: ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
    Create Procedure: CREATE PROCEDURE 'select_res_word'()
BEGIN
    SELECT * FROM except;
END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
1 row in set (0.00 sec)
```

The procedure uses a table named `except`, which is a new keyword in MySQL 8.0. Re-create the procedure by escaping the
string literal.

```
> drop procedure if exists select_res_word;
Query OK, 0 rows affected (0.00 sec)

> DELIMITER $$
 > CREATE PROCEDURE select_res_word()
    -> BEGIN
    ->     SELECT * FROM 'except';
    -> END$$
Query OK, 0 rows affected (0.00 sec)

 > DELIMITER ;
```

The precheck now passes.

```
{
  "id": "routineSyntaxCheck",
  "title": "MySQL syntax check for routine-like objects",
  "status": "OK",
  "detectedProblems": []
}
```

**schemaInconsistencyCheck**

**Precheck level: Error**

**Schema inconsistencies resulting from file removal or corruption**

As described previously, MySQL 8.0 introduced the [Atomic Data Dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html"), which stores all
metadata in a set of internal InnoDB tables in the `mysql` schema. This new architecture provides a transactional, [ACID](https://en.wikipedia.org/wiki/ACID "https://en.wikipedia.org/wiki/ACID")-compliant way to manage database metadata, solving the "atomic DDL"
problem from the old file-based approach. Before MySQL 8.0, it was possible for schema objects to become orphaned if a DDL operation
was unexpectedly interrupted. The migration of file-based metadata to the new Atomic Data Dictionary tables during upgrade ensures
that there are no such orphaned schema objects in the DB instance. If any orphaned objects are encountered, the upgrade
fails.

To help detect these orphaned objects before initiating the upgrade, the `schemaInconsistencyCheck` precheck is run to
ensure that all data dictionary metadata objects are in sync. If any orphaned metadata objects are detected, the upgrade doesn't
proceed. To proceed with the upgrade, clean up these orphaned metadata objects.

If you encounter any errors with this precheck, open a case with [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support")
to request that the metadata inconsistency be resolved. Alternatively, you can retry the upgrade by performing a logical dump, then
restoring to a new Aurora MySQL version 3 DB cluster.

**Example output:**

```
{
  "id": "schemaInconsistencyCheck",
  "title": "Schema inconsistencies resulting from file removal or corruption",
  "status": "OK",
  "description": "Error: Following tables show signs that either table datadir directory or frm file was removed/corrupted. Please check server logs, examine datadir to detect the issue and fix it before upgrade",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.schemaInconsistencyCheck_failure",
        "description": "present in INFORMATION_SCHEMA's INNODB_SYS_TABLES table but missing from TABLES table"
      }
  ]
}
```

The precheck reports that the `test.schemaInconsistencyCheck_failure` table has inconsistent metadata. In this case,
the table exists in the InnoDB storage engine metadata (`information_schema.INNODB_SYS_TABLES`), but not in the MySQL
metadata (`information_schema.TABLES`).

### Aurora MySQL prechecks that report errors

The following prechecks are specific to Aurora MySQL:

- [auroraCheckDDLRecovery](#auroraCheckDDLRecovery "#auroraCheckDDLRecovery")
- [auroraCheckRdsUpgradePrechecksTable](#auroraCheckRdsUpgradePrechecksTable "#auroraCheckRdsUpgradePrechecksTable")
- [auroraFODUpgradeCheck](#auroraFODUpgradeCheck "#auroraFODUpgradeCheck")
- [auroraGetDanglingFulltextIndex](#auroraGetDanglingFulltextIndex "#auroraGetDanglingFulltextIndex")
- [auroraUpgradeCheckForDatafilePathInconsistency](#auroraUpgradeCheckForDatafilePathInconsistency "#auroraUpgradeCheckForDatafilePathInconsistency")
- [auroraUpgradeCheckForFtsSpaceIdZero](#auroraUpgradeCheckForFtsSpaceIdZero "#auroraUpgradeCheckForFtsSpaceIdZero")
- [auroraUpgradeCheckForIncompleteXATransactions](#auroraUpgradeCheckForIncompleteXATransactions "#auroraUpgradeCheckForIncompleteXATransactions")
- [auroraUpgradeCheckForInstanceLimit](#auroraUpgradeCheckForInstanceLimit "#auroraUpgradeCheckForInstanceLimit")
- [auroraUpgradeCheckForInternalUsers](#auroraUpgradeCheckForInternalUsers "#auroraUpgradeCheckForInternalUsers")
- [auroraUpgradeCheckForInvalidUtf8mb3CharacterStringInViews](#auroraUpgradeCheckForInvalidUtf8mb3CharacterStringInViews "#auroraUpgradeCheckForInvalidUtf8mb3CharacterStringInViews")
- [auroraUpgradeCheckForInvalidUtf8mb3ColumnComments](#auroraUpgradeCheckForInvalidUtf8mb3ColumnComments "#auroraUpgradeCheckForInvalidUtf8mb3ColumnComments")
- [auroraUpgradeCheckForInvalidUtf8mb3IndexComments](#auroraUpgradeCheckForInvalidUtf8mb3IndexComments "#auroraUpgradeCheckForInvalidUtf8mb3IndexComments")
- [auroraUpgradeCheckForInvalidUtf8mb3TableComments](#auroraUpgradeCheckForInvalidUtf8mb3TableComments "#auroraUpgradeCheckForInvalidUtf8mb3TableComments")
- [auroraUpgradeCheckForMasterUser](#auroraUpgradeCheckForMasterUser "#auroraUpgradeCheckForMasterUser")
- [auroraUpgradeCheckForPrefixIndexOnGeometryColumns](#auroraUpgradeCheckForPrefixIndexOnGeometryColumns "#auroraUpgradeCheckForPrefixIndexOnGeometryColumns")
- [auroraUpgradeCheckForSpecialCharactersInProcedures](#auroraUpgradeCheckForSpecialCharactersInProcedures "#auroraUpgradeCheckForSpecialCharactersInProcedures")
- [auroraUpgradeCheckForSysSchemaObjectTypeMismatch](#auroraUpgradeCheckForSysSchemaObjectTypeMismatch "#auroraUpgradeCheckForSysSchemaObjectTypeMismatch")
- [auroraUpgradeCheckForViewColumnNameLength](#auroraUpgradeCheckForViewColumnNameLength "#auroraUpgradeCheckForViewColumnNameLength")
- [auroraUpgradeCheckIndexLengthLimitOnTinyColumns](#auroraUpgradeCheckIndexLengthLimitOnTinyColumns "#auroraUpgradeCheckIndexLengthLimitOnTinyColumns")
- [auroraUpgradeCheckMissingInnodbMetadataForMysqlHostTable](#auroraUpgradeCheckMissingInnodbMetadataForMysqlHostTable "#auroraUpgradeCheckMissingInnodbMetadataForMysqlHostTable")

**auroraCheckDDLRecovery**

**Precheck level: Error**

**Check for artifacts related to Aurora DDL recovery feature**

As part of the Data Definition Language (DDL) recovery implementation in Aurora MySQL, metadata on inflight DDL statements is
maintained in the `ddl_log_md_table` and `ddl_log_table` tables in the `mysql` schema. Aurora's
implementation of DDL recovery isn't supported for version 3 onward, because the functionality is part of the new [Atomic Data Dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html") implementation in
MySQL 8.0. If you have any DDL statements running during the compatibility checks, this precheck might fail. We recommend that you
try the upgrade while no DDL statements are running.

If this precheck fails without any running DDL statements, open a case with [AWS
Support](https://aws.amazon.com/support "https://aws.amazon.com/support") to request that the metadata inconsistency be resolved. Alternatively, you can retry the upgrade by performing a
logical dump, then restoring to a new Aurora MySQL version 3 DB cluster.

If any DDL statements are running, the precheck output prints the following message:

```
“There are DDL statements in process. Please allow DDL statements to finish before upgrading.”
```

**Example output:**

```
{
  "id": "auroraCheckDDLRecovery",
  "title": "Check for artifacts related to Aurora DDL recovery feature",
  "status": "OK",
  "description": "Aurora implementation of DDL recovery is not supported from 3.x onwards. This check verifies that the database do not have artifacts realted to the feature",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "mysql.ddl_log_md_table",
        "description": "Table mysql.ddl_log_md_table is not empty. Your database has pending DDL recovery operations. Reachout to AWS support for assistance."
      },
      {
        "level": "Error",
        "dbObject": "mysql.ddl_log_table",
        "description": "Table mysql.ddl_log_table is not empty. Your database has pending DDL recovery operations. Reachout to AWS support for assistance."
      },
      {
        "level": "Error",
        "dbObject": "information_schema.processlist",
        "description": "There are DDL statements in process. Please allow DDL statements to finish before upgrading."
      }
  ]
}
```

The precheck returned an error due to an inflight DDL running concurrently with the compatibility checks. We recommend that you
retry the upgrade without any DDLs running.

**auroraCheckRdsUpgradePrechecksTable**

**Precheck level: Error**

**Check existence of `mysql.rds_upgrade_prechecks` table**

This is an internal-only precheck carried out by the RDS service. Any errors will be automatically handled on upgrade and can be
safely ignored.

If you encounter any errors with this precheck, open a case with [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support")
to request that the metadata inconsistency be resolved. Alternatively, you can retry the upgrade by performing a logical dump, then
restoring to a new Aurora MySQL version 3 DB cluster.

```
{
  "id": "auroraCheckRdsUpgradePrechecksTable",
  "title": "Check existence of mysql.rds_upgrade_prechecks table",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraFODUpgradeCheck**

**Precheck level: Error**

**Check for artifacts related to Aurora fast DDL feature**

The [Fast DDL](AuroraMySQL.Managing.md "AuroraMySQL.Managing.md") optimization was introduced in [lab mode](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md") on Aurora MySQL version 2 to improve the efficiency of some DDL operations.
In Aurora MySQL version 3, lab mode has been removed, and the Fast DDL implementation has been superseded by the MySQL 8.0 feature
called [Instant DDL](https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-operations.html "https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-operations.html").

Before upgrading to Aurora MySQL version 3, any tables that use Fast DDL in lab mode will have to be rebuilt by running the
`OPTIMIZE TABLE` or `ALTER TABLE ... ENGINE=InnoDB` command to ensure compatibility with Aurora MySQL
version 3.

This precheck returns a list of any such tables. After the returned tables have been rebuilt, you can retry the upgrade.

**Example output:**

```
{
  "id": "auroraFODUpgradeCheck",
  "title": "Check for artifacts related to Aurora fast DDL feature",
  "status": "OK",
  "description": "Aurora fast DDL is not supported from 3.x onwards. This check verifies that the database does not have artifacts related to the feature",
  "documentationLink": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.FastDDL.html#AuroraMySQL.Managing.FastDDL-v2",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.test",
        "description": "Your table has pending Aurora fast DDL operations. Run 'OPTIMIZE TABLE <table name>' for the table to apply all the pending DDL updates. Then try the upgrade again."
      }
  ]
}
```

The precheck reports that the table `test.test` has pending Fast DDL operations.

To allow the upgrade to proceed, you can rebuild the table, then retry the upgrade.

###### Note

Before rebuilding tablespaces, see [Online DDL operations](https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html") in the MySQL documentation to understand the effects of locking and data movement on
foreground transactions.

```
mysql> optimize table test.test;
+-----------+----------+----------+-------------------------------------------------------------------+
| Table     | Op       | Msg_type | Msg_text                                                          |
+-----------+----------+----------+-------------------------------------------------------------------+
| test.test | optimize | note     | Table does not support optimize, doing recreate + analyze instead |
| test.test | optimize | status   | OK                                                                |
+-----------+----------+----------+-------------------------------------------------------------------+
2 rows in set (0.04 sec)
```

After rebuilding the table, the precheck succeeds.

```
{
  "id": "auroraFODUpgradeCheck",
  "title": "Check for artifacts related to Aurora fast DDL feature",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraGetDanglingFulltextIndex**

**Precheck level: Error**

**Tables with dangling `FULLTEXT` index reference**

Before MySQL 5.6.26, it was possible that after dropping a full-text search index, the hidden `FTS_DOC_ID` and
`FTS_DOC_ID_INDEX` columns would become orphaned. For more information, see [Bug #76012](https://bugs.mysql.com/bug.php?id=76012 "https://bugs.mysql.com/bug.php?id=76012").

If you have any tables created on earlier versions of MySQL where this has occurred, it can cause upgrades to Aurora MySQL version 3
to fail. This precheck verifies that no such orphaned, or “dangling” full-text indexes exist on your DB cluster before upgrading to MySQL
8.0. If this precheck fails, rebuild any tables that contain such dangling full-text indexes.

**Example output:**

```
{
  "id": "auroraGetDanglingFulltextIndex",
  "title": "Tables with dangling FULLTEXT index reference",
  "status": "OK",
  "description": "Error: The following tables contain dangling FULLTEXT index which is not supported. It is recommended to rebuild the table before upgrade.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.table_with_fts_index",
        "description": "Table `test.table_with_fts_index` contains dangling FULLTEXT index. Kindly recreate the table before upgrade."
      }
  ]
},
```

The precheck reports an error for the `test.table_with_fts_index` table because it contains a dangling full-text index.
To allow the upgrade to proceed, rebuild the table to clean up the full-text index auxiliary tables. Use `OPTIMIZE TABLE
 test.table_with_fts_index` or `ALTER TABLE test.table_with_fts_index, ENGINE=INNODB`.

After rebuilding the table, the precheck passes.

```
{
  "id": "auroraGetDanglingFulltextIndex",
  "title": "Tables with dangling FULLTEXT index reference",
  "status": "OK",
  "detectedProblems": []
},
```

**auroraUpgradeCheckForDatafilePathInconsistency**

**Precheck level: Error**

**Check for inconsistency related to `ibd` file path**

This precheck applies only to Aurora MySQL version 3.03.0 and lower. If you encounter an error with this precheck, upgrade to
Aurora MySQL version 3.04 or higher.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForDatafilePathInconsistency",
  "title": "Check for inconsistency related to ibd file path.",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckForFtsSpaceIdZero**

**Precheck level: Error**

**Check for full-text index with space ID as zero**

In MySQL, when you add a [full-text index](https://dev.mysql.com/doc/refman/5.7/en/innodb-fulltext-index.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-fulltext-index.html")
to an InnoDB table, a number of auxiliary index tablespaces are created. Due to a [bug](https://bugs.mysql.com/bug.php?id=72132 "https://bugs.mysql.com/bug.php?id=72132") in earlier versions of MySQL, which was fixed in version 5.6.20, it
was possible that these auxiliary index tables were created in the [system tablespace](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_system_tablespace "https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_system_tablespace"), rather than their
own InnoDB tablespace.

If any such auxiliary tablespaces exist, the upgrade will fail. Re-create the full-text indexes mentioned in the precheck error,
then retry the upgrade.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForFtsSpaceIdZero",
  "title": "Check for fulltext index with space id as zero",
  "status": "OK",
  "description": "The auxiliary tables of FTS indexes on the table are created in system table-space. Due to this DDL queries executed on MySQL8.0 shall cause database unavailability. To avoid that, drop and recreate all the FTS indexes on the table or rebuild the table using ALTER TABLE query before the upgrade.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.fts_space_zero_check",
        "description": " The auxiliary tables of FTS indexes on the table 'test.fts_space_zero_check' are created in system table-space due to https://bugs.mysql.com/bug.php?id=72132. In MySQL8.0, DDL queries executed on this table shall cause database unavailability. To avoid that, drop and recreate all the FTS indexes on the table or rebuild the table using ALTER TABLE query before the upgrade."
      }
  ]
},
```

The precheck reports an error for the `test.fts_space_zero_check` table, because it has auxiliary full-text search
(FTS) tables in the system tablespace.

After you drop and re-create the FTS indexes associated with this table, the precheck succeeds.

###### Note

Before rebuilding tablespaces, see [Partitioning
operations](https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html#online-ddl-partitioning "https://dev.mysql.com/doc/refman/5.7/en/innodb-online-ddl-operations.html#online-ddl-partitioning") in the MySQL documentation to understand the effects of locking and data movement on foreground
transactions.

```
{
 "id": "auroraUpgradeCheckForFtsSpaceIdZero",
 "title": "Check for fulltext index with space id as zero",
 "status": "OK",
 "detectedProblems": []
}
```

**auroraUpgradeCheckForIncompleteXATransactions**

**Precheck level: Error**

**Check for XA transactions in prepared state**

While running the major version upgrade process, it is essential that the Aurora MySQL version 2 DB instance undergo a [clean shutdown](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_slow_shutdown "https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_slow_shutdown"). This ensures that all
transactions are committed or rolled back, and that InnoDB has purged all undo log records. Because transaction rollback is
necessary, if your database has any [XA transactions](https://dev.mysql.com/doc/refman/5.7/en/xa.html "https://dev.mysql.com/doc/refman/5.7/en/xa.html") in a
prepared state, it can block the clean shutdown from proceeding. For this reason, if any prepared XA transactions are detected, the
upgrade will be unable to proceed until you take action to commit or roll them back.

For more information on finding XA transactions in a prepared state using `XA RECOVER`, see [XA transaction SQL statements](https://dev.mysql.com/doc/refman/5.7/en/xa-statements.html "https://dev.mysql.com/doc/refman/5.7/en/xa-statements.html") in the MySQL
documentation. For more information on XA transaction states, see [XA transaction states](https://dev.mysql.com/doc/refman/5.7/en/xa-states.html "https://dev.mysql.com/doc/refman/5.7/en/xa-states.html") in the MySQL documentation.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForIncompleteXATransactions",
  "title": "Pre-checks for XA Transactions in prepared state.",
  "status": "OK",
  "description": "Your cluster currently has XA transactions in the prepared state. To proceed with the upgrade, commit or rollback these transactions.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "all",
        "description": "Your cluster currently has XA transactions in the prepared state. To proceed with the upgrade, commit or rollback these transactions."
      }
  ]
}
```

This precheck reports an error because there are transactions in a prepared state that should be committed or rolled back.

After logging into the database, you can check the [information_schema.innodb_trx](https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-trx-table.html "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-trx-table.html")
table and the `XA RECOVER` output for more information.

###### Important

Before committing or rolling back a transaction, we recommend that you review the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/xa-restrictions.html "https://dev.mysql.com/doc/refman/5.7/en/xa-restrictions.html") and your application
requirements.

```
mysql> select trx_started,
    trx_mysql_thread_id,
    trx_id,trx_state,
    trx_operation_state,
    trx_rows_modified,
    trx_rows_locked
from
    information_schema.innodb_trx;
+---------------------+---------------------+---------+-----------+---------------------+-------------------+-----------------+
| trx_started         | trx_mysql_thread_id | trx_id  | trx_state | trx_operation_state | trx_rows_modified | trx_rows_locked |
+---------------------+---------------------+---------+-----------+---------------------+-------------------+-----------------+
| 2024-08-12 01:09:39 |                   0 | 2849470 | RUNNING   | NULL                |                 1 |               0 |
+---------------------+---------------------+---------+-----------+---------------------+-------------------+-----------------+
1 row in set (0.00 sec)

mysql> xa recover;
+----------+--------------+--------------+--------+
| formatID | gtrid_length | bqual_length | data   |
+----------+--------------+--------------+--------+
|        1 |            6 |            0 | xatest |
+----------+--------------+--------------+--------+
1 row in set (0.00 sec)
```

In this case, we roll back the prepared transaction.

```
mysql> XA ROLLBACK 'xatest';
Query OK, 0 rows affected (0.00 sec)
v
mysql> xa recover;
Empty set (0.00 sec)
```

After the XA transaction is rolled back, the precheck succeeds.

```
{
  "id": "auroraUpgradeCheckForIncompleteXATransactions",
  "title": "Pre-checks for XA Transactions in prepared state.",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckForInstanceLimit**

**Precheck level: Error**

**Check whether upgrade is supported on the current instance class**

Running an in-place upgrade from Aurora MySQL version 2.12.0 or 2.12.1, where the writer
[DB instance class](Concepts.md "Concepts.md") is
db.r6i.32xlarge, is currently not supported. In this case, the precheck returns an error. To allow the upgrade to proceed, you can
either change your DB instance class to db.r6i.24xlarge or smaller. Or you can upgrade to Aurora MySQL version 2.12.2 or higher, where
in-place upgrade to Aurora MySQL version 3 is supported on db.r6i.32xlarge.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForInstanceLimit",
  "title": "Checks if upgrade is supported on the current instance class",
  "status": "OK",
  "description": "Upgrade from Aurora Version 2.12.0 and 2.12.1 may fail for 32.xl and above instance class.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "all",
        "description": "Upgrade is not supported on this instance size for Aurora MySql Version 2.12.1. Before upgrading to Aurora MySql 3, please consider either: 1. Changing the instance class to 24.xl or lower. -or- 2. Upgrading to patch version 2.12.2 or higher."
      }
  ]
},
```

The precheck returns an error because the writer DB instance is using the db.r6i.32xlarge instance class, and is running on
Aurora MySQL version 2.12.1.

**auroraUpgradeCheckForInternalUsers**

**Precheck level: Error**

**Check for 8.0 internal users**

This precheck applies only to Aurora MySQL version 3.03.0 and lower. If you encounter an error with this precheck, upgrade to
Aurora MySQL version 3.04 or higher.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForInternalUsers",
  "title": "Check for 8.0 internal users.",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckForInvalidUtf8mb3CharacterStringInViews**

**Precheck level: Error**

**Check for invalid utf8mb3 characters in view definition**

This precheck identifies views that contain comments with invalid `utf8mb3` character encoding. In MySQL 8.0, stricter validation is applied to character encoding in metadata, including view comments. If any view definition contains characters that are not valid in the `utf8mb3` character set, the upgrade fails.

To resolve this issue, modify the view definition to remove or replace any non-BMP characters before you attempt the upgrade.

**Example output:**

```
{
"id": "auroraUpgradeCheckForInvalidUtf8mb3CharacterStringInViews",
"title": "Check for invalid utf8mb3 character string.",
"status": "OK",
"description": "Definition of following view(s) has/have invalid utf8mb3 character string.",
"detectedProblems": [
        {
            "level": "Error",
            "dbObject": "precheck.utf8mb3_invalid_char_view",
            "description": "Definition of view precheck.utf8mb3_invalid_char_view contains an invalid utf8mb3 character string. This is due to https://bugs.mysql.com/bug.php?id=110177. To fix the inconsistency, we recommend you to modify the view definition to not use non-BMP characters and try the upgrade again."
        }
    ]
},
```

The precheck reports that the `utf8mb3_invalid_char_view` view definition contains invalid `utf8mb3` characters in its definition.

To resolve this issue, identify the view that contains the unsupported characters and update the comments. First, examine the view structure and identify comments.

```
MySQL> SHOW CREATE VIEW precheck.utf8mb3_invalid_char_view\G
*************************** 1. row ***************************
                View: utf8mb3_invalid_char_view
        Create View: CREATE ALGORITHM=UNDEFINED DEFINER=`admin`@`%` SQL SECURITY DEFINER VIEW `utf8mb3_invalid_char_view` AS select 'This row contains a dolphin 🐬' AS `message`
character_set_client: utf8
collation_connection: utf8_general_ci
1 row in set, 1 warning (0.00 sec)
```

Once you've identified the view that contains the error, replace the view with the `CREATE OR REPLACE VIEW` statement.

```
MySQL> CREATE OR REPLACE VIEW precheck.utf8mb3_invalid_char_view AS select 'This view definition to not use non-BMP characters' AS message;
```

After updating all view definitions that contain unsupported characters, the precheck passes and the upgrade can proceed.

```
{
"id": "auroraUpgradeCheckForInvalidUtf8mb3ColumnComments",
"title": "Check for invalid utf8mb3 column comments.",
"status": "OK",
"detectedProblems": []
}
```

**auroraUpgradeCheckForInvalidUtf8mb3ColumnComments**

**Precheck level: Error**

**Check for invalid utf8mb3 column comments**

This precheck identifies tables that contain column comments with invalid `utf8mb3` character encoding. In MySQL 8.0, stricter validation is applied to character encoding in metadata, including column comments. If any column comments contain characters that are not valid in the utf8mb3 character set, the upgrade will fail.

To resolve this issue, you must modify the column comments to remove or replace any non-BMP characters before attempting the upgrade. You can use the `ALTER TABLE` statement to update the column comments.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForInvalidUtf8mb3ColumnComments",
  "title": "Check for invalid utf8mb3 column comments.",
  "status": "OK",
  "description": "Following table(s) has/have invalid utf8mb3 comments on the column/columns.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.t2",
        "description": "Table test.t2 has invalid utf8mb3 comments in it's column/columns. This is due to non-BMP characters in the comment field. To fix the inconsistency, we recommend you to modify comment fields to not use non-BMP characters and try the upgrade again."
      }
  ]
}
```

The precheck reports that the `test.t2` table contains invalid `utf8mb3` characters in one or more column comments, specifically due to the presence of non-BMP characters.

To resolve this issue, you can identify the problematic columns and update their comments. First, examine the table structure to identify columns with comments:

```
mysql> SHOW CREATE TABLE test.t2\G
```

Once you've identified the columns with problematic comments, update them using the `ALTER TABLE` statement. For example:

```
mysql> ALTER TABLE test.t2 MODIFY COLUMN column_name data_type COMMENT 'Updated comment without non-BMP characters';
```

Alternatively, you can remove the comment entirely:

```
mysql> ALTER TABLE test.t2 MODIFY COLUMN column_name data_type COMMENT '';
```

After updating all problematic column comments, the precheck will pass and the upgrade can proceed:

```
{
  "id": "auroraUpgradeCheckForInvalidUtf8mb3ColumnComments",
  "title": "Check for invalid utf8mb3 column comments.",
  "status": "OK",
  "detectedProblems": []
}
```

###### Note

Before modifying column comments, ensure that any application code or documentation that relies on these comments is updated accordingly. Consider migrating to the utf8mb4 character set for better Unicode support if your application requires non-BMP characters.

**auroraUpgradeCheckForInvalidUtf8mb3IndexComments**

**Precheck level: Error**

**Check for invalid utf8mb3 index comments**

This precheck identifies tables that contain index comments with invalid `utf8mb3` character encoding. In MySQL 8.0, stricter validation is applied to character encoding in metadata, including index comments. If any index comments contain characters that are not valid in the `utf8mb3` character set, the upgrade fails.

To resolve this issue, you must modify the index comments to remove or replace any non-BMP characters before attempting the upgrade.

**Example output:**

```
{
    "id": "auroraUpgradeCheckForInvalidUtf8mb3IndexComments",
    "title": "Check for invalid utf8mb3 index comments.",
    "status": "OK",
    "description": "Following table(s) has/have invalid utf8mb3 comments on the index.",
    "detectedProblems": [
        {
            "level": "Error",
            "dbObject": "precheck.utf8mb3_tab_index_comment",
            "description": "Table precheck.utf8mb3_tab_index_comment has invalid utf8mb3 comments in it's index. This is due to https://bugs.mysql.com/bug.php?id=110177. To fix the inconsistency, we recommend you to modify comment fields to not use non-BMP characters and try the upgrade again."
        }
    ]
},
```

The precheck reports that the `utf8mb3_tab_index_comment` table contains invalid `utf8mb3` characters in one or more column comments, specifically due to the presence of non-BMP characters.

To resolve this issue, first, examine the table structure to identify the index with problematic comments.

```
MySQL> SHOW CREATE TABLE precheck.utf8mb3_tab_index_comment\G
*************************** 1. row ***************************
    Table: utf8mb3_tab_index_comment
Create Table: CREATE TABLE `utf8mb3_tab_index_comment` (
`id` int(11) DEFAULT NULL,
`name` varchar(100) DEFAULT NULL,
KEY `idx_name` (`name`) COMMENT 'Name index 🐬'
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.01 sec)
```

Once you identify the index that contains comments that use unsupported characters, drop and recreate the index.

###### Note

Dropping and recreating a table index can lead to downtime. We recommend that you plan and schedule this operation during maintenance.

```
MySQL> ALTER TABLE precheck.utf8mb3_tab_index_comment DROP INDEX idx_name;
MySQL> ALTER TABLE precheck.utf8mb3_tab_index_comment ADD INDEX idx_name(name);
```

The following example shows another way to recreate the index.

```
MySQL> ALTER TABLE utf8mb3_tab_index_comment DROP INDEX idx_name, ADD INDEX idx_name (name) COMMENT 'Updated comment without non-BMP characters';
```

After you remove or update all unsupported index comments, the precheck passes and the upgrade can proceed.

```
{
"id": "auroraUpgradeCheckForInvalidUtf8mb3IndexComments",
"title": "Check for invalid utf8mb3 index comments.",
"status": "OK",
"detectedProblems": []
},
```

**auroraUpgradeCheckForInvalidUtf8mb3TableComments**

**Precheck level: Error**

**Check for invalid utf8mb3 characters in table definition**

This precheck identifies tables that contain comments with invalid `utf8mb3` character encoding. In MySQL 8.0, stricter validation is applied to character encoding in metadata, including table comments. If any table comments contain characters that are not valid in the `utf8mb3` character set, the upgrade fails.

To resolve this issue, you must modify the table comments to remove or replace any non-BMP characters before attempting the upgrade.

**Example output:**

```
{
    "id": "auroraUpgradeCheckForInvalidUtf8mb3TableComments",
    "title": "Check for invalid utf8mb3 table comments.",
    "status": "OK",
    "description": "Following table(s) has/have invalid utf8mb3 comments.",
    "detectedProblems": [
        {
            "level": "Error",
            "dbObject": "precheck.utf8mb3_table_with_comment",
            "description": "Table precheck.utf8mb3_table_with_comment has invalid utf8mb3 comments. This is due to https://bugs.mysql.com/bug.php?id=110177. To fix the inconsistency, we recommend you to modify comment fields to not use non-BMP characters and try the upgrade again."
        }

    ]
},
```

The precheck reports invalid `utf8mb3` comments defined for the `utf8mb3_table_with_comment` tables in the test database.

To resolve this issue, identify the table that contains unsupported characters and update the comments. First, examine the table structure and identify the comments.

```
MySQL> SHOW CREATE TABLE precheck.utf8mb3_table_with_comment\G
*************************** 1. row ***************************
    Table: utf8mb3_table_with_comment
Create Table: CREATE TABLE `utf8mb3_table_with_comment` (
`id` int(11) NOT NULL,
`name` varchar(100) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table comment contains flag 🏳️'
1 row in set (0.00 sec)
```

Once you've identified table comments that contain unsupported chatacters, update the comments with the `ALTER TABLE` statement.

```
MySQL> ALTER TABLE precheck.utf8mb3_table_with_comment COMMENT='Updated comment without non-BMP characters';
```

Alternatively, you can remove the comment.

```
MySQL> ALTER TABLE precheck.utf8mb3_table_with_comment COMMENT='';
```

After you remove all unsupported characters from all table comments, the precheck succeeds.

```
{
"id": "auroraUpgradeCheckForInvalidUtf8mb3TableComments",
"title": "Check for invalid utf8mb3 table comments.",
"status": "OK",
"detectedProblems": []
},
```

**auroraUpgradeCheckForMasterUser**

**Precheck level: Error**

**Check whether RDS master user exists**

MySQL 8 has added a new privilege model with support for [role](https://dev.mysql.com/doc/refman/8.0/en/roles.html "https://dev.mysql.com/doc/refman/8.0/en/roles.html") and [dynamic privileges](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#static-dynamic-privileges "https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#static-dynamic-privileges") to make privilege management easier and more fine grained. As part of this change, Aurora MySQL has
introduced the new `rds_superuser_role`, which is automatically granted to the database’s master user on upgrade from
Aurora MySQL version 2 to version 3.

For more information on the roles and privileges assigned to the master user in Aurora MySQL, see [Master user account privileges](UsingWithRDS.md "UsingWithRDS.md"). For more information on the role-based
privilege model in Aurora MySQL version 3, see [Role-based privilege model](AuroraMySQL.md#AuroraMySQL.privilege-model "AuroraMySQL.md#AuroraMySQL.privilege-model").

This precheck verifies that the master user exists in the database. If the master user doesn't exist, the precheck fails. To allow
the upgrade to proceed, re-create the master user by resetting the master user password, or by manually creating the user. Then
retry the upgrade. For more information on resetting the master user password, see [Changing the password for the database master user](Aurora.md#Aurora.Modifying.Password "Aurora.md#Aurora.Modifying.Password").

**Example output:**

```
{
  "id": "auroraUpgradeCheckForMasterUser",
  "title": "Check if master user exists",
  "status": "OK",
  "description": "Throws error if master user has been dropped!",
  "documentationLink": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "all",
        "description": "Your Master User on host '%' has been dropped. To proceed with the upgrade, recreate the master user `reinvent` on default host '%'"
      }
  ]
}
```

After you reset your master user password, the precheck will pass, and you can retry the upgrade.

The following example uses the AWS CLI to reset the password. Password changes are applied immediately.

```
aws rds modify-db-cluster \
    --db-cluster-identifier `my-db-cluster` \
    --master-user-password `my-new-password`
```

Then the precheck succeeds.

```
{
  "id": "auroraUpgradeCheckForMasterUser",
  title": "Check if master user exists",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckForPrefixIndexOnGeometryColumns**

**Precheck level: Error**

**Check for geometry columns on prefix indexes**

As of [MySQL 8.0.12](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-12.html#mysqld-8-0-12-spatial-support "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-12.html#mysqld-8-0-12-spatial-support") , you can no longer create a [prefixed](https://dev.mysql.com/doc/refman/5.7/en/column-indexes.html#column-indexes-prefix "https://dev.mysql.com/doc/refman/5.7/en/column-indexes.html#column-indexes-prefix") index on a column using the [GEOMETRY](https://dev.mysql.com/doc/refman/5.7/en/gis-data-formats.html "https://dev.mysql.com/doc/refman/5.7/en/gis-data-formats.html") data type. For more information, see [WL#11808](https://dev.mysql.com/worklog/task/?id=11808 "https://dev.mysql.com/worklog/task/?id=11808").

If any such indexes exist, your upgrade will fail. To resolve the issue, drop the prefixed `GEOMETRY` indexes on the
tables mentioned in the precheck failure.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForPrefixIndexOnGeometryColumns",
  "title": "Check for geometry columns on prefix indexs",
  "status": "OK",
  "description": "Consider dropping the prefix Indexes of geometry columns and restart the upgrade.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.geom_index_prefix",
        "description": "Table `test`.`geom_index_prefix` has an index `LatLon` on geometry column/s. Mysql 8.0 does not support this type of index on a geometry column https://dev.mysql.com/worklog/task/?id=11808. To upgrade to MySQL 8.0, Run 'DROP INDEX `LatLon` ON `test`.`geom_index_prefix`;"
      }
  ]
}
```

The precheck reports an error because the `test.geom_index_prefix` table contains an index with a prefix on a
`GEOMETRY` column.

After you drop this index, the precheck succeeds.

```
{
  "id": "auroraUpgradeCheckForPrefixIndexOnGeometryColumns",
  "title": "Check for geometry columns on prefix indexs",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckForSpecialCharactersInProcedures**

**Precheck level: Error**

**Check for inconsistency related to special characters in stored procedures**

Before MySQL 8.0, database names, table names, and other objects corresponded to files in the data directory, that is, file-based
metadata. As part of the upgrade to MySQL 8.0, all database objects are migrated to the new internal data dictionary tables that are
stored in the `mysql` schema to support the newly implemented [Atomic Data Dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html"). As part of
migrating stored procedures, the procedure definition and body for each procedure is validated as it's ingested into the new data
dictionary.

Before MySQL 8, in some cases it was possible to create stored routines, or insert directly into the `mysql.proc`
table, procedures that contained special characters. For example, you could create a stored procedure that contained a comment with
the noncompliant, [non-breaking space character](https://en.wikipedia.org/wiki/Non-breaking_space "https://en.wikipedia.org/wiki/Non-breaking_space")
`\xa0`. If any such procedures are encountered, the upgrade fails.

This precheck validates that the bodies and definitions of your stored procedures don't contain any such characters. To allow the
upgrade to proceed, re-create these stored procedures without any hidden or special characters.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForSpecialCharactersInProcedures",
  "title": "Check for inconsistency related to special characters in stored procedures.",
  "status": "OK",
  "description": "Following procedure(s) has special characters inconsistency.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "information_schema.routines",
        "description": "Data Dictionary Metadata is inconsistent for the procedure `get_version_proc` in the database `test` due to usage of special characters in procedure body. To avoid that, drop and recreate the procedure without any special characters before proceeding with the Upgrade."
      }
  ]
}
```

The precheck reports that the DB cluster contains a procedure called `get_version_proc` in the `test`
database that contains special characters in the procedure body.

After dropping and re-creating the stored procedure, the precheck succeeds, allowing the upgrade to proceed.

```
{
  "id": "auroraUpgradeCheckForSpecialCharactersInProcedures",
  "title": "Check for inconsistency related to special characters in stored procedures.",
  "status": "OK",
  "detectedProblems": []
},
```

**auroraUpgradeCheckForSysSchemaObjectTypeMismatch**

**Precheck level: Error**

**Check object type mismatch for `sys` schema**

The [sys schema](https://dev.mysql.com/doc/refman/8.0/en/sys-schema.html "https://dev.mysql.com/doc/refman/8.0/en/sys-schema.html") is a set of objects and views in a
MySQL database that helps users troubleshoot, optimize, and monitor their DB instances. When performing a major version upgrade from
Aurora MySQL version 2 to version 3, the `sys` schema views are re-created and updated to the new Aurora MySQL version 3
definitions.

As part of the upgrade, if any objects in the `sys` schema are defined using storage engines (`sys_config/BASE
 TABLE` in [INFORMATION_SCHEMA.TABLES](https://dev.mysql.com/doc/refman/5.7/en/information-schema-tables-table.html "https://dev.mysql.com/doc/refman/5.7/en/information-schema-tables-table.html")), rather than views, the upgrade will fail. Such tables can be found in the
`information_schema.tables` table. This is not an expected behavior, but in some cases can occur due to user
error.

This precheck validates all `sys` schema objects to ensure that they use the correct table definitions, and that views
aren't mistakenly defined as InnoDB or MyISAM tables. To resolve the issue, manually fix any returned objects by renaming or
dropping them. Then retry the upgrade.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForSysSchemaObjectTypeMismatch",
  "title": "Check object type mismatch for sys schema.",
  "status": "OK",
  "description": "Database contains objects with type mismatch for sys schema.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "sys.waits_global_by_latency",
        "description": "Your object sys.waits_global_by_latency has a type mismatch. To fix the inconsistency we recommend to rename or remove the object before upgrading (use RENAME TABLE command). "
      }
  ]
}
```

The precheck reports that the [sys.waits_global_by_latency](https://dev.mysql.com/doc/refman/5.7/en/sys-waits-global-by-latency.html "https://dev.mysql.com/doc/refman/5.7/en/sys-waits-global-by-latency.html") view in the `sys` schema has a type mismatch that is blocking the upgrade from
proceeding.

After logging into the DB instance, you can see that this object is defined as a InnoDB table, when it should be a view.

```
mysql> show create table sys.waits_global_by_latency\G
*************************** 1. row ***************************
       Table: waits_global_by_latency
Create Table: CREATE TABLE `waits_global_by_latency` (
  `events` varchar(128) DEFAULT NULL,
  `total` bigint(20) unsigned DEFAULT NULL,
  `total_latency` text,
  `avg_latency` text,
  `max_latency` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
```

To resolve this issue we can either drop and re-create the view with the [correct
definition](https://github.com/mysql/mysql-server/blob/mysql-5.7.44/scripts/sys_schema/views/p_s/waits_global_by_latency.sql "https://github.com/mysql/mysql-server/blob/mysql-5.7.44/scripts/sys_schema/views/p_s/waits_global_by_latency.sql") or rename it. During the upgrade process, it will be automatically created with the correct table
definition.

```
mysql> RENAME TABLE sys.waits_global_by_latency to sys.waits_global_by_latency_old;
Query OK, 0 rows affected (0.01 sec)
```

After doing this, the precheck passes.

```
{
  "id": "auroraUpgradeCheckForSysSchemaObjectTypeMismatch",
  "title": "Check object type mismatch for sys schema.",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckForViewColumnNameLength**

**Precheck level: Error**

**Check upper limit for column name in view**

The [maximum permitted length of a column name](https://dev.mysql.com/doc/refman/5.7/en/identifier-length.html "https://dev.mysql.com/doc/refman/5.7/en/identifier-length.html")
in MySQL is 64 characters. Before MySQL 8.0, in some cases it was possible to create a view with a column name larger than 64
characters. If any such views exist on your database instance, a precheck error is returned, and the upgrade will fail. To allow the
upgrade to proceed, you must re-create the views in question, making sure that their column lengths are less than 64 characters.
Then retry the upgrade.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForViewColumnNameLength",
  "title": "Check for upperbound limit related to column name in view.",
  "status": "OK",
  "description": "Following view(s) has column(s) with length greater than 64.",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.colname_view_test.col2_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad",
        "description": "View `test`.`colname_view_test`has column `col2_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad` with invalid column name length. To avoid Upgrade errors, view should be altered by renaming the column name so that its length is not 0 and doesn't exceed 64."
      }
  ]
}
```

The precheck reports that the `test.colname_view_test` view contains a column
`col2_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad` that exceeds the max permitted column
length of 64 characters.

Looking at the view definition, we can see the offending column.

```
mysql> desc `test`.`colname_view_test`;
+------------------------------------------------------------------+-------------+------+-----+---------+-------+
| Field                                                            | Type        | Null | Key | Default | Extra |
+------------------------------------------------------------------+-------------+------+-----+---------+-------+
| col1                                                             | varchar(20) | YES  |     | NULL    |       |
| col2_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad_pad | int(11)     | YES  |     | NULL    |       |
+------------------------------------------------------------------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```

To allow the upgrade to proceed, re-create the view, making sure that the column length doesn't exceed 64 characters.

```
mysql> drop view `test`.`colname_view_test`;
Query OK, 0 rows affected (0.01 sec)

mysql> create view `test`.`colname_view_test`(col1, col2_nopad) as select inf, fodcol from test;
Query OK, 0 rows affected (0.01 sec)

mysql> desc `test`.`colname_view_test`;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| col1       | varchar(20) | YES  |     | NULL    |       |
| col2_nopad | int(11)     | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```

After doing this, the precheck succeeds.

```
{
  "id": "auroraUpgradeCheckForViewColumnNameLength",
  "title": "Check for upperbound limit related to column name in view.",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckIndexLengthLimitOnTinyColumns**

**Precheck level: Error**

**Check for tables with indexes defined with a prefix length greater than 255 bytes on tiny columns**

When creating an index on a column using a [binary data
type](https://dev.mysql.com/doc/refman/5.7/en/binary-varbinary.html "https://dev.mysql.com/doc/refman/5.7/en/binary-varbinary.html") in MySQL, you must add a [prefix](https://dev.mysql.com/doc/refman/5.7/en/column-indexes.html#column-indexes-prefix "https://dev.mysql.com/doc/refman/5.7/en/column-indexes.html#column-indexes-prefix") length in the index
definition. Before MySQL 8.0, in some cases it was possible to specify a prefix length larger than the maximum allowed size of such
data types. An example is `TINYTEXT` and `TINYBLOB` columns, where the maximum permitted data size is 255
bytes, but index prefixes larger than this were permitted. For more information, see [InnoDB limits](https://dev.mysql.com/doc/refman/8.0/en/innodb-limits.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-limits.html") in the MySQL documentation.

If this precheck fails, drop the offending index or reduce the prefix length of `TINYTEXT` and `TINYBLOB`
columns of the index to less than 255 bytes. Then retry the upgrade.

**Example output:**

```
{
  "id": "auroraUpgradeCheckIndexLengthLimitOnTinyColumns",
  "title": "Check for the tables with indexes defined with prefix length greater than 255 bytes on tiny columns",
  "status": "OK",
  "description": "Prefix length of the indexes defined on tiny columns cannot exceed 255 bytes. With utf8mb4 char set, this limits the prefix length supported upto 63 characters only. A larger prefix length was allowed in MySQL5.7 using innodb_large_prefix parameter. This parameter is deprecated in MySQL 8.0.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/innodb-limits.html, https://dev.mysql.com/doc/refman/8.0/en/storage-requirements.html",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.tintxt_prefixed_index.col1",
        "description": "Index 'PRIMARY' on tinytext/tinyblob column `col1` of table `test.tintxt_prefixed_index` is defined with prefix length exceeding 255 bytes. Reduce the prefix length to <=255 bytes depending on character set used. For utf8mb4, it should be <=63."
      }
  ]
}
```

The precheck reports an error for the `test.tintxt_prefixed_index` table, because it has an Index `PRIMARY`
that has a prefix larger than 255 bytes on a TINYTEXT or TINYBLOB column.

Looking at the definition for this table, we can see that the primary key has a prefix of 65 on the `TINYTEXT` column
`col1`. Because the table is defined using the `utf8mb4` character set, which stores 4 bytes per
character, the prefix exceeds the 255-byte limit.

```
mysql> show create table `test`.`tintxt_prefixed_index`\G
*************************** 1. row ***************************
       Table: tintxt_prefixed_index
Create Table: CREATE TABLE `tintxt_prefixed_index` (
  `col1` tinytext NOT NULL,
  `col2` tinytext,
  `col_id` tinytext,
  PRIMARY KEY (`col1`(65))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC
1 row in set (0.00 sec)
```

Modifying the index prefix to 63 while using the `utf8mb4` character set will allow the upgrade to proceed.

```
mysql> alter table `test`.`tintxt_prefixed_index` drop PRIMARY KEY, ADD  PRIMARY KEY (`col1`(63));
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

After doing this, the precheck succeeds.

```
{
  "id": "auroraUpgradeCheckIndexLengthLimitOnTinyColumns",
  "title": "Check for the tables with indexes defined with prefix length greater than 255 bytes on tiny columns",
  "status": "OK",
  "detectedProblems": []
}
```

**auroraUpgradeCheckMissingInnodbMetadataForMysqlHostTable**

**Precheck level: Error**

**Check missing InnoDB metadata inconsistency for the `mysql.host` table**

This is an internal-only precheck carried out by the RDS service. Any errors will be automatically handled on upgrade and can be
safely ignored.

If you encounter any errors with this precheck, open a case with [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support")
to request that the metadata inconsistency be resolved. Alternatively, you can retry the upgrade by performing a logical dump, then
restoring to a new Aurora MySQL version 3 DB cluster.

## Warnings

The following prechecks generate warnings when the precheck fails, but the upgrade can proceed.

###### Topics

- [MySQL prechecks that report warnings](#precheck-descriptions-warnings.mysql "#precheck-descriptions-warnings.mysql")
- [Aurora MySQL prechecks that report warnings](#precheck-descriptions-warnings.aurora "#precheck-descriptions-warnings.aurora")

### MySQL prechecks that report warnings

The following prechecks are from Community MySQL:

- [defaultAuthenticationPlugin](#defaultAuthenticationPlugin "#defaultAuthenticationPlugin")
- [maxdbFlagCheck](#maxdbFlagCheck "#maxdbFlagCheck")
- [mysqlDollarSignNameCheck](#mysqlDollarSignNameCheck "#mysqlDollarSignNameCheck")
- [reservedKeywordsCheck](#reservedKeywordsCheck "#reservedKeywordsCheck")
- [utf8mb3Check](#utf8mb3Check "#utf8mb3Check")
- [zeroDatesCheck](#zeroDatesCheck "#zeroDatesCheck")

**defaultAuthenticationPlugin**

**Precheck level: Warning**

**New default authentication plugin considerations**

In MySQL 8.0, the `caching_sha2_password` authentication plugin was introduced, providing more secure password
encryption and better performance than the deprecated `mysql_native_password` plugin. For Aurora MySQL version 3, the
default authentication plugin used for database users is the `mysql_native_password` plugin.

This precheck warns that this plugin will be removed and the default changed in a future major version release. Consider
evaluating the compatibility of your application clients and users ahead of this change.

For more information, see [caching_sha2_password compatibility issues and solutions](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password-compatibility-issues "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password-compatibility-issues") in the MySQL documentation.

**Example output:**

```
{
  "id": "defaultAuthenticationPlugin",
  "title": "New default authentication plugin considerations",
  "description": "Warning: The new default authentication plugin 'caching_sha2_password' offers more secure password hashing than previously used 'mysql_native_password' (and consequent improved client connection authentication). However, it also has compatibility implications that may affect existing MySQL installations. If your MySQL installation must serve pre-8.0 clients and you encounter compatibility issues after upgrading, the simplest way to address those issues is to reconfigure the server to revert to the previous default authentication plugin (mysql_native_password). For example, use these lines in the server option file:\n\n[mysqld]\ndefault_authentication_plugin=mysql_native_password\n\nHowever, the setting should be viewed as temporary, not as a long term or permanent solution, because it causes new accounts created with the setting in effect to forego the improved authentication security.\nIf you are using replication please take time to understand how the authentication plugin changes may impact you.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password-compatibility-issues\nhttps://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password-replication"
},
```

**maxdbFlagCheck**

**Precheck level: Warning**

**Usage of obsolete `MAXDB`
`sql_mode` flag**

In MySQL 8.0, a number of deprecated [sql_mode](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_sql_mode "https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_sql_mode") system variable
options were [removed](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html"), one of which was
`MAXDB`. This precheck examines all currently connected sessions, along with routines and triggers, to ensure that
none have `sql_mode` set to any combination that includes `MAXDB`.

**Example output:**

```
{
  "id": "maxdbFlagCheck",
  "title": "Usage of obsolete MAXDB sql_mode flag",
  "status": "OK",
  "description": "Warning: The following DB objects have the obsolete MAXDB option persisted for sql_mode, which will be cleared during the upgrade. It can potentially change the datatype DATETIME into TIMESTAMP if it is used inside object's definition, and this in turn can change the behavior in case of dates earlier than 1970 or later than 2037. If this is a concern, please redefine these objects so that they do not rely on the MAXDB flag before running the upgrade.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html#mysql-nutshell-removals",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "test.maxdb_stored_routine",
        "description": "PROCEDURE uses obsolete MAXDB sql_mode",
        "dbObjectType": "Routine"
      }
  ]
}
```

The precheck reports that the `test.maxdb_stored_routine` routine contains a unsupported `sql_mode`
option.

After logging into the database, you can see in the routine definition that `sql_mode` contains
`MAXDB`.

```
 > SHOW CREATE PROCEDURE test.maxdb_stored_routine\G

*************************** 1. row ***************************
           Procedure: maxdb_stored_routine
            sql_mode: PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,MAXDB,NO_KEY_OPTIONS,NO_TABLE_OPTIONS,NO_FIELD_OPTIONS,NO_AUTO_CREATE_USER
    Create Procedure: CREATE DEFINER="msandbox"@"localhost" PROCEDURE "maxdb_stored_routine"()
BEGIN
    SELECT * FROM test;
END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
1 row in set (0.00 sec)
```

To resolve the issue, re-create the procedure after setting the correct `sql_mode` on the client.

###### Note

According to the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html "https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html"), MySQL
stores the `sql_mode` setting that's in effect when a routine is created or altered. It always runs the routine with
this setting, regardless of the `sql_mode` setting when the routine starts.

Before changing `sql_mode`, see [Server SQL
modes](https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html "https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html") in the MySQL documentation. Carefully evaluate any potential impact of doing so on your application.

Re-create the procedure without the unsupported `sql_mode`.

```
mysql > set sql_mode='PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE';
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql > DROP PROCEDURE test.maxdb_stored_routine\G
Query OK, 0 rows affected (0.00 sec)

mysql >
mysql > DELIMITER $$
mysql >
mysql > CREATE PROCEDURE test.maxdb_stored_routine()
    -> SQL SECURITY DEFINER
    -> BEGIN
    ->     SELECT * FROM test;
    -> END$$
Query OK, 0 rows affected (0.00 sec)

mysql >
mysql > DELIMITER ;
mysql > show create procedure test.maxdb_stored_routine\G
*************************** 1. row ***************************
           Procedure: maxdb_stored_routine
            sql_mode: PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE
    Create Procedure: CREATE DEFINER="msandbox"@"localhost" PROCEDURE "maxdb_stored_routine"()
BEGIN
    SELECT * FROM test;
END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
1 row in set (0.00 sec)
```

The precheck succeeds.

```
{
  "id": "maxdbFlagCheck",
  "title": "Usage of obsolete MAXDB sql_mode flag",
  "status": "OK",
  "detectedProblems": []
}
```

**mysqlDollarSignNameCheck**

**Precheck level: Warning**

**Check for deprecated usage of single dollar signs in object names**

As of [MySQL
8.0.32](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-32.html#mysqld-8-0-32-deprecation-removal "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-32.html#mysqld-8-0-32-deprecation-removal"), use of the dollar sign (`$`) as the first character of an unquoted identifier is deprecated. If you
have any schemas, tables, views, columns, or routines containing a `$` as the first character, this precheck returns a
warning. While this warning doesn't block the upgrade from proceeding, we recommend that you take action soon to resolve this. From
[MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html") any such identifiers will return a
syntax error rather than a warning.

**Example output:**

```
{
  "id": "mysqlDollarSignNameCheck",
  "title": "Check for deprecated usage of single dollar signs in object names",
  "status": "OK",
  "description": "Warning: The following objects have names with deprecated usage of dollar sign ($) at the begining of the identifier. To correct this warning, ensure, that names starting with dollar sign, also end with it, similary to quotes ($example$). ",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "test.$deprecated_syntx",
        "description": " name starts with $ sign."
      }
  ]
},
```

The precheck reports a warning because the `$deprecated_syntx` table in the `test` schema contains a
`$` as the first character.

**reservedKeywordsCheck**

**Precheck level: Warning**

**Usage of database objects with names conflicting with new reserved keywords**

This check is similar to the [routineSyntaxCheck](#routineSyntaxCheck "#routineSyntaxCheck"), in that it checks for usage of database
objects with names conflicting with new reserved keywords. While they don't block upgrades, you need to evaluate warnings
carefully.

**Example output:**

Using the previous example with the table named `except`, the precheck returns a warning:

```
{
  "id": "reservedKeywordsCheck",
  "title": "Usage of db objects with names conflicting with new reserved keywords",
  "status": "OK",
  "description": "Warning: The following objects have names that conflict with new reserved keywords. Ensure queries sent by your applications use `quotes` when referring to them or they will result in errors.",
  "documentationLink": "https://dev.mysql.com/doc/refman/en/keywords.html",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "test.except",
        "description": "Table name",
        "dbObjectType": "Table"
      }
  ]
}
```

This warning lets you know that there might be some application queries to review. If your application queries aren't correctly
[escaping string literals](https://dev.mysql.com/doc/refman/8.0/en/string-literals.html "https://dev.mysql.com/doc/refman/8.0/en/string-literals.html"), they might
experience errors after upgrading to MySQL 8.0. Review your applications to confirm, testing against a clone or snapshot of your
Aurora MySQL DB cluster running on version 3.

Example of a non-escaped application query that will fail after upgrading:

```
SELECT * FROM escape;
```

Example of a correctly escaped application query that will succeed after upgrading:

```
SELECT * FROM 'escape';
```

**utf8mb3Check**

**Precheck level: Warning**

**Usage of `utf8mb3` character set**

In MySQL 8.0 the `utf8mb3` character set is deprecated, and will be removed in a future MySQL major version. This
precheck is implemented to raise a warning if any database objects using this character set are detected. While this won't block an
upgrade from proceeding, we highly recommend that you think about migrating tables to the `utf8mb4` character set, which
is the default as of MySQL 8.0. For more information on [utf8mb3](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb3.html "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb3.html") and [utf8mb4](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb4.html "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb4.html"), see [Converting between 3-byte and 4-byte Unicode
character sets](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-conversion.html "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-conversion.html") in the MySQL documentation.

**Example output:**

```
{
  "id": "utf8mb3",
  "title": "Usage of utf8mb3 charset",
  "status": "OK",
  "description": "Warning: The following objects use the deprecated utf8mb3 character set. It is recommended to convert them to use utf8mb4 instead, for improved Unicode support. The utf8mb3 character is subject to removal in the future.",
  "documentationLink": "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb3.html",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "test.t1.col1",
        "description": "column's default character set: utf8",
        "dbObjectType": "Column"
      },
      {
        "level": "Warning",
        "dbObject": "test.t1.col2",
        "description": "column's default character set: utf8",
        "dbObjectType": "Column"
      }
  ]
}
```

To resolve this issue, you rebuild the objects and tables referenced. For more information and prerequisites before doing so, see
[Converting between 3-byte and 4-byte
Unicode character sets](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-conversion.html "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-conversion.html") in the MySQL documentation.

**zeroDatesCheck**

**Precheck level: Warning**

**Zero date, datetime, and timestamp values**

MySQL now enforces stricter rules regarding the use of zero values in date, datetime, and timestamp columns. We recommend that you
use the `NO_ZERO_IN_DATE` and `NO_ZERO_DATE SQL` modes in conjunction with `strict` mode, as they
will be merged with `strict` mode in a future MySQL release.

If the `sql_mode` setting for any of your database connections, at the time of running the precheck, doesn't include
these modes, a warning is raised in the precheck. Users might still be able to insert date, datetime, and timestamp values
containing zero values. However, we strongly advise replacing any zero values with valid ones, as their behavior might change in the
future and they might not function correctly. As this is a warning, it won't block upgrades, but we recommend that you start
planning to take action.

**Example output:**

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

### Aurora MySQL prechecks that report warnings

The following prechecks are specific to Aurora MySQL:

- [auroraUpgradeCheckForRollbackSegmentHistoryLength](#auroraUpgradeCheckForRollbackSegmentHistoryLength "#auroraUpgradeCheckForRollbackSegmentHistoryLength")
- [auroraUpgradeCheckForUncommittedRowModifications](#auroraUpgradeCheckForUncommittedRowModifications "#auroraUpgradeCheckForUncommittedRowModifications")

**auroraUpgradeCheckForRollbackSegmentHistoryLength**

**Precheck level: Warning**

**Checks whether the rollback segment history list length for the cluster is high**

As mentioned in [auroraUpgradeCheckForIncompleteXATransactions](#auroraUpgradeCheckForIncompleteXATransactions "#auroraUpgradeCheckForIncompleteXATransactions"), while running the major version upgrade process, it is essential that the
Aurora MySQL version 2 DB instance undergo a [clean shutdown](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_slow_shutdown "https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_slow_shutdown"). This ensures that all transactions are committed or rolled back, and that InnoDB has purged all undo
log records.

If your DB cluster has a high rollback segment history list length (HLL), it can prolong the amount of time that InnoDB takes to
complete its purge of undo log records, leading to extended downtime during the major version upgrade process. If the precheck
detects that the HLL on your DB cluster is high, it raises a warning. While this doesn't block your upgrade from proceeding, we
recommend that you closely monitor the HLL on your DB cluster. Keeping it at low levels reduces the downtime required during a major
version upgrade. For more information on monitoring HLL, see [The InnoDB history list length increased
significantly](proactive-insights.md "proactive-insights.md").

**Example output:**

```
{
  "id": "auroraUpgradeCheckForRollbackSegmentHistoryLength",
  "title": "Checks if the rollback segment history length for the cluster is high",
  "status": "OK",
  "description": "Rollback Segment History length is greater than 1M. Upgrade may take longer time.",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "information_schema.innodb_metrics",
        "description": "The InnoDB undo history list length('trx_rseg_history_len') is 82989114. Upgrade may take longer due to purging of undo information for old row versions."
      }
  ]
}
```

The precheck returns a warning because it detected the InnoDB undo HLL was high on the database cluster (82989114). Although the
upgrade proceeds, depending on the amount of undo to purge, it can extend the downtime required during the upgrade process.

We recommend that you [investigate open transactions](proactive-insights.md "proactive-insights.md")
on your DB cluster before running the upgrade in production, to make sure your HLL is kept at a manageable size.

**auroraUpgradeCheckForUncommittedRowModifications**

**Precheck level: Warning**

**Checks whether there are many uncommitted row modifications**

As mentioned in [auroraUpgradeCheckForIncompleteXATransactions](#auroraUpgradeCheckForIncompleteXATransactions "#auroraUpgradeCheckForIncompleteXATransactions"), while running the major version upgrade process, it is essential that the
Aurora MySQL version 2 DB instance undergo a [clean shutdown](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_slow_shutdown "https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_slow_shutdown"). This ensures that all transactions are committed or rolled back, and that InnoDB has purged all undo
log records.

If your DB cluster has transactions that have modified a large number of rows, it can prolong the amount of time InnoDB takes to
complete a rollback of this transaction as part of the clean shutdown process. If the precheck finds long-running transactions, with
a large number of modified rows on your DB cluster, it raises a warning. While this doesn't block your upgrade from proceeding, we
recommend that you closely monitor the size of active transactions on your DB cluster. Keeping it at low levels reduces the downtime
required during a major version upgrade.

**Example output:**

```
{
  "id": "auroraUpgradeCheckForUncommittedRowModifications",
  "title": "Checks if there are many uncommitted modifications to rows",
  "status": "OK",
  "description": "Database contains uncommitted row changes greater than 10M. Upgrade may take longer time.",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "information_schema.innodb_trx",
        "description": "The database contains 11000000 uncommitted row change(s) in 1 transaction(s). Upgrade may take longer due to transaction rollback."
      }
  ]
},
```

The precheck reports that the DB cluster contains a transaction with 11,000,000 uncommitted row changes that will need to be
rolled back during the clean shutdown process. The upgrade will proceed, but to reduce downtime during the upgrade process, we
recommend that you monitor and investigate this before running the upgrade on your production clusters.

To view active transactions on your writer DB instance, you can use the [information_schema.innodb_trx](https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-trx-table.html "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-trx-table.html")
table. The following query on the writer DB instance shows current transactions, run time, state, and modified rows for the DB
cluster.

```
# Example of uncommitted transaction
mysql> SELECT trx_started,
       TIME_TO_SEC(TIMEDIFF(now(), trx_started)) AS seconds_trx_has_been_running,
       trx_mysql_thread_id AS show_processlist_connection_id,
       trx_id,
       trx_state,
       trx_rows_modified AS rows_modified
FROM information_schema.innodb_trx;
+---------------------+------------------------------+--------------------------------+----------+-----------+---------------+
| trx_started         | seconds_trx_has_been_running | show_processlist_connection_id | trx_id   | trx_state | rows_modified |
+---------------------+------------------------------+--------------------------------+----------+-----------+---------------+
| 2024-08-12 18:32:52 |                         1592 |                          20041 | 52866130 | RUNNING   |      11000000 |
+---------------------+------------------------------+--------------------------------+----------+-----------+---------------+
1 row in set (0.01 sec)

# Example of transaction rolling back
mysql> SELECT trx_started,
       TIME_TO_SEC(TIMEDIFF(now(), trx_started)) AS seconds_trx_has_been_running,
       trx_mysql_thread_id AS show_processlist_connection_id,
       trx_id,
       trx_state,
       trx_rows_modified AS rows_modified
FROM information_schema.innodb_trx;
+---------------------+------------------------------+--------------------------------+----------+--------------+---------------+
| trx_started         | seconds_trx_has_been_running | show_processlist_connection_id | trx_id   | trx_state    | rows_modified |
+---------------------+------------------------------+--------------------------------+----------+--------------+---------------+
| 2024-08-12 18:32:52 |                         1719 |                          20041 | 52866130 | ROLLING BACK |      10680479 |
+---------------------+------------------------------+--------------------------------+----------+--------------+---------------+
1 row in set (0.01 sec)
```

After the transaction is committed or rolled back, the precheck no longer returns a warning. Consult the MySQL documentation and
your application team before rolling back any large transactions, as rollback can take some time to complete, depending on
transaction size.

```
{
  "id": "auroraUpgradeCheckForUncommittedRowModifications",
  "title": "Checks if there are many uncommitted modifications to rows",
  "status": "OK",
  "detectedProblems": []
},
```

For more information on optimizing InnoDB transaction management, and the potential impact of running and rolling back large
transactions on MySQL database instances, see [Optimizing InnoDB transaction
management](https://dev.mysql.com/doc/refman/5.7/en/optimizing-innodb-transaction-management.html "https://dev.mysql.com/doc/refman/5.7/en/optimizing-innodb-transaction-management.html") in the MySQL documentation.

## Notices

The following precheck generates a notice when the precheck fails, but the upgrade can proceed.

**sqlModeFlagCheck**

**Precheck level: Notice**

**Usage of obsolete `sql_mode` flags**

In addition to `MAXDB`, a number of other `sql_mode` options have been [removed](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html"): `DB2`, `MSSQL`,
`MYSQL323`, `MYSQL40`, `ORACLE`, `POSTGRESQL`, `NO_FIELD_OPTIONS`,
`NO_KEY_OPTIONS`, and `NO_TABLE_OPTIONS`. As of MySQL 8.0, none of these values can be assigned to the
`sql_mode` system variable. If this precheck finds any open sessions using these `sql_mode` settings, make
sure that your DB instance and DB cluster parameter groups, and client applications and configurations, are updated to disable them.-
For more information, see the [MySQL
documentation](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html").

**Example output:**

```
{
  "id": "sqlModeFlagCheck",
  "title": "Usage of obsolete sql_mode flags",
  "status": "OK",
  "detectedProblems": []
}
```

To resolve any of these precheck failures, see [maxdbFlagCheck](#maxdbFlagCheck "#maxdbFlagCheck").

## Errors, warnings, or notices

The following precheck can return an error, warning, or notice depending on the precheck output.

**checkTableOutput**

**Precheck level: Error, Warning, or Notice**

**Issues reported by the `check table x for upgrade` command**

Before starting the upgrade to Aurora MySQL version 3, `check table for upgrade` is run on each table in the user schemas in
your DB cluster. This precheck isn't the same as [checkTableMysqlSchema](#checkTableMysqlSchema "#checkTableMysqlSchema").

The `check table for upgrade` command examines tables for any potential issues that might arise during an upgrade to a
newer version of MySQL. Running this command before attempting an upgrade can help identify and resolve any incompatibilities ahead of
time, making the actual upgrade process smoother.

This command performs various checks on each table, such as the following:

- Verifying that the table structure and metadata are compatible with the target MySQL version
- Checking for any deprecated or removed features used by the table
- Ensuring that the table can be properly upgraded without data loss

Unlike other prechecks, it can return an error, warning, or notice depending on the `check table` output. If this precheck
returns any tables, review them carefully, along with the return code and message before initiating the upgrade. For more information,
see [CHECK TABLE statement](https://dev.mysql.com/doc/refman/5.7/en/check-table.html "https://dev.mysql.com/doc/refman/5.7/en/check-table.html") in the MySQL
documentation.

Here we provide an error example and a warning example.

**Error example:**

```
{
  "id": "checkTableOutput",
  "title": "Issues reported by 'check table x for upgrade' command",
  "status": "OK",
  "detectedProblems": [
      {
        "level": "Error",
        "dbObject": "test.parent",
        "description": "Table 'test.parent' doesn't exist"
      }
  ]
},
```

The precheck reports an error that the `test.parent` table doesn't exist.

The `mysql-error.log` file for the writer DB instance shows that there is a foreign key error.

```
2024-08-13T15:32:10.676893Z 62 [Warning] InnoDB: Load table `test`.`parent` failed, the table has missing foreign key indexes. Turn off 'foreign_key_checks' and try again.
2024-08-13T15:32:10.676905Z 62 [Warning] InnoDB: Cannot open table test/parent from the internal data dictionary of InnoDB though the .frm file for the table exists.
Please refer to http://dev.mysql.com/doc/refman/5.7/en/innodb-troubleshooting.html for how to resolve the issue.
```

Log into the writer DB instance and run `show engine innodb status\G` to get more information on the foreign key
error.

```
mysql> show engine innodb status\G
*************************** 1. row ***************************
  Type: InnoDB
  Name:
Status:
=====================================
2024-08-13 15:33:33 0x14ef7b8a1700 INNODB MONITOR OUTPUT
=====================================
.
.
.
------------------------
LATEST FOREIGN KEY ERROR
------------------------
2024-08-13 15:32:10 0x14ef6dbbb700 Error in foreign key constraint of table test/child:
there is no index in referenced table which would contain
the columns as the first columns, or the data types in the
referenced table do not match the ones in table. Constraint:
,
  CONSTRAINT `fk_pname` FOREIGN KEY (`p_name`) REFERENCES `parent` (`name`)
The index in the foreign key in table is p_name_idx
Please refer to http://dev.mysql.com/doc/refman/5.7/en/innodb-foreign-key-constraints.html for correct foreign key definition.
.
.
```

The `LATEST FOREIGN KEY ERROR` message reports that the `fk_pname` foreign key constraint in the
`test.child` table, which references the `test.parent` table,has either a missing index or data type mismatch.
The MySQL documentation on [foreign key
constraints](https://dev.mysql.com/doc/refman/5.7/en/create-table-foreign-keys.html "https://dev.mysql.com/doc/refman/5.7/en/create-table-foreign-keys.html") states that columns referenced in a foreign key must have an associated index, and the parent/child columns must
use the same data type.

To verify whether this is related to a missing index or data type mismatch, log into the database and check the table definitions by
temporarily disabling the session variable [foreign_key_checks](https://dev.mysql.com/doc/refman/5.7/en/create-table-foreign-keys.html#foreign-key-checks "https://dev.mysql.com/doc/refman/5.7/en/create-table-foreign-keys.html#foreign-key-checks"). After
doing so, we can see that the child constraint in question (`fk_pname`) uses `p_name varchar(20) CHARACTER SET latin1
 DEFAULT NULL` to reference the parent table `name varchar(20) NOT NULL`. The parent table uses `DEFAULT
 CHARSET=utf8`, but the child table’s `p_name` column uses `latin1`, so the data type mismatch error is
thrown.

```
mysql> show create table parent\G
ERROR 1146 (42S02): Table 'test.parent' doesn't exist

mysql> show create table child\G
*************************** 1. row ***************************
       Table: child
Create Table: CREATE TABLE `child` (
  `id` int(11) NOT NULL,
  `p_name` varchar(20) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `p_name_idx` (`p_name`),
  CONSTRAINT `fk_pname` FOREIGN KEY (`p_name`) REFERENCES `parent` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

mysql> set foreign_key_checks=0;
Query OK, 0 rows affected (0.00 sec)

mysql> show create table parent\G
*************************** 1. row ***************************
       Table: parent
Create Table: CREATE TABLE `parent` (
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

mysql> show create table child\G
*************************** 1. row ***************************
       Table: child
Create Table: CREATE TABLE `child` (
  `id` int(11) NOT NULL,
  `p_name` varchar(20) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `p_name_idx` (`p_name`),
  CONSTRAINT `fk_pname` FOREIGN KEY (`p_name`) REFERENCES `parent` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
```

To resolve this issue, we can either change the child table to use the same character set as the parent, or change the parent to use
the same character set as the child table. Here, because the child table explicitly uses `latin1` in the `p_name`
column definition, we run `ALTER TABLE` to modify the character set to `utf8`.

```
mysql> alter table child modify p_name varchar(20) character set utf8 DEFAULT NULL;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> flush tables;
Query OK, 0 rows affected (0.01 sec)
```

After doing so, the precheck passes, and the upgrade can proceed.

**Warning example:**

```
{
  "id": "checkTableOutput",
  "title": "Issues reported by 'check table x for upgrade' command",
  "status": "OK",
  "detectedProblems": [
      {
        "level": "Warning",
        "dbObject": "test.orders",
        "description": "Trigger test.orders.delete_audit_trigg does not have CREATED attribute."
      }
  ]
}
```

The precheck reports a warning for the `delete_audit_trigg` trigger on the `test.orders` table because it
doesn't have a `CREATED` attribute. According to [Checking version
compatibility](https://dev.mysql.com/doc/refman/5.7/en/check-table.html#check-table-version-compatibility "https://dev.mysql.com/doc/refman/5.7/en/check-table.html#check-table-version-compatibility") in the MySQL documentation, this message is informational, and is printed for triggers created before MySQL
5.7.2.

Because this is a warning, it doesn't block the upgrade from proceeding. However, if you wish to resolve the issue, you can re-create
the trigger in question, and the precheck succeeds with no warnings.

```
{
  "id": "checkTableOutput",
  "title": "Issues reported by 'check table x for upgrade' command",
  "status": "OK",
  "detectedProblems": []
},
```
