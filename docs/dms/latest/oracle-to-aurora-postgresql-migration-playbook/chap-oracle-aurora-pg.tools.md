# AWS SCT action code index

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

The links in the table point to the Oracle topic pages, which are immediately followed by the PostgreSQL pages for the same topics.

## SQL

![Three star automation level](images/pb-automation-3.png)

AWS SCT automatically converts the most commonly used SQL statements as both Oracle and Aurora PostgreSQL support the entry level ANSI compliance, some changes may be required for DML related to `ERROR LOG`, subquery, or partitions.

| Action code | Action message                                                                                                    |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 5024        | PostgreSQL doesn’t support `INSERT` statements that have a partition name or partition key value.                 |
| 5064        | PostgreSQL doesn’t support `UPDATE` statements with the `ERROR LOG` option.                                       |
| 5065        | PostgreSQL doesn’t support the `UPDATE` statement for subqueries.                                                 |
| 5067        | PostgreSQL doesn’t support `DELETE` statements with the `ERROR LOG` option.                                       |
| 5068        | PostgreSQL doesn’t support the `DELETE` statement for a subqueries.                                               |
| 5070        | PostgreSQL doesn’t support `INSERT` statements with the `ERROR LOG` option.                                       |
| 5071        | PostgreSQL doesn’t support the `INSERT` statement for subqueries.                                                 |
| 5087        | PostgreSQL doesn’t support `RETURNING BULK COLLECT INTO` clauses.                                                 |
| 5088        | PostgreSQL doesn’t support `EXECUTE IMMEDIATE` statements with the `BULK COLLECT` clause.                         |
| 5090        | PostgreSQL doesn’t support `INSERT` statements for a `SUBPARTITION`.                                              |
| 5098        | PostgreSQL doesn’t support `DELETE` statements for a `PARTITION`.                                                 |
| 5126        | PostgreSQL doesn’t support `MODEL` statements.                                                                    |
| 5139        | PostgreSQL doesn’t support `FOR UPDATE SKIP LOCKED`.                                                              |
| 5140        | PostgreSQL doesn’t support `BULK COLLECT INTO`.                                                                   |
| 5144        | PostgreSQL doesn’t support `FOR UPDATE WAIT`.                                                                     |
| 5334        | AWS SCT can’t convert statements with dynamic SQL.                                                                |
| 5352        | PostgreSQL doesn’t support synonyms.                                                                              |
| 5353        | PostgreSQL doesn’t support the usage of synonyms.                                                                 |
| 5557        | PostgreSQL doesn’t support the `GROUPING SETS`, `CUBE`, and `ROLLUP` functions.                                   |
| 5558        | PostgreSQL doesn’t support `UPDATE` statements for partitions.                                                    |
| 5578        | AWS SCT can’t convert the `SELECT` statement.                                                                     |
| 5585        | AWS SCT can’t convert outer joins into correlated subqueries.                                                     |
| 5608        | AWS SCT can’t convert `UPDATE` statements that have a subquery that returns multiple columns in the `SET` clause. |
| 5663        | PostgreSQL doesn’t explicitly support autonomous transactions.                                                    |

## Creating tables

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used constructs of the `CREATE TABLE` statement as both Oracle and Aurora PostgreSQL support the entry level ANSI compliance. These items include table names, containing security schema (or database), column names, basic column data types, column and table constraints, column default values, primary, candidate (UNIQUE), and foreign keys. Some changes may be required for computed columns and global temporary tables.

