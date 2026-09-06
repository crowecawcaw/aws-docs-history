

# Collations for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.collations"></a>

This topic provides reference information about collations and character sets in Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL, highlighting their differences and similarities. You can gain insight into how these database systems handle string management, sorting rules, and character encoding. The topic explores the various levels at which collations can be defined in SQL Server, from server-level to expression-level, and contrasts this with PostgreSQL’s approach.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  |  [Collations](chap-sql-server-aurora-pg.tools.actioncode.md#chap-sql-server-aurora-pg.tools.actioncode.collations)  |  `UTF16`, `NCHAR`, and `NVARCHAR` data types aren’t supported. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.collations.sqlserver"></a>

SQL Server collations define the rules for string management and storage in terms of sorting, case sensitivity, accent sensitivity, and code page mapping. SQL Server supports both ASCII and UCS-2 UNICODE data.

UCS-2 UNICODE data uses a dedicated set of UNICODE data types denoted by the prefix N: Nchar and Nvarchar. Their ASCII counterparts are `CHAR` and `VARCHAR`.

Choosing a collation and a character set has significant implications on data storage, logical predicate evaluations, query results, and query performance.

To view all collations supported by SQL Server, use the `fn_helpcollations` function:

```
SELECT * FROM sys.fn_helpcollations()
```

Collations define the actual bitwise binary representation of all string characters and the associated sorting rules. SQL Server supports multiple collations down to the column level. A table may have multiple string columns that use different collations. Collations for non-UNICODE character sets determine the code page number representing the string characters.

UNICODE and non-UNICODE data types in SQL Server aren’t compatible. A predicate or data modification that introduces a type conflict is resolved using predefined collation precedence rules. For more information, see [Collation Precedence](https://docs.microsoft.com/en-us/sql/t-sql/statements/collation-precedence-transact-sql?view=sql-server-ver15).

Collations define sorting and matching sensitivity for the following string characteristics:
+ Case
+ Accent
+ Kana
+ Width
+ Variation selector

SQL Server uses a suffix naming convention that appends the option name to the collation name. For example, the collation Azeri\_Cyrillic\_100\_CS\_AS\_KS\_WS\_SC, is an Azeri-Cyrillic-100 collation that is case-sensitive, accent-sensitive, kana type-sensitive, width-sensitive, and has supplementary characters.

SQL Server supports three types of collation sets:
+  **Windows collations** use the rules defined for collations by the operating system locale where UNICODE and non-UNICODE data use the same comparison algorithms.
+  **Binary collations** use the binary bit-wise code for comparison. Therefore, the locale doesn’t affect sorting.
+  **SQL Server collations** provide backward compatibility with previous SQL Server versions. They aren’t compatible with the windows collation rules for non-UNICODE data.

You can define collations at various levels:
+  **Server-level collations** determine the collations used for all system databases and is the default for future user databases. While the system databases collation can’t be changed, you can specify an alternative collation as part of the `CREATE DATABASE` statement.
+  **Database-level collations** inherit the server default unless the `CREATE DATABASE` statement explicitly sets a different collation. This collation is used as a default for all `CREATE TABLE` and `ALTER TABLE` statements.
+  **Column-level collations** can be specified as part of the `CREATE TABLE` or `ALTER TABLE` statements to override the default collation setting of your database.
+  **Expression-level collations** can be set for individual string expressions using the COLLATE function. For example, `SELECT * FROM MyTable ORDER BY StringColumn COLLATE Latin1_General_CS_AS`.

SQL Server supports UCS-2 UNICODE only.

SQL Server 2019 adds support for UTF-8 for import and export encoding, and as database-level or column-level collation for string data. Support includes PolyBase external tables, and Always Encrypted when not used with Enclaves. For more information, see [Collation and Unicode Support](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver15).

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.collations.sqlserver.syntax"></a>

```
CREATE DATABASE <Database Name>
[ ON <File Specifications> ]
COLLATE <Collation>
[ WITH <Database Option List> ];
```

```
CREATE TABLE <Table Name>
(
<Column Name> <String Data Type>
COLLATE <Collation> [ <Column Constraints> ]...
);
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.collations.sqlserver.examples"></a>

The following example creates a database with a default Bengali\_100\_CS\_AI collation.

```
CREATE DATABASE MyBengaliDatabase
ON
( NAME = MyBengaliDatabase_Datafile,
  FILENAME = 'C:\Program Files\Microsoft SQL Server-\MSSQL13.MSSQLSERVER\MSSQL\DATA\MyBengaliDatabase.mdf', SIZE = 100)
LOG ON
( NAME = MyBengaliDatabase_Logfile,
FILENAME = 'C:\Program Files\Microsoft SQL Server-\MSSQL13.MSSQLSERVER\MSSQL\DATA\MyBengaliDblog.ldf', SIZE = 25)
COLLATE Bengali_100_CS_AI;
```

The following example creates a table with two different collations.

```
CREATE TABLE MyTable
(
Col1 CHAR(10) COLLATE Hungarian_100_CI_AI_SC NOT NULL PRIMARY KEY,
COL2 VARCHAR(100) COLLATE Sami_Sweden_Finland_100_CS_AS_KS NOT NULL
);
```

For more information, see [Collation and Unicode support](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.collations.pg"></a>

PostgreSQL supports a variety of different character sets, also known as encoding, including support for both single-byte and multi-byte languages. The default character set is specified when initializing a PostgreSQL database cluster with `initdb`. Each individual database created on the PostgreSQL cluster supports individual character sets defined as part of database creation.

**Note**  
For Amazon Relational Database Service (Amazon RDS), starting with PostgreSQL 13, the Windows version now supports obtaining version information for collations or ordering rules from the operating system.

When you query the collation in PostgreSQL running on Windows, prior to version 13 there wasn’t any value to reflect the OS collation version. For example, for PostgreSQL version 11 running on Windows, the result is shown following:

```
CREATE COLLATION german (provider = libc, locale = 'de_DE');

CREATE COLLATION

select oid,collname,collversion from pg_collation
where collprovider='c' and collname='german';

oid    collname  collversion
16394  german
(1 row)

select pg_collation_actual_version (16394);

pg_collation_actual_version
(1 row)
```

For PostgreSQL version 13 running on Windows, the result is shown following:

```
CREATE COLLATION german (provider = libc, locale = 'de_DE');

CREATE COLLATION

select oid,collname,collversion from pg_collation
where collprovider='c' and collname='german';

oid    collname  collversion
32769  german    1539.5,1539.5
(1 row)

select pg_collation_actual_version (32769);

pg_collation_actual_version
1539.5,1539.5
(1 row)
```

Clients can use all supported character sets. However, some client-side only characters aren’t supported for use within the server.

Unlike SQL Server, PostgreSQL doesn’t natively support an NVARHCHAR data type and doesn’t provide support for UTF-16.


| Type | Function | Implementation level | 
| --- | --- | --- | 
| Encoding | Defines the basic rules on how alphanumeric characters are represented in binary format. For example, Unicode encoding. | Database | 
| Locale | A superset that includes `LC_COLLATE` and `LC_CTYPE` among others. For example, `LC_COLLATE` defines how strings are sorted and must be a subset supported by the database encoding. | Table-Column | 

### Examples
<a name="chap-sql-server-aurora-pg.tsql.collations.pg.examples"></a>

The following example creates a database named test01 which uses the Korean EUC\_KR Encoding the and the `ko_KR` locale.

```
CREATE DATABASE test01 WITH ENCODING 'EUC_KR' LC_COLLATE='ko_KR.euckr' LC_CTYPE='ko_KR.euckr' TEMPLATE=template0;
```

The following example shows how to view the character sets configured for each database by querying the system catalog.

```
select datname, datcollate, datctype from pg_database;
```

### Changing Character Sets or Encoding
<a name="chap-sql-server-aurora-pg.tsql.collations.pg.changing"></a>

In-place modification of the database encoding isn’t recommended nor supported. Instead, export all data, create a new database with the new encoding, and import the data.

Export the data using the `pg_dump` utility.

```
pg_dump mydb1 > mydb1_export.sql
```

Rename or delete a database.

```
ALTER DATABASE mydb1 TO mydb1_backup;
```

Create a new database using the modified encoding.

```
CREATE DATABASE mydb1_new_encoding WITH ENCODING 'UNICODE' TEMPLATE=template0;
```

Import data using the `pg_dump` file previously created. Verify that you set your client encoding to the encoding of your old database.

```
PGCLIENTENCODING=OLD_DB_ENCODING psql -f mydb1_export.sql mydb1_new_encoding
```

The `client_encoding` parameter overrides the use of `PGCLIENTENCODING`.

### Client-Server Character Set Conversions
<a name="chap-sql-server-aurora-pg.tsql.collations.pg.conversions"></a>

PostgreSQL supports conversion of character sets between servers and clients for specific character set combinations as described in the `pg_conversion` system catalog.

PostgreSQL includes predefined conversions. For more information, see [Available Character Set Conversions](https://www.postgresql.org/docs/13/static/multibyte.html#MULTIBYTE-TRANSLATION-TABLE) in the *PostgreSQL documentation*.

You can create a new conversion using the SQL command `CREATE CONVERSION`.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.collations.pg.conversionexamples"></a>

The following example creates a conversion from UTF8 to LATIN1 using the custom `myfunc1` function.

```
CREATE CONVERSION myconv FOR 'UTF8' TO 'LATIN1' FROM myfunc1;
```

The following example configures the PostgreSQL client character set.

```
Method 1
========
psql \encoding SJIS

Method 2
========
SET CLIENT_ENCODING TO 'value';
```

View the client character set and reset it back to the default value.

```
SHOW client_encoding;

RESET client_encoding;
```

### Table Level Collation
<a name="chap-sql-server-aurora-pg.tsql.collations.pg.collation"></a>

PostgreSQL supports specifying the sort order and character classification behavior on a per-column level.

### Example
<a name="chap-sql-server-aurora-pg.tsql.collations.pg.collationexample"></a>

Specify specific collations for individual table columns.

```
CREATE TABLE test1 (col1 text COLLATE "de_DE", col2 text COLLATE "es_ES");
```

## Summary
<a name="chap-sql-server-aurora-pg.tsql.collations.summary"></a>


| Feature | SQL Server |  Aurora PostgreSQL  | 
| --- | --- | --- | 
| View database character set |  `SELECT collation_name FROM sys.databases;`  |  `select datname, pg_encoding_to_char(encoding), datcollate, datctype from pg_database;`  | 
| Modify the database character set |  `RECRATE` the database |  +  Export the database. <br />+  Drop or rename the database. <br />+  Re-create the database with the desired new character set. <br />+  Import database data from the exported file into the new database.   | 
| Character set granularity | Database | Database | 
| UTF8 | Supported | Supported | 
| UTF16 | Supported | Not Supported | 
|  `NCHAR` or `NVARCHAR` data types | Supported | Not Supported | 

For more information, see [Character Set Support](https://www.postgresql.org/docs/13/multibyte.html) in the *PostgreSQL documentation*.