# Data types for ANSI SQL

This topic provides reference information about data type compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can use this information to understand how various SQL Server data types map to their PostgreSQL equivalents during migration

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                               | Key differences                  |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| Four star feature compatibility | Four star automation level         | [Data Types](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.types "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.types") | Syntax and handling differences. |

## SQL Server Usage

In SQL Server, each table column, variable, expression, and parameter has an associated data type. SQL Server provides a rich set of built-in data types as summarized in the following table.

| Category                | Data types                                                                                                  |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| Numeric                 | `BIT`, `TINYINT`, `SMALLINT`, `INT`, `BIGINT`, `NUMERIC`, `DECIMAL`, `MONEY`, `SMALLMONEY`, `FLOAT`, `REAL` |
| String and Character    | `CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`                                                                      |
| Temporal                | `DATE`, `TIME`, `SMALLDATETIME`, `DATETIME`, `DATETIME2`, `DATETIMEOFFSET`                                  |
| Binary                  | `BINARY`, `VARBINARY`                                                                                       |
| Large Object (LOB)      | `TEXT`, `NTEXT`, `IMAGE`, `VARCHAR(MAX)`, `NVARCHAR(MAX)`, `VARBINARY(MAX)`                                 |
| Cursor                  | `CURSOR`                                                                                                    |
| GUID                    | `UNIQUEIDENTIFIER`                                                                                          |
| Hierarchical identifier | `HIERARCHYID`                                                                                               |
| Spatial                 | `GEOMETRY`, `GEOGRAPHY`                                                                                     |
| Sets (table type)       | `TABLE`                                                                                                     |
| XML                     | `XML`                                                                                                       |
| Other specialty types   | `ROW VERSION`, `SQL_VARIANT`                                                                                |

You can create custom user defined data types using T-SQL, and the .NET Framework. Custom data types are based on the built-in system data types and are used to simplify development. For more information, see [User-Defined Types](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

### TEXT, NTEXT, and IMAGE Deprecated Data Types

The `TEXT`, `NTEXT`, and `IMAGE` data types have been deprecated as of SQL Server 2008R2. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)") in the _SQL Server documentation_.

These data types are legacy types for storing `BLOB` and `CLOB` data. The `TEXT` data type was used to store ASCII text `CLOBS`, the `NTEXT` data type to store `UNICODE CLOBS`, and `IMAGE` was used as a generic data type for storing all `BLOB` data. In SQL Server 2005, Microsoft introduced the new and improved `VARCHAR (MAX)`, `NVARCHAR(MAX)`, and `VARBINARY(MAX)` data types as the new BLOB and CLOB standard. These new types support a wider range of functions and operations. They also provide enhanced performance over the legacy types.

