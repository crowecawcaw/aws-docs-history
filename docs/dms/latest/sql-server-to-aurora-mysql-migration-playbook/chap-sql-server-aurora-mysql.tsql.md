# Identity and sequences for T-SQL

This topic provides reference content comparing identity and sequence features between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the key differences and similarities in how these database systems handle automatic enumeration functions and columns, which are commonly used for generating surrogate keys.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                                               | Key differences                                                                                                                                          |
| ------------------------------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Two star feature compatibility | Three star automation level        | [Identity and Sequences](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.identitysequences "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.identitysequences") | MySQL doesn’t support `SEQUENCE` objects. Rewrite `IDENTITY` to `AUTO_INCREMENT`. Last value is evaluated as `MAX(Existing Value) + 1` on every restart. |

## SQL Server Usage

Automatic enumeration functions and columns are common with relational database management systems and are often used for generating surrogate keys.

SQL Server provides several features that support automatic generation of monotonously increasing value generators:

- The `IDENTITY` property of a table column.
- The `SEQUENCE` objects framework.
- The numeric functions such as `IDENTITY` and `NEWSEQUENTIALID`.

### Identity

The `IDENTITY` property is probably the most widely used means of generating surrogate primary keys in SQL Server applications. Each table may have a single numeric column assigned as an `IDENTITY` using the `CREATE TABLE` or `ALTER TABLE` DDL statements. You can explicitly specify a starting value and increment.

###### Note

The identity property doesn’t enforce uniqueness of column values, indexing, or any other property. Additional constraints such as primary or unique keys, explicit index specifications, or other properties must be specified in addition to the `IDENTITY` property.

The `IDENTITY` value is generated as part of the transaction that inserts table rows. Applications can obtain `IDENTITY` values using the `@@IDENTITY`, `SCOPE_IDENTITY`, and `IDENT_CURRENT` functions.

`IDENTITY` columns may be used as primary keys by themselves, as part of a compound key, or as non-key columns.

You can manage `IDENTITY` columns using the `DBCC CHECKIDENT` command, which provides functionality for reseeding and altering properties.

#### Syntax

```
IDENTITY [(<Seed Value>, <Increment Value>)]
```

View the original seed value of an `IDENTITY` column with the `IDENT_SEED` system function.

```
SELECT IDENT_SEED (<Table>)
```

Reseed an `IDENTITY` column.

```
DBCC CHECKIDENT (<Table>, RESEED, <Seed Value>)
```

#### Examples

Create a table with an `IDENTITY` primary key column.

```
CREATE TABLE MyTABLE
(
    Col1 INT NOT NULL
    PRIMARY KEY NONCLUSTERED IDENTITY(1,1),
    Col2 VARCHAR(20) NOT NULL
);
```

Insert a row and retrieve the generated `IDENTITY` value.

```
DECLARE @LastIdent INT;
INSERT INTO MyTable(Col2)
VALUES('SomeString');
SET @LastIdent = SCOPE_IDENTITY()
```

Create a table with a non-key `IDENTITY` column and an increment of 10.

```
CREATE TABLE MyTABLE
(
    Col1 VARCHAR(20) NOT NULL
        PRIMARY KEY,
    Col2 INT NOT NULL
        IDENTITY(1,10),
);
```

Create a table with a compound PK including an `IDENTITY` column.

```
CREATE TABLE MyTABLE
(
    Col1 VARCHAR(20) NOT NULL,
    Col2 INT NOT NULL
        IDENTITY(1,10),
    PRIMARY KEY (Col1, Col2)
);
```

### SEQUENCE

Sequences are objects that are independent of a particular table or column and are defined using the `CREATE SEQUENCE` DDL statement. You can manage sequences using the `ALTER SEQUENCE` statement. Multiple tables and multiple columns from the same table may use the values from one or more `SEQUENCE` objects.

You can retrieve a value from a `SEQUENCE` object using the `NEXT VALUE FOR` function. For example, a `SEQUENCE` value can be used as a default value for a surrogate key column.

`SEQUENCE` objects provide several advantages over `IDENTITY` columns:

