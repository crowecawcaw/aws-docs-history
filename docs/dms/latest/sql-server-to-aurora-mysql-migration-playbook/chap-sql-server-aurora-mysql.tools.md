# AWS SCT action code index

This topic provides reference information for the automation levels and action codes used by AWS Schema Conversion Tool (AWS SCT) when migrating from Microsoft SQL Server 2019 to Amazon Aurora MySQL. You can use this information to understand the degree of automation available for various database objects and features during the migration process.

The following table shows the icons we use to describe the automation levels of AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS).

| Automation level icon       | Description                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Five star automation level  | \*_Full automation_<br>• — AWS SCT performs fully automatic conversion, no manual conversion needed.         |
| Four star automation level  | \*_High automation_<br>• — Minor, simple manual conversions may be needed.                                   |
| Three star automation level | \*_Medium automation_<br>• — Low-medium complexity manual conversions may be needed.                         |
| Two star automation level   | \*_Low automation_<br>• — Medium-high complexity manual conversions may be needed.                           |
| One star automation level   | \*_Very low automation_<br>• — High risk or complex manual conversions may be needed.                        |
| No automation               | \*_No automation_<br>• — Not currently supported by AWS SCT, manual conversion is required for this feature. |

The following sections list the AWS Schema Conversion Tool action codes for topics that are covered in this playbook.

###### Note

The links in the table point to the Microsoft SQL Server topic pages, which are immediately followed by the MySQL pages for the same topics.

## Creating Tables

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used constructs of the `CREATE TABLE` statement as both SQL Server and Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) support the entry level American National Standards Institute (ANSI) compliance. These items include table names, containing security schema or database, column names, basic column data types, column and table constraints, column default values, primary, `UNIQUE`, and foreign keys. Some changes may be required for computed columns and global temporary tables.