| Action code | Action message                                                                                                              |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| 5196        | PostgreSQL doesn’t support `OBJECT TABLE`.                                                                                  |
| 5198        | PostgreSQL doesn’t support `GLOBAL TEMPORARY TABLE`.                                                                        |
| 5199        | PostgreSQL doesn’t support `CLUSTERED TABLE`.                                                                               |
| 5200        | PostgreSQL doesn’t support `EXTERNAL TABLES`.                                                                               |
| 5201        | PostgreSQL doesn’t support this partition type.                                                                             |
| 5212        | PostgreSQL doesn’t support the `BFILE` data type.                                                                           |
| 5213        | PostgreSQL ensures support of microseconds for time, datetime, and timestamp data types.                                    |
| 5298        | PostgreSQL doesn’t support `DROP STORAGE` clauses in the `TRUNCATE` statement.                                              |
| 5299        | PostgreSQL doesn’t support `REUSE STORAGE` clauses in the `TRUNCATE` statement.                                             |
| 5300        | PostgreSQL doesn’t support `PRESERVE` clauses in the `TRUNCATE` statement.                                                  |
| 5301        | PostgreSQL doesn’t support `PURGE` clauses in the `TRUNCATE` statement.                                                     |
| 5326        | PostgreSQL doesn’t support status definitions in `CREATE` statements for triggers and constraints.                          |
| 5348        | PostgreSQL doesn’t support nested tables.                                                                                   |
| 5550        | PostgreSQL doesn’t support the `ROWID` data type.                                                                           |
| 5551        | PostgreSQL doesn’t support the `UROWID` data type.                                                                          |
| 5552        | PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types.                                |
| 5553        | PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types.                                |
| 5554        | PostgreSQL doesn’t support virtual columns.                                                                                 |
| 5581        | PostgreSQL doesn’t support index-organized tables.                                                                          |
| 5620        | The AWS SCT extension pack doesn’t support the `DELETE ROWS` option for the `ON COMMIT` clause for global temporary tables. |
| 5621        | Make sure that the unique constraint for the %s field exists.                                                               |
| 5635        | AWS SCT doesn’t support Oracle specific formatting settings.                                                                |
| 5659        | AWS SCT can’t convert tables that include columns of the %s data type.                                                      |

## Data types

![Four star automation level](images/pb-automation-4.png)

Data type syntax is very similar between Oracle and Aurora PostgreSQL and most are converted automatically by AWS SCT. Note that date and time handling paradigms are different for Oracle and Aurora PostgreSQL and require manual verifications and/or conversion. Also note that due to differences in data type behavior between Oracle and Aurora PostgreSQL, manual verification and strict testing are highly recommended.

For more information, see [Data Types](chap-oracle-aurora-pg.tables.md "chap-oracle-aurora-pg.tables.md").

| Action code | Action message                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------- |
| 5028        | AWS SCT can’t convert object definitions with the unsupported %s data type.                                   |
| 5029        | AWS SCT can’t convert the usage of objects with the unsupported %s data type.                                 |
| 5030        | AWS SCT can’t convert the usage of objects with the unsupported %s data type.                                 |
| 5212        | PostgreSQL doesn’t support the `BFILE` data type.                                                             |
| 5550        | PostgreSQL doesn’t support the `ROWID` data type.                                                             |
| 5551        | PostgreSQL doesn’t support the `UROWID` data type.                                                            |
| 5572        | PostgreSQL doesn’t support object type methods.                                                               |
| 5595        | AWS SCT can’t convert the `ROWID` usage. This object uses the `ROWID` column from the %s table.               |
| 5597        | AWS SCT can’t convert the `ROWID` usage. This object uses the `ROWID` column from the %s table.               |
| 5598        | PostgreSQL doesn’t support `ROWID`.                                                                           |
| 5609        | AWS SCT can’t convert unsupported data types. PostgreSQL doesn’t support the %s data type.                    |
| 5613        | AWS SCT can’t convert multi-dimensional arrays.                                                               |
| 5636        | AWS SCT can’t convert `VARRAY of VARRAY`.                                                                     |
| 5644        | AWS SCT can’t convert the assign operation of an array or a nested table because it includes a nested record. |

## Character set

![Four star automation level](images/pb-automation-4.png)

The character set granularity in Oracle and Aurora PostgreSQL are significantly different, in some cases.

For more information, see [Character Set](chap-oracle-aurora-pg.special.md "chap-oracle-aurora-pg.special.md").

| Action code | Action message                      |
| ----------- | ----------------------------------- |
| 5623        | AWS SCT doesn’t support uuencoding. |

## Cursors

