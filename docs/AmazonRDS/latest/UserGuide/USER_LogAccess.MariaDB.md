# Accessing the MariaDB slow query and general logs

You can write the MariaDB slow query log and general log to a file or database table by
setting parameters in your DB parameter group. For information about creating and
modifying a DB parameter group, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). You must set these parameters before
you can view the slow query log or general log in the Amazon RDS console or by using the
Amazon RDS API, AWS CLI, or AWS SDKs.

You can control MariaDB logging by using the parameters in this list:

- `slow_query_log` or `log_slow_query`: To create the slow query log,
  set to 1. The default is 0.
- `general_log`: To create the general log, set to 1. The default is

0.

- `long_query_time` or `log_slow_query_time`: To prevent fast-running
  queries from being logged in the slow query log, specify a value for the
  shortest query run time to be logged, in seconds. The default is 10 seconds; the
  minimum is 0. If log_output = FILE, you can specify a floating point value that
  goes to microsecond resolution. If log_output = TABLE, you must specify an
  integer value with second resolution. Only queries whose run time exceeds the
  `long_query_time` or `log_slow_query_time` value are
  logged. For example, setting `long_query_time` or
  `log_slow_query_time` to 0.1 prevents any query that runs for
  less than 100 milliseconds from being logged.
- `log_queries_not_using_indexes`: To log all queries that do not use
  an index to the slow query log, set this parameter to 1. The default is 0.
  Queries that do not use an index are logged even if their run time is
  less than the value of the `long_query_time`
  parameter.
- `log_output `option``: You can specify one
 of the following options for the `log_output` parameter:

      + TABLE (default)– Write
       general queries to the `mysql.general_log` table, and
       slow queries to the `mysql.slow_log` table.
      + FILE– Write both general
       and slow query logs to the file system. Log files are rotated
       hourly.
      + NONE– Disable
       logging.

  When logging is enabled, Amazon RDS rotates table logs or deletes log files at regular intervals. This measure is
  a precaution to reduce the possibility of a large log file either blocking database use or
  affecting performance. `FILE` and `TABLE` logging approach rotation and
  deletion as follows:

- When `FILE` logging is enabled, log files are examined every hour and log files
  older than 24 hours are deleted. In some cases, the remaining combined log file
  size after the deletion might exceed the threshold of 2 percent of a DB
  instance's allocated space. In these cases, the largest log files are deleted
  until the log file size no longer exceeds the threshold.
- When `TABLE` logging is enabled, in some cases log tables are rotated every 24
  hours. This rotation occurs if the space used by the table logs is more than 20
  percent of the allocated storage space. It also occurs if the size of all logs
  combined is greater than 10 GB. If the amount of space used for a DB instance is
  greater than 90 percent of the DB instance's allocated storage space, the
  thresholds for log rotation are reduced. Log tables are then rotated if the
  space used by the table logs is more than 10 percent of the allocated storage
  space. They're also rotated if the size of all logs combined is greater than 5
  GB.

When log tables are rotated, the current log table is copied to a backup log table and the
entries in the current log table are removed. If the backup log table already exists, then it is
deleted before the current log table is copied to the backup. You can query the backup log table
if needed. The backup log table for the `mysql.general_log` table is named
`mysql.general_log_backup`. The backup log table for the `mysql.slow_log` table is named
`mysql.slow_log_backup`.

You can rotate the `mysql.general_log` table
by calling the `mysql.rds_rotate_general_log` procedure.
You can rotate the `mysql.slow_log` table
by calling the `mysql.rds_rotate_slow_log` procedure.

Table logs are rotated during a database version upgrade.
Amazon RDS records both `TABLE` and `FILE` log rotation in an Amazon RDS event and
sends you a notification.

To work with the logs from the Amazon RDS console, Amazon RDS API, Amazon RDS CLI, or AWS SDKs, set the
`log_output` parameter to FILE. Like the MariaDB error log,
these log files are rotated hourly. The log files that were generated during the previous
24 hours are retained.

For more information about the slow query and general logs, go to the following topics in
the MariaDB documentation:

- [Slow query log](http://mariadb.com/kb/en/mariadb/slow-query-log/ "http://mariadb.com/kb/en/mariadb/slow-query-log/")
- [General query log](http://mariadb.com/kb/en/mariadb/general-query-log/ "http://mariadb.com/kb/en/mariadb/general-query-log/")
