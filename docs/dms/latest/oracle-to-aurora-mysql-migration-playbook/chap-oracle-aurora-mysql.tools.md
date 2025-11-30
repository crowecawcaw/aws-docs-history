# AWS SCT action code index

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

The links in the table point to the Oracle topic pages, which are immediately followed by the MySQL pages for the same topics.

## Creating tables

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used constructs of the `CREATE TABLE` statement because Oracle and Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) support the entry level American National Standards Institute (ANSI) compliance. These items include table names, containing security schema or database, column names, basic column data types, column and table constraints, column default values, primary, UNIQUE, and foreign keys. Some changes may be required for computed columns and global temporary tables.

| Action code | Action message                                                                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 73          | MySQL doesn’t support the `IDENTITY` statement with the `MAXVALUE`, `MINVALUE`, or `CYCLE` options or with the `INCREMENT BY` value that is different from 1. |
| 74          | MySQL doesn’t support `AUTO_INCREMENT` statements without the primary key option on the same column.                                                          |
| 190         | MySQL doesn’t support the `COLUMN_VALUE` pseudocolumn.                                                                                                        |
| 191         | MySQL doesn’t support the `OBJECT_ID` pseudocolumn.                                                                                                           |
| 192         | MySQL doesn’t support the `ORA_ROWSCN` pseudocolumn.                                                                                                          |
| 193         | MySQL doesn’t support the `ROWID` pseudocolumn.                                                                                                               |
| 198         | MySQL doesn’t support global temporary tables.                                                                                                                |
| 199         | MySQL doesn’t support clustered tables.                                                                                                                       |
| 200         | MySQL doesn’t support external tables.                                                                                                                        |
| 209         | AWS SCT uses triggers to emulate virtual columns because MySQL doesn’t support virtual columns.                                                               |
| 210         | AWS SCT uses triggers to emulate the usage of functions or expressions as default value in `CREATE TABLE` statements.                                         |
| 215         | MySQL doesn’t support virtual columns with unsupported build-in functions.                                                                                    |
| 245         | MySQL doesn’t support views with nested table columns.                                                                                                        |
| 296         | AWS SCT can’t convert tables that aren’t valid.                                                                                                               |
| 327         | MySQL doesn’t support the objects column.                                                                                                                     |
| 348         | MySQL doesn’t support global temporary tables.                                                                                                                |

## Constraints

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts most constraints because Oracle and Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) support the entry level ANSI compliance. These items include primary keys, foreign keys, null constraints, unique constraints, and default constraints with some exceptions. Manual conversions are required for some foreign key cascading options. AWS SCT replaces check constraints with triggers, and some default expressions for `DateTime` columns aren’t supported for automatic conversion. AWS SCT can’t automatically convert complex expressions for other default values.

For more information, see [Table Constraints](chap-oracle-aurora-mysql.tables.md "chap-oracle-aurora-mysql.tables.md").

| Action code | Action message                                                                                                 |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| 202         | MySQL doesn’t support foreign keys with different types of columns or with referenced columns.                 |
| 203         | AWS SCT can’t convert foreign keys with the `SET NULL` action for columns that have the `NOT NULL` constraint. |
| 204         | AWS SCT can’t convert foreign keys with `BLOB` and `TEXT` columns.                                             |
| 220         | MySQL doesn’t support the record type.                                                                         |
| 325         | AWS SCT uses triggers to emulate check constraints because MySQL doesn’t support them.                         |
| 326         | MySQL doesn’t support constraints with the status set to `DISABLED`.                                           |
| 591 / 593   | AWS SCT can’t convert the `ROWID` usage. This object uses the `ROWID` column from the %s table.                |

## Data types

![Four star automation level](images/pb-automation-4.png)

Data type syntax and rules are similar between Oracle and Aurora MySQL. AWS SCT automatically converts most of data type syntax and rules. Date and time handling paradigms are different for Oracle and Aurora MySQL and require manual verification or conversion. Also note that because of differences in data type behavior between Oracle and Aurora MySQL, manual verification and strict testing are highly recommended.

