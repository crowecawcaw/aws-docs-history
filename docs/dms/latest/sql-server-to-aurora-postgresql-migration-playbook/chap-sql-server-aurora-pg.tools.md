# AWS SCT Action Code Index overview

This topic provides reference information for the automation levels and action codes used by AWS Schema Conversion Tool (AWS SCT) when migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can use this information to understand the degree of automation available for various database objects and features during the migration process.

The following table shows the icons we use to describe the automation levels of AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS).

| Automation level icon       | Description                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------ |
| Five star automation level  | **Full automation**. AWS SCT performs fully automatic conversion, no manual conversion needed.         |
| Four star automation level  | **High automation**. Minor, simple manual conversions may be needed.                                   |
| Three star automation level | **Medium automation**. Low-medium complexity manual conversions may be needed.                         |
| Two star automation level   | **Low automation**. Medium-high complexity manual conversions may be needed.                           |
| One star automation level   | **Very low automation**. High risk or complex manual conversions may be needed.                        |
| No automation               | **No automation**. Not currently supported by AWS SCT, manual conversion is required for this feature. |

The following sections list the AWS Schema Conversion Tool Action codes for topics that are covered in this playbook.

###### Note

The links in the table point to the Microsoft SQL Server topic pages, which are immediately followed by the PostgreSQL pages for the same topics.

## Creating Tables

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used constructs of the `CREATE TABLE` statement as both SQL Server and Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) support the entry level American National Standards Institute (ANSI) compliance. These items include table names, containing security schema or database, column names, basic column data types, column and table constraints, column default values, primary, `UNIQUE`, and foreign keys. Some changes may be required for computed columns and global temporary tables.

