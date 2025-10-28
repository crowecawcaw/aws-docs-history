# Logging for Aurora MySQL databases

Aurora MySQL logs provide essential information about database activity and errors. By enabling these logs, you can identify and
troubleshoot issues, understand database performance, and audit database activity. We recommend that you enable these logs for
all of your Aurora MySQL DB instances to ensure optimal performance and availability of the databases. The following types of
logging can be enabled. Each log contains specific information that can lead to uncovering impacts to database
processing.

- Error – Aurora MySQL writes to the error log only on startup, shutdown, and when it encounters errors. A DB
  instance can go hours or days without new entries being written to the error log. If you see no recent entries, it's
  because the server didn't encounter an error that would result in a log entry. Error logging is enabled by default. For
  more information, see [Aurora MySQL error logs](USER_LogAccess.MySQL.md#USER_LogAccess.MySQL.Errorlog "USER_LogAccess.MySQL.md#USER_LogAccess.MySQL.Errorlog").
- General – The general log provides detailed information about database activity, including all SQL statements
  executed by the database engine. For more information on enabling general logging and setting logging parameters, see
  [Aurora MySQL slow query and general logs](USER_LogAccess.MySQL.md#USER_LogAccess.MySQL.Generallog "USER_LogAccess.MySQL.md#USER_LogAccess.MySQL.Generallog"), and [The general query log](https://dev.mysql.com/doc/refman/8.0/en/query-log.html "https://dev.mysql.com/doc/refman/8.0/en/query-log.html") in the MySQL
  documentation.

###### Note

General logs can grow to be very large and consume your storage. For more information, see [Log rotation and retention for Aurora MySQL](USER_LogAccess.MySQL.md#USER_LogAccess.AMS.LogFileSize.retention "USER_LogAccess.MySQL.md#USER_LogAccess.AMS.LogFileSize.retention").

- Slow query – The slow query log consists of SQL statements that take more than [long_query_time](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_long_query_time "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_long_query_time") seconds to run and require at least [min_examined_row_limit](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_min_examined_row_limit "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_min_examined_row_limit") rows to be examined. You can use the slow query log to find queries that take a long
  time to run and are therefore candidates for optimization.

The default value for `long_query_time` is 10 seconds. We recommend that you start with a high value to
identify the slowest queries, then work your way down for fine tuning.

You can also use related parameters, such as `log_slow_admin_statements` and
`log_queries_not_using_indexes`. Compare `rows_examined` with `rows_returned`. If
`rows_examined` is much greater than `rows_returned`, then those queries can potentially be
blocking.

In Aurora MySQL version 3, you can enable `log_slow_extra` to obtain more details. For more information, see
[Slow query log
contents](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html#slow-query-log-contents "https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html#slow-query-log-contents") in the MySQL documentation. You can also modify `long_query_time` at the session level
for debugging query execution interactively, which is especially useful if `log_slow_extra` is enabled
globally.

For more information on enabling slow query logging and setting logging parameters, see [Aurora MySQL slow query and general logs](USER_LogAccess.MySQL.md#USER_LogAccess.MySQL.Generallog "USER_LogAccess.MySQL.md#USER_LogAccess.MySQL.Generallog"), and [The slow query log](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html "https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html") in the MySQL
documentation.

- Audit – The audit log monitors and logs database activity. Audit logging for Aurora MySQL is called Advanced
  Auditing. To enable Advanced Auditing, you set certain DB cluster parameters. For more information, see [Using Advanced Auditing with an Amazon Aurora MySQL DB cluster](AuroraMySQL.md "AuroraMySQL.md").
- Binary – The binary log (binlog) contains events that describe database changes, such as table creation
  operations and changes to table data. It also contains events for statements that potentially could have made changes
  (for example, a [DELETE](https://dev.mysql.com/doc/refman/8.0/en/delete.html "https://dev.mysql.com/doc/refman/8.0/en/delete.html") that matched no rows),
  unless row-based logging is used. The binary log also contains information about how long each statement took that
  updated data.

Running a server with binary logging enabled makes performance slightly slower. However, the benefits of the binary
log in enabling you to set up replication and for restore operations generally outweigh this minor performance
decrease.

###### Note

Aurora MySQL doesn't require binary logging for restore operations.

For more information on enabling binary logging and setting the binlog format, see [Configuring Aurora MySQL binary logging for Single-AZ databases](USER_LogAccess.MySQL.md "USER_LogAccess.MySQL.md"), and [The binary log](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html "https://dev.mysql.com/doc/refman/8.0/en/binary-log.html") in the MySQL
documentation.
You can publish the error, general, slow, query, and audit logs to Amazon CloudWatch Logs. For more information, see [Publishing database logs to Amazon CloudWatch Logs](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md").

Another useful tool for summarizing slow, general, and binary log files is [pt-query-digest](https://docs.percona.com/percona-toolkit/pt-query-digest.html "https://docs.percona.com/percona-toolkit/pt-query-digest.html").
