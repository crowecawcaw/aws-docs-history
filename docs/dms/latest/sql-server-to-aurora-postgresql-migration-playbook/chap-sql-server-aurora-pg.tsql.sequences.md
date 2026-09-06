

# Identity and sequences for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.sequences"></a>

This topic provides reference information comparing automatic enumeration features between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. It focuses on how these databases handle sequence generation and identity columns, which are commonly used for creating surrogate keys in relational database systems.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  | N/A | Less options with `SERIAL`. Reseeding needs to be rewritten. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver"></a>

Automatic enumeration functions and columns are common with relational database management systems and are often used for generating surrogate keys.

SQL Server provides several features that support automatic generation of monotonously increasing value generators.
+  `IDENTITY` property of a table column.
+  `SEQUENCE` objects framework.
+ Numeric functions such as `IDENTITY` and `NEWSEQUENTIALID`.

### Identity
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.identity"></a>

The `IDENTITY` property is probably the most widely used means of generating surrogate primary keys in SQL Server applications. Each table may have a single numeric column assigned as an `IDENTITY`, using the `CREATE TABLE` or `ALTER TABLE` DDL statements. You can explicitly specify a starting value and increment.

**Note**  
The identity property doesn’t enforce uniqueness of column values, indexing, or any other property. Additional constraints such as primary or unique keys, explicit index specifications, or other properties must be specified in addition to the `IDENTITY` property.

The `IDENTITY` value is generated as part of the transaction that inserts table rows. Applications can obtain `IDENTITY` values using the `@@IDENTITY`, `SCOPE_IDENTITY`, and `IDENT_CURRENT` functions.

You can manage `IDENTITY` columns using the `DBCC CHECKIDENT` command, which provides functionality for reseeding and altering properties.

#### Syntax
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.identity.syntax"></a>

```
IDENTITY [(<Seed Value>, <Increment Value>)]
```

#### Examples
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.identity.examples"></a>

The following example creates a table with an `IDENTITY` column.

```
CREATE TABLE MyTABLE
(
  Col1 INT NOT NULL
  PRIMARY KEY NONCLUSTERED IDENTITY(1,1),
  Col2 VARCHAR(20) NOT NULL
);
```

The following example inserts a row and retrieve the generated `IDENTITY` value.

```
DECLARE @LastIdent INT;
INSERT INTO MyTable(Col2)
VALUES('SomeString');
SET @LastIdent = SCOPE_IDENTITY()
```

The following example creates a table with a non-key `IDENTITY` column and an increment of 10.

```
CREATE TABLE MyTABLE
(
  Col1 VARCHAR(20) NOT NULL
  PRIMARY KEY,
  Col2 INT NOT NULL
  IDENTITY(1,10),
);
```

The following example creates a table with a compound primary key including an `IDENTITY` column.

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
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.sequence"></a>

Sequences are objects that are independent of a particular table or column and are defined using the `CREATE SEQUENCE` DDL statement. You can manage sequences using the `ALTER SEQUENCE` statement. Multiple tables and multiple columns from the same table may use the values from one or more `SEQUENCE` objects.

You can retrieve a value from a `SEQUENCE` object using the `NEXT VALUE FOR` function. For example, a `SEQUENCE` value can be used as a default value for a surrogate key column.

 `SEQUENCE` objects provide several advantages over `IDENTITY` columns:
+ You can use `SEQUENCE` objects to obtain a value before the actual `INSERT` takes place.
+ You can share value series among columns and tables.
+ Easier management, restart, and modification of sequence properties.
+ Allows assignment of value ranges using `sp_sequence_get_range` and not just per-row values.

#### Syntax
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.sequence.syntax"></a>

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
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.sequence.examples"></a>

The following example creates sequence and uses it for a primary key default.

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

### Identity
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.enumeration"></a>

SQL Server provides two sequential generation functions: `IDENTITY` and `NEWSEQUENTIALID`.

**Note**  
The IDENTITY function should not be confused with the IDENTITY property of a column.

You can use the IDENTITY function only in a `SELECT …​ INTO` statement to insert `IDENTITY` column values into a new table.

The `NEWSEQUNTIALID` function generates a hexadecimal GUID, which is an integer. While the `NEWID` function generates a random GUID, the `NEWSEQUENTIALID` function guarantees that every GUID created is greater (in numeric value) than any other GUID previously generated by the same function on the same server since the operating system restart.

You can use `NEWSEQUENTIALID` only with `DEFAULT` constraints associated with columns having a `UNIQUEIDENTIFIER` data type.

#### Syntax
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.enumeration.syntax"></a>

```
IDENTITY (<Data Type> [, <Seed Value>, <Increment Value>]) [AS <Alias>]
```

```
NEWSEQUENTIALID()
```

#### Examples
<a name="chap-sql-server-aurora-pg.tsql.sequences.sqlserver.enumeration.examples"></a>

The following example uses the `IDENTITY` function as surrogate key for a new table based on an existing table.

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

```
SurrogateKey  Col1  Col2      Col3
100           95    String95  String95
101           25    String25  String25
102           12    String12  String12
```

