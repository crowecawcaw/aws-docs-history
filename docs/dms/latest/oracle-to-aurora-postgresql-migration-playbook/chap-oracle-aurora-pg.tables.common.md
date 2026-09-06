

# Common Oracle and PostgreSQL data types
<a name="chap-oracle-aurora-pg.tables.common"></a>

With AWS DMS, you can seamlessly migrate data between different database platforms, including Oracle and PostgreSQL, while ensuring data type compatibility. Common Oracle and PostgreSQL data types refer to the fundamental data structures used to store and represent various types of information within these database systems.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  |  [Data Types](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.datatypes)  | PostgreSQL doesn’t support `BFILE`, `ROWID`, `UROWID`. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.tables.common.ora"></a>

Oracle provides a set of primitive data types for defining table columns and PL/SQL code variables. The assigned data types for table columns or PL/SQL code (such as stored procedures and triggers) define the valid values each column or argument can store.

## Oracle data types and PostgreSQL data types
<a name="chap-oracle-aurora-pg.tables.common.orapg"></a>

 **Character data types** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| CHAR(n) | Maximum size of 2000 bytes | Yes | CHAR(n) | 
| CHARACTER(n) | Maximum size of 2000 bytes | Yes | CHARACTER(n) | 
| NCHAR(n) | Maximum size of 2000 bytes | No | CHAR(n) | 
| VARCHAR(n) | Maximum size of 2000 bytes | Yes | VARCHAR(n) | 
| NCHAR VARYING (n) | Varying-length UTF-8 string, maximum size of 4000 bytes | No | CHARACTER VARYING(n) | 
| VARCHAR2(n) 11g | Maximum size of 4000 bytes. Maximum size of 32KB in PL/SQL. | No | VARCHAR(n) | 
| VARCHAR2(n) 12g | Maximum size of 32767 bytes. MAX\_STRING\_SIZE=EXTENDED | No | VARCHAR(n) | 
| NVARCHAR2(n) | Maximum size of 4000 bytes | No | VARCHAR(n) | 
| LONG | Maximum size of 2GB | No | TEXT | 
| RAW(n) | Maximum size of 2000 bytes | No | BYTEA | 
| LONG RAW | Maximum size of 2GB | No | BYTEA | 

 **Numeric data types** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| NUMBER | Floating-point number | No | DOUBLE PRECISION | 
| NUMBER(\*) | Floating-point number | No | DOUBLE PRECISION | 
| NUMBER(p,s) | Precision can range from 1 to 38, scale can range from -84 to 127 | No | DECIMAL(p,s) | 
| NUMERIC(p,s) | Precision can range from 1 to 38 | Yes | NUMERIC(p,s) | 
| FLOAT(p) | Floating-point number | No | DOUBLE PRECISION | 
| DEC(p,s) | Fixed-point number | Yes | DEC(p,s) | 
| DECIMAL(p,s) | Fixed-point number | Yes | DECIMAL(p,s) | 
| INT | 38 digits integer | Yes | INTEGER or NUMERIC(38,0) | 
| INTEGER | 38 digits integer | Yes | INTEGER or NUMERIC(38,0) | 
| SMALLINT | 38 digits integer | Yes | SMALLINT | 
| REAL | Floating-point number | No | DOUBLE PRECISION | 
| DOUBLE PRECISION | Floating-point number | Yes | DOUBLE PRECISION | 

 **Date and time data types** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| DATE | DATE data type stores date and time data (year, month, day, hour, minute and second) | Yes | TIMESTAMP(0) | 
| TIMESTAMP(p) | Date and time with fraction | Yes | TIMESTAMP(p) | 
| TIMESTAMP(p) WITH TIME ZONE | Date and time with fraction and time zone | Yes | TIMESTAMP(p) WITH TIME ZONE | 
| INTERVAL YEAR(p) TO MONTH | Date interval | Yes | INTERVAL YEAR TO MONTH | 
| INTERVAL DAY(p) TO SECOND(s) | Day and time interval | Yes | INTERVAL DAY TO SECOND(s) | 

 **LOB data types** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| BFILE | Pointer to binary file, maximum file size of 4 GB | No | VARCHAR (255) or CHARACTER VARYING (255) | 