For more information, see [Data Types](chap-oracle-aurora-mysql.tables.md "chap-oracle-aurora-mysql.tables.md").

| Action code | Action message                                                                    |
| ----------- | --------------------------------------------------------------------------------- |
| 25          | MySQL doesn’t support assignment values for variables of the `INTERVAL` datatype. |
| 28          | AWS SCT can’t convert the variable declaration of the %s unsupported data type.   |
| 29          | AWS SCT can’t convert the reference of the %s unsupported data type.              |
| 30          | AWS SCT can’t convert the usage of the %s unsupported data type.                  |
| 33          | MySQL doesn’t support fractional seconds for `TIMESTAMP` literals.                |
| 212         | MySQL doesn’t support the `BFILE` data type.                                      |

## Common table expressions

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support common table expressions. AWS SCT can’t automatically convert common table expressions.

For workarounds using traditional SQL syntax, see [Common Table Expressions](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                                  |
| ----------- | ----------------------------------------------- |
| 127         | MySQL doesn’t support recursive `WITH` clauses. |

## Cursors

![Three star automation level](images/pb-automation-3.png)

AWS SCT automatically converts the most commonly used cursor operations. These operations include forward-only, read only cursors, and the `DECLARE CURSOR`, `CLOSE CURSOR`, and `FETCH NEXT` operations. Modifications through cursors and non-forward-only fetches, which aren’t supported by Aurora MySQL, require manual conversions.

For more information, see [Cursors](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                                                                                                                                                                                           |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31          | AWS SCT can’t convert `CURSOR` expressions.                                                                                                                                                              |
| 84          | AWS SCT doesn’t convert the `SQL%ISOPEN` cursor attribute because this is the default behavior in MySQL.                                                                                                 |
| 85          | MySQL doesn’t support the `SQL%BULK_ROWCOUNT` cursor attribute.                                                                                                                                          |
| 297         | MySQL doesn’t support `%ROWTYPE` attributes.                                                                                                                                                             |
| 330         | MySQL doesn’t support global cursors. AWS SCT replaces global cursors with local cursors.                                                                                                                |
| 337         | MySQL doesn’t support variables of the `SYS_REFCURSOR` type.                                                                                                                                             |
| 343         | AWS SCT can’t convert `SELECT` statements for cursors.                                                                                                                                                   |
| 354         | AWS SCT can’t convert dynamic SQL for the `REF_CURSOR` variable.                                                                                                                                         |
| 596         | Converted code might produce different results compared to the source code. If `SQL%ROWCOUNT` refers to `INSERT` or `DELETE` statements, make sure that you use `FOUND_ROWS()` instead of `ROW_COUNT()`. |
| 598         | MySQL doesn’t support `RETURN` clauses in cursors.                                                                                                                                                       |

## Transaction isolation

![Four star automation level](images/pb-automation-4.png)

Aurora MySQL supports the following four transaction isolation levels specified in the SQL:92 standard: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`. AWS Schema Conversion Tool (AWS SCT) automatically converts all these transaction isolation levels. AWS SCT also converts `BEGIN`, `COMMIT`, and `ROLLBACK` commands that use slightly different syntax. Manual conversion is required for named, marked, and delayed durability transactions that aren’t supported by Aurora MySQL.

For more information, see [Transactions](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                                                                         |
| ----------- | -------------------------------------------------------------------------------------- |
| 235         | MySQL doesn’t support `PRAGMA` options.                                                |
| 302         | MySQL doesn’t support `NOWAIT` clauses in `LOCK TABLE` statements.                     |
| 346         | MySQL doesn’t support `LOCK TABLE` statements inside stored procedures.                |
| 350         | AWS SCT can’t convert statements such as `START TRANSACTION`, `COMMIT`, or `ROLLBACK`. |

## Stored procedures

![Four star automation level](images/pb-automation-4.png)

Aurora MySQL stored procedures provide very similar functionality to Oracle stored procedures. AWS SCT automatically converts Oracle stored procedures. Manual conversion is required for procedures that use `RETURN` values and some less common `EXECUTE` options such as `RECOMPILE` and `RESULTS SETS`.

For more information, see [Stored Procedures](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                                                                         |
| ----------- | -------------------------------------------------------------------------------------- |
| 27          | The package body doesn’t include source code.                                          |
| 152         | Converted code might not cover all built-in exception names.                           |
| 234         | MySQL doesn’t support the `EXCEPTION` declaration.                                     |
| 253         | MySQL doesn’t support the %s function with two parameters.                             |
| 266         | MySQL doesn’t support the %s function with analytic clauses.                           |
| 329         | MySQL doesn’t support `RAISE` statements.                                              |
| 331         | MySQL doesn’t support global user-defined exceptions.                                  |
| 333         | MySQL doesn’t support exception blocks in initialization blocks in packages.           |
| 335         | MySQL doesn’t support `GOTO` operators.                                                |
| 340         | MySQL doesn’t support the %s function.                                                 |
| 342         | MySQL doesn’t support the %s exception.                                                |
| 345         | Converted code might not cover all conditions.                                         |
| 350         | AWS SCT can’t convert statements such as `START TRANSACTION`, `COMMIT`, or `ROLLBACK`. |
| 590         | AWS SCT converted the function as procedure.                                           |

## Triggers

![Three star automation level](images/pb-automation-3.png)

Aurora MySQL supports `BEFORE` and `AFTER` triggers for `INSERT`, `UPDATE`, and `DELETE`. Aurora MySQL triggers differ substantially from Oracle triggers. However, for most common use cases, AWS SCT can migrate triggers with minimal code changes. Although AWS SCT can automatically migrate trigger code, manual inspection and potential code modifications may be required because Aurora MySQL triggers run once for each row, not once for each statement such as triggers in Oracle.

For more information, see [Triggers](chap-oracle-aurora-mysql.tables.md "chap-oracle-aurora-mysql.tables.md").

| Action code | Action message                                                                                      |
| ----------- | --------------------------------------------------------------------------------------------------- |
| 236         | MySQL doesn’t support `INSTEAD OF` triggers.                                                        |
| 237         | MySQL doesn’t support statement triggers.                                                           |
| 238         | MySQL doesn’t support `REFERENCING` clauses.                                                        |
| 239         | MySQL doesn’t support triggers with `WHEN` conditions.                                              |
| 240         | MySQL doesn’t support triggers on nested table columns in views.                                    |
| 241         | MySQL doesn’t support triggers with `FOLLOWS` and `PRECEDES` clauses.                               |
| 242         | MySQL doesn’t support compound triggers.                                                            |
| 243         | MySQL doesn’t support `UPDATE OF` clauses.                                                          |
| 244         | MySQL doesn’t support conditional predicates.                                                       |
| 306         | AWS SCT can’t convert a trigger that isn’t valid.                                                   |
| 310         | MySQL doesn’t support triggers for views.                                                           |
| 311         | MySQL doesn’t support system triggers.                                                              |
| 312         | MySQL doesn’t support `DISABLED` clauses.                                                           |
| 313         | MySQL doesn’t support action-type clauses in triggers.                                              |
| 314         | MySQL doesn’t support cross edition triggers.                                                       |
| 316         | MySQL doesn’t support the apply-server-only property.                                               |
| 317         | MySQL doesn’t support `PARENT` referencing clauses.                                                 |
| 415         | MySQL doesn’t support system triggers.                                                              |
| 524         | MySQL doesn’t support triggers for multiple events.                                                 |
| 588         | MySQL doesn’t support multiple triggers for a single event. AWS SCT merged triggers in one trigger. |

## Sequences

![One star automation level](images/pb-automation-1.png)

Although the syntax for Oracle `IDENTITY` and Aurora MySQL
`AUTO_INCREMENT` auto-enumeration columns differs significantly, AWS SCT can automatically convert it. Some limitations imposed by Aurora MySQL require manual conversion such as explicit `SEED` and `INCREMENT` auto-enumeration columns that aren’t part of the primary key and the table-independent `SEQUENCE` objects.

For more information, see [Oracle Sequences and Identity Columns and MySQL Sequences and AUTO INCREMENT Columns](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                   |
| ----------- | -------------------------------- |
| 341         | MySQL doesn’t support sequences. |

## Date and time functions

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used date and time functions despite the significant difference in syntax. Be aware of differences in data types, time zone awareness, and locale handling as well the functions themselves, and inspect the expression value output carefully. Some less commonly used options such as millisecond, nanosecond, and time zone offsets require manual conversion.

| Action code | Action message                                                                                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 213         | AWS SCT expanded fractional seconds support for `TIME`, `DATETIME`, and `TIMESTAMP` values with up to 6 digits of precision.                                                                    |
| 214         | MySQL doesn’t support data types that store time zone information. The `DATETIME` data type stores timestamps in the MySQL server time zone.                                                    |
| 216         | AWS SCT expanded fractional seconds support for `TIME`, `DATETIME`, and `TIMESTAMP` values with up to 6 digits of precision. MySQL doesn’t support data types that store time zone information. |

## User-defined types

![Three star automation level](images/pb-automation-3.png)

Aurora MySQL 5.7 doesn’t support-user defined types and user-defined table-valued parameters. AWS SCT can convert standard user defined types by replacing it with their base types, but manual conversion is required for user defined table types, which are used for table valued parameters for stored procedures.

For more information, see [User-Defined Types](chap-oracle-aurora-mysql.tables.md "chap-oracle-aurora-mysql.tables.md").

| Action code | Action message                       |
| ----------- | ------------------------------------ |
| 196         | MySQL doesn’t support object tables. |
| 218         | MySQL doesn’t support user types.    |

## Synonyms

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support synonyms. AWS SCT can’t automatically convert synonyms.

| Action code | Action message                                                                               |
| ----------- | -------------------------------------------------------------------------------------------- |
| 352         | MySQL doesn’t support synonyms. AWS SCT replaces synonyms with fully-qualified object names. |

## XML

![Four star automation level](images/pb-automation-4.png)

Aurora MySQL provides minimal support for XML, but it does offer a native JSON data type and more than 25 dedicated JSON functions. Despite these differences, the most commonly used basic XML functions can be automatically migrated by AWS SCT. Some options such as `EXPLICIT`, used in functions or with subqueries, require manual conversion.

For more information, see [XML](chap-oracle-aurora-mysql.special.md "chap-oracle-aurora-mysql.special.md").

| Action code | Action message                                    |
| ----------- | ------------------------------------------------- |
| 194         | MySQL doesn’t support `XMLTYPE` tables.           |
| 195         | MySQL doesn’t support the `XMLDATA` pseudocolumn. |
| 303         | MySQL doesn’t support the `XMLTable` function.    |

## MERGE

![No automation](images/pb-automation-0.png)

Aurora MySQL version 5.7 doesn’t support the `MERGE` statement. AWS SCT can’t automatically convert `MERGE` statements. Manual conversion is straightforward in most cases.

| Action code | Action message                            |
| ----------- | ----------------------------------------- |
| 102         | MySQL doesn’t support `MERGE` statements. |

## Query hints

![Three star automation level](images/pb-automation-3.png)

AWS SCT can automatically convert basic query hints such as index hints, except for DML statements. Note that specific optimizations used for Oracle may be completely inapplicable to a new query optimizer. It is recommended to start migration testing with all hints removed. Then, selectively apply hints as a last resort if other means such as schema, index, and query optimizations have failed. Plan guides aren’t supported by Aurora MySQL.

For more information, see [Database Hints](chap-oracle-aurora-mysql.tuning.md "chap-oracle-aurora-mysql.tuning.md").

| Action code | Action message                                                  |
| ----------- | --------------------------------------------------------------- |
| 103         | AWS SCT can’t convert hints. MySQL doesn’t support the %s hint. |

## Indexes

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts basic non-clustered indexes, which are the most commonly used type of indexes. User-defined clustered indexes aren’t supported by Aurora MySQL because they are always created for the primary key. In addition, filtered indexes, indexes with included columns, and some Oracle specific index options can’t be migrated automatically and require manual conversion.

For more information, see [Indexes](chap-oracle-aurora-mysql.tables.md "chap-oracle-aurora-mysql.tables.md").

| Action code | Action message                                                         |
| ----------- | ---------------------------------------------------------------------- |
| 205         | MySQL has reached the limit of the internal InnoDB maximum key length. |
| 206         | MySQL doesn’t support bitmap indexes.                                  |
| 207         | MySQL doesn’t support function indexes.                                |
| 208         | MySQL doesn’t support domain indexes.                                  |
| 328         | AWS SCT can’t convert indexes that aren’t valid.                       |

## Partitioning

![Three star automation level](images/pb-automation-3.png)

Because Aurora MySQL stores each table in its own file, and because file management is performed by AWS and can’t be modified, some of the physical aspects of partitioning in Oracle don’t apply to Aurora MySQL. Because of the vast differences between partition creation, query, and management between Aurora MySQL and Oracle, AWS SCT doesn’t automatically convert table and index partitions. These items require manual conversion.

For more information, see [Table Partitioning](chap-oracle-aurora-mysql.storage.md "chap-oracle-aurora-mysql.storage.md").

| Action code | Action message                                                                  |
| ----------- | ------------------------------------------------------------------------------- |
| 201         | MySQL doesn’t support partition types that are implemented in your source code. |
| 699         | MySQL doesn’t support not allowed partitions functions.                         |

## Materialized views

![No automation](images/pb-automation-0.png)

Aurora MySQL 5.7 doesn’t support materialized views. AWS SCT can’t automatically convert materialized views.

For more information, see [Oracle Materialized Views and MySQL Summary Tables or Views](chap-oracle-aurora-mysql.special.md "chap-oracle-aurora-mysql.special.md").

| Action code | Action message                                         |
| ----------- | ------------------------------------------------------ |
| 94          | MySQL doesn’t support materialized views.              |
| 95          | MySQL doesn’t support the usage of materialized views. |

## Views

![Four star automation level](images/pb-automation-4.png)

Although the basic syntax for creating a view in Oracle and Aurora MySQL is almost identical, there are some sub-options that can differ significantly, requiring additional manual migration tasks.

For more information, see [Views](chap-oracle-aurora-mysql.special.md "chap-oracle-aurora-mysql.special.md").

| Action code | Action message                                       |
| ----------- | ---------------------------------------------------- |
| 75          | MySQL doesn’t support read-only views.               |
| 93          | MySQL doesn’t support `UPDATE` statements for views. |
| 97          | MySQL doesn’t support `DELETE` statements for views. |
| 320         | AWS SCT can’t convert a view that isn’t valid.       |
| 321         | MySQL doesn’t support object views.                  |
| 323         | MySQL doesn’t support subviews under a superview.    |
| 324         | MySQL doesn’t support editioning views.              |
| 583         | MySQL doesn’t support constraints for views.         |

## UTL_Mail and UTL_SMTP

![No automation](images/pb-automation-0.png)

Aurora MySQL doesn’t provide native support for sending emails from the database.

For more information, see [Database Mail](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                                   |
| ----------- | ------------------------------------------------ |
| 81          | MySQL doesn’t support sending SMS notifications. |
| 82          | MySQL doesn’t support sending emails.            |

## Database Links

![No automation](images/pb-automation-0.png)

Aurora MySQL doesn’t support remote data access. Connectivity between schemas is trivial, but connectivity to other instances requires a custom solution. AWS SCT can’t automatically convert database links.

For more information, see [Database Links](chap-oracle-aurora-mysql.special.md "chap-oracle-aurora-mysql.special.md").

| Action code | Action message                                     |
| ----------- | -------------------------------------------------- |
| 600         | MySQL doesn’t support the usage of database links. |

## PLSQL

![Four star automation level](images/pb-automation-4.png)

AWS SCT automatically converts the most commonly used SQL statements because Oracle and Aurora MySQL support the entry level ANSI compliance. Some changes may be required for DML related to `ERROR LOG`, subquery, and partitions.

| Action code | Action message                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| 63          | AWS SCT can’t convert `UPDATE` statements with multiple-column subqueries in `SET` clauses.                              |
| 64          | MySQL doesn’t support `UPDATE` statements with `ERROR LOG` clauses.                                                      |
| 65          | MySQL doesn’t support `UPDATE` statements for subqueries.                                                                |
| 66          | MySQL doesn’t support `UPDATE` statements for `RETURNING INTO` clauses.                                                  |
| 67          | MySQL doesn’t support `DELETE` statements with `ERROR LOG` clauses.                                                      |
| 68          | MySQL doesn’t support `DELETE` statements for subqueries.                                                                |
| 69          | MySQL doesn’t support `DELETE` statements for `RETURNING INTO` clauses.                                                  |
| 70          | MySQL doesn’t support `INSERT` statements with `ERROR LOG` clauses.                                                      |
| 71          | MySQL doesn’t support `INSERT` statements for subqueries.                                                                |
| 72          | MySQL doesn’t support `INSERT` statements for `RETURNING INTO` clauses.                                                  |
| 77          | MySQL doesn’t support `PIVOT` clauses for `SELECT` statements.                                                           |
| 78          | MySQL doesn’t support `UNPIVOT` clauses for `SELECT` statements.                                                         |
| 87          | MySQL doesn’t support `RETURNING BULK COLLECT INTO` clauses.                                                             |
| 89          | MySQL doesn’t support `INSERT` statements for views.                                                                     |
| 90          | MySQL doesn’t support `INSERT` statements for subpartitions.                                                             |
| 122         | MySQL doesn’t support hierarchical queries.                                                                              |
| 125         | MySQL doesn’t support `GROUPING SETS` statements.                                                                        |
| 128         | MySQL doesn’t support `ORACLE FLASHBACK VERSION QUERY`.                                                                  |
| 138         | MySQL doesn’t support `FOR UPDATE OF` clauses.                                                                           |
| 139         | MySQL doesn’t support `FOR UPDATE SKIP LOCKED` clauses.                                                                  |
| 140         | MySQL doesn’t support `BULK COLLECT INTO` clauses.                                                                       |
| 141         | MySQL doesn’t support `ORDER BY …​ NULLS FIRST` clauses.                                                                 |
| 143         | MySQL doesn’t support `FOR UPDATE NOWAIT` clauses.                                                                       |
| 144         | MySQL doesn’t support `FOR UPDATE WAIT` clauses.                                                                         |
| 585         | AWS SCT can’t convert outer join inside a correlated query.                                                              |
| 594         | MySQL doesn’t support `LATERAL`, `CROSS APPLY`, and `OUTER APPLY` correlated inline views.                               |
| 599         | MySQL doesn’t support `CURRENT OF` clauses for data manipulation language queries that are in the body of a cursor loop. |

## EXECUTE IMMEDIATE

![Four star automation level](images/pb-automation-4.png)

There is a major difference between Oracle and Aurora MySQL for the `EXECUTE IMMEDIATE` statement. In MySQL, this statement must be used after a `PREPARE` command. Running SQL with results and bind variables, and running anonymous blocks aren’t supported.

For more information, see [Execute Immediate](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                                                                       |
| ----------- | ------------------------------------------------------------------------------------ |
| 88          | MySQL doesn’t support `EXECUTE IMMEDIATE` statements with `BULK COLLECT`.            |
| 334         | MySQL doesn’t support `EXECUTE IMMEDIATE` dynamic SQL statements.                    |
| 336         | MySQL doesn’t support `EXECUTE IMMEDIATE` dynamic SQL statements with the %s clause. |

## DBMS_OUTPUT

![No automation](images/pb-automation-0.png)

Aurora MySQL doesn’t provide native support for the `dbms_output` procedure. Use the `RAISE` command instead.

For more information, see [DBMS_OUTPUT](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").

| Action code | Action message                                              |
| ----------- | ----------------------------------------------------------- |
| 332         | MySQL doesn’t support the `dbms_output.put_line` procedure. |
| 349         | MySQL doesn’t support the `dbms_output.put` procedure.      |
