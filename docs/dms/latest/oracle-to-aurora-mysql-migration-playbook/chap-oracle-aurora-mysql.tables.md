# Data types

With AWS DMS, you can migrate data between different database platforms, allowing you to consolidate databases, perform database modernization, or migrate databases to the cloud. Data types define the kind of data that can be stored in a database column or variable. The following sections will provide detailed information about different data types supported by Oracle and MySQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                   | Key differences                                              |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Four star feature compatibility | Four star automation level         | [Data Types](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.datatypes "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.datatypes") | Aurora MySQL doesn’t support `BFILE`, `ROWID`, and `UROWID`. |

## Oracle usage

Oracle provides a set of primitive data types for defining table columns and PL/SQL code variables. The assigned data types for table columns or PL/SQL code (such as stored procedures and triggers) define the valid values each column or argument can store.

## Oracle data types and MySQL data types

**Character data types**

| Oracle data type   | Oracle data type characteristic                         | MySQL identical compatibility | MySQL corresponding data type |
| ------------------ | ------------------------------------------------------- | ----------------------------- | ----------------------------- |
| `CHAR(n)`          | Maximum size of 2000 bytes                              | Yes                           | `CHAR(n)`                     |
| `CHARACTER(n)`     | Maximum size of 2000 bytes                              | Yes                           | `CHARACTER(n)`                |
| `NCHAR(n)`         | Maximum size of 2000 bytes                              | Yes                           | `NCHAR(n)`                    |
| `VARCHAR(n)`       | Maximum size of 2000 bytes                              | Yes                           | `VARCHAR(n)`                  |
| `NCHAR VARYING(n)` | Varying-length UTF-8 string, maximum size of 4000 bytes | Yes                           | `NCHAR VARYING(n)`            |
| `VARCHAR2(n)` 11g  | Maximum size of 4000 bytes or 32 KB in PL/SQL           | No                            | `VARCHAR(n)`                  |
| `VARCHAR2(n)` 12g  | Maximum size of 32767 bytes `MAX_STRING_SIZE= EXTENDED` | No                            | `VARCHAR(n)`                  |
| `NVARCHAR2(n)`     | Maximum size of 4000 bytes                              | No                            | `VARCHAR(n)`                  |
| `LONG`             | Maximum size of 2 GB                                    | Yes                           | `LONG`                        |
| `RAW(n)`           | Maximum size of 2000 bytes                              | No                            | `VARBINARY(n)`                |
| `LONG RAW`         | Maximum size of 2 GB                                    | No                            | `LONGTEXT`                    |

**Numeric data types**

| Oracle data type   | Oracle data type characteristic                                   | MySQL identical compatibility | MySQL corresponding data type |
| ------------------ | ----------------------------------------------------------------- | ----------------------------- | ----------------------------- |
| `NUMBER`           | Floating-point number                                             | No                            | `DECIMAL(p,s)`                |
| `NUMBER(*)`        | Floating-point number                                             | No                            | `DOUBLE`                      |
| `NUMBER(p,s)`      | Precision can range from 1 to 38, scale can range from -84 to 127 | No                            | `DECIMAL(p,s)`                |
| `NUMERIC(p,s)`     | Precision can range from 1 to 38                                  | Yes                           | `NUMERIC(p,s)`                |
| `FLOAT(p)`         | Floating-point number                                             | Yes                           | `FLOAT(p)`                    |
| `DEC(p,s)`         | Fixed-point number                                                | Yes                           | `DEC(p,s)`                    |
| `DECIMAL(p,s)`     | Fixed-point number                                                | Yes                           | `DECIMAL(p,s)`                |
| `INT`              | 38 digits integer                                                 | Yes                           | `INT`                         |
| `INTEGER`          | 38 digits integer                                                 | Yes                           | `INTEGER`                     |
| `SMALLINT`         | 38 digits integer                                                 | Yes                           | `SMALLINT`                    |
| `REAL`             | Floating-point number                                             | Yes                           | `REAL`                        |
| `DOUBLE PRECISION` | Floating-point number                                             | Yes                           | `DOUBLE PRECISION`            |

