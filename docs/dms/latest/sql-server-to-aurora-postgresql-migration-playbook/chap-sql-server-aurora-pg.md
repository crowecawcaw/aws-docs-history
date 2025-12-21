# SQL Server 2018 deprecated features list

This topic provides reference information related to migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. It covers a range of database concepts and features that differ between the two systems, including data types, table creation, maintenance operations, and query syntax. You’ll find information on how various SQL Server constructs and functionalities map to their PostgreSQL equivalents or alternatives.

| SQL Server 2018 deprecated feature                        | Section                                                                                                    |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `TEXT`, `NTEXT`, and `IMAGE` data types                   | [Data Types](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md")                          |
| `SET ROWCOUNT` for DML                                    | [Session Options](chap-sql-server-aurora-pg.configuration.md "chap-sql-server-aurora-pg.configuration.md") |
| `TIMESTAMP` syntax for `CREATE TABLE`                     | [Creating Tables](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md")                     |
| `DBCC DBREINDEX`, `INDEXDEFRAG`, and `SHOWCONTIG`         | [Maintenance Plans](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md")     |
| Old SQL Mail                                              | [Database Mail](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md")         |
| `IDENTITY` seed, increment, non primary key, and compound | [Sequences and Identity](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md")            |
| Stored procedures `RETURN` values                         | [Stored Procedures](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md")                 |
| `GROUP BY ALL`, `Cube`, and `Compute By`                  | [GROUP BY](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md")                            |
| DTS                                                       | [ETL](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md")                   |
| Old outer join syntax `**=**` and `=`                     | [Table JOIN](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md")                          |
| `'String Alias' = Expression`                             | [Migration Quick Tips](chap-sql-server-aurora-pg.md "chap-sql-server-aurora-pg.md")                        |
| `DEFAULT` keyword for `INSERT` statements                 | [Migration Quick Tips](chap-sql-server-aurora-pg.md "chap-sql-server-aurora-pg.md")                        |
