# Scheduling maintenance with the PostgreSQL pg_cron extension

You can use the PostgreSQL `pg_cron` extension to schedule maintenance commands
within a PostgreSQL database. For more information about the extension, see [What is pg_cron?](https://github.com/citusdata/pg_cron "https://github.com/citusdata/pg_cron") in the pg_cron
documentation.

The `pg_cron` extension is supported on Aurora PostgreSQL engine
versions 12.6 and higher version

To learn more about using `pg_cron`, see [Schedule jobs with pg_cron on your RDS for PostgreSQL or your Aurora PostgreSQL-Compatible Edition
databases](https://aws.amazon.com/blogs/database/schedule-jobs-with-pg_cron-on-your-amazon-rds-for-postgresql-or-amazon-aurora-for-postgresql-databases/ "https://aws.amazon.com/blogs/database/schedule-jobs-with-pg_cron-on-your-amazon-rds-for-postgresql-or-amazon-aurora-for-postgresql-databases/").

###### Note

The `pg_cron` extension version is displayed as a two digit version, for example, 1.6,
in the pg_available_extensions view. While you might see three digit versions, for
example, 1.6.4 or 1.6.5, listed in some contexts, you must specify the two digit version
when performing an extension upgrade.

###### Topics

- [Setting up the pg_cron extension](#PostgreSQL_pg_cron.enable "#PostgreSQL_pg_cron.enable")
- [Granting database users permissions to use pg_cron](#PostgreSQL_pg_cron.permissions "#PostgreSQL_pg_cron.permissions")
- [Scheduling pg_cron jobs](#PostgreSQL_pg_cron.examples "#PostgreSQL_pg_cron.examples")
- [Reference for the pg_cron extension](#PostgreSQL_pg_cron.reference "#PostgreSQL_pg_cron.reference")

## Setting up the pg_cron extension

Set up the `pg_cron` extension as follows:

1. Modify the custom parameter group associated with your PostgreSQL DB instance
   by adding `pg_cron` to the `shared_preload_libraries`
   parameter value.

Restart the PostgreSQL DB instance to have changes to the parameter group take
effect. To learn more about working with parameter groups, see
[Amazon Aurora PostgreSQL parameters](AuroraPostgreSQL.Reference.md "AuroraPostgreSQL.Reference.md"). 2. After the PostgreSQL DB instance has restarted, run the following command
using an account that has `rds_superuser` permissions. For example,
if you used the default settings when you created your Aurora PostgreSQL DB cluster, connect as user
`postgres` and create the extension.

```
CREATE EXTENSION pg_cron;
```

The `pg_cron` scheduler is set in the default PostgreSQL database
named `postgres`. The `pg_cron` objects are created in
this `postgres` database and all scheduling actions run in this
database. 3. You can use the default settings, or you can schedule jobs to run in other
databases within your PostgreSQL DB instance. To schedule jobs for other
databases within your PostgreSQL DB instance, see the example in [Scheduling a cron job for a database other than the default database](#PostgreSQL_pg_cron.otherDB "#PostgreSQL_pg_cron.otherDB").

## Granting database users permissions to use pg_cron

Installing the `pg_cron` extension requires the `rds_superuser`
privileges. However, permissions to use the `pg_cron` can be granted (by a
member of the `rds_superuser` group/role) to other database users, so that
they can schedule their own jobs. We recommend that you grant permissions to the
`cron` schema only as needed if it improves operations in your production
environment.

To grant a database user permission in the `cron` schema, run the following
command:

```
`postgres=>` GRANT USAGE ON SCHEMA cron TO `db-user`;
```

This gives `db-user` permission to access the
`cron` schema to schedule cron jobs for the objects that they have
permissions to access. If the database user doesn't have permissions, the job fails
after posting the error message to the `postgresql.log` file, as shown in the
following:

```
2020-12-08 16:41:00 UTC::@:[30647]:ERROR: permission denied for table *table-name*
2020-12-08 16:41:00 UTC::@:[27071]:LOG: background worker "pg_cron" (PID 30647) exited with exit code 1
```

In other words, make sure that database users that are granted permissions on the
`cron` schema also have permissions on the objects (tables, schemas, and
so on) that they plan to schedule.

The details of the cron job and its success or failure are also captured in the
`cron.job_run_details` table. For more information, see [Tables for scheduling jobs and capturing status](#PostgreSQL_pg_cron.tables "#PostgreSQL_pg_cron.tables").

## Scheduling pg_cron jobs

The following sections show how you can schedule various management tasks using
`pg_cron` jobs.

###### Note

When you create `pg_cron` jobs, check that the
`max_worker_processes` setting is larger than the number of
`cron.max_running_jobs`. A `pg_cron` job fails if it runs
out of background worker processes. The default number of `pg_cron` jobs
is `5`. For more information, see [Parameters for managing the pg_cron extension](#PostgreSQL_pg_cron.parameters "#PostgreSQL_pg_cron.parameters").

###### Topics

- [Vacuuming a table](#PostgreSQL_pg_cron.vacuum "#PostgreSQL_pg_cron.vacuum")
- [Purging the pg_cron history table](#PostgreSQL_pg_cron.job_run_details "#PostgreSQL_pg_cron.job_run_details")
- [Logging errors to the postgresql.log file only](#PostgreSQL_pg_cron.log_run "#PostgreSQL_pg_cron.log_run")
- [Scheduling a cron job for a database other than the default database](#PostgreSQL_pg_cron.otherDB "#PostgreSQL_pg_cron.otherDB")

### Vacuuming a table

Autovacuum handles vacuum maintenance for most cases. However, you might want to
schedule a vacuum of a specific table at a time of your choosing.

Following is an example of using the `cron.schedule` function to set up
a job to use `VACUUM FREEZE` on a specific table every day at 22:00
(GMT).

```
`SELECT cron.schedule('manual vacuum', '0 22 * * *', 'VACUUM FREEZE pgbench_accounts');`
 `schedule
----------
1
(1 row)`
```

After the preceding example runs, you can check the history in the
`cron.job_run_details` table as follows.

```
`postgres=>` `SELECT * FROM cron.job_run_details;`
`jobid | runid | job_pid | database | username | command | status | return_message | start_time | end_time
-------+-------+---------+----------+----------+--------------------------------+-----------+----------------+-------------------------------+-------------------------------
 1 | 1 | 3395 | postgres | adminuser| vacuum freeze pgbench_accounts | succeeded | VACUUM | 2020-12-04 21:10:00.050386+00 | 2020-12-04 21:10:00.072028+00
(1 row)`
```

Following is a query of the `cron.job_run_details` table to see the
failed jobs.

```
`postgres=>` `SELECT * FROM cron.job_run_details WHERE status = 'failed';`
`jobid | runid | job_pid | database | username | command | status | return_message | start_time | end_time
------+-------+---------+----------+----------+-------------------------------+--------+--------------------------------------------------+-------------------------------+------------------------------
 5 | 4 | 30339 | postgres | adminuser| vacuum freeze pgbench_account | failed | ERROR: relation "pgbench_account" does not exist | 2020-12-04 21:48:00.015145+00 | 2020-12-04 21:48:00.029567+00
(1 row)`
```

For more information, see [Tables for scheduling jobs and capturing status](#PostgreSQL_pg_cron.tables "#PostgreSQL_pg_cron.tables").

### Purging the pg_cron history table

The `cron.job_run_details` table contains a history of cron jobs that
can become very large over time. We recommend that you schedule a job that purges
this table. For example, keeping a week's worth of entries might be sufficient for
troubleshooting purposes.

The following example uses the [cron.schedule](#PostgreSQL_pg_cron.schedule "#PostgreSQL_pg_cron.schedule") function to schedule a job
that runs every day at midnight to purge the `cron.job_run_details`
table. The job keeps only the last seven days. Use your `rds_superuser`
account to schedule the job such as the following.

```
`SELECT cron.schedule('0 0 * * *', $$DELETE
 FROM cron.job_run_details
 WHERE end_time < now() - interval '7 days'$$);`
```

For more information, see [Tables for scheduling jobs and capturing status](#PostgreSQL_pg_cron.tables "#PostgreSQL_pg_cron.tables").

### Logging errors to the postgresql.log file only

To prevent writing to the `cron.job_run_details` table, modify the
parameter group associated with the PostgreSQL DB instance and set the
`cron.log_run` parameter to off. The `pg_cron` extension
no longer writes to the table and captures errors to the `postgresql.log`
file only. For more information, see [Modifying parameters in a DB parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

Use the following command to check the value of the `cron.log_run`
parameter.

```
`postgres=>` `SHOW cron.log_run;`
```

For more information, see [Parameters for managing the pg_cron extension](#PostgreSQL_pg_cron.parameters "#PostgreSQL_pg_cron.parameters").

### Scheduling a cron job for a database other than the default database

The metadata for `pg_cron` is all held in the PostgreSQL default
database named `postgres`. Because background workers are used for
running the maintenance cron jobs, you can schedule a job in any of your databases
within the PostgreSQL DB instance:

###### Note

Only users with `rds_superuser` role or `rds_superuser`
privileges can list all cron jobs in the database. Other users can view only
their own jobs in the `cron.job` table.

1. In the cron database, schedule the job as you normally do using the [cron.schedule](#PostgreSQL_pg_cron.schedule "#PostgreSQL_pg_cron.schedule").

```
`postgres=>` `SELECT cron.schedule('database1 manual vacuum', '29 03 * * *', 'vacuum freeze test_table');`
```

2. As a user with the `rds_superuser` role, update the database
   column for the job that you just created so that it runs in another database
   within your PostgreSQL DB instance.

```
`postgres=>` `UPDATE cron.job SET database = 'database1' WHERE jobid = 106;`
```

3. Verify by querying the `cron.job` table.

```
`postgres=>` `SELECT * FROM cron.job;`
`jobid | schedule | command | nodename | nodeport | database | username | active | jobname
------+-------------+--------------------------------+-----------+----------+----------+-----------+--------+-------------------------
106 | 29 03 * * * | vacuum freeze test_table | localhost | 8192 | database1| adminuser | t | database1 manual vacuum
 1 | 59 23 * * * | vacuum freeze pgbench_accounts | localhost | 8192 | postgres | adminuser | t | manual vacuum
(2 rows)`
```

###### Note

In some situations, you might add a cron job that you intend to run on a
different database. In such cases, the job might try to run in the default
database (`postgres`) before you update the correct database column.
If the user name has permissions, the job successfully runs in the default
database.

## Reference for the pg_cron extension

You can use the following parameters, functions, and tables with the
`pg_cron` extension. For more information, see [What is pg_cron?](https://github.com/citusdata/pg_cron "https://github.com/citusdata/pg_cron") in the pg_cron
documentation.

###### Topics

- [Parameters for managing the pg_cron extension](#PostgreSQL_pg_cron.parameters "#PostgreSQL_pg_cron.parameters")
- [Function reference: cron.schedule](#PostgreSQL_pg_cron.schedule "#PostgreSQL_pg_cron.schedule")
- [Function reference: cron.unschedule](#PostgreSQL_pg_cron.unschedule "#PostgreSQL_pg_cron.unschedule")
- [Tables for scheduling jobs and capturing status](#PostgreSQL_pg_cron.tables "#PostgreSQL_pg_cron.tables")

### Parameters for managing the pg_cron extension

Following is a list of parameters that control the `pg_cron` extension
behavior.

| Parameter                     | Description                                                                                                                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cron.database_name            | The database in which `pg_cron` metadata is<br>kept.                                                                                                                                                                          |
| `cron.host`                   | The hostname to connect to PostgreSQL. You can't modify<br>this value.                                                                                                                                                        |
| `cron.log_run`                | Log every job that runs in the `job_run_details`<br>table. Values are `on` or `off`. For more<br>information, see [Tables for scheduling jobs and capturing status](#PostgreSQL_pg_cron.tables "#PostgreSQL_pg_cron.tables"). |
| `cron.log_statement`          | Log all cron statements before running them. Values are<br>`on` or `off`.                                                                                                                                                     |
| `cron.max_running_jobs`       | The maximum number of jobs that can run concurrently.                                                                                                                                                                         |
| `cron.use_background_workers` | Use background workers instead of client sessions. You<br>can't modify this value.                                                                                                                                            |

Use the following SQL command to display these parameters and their values.

```
`postgres=>` SELECT name, setting, short_desc FROM pg_settings WHERE name LIKE 'cron.%' ORDER BY name;
```

### Function reference: cron.schedule

This function schedules a cron job. The job is initially scheduled in the default
`postgres` database. The function returns a `bigint` value
representing the job identifier. To schedule jobs to run in other databases within
your PostgreSQL DB instance, see the example in [Scheduling a cron job for a database other than the default database](#PostgreSQL_pg_cron.otherDB "#PostgreSQL_pg_cron.otherDB").

The function has two syntax formats.

**Syntax**

```
cron.schedule (job_name,
    schedule,
    command
);

cron.schedule (schedule,
    command
);
```

**Parameters**

| Parameter  | Description                                                                               |
| ---------- | ----------------------------------------------------------------------------------------- |
| `job_name` | The name of the cron job.                                                                 |
| `schedule` | Text indicating the schedule for the cron job. The<br>format is the standard cron format. |
| `command`  | Text of the command to run.                                                               |

**Examples**

```
`postgres=>` `SELECT cron.schedule ('test','0 10 * * *', 'VACUUM pgbench_history');`
 `schedule
----------
 145
(1 row)`

`postgres=>` SELECT cron.schedule ('0 15 * * *', 'VACUUM pgbench_accounts');
 `schedule
----------
 146
(1 row)`
```

### Function reference: cron.unschedule

This function deletes a cron job. You can specify either the `job_name`
or the `job_id`. A policy makes sure that you are the owner to remove the
schedule for the job. The function returns a Boolean indicating success or
failure.

The function has the following syntax formats.

**Syntax**

```
cron.unschedule (job_id);

cron.unschedule (job_name);
```

**Parameters**

| Parameter  | Description                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `job_id`   | A job identifier that was returned from the<br>`cron.schedule` function when the cron<br>job was scheduled. |
| `job_name` | The name of a cron job that was scheduled with the<br>`cron.schedule` function.                             |

**Examples**

```
`postgres=>` SELECT cron.unschedule(108);
 `unschedule
------------
 t
(1 row)`

`postgres=>` `SELECT cron.unschedule('test');`
 `unschedule
------------
 t
(1 row)`
```

### Tables for scheduling jobs and capturing status

The following tables are used to schedule the cron jobs and record how the jobs
completed.

| Table                  | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cron.job`             | Contains the metadata about each scheduled job. Most<br>interactions with this table should be done by using the<br>`cron.schedule` and `cron.unschedule`<br>functions.<br>ImportantWe recommend that you don't give update or insert<br>privileges directly to this table. Doing so would allow the<br>user to update the `username` column to run as<br>`rds-superuser`.                                   |
| `cron.job_run_details` | Contains historic information about past scheduled jobs that<br>ran. This is useful to investigate the status, return messages,<br>and start and end time from the job that ran.<br>NoteTo prevent this table from growing indefinitely, purge it<br>on a regular basis. For an example, see [Purging the pg_cron history table](#PostgreSQL_pg_cron.job_run_details "#PostgreSQL_pg_cron.job_run_details"). |
