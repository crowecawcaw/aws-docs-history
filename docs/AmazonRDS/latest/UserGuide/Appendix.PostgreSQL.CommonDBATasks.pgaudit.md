# Reference for the pgAudit

extension

You can specify the level of detail that you want for your audit log by changing one or more of the
parameters listed in this section.

## Controlling pgAudit behavior

You can control the audit logging by changing one or more of the parameters listed in the following table.

| Parameter                    | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pgaudit.log`                | Specifies the statement classes that will be logged by session audit logging. Allowable<br>values include ddl, function, misc, read, role, write, none, all. For more information, see [List of allowable settings for the pgaudit.log parameter](#Appendix.PostgreSQL.CommonDBATasks.pgaudit.reference.pgaudit-log-settings "#Appendix.PostgreSQL.CommonDBATasks.pgaudit.reference.pgaudit-log-settings"). |
| `pgaudit.log_catalog`        | When turned on (set to 1), adds statements to audit trail if all relations in a statement are in pg_catalog.                                                                                                                                                                                                                                                                                                |
| `pgaudit.log_level`          | Specifies the log level to use for log entries. Allowed values: debug5, debug4, debug3, debug2, debug1, info, notice, warning, log                                                                                                                                                                                                                                                                          |
| `pgaudit.log_parameter`      | When turned on (set to 1), parameters passed with the statement are captured in the audit log.                                                                                                                                                                                                                                                                                                              |
| `pgaudit.log_relation`       | When turned on (set to 1), the audit log for the session creates a separate log entry for each relation (TABLE, VIEW, and so on) referenced in a SELECT or DML statement.                                                                                                                                                                                                                                   |
| `pgaudit.log_statement_once` | Specifies whether logging will include the statement text and parameters with the first log entry for a statement/substatement combination or with every entry.                                                                                                                                                                                                                                             |
| `pgaudit.role`               | Specifies the master role to use for object audit logging. The only allowable entry is `rds_pgaudit`.                                                                                                                                                                                                                                                                                                       |

## List of allowable settings for the `pgaudit.log` parameter

| Value    | Description                                                                                                                  |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| none     | This is the default. No database changes are logged.                                                                         |
| all      | Logs everything (read, write, function, role, ddl, misc).                                                                    |
| ddl      | Logs all data definition language (DDL) statements that<br>aren't included in the `ROLE` class.                              |
| function | Logs function calls and `DO` blocks.                                                                                         |
| misc     | Logs miscellaneous commands, such as `DISCARD`, `FETCH`,<br>`CHECKPOINT`, `VACUUM`, and `SET`.                               |
| read     | Logs `SELECT` and `COPY` when the source is a relation (such<br>as a table) or a query.                                      |
| role     | Logs statements related to roles and privileges, such as<br>`GRANT`, `REVOKE`, `CREATE ROLE`, `ALTER ROLE`, and `DROP ROLE`. |
| write    | Logs `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`,<br>and `COPY` when the destination is a relation (table).                     |

To log multiple event types with session auditing, use a comma-separated list. To log all event types,
set `pgaudit.log` to `ALL`. Reboot your DB instance to apply the changes.

With object auditing, you can refine audit logging to work with specific relations. For
example, you can specify that you want audit logging for `READ` operations on one or more tables.