For more information, see [Creating Tables](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md").

| Action code | Action message                                                                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 7659        | If you use recursion, make sure that table variables in your source database and temporary tables in your target database have the same scope. |
| 7665        | PostgreSQL doesn’t support `FILESTREAM` clauses. AWS SCT skips `FILESTREAM` clauses in the converted code.                                     |
| 7678        | AWS SCT replaced computed columns with regular columns in the converted code.                                                                  |
| 7679        | AWS SCT replaced computed columns with triggers in the converted code.                                                                         |
| 7680        | PostgreSQL doesn’t support global temporary tables.                                                                                            |
| 7812        | Make sure that you remove the temporary table before the end of the function.                                                                  |
| 7835        | PostgreSQL doesn’t support `CREATE TABLE` statements with the `AS FileTable` option.                                                           |

## Data Types

![Four star automation level](images/pb-automation-4.png)

Data type syntax and rules are very similar between SQL Server and Aurora PostgreSQL and most are converted automatically by AWS SCT. Note that date and time handling paradigms are different for SQL Server and Aurora PostgreSQL and require manual verification or conversion. Also note that due to differences in data type behavior between SQL Server and Aurora PostgreSQL, manual verification and strict testing are highly recommended.

For more information, see [Data Types](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md").

| Action code | Action message                                                                       |
| ----------- | ------------------------------------------------------------------------------------ |
| 7657        | PostgreSQL doesn’t support the `hierarchyid` data type.                              |
| 7658        | PostgreSQL doesn’t support the `sql_variant` data type.                              |
| 7662        | PostgreSQL doesn’t support the `geography` data type.                                |
| 7664        | PostgreSQL doesn’t support the `geometry` data type.                                 |
| 7690        | PostgreSQL doesn’t support table types.                                              |
| 7706        | AWS SCT can’t convert the declaration of a variable of the unsupported %s data type. |
| 7707        | AWS SCT can’t convert the usage of a variable of the unsupported %s data type.       |
| 7708        | AWS SCT can’t convert the usage of the unsupported %s data type.                     |
| 7773        | AWS SCT can’t convert arithmetic operations with dates.                              |
| 7775        | Converted code might lose accuracy compared to the source code.                      |

## Collations

![No automation](images/pb-automation-0.png)

The collation paradigms of SQL Server and Aurora PostgreSQL are significantly different. AWS SCT can’t migrate collations automatically to PostgreSQL.

For more information, see [SQL Server Collations and PostgreSQL Encoding](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                    |
| ----------- | --------------------------------- |
| 7646        | AWS SCT can’t convert collations. |

## PIVOT and UNPIVOT

![No automation](images/pb-automation-0.png)

Aurora PostgreSQL version 10 doesn’t support `PIVOT` and `UNPIVOT` clauses. AWS SCT can’t automatically convert `PIVOT` and `UNPIVOT` clauses.

For more information, see [PIVOT and UNPIVOT](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                        |
| ----------- | --------------------------------------------------------------------- |
| 7905        | PostgreSQL doesn’t support `PIVOT` clauses for `SELECT` statements.   |
| 7906        | PostgreSQL doesn’t support `UNPIVOT` clauses for `SELECT` statements. |

## TOP and FETCH

![Four star automation level](images/pb-automation-4.png)

Aurora PostgreSQL supports the non-ANSI compliant but popular with other engines `LIMIT…​ OFFSET` operator for paging results sets. AWS SCT can’t automatically convert some options such as `WITH TIES`. These options require manual conversion.

For more information, see [SQL Server TOP and FETCH and PostgreSQL LIMIT and OFFSET](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                        |
| ----------- | --------------------------------------------------------------------- |
| 7605        | PostgreSQL doesn’t support the `WITH TIES` argument in `TOP` clauses. |
| 7796        | PostgreSQL doesn’t support `TOP` clauses in `UPDATE` statements.      |
| 7798        | PostgreSQL doesn’t support `TOP` clauses in `DELETE` statements.      |
| 7799        | PostgreSQL doesn’t support `TOP` clauses in `INSERT` operators.       |

## Cursors

![Three star automation level](images/pb-automation-3.png)

PostgreSQL has PL/pgSQL cursors that enable you to iterate business logic on rows read from the database. They can encapsulate the query and read the query results a few rows at a time. All access to cursors in PL/pgSQL is performed through cursor variables, which are always of the `refcursor` data type. There are specific options which aren’t supported for automatic conversion by AWS SCT.

For more information, see [Cursors](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                                                                                      |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 7637        | PostgreSQL doesn’t support global cursors.                                                                                          |
| 7639        | PostgreSQL doesn’t support dynamic cursors.                                                                                         |
| 7700        | AWS SCT can’t convert the `KEYSET` option because PostgreSQL doesn’t support changing the membership and order of rows for cursors. |
| 7701        | AWS SCT doesn’t convert the `FAST_FORWARD` option because this is a default option for cursors in PostgreSQL.                       |
| 7702        | AWS SCT doesn’t convert the `READ_ONLY` option because this is a default option for cursors in PostgreSQL.                          |
| 7704        | PostgreSQL doesn’t support the `OPTIMISTIC` option for cursors.                                                                     |
| 7705        | PostgreSQL doesn’t support the `TYPE_WARNING` option for cursors.                                                                   |
| 7803        | PostgreSQL doesn’t support the `FOR UPDATE` option.                                                                                 |

## Flow Control

![Three star automation level](images/pb-automation-3.png)

Although the flow control syntax of SQL Server differs from Aurora PostgreSQL, AWS SCT can convert most constructs automatically including loops, command blocks, and delays. Aurora PostgreSQL doesn’t support the `GOTO` and `WAITFOR TIME` commands, which require manual conversion.

For more information, see [SQL Server Flow Control and PostgreSQL Control Structures](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                                                             |
| ----------- | ---------------------------------------------------------------------------------------------------------- |
| 7628        | PostgreSQL doesn’t support `GOTO` statements.                                                              |
| 7691        | PostgreSQL doesn’t support the `WAITFOR TIME` feature.                                                     |
| 7801        | Make sure that your table isn’t locked by an open cursor.                                                  |
| 7802        | Make sure that you delete the table that you created within the procedure before the end of the procedure. |
| 7810        | PostgreSQL doesn’t support `SET NOCOUNT OFF` statements.                                                   |
| 7821        | AWS SCT can’t convert the `WAITFOR` operator with a variable.                                              |
| 7826        | AWS SCT can’t convert the default value of the `DateTime` variable.                                        |
| 7827        | AWS SCT can’t convert default values.                                                                      |

## Transaction Isolation

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL supports the four transaction isolation levels specified in the SQL:92 standard: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`, all of which are automatically converted by AWS SCT. Also, AWS SCT converts `BEGIN / COMMIT` and `ROLLBACK` commands that use slightly different syntax. Manual conversion is required for named, marked, and delayed durability transactions that aren’t supported by Aurora PostgreSQL.

For more information, see [Transactions](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                                                                                                                                |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7807        | AWS SCT can’t convert the transaction management command. PostgreSQL doesn’t support explicit transaction management commands such as `BEGIN TRAN`, `SAVE TRAN` in functions. |

## Stored Procedures

![Four star automation level](images/pb-automation-4.png)

Aurora PostgreSQL stored procedures provide very similar functionality to SQL Server stored procedures. You can automatically convert them with AWS SCT. Manual conversion is required for procedures that use `RETURN` values and some less common `EXECUTE` options such as the `RECOMPILE` and `RESULTS SETS`.

For more information, see [Stored Procedures](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                                            |
| ----------- | ----------------------------------------------------------------------------------------- |
| 7640        | PostgreSQL doesn’t support `EXECUTE` statements with the `WITH RECOMPILE` option.         |
| 7641        | PostgreSQL doesn’t support `EXECUTE` statements with the `RESULT SETS UNDEFINED` option.  |
| 7642        | PostgreSQL doesn’t support `EXECUTE` statements with the `RESULT SETS NONE` option.       |
| 7643        | PostgreSQL doesn’t support `EXECUTE` statements with the `RESULT SETS DEFINITION` option. |
| 7672        | PostgreSQL doesn’t support `EXECUTE` statements that run a character string.              |
| 7695        | PostgreSQL doesn’t support support the call of a procedure as a variable.                 |
| 7800        | PostgreSQL doesn’t support result sets in the SQL Server style.                           |
| 7830        | AWS SCT can’t convert arithmetic operations with the `CASE` operand.                      |
| 7838        | AWS SCT can’t convert `EXECUTE` statements with `LOGIN` or `USER` options.                |
| 7839        | Converted code might not work correctly because of parameter names.                       |

## Triggers

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL supports `BEFORE` and `AFTER` triggers for `INSERT`, `UPDATE`, and `DELETE`. However, Aurora PostgreSQL triggers differ substantially from SQL Server’s triggers. You can migrate the most common use cases with minimal code changes.

For more information, see [Triggers](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                          |
| ----------- | ----------------------------------------------------------------------- |
| 7809        | PostgreSQL doesn’t support `INSTEAD OF` triggers on tables.             |
| 7832        | AWS SCT can’t convert `INSTEAD OF` triggers on views.                   |
| 7909        | AWS SCT can’t convert `UPDATE(column)` or `COLUMNS_UPDATED` statements. |

## MERGE

![No automation](images/pb-automation-0.png)

Aurora PostgreSQL version 10 doesn’t support `MERGE` statements. AWS SCT can’t automatically convert these statements. Manual conversion is straightforward in most cases.

For more information, see [MERGE](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                                                                                    |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 7915        | Converted code might produce different results compared to the source code. Make sure that the constraint includes the %s column. |
| 7916        | AWS SCT can’t emulate the `MERGE` statement using the `INSERT ON CONFLICT` statement.                                             |

## Query Hints

![Three star automation level](images/pb-automation-3.png)

You can use AWS SCT to convert basic query hints such as index hints, except for data manipulation language (DML) statements. Note that specific optimizations used for SQL Server may be completely inapplicable to a new query optimizer. AWS recommends to start migration testing with all hints removed. Then, selectively apply hints as a last resort if other means such as schema, index, and query optimizations have failed. Plan guides aren’t supported by Aurora PostgreSQL.

For more information, see [SQL Server Query Hints and Plan Guides and PostgreSQL DB Query Planning](chap-sql-server-aurora-pg.tuning.md "chap-sql-server-aurora-pg.tuning.md").

| Action code | Action message                                            |
| ----------- | --------------------------------------------------------- |
| 7823        | PostgreSQL doesn’t support table hints in DML statements. |

## Full-Text Search

![No automation](images/pb-automation-0.png)

Migrating full-text indexes from SQL Server to Aurora PostgreSQL requires a full rewrite of the code that deals with both creating, managing, and querying full-text indexes. AWS SCT can’t automatically convert these statements.

For more information, see [Full-Text Search](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                    |
| ----------- | ------------------------------------------------- |
| 7688        | PostgreSQL doesn’t support `FREETEXT` predicates. |

## Indexes

![Three star automation level](images/pb-automation-3.png)

Basic non-clustered indexes, which are the most commonly used type of indexes are automatically migrated by AWS SCT. In addition, filtered indexes, indexes with included columns, and some SQL Server specific index options can’t be migrated automatically and require manual conversion.

For more information, see [Indexes](chap-sql-server-aurora-pg.md "chap-sql-server-aurora-pg.md").

| Action code | Action message                                                               |
| ----------- | ---------------------------------------------------------------------------- |
| 7675        | PostgreSQL doesn’t support `ASC` and `DESC` sorting options for constraints. |
| 7681        | PostgreSQL doesn’t support clustered indexes.                                |
| 7682        | PostgreSQL doesn’t support the `INCLUDE` option in indexes.                  |
| 7781        | PostgreSQL doesn’t support the `PAD_INDEX` option in indexes.                |
| 7782        | PostgreSQL doesn’t support the `SORT_IN_TEMPDB` option in indexes.           |
| 7783        | PostgreSQL doesn’t support the `IGNORE_DUP_KEY` option in indexes.           |
| 7784        | PostgreSQL doesn’t support the `STATISTICS_NORECOMPUTE` option in indexes.   |
| 7785        | PostgreSQL doesn’t support the `STATISTICS_INCREMENTAL` option in indexes.   |
| 7786        | PostgreSQL doesn’t support the `DROP_EXISTING` option in indexes.            |
| 7787        | PostgreSQL doesn’t support the `ONLINE` option in indexes.                   |
| 7788        | PostgreSQL doesn’t support the `ALLOW_ROW_LOCKS` option in indexes.          |
| 7789        | PostgreSQL doesn’t support the `ALLOW_PAGE_LOCKS` option in indexes.         |
| 7790        | PostgreSQL doesn’t support the `MAXDOP` option in indexes.                   |
| 7791        | PostgreSQL doesn’t support the `DATA_COMPRESSION` option in indexes.         |

## Partitioning

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL uses table inheritance, some of the physical aspects of partitioning in SQL Server don’t apply to Aurora PostgreSQL. For example, the concept of file groups and assigning partitions to file groups. Aurora PostgreSQL supports a much richer framework for table partitioning than SQL Server, with many additional options such as hash partitioning, and sub partitioning.

For more information, see [SQL Server Partitioning and PostgreSQL Partitions or Table Inheritance](chap-sql-server-aurora-pg.storage.md "chap-sql-server-aurora-pg.storage.md").

| Action code | Action message                                                                             |
| ----------- | ------------------------------------------------------------------------------------------ |
| 7910        | PostgreSQL doesn’t support `NULL` columns for partitioning.                                |
| 7911        | PostgreSQL doesn’t support foreign keys referencing partitioned tables.                    |
| 7912        | PostgreSQL doesn’t support foreign key references from partitioned tables to other tables. |
| 7913        | PostgreSQL doesn’t support `LEFT` partitioning.                                            |
| 7914        | Converted code might produce different results compared to the source code.                |

Starting from version 11, PostgreSQL supports `NULL` columns for partitioning. In this case, you can ignore the action item with the 7910 code and use `NULL` columns for partitioning in your target tables.

## Backup

![No automation](images/pb-automation-0.png)

Migrating from a self-managed backup policy to a Platform as a Service (PaaS) environment such as Aurora PostgreSQL is a complete paradigm shift. You don’t need to worry about transaction logs, file groups, disks running out of space, and purging old backups. Amazon Relational Database Service (Amazon RDS) provides guaranteed continuous backup with point in time restore up to 35 days. Therefore, AWS SCT doesn’t automatically convert backups.

For more information, see [Backup and Restore](chap-sql-server-aurora-pg.hadr.md "chap-sql-server-aurora-pg.hadr.md").

| Action code | Action message                                                         |
| ----------- | ---------------------------------------------------------------------- |
| 7903        | PostgreSQL doesn’t support functionality similar to SQL Server Backup. |

## SQL Server Mail

![No automation](images/pb-automation-0.png)

Aurora PostgreSQL doesn’t provide native support for sending emails from the database.

For more information, see [Database Mail](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").

| Action code | Action message                                                                |
| ----------- | ----------------------------------------------------------------------------- |
| 7900        | PostgreSQL doesn’t support functionality similar to SQL Server Database Mail. |

## Graph

![No automation](images/pb-automation-0.png)

AWS SCT doesn’t convert graph database capabilities.

For more information and potential workarounds, see [SQL Server Graph and PostgreSQL Apache AGE Extension](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                               |
| ----------- | ------------------------------------------------------------ |
| 7931        | AWS SCT can’t convert SQL Graph tables.                      |
| 7932        | AWS SCT can’t convert DML constructs of SQL Graph databases. |

## SQL Server Agent

![No automation](images/pb-automation-0.png)

Aurora PostgreSQL doesn’t provide functionality similar to SQL Server Agent as an external, cross-instance scheduler. However, Aurora PostgreSQL provides a native, in-database scheduler. It is limited to the cluster scope and can’t be used to manage multiple clusters. Therefore, AWS SCT can’t automatically convert Agent jobs and alerts.

For more information, see [SQL Server Agent and PostgreSQL Scheduled Lambda](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").

| Action code | Action message                                                        |
| ----------- | --------------------------------------------------------------------- |
| 7902        | PostgreSQL doesn’t support functionality similar to SQL Server Agent. |

## Service Broker

![No automation](images/pb-automation-0.png)

Aurora PostgreSQL doesn’t provide a compatible solution to the SQL Server Service Broker. However, you can use DB Links and AWS Lambda to achieve similar functionality.

For more information, see [SQL Server Service Broker Essentials](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                                 |
| ----------- | ------------------------------------------------------------------------------ |
| 7901        | PostgreSQL doesn’t support functionality similar to SQL Server Service Broker. |

## XML

![Three star automation level](images/pb-automation-3.png)

The XML options and features in Aurora PostgreSQL are similar or almost identical to SQL Server `XPATH` and `XQUERY` functions. PostgreSQL doesn’t support `FOR` XML clause, the walkaround for that is using `string_agg` instead. In some cases, it might be more efficient to use JSON instead of XML.

For more information, see [JSON and XML](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                                                          |
| ----------- | ----------------------------------------------------------------------- |
| 7816        | PostgreSQL doesn’t support methods for the XML data type.               |
| 7817        | PostgreSQL doesn’t support the `FOR XML PATH` option in SQL queries.    |
| 7920        | PostgreSQL doesn’t support `EXPLICIT` mode with `FOR XML`.              |
| 7924        | PostgreSQL doesn’t support XPath queries that return multiple elements. |

## Constraints

![Four star automation level](images/pb-automation-4.png)

Constraints feature is almost fully automated and compatible between SQL Server and Aurora PostgreSQL. The differences are: missing `SET DEFAULT` and check constraint with sub-query.

For more information, see [SQL Server Constraints and PostgreSQL Table Constraints](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md").

| Action code | Action message                                                                                                                    |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 7606        | PostgreSQL doesn’t support foreign keys that reference partitioned tables.                                                        |
| 7675        | PostgreSQL doesn’t support `ASC` and `DESC` sorting options for constraints.                                                      |
| 7825        | AWS SCT removed the default value of the `DateTime` column.                                                                       |
| 7915        | Converted code might produce different results compared to the source code. Make sure that the constraint includes the %s column. |

## Linked Servers

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL supports remote data access from the database. Connectivity between schemas is trivial, but connectivity to other instances require an extension installation.

For more information, see [SQL Server Linked Servers and PostgreSQL DBLink and FDWrapper](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").

| Action code | Action message                                                              |
| ----------- | --------------------------------------------------------------------------- |
| 7645        | PostgreSQL doesn’t support running pass-through commands on linked servers. |

## Synonyms

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL supports synonyms. If synonyms refer to tables, views, or functions, you can replace them with views or functions to wrap those. It becomes more challenging when synonyms refer to other objects.

For more information, see [SQL Server Synonyms and PostgreSQL Views, Types, and Functions](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

| Action code | Action message                       |
| ----------- | ------------------------------------ |
| 7792        | PostgreSQL doesn’t support synonyms. |
