# Amazon RDS for Db2 user-defined function reference

The following user-defined functions are available for Amazon RDS DB instances
running the Db2 engine.

###### Topics

- [rdsadmin.get_task_status](#db2-udf-get-task-status "#db2-udf-get-task-status")
- [rdsadmin.list_databases](#db2-udf-list-databases "#db2-udf-list-databases")
- [rdsadmin.list_modifiable_db_params](#db2-udf-list-modi-db-params "#db2-udf-list-modi-db-params")

## rdsadmin.get_task_status

Returns the status of a task.

### Syntax

```
db2 "select task_id, task_type, database_name, lifecycle,
    varchar(bson_to_json(task_input_params), 500) as task_params,
    cast(task_output as varchar(500)) as task_output
    from table(rdsadmin.get_task_status(task_id,'database_name','task_type'))"
```

### Parameters

The following parameters are optional. If you do not provide any parameters, the
user-defined function returns the status of all tasks for all databases. Amazon RDS
retains task history for 35 days.

`task_id`

The ID of the task being run. This ID is returned when you run a task.
Default: `0`.

`database_name`

The name of the database for which the task is being run.

`task_type`

The type of the task to query. Valid values: `ADD_GROUPS`,
`ADD_USER`, `ALTER_BUFFERPOOL`,
`ALTER_TABLESPACE`, `CHANGE_PASSWORD`,
`COMPLETE_ROLLFORWARD`, `CREATE_BUFFERPOOL`,
`CREATE_DATABASE`, `CREATE_ROLE`,
`CREATE_TABLESPACE`, `DROP_BUFFERPOOL`,
`DROP_DATABASE`, `DROP_TABLESPACE`,
`LIST_USERS`, `REMOVE_GROUPS`,
`REMOVE_USER`, `RESTORE_DB`,
`ROLLFORWARD_DB_LOG`, `ROLLFORWARD_STATUS`,
`UPDATE_DB_PARAM`.

### Usage notes

You can use the `rdsadmin.get_task_status` user-defined function to check the
status of the following tasks for Amazon RDS for Db2. This list is not exhaustive.

- Creating, altering, or dropping a buffer pool
- Creating, altering, or dropping a tablespace
- Creating or dropping a database
- Restoring a database backup from Amazon S3
- Rolling forward database logs from Amazon S3

### Examples

The following example displays the columns returned when
`rdsadmin.get_task_status` is called.

```
db2 "describe select * from table(rdsadmin.get_task_status())"
```

The following example lists the status of all tasks.

```
db2 "select task_id, task_type, database_name, lifecycle,
    varchar(bson_to_json(task_input_params), 500) as task_params,
    cast(task_output as varchar(500)) as task_output
    from table(rdsadmin.get_task_status(null,null,null))"
```

The following example lists the status of a specific task.

```
db2 "select task_id, task_type, database_name,
    varchar(bson_to_json(task_input_params), 500) as task_params
    from table(rdsadmin.get_task_status(1,null,null))"
```

The following example lists the status of a specific task and database.

```
db2 "select task_id, task_type, database_name,
    varchar(bson_to_json(task_input_params), 500) as task_params
    from table(rdsadmin.get_task_status(2,'SAMPLE',null))"
```

The following example lists the status of all `ADD_GROUPS`
tasks.

```
db2 "select task_id, task_type, database_name,
    varchar(bson_to_json(task_input_params), 500) as task_params
    from table(rdsadmin.get_task_status(null,null,'add_groups'))"
```

The following example lists the status of all tasks for a specific database.

```
db2 "select task_id, task_type, database_name,
    varchar(bson_to_json(task_input_params), 500) as task_params
    from table(rdsadmin.get_task_status(null,'testdb', null))"
```

The following example outputs the JSON values as columns.

```
db2 "select varchar(r.task_type,25) as task_type, varchar(r.lifecycle,10) as lifecycle, r.created_at, u.* from
    table(rdsadmin.get_task_status(null,null,'restore_db')) as r, json_table(r.task_input_params, 'strict $' columns(s3_prefix varchar(500)
    null on empty, s3_bucket_name varchar(500) null on empty) error on error ) as U"
```

### Response

The `rdsadmin.get_task_status` user-defined function returns the
following columns:

`TASK_ID`

The ID of the task.

`TASK_TYPE`

Depends on the input parameters.

- `ADD_GROUPS` – Adds groups.
- `ADD_USER` – Adds a user.
- `ALTER_BUFFERPOOL` – Alters a buffer
  pool.
- `ALTER_TABLESPACE` – Alters a
  tablespace.
- `CHANGE_PASSWORD` – Changes a user's
  password.
- `COMPLETE_ROLLFORWARD` – Completes an
  `rdsadmin.rollforward_database` task and
  activates a database.
- `CREATE_BUFFERPOOL` – Creates a buffer
  pool.
- `CREATE_DATABASE` – Creates a
  database.
- `CREATE_ROLE` – Creates a Db2 role for a
  user.
- `CREATE_TABLESPACE` – Creates a
  tablespace.
- `DROP_BUFFERPOOL` – Drops a buffer
  pool.
- `DROP_DATABASE` – Drops a database.
- `DROP_TABLESPACE` – Drops a
  tablespace.
- `LIST_USERS` – Lists all users.
- `REMOVE_GROUPS` – Removes groups.
- `REMOVE_USER` – Removes a user.
- `RESTORE_DB` – Restores a full
  database.
- `ROLLFORWARD_DB_LOG` – Performs an
  `rdsadmin.rollforward_database` task on database
  logs.
- `ROLLFORWARD_STATUS` – Returns the status of
  an `rdsadmin.rollforward_database` task.
- `UPDATE_DB_PARAM` – Updates the data
  parameters.

`DATABASE_NAME`

The name of the database with which the task is associated.

`COMPLETED_WORK_BYTES`

The number of bytes restored by the task.

`DURATION_MINS`

The time taken to complete the task.

`LIFECYCLE`

The status of the task. Possible statuses:

- `CREATED` – After a task is submitted to
  Amazon RDS, Amazon RDS sets the status to `CREATED`.
- `IN_PROGRESS` – After a task starts, Amazon RDS
  sets the status to `IN_PROGRESS`. It can take up to 5
  minutes for a status to change from `CREATED` to
  `IN_PROGRESS`.
- `SUCCESS` – After a task completes, Amazon RDS
  sets the status to `SUCCESS`.
- `ERROR` – If a restore task fails, Amazon RDS
  sets the status to `ERROR`. For more information
  about the error, see `TASK_OUPUT`.

`CREATED_BY`

The `authid` that created the command.

`CREATED_AT`

The date and time when the task was created.

`LAST_UPDATED_AT`

The data and time when the task was last updated.

`TASK_INPUT_PARAMS`

The parameters differ based on the task type. All of the input
parameters are represented as a JSON object. For example, the JSON keys
for the `RESTORE_DB` task are the following:

- `DBNAME`
- `RESTORE_TIMESTAMP`
- `S3_BUCKET_NAME`
- `S3_PREFIX`

`TASK_OUTPUT`

Additional information about the task. If an error occurs during
native restore, this column includes information about the error.

### Response examples

The following response example shows that a database called `TESTJP`
was successfully created. For more information, see the [rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database") stored procedure.

```
`1 SUCCESS CREATE_DATABASE RDSDB 2023-10-24-18.32.44.962689 2023-10-24-18.34.50.038523 1 TESTJP { "CODESET" : "IBM-437", "TERRITORY" : "JP", "COLLATION" : "SYSTEM", "AUTOCONFIGURE_CMD" : "", "PAGESIZE" : 4096 }
2023-10-24-18.33.30.079048 Task execution has started.

2023-10-24-18.34.50.038523 Task execution has completed successfully`.
```

The following response example explains why dropping a database failed. For more
information, see the [rdsadmin.drop_database](db2-sp-managing-databases.md#db2-sp-drop-database "db2-sp-managing-databases.md#db2-sp-drop-database") stored procedure.

```
1 ERROR DROP_DATABASE RDSDB 2023-10-10-16.33.03.744122 2023-10-10-16.33.30.143797 - 2023-10-10-16.33.30.098857 Task execution has started.
2023-10-10-16.33.30.143797 Caught exception during executing task id 1, Aborting task.
Reason Dropping database created via rds CreateDBInstance api is not allowed.
Only database created using rdsadmin.create_database can be dropped
```

The following response example shows the successful restoration of a database. For
more information, see the [rdsadmin.restore_database](db2-sp-managing-databases.md#db2-sp-restore-database "db2-sp-managing-databases.md#db2-sp-restore-database") stored
procedure.

```
1 RESTORE_DB  SAMPLE  SUCCESS

{ "S3_BUCKET_NAME" : "`amzn-s3-demo-bucket`", "S3_PREFIX" : "SAMPLE.0.rdsdb3.DBPART000.20230413183211.001", "RESTORE_TIMESTAMP" : "20230413183211", "BACKUP_TYPE" : "offline" }

2023-11-06-18.31.03.115795 Task execution has started.
2023-11-06-18.31.04.300231 Preparing to download
2023-11-06-18.31.08.368827 Download complete. Starting Restore
2023-11-06-18.33.13.891356 Task Completed Successfully
```

## rdsadmin.list_databases

Returns a list of all databases running on an RDS for Db2 DB instance.

### Syntax

```
db2 "select * from table(rdsadmin.list_databases())"
```

### Usage notes

This user-defined function doesn't specify whether databases are in an activated
or deactivated state.

If you don't see your databases in the list, call the
[rdsadmin.get_task_status](#db2-udf-get-task-status "#db2-udf-get-task-status") user-defined function and look for error
messages.

### Response

The `rdsadmin.list_databases` user-defined function returns the
following columns:

`DATABASE_NAME`

The name of a database.

`CREATE_TIME`

The date and time when the database was created.

`DATABASE_UNIQUE_ID`

The RDS created GUID to uniquely identify Db2 database.

`ARCHIVE_LOG_RETENTION_HOUR`

The number of hours to retain the archive log files.

`ARCHIVE_LOG_COPY`

Displays if the feature is ENABLED or DISABLED for the database.

`ARCHIVE_LOG_LAST_UPLOAD_FILE`

Indicates last archive log uploaded to S3.

`ARCHIVE_LOG_LAST_UPLOAD_FILE_TIME`

Indicates the time when the log file was archived.

`ARCHIVE_LOG_COPY_STATUS`

Displays the status of the archive log copy.

UPLOADING : indicates that archive log files are being uploaded to S3.

CONFIGURATION_ERROR : indicates that there is a configuration issue requiring your attention.

To view detailed error look at RDS Event Messages for you Db Instance. The Event Messages can be viewed at [Viewing Amazon RDS events.](USER_ListEvents.md "USER_ListEvents.md")

### Response examples

The following response example shows a list of databases and the times when they
were created. `rdsadmin` is a database that Amazon RDS manages and always
appears in the output.

```
DATABASE_NAME   CREATE_TIME                DATABASE_UNIQUE_ID                                 ARCHIVE_LOG_RETENTION_HOURS ARCHIVE_LOG_COPY ARCHIVE_LOG_LAST_UPLOAD_FILE ARCHIVE_LOG_LAST_UPLOAD_FILE_TIME ARCHIVE_LOG_COPY_STATUS
--------------- -------------------------- -------------------------------------------------- --------------------------- ---------------- ---------------------------- --------------------------------- ------------------------------
RDSADMIN        2026-01-06-02.03.42.569069 RDSADMIN                                                                     0 DISABLED         -                            -                                 -
FOO             2026-01-06-02.13.42.885650 F0D81C7E-7213-4565-B376-4F33FCF420E3                                         0 ENABLED          S0006536.LOG                 2026-01-28-19.15.10.000000        UPLOADING
CODEP           2026-01-14-19.42.42.508476 106EEF95-6E30-4FFF-85AE-B044352DF095                                         0 DISABLED         -                            -                                 -
...
```

## rdsadmin.list_modifiable_db_params

Returns a list of all the modifiable database configuration parameters.

### Syntax

```
db2 "select * from table(rdsadmin.list_modifiable_db_params())"
```

### Usage notes

This user-defined function displays a selected lists of modifiable database parameters. These parameters can be updated using the stored procedure [rdsadmin.update_db_param](db2-sp-managing-databases.md#db2-sp-update-db-param "db2-sp-managing-databases.md#db2-sp-update-db-param").

Any database parameter not included in this list has been restricted and cannot be modified.

### Response

The `rdsadmin.list_modifiable_db_params` user-defined function returns the
following columns:

`PARAM_NAME`

The name of the parameter that can be modified.

`DEFAULT_VALUE`

Default parameter value at the time of database creation.

`RESTART_REQUIRED`

If database recycle is required of not.

Y = Yes, Database restart is required.

N = No, Database restart is not required.

### Response examples

The following is a sample (truncated) list of expected output.

```
PARAM_NAME             DEFAULT_VALUE RESTART_REQUIRED
---------------------- ------------- ----------------
ACT_SORTMEM_LIMIT      NONE          N
ARCHRETRYDELAY         20            N
AUTHN_CACHE_DURATION   3             N
AUTHN_CACHE_USERS      0             N
AUTO_CG_STATS          OFF           N
...
```
