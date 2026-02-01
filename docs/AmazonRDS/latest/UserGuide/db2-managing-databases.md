# Common tasks for databases

You can create, drop, or restore databases on your RDS for Db2 DB instance. Creating,
dropping, or restoring databases requires higher-level `SYSADM` authority, which
isn't available to the master user. Instead, use Amazon RDS stored procedures.

You can also perform common management tasks such as monitoring, maintenance, and the
collection of information about your databases.

###### Topics

- [Creating a database](#db2-creating-database "#db2-creating-database")
- [Configuring settings for a database](#db2-configuring-database "#db2-configuring-database")
- [Modifying database parameters](#db2-modifying-db-parameters "#db2-modifying-db-parameters")
- [Configuring log retention](#db2-configuring-log-retention "#db2-configuring-log-retention")
- [Listing log information](#db2-listing-log-information "#db2-listing-log-information")
- [Using fine-grained access
  control (FGAC)](#db2-using-fine-grained-access-control "#db2-using-fine-grained-access-control")
- [Deactivating a database](#db2-deactivating-database "#db2-deactivating-database")
- [Activating a database](#db2-activating-database "#db2-activating-database")
- [Reactivating a database](#db2-reactivating-database "#db2-reactivating-database")
- [Dropping a database](#db2-dropping-database "#db2-dropping-database")
- [Backing up a database](#db2-backing-up-database "#db2-backing-up-database")
- [Copying archive logs to Amazon S3](#db2-copying-archive-logs-to-s3 "#db2-copying-archive-logs-to-s3")
- [Restoring a database](#db2-restoring-database "#db2-restoring-database")
- [Listing databases](#db2-listing-databases "#db2-listing-databases")
- [Collecting information about databases](#db2-collecting-info-db "#db2-collecting-info-db")
- [Forcing applications off of
  databases](#db2-forcing-application-off-db "#db2-forcing-application-off-db")
- [Generating performance
  reports](#db2-generating-performance-reports "#db2-generating-performance-reports")

## Creating a database

To create a database on your RDS for Db2 DB instance, call the
`rdsadmin.create_database` stored procedure. For more information, see
[CREATE DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-create-database "https://www.ibm.com/docs/en/db2/11.5?topic=commands-create-database") in the IBM Db2
documentation.

###### Note

If you plan on modifying the `db2_compatibility_vector` parameter,
modify the parameter before creating a database. For more information, see [Setting the
db2_compatibility_vector parameter](db2-known-issues-limitations.md#db2-known-issues-limitations-db2-compatibility-vector "db2-known-issues-limitations.md#db2-known-issues-limitations-db2-compatibility-vector").

###### To create a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Create a database by calling `rdsadmin.create_database`. For more
   information, see [rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database").

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

3. (Optional) Create additional databases by calling
   `rdsadmin.create_database` for each database you want to create.
   Each Db2 DB instance can contain up to 50 databases. For more information, see
   [rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database").

```
db2 "call rdsadmin.create_database('`database_name`')"
```

4. (Optional) Confirm that your database was created by using one of the
   following methods:
   - Call `rdsadmin.list_databases`. For more information, see
     [rdsadmin.list_databases](db2-user-defined-functions.md#db2-udf-list-databases "db2-user-defined-functions.md#db2-udf-list-databases").
   - Run the following SQL command:

   ```
   db2 "select varchar(r.task_type,25) as task_type, r.database_name,
       varchar(r.lifecycle,15) as lifecycle, r.created_at, r.database_name,
       varchar(bson_to_json(task_input_params),256) as input_params,
       varchar(r.task_output,1024) as task_output
       from table(rdsadmin.get_task_status(null,null,'create_database'))
       as r order by created_at desc"
   ```

## Configuring settings for a database

To configure the settings for a database on your RDS for Db2 DB instance, call the
`rdsadmin.set_configuration` stored procedure. For example, you could
configure the number of buffers or buffer manipulators to create during a restore
operation.

###### To configure settings for a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. (Optional) Check your current configuration settings by calling
   `rdsadmin.show_configuration`. For more information, see [rdsadmin.show_configuration](db2-sp-managing-databases.md#db2-sp-show-configuration "db2-sp-managing-databases.md#db2-sp-show-configuration").

```
db2 "call rdsadmin.show_configuration('`name`')"
```

3. Configure the settings for the database by calling
   `rdsadmin.set_configuration`. For more information, see [rdsadmin.set_configuration](db2-sp-managing-databases.md#db2-sp-set-configuration "db2-sp-managing-databases.md#db2-sp-set-configuration").

```
db2 "call rdsadmin.set_configuration(
    '`name`',
    '`value`')"
```

## Modifying database parameters

Amazon RDS for Db2 uses three types of parameters: database manager configuration
parameters, registry variables, and database configuration parameters. You can update
the first two types through parameter groups and the last type through the [rdsadmin.update_db_param](db2-sp-managing-databases.md#db2-sp-update-db-param "db2-sp-managing-databases.md#db2-sp-update-db-param") stored
procedure.

###### Note

You can only modify the values of existing parameters. You can't add new
parameters that RDS for Db2 doesn't support.

For more information these parameters and how to modify their values, see [Amazon RDS for Db2 parameters](db2-supported-parameters.md "db2-supported-parameters.md").

## Configuring log retention

To configure how long Amazon RDS retains log files for your RDS for Db2 database, call the
`rdsadmin.set_archive_log_retention` stored procedure.

###### To configure log retention for a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. (Optional) Check your current configuration for log retention by calling
   `rdsadmin.show_archive_log_retention`. For more information, see
   [rdsadmin.show_archive_log_retention](db2-sp-managing-databases.md#db2-sp-show-archive-log-retention "db2-sp-managing-databases.md#db2-sp-show-archive-log-retention").

```
db2 "call rdsadmin.show_archive_log_retention(
    ?,
    '`database_name`')"
```

3. Configure log retention for the database by calling
   `rdsadmin.set_archive_log_retention`. For more information, see
   [rdsadmin.set_archive_log_retention](db2-sp-managing-databases.md#db2-sp-set-archive-log-retention "db2-sp-managing-databases.md#db2-sp-set-archive-log-retention").

```
db2 "call rdsadmin.set_archive_log_retention(
    ?,
    '`database_name`',
    '`archive_log_retention_hours`')"
```

## Listing log information

To list details about archive log files, including such details as total storage size
used, call the `rdsadmin.list_archive_log_information` stored
procedure.

###### To list log information for a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Return a list of log file information by calling
   `rdsadmin.list_archive_log_information`. For more information,
   see [rdsadmin.list_archive_log_information](db2-sp-managing-databases.md#db2-sp-list-archive-log-information "db2-sp-managing-databases.md#db2-sp-list-archive-log-information").

```
db2 "call rdsadmin.list_archive_log_information(
    ?,
    '`database_name`')"
```

## Using fine-grained access

control (FGAC)

To use fine-grained access control commands to control access to table data in a
database on an RDS for Db2 DB instance, call the `rdsadmin.fgac_command` stored
procedure. You might want to use FGAC to limit access to data based on user roles or
data attributes. For example, you could limit access to patient health care data based
on the type of data or to certain medical care providers.

###### To use fine-grained access control to control access to table data in a

database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Run various fine-grained access control commands by calling
   `rdsadmin.fgac_command`. For more information, see [rdsadmin.fgac_command](db2-sp-managing-databases.md#db2-sp-fgac-command "db2-sp-managing-databases.md#db2-sp-fgac-command").

```
db2 "call rdsadmin.fgac_command(
    ?,
    '`database_name`',
    '`fgac_command`')"
```

## Deactivating a database

To deactivate a database on your RDS for Db2 DB instance, call the
`rdsadmin.deactivate_database` stored procedure.

By default, Amazon RDS activates a database when you create a database on your RDS for Db2 DB
instance. You can deactivate infrequently used databases to conserve memory
resources.

###### To deactivate a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Deactivate a database by calling `rdsadmin.deactivate_database`.
   For more information, see [rdsadmin.deactivate_database](db2-sp-managing-databases.md#db2-sp-deactivate-database "db2-sp-managing-databases.md#db2-sp-deactivate-database").

```
db2 "call rdsadmin.deactivate_database(
    ?,
    '`database_name`')"
```

## Activating a database

To activate a database on a standalone RDS for Db2 DB instance, call the
`rdsadmin.activate_database` stored procedure.

By default, Amazon RDS activates a database when you create a database on your RDS for Db2 DB
instance. You can deactivate infrequently used databases to conserve memory resources,
and then later activate a deactivated database.

###### To activate a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Activate a database by calling `rdsadmin.activate_database`. For
   more information, see [rdsadmin.activate_database](db2-sp-managing-databases.md#db2-sp-activate-database "db2-sp-managing-databases.md#db2-sp-activate-database").

```
db2 "call rdsadmin.activate_database(
    ?,
    '`database_name`')"
```

## Reactivating a database

To reactivate a database on a replica source RDS for Db2 DB instance, call the
`rdsadmin.reactivate_database` stored procedure. After you make changes
to database configurations, you might need to reactivate a database on an RDS for Db2 DB
instance. To determine if you need to reactivate a database, connect to the database and
run `db2 get db cfg show detail`.

You can also call this stored procedure to reactivate a database on a standalone
RDS for Db2 DB instance after you make changes to database configurations. Or, you could
reactivate a database on a standalone RDS for Db2 DB instance by first calling the
`rdsadmin.deactivate_database` stored procedure and then the
`rdsadmin.activate_database` stored procedure. For more information, see
[Deactivating a database](#db2-deactivating-database "#db2-deactivating-database") and [Activating a database](#db2-activating-database "#db2-activating-database").

###### To reactivate a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Reactivate a database by calling `rdsadmin.reactivate_database`.
   For more information, see [rdsadmin.reactivate_database](db2-sp-managing-databases.md#db2-sp-reactivate-database "db2-sp-managing-databases.md#db2-sp-reactivate-database").

```
db2 "call rdsadmin.reactivate_database(
    ?,
    '`database_name`')"
```

## Dropping a database

To drop a database from your RDS for Db2 DB instance, call the
`rdsadmin.drop_database` stored procedure. For more information, see
[Dropping
databases](https://www.ibm.com/docs/en/db2/11.5?topic=databases-dropping "https://www.ibm.com/docs/en/db2/11.5?topic=databases-dropping") in the IBM Db2 documentation.

###### Note

You can drop a database by calling the stored procedure only if certain conditions
are met. For more information, see [Usage notes](db2-sp-managing-databases.md#db2-sp-drop-database-usage-notes "db2-sp-managing-databases.md#db2-sp-drop-database-usage-notes") for `rdsadmin.drop_database`.

###### To drop a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Drop a database by calling `rdsadmin.drop_database`. For more
   information, see [rdsadmin.drop_database](db2-sp-managing-databases.md#db2-sp-drop-database "db2-sp-managing-databases.md#db2-sp-drop-database").

```
db2 "call rdsadmin.drop_database('`database_name`')"
```

## Backing up a database

To back up a database in your RDS for Db2 DB instance to Amazon S3, call the
`rdsadmin.backup_database` stored procedure. For more information, see
[BACKUP DATABASE command](https://www.ibm.com/docs/en/db2/11.5.x?topic=commands-backup-database "https://www.ibm.com/docs/en/db2/11.5.x?topic=commands-backup-database") in the IBM Db2 documentation.

###### Note

This stored procedure uses the integration with Amazon S3. Make sure that you have
configured the integration before proceeding. For more information, see [Integrating an Amazon RDS for Db2 DB instance with
Amazon S3](db2-s3-integration.md "db2-s3-integration.md").

###### To back up a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Create a VPC gateway endpoint for S3. If you already have a VPC gateway
   endpoint for S3, skip to Step 4.

For an RDS for Db2 DB instance to be able to interact with Amazon S3, you must have a
VPC and an Amazon S3 gateway endpoint for private subnets to use. For more
information, see [Step 1: Create a VPC gateway endpoint for
Amazon S3](db2-troubleshooting.md#db2-creating-endpoint "db2-troubleshooting.md#db2-creating-endpoint"). 3. Confirm the VPC gateway endpoint for S3. For more information, see [Step 2: Confirm that your VPC gateway
endpoint for Amazon S3 exists](db2-troubleshooting.md#db2-confirming-endpoint "db2-troubleshooting.md#db2-confirming-endpoint"). 4. Back up a database by calling `rdsadmin.backup_database`. For more
information, see [rdsadmin.backup_database](db2-sp-managing-databases.md#db2-sp-backup-database "db2-sp-managing-databases.md#db2-sp-backup-database").

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

5. Terminate your connection.

```
terminate
```

6. (Optional) Confirm that the backup files were uploaded to your Amazon S3 bucket
   under `s3_prefix/dbi_resource_id/db_name`. If the files
   don't appear at `s3_prefix/dbi_resource_id/db_name`,
   check the status of backing up your database to identify any issues. For more
   information, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status"). If you can't resolve any
   identified issues, contact [AWS
   Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
7. (Optional) After the backup to Amazon S3 completes, you can restore the backup to
   an RDS for Db2 DB instance or to another location such as a local server. For
   information about restoring to an RDS for Db2 DB instance, see [Restoring a database](#db2-restoring-database "#db2-restoring-database").

## Copying archive logs to Amazon S3

Db2 archive logs can now be copied from your RDS for Db2 DB instance to Amazon S3. The archive logs
combined with native backup created using `rdsadmin.backup_database` can be
used to restore and rollforward database to point in time on another RDS for Db2 instance or EC2 database.

Before configuring this feature, use the stored procedure `rdsadmin.backup_database` to set up RDS for Db2 database.

This feature operates at the RDS for Db2 DB instance level, though archive log copying can be enabled
or disabled per database.

###### To configure archive log copying to Amazon S3

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB Instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Setup archive log backup to S3 by calling [rdsadmin.set_configuration](db2-sp-managing-databases.md#db2-sp-set-configuration "db2-sp-managing-databases.md#db2-sp-set-configuration").

```
db2 "call rdsadmin.set_configuration(
    '`name'`,
    '`value`')"
```

**Example:**

```
db2 "call rdsadmin.set_configuration('ARCHIVE_LOG_COPY_TARGET_S3_ARN', 'arn:aws:s3:::my_rds_db2_backups/archive-log-copy/')"
```

3. Enable archive log copying for a database by calling `rdsadmin.enable_archive_log_copy`.
   Replace `database_name` with your database name.

```
db2 "call rdsadmin.enable_archive_log_copy(?, '`database_name`')"
```

4. Similarly,to disable archive log copying for a database, call `rdsadmin.disable_archive_log_copy`.

```
db2 "call rdsadmin.disable_archive_log_copy(?, '`database_name`')"
```

5. Confirm the archive log copy status by calling `rdsadmin.list_databases`.

```
db2 "select * from table(rdsadmin.list_databases())"
```

**Sample output:**

```
DATABASE_NAME   CREATE_TIME                DATABASE_UNIQUE_ID                                 ARCHIVE_LOG_RETENTION_HOURS ARCHIVE_LOG_COPY ARCHIVE_LOG_LAST_UPLOAD_FILE ARCHIVE_LOG_LAST_UPLOAD_FILE_TIME ARCHIVE_LOG_COPY_STATUS
--------------- -------------------------- -------------------------------------------------- --------------------------- ---------------- ---------------------------- --------------------------------- ------------------------------
RDSADMIN        2026-01-06-02.03.42.569069 RDSADMIN                                                                     0 DISABLED         -                            -                                 -
FOO             2026-01-06-02.13.42.885650 F0D81C7E-7213-4565-B376-4F33FCF420E3                                         7 ENABLED          S0006536.LOG                 2026-01-28-19.15.10.000000        UPLOADING
CODEP           2026-01-14-19.42.42.508476 106EEF95-6E30-4FFF-85AE-B044352DF095                                         0 DISABLED         -                            -                                 -
...
```

## Restoring a database

To move a database from an Amazon S3 bucket to your RDS for Db2 DB instance, call the
`rdsadmin.restore_database` stored procedure. For more information, see
[RESTORE DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-restore-database "https://www.ibm.com/docs/en/db2/11.5?topic=commands-restore-database") in the IBM Db2 documentation.

###### To restore a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. (Optional) Check your current configuration settings to optimize the restore
   operation by calling `rdsadmin.show_configuration`. For more
   information, see [rdsadmin.show_configuration](db2-sp-managing-databases.md#db2-sp-show-configuration "db2-sp-managing-databases.md#db2-sp-show-configuration").

```
db2 "call rdsadmin.show_configuration('`name`')"
```

3. Configure the settings to optimize the restore operation by calling
   `rdsadmin.set_configuration`. Explicitly setting these values can
   improve the performance when restoring databases with large volumes of data. For
   more information, see [rdsadmin.set_configuration](db2-sp-managing-databases.md#db2-sp-set-configuration "db2-sp-managing-databases.md#db2-sp-set-configuration").

```
db2 "call rdsadmin.set_configuration(
    '`name`',
    '`value`')"
```

4. Restore the database by calling `rdsadmin.restore_database`. For
   more information, see [rdsadmin.restore_database](db2-sp-managing-databases.md#db2-sp-restore-database "db2-sp-managing-databases.md#db2-sp-restore-database").

```
db2 "call rdsadmin.restore_database(
    ?,
    '`database_name`',
    '`s3_bucket_name`',
    '`s3_prefix`',
    `restore_timestamp`,
    '`backup_type`')"
```

5. (Optional) Confirm that your database was restored by calling
   `rdsadmin.list_databases` and checking that the restored database
   is listed. For more information, see [rdsadmin.list_databases](db2-user-defined-functions.md#db2-udf-list-databases "db2-user-defined-functions.md#db2-udf-list-databases").
6. Bring the database back online and apply additional transaction logs by
   calling `rdsadmin.rollforward_database`. For more information, see
   [rdsadmin.rollforward_database](db2-sp-managing-databases.md#db2-sp-rollforward-database "db2-sp-managing-databases.md#db2-sp-rollforward-database").

```
db2 "call rdsadmin.rollforward_database(
    ?,
    '`database_name`',
    '`s3_bucket_name`',
    `s3_prefix`,
    '`rollforward_to_option`',
    '`complete_rollforward`')"
```

7. (Optional) Check the status of the `rdsadmin.rollforward_database`
   stored procedure by calling the [rdsadmin.rollforward_status](db2-sp-managing-databases.md#db2-sp-rollforward-status "db2-sp-managing-databases.md#db2-sp-rollforward-status")
   stored procedure.
8. If you set `complete_rollforward` to `FALSE` in the
   previous step, then you must finish bringing the database back online by calling
   `rdsadmin.complete_rollforward`. For more information, see [rdsadmin.complete_rollforward](db2-sp-managing-databases.md#db2-sp-complete-rollforward "db2-sp-managing-databases.md#db2-sp-complete-rollforward").

```
db2 "call rdsadmin.complete_rollforward(
    ?,
    '`database_name`')"
```

9. (Optional) Check the status of the `rdsadmin.complete_rollforward`
   stored procedure by calling the [rdsadmin.rollforward_status](db2-sp-managing-databases.md#db2-sp-rollforward-status "db2-sp-managing-databases.md#db2-sp-rollforward-status")
   stored procedure.

## Listing databases

You can list all of your databases running on Amazon RDS for Db2 by calling the
`rdsadmin.list_databases` user-defined function.

###### To list your databases

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. List your databases by calling `rdsadmin.list_databases`. For more
   information, see [rdsadmin.list_databases](db2-user-defined-functions.md#db2-udf-list-databases "db2-user-defined-functions.md#db2-udf-list-databases").

```
db2 "select * from table(rdsadmin.list_databases())"
```

## Collecting information about databases

To collect information about a database on a RDS for Db2 DB instance, call the
`rdsadmin.db2pd_command` stored procedure. This information can help with
monitoring your databases or troubleshooting issues.

###### To collect information about a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Collect information about the database by calling
   `rdsadmin.db2pd_command`. For more information, see [rdsadmin.db2pd_command](db2-sp-managing-databases.md#db2-sp-db2pd-command "db2-sp-managing-databases.md#db2-sp-db2pd-command").

```
db2 "call rdsadmin.db2pd_command('`db2pd_cmd`')"
```

## Forcing applications off of

databases

To force applications off of a database on your RDS for Db2 DB instance, call the
`rdsadmin.force_application` stored procedure. Before you perform
maintenance on your databases, force applications off of your databases.

###### To force applications off of a database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Force applications off of a database by calling
   `rdsadmin.force_application`. For more information, see [rdsadmin.force_application](db2-sp-managing-databases.md#db2-sp-force-application "db2-sp-managing-databases.md#db2-sp-force-application").

```
db2 "call rdsadmin.force_application(
    ?,
    '`applications`')"
```

## Generating performance

reports

You can generate performance reports with a procedure or a script. For information about
using a procedure, see [DBSUMMARY procedure ‐ Generate a summary report of system and
application performance metrics](https://www.ibm.com/docs/en/db2/11.5?topic=mm-dbsummary-procedure-generate-summary-report-system-application-performance-metrics "https://www.ibm.com/docs/en/db2/11.5?topic=mm-dbsummary-procedure-generate-summary-report-system-application-performance-metrics") in the IBM Db2 documentation.

Db2 includes a `db2mon.sh` file in its `~sqllib/sample/perf`
directory. Running the script produces a low-cost, extensive SQL metrics report. To download
the `db2mon.sh` file and related script files, see the [perf](https://github.com/IBM/db2-samples/tree/master/perf "https://github.com/IBM/db2-samples/tree/master/perf")
directory in the IBM db2-samples GitHub repository.

###### To generate performance reports with the script

1. Connect to your Db2 database using the master username and master password for
   your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadminuser `master_username` using `master_password`
```

2. Create a buffer pool named `db2monbp` with a page size of 4096 by
   calling `rdsadmin.create_bufferpool`. For more information, see [rdsadmin.create_bufferpool](db2-sp-managing-buffer-pools.md#db2-sp-create-buffer-pool "db2-sp-managing-buffer-pools.md#db2-sp-create-buffer-pool").

```
db2 "call rdsadmin.create_bufferpool('`database_name`','db2monbp',4096)"
```

3. Create a temporary tablespace named `db2montmptbsp` that uses the
   `db2monbp` buffer pool by calling
   `rdsadmin.create_tablespace`. For more information, see [rdsadmin.create_tablespace](db2-sp-managing-tablespaces.md#db2-sp-create-tablespace "db2-sp-managing-tablespaces.md#db2-sp-create-tablespace").

```
db2 "call rdsadmin.create_tablespace('database_name',\
    'db2montmptbsp','db2monbp',4096,1000,100,'T')"
```

4. Open the `db2mon.sh` script, and modify the line about connecting to a
   database.
   1. Remove the following line.

   ```
   db2 -v connect to $dbName
   ```

   2. Replace the line in the previous step with the following line. In the
      following example, replace `master_username` and
      `master_password` with the master username and
      master password for your RDS for Db2 DB instance.

   ```
   db2 -v connect to $dbName user `master_username` using `master_password`
   ```

   3. Remove the following lines.

   ```
   db2 -v create bufferpool db2monbp

   db2 -v create user temporary tablespace db2montmptbsp bufferpool db2monbp

   db2 -v drop tablespace db2montmptbsp

   db2 -v drop bufferpool db2monbp
   ```

5. Run the `db2mon.sh` script to output a report at specified intervals.
   In the following example, replace `absolute_path` with the
   complete path to the script file, `rds_database_alias` with
   the name of your database, and `seconds` with the number of
   seconds (0 to 3600) between report generation.

```
`absolute_path`/db2mon.sh `rds_database_alias` `seconds` | tee -a db2mon.out
```

**Examples**

The following example shows that the script file is located in the
`perf` directory under the `home` directory.

```
/home/db2inst1/sqllib/samples/perf/db2mon.sh `rds_database_alias` `seconds` | tee -a db2mon.out
```

6. Drop the buffer pool and the tablespace that were created for the
   `db2mon.sh` file. In the following example, replace
   `master_username` and
   `master_password` with the master username and master
   password for your RDS for Db2 DB instance. Replace
   `database_name` with the name of your database. For
   more information, see [rdsadmin.drop_tablespace](db2-sp-managing-tablespaces.md#db2-sp-drop-tablespace "db2-sp-managing-tablespaces.md#db2-sp-drop-tablespace") and [rdsadmin.drop_bufferpool](db2-sp-managing-buffer-pools.md#db2-sp-drop-buffer-pool "db2-sp-managing-buffer-pools.md#db2-sp-drop-buffer-pool").

```
db2 connect to rdsadmin user `master_username` using `master_password`

db2 "call rdsadmin.drop_tablespace('`database_name`','db2montmptbsp')"

db2 "call rdsadmin.drop_bufferpool('`database_name`','db2monbp')"
```
