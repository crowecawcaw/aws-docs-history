# Logging autovacuum and

vacuum activities

Information about autovacuum activities is sent to the `postgresql.log` based
on the level specified in the `rds.force_autovacuum_logging_level` parameter.
Following are the values allowed for this parameter and the PostgreSQL versions for which that
value is the default setting:

- `disabled` (PostgreSQL 10, PostgreSQL 9.6)
- `debug5`, `debug4`, `debug3`, `debug2`,
  `debug1`
- `info` (PostgreSQL 12, PostgreSQL 11)
- `notice`
- `warning` (PostgreSQL 13 and above)
- `error`, log, `fatal`, `panic`
  The `rds.force_autovacuum_logging_level` works with the
  `log_autovacuum_min_duration` parameter. The
  `log_autovacuum_min_duration` parameter's value is the threshold (in
  milliseconds) above which autovacuum actions get logged. A setting of `-1` logs
  nothing, while a setting of 0 logs all actions. As with
  `rds.force_autovacuum_logging_level`, default values for
  `log_autovacuum_min_duration` are version dependent, as follows:

- `10000 ms` – PostgreSQL 14, PostgreSQL 13, PostgreSQL 12, and
  PostgreSQL 11
- `(empty)` – No default value for PostgreSQL 10 and PostgreSQL
  9.6
  We recommend that you set `rds.force_autovacuum_logging_level` to
  `WARNING`. We also recommend that you set
  `log_autovacuum_min_duration` to a value from 1000 to 5000. A setting of 5000
  logs activity that takes longer than 5,000 milliseconds. Any setting other than -1 also logs
  messages if the autovacuum action is skipped because of a conflicting lock or concurrently
  dropped relations. For more information, see [Automatic
  Vacuuming](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html "https://www.postgresql.org/docs/current/runtime-config-autovacuum.html") in the PostgreSQL documentation.

To troubleshoot issues, you can change the `rds.force_autovacuum_logging_level`
parameter to one of the debug levels, from `debug1` up to `debug5` for
the most verbose information. We recommend that you use debug settings for short periods of
time and for troubleshooting purposes only. To learn more, see [When to log](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN "https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN") in the PostgreSQL documentation.

###### Note

PostgreSQL allows the `rds_superuser` account to view autovacuum sessions in
`pg_stat_activity`. For example, you can identify and end an autovacuum session
that is blocking a command from running, or running slower than a manually issued vacuum
command.
