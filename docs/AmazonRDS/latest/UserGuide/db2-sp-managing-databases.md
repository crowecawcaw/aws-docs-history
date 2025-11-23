# Stored procedures for databases for

RDS for Db2

The built-in stored procedures described in this topic manage databases for Amazon RDS for Db2.
To run these procedures, the master user must first connect to the `rdsadmin`
database.

These stored procedures are used in a variety of tasks. This list isn't exhaustive.

- [Common tasks for databases](db2-managing-databases.md "db2-managing-databases.md")
- [Creating databases with EBCDIC collation](db2-ebcdic.md "db2-ebcdic.md")
- [Collecting information about
  databases](db2-supported-parameters.md#db2-modifying-parameters-db2-commands "db2-supported-parameters.md#db2-modifying-parameters-db2-commands")
- [Modifying database
  configuration parameters](db2-supported-parameters.md#db2-modifying-parameters-db2-commands "db2-supported-parameters.md#db2-modifying-parameters-db2-commands")
- [Migrating from Linux to
  Linux](db2-one-time-migration-linux.md "db2-one-time-migration-linux.md")
- [Migrating from Linux to Linux
  with near-zero downtime](db2-near-zero-downtime-migration.md "db2-near-zero-downtime-migration.md")
  Refer to the following built-in stored procedures for information about their syntax,
  parameters, usage notes, and examples.

###### Stored procedures

- [rdsadmin.create_database](#db2-sp-create-database "#db2-sp-create-database")
- [rdsadmin.deactivate_database](#db2-sp-deactivate-database "#db2-sp-deactivate-database")
- [rdsadmin.activate_database](#db2-sp-activate-database "#db2-sp-activate-database")
- [rdsadmin.reactivate_database](#db2-sp-reactivate-database "#db2-sp-reactivate-database")
- [rdsadmin.drop_database](#db2-sp-drop-database "#db2-sp-drop-database")
- [rdsadmin.update_db_param](#db2-sp-update-db-param "#db2-sp-update-db-param")
- [rdsadmin.set_configuration](#db2-sp-set-configuration "#db2-sp-set-configuration")
- [rdsadmin.show_configuration](#db2-sp-show-configuration "#db2-sp-show-configuration")
- [rdsadmin.backup_database](#db2-sp-backup-database "#db2-sp-backup-database")
- [rdsadmin.restore_database](#db2-sp-restore-database "#db2-sp-restore-database")
- [rdsadmin.rollforward_database](#db2-sp-rollforward-database "#db2-sp-rollforward-database")
- [rdsadmin.rollforward_status](#db2-sp-rollforward-status "#db2-sp-rollforward-status")
- [rdsadmin.complete_rollforward](#db2-sp-complete-rollforward "#db2-sp-complete-rollforward")
- [rdsadmin.db2pd_command](#db2-sp-db2pd-command "#db2-sp-db2pd-command")
- [rdsadmin.force_application](#db2-sp-force-application "#db2-sp-force-application")
- [rdsadmin.set_archive_log_retention](#db2-sp-set-archive-log-retention "#db2-sp-set-archive-log-retention")
- [rdsadmin.show_archive_log_retention](#db2-sp-show-archive-log-retention "#db2-sp-show-archive-log-retention")
- [rdsadmin.list_archive_log_information](#db2-sp-list-archive-log-information "#db2-sp-list-archive-log-information")
- [rdsadmin.fgac_command](#db2-sp-fgac-command "#db2-sp-fgac-command")

## rdsadmin.create_database

Creates a database.

### Syntax

```
db2 "call rdsadmin.create_database(
    '`database_name`',
    '`database_page_size`',
    '`database_code_set`',
    '`database_territory`',
    '`database_collation`',
    '`database_autoconfigure_str`',
    '`database_non-restrictive`')"
```

### Parameters

###### Note

This stored procedure doesn't validate the combination of required parameters.
When you call [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status"), the user-defined function could
return an error because of a combination of `database_codeset`,
`database_territory`, and `database_collation` that is
not valid. For more information, see [Choosing the code page, territory, and collation for your database](https://www.ibm.com/docs/en/db2/11.5?topic=support-choosing-code-page-territory-collation-your-database "https://www.ibm.com/docs/en/db2/11.5?topic=support-choosing-code-page-territory-collation-your-database")
in the IBM Db2 documentation.

The following parameter is required:

`database_name`

The name of the database to create. The data type is
`varchar`.

The following parameters are optional:

`database_page_size`

The default page size of the database. Valid values:
`4096`, `8192`, `16384`,
`32768`. The data type is `integer`. The
default is `8192`.

###### Important

Amazon RDS supports write atomicity for 4 KiB, 8 KiB, and 16 KiB pages.
In contrast, 32 KiB pages risk _torn
writes_, or partial data being written to the disk. If
you use 32 KiB pages, we recommend that you enable point-in-time
recovery and automated backups. Otherwise, you run the risk of being
unable to recover from torn pages. For more information, see [Introduction to backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md") and [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

`database_code_set`

The code set for the database. The data type is `varchar`.
The default is `UTF-8`.

`database_territory`

The two-letter country code for the database. The data type is
`varchar`. The default is `US`.

`database_collation`

The collation sequence that determines how character strings stored in
the database are sorted and compared. The data type is
`varchar`.

Valid values:

- `COMPATIBILITY` – An IBM Db2 Version 2
  collation sequence.
- `EBCDIC_819_037` – ISO Latin code page,
  collation; CCSID 037 (EBCDIC US English).
- `EBCDIC_819_500` – ISO Latin code page,
  collation; CCSID 500 (EBCDIC International).
- `EBCDIC_850_037` – ASCII Latin code page,
  collation; CCSID 037 (EBCDIC US English).
- `EBCDIC_850_500` – ASCII Latin code page,
  collation; CCSID 500 (EBCDIC International).
- `EBCDIC_932_5026` – ASCII Japanese code
  page, collation; CCSID 5026 (EBCDIC US English).
- `EBCDIC_932_5035` – ASCII Japanese code
  page, collation; CCSID 5035 (EBCDIC International).
- `EBCDIC_1252_037` – Windows Latin code page,
  collation; CCSID 037 (EBCDIC US English).
- `EBCDIC_1252_500` – Windows Latin code page,
  collation; CCSID 500 (EBCDIC International).
- `IDENTITY` – Default collation. Strings are
  compared byte for byte.
- `IDENTITY_16BIT` – The Compatibility
  Encoding Scheme for UTF-16: 8-bit (CESU-8) collation sequence.
  For more information, see [Unicode Technical Report #26](https://www.unicode.org/reports/tr26/tr26-4.html "https://www.unicode.org/reports/tr26/tr26-4.html") on the Unicode
  Consortium website.
- `NLSCHAR` – Only for use with the Thai code
  page (CP874).
- `SYSTEM` – If you use `SYSTEM`,
  the database uses the collation sequence automatically for
  `database_codeset` and
  `database_territory`.

The default is `IDENTITY`.

Additionally, RDS for Db2 supports the following groups of collations:
`language-aware-collation` and
`locale-sensitive-collation`. For more information, see
[Choosing a collation for a Unicode database](https://www.ibm.com/docs/en/db2/11.5?topic=collation-choosing-unicode-database "https://www.ibm.com/docs/en/db2/11.5?topic=collation-choosing-unicode-database") in the IBM Db2
documentation.

`database_autoconfigure_str`

The `AUTOCONFIGURE` command syntax, for example,
`'AUTOCONFIGURE APPLY DB'`. The data type is
`varchar`. The default is an empty string or null.

For more information, see [AUTOCONFIGURE command](https://www.ibm.com/docs/en/db2/11.5?topic=cc-autoconfigure "https://www.ibm.com/docs/en/db2/11.5?topic=cc-autoconfigure") in the IBM Db2
documentation.

`database_non-restrictive`

The granting of default authorities and privileges within the
database. The data type is `varchar`. The default is
`N`.

Valid values:

- `N` – The created database is restrictive
  and doesn't grant authorities or privileges.
- `Y` – The created database is
  non-restrictive and grants a set of permissions to the special
  group `PUBLIC`. For more information, see [Default privileges granted on creating a database](https://www.ibm.com/docs/en/db2/11.5.x?topic=ownership-default-privileges-granted-creating-database "https://www.ibm.com/docs/en/db2/11.5.x?topic=ownership-default-privileges-granted-creating-database")
  in the IBM Db2 documentation.

### Usage notes

If you plan on modifying the `db2_compatibility_vector` parameter,
modify the parameter before creating a database. For more information, see [Setting the
db2_compatibility_vector parameter](db2-known-issues-limitations.md#db2-known-issues-limitations-db2-compatibility-vector "db2-known-issues-limitations.md#db2-known-issues-limitations-db2-compatibility-vector").

Special considerations:

- The `CREATE DATABASE` command sent to the Db2 instance uses the
  `RESTRICTIVE` option.
- RDS for Db2 only uses `AUTOMATIC STORAGE` tablespaces.
- RDS for Db2 uses the default values for `NUMSEGS` and
  `DFT_EXTENT_SZ`.
- RDS for Db2 uses storage encryption and doesn't support database
  encryption.

For more information about these considerations, see [CREATE DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-create-database#:~:text=in%20the%20database.-,RESTRICTIVE,-If%20the%20RESTRICTIVE "https://www.ibm.com/docs/en/db2/11.5?topic=commands-create-database#:~:text=in%20the%20database.-,RESTRICTIVE,-If%20the%20RESTRICTIVE") in the IBM Db2
documentation.

Before calling `rdsadmin.create_database`, you must connect to the
`rdsadmin` database. In the following example, replace
`master_username` and
`master_password` with your RDS for Db2 DB instance
information:

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

For information about checking the status of creating a database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling `rdsadmin.create_database`,
see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

The following example creates a database called `TESTJP` with a correct
combination of the `database_code_set`,
`database_territory`, and
`database_collation` parameters for Japan:

```
db2 "call rdsadmin.create_database('TESTJP', 4096, 'IBM-437', 'JP', 'SYSTEM')"
```

## rdsadmin.deactivate_database

Deactivates a database.

### Syntax

```
db2 "call rdsadmin.deactivate_database(
    ?,
    '`database_name`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`database_name`

The name of the database to deactivate. The data type is
`varchar`.

### Usage notes

You can deactivate databases to conserve memory resources or to make other
database configuration changes. To bring deactivated databases back online, call the
[rdsadmin.activate_database](#db2-sp-activate-database "#db2-sp-activate-database") stored procedure.

You can't deactivate a database on a source DB instance during replication
by calling the `rdsadmin.deactivate_database` stored procedure.

For information about checking the status of deactivating a database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling
`rdsadmin.deactivate_database`, see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

The following example deactivates a database called `TESTDB`.

```
db2 "call rdsadmin.deactivate_database(?, 'TESTDB')"
```

## rdsadmin.activate_database

Activates a database.

For information about the differences between [rdsadmin.reactivate_database](#db2-sp-reactivate-database "#db2-sp-reactivate-database")
and `rdsadmin.activate_database`, see [Usage notes](#db2-sp-activate-database-usage-notes "#db2-sp-activate-database-usage-notes").

### Syntax

```
db2 "call rdsadmin.activate_database(
    ?,
    '`database_name`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`database_name`

The name of the database to activate. The data type is
`varchar`.

### Usage notes

All databases are activated by default when they are created. If you deactivate a database on a
standalone DB instance to conserve memory resources or to make other database
configuration changes, call the `rdsadmin.activate_database` stored
procedure to activate the database again.

This stored procedure only activates a database that is on a standalone DB
instance and that was deactivated by calling the [rdsadmin.deactivate_database](#db2-sp-deactivate-database "#db2-sp-deactivate-database") stored procedure. To activate a database on a replica source DB instance, you
must call the [rdsadmin.reactivate_database](#db2-sp-reactivate-database "#db2-sp-reactivate-database") stored procedure.

For information about checking the status of activating a database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling `rdsadmin.activate_database`,
see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

The following example activates a database called `TESTDB`.

```
db2 "call rdsadmin.activate_database(?, 'TESTDB')"
```

## rdsadmin.reactivate_database

Reactivates a database.

For information about differences between [rdsadmin.activate_database](#db2-sp-activate-database "#db2-sp-activate-database") and
`rdsadmin.reactivate_database`, see [Usage notes](#db2-sp-reactivate-database-usage-notes "#db2-sp-reactivate-database-usage-notes").

### Syntax

```
db2 "call rdsadmin.reactivate_database(
    ?,
    '`database_name`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`database_name`

The name of the database to reactivate. The data type is
`varchar`.

### Usage notes

When you call the `rdsadmin.reactivate_database` stored procedure, the
stored procedure first deactivates the database by calling the [rdsadmin.deactivate_database](#db2-sp-deactivate-database "#db2-sp-deactivate-database") stored procedure, and then activates the database by calling the [rdsadmin.activate_database](#db2-sp-activate-database "#db2-sp-activate-database")
stored procedure.

After you make changes to database configurations, you might need to reactivate a
database on an RDS for Db2 DB instance. To determine if you need to reactivate a
database, connect to the database and run `db2 get db cfg show detail`.

For a database on a standalone DB instance, you can use the
`rdsadmin.reactivate_database` store procedure to reactivate the
database. Or, if you already called the [rdsadmin.deactivate_database](#db2-sp-deactivate-database "#db2-sp-deactivate-database") stored procedure, you can call the
[rdsadmin.activate_database](#db2-sp-activate-database "#db2-sp-activate-database") stored procedure instead.

For a database on a replica source DB instance, you must use the
`rdsadmin.reactivate_database` stored procedure to reactivate the
database.

For information about checking the status of reactivating a database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling
`rdsadmin.reactivate_database`, see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

The following example reactivates a database called `TESTDB`.

```
db2 "call rdsadmin.reactivate_database(?, 'TESTDB')"
```

## rdsadmin.drop_database

Drops a database.

### Syntax

```
db2 "call rdsadmin.drop_database('`database_name`')"
```

### Parameters

The following parameter is required:

`database_name`

The name of the database to drop. The data type is
`varchar`.

### Usage notes

You can drop a database by calling `rdsadmin.drop_database` only if the
following conditions are met:

- You didn't specify the name of the database when you created your RDS for Db2
  DB instance by using either the Amazon RDS console or the AWS CLI. For more
  information, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").
- You created the database by calling the [rdsadmin.create_database](#db2-sp-create-database "#db2-sp-create-database") stored procedure.
- You restored the database from an offline or backed-up image by calling
  the [rdsadmin.restore_database](#db2-sp-restore-database "#db2-sp-restore-database") stored procedure.

Before calling `rdsadmin.drop_database`, you must connect to the
`rdsadmin` database. In the following example, replace
`master_username` and
`master_password` with your RDS for Db2 DB instance
information:

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

For information about checking the status of dropping a database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling `rdsadmin.drop_database`, see
[Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

The following example drops a database called `TESTDB`:

```
db2 "call rdsadmin.drop_database('TESTDB')"
```

## rdsadmin.update_db_param

Updates database parameters.

### Syntax

```
db2 "call rdsadmin.update_db_param(
    '`database_name`',
    '`parameter_to_modify`',
    '`changed_value`',
    '`restart_database`')"
```

### Parameters

The following parameters are required:

`database_name`

The name of the database to run the task for. The data type is
`varchar`.

`parameter_to_modify`

The name of the parameter to modify. The data type is
`varchar`. For more information, see [Amazon RDS for Db2 parameters](db2-supported-parameters.md "db2-supported-parameters.md").

`changed_value`

The value to change the parameter value to. The data type is
`varchar`.

The following parameter is optional:

`restart_database`

Specifies whether RDS restarts the database if a restart is necessary.
The data type is `varchar`. To modify `logprimary`
and `logfilsiz`, set this parameter to `'YES'`.

### Usage notes

For information about checking the status of updating database parameters, see
[rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling `rdsadmin.update_db_param`,
see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

**Example 1: Updating a parameter**

The following example updates the `archretrydelay` parameter to
`100` for a database called `TESTDB`:

```
db2 "call rdsadmin.update_db_param(
    'TESTDB',
    'archretrydelay',
    '100')"
```

**Example 2: Deferring validation of objects**

The following example defers the validation of created objects on a database
called `TESTDB` to avoid dependency checking:

```
db2 "call rdsadmin.update_db_param(
    'TESTDB',
    'auto_reval',
    'deferred_force')"
```

## rdsadmin.set_configuration

Configures specific settings for the database.

### Syntax

```
db2 "call rdsadmin.set_configuration(
    '`name`',
    '`value`')"
```

### Parameters

The following parameters are required:

`name`

The name of the configuration setting. The data type is
`varchar`.

`value`

The value for the configuration setting. The data type is
`varchar`.

### Usage notes

The following table shows the configuration settings that you can control with
`rdsadmin.set_configuration`.

| Name                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `RESTORE_DATABASE_NUM_BUFFERS`     | The number of buffers to create during a restore operation.<br>This value must be less than the total memory size of the DB<br>instance class. If this setting isn't configured, Db2 determines<br>the value to use during the restore operation. For more<br>information, see [RESTORE DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-restore-database "https://www.ibm.com/docs/en/db2/11.5?topic=commands-restore-database") in the IBM Db2<br>documentation.                                                                                                                                                                                                                                  |
| `RESTORE_DATABASE_PARALLELISM`     | The number of buffer manipulators to create during a restore<br>operation. This value must be less than double the number of<br>vCPUs for the DB instance. If this setting isn't configured, Db2<br>determines the value to use during the restore operation. For<br>more information, see [RESTORE DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-restore-database "https://www.ibm.com/docs/en/db2/11.5?topic=commands-restore-database") in the IBM Db2<br>documentation.                                                                                                                                                                                                                      |
| `RESTORE_DATABASE_NUM_MULTI_PATHS` | The number of paths (or I/O streams) to use during a restore<br>from Amazon S3 operation. To use this configuration setting, you must<br>have multiple backup files. This value can improve performance<br>when restoring databases with large volumes of data because it<br>restores multiple database backup files in parallel. We<br>recommend that you set this value to match the number of your<br>database backup files. For more information, see [BACKUP DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-backup-database "https://www.ibm.com/docs/en/db2/11.5?topic=commands-backup-database") in the IBM Db2<br>documentation.                                                          |
| `USE_STREAMING_RESTORE`            | Specifies whether to stream backup data directly during<br>restoration rather than first downloading the entire backup to<br>your RDS for Db2 DB instance and then extracting it. Setting<br>`USE_STREAMING_RESTORE` to `TRUE`<br>significantly reduces storage requirements and can improve<br>restore performance. This setting requires IBM Db2 engine<br>version 11.5.9.0.sb00063198.r1 or higher, and Amazon S3 connectivity<br>through your database's elastic network interface (ENI). For<br>more information, see [Remote storage](https://www.ibm.com/docs/en/db2/11.5.x?topic=databases-remote-storage "https://www.ibm.com/docs/en/db2/11.5.x?topic=databases-remote-storage") in the IBM Db2 documentation. |

### Examples

**Example 1: Specifying number of buffers to
create**

The following example sets the `RESTORE_DATABASE_NUM_BUFFERS`
configuration to `150`.

```
db2 "call rdsadmin.set_configuration(
    'RESTORE_DATABASE_NUM_BUFFERS',
    '150')"
```

**Example 2: Specifying number of buffer manipulators to
create**

The following example sets the `RESTORE_DATABASE_PARALLELISM`
configuration to `8`.

```
db2 "call rdsadmin.set_configuration(
    'RESTORE_DATABASE_PARALLELISM',
    '8')"
```

**Example 3: Specifying number of paths or I/O streams to use during restore**

The following example sets the `RESTORE_DATABASE_NUM_MULTI_PATHS`
configuration to `5`.

```
db2 "call rdsadmin.set_configuration(
    'RESTORE_DATABASE_NUM_MULTI_PATHS',
    '5')"
```

**Example 4: Setting restoration to stream backup
data**

The following example sets the `USE_STREAMING_RESTORE` configuration to
`TRUE`.

```
db2 "call rdsadmin.set_configuration(
    'USE_STREAMING_RESTORE',
    'TRUE')"
```

## rdsadmin.show_configuration

Returns the current settings that you can set by using the stored procedure
`rdsadmin.set_configuration`.

### Syntax

```
db2 "call rdsadmin.show_configuration(
    '`name`')"
```

### Parameters

The following parameter is optional:

`name`

The name of the configuration setting to return information about. The
data type is `varchar`.

The following configuration names are valid:

- `RESTORE_DATABASE_NUM_BUFFERS` – The number
  of buffers to create during a restore operation.
- `RESTORE_DATABASE_PARALLELISM` – The number
  of buffer manipulators to create during a restore
  operation.
- `RESTORE_DATABASE_NUM_MULTI_PATHS` – The
  number of paths (or I/O streams) to use during a restore from
  Amazon S3 operation.
- `USE_STREAMING_RESTORE` – Specifies whether
  to stream backup data directly during restoration rather than
  first downloading the entire backup data to your RDS for Db2 DB
  instance and then extracting it.

### Usage notes

If you don't specify the name of a configuration setting,
`rdsadmin.show_configuration` returns information for all
configuration settings that you can set by using the stored procedure
`rdsadmin.set_configuration`.

### Examples

The following example returns information about the current
`RESTORE_DATABASE_PARALLELISM` configuration.

```
db2 "call rdsadmin.show_configuration(
    'RESTORE_DATABASE_PARALLELISM')"
```

## rdsadmin.backup_database

Backs up a database from an RDS for Db2 DB instance to an Amazon S3 bucket.

### Syntax

```
db2 "call rdsadmin.backup_database(
    ?,
    '`database_name`',
    '`s3_bucket_name`',
    '`s3_prefix`',
    '`backup_type`',
    '`compression_option`',
    '`util_impact_priority`',
    '`num_files`',
    '`parallelism`',
    '`num_buffers`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameters are required:

`database_name`

The name of the target database on an RDS for Db2 DB instance to back up.
The data type is `varchar`.

The database must exist in the DB instance. You can't back up the
`rdsadmin` database.

`s3_bucket_name`

The name of the Amazon S3 bucket where you want your backup to reside. The
data type is `varchar`.

The S3 bucket must exist before calling
`rdsadmin.backup_database`, be in the same AWS Region
as the target database in the RDS for Db2 DB instance that you want to back
up, and be accessible through the IAM role attached to the DB
instance.

`s3_prefix`

The prefix of the path to Amazon S3 where RDS for Db2 uploads the backup
files. The data type is `varchar`.

The prefix is limited to 1024 characters. It must not include a
leading or trailing slash (/). Because of a limitation with IBM
streaming to Amazon S3, we recommend that the prefix includes
subdirectories.

For better file management, RDS for Db2 creates extra directories after
`s3_prefix`. RDS for Db2 uploads all backup
files to `s3_prefix/dbi_resource_id/db_name`.
If you set `num_files` higher than
`1`, the `db_name` directory
will contain more than one backup file.

The following is an example Amazon S3 location for backup files. In the
example, `backups/daily` is the value set for the
`s3_prefix` parameter.

```
backups/daily/db-5N7FXOY4GDP7RG2NSH2ZTAI2W4/SAMPLEDB
```

`backup_type`

The type of backup that determines if the database remains available
during backup. The data type is `varchar`.

Valid values:

- `OFFLINE` – The database is unavailable
  during backup. This type is faster, but it causes downtime.
- `ONLINE` – The database remains available
  during backup. By default, `ONLINE` is set to
  `INCLUDE LOGS`.

The following parameters are optional:

`compression_option`

The type of compression algorithm used that impacts backup time, CPU
usage, and storage costs. The data type is `varchar`. The
default is `NONE`.

Valid values:

- `NONE` – The largest file size, the least
  CPU usage, and cheapest storage costs.
- `STANDARD` – Standard Db2 compression. Uses
  `libdb2compr.so`.
- `ZLIB` – Enhanced Db2 compression. Uses
  `libdb2zcompr.so`, but is more CPU-intensive and
  most expensive storage cost.

`util_impact_priority`

The setting that controls the impact of the backup on the system
resources. The data type is `integer`. Valid values:
`1`–`100` (from low to high). The
default is `50`.

Lower values reduce the impact of the backup on the system resources,
but might increase the time it takes to back up the database. Higher
values might complete the backup of the database faster, but could
affect other operations. The actual impact depends on the overall system
utilization and the `util_impact_lim` setting. You can view
and modify the `util_impact_lim` setting in parameter groups.
For more information, see [Amazon RDS for Db2 parameters](db2-supported-parameters.md "db2-supported-parameters.md").

`num_files`

The number of parallel upload streams to Amazon S3. The data type is
`integer`. Valid values:
`1`–`256`.

We recommend that you only set this parameter after observing the
backup performance at the default that Amazon RDS automatically calculates.
Higher values could improve performance for large backups, especially
with high-bandwidth connections, but at a certain point, higher values
degrade performance. Also, make sure to take into account your available
system resources and network capacity.

`parallelism`

The number of tablespaces that the backup utility can read in
parallel. The data type is `integer`. Valid values:
`1`–`256`.

We recommend that you only set this parameter after observing the
backup performance at the default that the Db2 engine automatically
calculates as the optimal value. If you set this parameter, Amazon RDS
validates against the available processors and won't execute the backup
request if processing power is insufficient.

`num_buffers`

The number of buffers to use. The data type is `integer`.
Valid values: `1`–`268435456`.

We recommend that you only set this parameter after observing the
backup performance at the default that Amazon RDS automatically calculates
based on memory. If you set this parameter, Amazon RDS validates against the
available memory and won't execute the backup request if available
memory is insufficient. If you are backing up to multiple locations
(`num_files` is set to more than `1`), then a
higher number of buffers could improve performance. If you don't set
`compression_option` to `NONE`, then you can
improve performance by increasing `num_buffers` and
`parallelism`.

### Usage notes

This stored procedure creates asynchronous backup tasks that stream the backup of
your database directly to your Amazon S3 bucket by using the Amazon S3 integration. You can
make backups both from your local server or from an RDS for Db2 DB instance, stream
them to Amazon S3, and then restore them wherever you want. For information about
restoring a database to an RDS for Db2 DB instance, see [rdsadmin.restore_database](#db2-sp-restore-database "#db2-sp-restore-database").

Before calling the stored procedure, review the following considerations:

- You can only back up one database at a time.
- You can't perform a backup and restore together on a DB instance.
- Amazon S3 server-side encryption with AWS KMS (SSE-KMS) isn't supported. Even if
  the S3 bucket is set to SSE-KMS, the files uploaded to the S3 bucket won't
  use SSE-KMS encryption.
- To stream the backup files to Amazon S3, you must have already configured the
  integration. For more information, see [Integrating an Amazon RDS for Db2 DB instance with
  Amazon S3](db2-s3-integration.md "db2-s3-integration.md").
- For an RDS for Db2 DB instance to be able to interact with Amazon S3, you must
  have a VPC and an Amazon S3 gateway endpoint for private subnets to use. For more
  information, see [Step 1: Create a VPC gateway endpoint for
  Amazon S3](db2-troubleshooting.md#db2-creating-endpoint "db2-troubleshooting.md#db2-creating-endpoint") and [Step 2: Confirm that your VPC gateway
  endpoint for Amazon S3 exists](db2-troubleshooting.md#db2-confirming-endpoint "db2-troubleshooting.md#db2-confirming-endpoint").

Before calling `rdsadmin.backup_database`, you must connect to the
`rdsadmin` database. In the following example, replace
`master_username` and
`master_password` with your RDS for Db2 DB instance
information:

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

After you back up your database, be sure to terminate the connection.

```
terminate
```

For information about checking the status of backing up a database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling `rdsadmin.backup_database`,
see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

All the examples back up a database called `MYDB` to the Amazon S3 bucket
called `amzn-s3-demo-bucket` and set the
`s3_prefix` to `backups/daily`.

**Example #1: Specifying database offline and unavailable with
median utilization and a single upload stream**

In the following example, the database is offline, which is faster but means that
the database is unavailable during backup. The example performs no compression of
the files, has median impact on system resources, and uses a single upload stream to
Amazon S3.

```
db2 call "rdsadmin.backup_database(
    ?,
    'MYDB',
    'amzn-s3-demo-bucket',
    'backups/daily',
    'OFFLINE',
    'NONE',
    50,
    1)"
```

**Example #2: Specifying database online and available with
enhanced compression, median utilization, and few parallel upload
streams**

In the following example, the database in online and available during backup. The
example performs enhanced compression, which results in a small file size, but is
CPU-intensive. It has a slightly higher than median impact on system resources and
uses five upload streams to Amazon S3.

```
db2 call "rdsadmin.backup_database(
    ?,
    'MYDB',
    'amzn-s3-demo-bucket',
    'backups/daily',
    'ONLINE',
    'ZLIB',
    60,
    5)"
```

**Example #3: Specifying database offline and unavailable with
defaults and system calculations**

In the following example, the database is offline, which is faster but means that
the database is unavailable during backup. The example uses the default compression
of the files and impact on system resources. It also allows RDS for Db2 to calculate
the number of parallel upload streams to Amazon S3, tablespaces to read in parallel, and
buffers to use.

```
db2 "call rdsadmin.backup_database(
    ?,
    'MYDB',
    'amzn-s3-demo-bucket',
    'backups/daily',
    'OFFLINE')"
```

**Example #4: Specifying database offline and unavailable with
no compression, high utilization, and custom calculations**

In the following example, the database is offline, which is faster but means that
the database is unavailable during backup. The example performs no compression of
the files, has a high impact on system resources, and uses 20 upload streams to
Amazon S3. It sets the maximum number of tablespaces to read in parallel, which can cause
the backup request to fail if processing power is insufficient. It also sets the
maximum number of buffers to use, which can cause the backup request to fail if
memory is insufficient.

```
db2 "call rdsadmin.backup_database(
    ?,
    'MYDB',
    'amzn-s3-demo-bucket',
    'backups/daily',
    'OFFLINE',
    'NONE',
    90,
    20,
    256,
    268435456)"
```

## rdsadmin.restore_database

Restores a database from an Amazon S3 bucket to your RDS for Db2 DB instance.

### Syntax

```
db2 "call rdsadmin.restore_database(
    ?,
    '`database_name`',
    '`s3_bucket_name`',
    '`s3_prefix`',
    `restore_timestamp`,
    '`backup_type`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameters are required:

`database_name`

The name of the target database to restore in RDS for Db2. The data type
is `varchar`.

For example, if the source database name was `TESTDB` and
you set `database_name` to `NEWDB`,
then Amazon RDS restores `NEWDB` as the source database.

`s3_bucket_name`

The name of the Amazon S3 bucket where your backup resides. The data type
is `varchar`.

`s3_prefix`

The prefix to use for file matching during download. The data type is
`varchar`.

If this parameter is empty, then all files in the Amazon S3 bucket will be
processed. The following is an example prefix:

```
backupfolder/SAMPLE.0.rdsdb.DBPART000.20230615010101
```

`restore_timestamp`

The timestamp of the database backup image. The data type is
`varchar`.

The timestamp is included in the backup file name. For example,
`20230615010101` is the timestamp for the file name
`SAMPLE.0.rdsdb.DBPART000.20230615010101.001`.

`backup_type`

The type of backup. The data type is `varchar`. Valid
values: `OFFLINE`, `ONLINE`.

Use `ONLINE` for near-zero downtime migrations. For more
information, see [Migrating from Linux to Linux with near-zero downtime for Amazon RDS for Db2](db2-near-zero-downtime-migration.md "db2-near-zero-downtime-migration.md").

### Usage notes

You can use this stored procedure to migrate a Db2 database to an RDS for Db2 DB
instance. For more information, see [Using AWS services to migrate data from Db2 to Amazon RDS for Db2](db2-migration-approaches.md "db2-migration-approaches.md"). You can also use this stored
procedure to create multiple copies of the same database with different database
names that use the same restore image.

Before calling the stored procedure, review the following considerations:

- Before restoring a database, you must provision storage space for your
  RDS for Db2 DB instance that is greater than the original Db2 database on disk.
  If you enabled `USE_STREAMING_RESTORE`, then when you restore
  your backup, Amazon RDS streams the backup files directly from your S3 bucket to
  your RDS for Db2 DB instance. If you don't enable
  `USE_STREAMING_RESTORE`, you must provision storage space for
  your RDS for Db2 DB instance that is equal to or greater than the sum of the
  backup size plus the original Db2 database on disk. For more information,
  see [Insufficient disk space](db2-troubleshooting.md#restore-database-sp-insufficient-disk-space "db2-troubleshooting.md#restore-database-sp-insufficient-disk-space").
- When you restore the backup, Amazon RDS extracts the backup file on your
  RDS for Db2 DB instance. Each backup file must be 5 TB or smaller. If a backup
  file exceeds 5 TB, then you must split the backup file into smaller files.
- To restore all files using the `rdsadmin.restore_database`
  stored procedure, don't include the file number suffix after the timestamp
  in the file names. For example, the `s3_prefix`
  `backupfolder/SAMPLE.0.rdsdb.DBPART000.20230615010101` restores
  the following files:

```
SAMPLE.0.rdsdb.DBPART000.20230615010101.001
SAMPLE.0.rdsdb.DBPART000.20230615010101.002
SAMPLE.0.rdsdb.DBPART000.20230615010101.003
SAMPLE.0.rdsdb.DBPART000.20230615010101.004
SAMPLE.0.rdsdb.DBPART000.20230615010101.005
```

- RDS for Db2 doesn't support non-automatic storage. For more information, see
  [Tablespaces not restored](db2-troubleshooting.md#restore-database-sp-tablespaces-not-restored "db2-troubleshooting.md#restore-database-sp-tablespaces-not-restored").
- RDS for Db2 doesn't support non-fenced routines. For more information, see
  [Non-fenced routines not allowed](db2-troubleshooting.md#restore-database-sp-non-fenced-routines "db2-troubleshooting.md#restore-database-sp-non-fenced-routines").
- To improve the performance of database restore operations, you can
  configure the number of buffers, buffer manipulators, and the number of
  multiple backup paths for RDS to use. To optimize storage usage and to
  potentially improve performance, you can also directly stream a backup from
  Amazon S3. To check the current configuration, use [rdsadmin.show_configuration](#db2-sp-show-configuration "#db2-sp-show-configuration"). To change the configuration, use
  [rdsadmin.set_configuration](#db2-sp-set-configuration "#db2-sp-set-configuration").

To bring the database online and apply additional transaction logs after restoring
the database, see [rdsadmin.rollforward_database](#db2-sp-rollforward-database "#db2-sp-rollforward-database").

For information about checking the status of restoring your database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling `rdsadmin.restore_database`,
see [Stored
procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

The following example restores an offline backup with a single file or multiple
files that have the `s3_prefix`
`backupfolder/SAMPLE.0.rdsdb.DBPART000.20230615010101`:

```
db2 "call rdsadmin.restore_database(
    ?,
    'SAMPLE',
    'amzn-s3-demo-bucket',
    'backupfolder/SAMPLE.0.rdsdb.DBPART000.20230615010101',
    20230615010101,
    'OFFLINE')"
```

## rdsadmin.rollforward_database

Brings the database online and applies additional transaction logs after restoring a
database by calling [rdsadmin.restore_database](#db2-sp-restore-database "#db2-sp-restore-database").

### Syntax

```
db2 "call rdsadmin.rollforward_database(
    ?,
    '`database_name`',
    '`s3_bucket_name`',
    `s3_prefix`,
    '`rollforward_to_option`',
    '`complete_rollforward`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameters are required:

`database_name`

The name of the database to perform the operation on. The data type is
`varchar`.

`s3_bucket_name`

The name of the Amazon S3 bucket where your backup resides. The data type
is `varchar`.

`s3_prefix`

The prefix to use for file matching during download. The data type is
`varchar`.

If this parameter is empty, then all files in the S3 bucket will be
downloaded. The following example is an example prefix:

```
backupfolder/SAMPLE.0.rdsdb.DBPART000.20230615010101
```

The following input parameters are optional:

`rollforward_to_option`

The point to which you want to roll forward. The data type is
`varchar`. Valid values: `END_OF_LOGS`,
`END_OF_BACKUP` with the timestamp in the format
`YYYY-MM-DD-HH.MM.SS`. The default is
`END_OF_LOGS`.

`complete_rollforward`

Specifies whether to complete the roll-forward process. The data type
is `varchar`. The default is `TRUE`.

If `TRUE`, then after completion, the database is online
and accessible. If `FALSE`, then the database remains in a
`ROLL-FORWARD PENDING` state.

### Usage notes

You can use `rds.rollforward_database` for an online backup with
include logs that are produced on-premises in many different scenarios.

**Scenario 1: Restoring the database, rolling forward the
included logs, and bringing the database online**

After `rdsadmin.restore_database()` completes, use the syntax in [Example 1](#db2-sp-rollforward-database-examples "#db2-sp-rollforward-database-examples") to bring the
database with transaction logs online.

**Scenario 2: Bringing the database online but not rolling
forward the included logs.**

After `rdsadmin.restore_database()` completes, use the syntax in [Example 2](#db2-sp-rollforward-database-examples "#db2-sp-rollforward-database-examples") to bring the
database without the transaction logs online.

**Scenario 3: Rolling forward the included logs in the backup,
and applying additional transaction logs as they are produced
on-premises**

After `rdsadmin.restore_database()` completes, use the syntax in [Example 3 or Example 4](#db2-sp-rollforward-database-examples "#db2-sp-rollforward-database-examples") to
rollforward logs without bringing the database online.

If you set `complete_rollforward` to `FALSE`, then your
database is in a `ROLL-FORWARD PENDING` state and offline. To bring the
database online, you must call [rdsadmin.complete_rollforward](#db2-sp-complete-rollforward "#db2-sp-complete-rollforward").

For information about checking the status of rolling forward the database, see
[rdsadmin.rollforward_status](#db2-sp-rollforward-status "#db2-sp-rollforward-status").

### Examples

**Example 1: Bringing database with transaction logs
online**

The following example rolls forward to an online backup of the database with
transaction logs and then brings the database online:

```
db2 "call rdsadmin.rollforward_database(
    ?,
    null,
    null,
    'END_OF_LOGS',
    'TRUE')"
```

**Example 2: Bringing database without transaction logs online**

The following example rolls forward to an online backup of the database without
transaction logs, and then brings the database online:

```
db2 "call rdsadmin.rollforward_database(
    ?,
    'TESTDB',
    'amzn-s3-demo-bucket',
    'logsfolder/,
    'END_OF_BACKUP',
    'TRUE')"
```

**Example 3: Not bringing database with transaction logs
online**

The following example rolls forward to an online backup of the database with
transaction logs, and then doesn't bring the database online:

```
db2 "call rdsadmin.rollforward_database(
    ?,
    'TESTDB',
    null,
    'onlinebackup/TESTDB',
    'END_OF_LOGS',
    'FALSE')"
```

**Example 4: Not bringing database with additional transaction
logs online**

The following example rolls forward to an online backup of the database with
additional transaction logs, and then doesn't bring the database online:

```
db2 "call rdsadmin.rollforward_database(
    ?,
    'TESTDB',
    'amzn-s3-demo-bucket',
    'logsfolder/S0000155.LOG',
    'END_OF_LOGS',
    'FALSE')"
```

## rdsadmin.rollforward_status

Returns the output of `ROLLFORWARD DATABASE
 `database_name` QUERY STATUS`.

### Syntax

```
db2 "call rdsadmin.rollforward_status(
    ?,
    '`database_name`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`database_name`

The name of the database to perform the operation on. The data type is
`varchar`.

### Usage notes

After you call [rdsadmin.rollforward_database](#db2-sp-rollforward-database "#db2-sp-rollforward-database"), you can call
`rdsadmin.rollforward_status` to check on the status of the
rollforward in the database.

For information about checking the status of this stored procedure, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

## rdsadmin.complete_rollforward

Brings database online from a `ROLL-FORWARD PENDING` state.

### Syntax

```
db2 "call rdsadmin.complete_rollforward(
    ?,
    '`database_name`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`database_name`

The name of the database that you want to bring online. The data type
is `varchar`.

### Usage notes

If you called [rdsadmin.rollforward_database](#db2-sp-rollforward-database "#db2-sp-rollforward-database") with
`complete_rollforward` set to `FALSE`, then your database
is in a `ROLL-FORWARD PENDING` state and offline. To complete the
roll-forward process and bring the database online, call
`rdsadmin.complete_rollforward`.

For information about checking the status of completing the rollforward process,
see [rdsadmin.rollforward_status](#db2-sp-rollforward-status "#db2-sp-rollforward-status").

### Examples

The following example brings the TESTDB database online:

```
db2 "call rdsadmin.complete_rollforward(
    ?,
    'TESTDB')"
```

## rdsadmin.db2pd_command

Collects information about an RDS for Db2 database.

### Syntax

```
db2 "call rdsadmin.db2pd_command('`db2pd_cmd`')"
```

### Parameters

The following input parameter is required:

`db2pd_cmd`

The name of the `db2pd` command that you want to run. The
data type is `varchar`.

The parameter must start with a hyphen. For a list of parameters, see
[db2pd - Monitor and troubleshoot Db2 database command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2pd-monitor-troubleshoot-db2-engine-activities "https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2pd-monitor-troubleshoot-db2-engine-activities") in
the IBM Db2 documentation.

The following options aren't supported:

- `-addnode`
- `-alldatabases`
- `-alldbp`
- `-alldbs`
- `-allmembers`
- `-alm_in_memory`
- `-cfinfo`
- `-cfpool`
- `-command`
- `-dbpartitionnum`
- `-debug`
- `-dump`
- `-everything`
- `-file | -o`
- `-ha`
- `-interactive`
- `-member`
- `-pages`

###### Note

`-pages summary` is supported.

- `-pdcollection`
- `-repeat`
- `-stack`
- `-totalmem`

The `file` suboption isn't supported, for example,
`db2pd -db testdb -tcbstats file=tcbstat.out`.

The use of the `stacks` option isn't supported, for
example, `db2pd -edus interval=5 top=10 stacks`.

### Usage notes

This stored procedure gathers information that can help with monitoring and
troubleshooting RDS for Db2 databases.

The stored procedure uses the IBM
`db2pd` utility to run various commands. The `db2pd` utility
requires `SYSADM` authorization, which the RDS for Db2 master user doesn't
have. However, with the Amazon RDS stored procedure, the master user is able to use the
utility to run various commands. For more information about the utility, see [db2pd - Monitor and troubleshoot Db2 database command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2pd-monitor-troubleshoot-db2-engine-activities "https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2pd-monitor-troubleshoot-db2-engine-activities") in the IBM Db2
documentation.

The output is restricted to a maximum of 2 GB.

For information about checking the status of collecting information about the
database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

**Example 1: Returning uptime of DB instance**

The following example returns the uptime of an RDS for Db2 DB instance:

```
db2 "call rdsadmin.db2pd_command('-')"
```

**Example 2: Returning uptime of database**

The following example returns the uptime of a database called
`TESTDB`:

```
db2 "call rdsadmin.db2pd_command('-db TESTDB -')"
```

**Example 3: Returning memory usage of DB
instance**

The following example returns the memory usage of an RDS for Db2 DB instance:

```
db2 "call rdsadmin.db2pd_command('-dbptnmem')"
```

**Example 4: Returning memory sets of DB instance and
database**

The following example returns the memory sets of an RDS for Db2 DB instance and a
database called `TESTDB`:

```
db2 "call rdsadmin.db2pd_command('-inst -db TESTDB -memsets')"
```

## rdsadmin.force_application

Forces applications off of an RDS for Db2 database.

### Syntax

```
db2 "call rdsadmin.force_application(
    ?,
    '`applications`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`applications`

The applications that you want to force off of an RDS for Db2 database.
The data type is `varchar`. Valid values: `ALL` or
`application_handle`.

Separate the names of multiple applications with commas. Example:
'`application_handle_1`,
`application_handle_2`'.

### Usage notes

This stored procedure forces all applications off of a database so you can perform
maintenance.

The stored procedure uses the IBM
`FORCE APPLICATION` command. The `FORCE APPLICATION` command
requires `SYSADM`, `SYSMAINT`, or `SYSCTRL`
authorization, which the RDS for Db2 master user doesn't have. However, with the Amazon RDS
stored procedure, the master user is able to use the command. For more information,
see [FORCE APPLICATION command](https://www.ibm.com/docs/en/db2/11.1?topic=commands-force-application "https://www.ibm.com/docs/en/db2/11.1?topic=commands-force-application") in the IBM Db2 documentation.

For information about checking the status of forcing applications off of a
database, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

**Example 1: Specifying all applications**

The following example forces all applications off of an RDS for Db2 database:

```
db2 "call rdsadmin.force_application(
    ?,
    'ALL')"
```

**Example 2: Specifying multiple
applications**

The following example forces application handles `9991`,
`8891`, and `1192` off of an RDS for Db2 database:

```
db2 "call rdsadmin.force_application(
    ?,
    '9991, 8891, 1192')"
```

## rdsadmin.set_archive_log_retention

Configures the amount of time (in hours) to retain archive log files for the specified
RDS for Db2 database.

### Syntax

```
db2 "call rdsadmin.set_archive_log_retention(
    ?,
    '`database_name`',
    '`archive_log_retention_hours`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameters are required:

`database_name`

The name of the database to configure archive log retention for. The
data type is `varchar`.

`archive_log_retention_hours`

The number of hours to retain the archive log files. The data type is
`smallint`. The default is `0`, and the
maximum is `168` (7 days).

If the value is `0`, Amazon RDS doesn't retain the archive log
files.

### Usage notes

By default, RDS for Db2 retains logs for 5 minutes. We recommend that if you use
replication tools such as AWS DMS for change data capture (CDC) or IBM Q
Replication, you set log retention in those tools for longer than 5
minutes.

You can view the current archive log retention setting by calling [rdsadmin.show_archive_log_retention](#db2-sp-show-archive-log-retention "#db2-sp-show-archive-log-retention").

You can't configure the archive log retention setting on the `rdsadmin`
database.

### Examples

**Example 1: Setting retention time**

The following example sets the archive log retention time for a database called
`TESTDB` to 24 hours.

```
db2 "call rdsadmin.set_archive_log_retention(
    ?,
    'TESTDB',
    '24')"
```

**Example 2: Disabling retention time**

The following example disables archive log retention for a database called
`TESTDB`.

```
db2 "call rdsadmin.set_archive_log_retention(
    ?,
    'TESTDB',
    '0')"
```

## rdsadmin.show_archive_log_retention

Returns the current archive log retention setting for the specified database.

### Syntax

```
db2 "call rdsadmin.show_archive_log_retention(
    ?,
    '`database_name`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`database_name`

The name of the database to show the archive log retention setting
for. The data type is `varchar`.

### Examples

The following example shows the archive log retention setting for a database
called `TESTDB`.

```
db2 "call rdsadmin.show_archive_log_retention(?,'TESTDB')"
```

## rdsadmin.list_archive_log_information

Returns details about the archive log files, such as the size, the creation date and
time, and the name of individual log files for the specified database. It also returns
the total storage amount used by the log files in the database.

### Syntax

```
db2 "call rdsadmin.list_archive_log_information(
    ?,
    '`database_name`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameter is required:

`database_name`

The name of the database to list archive log information for. The data
type is `varchar`.

### Examples

The following example returns archive log information for a database called
`TESTDB`.

```
db2 "call rdsadmin.list_archive_log_information(
    ?,
    'TESTDB')"
```

## rdsadmin.fgac_command

Runs fine-grained access control (FGAC) commands.

### Syntax

```
db2 "call rdsadmin.fgac_command(
    ?,
    '`database_name`',
    '`fgac_cmd`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. This parameter only
accepts `?`.

The following input parameters are required:

`database_name`

The name of the database that you want to run FGAC commands on. The
data type is `varchar`.

`fgac_cmd`

The fine-grained access control command that you want to run. The data
type is `varchar`.

The following commands are valid:

- `ALTER MASK` – Alters an existing column
  mask in row and column access control (RCAC).
- `ALTER PERMISSION` – Alters properties of an
  existing row permission in RCAC.
- `ALTER SECURITY POLICY` – Alters an existing
  security policy for RCAC.
- `ALTER SECURITY LABEL` – Alters properties
  of an existing security label in label-based access control
  (LBAC).
- `ALTER TABLE` – Alters table structure,
  including adding RCAC or LBAC controls.
- `CREATE MASK` – Creates a new column mask
  for RCAC.
- `CREATE PERMISSION` – Creates a new row
  permission for RCAC.
- `CREATE SECURITY LABEL` – Creates a new
  security label for LBAC.
- `CREATE SECURITY POLICY` – Creates a new
  security policy for RCAC.
- `DROP MASK` – Drops an existing column
  mask.
- `DROP PERMISSION` – Drops an existing row
  permission.
- `DROP SECURITY LABEL` – Drops a security
  label from LBAC.
- `DROP SECURITY POLICY` – Drops an existing
  RCAC security policy.
- `GRANT EXEMPTION ON RULE` – Allows a user to
  bypass specific LBAC rules.
- `GRANT SECURITY LABEL` – Assigns an LBAC
  security label to a user.
- `REVOKE EXEMPTION ON RULE` – Removes a
  user's exemption from LBAC rules.
- `REVOKE SECURITY LABEL` – Removes an LBAC
  security label from a user.

### Usage notes

This stored procedure controls access at the row or column level to table data in
your database on an RDS for Db2 DB instance. RDS for Db2 supports two types of FGAC on the
database:

- Label-based access control (LBAC)
- Row and column access control (RCAC)

Before calling the stored procedure, review the following considerations:

- To escape a single quote ('), use an additional single quote. The following
  examples show how to escape `'apple'`, `'banana'`, and
  `'fruit'`.

```
db2 "call rdsadmin.fgac_command(
    ?,
    'testdb',
    'CREATE SECURITY LABEL COMPONENT FRUITSET SET{''apple'',''banana''}')"
```

```
db2 "call rdsadmin.fgac_command(
    ?,
    'testdb',
    'CREATE SECURITY LABEL COMPONENT FRUITTREE TREE(''fruit'' ROOT, ''apple'' UNDER ''fruit'', ''banana'' UNDER ''fruit'')')"
```

- To escape brackets ([ ]), use a backslash (\). The following example shows
  how to escape `[''apple'',''banana'']`.

```
db2 "call rdsadmin.fgac_command(
    ?, '
    testdb',
    'CREATE SECURITY LABEL COMPONENT FRUITARRAY ARRAY\[''apple'',''banana''\]')"
```

### Examples

The following examples all run FGAC commands on a database called
`testdb`.

**Example 1: Creating a new security label called
`FRUITSET`**

```
db2 "call rdsadmin.fgac_command(
    ?,
    'testdb',
    'CREATE SECURITY LABEL COMPONENT FRUITSET SET{''apple'',''banana''}')"
```

**Example 2: Creating a new mask for the `EMP_ID`
column that is enabled when `EMP_ID` is set to less than
three**

```
db2 "call rdsadmin.fgac_command(
    ?,
    'testdb',
    'CREATE MASK id_MASK ON EMPLOYEE FOR COLUMN EMP_ID RETURN CASE WHEN (EMP_ID < 3) THEN EMP_ID ELSE NULL END ENABLE')"
```

**Example 3: Creating a new mask for the
`DEPARTMENT` column that is enabled when
`SESSION_USER` is set to `security_user`**

```
db2 "call rdsadmin.fgac_command(
    ?,
    'testdb',
    'CREATE MASK DEPARTMENT_MASK ON EMPLOYEE FOR COLUMN DEPARTMENT RETURN CASE  WHEN SESSION_USER = ''security_user'' THEN DEPARTMENT ELSE NULL END ENABLE')"
```

**Example 4: Creating a new security label called
`treelabel`**

```
db2 "call rdsadmin.fgac_command(
    ?,
    'testdb',
    'CREATE SECURITY LABEL COMPONENT treelabel  TREE(''COMPANY'' ROOT, ''HR'' UNDER ''COMPANY'', ''FINANCE'' UNDER ''COMPANY'', ''IT'' UNDER ''COMPANY'')')"
```