| BLOB | Binary large object, maximum file size of 4 GB | No | BYTEA | 
| CLOB | Character large object, maximum file size of 4 GB | No | TEXT | 
| NCLOB | Variable-length Unicode string, maximum file size of 4 GB | No | TEXT | 

 **ROWID data types** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| ROWID | Physical row address | No | CHARACTER (255) | 
| UROWID(n) | Universal row id, logical row addresses | No | CHARACTER VARYING | 

 **XML data type** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| XMLTYPE | XML data | No | XML | 

 **Logical data type** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| BOOLEAN | Values `TRUE`, `FALSE`, and `NULL`, can’t be assigned to a database table column | Yes | BOOLEAN | 

 **Spatial types** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| SDO\_GEOMETRY | The geometric description of a spatial object | No | N/A | 
| SDO\_TOPO\_GEOMETRY | Describes a topology geometry | No | N/A | 
| SDO\_GEORASTER | A raster grid or image object is stored in a single row | No | N/A | 

 **Media types** 


| Oracle data type | Oracle data type characteristic | PostgreSQL identical compatibility | PostgreSQL corresponding data type | 
| --- | --- | --- | --- | 
| ORDDicom | Supports the storage and management of audio data | No | N/A | 
| ORDDicom | Supports the storage and management of Digital Imaging and Communications in Medicine (DICOM). | No | N/A | 
| ORDDoc | Supports storage and management of any type of media data | No | N/A | 
| ORDImage | Supports the storage and management of image data | No | N/A | 
| ORDVideo | Supports the storage and management of video data | No | N/A | 

**Note**  
The “PostgreSQL identical compatibility” column indicates if you can use the exact Oracle data type syntax when migrating to Amazon Aurora PostgreSQL.

### Oracle character column semantics
<a name="chap-oracle-aurora-pg.tables.common.ora.semantics"></a>

Oracle supports both `BYTE` and `CHAR` semantics for column size, which determines the amount of storage allocated for `CHAR` and `VARCHAR` columns.
+ If you define a field as `VARCHAR2(10 BYTE)`, Oracle can use up to 10 bytes for storage. However, based on your database codepage and NLS settings, you may not be able to store 10 characters in that field because the physical size of some non-English characters exceeds one byte.
+ If you define a field as `VARCHAR2(10 CHAR)`, Oracle can store 10 characters no matter how many bytes are required to store each non-English character.

```
CREATE TABLE table1 (col1 VARCHAR2(10 CHAR), col2 VARCHAR2(10 BYTE));
```

By default, Oracle uses `BYTE` semantics. When using a multi-byte character set such as UTF8, use one of the following options.
+ Use the `CHAR` modifier in the `VARCHAR2` or `CHAR` column definition.
+ Modify the session or system parameter `NLS_LENGTH_SEMANTICS` to change the default from `BYTE` to `CHAR`.

```
ALTER system SET nls_length_semantics=char scope=both;
ALTER system SET nls_length_semantics=byte scope=both;

ALTER session SET nls_length_semantics=char;
ALTER session SET nls_length_semantics=byte;
```

