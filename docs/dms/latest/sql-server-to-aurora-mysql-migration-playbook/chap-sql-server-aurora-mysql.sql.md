# Creating tables for ANSI SQL

This topic provides reference content comparing the creation of tables in Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the similarities and differences in table creation syntax, features, and capabilities between these two database systems.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                  | Key differences                                                                                                                    |
| ------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [Creating Tables](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.tables "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.tables") | `IDENTITY` and `AUTO_INCREMENT`. Primary key is always clustered. `CREATE TEMPORARY TABLE` syntax. Unsupported `@table` variables. |

## SQL Server Usage

Tables in SQL Server are created using the `CREATE TABLE` statement and conform to the ANSI and ISO entry level standard. The basic features of `CREATE TABLE` are similar for most relational database management engines and are well defined in the ANSI and ISO standards.

In its most basic form, the `CREATE TABLE` statement in SQL Server is used to define:

- Table names, the containing security schema, and database.
- Column names.
- Column data types.
- Column and table constraints.
- Column default values.
- Primary, unique, and foreign keys.

### T-SQL Extensions

SQL Server extends the basic syntax and provides many additional options for the `CREATE TABLE` or `ALTER TABLE` statements. The most often used options are:

- Supporting index types for primary keys and unique constraints, clustered or non-clustered, and index properties such as `FILLFACTOR`.
- Physical table data storage containers using the `ON <File Group>` clause.
- Defining `IDENTITY` auto-enumerator columns.
- Encryption.
- Compression.
- Indexes.

For more information, see [Data Types](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md"), [Column Encryption](chap-sql-server-aurora-mysql.security.md "chap-sql-server-aurora-mysql.security.md"), and [Databases and Schemas](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

### Table Scope

SQL Server provides five scopes for tables:

- Standard tables are created on disk, globally visible, and persist through connection resets and server restarts.
- Temporary tables are designated with the `#` prefix. Temporary tables are persisted in TempDB and are visible to the run scope where they were created and any sub-scope. Temporary tables are cleaned up by the server when the run scope terminates and when the server restarts.
- Global temporary tables are designated by the `##` prefix. They are similar in scope to temporary tables, but are also visible to concurrent scopes.
- Table variables are defined with the `DECLARE` statement, not with `CREATE TABLE`. They are visible only to the run scope where they were created.
- Memory-Optimized tables are special types of tables used by the In-Memory Online Transaction Processing (OLTP) engine. They use a nonstandard `CREATE TABLE` syntax.

### Creating a Table Based on an Existing Table or Query

In SQL Server, you can create new tables based on `SELECT` queries as an alternate to the `CREATE TABLE` statement. A `SELECT` statement that returns a valid set with unique column names can be used to create a new table and populate data.

`SELECT INTO` is a combination of DML and DDL. The simplified syntax for `SELECT INTO` is:

```
SELECT <Expression List>
INTO <Table Name>
[FROM <Table Source>]
[WHERE <Filter>]
[GROUP BY <Grouping Expressions>...];
```

When creating a new table using `SELECT INTO`, the only attributes created for the new table are column names, column order, and the data types of the expressions. Even a straight forward statement such as `SELECT * INTO <New Table> FROM <Source Table>` doesn’t copy constraints, keys, indexes, identity property, default values, or any other related objects.

### TIMESTAMP Syntax for ROWVERSION Deprecated Syntax

The `TIMESTAMP` syntax synonym for `ROWVERSION` has been deprecated as of SQL Server 2008 R2. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)") in the _SQL Server documentation_.

Previously, you could use either the `TIMESTAMP` or the `ROWVERSION` keywords to denote a special data type that exposes an auto-enumerator. The auto-enumerator generates unique eight-byte binary numbers typically used to version-stamp table rows. Clients read the row, process it, and check the `ROWVERSION` value against the current row in the table before modifying it. If they are different, the row has been modified since the client read it. The client can then apply different processing logic.