The following example uses `NEWSEQUENTIALID` as a surrogate key for a new table.

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

```
Col1

9CC01320-C5AA-E811-8440-305B3A017068
```

For more information, see [Sequence Numbers](https://docs.microsoft.com/en-us/sql/relational-databases/sequence-numbers/sequence-numbers?view=sql-server-ver15) and [CREATE TABLE (Transact-SQL) IDENTITY (Property)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql-identity-property?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.sequences.pg"></a>

The PostgreSQL `CREATE SEQUENCE` command is mostly compatible with the SQL Server `CREATE SEQUENCE` command. Sequences in PostgreSQL serve the same purpose as in SQL Server; they generate numeric identifiers automatically. A sequence object is owned by the user that created it.

### Sequence Parameters
<a name="chap-sql-server-aurora-pg.tsql.sequences.pg.parameters"></a>
+  `TEMPORARY` or `TEMP` — PostgreSQL can create a temporary sequence within a session. Once the session ends, the sequence is automatically dropped.
+  `IF NOT EXISTS` — Creates a sequence. If a sequence with an identical name already exists, it is replaced.
+  `INCREMENT BY` — An optional parameter with a default value of 1. Positive values generate sequence values in ascending order. Negative values generate sequence values in descending sequence.
+  `START WITH` — An optional parameter having a default of 1. It uses the MINVALUE for ascending sequences and the MAXVALUE for descending sequences.
+  `MAXVALUE` \| `NO MAXVALUE` — Defaults are between 263 for ascending sequences and -1 for descending sequences.
+  `MINVALUE` \| `NO MINVALUE` — Defaults are between 1 for ascending sequences and -263 for descending sequences.
+  `CYCLE` \| `NO CYCLE` — If the sequence value reaches `MAXVALUE` or `MINVALUE`, the `CYCLE` parameter instructs the sequence to return to the initial value (`MINVALUE` or `MAXVALUE`). The default is `NO CYCLE`.
+  `CACHE` — In PostgreSQL, the `NOCACHE` isn’t supported. By default, when the `CACHE` parameter isn’t specified, no sequence values are pre-cached into memory (equivalent to the SQL Server `NOCACHE` parameter). The minimum value is 1.
+  `OWNED BY` \| `OWNBY NON` — Specifies that the sequence object is to be associated with a specific column in a table. When dropping this type of sequence, an error is returned due to the sequence/table association.
+  `AS data_type` — This option is available in PostgreSQL version 10 and higher. To easily determine the minimum and maximum values and also improve storage management, you can select the data type for the sequence. The available data types are smallint, integer, and bigint. The default data type is bigint.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.sequences.pg.syntax"></a>

```
CREATE [ TEMPORARY | TEMP ] SEQUENCE [ IF NOT EXISTS ] name
[ INCREMENT [ BY ] increment ]
[ MINVALUE minvalue | NO MINVALUE ] [ MAXVALUE maxvalue | NO MAXVALUE ]
[ START [ WITH ] start ] [ CACHE cache ] [ [ NO ] CYCLE ]
[ OWNED BY { table_name.column_name | NONE } ]
```

Most SQL Server `CREATE SEQUENCE` parameters are compatible with PostgreSQL.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.sequences.pg.examples"></a>

The following example creates a sequence.

```
CREATE SEQUENCE SEQ_1 START WITH 100
  INCREMENT BY 1 MAXVALUE 99999999999 CACHE 20 NO CYCLE;
```

The following example drops a sequence.

```
DROP SEQUENCE SEQ_1;
```

View sequences created in the current schema and sequence specifications.

```
SELECT * FROM INFORMATION_SCHEMA.SEQUENCES;
OR
\ds
```

The following example uses a PostgreSQL sequence as part of a `CREATE TABLE` and an `INSERT` statement.

```
CREATE TABLE SEQ_TST
(COL1 NUMERIC DEFAULT NEXTVAL('SEQ_1') PRIMARY KEY, COL2 VARCHAR(30));
INSERT INTO SEQ_TST (COL2) VALUES('A');
SELECT * FROM SEQ_TST;

col1  col2
100   A
```

Use the OWNED BY parameter to associate the sequence with a table.

```
CREATE SEQUENCE SEQ_1 START WITH 100 INCREMENT BY 1 OWNED BY SEQ_TST.COL1;
```

Query the current value of a sequence.

```
SELECT CURRVAL('SEQ_1);
```

Manually increment a sequence value according to the `INCREMENT BY` value.

```
SELECT NEXTVAL('SEQ_1');
OR
SELECT SETVAL('SEQ_1', 200);
```

Alter an existing sequence.

```
ALTER SEQUENCE SEQ_1 MAXVALUE 1000000;
```

### IDENTITY Usage
<a name="chap-sql-server-aurora-pg.tsql.sequences.pg.identity"></a>

Starting from PostgreSQL 10, there is a new option called identity columns which is similar to the `SERIAL` data type but more SQL standard compliant. The identity columns are slightly more compatible compared to SQL Server identity columns.

To create a table with identity columns, use the following statement:

```
CREATE TABLE emps (
  emp_id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  emp_name VARCHAR(35) NOT NULL);

INSERT INTO emps (emp_name) VALUES ('Robert');
INSERT INTO emps (emp_id, emp_name) VALUES (DEFAULT, 'Brian');

SELECT * FROM emps;

col1  col2
1     Robert
2     Brian
```

In PostgreSQL, for `SERIAL` and `IDENTITY`, you can insert any value, so long as it won’t violate the primary key constraint. If the value violates the primary key constraint and you use the identity column sequence value again, the following error might be raised:

```
SQL Error [23505]: ERROR: duplicate key value violates unique constraint "emps_iden_pkey"
Detail: Key (emp_id)=(2) already exists.
```

### SERIAL Usage
<a name="chap-sql-server-aurora-pg.tsql.sequences.pg.serial"></a>

In PostgreSQL, you can create a sequence similar to the `IDENTITY` property supported by identity columns. When you create a new table, the sequence is created through the `SERIAL` pseudo-type. Other types from the same family are `SMALLSERIAL` and `BIGSERIAL`.

By assigning a `SERIAL` type to a column during table creation, PostgreSQL creates a sequence using the default configuration and adds a NOT NULL constraint to the column. The newly created sequence behaves like a regular sequence (incremented by 1) and no composite `SERIAL` option.

The following example uses `SERIAL` sequence.

```
CREATE TABLE SERIAL_SEQ_TST(COL1 SERIAL PRIMARY KEY, COL2 VARCHAR(10));

INSERT INTO SERIAL_SEQ_TST(COL2) VALUES('A');
SELECT * FROM SERIAL_SEQ_TST;

col1  col2
1     A

\ds

Schema  Name                     Type      Owner
public  serial_seq_tst_col1_seq  sequence  pg_tst_db
```

The following example uses the PostgreSQL `SERIAL` pseudo-type with a sequence that is created implicitly.

```
CREATE TABLE SERIAL_SEQ_TST(COL1 SERIAL PRIMARY KEY, COL2 VARCHAR(10));

\ds

Schema  Name                     Type      Owner
public  serial_seq_tst_col1_seq  sequence  pg_tst_db

ALTER SEQUENCE SERIAL_SEQ_TST_COL1_SEQ RESTART WITH 100 INCREMENT BY 10;
INSERT INTO SERIAL_SEQ_TST(COL2) VALUES('A');
INSERT INTO SERIAL_SEQ_TST(COL1, COL2) VALUES(DEFAULT, 'B');
SELECT * FROM SERIAL_SEQ_TST;

col1  col2
100   A
110   B
```

Use the `ALTER SEQUENCE` command to change the default sequence configuration in a `SERIAL` column.

Create a table with a `SERIAL` column that uses increments of 10:

```
CREATE TABLE SERIAL_SEQ_TST(COL1 SERIAL PRIMARY KEY, COL2 VARCHAR(10));

ALTER SEQUENCE serial_seq_tst_col1_seq INCREMENT BY 10;
```

**Note**  
The auto generated sequence’s name should be created with the following format: `TABLENAME_COLUMNNAME_seq`.

Create a table with a compound primary key including a `SERIAL` column:

```
CREATE TABLE SERIAL_SEQ_TST
(COL1 SERIAL, COL2 VARCHAR(10), PRIMARY key (COL1,COL2));
```

## Summary
<a name="chap-sql-server-aurora-pg.tsql.sequences.summary"></a>

The following table identifies similarities, differences, and key migration considerations.


| Feature | SQL Server |  Aurora PostgreSQL  | 
| --- | --- | --- | 
| Independent `SEQUENCE` object |  `CREATE SEQUENCE`  |  `CREATE SEQUENCE`  | 
| Automatic enumerator column property |  `IDENTITY`  |  `SERIAL` or `IDENTITY`  | 
| Reseed sequence value |  `DBCC CHECKIDENT`  |  1.  Find sequence name: `pg_get_serial_sequence('[table_name]', '[serial_field_name]')`  <br />2.   `SELECT SETVALSELECT pg_get_serial_sequence('table_name', 'person_id', 1, false);`    | 
| Column restrictions | Numeric | Numeric | 
| Controlling seed and interval values |  `CREATE/ALTER SEQUENCE`  |  `CREATE/ALTER SEQUENCE`  | 
| Sequence setting initialization | Maintained through service restarts |  `ALTER SEQUENCE`  | 
| Explicit values to column | Not allowed by default, `SET IDENTITY_INSERT ON` required | Allowed | 

For more information, see [CREATE SEQUENCE](https://www.postgresql.org/docs/13/sql-createsequence.html), [Sequence Manipulation Functions](https://www.postgresql.org/docs/13/functions-sequence.html), [Numeric Types](https://www.postgresql.org/docs/13/datatype-numeric.html), and [CREATE TABLE](https://www.postgresql.org/docs/13/sql-createtable.html) in the *PostgreSQL documentation*.