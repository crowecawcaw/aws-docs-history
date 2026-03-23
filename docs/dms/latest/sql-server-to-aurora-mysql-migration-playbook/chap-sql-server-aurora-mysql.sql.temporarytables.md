# Temporary tables for ANSI SQL

This topic provides reference content for temporary table functionality between Microsoft SQL Server and MySQL, specifically in the context of migrating from SQL Server 2019 to Amazon Aurora MySQL. You’ll gain insight into how temporary tables are created, stored, and managed in both database systems.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Three star feature compatibility | Three star automation level        | N/A                       | N/A             |

## SQL Server Usage

SQL Server temporary tables are stored in the `tempdb` system database. There are two types of temporary tables: local and global. They differ from each other in their names, their visibility, and their availability. Local temporary tables have a single number sign `#` as the first character of their names; they are visible only to the current connection for the user, and they are deleted when the user disconnects from the instance of SQL Server.

Global temporary tables have two number signs `##` as the first characters of their names; they are visible to any user after they are created, and they are deleted when all users referencing the table disconnect from the instance of SQL Server.

```
CREATE TABLE #MyTempTable (col1 INT PRIMARY KEY);
```

For more information, see [Tables](https://docs.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/tables/tables?view=sql-server-ver15") and [Temporary Tables](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?redirectedfrom=MSDN&view=sql-server-ver15#temporary-tables "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?redirectedfrom=MSDN&view=sql-server-ver15#temporary-tables") in the _SQL Server documentation_.

## MySQL Usage

In MySQL, the table structure (DDL) of temporary tables isn’t stored in the database. When a session ends, the temporary table is dropped.

- **Session-Specific** — In MySQL, each session is required to create its own temporary tables. Each session can create its own private temporary tables using identical table names.
- **In SQL Server**, the default behavior when the `ON COMMIT` clause is omitted is `ON COMMIT DELETE ROWS`. In MySQL, the default is `ON COMMIT PRESERVE ROWS` and it can’t be changed.

###### Note

In Amazon Relational Database Service (Amazon RDS) for MySQL 8.0.13, user-created temporary tables and internal temporary tables created by the optimizer are stored in session temporary tablespaces that are allocated to a session from a pool of temporary tablespaces. When a session disconnects its temporary tablespaces are truncated and released back to the pool. In previous releases temporary tables were created in the `ibtmp1` global temporary tablespace which did not return disk space to the operating system after temporary tables were dropped. The `innodb_temp_tablespaces_dir` variable defines the location where session temporary tablespaces are created. The default location is the `#innodb_temp` directory in the data directory. The `INNODB_SESSION_TEMP_TABLESPACES` table provides metadata about session temporary tablespaces. The `ibtmp1` global temporary tablespace now stores rollback segments for changes made to user-created temporary tables.

### Examples

```
CREATE TEMPORARY TABLE EMP_TEMP (
    EMP_ID INT PRIMARY KEY,
    EMP_FULL_NAME VARCHAR(60) NOT NULL,
    AVG_SALARY INT NOT NULL1;
```

## Summary

| Feature                                                                                  | SQL Server                      | Aurora MySQL                           |
| ---------------------------------------------------------------------------------------- | ------------------------------- | -------------------------------------- |
| Semantic                                                                                 | Global temporary table          | Temporary table                        |
| Create table                                                                             | `CREATE GLOBAL TEMPORARY…`      | `CREATE TEMPORARY…`                    |
| Accessible from multiple sessions                                                        | Yes                             | No                                     |
| Temporary table DDL persist after session end or database restart user-managed datafiles | Yes                             | No (dropped at the end of the session) |
| Create index support                                                                     | Yes                             | Yes                                    |
| Foreign key support                                                                      | Yes                             | Yes                                    |
| `ON COMMIT` default                                                                      | `COMMIT DELETE ROWS`            | `ON COMMIT PRESERVE ROWS`              |
| `ON COMMIT PRESERVE ROWS`                                                                | Yes                             | Yes                                    |
| `ON COMMIT DELETE ROWS`                                                                  | Yes                             | Yes                                    |
| Alter table support                                                                      | Yes                             | Yes                                    |
| Gather statistics                                                                        | `dbms_stats.gather_table_stats` | `ANALYZE`                              |
| Oracle 12c `GLOBAL_TEMP_TABLE_STATS`                                                     | `dbms_stats.set_table_prefs`    | `ANALYZE`                              |

For more information, see [CREATE TEMPORARY TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-temporary-table.html "https://dev.mysql.com/doc/refman/5.7/en/create-temporary-table.html") in the _MySQL documentation_.