Note that when you migrate to Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) using AWS Schema Conversion Tool (AWS SCT), neither `ROWVERSION` nor `TIMESTAMP` are supported. AWS SCT raises the following error: `706 — Unsupported data type …​ of variable/column was replaced. Check the conversion result`.

To maintain this functionality, add customer logic, potentially in the form of a trigger.

### Syntax

Simplified syntax for `CREATE TABLE`.

```
CREATE TABLE [<Database Name>.<Schema Name>].<Table Name> (<Column Definitions>)
[ON{<Partition Scheme Name> (<Partition Column Name>)];
```

```
<Column Definition>:
<Column Name> <Data Type>
[CONSTRAINT <Column Constraint>
[DEFAULT <Default Value>]]
[IDENTITY [(<Seed Value>, <Increment Value>)]
[NULL | NOT NULL]
[ENCRYPTED WITH (<Encryption Specifications>)
[<Column Constraints>]
[<Column Index Specifications>]
```

```
<Column Constraint>:
[CONSTRAINT <Constraint Name>]
{{PRIMARY KEY | UNIQUE} [CLUSTERED | NONCLUSTERED]
[WITH FILLFACTOR = <Fill Factor>]
| [FOREIGN KEY]
REFERENCES <Referenced Table> (<Referenced Columns>)]
```

```
<Column Index Specifications>:
INDEX <Index Name> [CLUSTERED | NONCLUSTERED]
[WITH(<Index Options>]
```

### Examples

The following example creates a basic table.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

The following example creates a table with column constraints and an identity.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL PRIMARY KEY IDENTITY (1,1),
    Col2 VARCHAR(20) NOT NULL CHECK (Col2 <> ''),
    Col3 VARCHAR(100) NULL
    REFERENCES MyOtherTable (Col3)
);
```

The following example creates a table with an additional index.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
    INDEX IDX_Col2 NONCLUSTERED
);
```

