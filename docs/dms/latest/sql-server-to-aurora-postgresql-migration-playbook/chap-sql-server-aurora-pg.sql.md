# Creating tables for ANSI SQL

This topic provides reference information comparing the creation of tables in Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can understand the similarities and differences in table creation syntax, features, and capabilities between these two database systems. The topic highlights key aspects such as table and column naming, data types, constraints, and auto-generated values.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                      | Key differences                                                                                                                 |
| -------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Three star feature compatibility | Four star automation level         | [Creating Tables](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.tables "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.tables") | Auto generated value column is different. Can’t use physical attribute `ON`. Missing table variable and memory-optimized table. |

## SQL Server Usage

### ANSI Syntax Conformity

You can create tables in SQL Server using the `CREATE TABLE` statement and conform to the ANSI/ISO entry level standard. The basic features of `CREATE TABLE` are similar for most relational database management engines and are well defined in the ANSI/ISO standards.

In its most basic form, the `CREATE TABLE` statement in SQL Server is used to define:

- Table names, the containing security schema, and database.
- Column names.
- Column data types.
- Column and table constraints.
- Column default values.
- Primary, candidate (UNIQUE), and foreign keys.

### T-SQL Extensions

SQL Server extends the basic syntax and provides many additional options for the `CREATE TABLE` or `ALTER TABLE` statements. The most often used options are:

- Supporting index types for primary keys and unique constraints, clustered or non-clustered, and index properties such as `FILLFACTOR`.
- Physical table data storage containers using the `ON <File Group>` clause.
- Defining `IDENTITY` auto-enumerator columns.
- Encryption.
- Compression.
- Indexes.

