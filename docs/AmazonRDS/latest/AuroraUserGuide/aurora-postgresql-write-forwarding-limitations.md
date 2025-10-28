# Limitations and considerations of local write forwarding in Aurora PostgreSQL

The following limitations currently apply to local write forwarding in Aurora PostgreSQL:

- Local write forwarding is not supported with RDS Proxy.
- Certain statements aren't allowed or can produce stale results when you use them in Aurora PostgreSQL with write forwarding.
  In addition, user defined functions and user defined procedures aren't supported. Thus, the `EnableLocalWriteForwarding` setting is turned off by default for DB clusters. Before turning it on, check
  to make sure that your application code isn't affected by any of these restrictions.
- The following kinds of SQL statements aren't supported with write forwarding:

###### Note

These statements can be implicitly used by you in your application or inferred by the PostgreSQL protocol. For example, PL/SQL exception handling
can result in the use of SAVEPOINT, which is not a supported statement.

    + `ANALYZE`
    + `CLUSTER`
    + `COPY`
    + Cursors – Cursors aren't supported, so make sure to close them before using
     local write forwarding.
    + Data definition language (DDL) statements
    + `GRANT`|`REVOKE`|`REASSIGN OWNED`|`SECURITY LABEL`
    + `LISTEN / NOTIFY`
    + `LOCK`
    + `SAVEPOINT`
    + `SELECT INTO`
    + `SET CONSTRAINTS`
    + Sequence updates: `nextval()`, `setval()`
    + `TRUNCATE`
    + Two-phase commit commands: `PREPARE TRANSACTION`, `COMMIT PREPARED`, `ROLLBACK PREPARED`
    + User defined functions and user defined procedures.
    + `VACUUM`

You can consider using the following SQL statements with write forwarding:

- A DML statement might consist of multiple parts, such as an `INSERT ... SELECT` statement or a `DELETE ...
WHERE` statement. In this case, the entire statement is forwarded to the writer DB instance and run there.
- Data manipulation language (DML) statements, such as `INSERT`,
  `DELETE`, and `UPDATE`.
- `EXPLAIN` statements with the statements in this list.
- `PREPARE` and `EXECUTE` statements.
- `SELECT FOR { UPDATE | NO KEY UPDATE | SHARE | KEY SHARE }` statements.