For more information, see [CREATE TABLE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Like SQL Server, Aurora MySQL provides ANSI/ISO syntax entry level conformity for `CREATE TABLE` and custom extensions to support Aurora MySQL specific functionality.

###### Note

Unlike SQL Server that uses a single set of physical files for each database, Aurora MySQL tables are created as separate files for each table. Therefore, the SQL Server concept of File Groups doesn’t apply to Aurora MySQL. For more information, see [Databases and Schemas](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

In its most basic form, and very similar to SQL Server, you can use the `CREATE TABLE` statement in Aurora MySQL to define:

- Table name, containing security schema, and database.
- Column names.
- Column data types.
- Column and table constraints.
- Column default values.
- Primary, unique, and foreign keys.

### Aurora MySQL Extensions

Aurora MySQL extends the basic syntax and allows many additional options to be defined as part of the `CREATE TABLE` or `ALTER TABLE` statements. The most often used options are:

- Defining `AUTO_INCREMENT` properties for auto-enumerator columns.
- Encryption.
- Compression.
- Indexes.

### Table Scope

Aurora MySQL provides two table scopes:

- Standard tables are created on disk, visible globally, and persist through connection resets and server restarts.
- Temporary tables are created using the `CREATE TEMPORARY TABLE` statement. A temporary table is visible only to the session that creates it and is dropped automatically when the session is closed.

### Creating a Table Based on an Existing Table or Query

Aurora MySQL provides two ways to create standard or temporary tables based on existing tables and queries.

`CREATE TABLE <New Table> LIKE <Source Table>` creates an empty table based on the definition of another table including any column attributes and indexes defined in the original table.

`CREATE TABLE …​ AS <Query Expression>` is similar to `SELECT INTO` in SQL Server. You can use this statement to create a new table and populate data in a single step. Unlike SQL Server, you can combine standard column definitions and additional columns derived from the query in Aurora MySQL. This statement doesn’t copy supporting objects or attributes from the source table, similar to SQL Server. For example:

```
CREATE TABLE SourceTable
(
    Col1 INT
);
```

```
INSERT INTO SourceTable
VALUES (1)
```

```
CREATE TABLE NewTable
(
    Col1 INT
)
AS
SELECT Col1 AS Col2
FROM SourceTable;
```

```
INSERT INTO NewTable (Col1, Col2)
VALUES (2,3);
```

```
SELECT * FROM NewTable
```

For the preceding examples, the result looks as shown following.

```
Col1  Col2
NULL  1
2     3
```

### Converting TIMESTAMP and ROWVERSION columns

###### Note

Aurora MySQL has a `TIMESTAMP` data type, which is a temporal type not to be confused with `TIMESTAMP` in SQL Server. For more information, see [Data Types](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md").

SQL server provides an automatic mechanism for stamping row versions for application concurrency control.

Consider the following example.

```
CREATE TABLE WorkItems
(
    WorkItemID INT IDENTITY(1,1) PRIMARY KEY,
    WorkItemDescription XML NOT NULL,
    Status VARCHAR(10) NOT NULL DEFAULT ('Pending'),
    -- other columns...
    VersionNumber ROWVERSION
);
```

The `VersionNumber` column automatically updates when a row is modified. The actual value is meaningless, just the fact that it changed is what indicates a row modification. The client can now read a work item row, process it, and ensure no other clients updated the row before updating the status.

```
SELECT @WorkItemDescription = WorkItemDescription,
    @Status = Status,
    @VersionNumber = VersionNumber
FROM WorkItems
WHERE WorkItemID = @WorkItemID;

EXECUTE ProcessWorkItem @WorkItemID, @WorkItemDescription, @Status OUTPUT;

IF (
        SELECT VersionNumber
        FROM WorkItems
        WHERE WorkItemID = @WorkItemID
    ) = @VersionNumber;
    EXECUTE UpdateWorkItems @WorkItemID, 'Completed'; -- Success
ELSE
    EXECUTE ConcurrencyExceptionWorkItem; -- Row updated while processing
```

In Aurora MySQL, you can add a trigger to maintain the updated stamp for each row.

```
CREATE TABLE WorkItems
(
    WorkItemID INT AUTO_INCREMENT PRIMARY KEY,
    WorkItemDescription JSON NOT NULL,
    Status VARCHAR(10) NOT NULL DEFAULT 'Pending',
    -- other columns...
    VersionNumber INTEGER NULL
);

CREATE TRIGGER MaintainWorkItemVersionNumber
AFTER UPDATE
ON WorkItems FOR EACH ROW
SET NEW.VersionNumber = OLD.VersionNumber + 1;
```

For more information, see [Triggers](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

### Syntax

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] <Table Name>
(<Create Definition> ,...)[<Table Options>];
```

```
<Create Definition>:
<Column Name> <Column Definition> | [CONSTRAINT [symbol]]
[PRIMARY KEY | UNIQUE | FOREIGN KEY <Foreign Key Definition> | CHECK (<Check Predicate>)]
(INDEX <Index Column Name>,...)
```

```
<Column Definition>:
<Data Type> [NOT NULL | NULL]
[DEFAULT <Default Value>]
[AUTO_INCREMENT]
[UNIQUE [KEY]] [[PRIMARY] KEY]
[COMMENT <comment>]
```

### Migration Considerations

Migrating `CREATE TABLE` statements should be mostly compatible with the SQL Server syntax when using only ANSI standard syntax.

`IDENTITY` columns should be rewritten to use the Aurora MySQL syntax of `AUTO_INCREMENT`. Note that similar to SQL Server, there can be only one such column in a table, but in Aurora MySQL it also must be indexed.

Temporary table syntax should be modified to use the `CREATE TEMPORARY TABLE` statement instead of the `CREATE #Table` syntax of SQL Server. Global temporary tables and table variables aren’t supported by Aurora MySQL. For sharing data across connections, use standard tables.

`SELECT INTO` queries should be rewritten to use `CREATE TABLE …​ AS` syntax. When copying tables, remember that the `CREATE TABLE …​ LIKE` syntax also retains all supporting objects such as constraints and indexes.

Aurora MySQL doesn’t require specifying constraint names when using the CONSTRAINT keyword. Unique constraint names are created automatically. If specifying a name, the name must be unique for the database.

Unlike SQL Server `IDENTITY` columns, which require `EXPLICIT SET IDENTITY_INSERT ON` to bypass the automatic generation, Aurora MySQL allows inserting explicit values into the column. To generate an automatic value, insert a NULL or a 0 value. To reseed the automatic value, use `ALTER TABLE` as opposed to `DBCC CHECKIDENT` in SQL Server.

In Aurora MySQL, you can add a comment to a column for documentation purposes, similar to SQL Server extended properties feature.

###### Note

Contrary to the SQL standard, foreign keys in Aurora MySQL can point to non-unique parent column values. In this case, the foreign key prohibits deletion of any of the parent rows. For more information, see [Constraints](chap-sql-server-aurora-mysql.sql.md "chap-sql-server-aurora-mysql.sql.md") and [FOREIGN KEY Constraint Differences](https://dev.mysql.com/doc/refman/5.7/en/ansi-diff-foreign-keys.html "https://dev.mysql.com/doc/refman/5.7/en/ansi-diff-foreign-keys.html") in the _MySQL documentation_.

### Examples

The following example creates a basic table.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

The following example creates a table with column constraints and an auto increment column.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
    CHECK (Col2 <> ''),
    Col3 VARCHAR(100) NULL
    REFERENCES MyOtherTable (Col3)
);
```

The following example creates a table with an additional index.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL,
    INDEX IDX_Col2 (Col2)
);
```

## Summary

The following table identifies similarities, differences, and key migration considerations.

| Feature                     | SQL Server                  | Aurora MySQL                                   | Comments                                                                                                                                                                                                                                           |
| --------------------------- | --------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ANSI compliance             | Entry level                 | Entry level                                    | Basic syntax is compatible.                                                                                                                                                                                                                        |
| Auto generated enumerator   | `IDENTITY`                  | `AUTO_INCREMENT`                               | Only one allowed for each table. In Aurora MySQL, insert NULL or 0 to generate a new value.                                                                                                                                                        |
| Reseed auto generated value | `DBCC CHECKIDENT`           | `ALTER TABLE`                                  | For more information, see [ALTER TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/alter-table.html "https://dev.mysql.com/doc/refman/5.7/en/alter-table.html").                                                                            |
| Index types                 | `CLUSTERED`, `NONCLUSTERED` | Implicit — primary keys use clustered indexes. | For more information, see [Indexes](chap-sql-server-aurora-mysql.md "chap-sql-server-aurora-mysql.md").                                                                                                                                            |
| Physical storage location   | `ON <File Group>`           | Not supported                                  | Physical storage is managed by AWS.                                                                                                                                                                                                                |
| Temporary tables            | #TempTable                  | `CREATE TEMPORARY TABLE`                       |                                                                                                                                                                                                                                                    |
| Global temporary tables     | `##GlobalTempTable`         | Not supported                                  | Use standard tables to share data between connections.                                                                                                                                                                                             |
| Table variables             | `DECLARE @Table`            | Not supported                                  |                                                                                                                                                                                                                                                    |
| Create table as query       | `SELECT…​ INTO`             | `CREATE TABLE…​ AS`                            |                                                                                                                                                                                                                                                    |
| Copy table structure        | Not supported               | `CREATE TABLE…​ LIKE`                          |                                                                                                                                                                                                                                                    |
| Memory-optimized tables     | Supported                   | Not supported                                  | For workloads that require memory resident tables, consider using Amazon ElastiCache (Redis OSS). For more information, see [Amazon ElastiCache for Redis](https://aws.amazon.com/elasticache/redis/ "https://aws.amazon.com/elasticache/redis/"). |

For more information, see [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html "https://dev.mysql.com/doc/refman/5.7/en/create-table.html") in the _MySQL documentation_.