For more information, see [Data Types](chap-sql-server-aurora-pg.sql.md "chap-sql-server-aurora-pg.sql.md"), [Column Encryption](chap-sql-server-aurora-pg.security.md "chap-sql-server-aurora-pg.security.md"), and [Databases and Schemas](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

### Table Scope

SQL Server provides five scopes for tables

- Standard tables are created on disk, globally visible, and persist through connection resets and server restarts.
- Temporary tables are designated with the "# " prefix. They are persisted in TempDB and are visible to the run scope and any sub-scopes where they were created. Temporary tables are cleaned up by the server when the run scope terminates and when the server restarts.
- Global temporary tables are designated by the "## " prefix. They are similar in scope to temporary tables, but are also visible to concurrent scopes.
- Table variables are defined with the `DECLARE` statement, not with `CREATE TABLE`. They are visible only to the run scope where they were created.
- Memory-optimized tables are special types of tables used by the In-Memory Online Transaction Processing (OLTP) engine. They use a non-standard `CREATE TABLE` syntax.

### Creating a Table Based on an Existing Table or Query

In SQL Server, you can create new tables based on `SELECT` queries as an alternate to the `CREATE TABLE` statement. You can use a `SELECT` statement that returns a valid set with unique column names to create a new table and populate data.

`SELECT INTO` is a combination of DML and DDL. The simplified syntax for `SELECT INTO` is shown following.

```
SELECT <Expression List>
INTO <Table Name>
[FROM <Table Source>]
[WHERE <Filter>]
[GROUP BY <Grouping Expressions>...];
```

When you create a new table using `SELECT INTO`, the only attributes created for the new table are column names, column order, and the data types of the expressions. Even a straight forward statement such as` SELECT \* INTO <New Table> FROM <Source Table>` doesn’t copy constraints, keys, indexes, identity property, default values, or any other related objects.

### TIMESTAMP Syntax for ROWVERSION Deprecated Syntax

The `TIMESTAMP` syntax synonym for `ROWVERSION` has been deprecated as of SQL Server 2008R2 in accordance with [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)").

Previously, you could use either the `TIMESTAMP` or the `ROWVERSION` keywords to denote a special data type that exposes an auto-enumerator. The auto-enumerator generates unique eight-byte binary numbers typically used to version-stamp table rows. Clients read the row, process it, and check the `ROWVERSION` value against the current row in the table before modifying it. If they are different, the row has been modified since the client read it. The client can then apply different processing logic.

Note that when migrating to Aurora PostgreSQL using the AWS Schema Conversion Tool, neither `ROWVERSION` nor `TIMESTAMP` are supported. You must add customer logic, potentially in the form of a trigger, to maintain this functionality.

### Syntax

Simplified syntax for `CREATE TABLE` is shown following.

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

Create a basic table.

```
CREATE TABLE MyTable
(
Col1 INT NOT NULL PRIMARY KEY,
Col2 VARCHAR(20) NOT NULL
);
```

Create a table with column constraints and an identity.

```
CREATE TABLE MyTable
(
Col1 INT NOT NULL PRIMARY KEY IDENTITY (1,1),
Col2 VARCHAR(20) NOT NULL CHECK (Col2 <> ''),
Col3 VARCHAR(100) NULL
REFERENCES MyOtherTable (Col3)
);
```

Create a table with an additional index.

```
CREATE TABLE MyTable
(
Col1 INT NOT NULL PRIMARY KEY,
Col2 VARCHAR(20) NOT NULL
INDEX IDX_Col2 NONCLUSTERED
);
```

For more information, see [CREATE TABLE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

As SQL Server, Aurora PostgreSQL provides ANSI/ISO syntax entry level conformity for `CREATE TABLE` and custom extensions to support Aurora PostgreSQL specific functionality.

In its most basic form, and very similar to SQL Server, the `CREATE TABLE` statement in Aurora PostgreSQL is used to define:

- Table names containing security schema and/or database.
- Column names.
- Column data types.
- Column and table constraints.
- Column default values.
- Primary, candidate (UNIQUE), and foreign keys.

Starting with PostgreSQL 12 support for generated columns has been added. Generated columns can be either calculated from other columns values on the fly or calculated and stored.

```
CREATE TABLE tst_gen(
n NUMERIC,
n_gen GENERATED ALWAYS AS (n*0.01)
);
```

### Aurora PostgreSQL Extensions

Aurora PostgreSQL extends the basic syntax and allows many additional options to be defined as part of the `CREATE TABLE` or `ALTER TABLE` statements. The most often used option is in-line index definition.

### Table Scope

Aurora PostgreSQL provides two table scopes:

- Standard tables are created on disk, visible globally, and persist through connection resets and server restarts.
- Temporary tables are created using the `CREATE GLOBAL TEMPORARY TABLE` statement. A `TEMPORARY` table is visible only to the session that creates it and is dropped automatically when the session is closed.

### Creating a Table Based on an Existing Table or Query

Aurora PostgreSQL provides two ways to create standard or temporary tables based on existing tables and queries: `CREATE TABLE <New Table> LIKE <Source Table>` and `CREATE TABLE …​ AS <Query Expression>`.

`CREATE TABLE <New Table> LIKE <Source Table>` creates an empty table based on the definition of another table including any column attributes and indexes defined in the original table.

`CREATE TABLE …​ AS <Query Expression>` is very similar to `SELECT INTO` in SQL Server. You can use this query to create a new table and populate data in a single step.

The following code example creates a new empty table based on the definition of the SourceTable table.

```
CREATE TABLE SourceTable(Col1 INT);

INSERT INTO SourceTable VALUES (1);

CREATE TABLE NewTable AS SELECT Col1 AS Col2 FROM SourceTable;

INSERT INTO NewTable (Col2) VALUES (2);

SELECT * FROM NewTable;
Col2
1
2
```

### Converting TIMESTAMP and ROWVERSION Columns

The following code example shows how you can use SQL server to provide an automatic mechanism for stamping row versions for application concurrency control.

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

The VersionNumber column automatically updates when a row is modified. The actual value is meaningless. Just the fact that it changed is what indicates a row modification. The client can now read a work item row, process it, and ensure no other clients updated the row before updating the status.

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

In Aurora PostgreSQL, you can add a trigger to maintain the updated stamp for each row.

```
CREATE OR REPLACE FUNCTION IncByOne()
  RETURNS TRIGGER
  AS $$
  BEGIN
    UPDATE WorkItems SET VersionNumber = VersionNumber+1
    WHERE WorkItemID = OLD.WorkItemID;
  END; $$
  LANGUAGE PLPGSQL;

CREATE TRIGGER MaintainWorkItemVersionNumber
  AFTER UPDATE OF WorkItems
  FOR EACH ROW
  EXECUTE PROCEDURE IncByOne();
```

For more information, see [Triggers](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

### Syntax

```
CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ]
table_name ( [
{ column_name data_type [ COLLATE collation ] [ column_constraint [ ... ] ]
| table_constraint
| LIKE source_table [ like_option ... ] }
[, ... ]
] )
[ INHERITS ( parent_table [, ... ] ) ]
[ PARTITION BY { RANGE | LIST } ( { column_name | ( expression ) } [ COLLATE collation
] [ opclass ] [, ... ] ) ]
[ WITH ( storage_parameter [= value] [, ... ] ) | WITH OIDS | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]
```

```
CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ]
table_name
OF type_name [ (
{ column_name [ WITH OPTIONS ] [ column_constraint [ ... ] ]
| table_constraint }
[, ... ]
) ]
[ PARTITION BY { RANGE | LIST } ( { column_name | ( expression ) } [ COLLATE collation
] [ opclass ] [, ... ] ) ]
[ WITH ( storage_parameter [= value] [, ... ] ) | WITH OIDS | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]
```

```
CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ]
table_name
PARTITION OF parent_table [ (
{ column_name [ WITH OPTIONS ] [ column_constraint [ ... ] ]
| table_constraint }
[, ... ]
) ] FOR VALUES partition_bound_spec
[ PARTITION BY { RANGE | LIST } ( { column_name | ( expression ) } [ COLLATE collation
] [ opclass ] [, ... ] ) ]
[ WITH ( storage_parameter [= value] [, ... ] ) | WITH OIDS | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]
```

The `column_constraint` is:

```
[ CONSTRAINT constraint_name ]
{ NOT NULL |
NULL |
CHECK ( expression ) [ NO INHERIT ] |
DEFAULT default_expr |
GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY [ ( sequence_options ) ] |
UNIQUE index_parameters |
PRIMARY KEY index_parameters |
REFERENCES reftable [ ( refcolumn ) ] [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ]
[ ON DELETE action ] [ ON UPDATE action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
```

The `table_constraint` is:

```
[ CONSTRAINT constraint_name ]
{ CHECK ( expression ) [ NO INHERIT ] |
UNIQUE ( column_name [, ... ] ) index_parameters |
PRIMARY KEY ( column_name [, ... ] ) index_parameters |
EXCLUDE [ USING index_method ] ( exclude_element WITH operator [, ... ] ) index_parameters
[ WHERE ( predicate ) ] |
FOREIGN KEY ( column_name [, ... ] ) REFERENCES reftable [ ( refcolumn [, ... ] ) ]
[ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ] [ ON DELETE action ] [ ON UPDATE
action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
```

The `like_option` is:

```
{ INCLUDING | EXCLUDING } { COMMENTSDEFAULTS | CONSTRAINTS | DEFAULTS | IDENTITY |
INDEXES | STATISTICS | STORAGE |COMMENTS | ALL }
```

The `partition_bound_spec` is:

```
IN ( { numeric_literal | string_literal | TRUE | FALSE | NULL } [, ...] ) |
FROM ( { numeric_literal | string_literal | TRUE | FALSE | MINVALUE | MAXVALUE } [,
...] )
TO ( { numeric_literal | string_literal | TRUE | FALSE | MINVALUE | MAXVALUE } [,
...] )
```

The `index_parameters` in `UNIQUE`, `PRIMARY KEY`, and `EXCLUDE` constraints are:

```
[ WITH ( storage_parameter [= value] [, ... ] ) ]
[ USING INDEX TABLESPACE tablespace_name ]
```

The `exclude_element` in an `EXCLUDE` constraint is:

```
{ column_name | ( expression ) } [ opclass ] [ ASC | DESC ] [ NULLS { FIRST | LAST } ]
```

### Examples

Create a basic table.

```
CREATE TABLE MyTable
(
Col1 INT PRIMARY KEY,
Col2 VARCHAR(20) NOT NULL
);
```

Create a table with column constraints.

```
CREATE TABLE MyTable
(
Col1 INT PRIMARY KEY,
Col2 VARCHAR(20) NOT NULL
  CHECK (Col2 <> ''),
Col3 VARCHAR(100) NULL
  REFERENCES MyOtherTable (Col3)
);
```

## Summary

| Feature                     | SQL Server                    | Aurora PostgreSQL                                                           |
| --------------------------- | ----------------------------- | --------------------------------------------------------------------------- |
| ANSI compliance             | Entry level                   | Entry level                                                                 |
| Auto generated enumerator   | `IDENTITY`                    | `SERIAL`                                                                    |
| Reseed auto generated value | `DBCC CHECKIDENT`             | N/A                                                                         |
| Index types                 | `CLUSTERED` or `NONCLUSTERED` | See [Indexes](chap-sql-server-aurora-pg.md "chap-sql-server-aurora-pg.md"). |
| Physical storage location   | `ON <File Group>`             | Not supported                                                               |
| Temporary tables            | `#TempTable`                  | `CREATE TEMPORARY TABLE`                                                    |
| Global temporary tables     | `##GlobalTempTable`           | `CREATE GLOBAL TEMPORARY TABLE`                                             |
| Table variables             | `DECLARE @Table`              | Not supported                                                               |
| Create table as query       | `SELECT…​ INTO`               | `CREATE TABLE…​ AS`                                                         |
| Copy table structure        | Not supported                 | `CREATE TABLE…​ LIKE`                                                       |
| Memory-optimized tables     | Supported                     | N/A                                                                         |

For more information, see [CREATE TABLE](https://www.postgresql.org/docs/13/sql-createtable.html "https://www.postgresql.org/docs/13/sql-createtable.html") in the _PostgreSQL documentation_.