![Three star automation level](images/pb-automation-3.png)

PostgreSQL has PL/pgSQL cursors that enable you to iterate business logic on rows read from the database. They can encapsulate the query and read the query results a few rows at a time. All access to cursors in PL/pgSQL is performed through cursor variables, which are always of the refcursor data type.

There are specific options which aren’t supported for automatic conversion by AWS SCT.

For more information, see [Cursors](chap-oracle-aurora-pg.sql.md "chap-oracle-aurora-pg.sql.md").

| Action code | Action message                                                                                                    |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 5031        | AWS SCT can’t convert `CURSOR` expressions.                                                                       |
| 5040        | AWS SCT can’t convert `SHARING` clauses. PostgreSQL doesn’t support the %s `SHARING` clause.                      |
| 5042        | PostgreSQL doesn’t support cursors of a specified type.                                                           |
| 5117        | AWS SCT can’t convert cursor attributes. PostgreSQL doesn’t support the %s attribute.                             |
| 5225        | PostgreSQL doesn’t support `TYPE …​ IS REF CURSOR` declarations.                                                  |
| 5226        | PostgreSQL doesn’t support the `TYPE …​ IS REF CURSOR` usage.                                                     |
| 5330        | PostgreSQL doesn’t support global cursors.                                                                        |
| 5559        | PostgreSQL doesn’t support `RETURN TYPE` for cursors.                                                             |
| 5560        | PostgreSQL doesn’t support `PROGRAM_ERROR` exceptions.                                                            |
| 5561        | AWS SCT can’t convert pre-defined exceptions. PostgreSQL doesn’t support the %s exception.                        |
| 5580        | The exception block in the converted code is empty.                                                               |
| 5599        | PostgreSQL doesn’t support references to `SQLERRM` outside of an exception handler.                               |
| 5600        | PostgreSQL doesn’t support references to `SQLERRM` with any specified parameter value.                            |
| 5601        | PostgreSQL doesn’t support references to `SQLCODE` outside of an exception handler.                               |
| 5602        | PostgreSQL error code type isn’t compatible with the number type variables.                                       |
| 5604        | PostgreSQL doesn’t support global cursors. AWS SCT converts global cursors to local cursors.                      |
| 5612        | AWS SCT can’t convert the `FETCH` command for a global parameterized cursor before the cursor variable is opened. |

## Flow control

![Four star automation level](images/pb-automation-4.png)

Although the flow control syntax of Oracle differs from Aurora PostgreSQL , AWS SCT can convert most constructs automatically including loops, command blocks, and delays. Aurora PostgreSQL doesn’t support the `GOTO` command nor conditional compilation command, which require manual conversion.

| Action code | Action message                                      |
| ----------- | --------------------------------------------------- |
| 5335        | PostgreSQL doesn’t support `GOTO` operators.        |
| 5603        | PostgreSQL doesn’t support conditional compilation. |

## Transaction isolation

![Four star automation level](images/pb-automation-4.png)