- Can be used to obtain a value before the actual `INSERT` takes place.
- Value series can be shared among columns and tables.
- Easier management, restart, and modification of sequence properties.
- Allow assignment of value ranges using `sp_sequence_get_range` and not just per-row values.

#### Syntax

```
CREATE SEQUENCE <Sequence Name> [AS <Integer Data Type> ]
START WITH <Seed Value>
INCREMENT BY <Increment Value>;
```

```
ALTER SEQUENCE <Sequence Name>
RESTART [WITH <Reseed Value>]
INCREMENT BY <New Increment Value>;
```

#### Examples

Create a sequence for use as a primary key default.

```
CREATE SEQUENCE MySequence AS INT START WITH 1 INCREMENT BY 1;
CREATE TABLE MyTable
(
    Col1 INT NOT NULL
        PRIMARY KEY NONCLUSTERED DEFAULT (NEXT VALUE FOR MySequence),
    Col2 VARCHAR(20) NULL
);
```

```
INSERT MyTable (Col1, Col2) VALUES (DEFAULT, 'cde'), (DEFAULT, 'xyz');
```

```
SELECT * FROM MyTable;
```

```
Col1  Col2
1     cde
2     xyz
```

### Sequential Enumeration Functions

SQL Server provides two sequential generation functions: `IDENTITY` and `NEWSEQUENTIALID`.

###### Note

The `IDENTITY` function shouldn’t be confused with the `IDENTITY` property of a column.

You can use the `IDENTITY` function only in a `SELECT …​ INTO` statement to insert `IDENTITY` column values into a new table.

The `NEWSEQUNTIALID` function generates a hexadecimal GUID, which is an integer. While the `NEWID` function generates a random GUID, the `NEWSEQUENTIALID` function guarantees that every GUID created is greater in numeric value than any other GUID previously generated by the same function on the same server since the operating system restart.

###### Note

You can use `NEWSEQUENTIALID` only with `DEFAULT` constraints associated with columns having a `UNIQUEIDENTIFIER` data type.

#### Syntax

```
IDENTITY (<Data Type> [, <Seed Value>, <Increment Value>]) [AS <Alias>]
```

```
NEWSEQUENTIALID()
```

#### Examples

Use the `IDENTITY` function as surrogate key for a new table based on an existing table.

```
CREATE TABLE MySourceTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(10) NOT NULL,
    Col3 VARCHAR(10) NOT NULL
);
```

```
INSERT INTO MySourceTable
VALUES
(12, 'String12', 'String12'),
(25, 'String25', 'String25'),
(95, 'String95', 'String95');
```

```
SELECT IDENTITY(INT, 100, 1) AS SurrogateKey,
    Col1,
    Col2,
    Col3
INTO MyNewTable
FROM MySourceTable
ORDER BY Col1 DESC;
```

```
SELECT *
FROM MyNewTable;
```

For the preceding example, the result looks as shown following.

```
SurrogateKey  Col1  Col2      Col3
100           95    String95  String95
101           25    String25  String25
102           12    String12  String12
```

Use `NEWSEQUENTIALID` as a surrogate key for a new table.

```
CREATE TABLE MyTable
(
    Col1 UNIQUEIDENTIFIER NOT NULL
    PRIMARY KEY NONCLUSTERED DEFAULT NEWSEQUENTIALID()
);
```

```
INSERT INTO MyTable
DEFAULT VALUES;
```

```
SELECT *
FROM MyTable;
```

For the preceding example, the result looks as shown following.

```
Col1

9CC01320-C5AA-E811-8440-305B3A017068
```

