# Rotating the query logs

The following stored procedures rotate MySQL logs to backup tables. For more information, see [AuroraMySQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md").

###### Topics

- [mysql.rds_rotate_general_log](#mysql_rds_rotate_general_log "#mysql_rds_rotate_general_log")
- [mysql.rds_rotate_slow_log](#mysql_rds_rotate_slow_log "#mysql_rds_rotate_slow_log")

## mysql.rds_rotate_general_log

Rotates the `mysql.general_log` table to a backup table.

### Syntax

```
CALL mysql.rds_rotate_general_log;
```

### Usage notes

You can rotate the `mysql.general_log` table to a backup table by
calling the `mysql.rds_rotate_general_log` procedure. When log tables are
rotated, the current log table is copied to a backup log table and the entries in
the current log table are removed. If a backup log table already exists, then it is
deleted before the current log table is copied to the backup. You can query the
backup log table if needed. The backup log table for the
`mysql.general_log` table is named
`mysql.general_log_backup`.

You can run this procedure only when the `log_output` parameter is set to `TABLE`.

## mysql.rds_rotate_slow_log

Rotates the `mysql.slow_log` table to a backup table.

### Syntax

```
CALL mysql.rds_rotate_slow_log;
```

### Usage notes

You can rotate the `mysql.slow_log` table to a backup table by calling
the `mysql.rds_rotate_slow_log` procedure. When log tables are rotated,
the current log table is copied to a backup log table and the entries in the current
log table are removed. If a backup log table already exists, then it is deleted
before the current log table is copied to the backup.

You can query the backup log table if needed. The backup log table for the `mysql.slow_log` table is named `mysql.slow_log_backup`.