For more information, see [Creating Tables](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                                                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 659         | If you use recursion, make sure that table variables in your source database and temporary tables in your target database have the same scope. |
| 679         | AWS SCT replaced computed columns with triggers.                                                                                               |
| 680         | MySQL doesn’t support global temporary tables.                                                                                                 |

## Constraints

![Four star automation level](images/pb-automation-4.png)

AWS Schema Conversion Tool (AWS SCT automatically converts most constraints because SQL Server and Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) support the entry level ANSI compliance. These items include primary keys, foreign keys, null constraints, unique constraints, and default constraints with some exceptions. Manual conversions are required for some foreign key cascading options. AWS SCT replaces check constraints with triggers, and some default expressions for `DateTime` columns aren’t supported for automatic conversion. AWS SCT can’t automatically convert complex expressions for other default values.

For more information, see [Constraints](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------ |
| 676         | MySQL doesn’t support the `SET DEFAULT` referential constraint action.                           |
| 677         | MySQL doesn’t support functions or expressions as a default value for `BLOB` and `TEXT` columns. |
| 678         | MySQL doesn’t support check constraints.                                                         |
| 825         | AWS SCT removed the default value of the ё column.                                               |
| 826         | AWS SCT can’t convert the default value of the ё variable.                                       |
| 827         | AWS SCT can’t convert default values.                                                            |

## Data Types

![Four star automation level](images/pb-automation-4.png)

Data type syntax and rules are very similar between SQL Server and Aurora MySQL. AWS SCT automatically converts most of data type syntax and rules. Note that date and time handling paradigms are different for SQL Server and Aurora MySQL and require manual verification or conversion. Also note that because of differences in data type behavior between SQL Server and Aurora MySQL, manual verification and strict testing are highly recommended.

For more information, see [Data Types](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                                                                                                     |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 601         | MySQL doesn’t support including `BLOB` and `TEXT` columns in foreign keys.                                                         |
| 706         | AWS SCT replaced the unsupported %s data type.                                                                                     |
| 707         | AWS SCT can’t convert the usage of a variable of the unsupported %s data type.                                                     |
| 708         | AWS SCT can’t convert the usage of the unsupported %s data type.                                                                   |
| 775         | Converted code might lose accuracy compared to the source code.                                                                    |
| 844         | AWS SCT expanded fractional seconds support for `TIME`, `DATETIME2`, and `DATETIMEOFFSET` values with up to 6 digits of precision. |
| 919         | MySQL doesn’t support the `DECIMAL` data type with scale greater than 30.                                                          |

## Collations

![Four star automation level](images/pb-automation-4.png)

The collation paradigms of SQL Server and Aurora MySQL are significantly different. AWS SCT can successfully migrate most common use cases including data type differences such as `NCHAR` and `NVARCHAR` in SQL Server that don’t exist in Aurora MySQL. Aurora MySQL provides more options and flexibility in terms of collations. Rewrites are required for explicit collation clauses that aren’t supported by Aurora MySQL.

For more information, see [Collations](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                              |
| ----------- | ------------------------------------------- |
| 646         | MySQL doesn’t support the `COLLATE` clause. |

## Window Functions

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support window functions. AWS SCT can’t automatically convert window functions.

For workarounds using traditional SQL syntax, see [Window Functions](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                                       |
| ----------- | -------------------------------------------------------------------- |
| 647         | MySQL doesn’t support the analytic form of the %s function.          |
| 648         | MySQL doesn’t support the `RANK` function.                           |
| 649         | MySQL doesn’t support the `DENSE_RANK` function.                     |
| 650         | MySQL doesn’t support the `NTILE` function.                          |
| 754         | MySQL doesn’t ssupport `STDEV` functions with the `DISTINCT` clause. |
| 755         | MySQL doesn’t support `STDEVP` functions with the `DISTINCT` clause. |
| 756         | MySQL doesn’t support `VAR` functions with the `DISTINCT` clause.    |
| 757         | MySQL doesn’t support `VARP` functions with the `DISTINCT` clause.   |

## PIVOT and UNPIVOT

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support the `PIVOT` and `UNPIVOT` syntax. AWS SCT can’t automatically convert the PIVOT and UNPIVOT clauses.

For workarounds using traditional SQL syntax, see [PIVOT and UNPIVOT](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                   |
| ----------- | ---------------------------------------------------------------- |
| 905         | MySQL doesn’t support `PIVOT` clauses for `SELECT` statements.   |
| 906         | MySQL doesn’t support `UNPIVOT` clauses for `SELECT` statements. |

## TOP and FETCH

![Four star automation level](images/pb-automation-4.png)

Aurora MySQL supports the non-ANSI compliant (although popular with other common RDBMS engines) `LIMIT…​ OFFSET` operator for paging of results sets. Despite the differences, AWS SCT can automatically convert most common paging queries to use the Aurora MySQL syntax. Some options such as `PERCENT` and `WITH TIES` can’t be automatically converted and require manual conversion.

For more information, see [SQL Server TOP and FETCH and MySQL LIMIT](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------- |
| 604         | MySQL doesn’t support the `PERCENT` argument in `TOP` clauses. AWS SCT skips this argument in the converted code.   |
| 605         | MySQL doesn’t support the `WITH TIES` argument in `TOP` clauses. AWS SCT skips this argument in the converted code. |
| 608         | MySQL doesn’t support the `PERCENT` argument in `TOP` clauses of `INSERT` statements.                               |
| 612         | MySQL doesn’t support the `PERCENT` argument in `TOP` clauses of `UPDATE` statements.                               |
| 621         | MySQL doesn’t support the `PERCENT` argument in TOP clauses. AWS SCT skips this argument in the converted code.     |
| 830         | MySQL doesn’t support `LIMIT` clauses with `IN`, `ALL`, `ANY`, or `SOME` subqueries.                                |

## Common Table Expressions

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support common table expressions. AWS SCT can’t automatically convert common table expressions.

For workarounds using traditional SQL syntax, see [Common Table Expressions](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                                        |
| ----------- | --------------------------------------------------------------------- |
| 611         | MySQL doesn’t support `WITH` queries in `UPDATE` statements.          |
| 619         | MySQL doesn’t support query definitions for common table expressions. |
| 839         | MySQL doesn’t support query definitions for common table expressions. |
| 840         | AWS SCT can’t convert updated common table expressions.               |

## Cursors

![Three star automation level](images/pb-automation-3.png)

AWS SCT automatically converts the most commonly used cursor operations. These operations include forward-only, read only cursors, and the `DECLARE CURSOR`, `CLOSE CURSOR`, and `FETCH NEXT` operations. Modifications through cursors and non-forward-only fetches, which aren’t supported by Aurora MySQL, require manual conversions.

For more information, see [Cursors](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 618         | MySQL doesn’t support `CURRENT OF` clauses for DML queries that are in the body of a cursor loop.                              |
| 624         | MySQL doesn’t support `CURRENT OF` clauses for DML queries that are in the body of a cursor loop.                              |
| 625         | MySQL doesn’t support the `CURSOR` data type as a procedure argument.                                                          |
| 637         | MySQL doesn’t support global cursors.                                                                                          |
| 638         | MySQL doesn’t support the `SCROLL` option in cursors.                                                                          |
| 639         | MySQL doesn’t support dynamic cursors.                                                                                         |
| 667         | MySQL doesn’t support the %s option in cursors.                                                                                |
| 668         | MySQL doesn’t support the `FIRST` option in cursors.                                                                           |
| 669         | MySQL doesn’t support the `PRIOR` option in cursors.                                                                           |
| 670         | MySQL doesn’t support the `ABSOLUTE` option in cursors.                                                                        |
| 671         | MySQL doesn’t support the `RELATIVE` option in cursors.                                                                        |
| 692         | MySQL doesn’t support cursor variables.                                                                                        |
| 700         | AWS SCT can’t convert the `KEYSET` option because MySQL doesn’t support changing the membership and order of rows for cursors. |
| 701         | AWS SCT doesn’t convert the `FAST_FORWARD` option because this is a default option for cursors in MySQL.                       |
| 702         | AWS SCT doesn’t convert the `READ_ONLY` option because this is a default option for cursors in MySQL.                          |
| 703         | MySQL doesn’t support the `SCROLL_LOCKS` option.                                                                               |
| 704         | MySQL doesn’t support the `OPTIMISTIC` option for cursors.                                                                     |
| 705         | MySQL doesn’t support the `TYPE_WARNING` option for cursors.                                                                   |
| 842         | MySQL doesn’t support the %s option in cursors.                                                                                |

## Flow Control

![Four star automation level](images/pb-automation-4.png)

Although the flow control syntax of SQL Server differs from Aurora MySQL, AWS SCT can convert most constructs automatically including loops, command blocks, and delays. Aurora MySQL doesn’t support the `GOTO` command nor the `WAITFOR TIME` command, which require manual conversion.

For more information, see [Flow Control](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                    |
| ----------- | ------------------------------------------------- |
| 628         | MySQL doesn’t support `GOTO` statements.          |
| 691         | MySQL doesn’t support the `WAITFOR TIME` feature. |

## Transaction Isolation

![Four star automation level](images/pb-automation-4.png)

Aurora MySQL supports the following four transaction isolation levels specified in the SQL:92 standard: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`. AWS SCT automatically converts all these transaction isolation levels. AWS SCT also converts `BEGIN`, `COMMIT`, and `ROLLBACK` commands that use slightly different syntax. Manual conversion is required for named, marked, and delayed durability transactions that aren’t supported by Aurora MySQL.

For more information, see [Transactions](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                    |
| ----------- | ----------------------------------------------------------------- |
| 629         | MySQL doesn’t support named transactions.                         |
| 630         | MySQL doesn’t support `WITH MARK` options.                        |
| 631         | MySQL doesn’t support distributed transactions.                   |
| 632         | MySQL doesn’t support rolling back named transactions             |
| 633         | MySQL doesn’t support the `DELAYED_DURABILITY` option.            |
| 916         | MySQL doesn’t support the `SNAPSHOT` transaction isolation level. |

## Stored Procedures

![Four star automation level](images/pb-automation-4.png)

Aurora MySQL stored procedures provide very similar functionality to SQL Server stored procedures. AWS SCT automatically converts SQL Server stored procedures. Manual conversion is required for procedures that use `RETURN` values and some less common `EXECUTE` options such as `RECOMPILE` and `RESULTS SETS`.

For more information, see [Stored Procedures](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                                             |
| ----------- | ------------------------------------------------------------------------------------------ |
| 640         | MySQL doesn’t support `EXECUTE` statements with the `WITH RECOMPILE` option.               |
| 641         | MySQL doesn’t support `EXECUTE` statements with the `RESULT SETS UNDEFINED` option.        |
| 642         | MySQL doesn’t support `EXECUTE` statements with the `RESULT SETS NONE` option.             |
| 643         | MySQL doesn’t support `EXECUTE` statements with the `RESULT SETS DEFINITION` option.       |
| 689         | MySQL doesn’t support `RETURN` statements that are used to return values from a procedure. |
| 695         | MySQL doesn’t support the call of a procedure as a variable.                               |

## Triggers

![Three star automation level](images/pb-automation-3.png)

Aurora MySQL supports `BEFORE` and `AFTER` triggers for `INSERT`, `UPDATE`, and `DELETE`. However, Aurora MySQL triggers differ substantially from SQL Server triggers, but most common use cases can be migrated with minimal code changes. Although AWS SCT can automatically migrate trigger code, manual inspection and potential code modifications may be required because Aurora MySQL triggers are ran once for each row, not once for each statement such as triggers in SQL Server.

For more information, see [Triggers](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                  |
| ----------- | --------------------------------------------------------------- |
| 686         | MySQL doesn’t support triggers with the `FOR STATEMENT` clause. |

## GROUP BY

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the `GROUP BY` queries, except for `CUBE` and `GROUPING SETS`. You can create workarounds for these queries, but they require manual code changes.

For more information, see [GROUP BY](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                          |
| ----------- | ------------------------------------------------------- |
| 654         | MySQL doesn’t support the `GROUP BY CUBE` option.       |
| 655         | MySQL doesn’t support `GROUP BY GROUPING SETS` clauses. |

## Identity and Sequences

![Three star automation level](images/pb-automation-3.png)

Although the syntax for SQL Server `IDENTITY` and Aurora MySQL
`AUTO_INCREMENT` auto-enumeration columns differs significantly, it can be automatically converted by AWS SCT. Some limitations imposed by Aurora MySQL require manual conversion such as explicit `SEED` and `INCREMENT` auto-enumeration columns that aren’t part of the primary key and the table-independent `SEQUENCE` objects.

For more information, see [Identity and Sequences](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                                                                                                                              |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 696         | MySQL doesn’t support identity columns with seed and increment.                                                                                                             |
| 697         | MySQL doesn’t support identity columns outside the primary key.                                                                                                             |
| 732         | MySQL doesn’t support identity columns in compound primary keys.                                                                                                            |
| 815         | MySQL doesn’t support sequences.                                                                                                                                            |
| 841         | MySQL doesn’t support numeric (x, 0) or decimal (x, 0) data types in columns with the `AUTO_INCREMENT` option. AWS SCT replaced this data type with a compatible data type. |
| 920         | MySQL doesn’t support identity columns of the `DECIMAL` or `NUMERIC` data type with precision greater than 19.                                                              |

## Error Handling

![Three star automation level](images/pb-automation-3.png)

The error handling paradigms in Aurora MySQL and SQL Server are significantly different; the former uses condition and handler objects. AWS SCT migrates the basic error handling constructs automatically. Due to the paradigm differences, we highly recommend that you perform strict inspection and validation of the migrated code. Manual conversions are required for `THROW` with variables and for built-in messages in SQL Server.

For more information, see [Error Handling](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                                             |
| ----------- | ------------------------------------------------------------------------------------------ |
| 729         | AWS SCT can’t convert `THROW` operators with variables.                                    |
| 730         | AWS SCT truncated the error code.                                                          |
| 733         | MySQL doesn’t support `PRINT` procedures.                                                  |
| 814         | AWS SCT can’t convert the `RAISERROR` operator with messages from the `sys.messages` view. |
| 837         | MySQL uses a different approach to handle errors compared to the source code.              |

## Date and Time Functions

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used date and time functions despite the significant difference in syntax. Be aware of differences in data types, time zone awareness, and locale handling as well the functions themselves, and inspect the expression value output carefully. Some less commonly used options such as millisecond, nanosecond, and time zone offsets require manual conversion.

For more information, see [Date and Time Functions](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                             |
| ----------- | -------------------------------------------------------------------------- |
| 759         | MySQL doesn’t support `DATEADD` functions with the nanosecond date part.   |
| 760         | MySQL doesn’t support `DATEDIFF` functions with the week date part.        |
| 761         | MySQL doesn’t support `DATEDIFF` functions with the millisecond date part. |
| 762         | MySQL doesn’t support `DATEDIFF` functions with the nanosecond date part.  |
| 763         | MySQL doesn’t support `DATENAME` functions with the millisecond date part. |
| 764         | MySQL doesn’t support `DATENAME` functions with the nanosecond date part.  |
| 765         | MySQL doesn’t support `DATENAME` functions with the TZoffset date part.    |
| 767         | MySQL doesn’t support `DATEPART` functions with the nanosecond date part.  |
| 768         | MySQL doesn’t support `DATEPART` functions with the TZoffset date part.    |
| 773         | AWS SCT can’t convert arithmetic operations with dates.                    |

## User-Defined Functions

![Three star automation level](images/pb-automation-3.png)

Aurora MySQL supports only scalar user-defined functions, which are automatically converted by AWS SCT. Table-valued user-defined functions, both in-line and multi-statement, require manual conversion. Workarounds using views or derived tables should be straightforward in most cases.

For more information, see [User-Defined Functions](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| 777         | AWS SCT can’t emulate a table-valued function because the column from the current query is used as a function parameter. |
| 822         | MySQL doesn’t support table-valued functions in views.                                                                   |

## User-Defined Types

![Three star automation level](images/pb-automation-3.png)

Aurora MySQL 5.7 doesn’t support-user defined types and user-defined table-valued parameters. AWS SCT can convert standard user defined types by replacing it with their base types, but manual conversion is required for user defined table types, which are used for table valued parameters for stored procedures.

For more information, see [User-Defined Types](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                     |
| ----------- | ---------------------------------- |
| 690         | MySQL doesn’t support table types. |

## Synonyms

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support synonyms. AWS SCT can’t automatically convert synonyms.

For more information, see [Synonyms](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                  |
| ----------- | ------------------------------- |
| 792         | MySQL doesn’t support synonyms. |

## XML and JSON

![Four star automation level](images/pb-automation-4.png)

Aurora MySQL provides minimal support for XML, but it does offer a native JSON data type and more than 25 dedicated JSON functions. Despite these differences, the most commonly used basic XML functions can be automatically migrated by AWS SCT. Some options such as `EXPLICIT`, used in functions or with subqueries, require manual conversion.

For more information, see [JSON and XML](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                                          |
| ----------- | ----------------------------------------------------------------------- |
| 817         | AWS SCT can’t convert `FOR XML` clauses with `EXPLICIT` mode specified. |
| 818         | AWS SCT can’t convert correlated subqueries with `FOR XML` clauses.     |
| 843         | AWS SCT can’t convert `FOR XML` statements in functions.                |

## Table Joins

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used join types. These types include `INNER`, `OUTER`, and `CROSS` joins. `APPLY` joins, also known as `LATERAL` joins, aren’t supported by Aurora MySQL and require manual conversion.

For more information, see [Table JOIN](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 831         | MySQL doesn’t support the `CROSS APPLY` and `OUTER APPLY` operators where the subquery references to the column of attachable table. |

## MERGE

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support the `MERGE` statement. AWS SCT can’t automatically convert `MERGE` statements. Manual conversion is straightforward in most cases.

For more information and potential workarounds, see [MERGE](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                            |
| ----------- | ----------------------------------------- |
| 832         | MySQL doesn’t support `MERGE` statements. |

## Query Hints

![Three star automation level](images/pb-automation-3.png)

Basic query hints such as index hints can be converted automatically by AWS SCT, except for DML statements. Note that specific optimizations used for SQL Server may be completely inapplicable to a new query optimizer. We recommend that you remove all hints before the start of migration testin. Then, selectively apply hints as a last resort if other means such as schema, index, and query optimizations have failed. Plan guides aren’t supported by Aurora MySQL.

For more information, see [Query Hints and Plan Guides](chap-sql-server-aurora-mysql.tuning.md "chap-sql-server-aurora-mysql.tuning.md").

| Action code | Action message                                                                                                              |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| 610         | MySQL doesn’t support hints in `INSERT` statements. AWS SCT skips `WITH(Table_Hint_Limited)` options in the converted code. |
| 617         | MySQL doesn’t support hints in `UPDATE` statements. AWS SCT skips `WITH(Table_Hint_Limited)` options in the converted code. |
| 623         | MySQL doesn’t support hints in `DELETE` statements. AWS SCT skips `WITH(Table_Hint_Limited)` options in the converted code. |
| 823         | MySQL doesn’t support table hints in DML statements.                                                                        |

## Full-Text Search

![No automation](images/pb-automation-0.png)

Migrating full-text indexes from SQL Server to Aurora MySQL requires a full rewrite of the code that deals with both creating, managing, and querying of full-text indexes. AWS SCT can’t automatically convert full-text indexes.

For more information, see [Full-Text Search](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

| Action code | Action message                                  |
| ----------- | ----------------------------------------------- |
| 687         | MySQL doesn’t support the `CONTAINS` predicate. |
| 688         | MySQL doesn’t support the `FREETEXT` predicate. |

## Indexes

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts basic non-clustered indexes, which are the most commonly used type of indexes. User-defined clustered indexes aren’t supported by Aurora MySQL because they are always created for the primary key. In addition, filtered indexes, indexes with included columns, and some SQL Server specific index options can’t be migrated automatically and require manual conversion.

For more information, see [Indexes](chap-sql-server-aurora-mysql.md "chap-sql-server-aurora-mysql.md").

| Action code | Action message                                                         |
| ----------- | ---------------------------------------------------------------------- |
| 602         | MySQL has reached the limit of the internal InnoDB maximum key length. |
| 681         | MySQL doesn’t support clustered indexes.                               |
| 682         | MySQL doesn’t support the `INCLUDE` clause in indexes.                 |
| 683         | MySQL doesn’t support the `WHERE` clause in indexes.                   |
| 684         | MySQL doesn’t support the `WITH` clause in indexes.                    |

## Partitioning

![No automation](images/pb-automation-0.png)

Because Aurora MySQL stores each table in its own file, and because file management is performed by AWS and can’t be modified, some of the physical aspects of partitioning in SQL Server don’t apply to Aurora MySQL. For example, the concept of file groups and assigning partitions to file groups. Aurora MySQL supports a much richer framework for table partitioning than SQL Server, with many additional options such as hash partitioning, and sub partitioning. Due to the vast differences between partition creation, query, and management between Aurora MySQL and SQL Server, AWS SCT doesn’t automatically convert table and index partitions. These items require manual conversion.

For more information, see [Storage](chap-sql-server-aurora-mysql.md "chap-sql-server-aurora-mysql.md").

| Action code | Action message                                               |
| ----------- | ------------------------------------------------------------ |
| 907         | AWS SCT can’t convert tables arranged in several partitions. |

## Backup

![No automation](images/pb-automation-0.png)

Migrating from a self-managed backup policy to a Platform as a Service (PaaS) environment such as Aurora MySQL is a complete paradigm shift. You no longer need to worry about transaction logs, file groups, disks running out of space, and purging old backups. Amazon Relational Database Service (Amazon RDS) provides guaranteed continuous backup with point-in-time restore up to 35 days. Therefore, AWS SCT doesn’t automatically convert backups.

For more information, see [Backup and Restore](chap-sql-server-aurora-mysql.hadr.md "chap-sql-server-aurora-mysql.hadr.md").

| Action code | Action message                                                    |
| ----------- | ----------------------------------------------------------------- |
| 903         | MySQL doesn’t support functionality similar to SQL Server Backup. |

## SQL Server Database Mail

![No automation](images/pb-automation-0.png)

Aurora MySQL doesn’t provide native support for sending mail from the database.

For more information and potential workarounds, see [Database Mail](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

| Action code | Action message                                                           |
| ----------- | ------------------------------------------------------------------------ |
| 900         | MySQL doesn’t support functionality similar to SQL Server Database Mail. |

## SQL Server Agent

![No automation](images/pb-automation-0.png)

Aurora MySQL doesn’t provide functionality similar to SQL Server Agent as an external, cross-instance scheduler. However, Aurora MySQL provides a native, in-database scheduler. It is limited to the cluster scope and can’t be used to manage multiple clusters. Therefore, AWS SCT can’t automatically convert Agent jobs and alerts.

For more information, see [SQL Server Agent and MySQL Agent](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

| Action code | Action message                                                   |
| ----------- | ---------------------------------------------------------------- |
| 902         | MySQL doesn’t support functionality similar to SQL Server Agent. |

## Linked Servers

![No automation](images/pb-automation-0.png)

Aurora MySQL doesn’t support remote data access from the database. Connectivity between schemas is trivial, but connectivity to other instances require a custom solution. AWS SCT can’t automatically convert commands on linked servers.

For more information, see [Linked Servers](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

| Action code | Action message                                                         |
| ----------- | ---------------------------------------------------------------------- |
| 645         | MySQL doesn’t support running pass-through commands on linked servers. |

## Views

![Four star automation level](images/pb-automation-4.png)

MySQL views are similar to views in SQL Server. However, there are slight differences between the two, mostly around indexing and triggers on views, and also in the query definition.

For more information, see [Views](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

| Action code | Action message                                                                          |
| ----------- | --------------------------------------------------------------------------------------- |
| 779         | AWS SCT can’t convert `SELECT` statements that contain a subquery in the `FROM` clause. |
