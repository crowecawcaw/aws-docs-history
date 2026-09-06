

# SQL Server 2018 deprecated features list
<a name="chap-sql-server-aurora-pg.deprecatedfeatures"></a>

This topic provides reference information related to migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. It covers a range of database concepts and features that differ between the two systems, including data types, table creation, maintenance operations, and query syntax. You’ll find information on how various SQL Server constructs and functionalities map to their PostgreSQL equivalents or alternatives.


| SQL Server 2018 deprecated feature | Section | 
| --- | --- | 
|  `TEXT`, `NTEXT`, and `IMAGE` data types |  [Data Types](chap-sql-server-aurora-pg.sql.datatypes.md)  | 
|  `SET ROWCOUNT` for DML |  [Session Options](chap-sql-server-aurora-pg.configuration.sessionoptions.md)  | 
|  `TIMESTAMP` syntax for `CREATE TABLE`  |  [Creating Tables](chap-sql-server-aurora-pg.sql.tables.md)  | 
|  `DBCC DBREINDEX`, `INDEXDEFRAG`, and `SHOWCONTIG`  |  [Maintenance Plans](chap-sql-server-aurora-pg.management.maintenanceplans.md)  | 
| Old SQL Mail |  [Database Mail](chap-sql-server-aurora-pg.management.databasemail.md)  | 
|  `IDENTITY` seed, increment, non primary key, and compound |  [Sequences and Identity](chap-sql-server-aurora-pg.tsql.sequences.md)  | 
| Stored procedures `RETURN` values |  [Stored Procedures](chap-sql-server-aurora-pg.tsql.storedprocedures.md)  | 
|  `GROUP BY ALL`, `Cube`, and `Compute By`  |  [GROUP BY](chap-sql-server-aurora-pg.sql.groupby.md)  | 
| DTS |  [ETL](chap-sql-server-aurora-pg.management.etl.md)  | 
| Old outer join syntax ` = ` and `=`  |  [Table JOIN](chap-sql-server-aurora-pg.sql.tablejoin.md)  | 
|  `'String Alias' = Expression`  |  [Migration Quick Tips](chap-sql-server-aurora-pg.tips.md)  | 
|  `DEFAULT` keyword for `INSERT` statements |  [Migration Quick Tips](chap-sql-server-aurora-pg.tips.md)  | 