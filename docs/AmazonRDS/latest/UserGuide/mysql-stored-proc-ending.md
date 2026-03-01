# Ending a session or query

The following stored procedures end a session or query.

###### Topics

- [mysql.rds_kill](#mysql_rds_kill "#mysql_rds_kill")
- [mysql.rds_kill_query](#mysql_rds_kill_query "#mysql_rds_kill_query")

## mysql.rds_kill

Ends a connection to the MySQL server.

### Syntax

```
CALL mysql.rds_kill(`processID`);
```

### Parameters

`processID`

The identity of the connection thread to be ended.

### Usage notes

Each connection to the MySQL server runs in a separate thread. To end a
connection, use the `mysql.rds_kill` procedure and pass in the thread ID
of that connection. To obtain the thread ID, use the MySQL [SHOW
PROCESSLIST](https://dev.mysql.com/doc/refman/8.0/en/show-processlist.html "https://dev.mysql.com/doc/refman/8.0/en/show-processlist.html") command.

For information about limitations, see [MySQL stored procedure limitations](MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.KillProcedures "MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.KillProcedures").

### Examples

The following example ends a connection with a thread ID of 4243:

```
CALL mysql.rds_kill(4243);
```

## mysql.rds_kill_query

Ends a query running against the MySQL server.

### Syntax

```
CALL mysql.rds_kill_query(`processID`);
```

### Parameters

`processID`

The identity of the process or thread that is running the query to be
ended.

### Usage notes

To stop a query running against the MySQL server, use the
`mysql_rds_kill_query` procedure and pass in the connection ID of the
thread that is running the query. The procedure then terminates the
connection.

To obtain the ID, query the MySQL [INFORMATION_SCHEMA PROCESSLIST table](https://dev.mysql.com/doc/refman/8.0/en/information-schema-processlist-table.html "https://dev.mysql.com/doc/refman/8.0/en/information-schema-processlist-table.html") or use the MySQL [SHOW
PROCESSLIST](https://dev.mysql.com/doc/refman/8.0/en/show-processlist.html "https://dev.mysql.com/doc/refman/8.0/en/show-processlist.html") command. The value in the ID column from `SHOW
 PROCESSLIST` or `SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST`
is the `processID`.

For information about limitations, see [MySQL stored procedure limitations](MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.KillProcedures "MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.KillProcedures").

### Examples

The following example stops a query with a query thread ID of 230040:

```
CALL mysql.rds_kill_query(230040);
```