**Date and time data types**

| Oracle data type               | Oracle data type characteristic                                       | MySQL identical compatibility | MySQL corresponding data type |
| ------------------------------ | --------------------------------------------------------------------- | ----------------------------- | ----------------------------- |
| `DATE`                         | Stores date and time data (year, month, day, hour, minute and second) | Yes                           | `DATETIME`                    |
| `TIMESTAMP(p)`                 | Date and time with fraction                                           | Yes                           | `TIMESTAMP(6)`                |
| `TIMESTAMP(p) WITH TIME ZONE`  | Date and time with fraction and time zone                             | No                            | `DATETIME(n)`                 |
| `INTERVAL YEAR(p) TO MONTH`    | Date interval                                                         | No                            | `VARCHAR(n)`                  |
| `INTERVAL DAY(p) TO SECOND(s)` | Day and time interval                                                 | No                            | `VARCHAR(n)`                  |

**LOB data types**

| Oracle data type | Oracle data type characteristic                           | MySQL identical compatibility | MySQL corresponding data type |
| ---------------- | --------------------------------------------------------- | ----------------------------- | ----------------------------- |
| `BFILE`          | Pointer to binary file, maximum file size of 4 GB         | No                            | `VARCHAR (255)`               |
| `BLOB`           | Binary large object, maximum file size of 4 GB            | Yes                           | `BLOB`                        |
| `CLOB`           | Character large object, maximum file size of 4 GB         | No                            | `LONGTEXT`                    |
| `NCLOB`          | Variable-length Unicode string, maximum file size of 4 GB | No                            | `LONGTEXT`                    |

**ROWID data types**

| Oracle data type | Oracle data type characteristic         | MySQL identical compatibility | MySQL corresponding data type |
| ---------------- | --------------------------------------- | ----------------------------- | ----------------------------- |
| `ROWID`          | Physical row address                    | No                            | `CHAR(n)`                     |
| `UROWID(n)`      | Universal row id, logical row addresses | No                            | `VARCHAR(n)`                  |

**XML data type**

| Oracle data type | Oracle data type characteristic | MySQL identical compatibility | MySQL corresponding data type |
| ---------------- | ------------------------------- | ----------------------------- | ----------------------------- |
| `XMLTYPE`        | XML data                        | No                            | `LONGTEXT`                    |

**Logical data type**

| Oracle data type | Oracle data type characteristic                                                  | MySQL identical compatibility | MySQL corresponding data type |
| ---------------- | -------------------------------------------------------------------------------- | ----------------------------- | ----------------------------- |
| `BOOLEAN`        | Values `TRUE`, `FALSE`, and `NULL`, can’t be assigned to a database table column | Yes                           | `BOOLEAN`                     |

**Spatial types**

| Oracle data type    | Oracle data type characteristic                         | MySQL identical compatibility | MySQL corresponding data type |
| ------------------- | ------------------------------------------------------- | ----------------------------- | ----------------------------- |
| `SDO_GEOMETRY`      | The geometric description of a spatial object           | No                            | N/A                           |
| `SDO_TOPO_GEOMETRY` | Describes a topology geometry                           | No                            | N/A                           |
| `SDO_GEORASTER`     | A raster grid or image object is stored in a single row | No                            | N/A                           |

**Media types**

| Oracle data type | Oracle data type characteristic                                                                | MySQL identical compatibility | MySQL corresponding data type |
| ---------------- | ---------------------------------------------------------------------------------------------- | ----------------------------- | ----------------------------- |
| `ORDDicom`       | Supports the storage and management of audio data                                              | No                            | N/A                           |
| `ORDDicom`       | Supports the storage and management of Digital Imaging and Communications in Medicine (DICOM). | No                            | N/A                           |
| `ORDDoc`         | Supports storage and management of any type of media data                                      | No                            | N/A                           |
| `ORDImage`       | Supports the storage and management of image data                                              | No                            | N/A                           |
| `ORDVideo`       | Supports the storage and management of video data                                              | No                            | N/A                           |

### Oracle character column semantics

