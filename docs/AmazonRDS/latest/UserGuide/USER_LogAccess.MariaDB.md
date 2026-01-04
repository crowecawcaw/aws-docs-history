# Accessing MariaDB error logs

The MariaDB error log is written to the `<host-name>.err` file.
You can view this file by using the Amazon RDS console, You can also retrieve the log using
the Amazon RDS API, Amazon RDS CLI, or AWS SDKs. The `<host-name>.err`
file is flushed every 5 minutes, and its contents are appended to
`mysql-error-running.log`. The
`mysql-error-running.log` file is then rotated every hour and the
hourly files generated during the last 24 hours are retained. Each log file has the hour
it was generated (in UTC) appended to its name. The log files also have a timestamp that
helps you determine when the log entries were written.

MariaDB writes to the error log only on startup, shutdown, and when it encounters errors.
A DB instance can go hours or days without new entries being written to the error
log. If you see no recent entries, it's because the server did not encounter an
error that resulted in a log entry.
