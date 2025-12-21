# Oracle and MySQL monitoring

This section provides information about Oracle and MySQL monitoring.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                              |
| -------------------------------- | ---------------------------------- | ------------------------- | ------------------------------------------------------------ |
| Three star feature compatibility | N/A                                | N/A                       | Make sure to change table names in queries when using MySQL. |

## Oracle usage

Oracle provides several built-in views used to monitor the database and query its operational state. You can use these views to track the status of the database, view information about database schema objects, and obtain other information.

The data dictionary is a collection of internal tables and views that supply information about the state and operations of an Oracle database including database status, database schema objects such as tables, views, sequences, and so on, users and security, and physical database structure (datafiles). The contents of the data dictionary are persisted to disk.

Examples of data dictionary views include:

- `DBA_TABLES` — Information about all tables in the current database.
- `DBA_USERS` — Information about all database users.
- `DBA_DATA_FILES` — Information about all physical data files in the database.
- `DBA_TABLESPACES` — Information about all tablespaces in the database.
- `DBA_TAB_COLS` — Information about columns (for all tables) in the database.

###### Note

Data dictionary view names can start with `DBA_*`, `ALL_*`, `USER_*`, depending on the presented level and scope of information (user-level or database-level).

For more information, see [Static Data Dictionary Views](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/static-data-dictionary-views-1.html "https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/static-data-dictionary-views-1.html") in the _Oracle documentation_.

Dynamic performance views (V$ Views) are a collection of views that provide real-time monitoring information about the current state of the database instance configuration, runtime statistics, and operations. These views are continuously updated while the database is running.

Information provided by the dynamic performance views includes session information, memory usage, progress of jobs and tasks, SQL execution state and statistics, and various other metrics.

Common dynamic performance views include:

- `V$SESSION` — Information about all current connected sessions in the instance.
- `V$LOCKED_OBJECT` — Information about all objects in the instance on which active locks exist.
- `V$INSTANCE` — Dynamic instance properties.
- `V$SESSION_LONG_OPS` — Information about certain long-running operations in the database such as queries currently executing.
- `V$MEMORY_TARGET_ADVICE` — Advisory view on how to size the instance memory, based on instance activity and past workloads.

For more information, see [Data Dictionary and Dynamic Performance Views](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/data-dictionary-and-dynamic-performance-views.html#GUID-BDF5B748-EB43-4B48-938E-89099069C3BB "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/data-dictionary-and-dynamic-performance-views.html#GUID-BDF5B748-EB43-4B48-938E-89099069C3BB") in the _Oracle documentation_.

## MySQL usage

MySQL provides two different ways to retrieve information about the state of the database and current activities. The information is similar in nature to the Oracle data dictionary tables and V$ performance views. In addition, Amazon Aurora MySQL provides a Performance insights console for monitoring and analyzing database workloads and troubleshooting performance issues.

### Information schema tables

The information schema consists of views containing information about objects that were created in the current database.

- The information schema is specified by the SQL standard and is supported by MySQL.
- Some of these tables are comparable to Oracle `USER_*` Data Dictionary tables.
- The owner of this schema is the initial database user.
- Since the information schema is defined as part of the SQL standard, it can be expected to remain stable across MySQL versions.

### SHOW command

The `SHOW` command provides information about databases, tables, columns, and status information about the server.

- If the syntax for a `SHOW` statement includes a `LIKE` pattern part, the pattern is a string that can contain the SQL `%` and `_` wildcard characters. The pattern is useful for restricting statement output to matching values.
- The `SHOW` command has more dynamic views such as `PROCESSLIST`.
- Users must have `PROCESS` privilege to query this data.

## Summary

| Information                             | Oracle            | MySQL                                                         |
| --------------------------------------- | ----------------- | ------------------------------------------------------------- |
| Database properties                     | `V$DATABASE`      | `pg_database`                                                 |
| Database sessions                       | `V$SESSION`       | `SHOW PROCESSLIST`                                            |
| Database users                          | `DBA_USERS`       | `mysql.user`                                                  |
| Database tables                         | `DBA_TABLES`      | `information_schema.TABLES`                                   |
| Database data files                     | `DBA_DATA_FILES`  | `information_schema.FILES`                                    |
| Table columns                           | `DBA_TAB_COLS`    | `information_schema.COLUMNS`                                  |
| Database locks                          | `V$LOCKED_OBJECT` | `information_schema.INNODB_LOCKS`                             |
| Currently configured runtime parameters | `V$PARAMETER`     | `SHOW GLOBAL VARIABLES`                                       |
| All system statistics                   | `V$SYSSTAT`       | `information_schema.INNODB_METRICS`                           |
| Privileges on tables                    | `DBA_TAB_PRIVS`   | `information_schema.TABLE_PRIVILEGES`                         |
| Information about IO operations         | `V$SEGSTAT`       | `SHOW STATUS LIKE '%read%';`<br>`SHOW STATUS LIKE '%write%';` |

For more information, see [SHOW Statements](https://dev.mysql.com/doc/refman/5.7/en/show.html "https://dev.mysql.com/doc/refman/5.7/en/show.html") and [INFORMATION_SCHEMA Tables](https://dev.mysql.com/doc/refman/5.7/en/information-schema.html "https://dev.mysql.com/doc/refman/5.7/en/information-schema.html") in the _MySQL documentation_.