If your code uses `TEXT`, `NTEXT` or `IMAGE` data types, AWS SCT automatically converts them to the appropriate Aurora PostgreSQL
`BYTEA` data type. Also, AWS SCT converts `TEXT` and `NTEXT` data types to `LONGTEXT` and `IMAGE` to `LONGBLOB`. Make sure you use the proper collations. For more information, see the [SQL Server Collations and PostgreSQL Encoding](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

### Examples

Define table columns.

```
CREATE TABLE MyTable
(
Col1 AS INTEGER NOT NULL PRIMARY KEY,
Col2 AS NVARCHAR(100) NOT NULL
);
```

Define variable types.

```
DECLARE @MyXMLType AS XML,
  @MyTemporalType AS DATETIME2
```

```
DECLARE @MyTableType
AS TABLE
(
Col1 AS BINARY(16) NOT NULL PRIMARY KEY,
Col2 AS XML NULL
);
```

For more information, see [Data types (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL provides multiple data types equivalent to certain SQL Server data types. The following tables include the full list of PostgreSQL data types.

**Character data types**

| SQL Server data type | SQL Server data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type |
| -------------------- | ----------------------------------- | ---------------------------------- | ---------------------------------- |
| CHAR                 | Fixed length 1-8,000                | Yes                                | CHAR                               |
| VARCHAR              | Variable length 1-8,000             | Yes                                | VARCHAR                            |
| NCHAR                | Fixed length 1-4,000                | Yes                                | CHAR (n)                           |
| NVARCHAR             | Variable length 1-4,000             | Yes                                | VARCHAR (n)                        |

**Numeric data types**

| SQL Server data type | SQL Server data type characteristic                                                     | PostgreSQL identical compatibility | PostgreSQL corresponding data type |
| -------------------- | --------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------- |
| BIT                  | First 8 BIT column will consume 1 byte, 9 to 16 BIT columns will be 2 bytes, and so on. | Yes                                | BIT                                |
| TINYINT              | 8-bit unsigned integer, 0 to 255                                                        | No                                 | SMALLINT                           |
| SMALLINT             | 16-bit integer                                                                          | Yes                                | SMALLINT                           |
| INT, INTEGER         | 32-bit integer                                                                          | Yes                                | INT, INTEGER                       |
| BIGINT               | 64-bit integer                                                                          | Yes                                | BIGINT                             |
| NUMERIC              | Fixed-point number                                                                      | Yes                                | NUMERIC                            |
| DECIMAL              | Fixed-point number                                                                      | Yes                                | DECIMAL                            |
| MONEY                | 64-bit currency amount                                                                  | Yes                                | MONEY                              |
| SMALLMONEY           | 32-bit currency amount                                                                  | No                                 | MONEY                              |
| FLOAT                | Floating-point number                                                                   | Yes                                | FLOAT                              |
| REAL                 | Single-precision floating-point number                                                  | Yes                                | REAL                               |

**Temporal data types**

| SQL Server data type | SQL Server data type characteristic       | PostgreSQL identical compatibility | PostgreSQL corresponding data type |
| -------------------- | ----------------------------------------- | ---------------------------------- | ---------------------------------- |
| DATE                 | Date (year, month and day)                | Yes                                | DATE                               |
| TIME                 | Time (hour, minute, second and fraction)  | Yes                                | TIME                               |
| SMALLDATETIME        | Date and time                             | No                                 | TIMESTAMP(0)                       |
| DATETIME             | Date and time with fraction               | No                                 | TIMESTAMP(3)                       |
| DATETIME2            | Date and time with fraction               | No                                 | TIMESTAMP(p)                       |
| DATETIMEOFFSET       | Date and time with fraction and time zone | No                                 | TIMESTAMP(p) WITH TIME ZONE        |

**Binary data types**

| SQL Server data type | SQL Server data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type |
| -------------------- | ----------------------------------- | ---------------------------------- | ---------------------------------- |
| BINARY               | Fixed-length byte string            | No                                 | BYTEA                              |
| VARBINARY            | Variable length 1-8,000             | No                                 | BYTEA                              |

**LOB data types**

| SQL Server data type | SQL Server data type characteristic           | PostgreSQL identical compatibility | PostgreSQL corresponding data type |
| -------------------- | --------------------------------------------- | ---------------------------------- | ---------------------------------- |
| TEXT                 | Variable-length character data up to 2 GB     | Yes                                | TEXT                               |
| NTEXT                | Variable-length Unicode UCS-2 data up to 2 GB | No                                 | TEXT                               |
| IMAGE                | Variable-length character data up to 2 GB     | No                                 | BYTEA                              |
| VARCHAR(MAX)         | Variable-length character data up to 2 GB     | Yes                                | TEXT                               |
| NVARCHAR(MAX)        | Variable-length Unicode UCS-2 data up to 2 GB | No                                 | TEXT                               |
| VARBINARY(MAX)       | Variable-length character data up to 2 GB     | No                                 | BYTEA                              |

**Spatial data types**

| SQL Server data type | SQL Server data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type |
| -------------------- | ----------------------------------- | ---------------------------------- | ---------------------------------- |
| GEOMETRY             | Euclidean (flat) coordinate system  | Yes                                | GEOMETRY                           |
| GEOGRAPHY            | Round-earth coordinate system       | Yes                                | GEOGRAPHY                          |
| SQL_VARIANT          | Maximum length of 8016              | No                                 | No equivalent                      |

**Other data types**

| SQL Server data type | SQL Server data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type |
| -------------------- | ----------------------------------- | ---------------------------------- | ---------------------------------- |
| XML                  | XML data                            | Yes                                | XML                                |
| UNIQUEIDENTIFIER     | 16-byte GUID (UUID)                 | No                                 | CHAR(16)                           |
| HIERARCHYID          | Approximately 5 bytes               | No                                 | VARCHAR (n)                        |
| ROWVERSION           | 8 bytes                             | No                                 | TIMESTAMP(p)                       |

### PostgreSQL Character Column Semantics

PostgreSQL only supports `CHAR` for column size semantics. If you define a field as `VARCHAR (10)`, PostgreSQL can store 10 characters regardless of how many bytes it takes to store each non-English character. `VARCHAR(n)` stores strings up to n characters, not bytes, in length.

### Migration of SQL Server Data Types to PostgreSQL Data Types

You can use AWS Schema Conversion Tool (AWS SCT) for automatic migration and conversion of SQL Server tables and data types.

### Examples

To demonstrate AWS SCT capability for migrating SQL Server tables to their PostgreSQL equivalents, a table containing columns representing the majority of SQL Server data types was created and converted using AWS SCT.

Source SQL Server compatible DDL for creating the `DATATYPES` table

```
CREATE TABLE "DataTypes"(
  "BINARY_FLOAT" REAL,
  "BINARY_DOUBLE" FLOAT,
  "BLOB" VARBINARY(4000),
  "CHAR" CHAR(10),
  "CHARACTER" CHAR(10),
  "CLOB" VARCHAR(4000),
  "DATE" DATE,
  "DECIMAL" NUMERIC(3,2),
  "DOUBLE_PRECISION" FLOAT(52),
  "FLOAT" FLOAT(3),
  "INTEGER" INTEGER,
  "LONG" TEXT,
  "NCHAR" NCHAR(10),
  "NUMBER" NUMERIC(9,9),
  "NUMBER1" NUMERIC(9,0),
  "NUMERIC" NUMERIC(9,9),
  "RAW" BINARY(10),
  "REAL" FLOAT(52),
  "SMALLINT" SMALLINT,
  "TIMESTAMP" TIMESTAMP,
  "TIMESTAMP_WITH_TIME_ZONE" DATETIMEOFFSET(5),
  "VARCHAR" VARCHAR(10),
  "VARCHAR2" VARCHAR(10),
  "XMLTYPE" XML
);
```

Target PostgreSQL compatible DDL for creating the DATATYPES table migrated from SQL Server with AWS SCT.

```
CREATE TABLE IF NOT EXISTS datatypes(
  binary_float real DEFAULT NULL,
  binary_double double precision DEFAULT NULL,
  blob bytea DEFAULT NULL,
  char character(10) DEFAULT NULL,
  character character(10) DEFAULT NULL,
  clob text DEFAULT NULL,
  date TIMESTAMP(0) without time zone DEFAULT NULL,
  decimal numeric(3,2) DEFAULT NULL,
  dec numeric(3,2) DEFAULT NULL,
  double_precision double precision DEFAULT NULL,
  float double precision DEFAULT NULL,
  integer numeric(38,0) DEFAULT NULL,
  long text DEFAULT NULL,
  nchar character(10) DEFAULT NULL,
  number numeric(9,9) DEFAULT NULL,
  number1 numeric(9,0) DEFAULT NULL,
  numeric numeric(9,9) DEFAULT NULL,
  raw bytea DEFAULT NULL,
  real double precision DEFAULT NULL,
  smallint numeric(38,0) DEFAULT NULL,
  timestamp TIMESTAMP(5) without time zone DEFAULT NULL,
  timestamp_with_time_zone TIMESTAMP(5) with time zone DEFAULT NULL,
  varchar character varying(10) DEFAULT NULL,
  varchar2 character varying(10) DEFAULT NULL,
  xmltype xml DEFAULT NULL
)
WITH (
  OIDS=FALSE
);
```

## Summary

AWS SCT converts all incompatible data types.

SQL Server CREATE TABLE command:

```
CREATE TABLE scttest(
SMALLDATETIMEcol SMALLDATETIME,
datetimecol DATETIME,
datetime2col DATETIME2,
datetimeoffsetcol DATETIMEOFFSET,
binarycol BINARY,
varbinarycol VARBINARY,
ntextcol NTEXT,
imagecol IMAGE,
nvarcharmaxcol NVARCHAR(MAX),
varbinarymaxcol VARBINARY(MAX),
uniqueidentifiercol UNIQUEIDENTIFIER,
hierarchyiDcol HIERARCHYID,
sql_variantcol SQL_VARIANT,
rowversioncol ROWVERSION);
```

The equivalent command that was created by AWS SCT:

```
CREATE TABLE scttest(
smalldatetimecol TIMESTAMP WITHOUT TIME ZONE,
datetimecol TIMESTAMP WITHOUT TIME ZONE,
datetime2col TIMESTAMP(6) WITHOUT TIME ZONE,
datetimeoffsetcol TIMESTAMP(6) WITH TIME ZONE,
binarycol BYTEA,
varbinarycol BYTEA,
ntextcol TEXT,
imagecol BYTEA,
nvarcharmaxcol TEXT,
varbinarymaxcol BYTEA,
uniqueidentifiercol UUID,
hierarchyidcol VARCHAR(8000),
sql_variantcol VARCHAR(8000),
rowversioncol VARCHAR(8000) NOT NULL);
```

For more information, see [System Columns](https://www.postgresql.org/docs/13/ddl-system-columns.html "https://www.postgresql.org/docs/13/ddl-system-columns.html") and [Data Types](https://www.postgresql.org/docs/13/datatype.html "https://www.postgresql.org/docs/13/datatype.html") in the _PostgreSQL documentation_, and [Schema Conversion Tool Documentation](../../../SchemaConversionTool/index.md "../../../SchemaConversionTool/index.md").