Oracle supports `BYTE` and `CHAR` semantics for column size, which determines the amount of storage allocated for `CHAR` and `VARCHAR` columns.

- If you define a field as `VARCHAR2(10 BYTE)`, Oracle can use up to 10 bytes for storage. However, based on your database codepage and NLS settings, you may not be able to store 10 characters in that field because the physical size of some non-English characters exceeds one byte.
- If you define a field as `VARCHAR2(10 CHAR)`, Oracle can store 10 characters no matter how many bytes are required to store each non-English character.

```
CREATE TABLE table1 (col1 VARCHAR2(10 CHAR), col2 VARCHAR2(10 BYTE));
```

By default, Oracle uses `BYTE` semantics. When using a multi-byte character set such as UTF8, use one of the following options.

- Use the `CHAR` modifier in the `VARCHAR2` or `CHAR` column definition.
- Modify the session or system parameter `NLS_LENGTH_SEMANTICS` to change the default from `BYTE` to `CHAR`.

```
ALTER system SET nls_length_semantics=char scope=both;
ALTER system SET nls_length_semantics=byte scope=both;

ALTER session SET nls_length_semantics=char;
ALTER session SET nls_length_semantics=byte;
```

For more information, see [Data Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html#GUID-A3C0D836-BADB-44E5-A5D4-265BA5968483 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html#GUID-A3C0D836-BADB-44E5-A5D4-265BA5968483") in the _Oracle documentation_.

## MySQL usage

MySQL provides multiple data types equivalent to certain Oracle data types. The following table provides the full list of MySQL data types.

**Character data types**

| MySQL data type | MySQL data type characteristic                                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CHAR(n)`       | Stores exactly (n) characters.                                                                                                                       |
| `VARCHAR(n)`    | Stores a variable number of characters, up to a maximum of n characters.                                                                             |
| `BINARY`        | Stores exactly (n) bytes.                                                                                                                            |
| `VARBINARY`     | Stores a variable number of characters, up to a maximum of n bytes.                                                                                  |
| `BLOLB`         | Binary large object that can hold a variable amount of data.                                                                                         |
| `TEXT`          | Specific variant of varchar, which does not require you to specify an upper limit on the number of characters.                                       |
| `ENUM`          | String object with a value chosen from a list of permitted values that are enumerated explicitly in the column specification at table creation time. |
| `SET`           | String object that can have zero or more values, each of which must be chosen from a list of permitted values specified when the table is created.   |

**Numeric data types**

| MySQL data type | MySQL data type characteristic                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| `INTEGER`       | Max value is 2147483647.                                                                             |
| `INT`           | Max value is 2147483647.                                                                             |
| `SMALLINT`      | Max value is 32767.                                                                                  |
| `TINYINT`       | Max value is 127.                                                                                    |
| `MEDIUMINT`     | Max value is 8388607.                                                                                |
| `BIGINT`        | Max value is 2^63-1.                                                                                 |
| `DECIMAL (p,s)` | Stores any value with p digits and s decimals.                                                       |
| `NUMERIC(p,s)`  | Stores any value with p digits and s decimals.                                                       |
| `FLOAT (m,d)`   | Values can be stored with up to M digits in total, of which D digits may be after the decimal point. |
| `DOUBLE (m,d)`  | Values can be stored with up to M digits in total, of which D digits may be after the decimal point. |
| `BIT (m)`       | Stores M-bit values. M can range from 1 to 64.                                                       |

**Date and time data types**

| MySQL data type | MySQL data type characteristic                                                                                                                                                                                                                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DATE`          | Values with a date part but no time part. MySQL retrieves and displays `DATE` values in the `YYYY-MM-DD` format. The supported range is `1000-01-01` to `9999-12-31`.                                                                                                                                                |
| `DATETIME`      | Values that contain both date and time parts. MySQL retrieves and displays `DATETIME` values in `YYYY-MM-DD HH:MM:SS` format. The supported range is `1000-01-01 00:00:00` to `9999-12-31 23:59:59`.                                                                                                                 |
| `TIMESTAMP`     | Values that contain both date and time parts. `TIMESTAMP` has a range of `1970-01-01 00:00:01` UTC to `2038-01-19 03:14:07` UTC.                                                                                                                                                                                     |
| `TIME`          | Values may range from `-838:59:59` to `838:59:59`. The hours part may be so large because the `TIME` type can be used not only to represent a time of day, which must be less than 24 hours, but also elapsed time or a time interval between two events, which may be much greater than 24 hours, or even negative. |
| `YEAR`          | `YEAR` 1-byte type used to represent year values. It can be declared as `YEAR` or `YEAR(n)` and has a display width of n characters.                                                                                                                                                                                 |

**Logical data type**

| MySQL data type | MySQL data type characteristic                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `BOOLEAN`       | Holds a truth value. Will accept values such as TRUE, 't','true', 'y', 'yes', and '1' as true. Uses 1 byte of storage, and can store NULL. |

**Geometric data types**

| MySQL data type      | MySQL data type characteristic                                         |
| -------------------- | ---------------------------------------------------------------------- |
| `GEOMETRY`           | The column type to specify when you want to use the data models below. |
| `POINT`              | An (x,y) value.                                                        |
| `LINESTRING`         | A line (pt1, pt2).                                                     |
| `POLYGON`            | A sequence of points, effectively a closed path.                       |
| `MULTIPOINT`         | Collection of `POINT`s.                                                |
| `MULTILINESTRING`    | Collection of `LINE`s.                                                 |
| `MULTIPOLYGON`       | Collection of `POLYGON`s.                                              |
| `GEOMETRYCOLLECTION` | Collection of geometry data types.                                     |

**Other data types**

| MySQL data type | MySQL data type characteristic |
| --------------- | ------------------------------ |
| `JSON`          | Textual JSON data              |

## Migration of Oracle data types to MySQL data types

You can perform automatic migration and conversion of Oracle tables and data types using AWS Schema Conversion Tool (AWS SCT).

**Examples**

To demonstrate AWS SCT capability for migrating Oracle tables to their MySQL equivalents, a table containing columns representing the majority of Oracle data types was created and converted using AWS SCT.

Source Oracle compatible DDL for creating the `DATATYPES` table.

```
CREATE TABLE "DATATYPES"(
  "BFILE"                    BFILE,
  "BINARY_FLOAT"             BINARY_FLOAT,
  "BINARY_DOUBLE"            BINARY_DOUBLE,
  "BLOB"                     BLOB,
  "CHAR"                     CHAR(10 BYTE),
  "CHARACTER"                CHAR(10 BYTE),
  "CLOB"                     CLOB,
  "NCLOB"                    NCLOB,
  "DATE"                     DATE,
  "DECIMAL"                  NUMBER(3,2),
  "DEC"                      NUMBER(3,2),
  "DOUBLE_PRECISION"         FLOAT(126),
  "FLOAT"                    FLOAT(3),
  "INTEGER"                  NUMBER(*,0),
  "INT"                      NUMBER(*,0),
  "INTERVAL_YEAR"            INTERVAL YEAR(4) TO MONTH,
  "INTERVAL_DAY"             INTERVAL DAY(4) TO SECOND(4),
  "LONG"                     LONG,
  "NCHAR"                    NCHAR(10),
  "NCHAR_VARYING"            NVARCHAR2(10),
  "NUMBER"                   NUMBER(9,9),
  "NUMBER1"                  NUMBER(9,0),
  "NUMBER(*)"                NUMBER,
  "NUMERIC"                  NUMBER(9,9),
  "NVARCHAR2"                NVARCHAR2(10),
  "RAW"                      RAW(10),
  "REAL"                     FLOAT(63),
  "ROW_ID"                   ROWID,
  "SMALLINT"                 NUMBER(*,0),
  "TIMESTAMP"                TIMESTAMP(5),
  "TIMESTAMP_WITH_TIME_ZONE" TIMESTAMP(5) WITH TIME ZONE,
  "UROWID"                   UROWID(10),
  "VARCHAR"                  VARCHAR2(10 BYTE),
  "VARCHAR2"                 VARCHAR2(10 BYTE),
  "XMLTYPE"                  XMLTYPE
);
```

Target MySQL compatible DDL for creating the `DATATYPES` table migrated from Oracle with AWS SCT.

```
CREATE TABLE IF NOT EXISTS datatypes(
bfile VARCHAR(1000) DEFAULT NULL,
BINARY_FLOAT FLOAT(12) DEFAULT NULL,
BINARY_DOUBLE DOUBLE DEFAULT NULL,
`BLOB` LONGBLOB DEFAULT NULL,
`CHAR` CHAR(10) DEFAULT NULL,
`CHARACTER` CHAR(10) DEFAULT NULL,
CLOB LONGTEXT DEFAULT NULL,
NCLOB LONGTEXT DEFAULT NULL,
`DATE` DATETIME DEFAULT NULL,
`DECIMAL` DECIMAL(3,2) DEFAULT NULL,
`DEC` DECIMAL(3,2) DEFAULT NULL,
DOUBLE_PRECISION DOUBLE DEFAULT NULL,
`FLOAT` DOUBLE DEFAULT NULL,
`INTEGER` DECIMAL(38,0) DEFAULT NULL,
`INT` DECIMAL(38,0) DEFAULT NULL,
INTERVAL_YEAR VARCHAR(30) DEFAULT NULL,
INTERVAL_DAY VARCHAR(30) DEFAULT NULL,
`LONG` LONGTEXT DEFAULT NULL,
NCHAR CHAR(10) DEFAULT NULL,
NCHAR_VARYING VARCHAR(10) DEFAULT NULL,
NUMBER DECIMAL(9,9) DEFAULT NULL,
NUMBER1 DECIMAL(9,0) DEFAULT NULL,
`NUMBER(*)` DOUBLE DEFAULT NULL,
`NUMERIC` DECIMAL(9,9) DEFAULT NULL,
NVARCHAR2 VARCHAR(10) DEFAULT NULL,
RAW VARBINARY(10) DEFAULT NULL,
`REAL` DOUBLE DEFAULT NULL,
ROW_ID CHAR(10) DEFAULT NULL,
`SMALLINT` DECIMAL(38,0) DEFAULT NULL,
`TIMESTAMP` DATETIME(5) DEFAULT NULL,
TIMESTAMP_WITH_TIME_ZONE DATETIME(5) DEFAULT NULL,
UROWID VARCHAR(10) DEFAULT NULL,
`VARCHAR` VARCHAR(10) DEFAULT NULL,
VARCHAR2 VARCHAR(10) DEFAULT NULL,
XMLTYPE LONGTEXT DEFAULT NULL);
```

AWS SCT converted most of the data types. However, a few exceptions were raised for data types that AWS SCT is unable to automatically convert and where AWS SCT recommended manual actions.

**MySQL doesn’t have a data type BFILE**

`BFILE`s are pointers to binary files.

_Recommended actions_: Either store a named file with the data and create a routine that gets that file from the file system, or store the data blob inside your database.

**MySQL doesn’t have a data type ROWID**

`ROWID`s are physical row addresses inside Oracle storage subsystems. The `ROWID` data type is primarily used for values returned by the `ROWID` pseudocolumn.

_Recommended actions_: Although MySQL contains a `ctid` column that is the physical location of the row version within its table, it doesn’t have a comparable data type. However, you can use `CHAR` as a partial data type equivalent. If you use `ROWID` data types in your code, modifications may be necessary.

**MySQL doesn’t have a data type UROWID**

Universal row identifier, or `UROWID`, is a single Oracle data type that supports both logical and physical row identifiers of foreign table row identifiers such as non-Oracle tables accessed through a gateway.

_Recommended actions_: MySQL doesn’t have a comparable data type. You can use `VARCHAR(n)` as a partial data type equivalent. However, if you are using `UROWID` data types in your code, modifications may be necessary.

For more information, see [Schema Conversion Tool Documentation](../../../SchemaConversionTool/index.md "../../../SchemaConversionTool/index.md") and [Data Types](https://dev.mysql.com/doc/refman/5.7/en/data-types.html "https://dev.mysql.com/doc/refman/5.7/en/data-types.html") in the _MySQL documentation_.