For more information, see [Sequence Numbers](https://docs.microsoft.com/en-us/sql/relational-databases/sequence-numbers/sequence-numbers?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/sequence-numbers/sequence-numbers?view=sql-server-ver15") and [CREATE TABLE (Transact-SQL) IDENTITY (Property)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql-identity-property?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql-identity-property?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports automatic sequence generation using the `AUTO_INCREMENT` column property, similar to the `IDENTITY` column property in SQL Server.

Aurora MySQL doesn’t support table-independent sequence objects.

Any numeric column may be assigned the `AUTO_INCREMENT` property. To make the system generate the next sequence value, the application must not mention the relevant column’s name in the insert command, in case the column was created with the NOT NULL definition then also inserting a NULL value into an `AUTO_INCREMENT` column will increment it. In most cases, the seed value is 1 and the increment is 1.

Client applications use the `LAST_INSERT_ID` function to obtain the last generated value.

Each table can have only one `AUTO_INCREMENT` column. The column must be explicitly indexed or be a primary key, which is indexed by default.

The `AUTO_INCREMENT` mechanism is designed to be used with positive numbers only. Do not use negative values because they will be misinterpreted as a complementary positive value. This limitation is due to precision issues with sequences crossing a zero boundary.

There are two server parameters used to alter the default values for new `AUTO_INCREMENT` columns:

- `auto_increment_increment` — Controls the sequence interval.
- `auto_increment_offset` — Determines the starting point for the sequence.

To reseed the `AUTO_INCREMENT` value, use `ALTER TABLE <Table Name> AUTO_INCREMENT = <New Seed Value>`.

### Syntax

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] <Table Name>
(<Column Name> <Data Type> [NOT NULL | NULL]
AUTO_INCREMENT [UNIQUE [KEY]] [[PRIMARY] KEY]...
```

### Migration Considerations

Since Aurora MySQL doesn’t support table-independent `SEQUENCE` objects, applications that rely on its properties must use a custom solution to meet their requirements.

In Aurora MySQL, you can use `AUTO_INCREMENT` instead of `IDENTITY` in SQL Server for most cases. For `AUTO_INCREMENT` columns, the application must explicitly `INSERT` a NULL or a 0.

###### Note

Omitting the `AUTO_INCREMENT` column from the `INSERT` column list has the same effect as inserting a NULL value.

Make sure that your `AUTO_INCREMENT` columns are indexed and don’t have default constraints assigned to the same column. There is a critical difference between `IDENTITY` and `AUTO_INCREMENT` in the way the sequence values are maintained upon service restart. Application developers must be aware of this difference.

### Sequence Value Initialization

SQL Server stores the `IDENTITY` metadata in system tables on disk. Although some values may be cached and lost when the service is restarted, the next time the server restarts, the sequence value continues after the last block of values that was assigned to cache. If you run out of values, you can explicitly set the sequence value to start the cycle over. As long as there are no key conflicts, it can be reused after the range has been exhausted.

In Aurora MySQL, an `AUTO_INCREMENT` column for a table uses a special counter called the auto-increment counter to assign new values for the column. This counter is stored in cache memory only and isn’t persisted to disk. After a service restart, and when Aurora MySQL encounters an `INSERT` to a table containing an `AUTO_INCREMENT` column, it issues an equivalent of the following statement:

```
SELECT MAX(<Auto Increment Column>) FROM <Table Name> FOR UPDATE;
```

###### Note

The `FOR UPDATE CLAUSE` is required to maintain locks on the column until the read completes.

Aurora MySQL then increments the value retrieved by the preceding statement and assigns it to the in-memory autoincrement counter for the table. By default, the value is incremented by one. You can change the default using the `auto_increment_increment` configuration setting. If the table has no values, Aurora MySQL uses the value 1. You can change the default using the `auto_increment_offset` configuration setting.

Every server restart effectively cancels any `AUTO_INCREMENT = <Value>` table option in `CREATE TABLE` and `ALTER TABLE` statements.

Unlike `IDENTITY` columns in SQL Server, which by default don’t allow inserting explicit values, Aurora MySQL allows explicit values to be set. If a row has an explicitly specified `AUTO_INCREMENT` column value and the value is greater than the current counter value, the counter is set to the specified column value.

### Examples

Create a table with an `AUTO_INCREMENT` column.

```
CREATE TABLE MyTable
(
    Col1 INT NOT NULL
    AUTO_INCREMENT PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

Insert `AUTO_INCREMENT` values.

```
INSERT INTO MyTable (Col2)
VALUES ('AI column omitted');
```

```
INSERT INTO MyTable (Col1, Col2)
VALUES (NULL, 'Explicit NULL');
```

```
INSERT INTO MyTable (Col1, Col2)
VALUES (10, 'Explicit value');
```

```
INSERT INTO MyTable (Col2)
VALUES ('Post explicit value');
```

```
SELECT *
FROM MyTable;
```

For the preceding example, the result looks as shown following.

```
Col1  Col2
1     AI column omitted
2     Explicit NULL
10    Explicit value
11    Post explicit value
```

Reseed `AUTO_INCREMENT`.

```
ALTER TABLE MyTable AUTO_INCREMENT = 30;
```

```
INSERT INTO MyTable (Col2)
VALUES ('Post ALTER TABLE');
```

```
SELECT *
FROM MyTable;
```

For the preceding example, the result looks as shown following.

```
1     AI column omitted
2     Explicit NULL
10    Explicit value
11    Post explicit value
30    Post ALTER TABLE
```

Change the increment value to 10.

###### Note

Changing the `@@auto_increment_increment` value to 10 impacts all `AUTO_INCREMENT` enumerators in the database.

```
SET @@auto_increment_increment=10;
```

Verify variable change.

```
SHOW VARIABLES LIKE 'auto_inc%';
```

For the preceding example, the result looks as shown following.

```
Variable_name             Value
auto_increment_increment  10
auto_increment_offset     1
```

Insert several rows and then read.

```
INSERT INTO MyTable (Col1, Col2)
VALUES (NULL, 'Row1'), (NULL, 'Row2'), (NULL, 'Row3'), (NULL, 'Row4');
```

```
SELECT Col1, Col2
FROM MyTable;
```

For the preceding example, the result looks as shown following.

```
1     AI column omitted
2     Explicit NULL
10    Explicit value
11    Post explicit value
30    Post ALTER TABLE
40    Row1
50    Row2
60    Row3
70    Row4
```

## Summary

The following table identifies similarities, differences, and key migration considerations.

| Feature                                 | SQL Server                                                | Aurora MySQL                                                 | Comments                                                                                                                                                                                                          |
| --------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Independent `SEQUENCE` object           | `CREATE SEQUENCE`                                         | Not supported                                                |                                                                                                                                                                                                                   |
| Automatic enumerator column property    | `IDENTITY`                                                | `AUTO_INCREMENT`                                             |                                                                                                                                                                                                                   |
| Reseed sequence value                   | `DBCC CHECKIDENT`                                         | `ALTER TABLE <Table Name> AUTO_INCREMENT = <New Seed Value>` |                                                                                                                                                                                                                   |
| Column restrictions                     | Numeric                                                   | Numeric, indexed, and no `DEFAULT`                           |                                                                                                                                                                                                                   |
| Controlling seed and interval values    | `CREATE/ALTER TABLE`                                      | `auto_increment_increment`<br>`auto_increment_offset`        | Aurora MySQL settings are global and can’t be customized for each column as in SQL Server.                                                                                                                        |
| Sequence setting initialization         | Maintained through service restarts                       | Re-initialized every service restart                         | For more information, see [Sequence Value Initialization](#chap-sql-server-aurora-mysql.tsql.identitysequences.mysql.initialization "#chap-sql-server-aurora-mysql.tsql.identitysequences.mysql.initialization"). |
| Explicit values to column               | Not allowed by default, `SET IDENTITY_INSERT ON` required | Supported                                                    | Aurora MySQL requires explicit NULL or 0 to trigger sequence value assignment. Inserting an explicit value larger than all others will reinitialize the sequence.                                                 |
| Non PK auto enumerator column           | Supported                                                 | Not Supported                                                | Implement an application enumerator.                                                                                                                                                                              |
| Compound PK with auto enumerator column | Supported                                                 | Not Supported                                                | Implement an application enumerator.                                                                                                                                                                              |

For more information, see [Using AUTO_INCREMENT](https://dev.mysql.com/doc/refman/5.7/en/example-auto-increment.html "https://dev.mysql.com/doc/refman/5.7/en/example-auto-increment.html"), [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html "https://dev.mysql.com/doc/refman/5.7/en/create-table.html"), and [AUTO_INCREMENT Handling in InnoDB](https://dev.mysql.com/doc/refman/5.7/en/innodb-auto-increment-handling.html#innodb-auto-increment-initialization.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-auto-increment-handling.html#innodb-auto-increment-initialization.html") in the _MySQL documentation_.