Aurora PostgreSQL supports the four transaction isolation levels specified in the SQL:92 standard: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`, all of which are automatically converted by AWS SCT. AWS SCT also converts `BEGIN / COMMIT` and `ROLLBACK` commands that use slightly different syntax. Manual conversion is required for named, marked, and delayed durability transactions that aren’t supported by Aurora PostgreSQL.

For more information, see [Transaction Isolation](chap-oracle-aurora-pg.sql.md "chap-oracle-aurora-pg.sql.md").

| Action code | Action message                                                                      |
| ----------- | ----------------------------------------------------------------------------------- |
| 5350        | AWS SCT can’t convert statements that explicitly apply or cancel a transaction.     |
| 5611        | PostgreSQL doesn’t support `SAVEPOINT` and `ROLLBACK TO SAVEPOINT` inside routines. |

## Stored procedures

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL stored procedures (functions) provide very similar functionality to Oracle stored procedures and can be automatically converted by AWS SCT. Manual conversion is required for procedures that use `RETURN` values and some less common `EXECUTE` options such as the `RECOMPILE` and `RESULTS SETS` options.

For more information, see [Stored Procedures](chap-oracle-aurora-pg.sql.md "chap-oracle-aurora-pg.sql.md").

| Action code | Action message                                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------- |
| 5027        | The package body doesn’t include source code.                                                                        |
| 5340        | PostgreSQL doesn’t support the %s function.                                                                          |
| 5579        | Make sure that the second parameter of the %s function is processed correctly.                                       |
| 5584        | The %s function depends on the time zone settings.                                                                   |
| 5607        | AWS SCT can’t convert Java stored routine.                                                                           |
| 5616        | AWS SCT can’t convert `TABLE` functions.                                                                             |
| 5617        | PostgreSQL doesn’t fully support m and x as match parameters or as subexpression parameters for regular expressions. |
| 5624        | Converted code might not work correctly because of the bind variable names.                                          |
| 5625        | PostgreSQL doesn’t support parameters in an anonymous block.                                                         |
| 5626        | AWS SCT can’t convert the %s function.                                                                               |
| 5627        | Converted code might not work correctly because of the user-defined functions.                                       |
| 5628        | Converted code might not work correctly because of the dynamic SQL statements.                                       |
| 5629        | PostgreSQL doesn’t support all features of the `DBMS_SQL` package.                                                   |
| 5630        | AWS SCT can’t convert the `DBMS_SQL` package functions.                                                              |
| 5633        | Converted code might not work correctly because of the dynamic SQL statements.                                       |
| 5634        | AWS SCT can’t convert the use of user-defined functions with `OUT` and `INOUT` parameters.                           |

## Triggers

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL supports `BEFORE` and `AFTER` triggers for `INSERT`, `UPDATE`, and `DELETE`. However, Aurora PostgreSQL triggers differ substantially from Oracle triggers, but most common use cases can be migrated with minimal code changes.

For more information, see [Triggers](chap-oracle-aurora-pg.tables.md "chap-oracle-aurora-pg.tables.md").

| Action code | Action message                                                                                                                                                                |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5238        | PostgreSQL doesn’t support `REFERENCING` clauses.                                                                                                                             |
| 5240        | PostgreSQL doesn’t support triggers on nested table columns in views.                                                                                                         |
| 5241        | PostgreSQL doesn’t support `FOLLOWS` and `PRECEDES` clauses.                                                                                                                  |
| 5242        | PostgreSQL doesn’t support `COMPOUND TRIGGER`.                                                                                                                                |
| 5243        | PostgreSQL always creates a trigger under the table’s schema. Review the converted code to make sure that your trigger and its function are created under the table’s schema. |
| 5306        | AWS SCT can’t convert the trigger that isn’t valid.                                                                                                                           |
| 5311        | PostgreSQL doesn’t support system triggers.                                                                                                                                   |
| 5313        | PostgreSQL doesn’t support action-type clauses in triggers.                                                                                                                   |
| 5317        | PostgreSQL doesn’t support `PARENT` referencing clauses.                                                                                                                      |
| 5415        | PostgreSQL doesn’t support system triggers.                                                                                                                                   |
| 5556        | PostgreSQL doesn’t support conditional predicates.                                                                                                                            |

## Sequences

![Three star automation level](images/pb-automation-3.png)

Although the syntax for Oracle `IDENTITY` and Aurora PostgreSQL `SERIAL` auto-enumeration columns differs significantly, it can be automatically converted by AWS SCT.

For more information, see [Sequences](chap-oracle-aurora-pg.sql.md "chap-oracle-aurora-pg.sql.md") and [Identity](chap-oracle-aurora-pg.sql.md "chap-oracle-aurora-pg.sql.md").

| Action code | Action message                                |
| ----------- | --------------------------------------------- |
| 5574        | PostgreSQL doesn’t support sequence statuses. |

## Views

![Four star automation level](images/pb-automation-4.png)

Although the basic syntax for creating a view in Oracle and Aurora PostgreSQL is almost identical there are some sub-options that can differs significantly and this can add manual needed tasks to the migration process.

For more information, see [Views](chap-oracle-aurora-pg.special.md "chap-oracle-aurora-pg.special.md").

| Action code | Action message                                                         |
| ----------- | ---------------------------------------------------------------------- |
| 5075        | PostgreSQL doesn’t support the `WITH READ ONLY` clause for views.      |
| 5077        | PostgreSQL doesn’t support the `PIVOT` clause for `SELECT` statements. |
| 5245        | PostgreSQL doesn’t support views with nested table columns.            |
| 5320        | PostgreSQL doesn’t support views with the `INVALID` status.            |
| 5321        | PostgreSQL doesn’t support object views.                               |
| 5322        | PostgreSQL doesn’t support typed views.                                |
| 5583        | PostgreSQL doesn’t support constraints for views.                      |
| 5614        | PostgreSQL doesn’t support DML operations with non-updatable views.    |

## User-defined types

![Three star automation level](images/pb-automation-3.png)

User-defined types aren’t supported, AWS SCT can convert standard user-defined types by replacing it with their base types. More complicated user-defined types may require manual intervention.

For more information, see [User-Defined Types](chap-oracle-aurora-pg.tables.md "chap-oracle-aurora-pg.tables.md").

| Action code | Action message                                                                                                                                                                  |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5032        | AWS SCT can’t convert user-defined data types with incomplete definitions. PostgreSQL doesn’t support data types that are based on data types that have incomplete definitions. |
| 5062        | AWS SCT converted the %s type constructor to a direct assignment.                                                                                                               |
| 5099        | AWS SCT can’t convert the object because the %s parent object wasn’t created.                                                                                                   |
| 5118        | PostgreSQL doesn’t support associative arrays. AWS SCT can’t convert the %s data type declaration.                                                                              |
| 5120        | PostgreSQL doesn’t support constructors of the collection data type.                                                                                                            |
| 5121        | PostgreSQL doesn’t support `FORALL` statements.                                                                                                                                 |
| 5332        | AWS SCT can’t convert the object that references an object in the %s schema, which isn’t converted.                                                                             |
| 5569        | PostgreSQL supports only standard SQL date and time types for session variables.                                                                                                |
| 5575        | AWS SCT can’t convert `DEFAULT` statements for user-defined types. PostgreSQL doesn’t support the assignment of default values when creating the %s user-defined type.          |
| 5577        | PostgreSQL doesn’t support member functions in user-defined types.                                                                                                              |
| 5582        | PostgreSQL doesn’t support encrypted objects in the `CREATE` statement.                                                                                                         |
| 5587        | PostgreSQL doesn’t support `EXTEND` methods with parameters.                                                                                                                    |
| 5638        | AWS SCT doesn’t support global variables of nested table as an argument for functions or procedures.                                                                            |

## Merge

![No automation](images/pb-automation-0.png)

The `MERGE` statement isn’t supported and it can’t be automatically converted by AWS SCT. Manual conversion is straight-forward in most cases.

For more information, see [Merge](chap-oracle-aurora-pg.sql.md "chap-oracle-aurora-pg.sql.md").

| Action code | Action message                                                             |
| ----------- | -------------------------------------------------------------------------- |
| 5102        | PostgreSQL doesn’t support `MERGE` statements.                             |
| 5618        | PostgreSQL doesn’t support `MERGE` statements with the `ERROR LOG` clause. |
| 5621        | Make sure that the unique constraint for the %s field exists.              |

## Materialized views

![Two star automation level](images/pb-automation-2.png)

Materialized views aren’t supported, some features such as incremental refresh or DML commands on materialized views aren’t supported.

For more information, see [Materialized Views](chap-oracle-aurora-pg.special.md "chap-oracle-aurora-pg.special.md").

| Action code | Action message                                                   |
| ----------- | ---------------------------------------------------------------- |
| 5093        | AWS SCT can’t convert the query of the materialized view         |
| 5094        | AWS SCT can’t convert the materialized view.                     |
| 5095        | PostgreSQL doesn’t support DML statements on materialized views. |

## Query hints

![Three star automation level](images/pb-automation-3.png)

Basic query hints such as index hints can be converted automatically by AWS SCT, except for DML statements. Note that specific optimizations used for Oracle may be completely inapplicable to a new query optimizer. It is recommended to start migration testing with all hints removed. Then, selectively apply hints as a last resort if other means such as schema, index, and query optimizations have failed. Plan guides aren’t supported by Aurora PostgreSQL.

For more information, see [Query Hints and Plan Guides](chap-oracle-aurora-pg.tuning.md "chap-oracle-aurora-pg.tuning.md").

| Action code | Action message                                                       |
| ----------- | -------------------------------------------------------------------- |
| 5103        | AWS SCT can’t convert hints. PostgreSQL doesn’t support the %s hint. |

## Database links

![No automation](images/pb-automation-0.png)

Migrating database links from Oracle to Aurora PostgreSQL requires a full rewrite the mechanism that managed the database links. This can’t be automatically converted by AWS SCT.

For more information, see [Database Links](chap-oracle-aurora-pg.special.md "chap-oracle-aurora-pg.special.md").

| Action code | Action message                                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 5605        | PostgreSQL doesn’t support the usage of database links.                                                                                         |
| 5639        | Make sure that you installed the `postgres_fdw` extension.                                                                                      |
| 5640        | AWS SCT can’t convert the database link because the remote table isn’t defined. AWS SCT created the structure of this table based on referenes. |
| 5641        | PostgreSQL foreign data wrapper doesn’t support the usage of user-defined functions.                                                            |
| 5657        | PostgreSQL can’t create views that are based on undefined foreign tables.                                                                       |

## Indexes

![Four star automation level](images/pb-automation-4.png)

Basic non-clustered indexes, which are the most commonly used type of indexes are automatically migrated by AWS SCT. In addition, filtered indexes, indexes with included columns, and some Oracle specific index options such as bitmap or domain can’t be migrated automatically and require manual conversion.

For more details, see the Indexes topics.

| Action code | Action message                                                           |
| ----------- | ------------------------------------------------------------------------ |
| 5206        | PostgreSQL doesn’t support bitmap indexes.                               |
| 5208        | PostgreSQL doesn’t support domain indexes.                               |
| 5555        | PostgreSQL doesn’t support functional indexes that aren’t single-column. |

## Partitioning

![Three star automation level](images/pb-automation-3.png)

Aurora PostgreSQL uses table inheritance, some of the physical aspects of partitioning in Oracle don’t apply to Aurora PostgreSQL. For example, the concept of file groups and assigning partitions to file groups. Aurora PostgreSQL supports a much richer framework for table partitioning than Oracle, with many additional options such as hash partitioning, and sub partitioning.

For more information, see [Partitioning](chap-oracle-aurora-pg.storage.md "chap-oracle-aurora-pg.storage.md").

| Action code | Action message                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| 5652        | PostgreSQL doesn’t have a mechanism that handles null values for partition keys.                       |
| 5653        | PostgreSQL doesn’t support foreign keys that reference partitioned tables.                             |
| 5654        | PostgreSQL doesn’t support foreign keys in partitioned tables that reference other tables.             |
| 5655        | AWS SCT can’t convert update operations of partitioned tables, partitions, or subpartitions.           |
| 5656        | The timestamp data type in converted code might produce different results compared to the source code. |
| 5658        | You can use `DEFAULT` partitions in PostgreSQL version 11 and higher.                                  |

## OLAP functions

![Four star automation level](images/pb-automation-4.png)

Aurora PostgreSQL does provide native support for almost all OLAP Functions.

For more information, see [OLAP Functions](chap-oracle-aurora-pg.sql.md "chap-oracle-aurora-pg.sql.md").

| Action code | Action message                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| 5271        | The `GREATEST` function in converted code might produce different results compared to the source code. |
| 5272        | The `LEAST` function in converted code might produce different results compared to the source code.    |
| 5622        | AWS SCT converts the `dbms_transaction.local_transaction_id` function with the parameter set to true.  |