For more information, see [Data Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html#GUID-A3C0D836-BADB-44E5-A5D4-265BA5968483) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.tables.common.pg"></a>

PostgreSQL provides multiple data types equivalent to certain Oracle data types. The following table provides the full list of PostgreSQL data types.

 **Character data types** 


| PostgreSQL data type | PostgreSQL data type characteristic | 
| --- | --- | 
| CHAR | Stores a single character | 
| CHARACTER | Stores a single character | 
| CHAR(n) | Stores exactly (n) characters | 
| VARCHAR(N) | Stores a variable number of characters, up to a maximum of n characters | 
| TEXT | Specific variant of varchar, which doesn’t require you to specify an upper limit on the number of characters | 

 **Numeric data types** 


| PostgreSQL data type | PostgreSQL data type characteristic | 
| --- | --- | 
| NUMERIC (P,S) | Exact numeric of selectable precision | 
| REAL | Single precision floating-point number (4 bytes) | 
| DOUBLE PRECISION | Double precision floating-point number (8 bytes) | 
| INT | A signed 4-byte integer that can store from -2147483648 to \+2147483647 | 
| INTEGER | A signed 4-byte integer that can store from -2147483648 to \+2147483647 | 
| SMALLINT | A signed 2-byte integer that can store from -32768 to \+32767 | 
| BIGINT | A signed 8-byte integer, giving approximately 18 digits of precision | 
| BIT | Stores a single bit, 0 or 1 | 
| BIT VARYING | Stores a string of bits | 
| MONEY | Equivalent to NUMERIC (9,2), storing 4 bytes of data. Its use is discouraged. | 

 **Date and time data types** 


| PostgreSQL data type | PostgreSQL data type characteristic | 
| --- | --- | 
| TIMESTAMP | Stores dates and times from 4713 BC to 1465001 AD, with a resolution of 1 microsecond - 8 bytes | 
| INTERVAL | Stores an interval of approximately 178,000,000 years, with a resolution of 1 microsecond - 16 bytes | 
| DATE | Stores dates from 4713 BC to 32767 AD, with a resolution of 1 day - 4 bytes | 
| TIME | Stores a time of day, from 0 to 23:59:59.99, with a resolution of 1 microsecond - 8 bytes with no timezone, 12 bytes with timezone | 

 **Logical data type** 


| PostgreSQL data type | PostgreSQL data type characteristic | 
| --- | --- | 
| BOOLEAN | Holds a truth value. Will accept values such as TRUE, 't','true', 'y', 'yes', and '1' as true. Uses 1 byte of storage, and can store NULL. You can use this type upon table creation. | 

 **XML data type** 


| PostgreSQL data type | PostgreSQL data type characteristic | 
| --- | --- | 
| XML | XML data | 

 **Geometric data types** 


| PostgreSQL data type | PostgreSQL data type characteristic | 
| --- | --- | 
| POINT | The column type to specify when you want to use the following data models | 
| LINE | An (x,y) value | 
| LSEG | A line (pt1, pt2) | 
| BOX | A sequence of points, effectively a closed path | 
| PATH | Collection of POINTs | 
| POLYGON | Collection of LINEs | 
| CIRCLE | Collection of POLYGONs | 

 **PotgreSQL data types** 


| PostgreSQL data type | PostgreSQL data type characteristic | 
| --- | --- | 
| JSON | Textual JSON data | 
| JSONB | Binary JSON data, decomposed | 
| SERIAL | A numeric column in a table that increases each time a row is added | 
| OID | An object identifier. Internally, PostgreSQL adds, by default, a hidden oid to each row, and stores a 4-byte integer. | 
| CIDR | Stores a network address of the form x.x.x.x/y where y is the netmask | 
| INET | Similar to cidr, except the host part can be 0 | 
| MACADDR | MAC (Media Access Control) address | 
| MACADDR8 | MAC (Media Access Control) address in EUI-64 format (PostgreSQL 10) | 
| PG\_LSN | PostgreSQL Log Sequence Number | 
| BYTEA | Binary data ("byte array") | 
| TSQUERY | Text search query | 
| TSVECTOR | Text search document | 
| TXID\_SNAPSHOT | User-level transaction ID snapshot | 
| UUID | Universally unique identifier | 

### PostgreSQL character column semantics
<a name="chap-oracle-aurora-pg.tables.common.pg.semantics"></a>

PostgreSQL only supports `CHAR` for column size semantics. If you define a field as `VARCHAR (10)`, PostgreSQL can store 10 characters regardless of how many bytes it takes to store each non-English character. `VARCHAR(n)` stores strings up to n characters (not bytes) in length.

## Migration of Oracle data types to PostgreSQL data types
<a name="chap-oracle-aurora-pg.tables.common.migration"></a>

You can perform automatic migration and conversion of Oracle tables and data types using AWS Schema Conversion Tool (AWS SCT).

 **Examples** 

To demonstrate AWS SCT capability for migrating Oracle tables to their PostgreSQL equivalents, a table containing columns representing the majority of Oracle data types was created and converted using AWS SCT.

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

Target PostgreSQL compatible DDL for creating the `DATATYPES` table migrated from Oracle with AWS SCT.

```
CREATE TABLE IF NOT EXISTS datatypes(
bfile                    character varying(255) DEFAULT NULL,
binary_float             real DEFAULT NULL,
binary_double            double precision DEFAULT NULL,
blob                     bytea DEFAULT NULL,
char                     character(10) DEFAULT NULL,
character                character(10) DEFAULT NULL,
clob                     text DEFAULT NULL,
nclob                    text DEFAULT NULL,
date                     TIMESTAMP(0) without time zone DEFAULT NULL,
decimal                  numeric(3,2) DEFAULT NULL,
dec                      numeric(3,2) DEFAULT NULL,
double_precision         double precision DEFAULT NULL,
float                    double precision DEFAULT NULL,
integer                  numeric(38,0) DEFAULT NULL,
int                      numeric(38,0) DEFAULT NULL,
interval_year            interval year to month(6) DEFAULT NULL,
interval_day             interval day to second(4) DEFAULT NULL,
long                     text DEFAULT NULL,
nchar                    character(10) DEFAULT NULL,
nchar_varying            character varying(10) DEFAULT NULL,
number                   numeric(9,9) DEFAULT NULL,
number1                  numeric(9,0) DEFAULT NULL,
"number(*)"              double precision DEFAULT NULL,
numeric                  numeric(9,9) DEFAULT NULL,
nvarchar2                character varying(10) DEFAULT NULL,
raw                      bytea DEFAULT NULL,
real                     double precision DEFAULT NULL,
row_id                   character(255) DEFAULT NULL,
smallint                 numeric(38,0) DEFAULT NULL,
timestamp                TIMESTAMP(5) without time zone DEFAULT NULL,
timestamp_with_time_zone TIMESTAMP(5) with time zone DEFAULT NULL,
urowid                   character varying DEFAULT NULL,
varchar                  character varying(10) DEFAULT NULL,
varchar2                 character varying(10) DEFAULT NULL,
xmltype                  xml DEFAULT NULL
)
WITH (
OIDS=FALSE
);
```

 AWS SCT converted most of the datatypes. However, a few exceptions were raised for datatypes that AWS SCT is unable to automatically convert and where AWS SCT recommended manual actions.

 **PostgreSQL doesn’t have a data type BFILE** 

 `BFILE`s are pointers to binary files.

 *Recommended actions*: Either store a named file with the data and create a routine that gets that file from the file system, or store the data blob inside your database.

 **PostgreSQL doesn’t have a data type ROWID** 

 `ROWID`s are physical row addresses inside Oracle storage subsystems. The `ROWID` datatype is primarily used for values returned by the `ROWID` pseudocolumn.

 *Recommended actions*: While PostgreSQL contains a `ctid` column that is the physical location of the row version within its table, it doesn’t have a comparable data type. However, you can use `CHAR` as a partial datatype equivalent.

**Example**  
If you use ROWID datatypes in your code, modifications may be necessary.

 **PostgreSQL doesn’t have a data type UROWID** 

Universal rowid, or `UROWID`, is a single Oracle datatype that supports both logical and physical rowids of foreign table rowids such as non-Oracle tables accessed through a gateway.

 *Recommended actions*: PostgreSQL doesn’t have a comparable data type. You can use `VARCHAR(n)` as a partial datatype equivalent. However, if you are using `UROWID` datatypes in your code, modifications may be necessary.

For more information, see [System Columns](https://www.postgresql.org/docs/13/ddl-system-columns.html) and [Data Types](https://www.postgresql.org/docs/13/datatype.html) in the *PostgreSQL documentation*, and [What is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) in the *user guide*.