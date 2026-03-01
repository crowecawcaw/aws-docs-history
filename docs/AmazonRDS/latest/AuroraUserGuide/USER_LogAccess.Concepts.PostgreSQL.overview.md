# Parameters for logging in Aurora PostgreSQL

You can customize the logging behavior for your Aurora PostgreSQL DB cluster
by modifying various
parameters. In the following table you can find the parameters that affect how long the
logs are stored, when to rotate the log, and whether to output the log as a CSV
(comma-separated value) format. You can also find the text output sent to STDERR, among
other settings. To change settings for the parameters that are modifiable, use a custom
DB cluster
parameter group for your Aurora PostgreSQL DB cluster.
For more information, see
[Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

| Parameter                | Default                      | Description                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| log_destination          | stderr                       | Sets the output format for the log. The default is<br>`stderr` but you can also specify comma-separated<br>value (CSV) by adding `csvlog` to the setting. For more<br>information, see [Setting the log destination (stderr, csvlog)](#USER_LogAccess.Concepts.PostgreSQL.Log_Format "#USER_LogAccess.Concepts.PostgreSQL.Log_Format").     |
| log_filename             | postgresql.log.%Y-%m-%d-%H%M | Specifies the pattern for the log file name. In addition to the default, this parameter<br>supports `postgresql.log.%Y-%m-%d` and<br>`postgresql.log.%Y-%m-%d-%H` for the filename<br>pattern. For Aurora PostgreSQL version 17.4 and later, you can't modify this parameter.                                                               |
| log_line_prefix          | %t:%r:%u@%d:[%p]:            | Defines the prefix for each log line that gets written to<br>`stderr`, to note the time (%t), remote host (%r),<br>user (%u), database (%d), and process ID (%p).                                                                                                                                                                           |
| log_rotation_age         | 60                           | Minutes after which log file is automatically rotated. You can<br>change this value within the range of 1 and 1440 minutes. For more<br>information, see [Setting log file rotation](#USER_LogAccess.Concepts.PostgreSQL.log_rotation "#USER_LogAccess.Concepts.PostgreSQL.log_rotation").                                                  |
| log_rotation_size        | –                            | The size (kB) at which the log is automatically rotated.<br>You can change this value within the<br>range of 50,000 to 1,000,000 kilobytes. To learn more,<br>see [Setting log file rotation](#USER_LogAccess.Concepts.PostgreSQL.log_rotation "#USER_LogAccess.Concepts.PostgreSQL.log_rotation").                                         |
| rds.log_retention_period | 4320                         | PostgreSQL logs that are older than the specified number of<br>minutes are deleted. The default value of 4320 minutes deletes log<br>files after 3 days. For more information, see [Setting the log retention period](#USER_LogAccess.Concepts.PostgreSQL.log_retention_period "#USER_LogAccess.Concepts.PostgreSQL.log_retention_period"). |

To identify application issues, you can look for query failures, login failures,
deadlocks, and fatal server errors in the log. For example, suppose that you converted a
legacy application from Oracle to Aurora PostgreSQL, but not all queries converted
correctly. These incorrectly formatted queries generate error messages that you can find
in the logs to help identify problems. For more information about logging queries, see
[Turning on query logging for your Aurora PostgreSQL DB cluster](USER_LogAccess.Concepts.PostgreSQL.md "USER_LogAccess.Concepts.PostgreSQL.md") .

In the following topics, you can find information about how to set various parameters
that control the basic details for your PostgreSQL logs.

###### Topics

- [Setting the log retention period](#USER_LogAccess.Concepts.PostgreSQL.log_retention_period "#USER_LogAccess.Concepts.PostgreSQL.log_retention_period")
- [Setting log file rotation](#USER_LogAccess.Concepts.PostgreSQL.log_rotation "#USER_LogAccess.Concepts.PostgreSQL.log_rotation")
- [Setting the log destination (stderr, csvlog)](#USER_LogAccess.Concepts.PostgreSQL.Log_Format "#USER_LogAccess.Concepts.PostgreSQL.Log_Format")
- [Understanding the log_line_prefix parameter](#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix "#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix")

## Setting the log retention period

The `rds.log_retention_period` parameter specifies how long your
Aurora PostgreSQL DB cluster
keeps its log
files. The default setting is 3 days (4,320 minutes), but you can set this value to
anywhere from 1 day (1,440 minutes) to 7 days (10,080 minutes). Be sure that your
Aurora PostgreSQL DB cluster has sufficient storage
to hold the log files for the period of time.

We recommend that you have your logs routinely published to Amazon CloudWatch Logs so that you
can view and analyze system data long after the logs have been removed from your
Aurora PostgreSQL DB cluster.
For more
information, see
[Publishing Aurora PostgreSQL logs to Amazon CloudWatch Logs](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). After you set up CloudWatch
publishing, Aurora doesn't delete a log until after it's published to
CloudWatch Logs.

Amazon Aurora compresses older PostgreSQL logs when storage for the
DB instance reaches a threshold. Aurora compresses the files using the gzip
compression utility. For more information, see the [gzip](https://www.gzip.org "https://www.gzip.org") website.

When storage for the DB instance is low and all available logs
are compressed, you get a warning such as the following:

```
Warning: local storage for PostgreSQL log files is critically low for
this Aurora PostgreSQL instance, and could lead to a database outage.
```

If there's not enough storage, Aurora might delete
compressed PostgreSQL logs before the end of a specified retention period. If that
happens, you see a message similar to the following:

```
The oldest PostgreSQL log files were deleted due to local storage constraints.
```

## Setting log file rotation

Aurora creates new log files every hour by default. The timing is
controlled by the `log_rotation_age` parameter. This parameter has a
default value of 60 (minutes), but you can set it to anywhere from 1 minute to 24
hours (1,440 minutes). When it's time for rotation, a new distinct log file is
created. The file is named according to the pattern specified by the
`log_filename` parameter.

Log files can also be rotated according to their size, as specified in the
`log_rotation_size` parameter. This parameter specifies that the log
should be rotated when it reaches the specified size (in kilobytes). The default `log_rotation_size` is 100000 kB
(kilobytes) for an Aurora PostgreSQL DB cluster, but you can set this value to
anywhere from 50,000 to 1,000,000 kilobytes.

The log file names are based on the file name pattern specified in the
`log_filename` parameter. The available settings for this parameter
are as follows:

- `postgresql.log.%Y-%m-%d` – Default format for the log
  file name. Includes the year, month, and date in the name of the log
  file.
- `postgresql.log.%Y-%m-%d-%H` – Includes the hour in the
  log file name format.
- `postgresql.log.%Y-%m-%d-%H%M` – Includes hour:minute in
  the log file name format.

If you set `log_rotation_age` parameter to less than
60 minutes, set the `log_filename` parameter to the minute format.

For more information, see [`log_rotation_age`](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-ROTATION-AGE "https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-ROTATION-AGE") and [`log_rotation_size`](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-ROTATION-SIZE "https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-ROTATION-SIZE") in the PostgreSQL documentation.

## Setting the log destination (`stderr`, `csvlog`)

By default, Aurora PostgreSQL generates logs in standard error (stderr) format.
This format is the default setting for the `log_destination` parameter.
Each message is prefixed using the pattern specified in the
`log_line_prefix` parameter. For more information, see [Understanding the log_line_prefix parameter](#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix "#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix").

Aurora PostgreSQL can also generate the logs in `csvlog`
format. The `csvlog` is useful for analyzing the log data as
comma-separated values (CSV) data. For example, suppose that you use the
`log_fdw` extension to work with your logs as foreign tables. The
foreign table created on `stderr` log files contains a single column with
log event data. By adding `csvlog` to the `log_destination`
parameter, you get the log file in the CSV format with demarcations for the multiple
columns of the foreign table. You can now sort and analyze your logs more easily.

If you specify `csvlog` for this parameter, be aware that both
`stderr` and `csvlog` files are generated. Be sure to
monitor the storage consumed by the logs, taking into account the
`rds.log_retention_period` and other settings that affect log storage
and turnover. Using `stderr` and `csvlog` more than doubles
the storage consumed by the logs.

If you add `csvlog` to `log_destination` and you want to
revert to the `stderr` alone, you need to reset the parameter. To do so,
open the Amazon RDS Console and then open the custom DB
cluster
parameter group for your instance. Choose
the `log_destination` parameter, choose **Edit
parameter**, and then choose **Reset**.

For more information about configuring logging, see [Working with
Amazon RDS and Aurora PostgreSQL logs: Part 1](https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-1/ "https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-1/").

## Understanding the log_line_prefix parameter

The `stderr` log format prefixes each log message with the details
specified by the `log_line_prefix` parameter. The default value
is:

```
%t:%r:%u@%d:[%p]:t
```

Starting from Aurora PostgreSQL version 16, you can also choose:

```
%m:%r:%u@%d:[%p]:%l:%e:%s:%v:%x:%c:%q%a
```

Each log entry sent to stderr includes the following information based on the selected value:

- `%t` – Time of log entry without milliseconds
- `%m` – Time of log entry with milliseconds
- `%r` – Remote host address
- `%u@%d` – User name @ database name
- `[%p]` – Process ID if available
- `%l` – Log line number per session
- `%e` – SQL error code
- `%s` – Process start timestamp
- `%v` – Virtual transaction id
- `%x` – Transaction ID
- `%c` – Session ID
- `%q` – Non-session terminator
- `%a` – Application name
