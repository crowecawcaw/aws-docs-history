

# Oracle character sets and PostgreSQL encoding
<a name="chap-oracle-aurora-pg.special.charset"></a>

With AWS DMS, you can migrate databases between different database platforms while handling character set and encoding differences. Oracle databases use character sets to define which characters are allowed, while PostgreSQL uses encodings for the same purpose.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  | N/A | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-pg.special.charset.ora"></a>

Oracle supports most national and international encoded character set standards including extensive support for Unicode.

Oracle provides two scalar string-specific data types:
+  **VARCHAR2** — Stores variable-length character strings with a length between 1 and 4000 bytes. The Oracle database can be configured to use the VARCHAR2 data type to store either Unicode or Non-Unicode characters.
+  **NVARCHAR2** — Scalar data type used to store Unicode data. Supports AL16UTF16 or UTF8 and id specified during database creation.

Character sets in Oracle are defined at the instance level (Oracle 11g) or the pluggable database level (Oracle 12c R2). In Pre-12cR2 Oracle databases, the character set for the root container and all pluggable databases were required to be identical.

Oracle 18c updates AL32UTF8 and AL16UTF16 characted sets to Unicode standard version 9.0.

### UTF8 Unicode
<a name="chap-oracle-aurora-pg.special.charset.ora.utf"></a>

Oracle’s implementation uses the AL32UTF8 character set and provides encoding of ASCII characters as single-byte for latin characters, two-bytes for some European and Middle-Eastern languages, and three-bytes for certain South and East-Asian characters. Therefore, Unicode storage requirements are usually higher when compared non-Unicode character sets.

### Character set migration
<a name="chap-oracle-aurora-pg.special.charset.ora.csm"></a>

Two options exist for modifying existing instance-level or database-level character sets:
+ Export/Import from the source Instance/PDB to a new Instance/PDB with a modified character set.
+ Use the Database Migration Assistant for Unicode (DMU), which simplifies the migration process to the Unicode character set.

As of 2012, use of the `CSALTER` utility for character set migrations is deprecated.

**Note**  
Oracle Database 12c Release 1 (12.1.0.1) complies with version 6.1 of the Unicode standard.  
Oracle Database 12c Release 2 (12.1.0.2) extends the compliance to version 6.2 of the Unicode standard.  
UTF-8 is supported through the AL32UTF8 CS and is valid as both the client and database character sets.  
UTF-16BE is supported through AL16UTF16 and is valid as the national (NCHAR) character set.

For more information, see [Choosing a Character Set](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/choosing-character-set.html#GUID-BF26E01D-AB92-48FC-855A-69A5B3AF9A92), [Locale Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/appendix-A-locale-data.html#GUID-A9E30C27-FD47-4552-B670-F41A95B11405), and [Supporting Multilingual Databases with Unicode](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/supporting-multilingual-databases-with-unicode.html#GUID-AA09A60E-123E-457C-ACE1-89E4634E492C) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.special.charset.pg"></a>

PostgreSQL supports a variety of different character sets, also known as encoding, including support for both single-byte and multi-byte languages. The default character set is specified when initializing your PostgreSQL database cluster with initdb. Each individual database created on the PostgreSQL cluster supports individual character sets defined as part of database creation.

**Note**  
Starting with PostgreSQL 13, Windows version now support obtaining version information for collations (ordering rules) from OS. This option is relevant for self-managed PostgreSQL installations running on Windows.

When querying the collversion from pg\_collation in PostgreSQL running on Windows, prior to version 13 there wasn’t any value to reflect the OS collation version, for example version 11 running on Windows.

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

Starting with PostgreSQL 13 running on Windows.

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

**Note**  
All supported character sets can be used by clients. However, some client-side only characters are not supported for use within the server.  
Unlike Oracle, PostgreSQL doesn’t support an NVARHCHAR data type and doesn’t offer support for UTF-16.


| Type | Function | Implementation level | 
| --- | --- | --- | 
| Encoding | Defines the basic rules on how alphanumeric characters are represented in binary format, for example, Unicode Encoding. | Database | 
| Locale | Superset which include LC\_COLLATE and LC\_CTYPE, among others. LC\_COLLATE defines how strings are sorted and needs to be a subset supported by the database Encoding. LC\_CTYPE is used to classify if a character is a digit, letter, whitespace, punctuation, and so on. | Table-Column | 

 **Examples** 

Create a database named test01 which uses the Korean EUC\_KR Encoding the and the ko\_KR locale.

```
CREATE DATABASE test01 WITH ENCODING 'EUC_KR' LC_COLLATE='ko_KR.euckr' LC_CTYPE='ko_KR.euckr' TEMPLATE=template0;
```

View the character sets configured for each database by querying the System Catalog.

```
select datname, datcollate, datctype from pg_database;
```

### Changing character sets or encoding
<a name="chap-oracle-aurora-pg.special.charset.pg.change"></a>

In-place modification of the database encoding is not recommended nor supported. You must export all data, create a new database with the new encoding, and import the data.

Export the data using the pg\_dump utility.

```
pg_dump mydb1 > mydb1_export.sql
```

Rename or delete your current database.

```
ALTER DATABASE mydb1 TO mydb1_backup;
```

Create a new database using the modified encoding.

```
CREATE DATABASE mydb1_new_encoding WITH ENCODING 'UNICODE' TEMPLATE=template0;
```

Import the data using the pg\_dump file previously created. Verify that you set your client encoding to the encoding of your old database.

```
PGCLIENTENCODING=OLD_DB_ENCODING psql -f mydb1_export.sql mydb1_new_encoding
```

**Note**  
Using the client\_encoding parameter overrides the use of PGCLIENTENCODING.

### Client/server character set conversions
<a name="chap-oracle-aurora-pg.special.charset.pg.client"></a>

PostgreSQL supports conversion of character sets between server and client for specific character set combinations as described in the pg\_conversion system catalog.

PostgreSQL includes predefined conversions. For a complete list, see [Built-in Client/Server Character Set Conversions](https://www.postgresql.org/docs/13/static/multibyte.html#MULTIBYTE-TRANSLATION-TABLE).

You can create a new conversion using the SQL command CREATE CONVERSION.

 **Examples** 

Create a conversion from UTF8 to LATIN1 using a custom-made myfunc1 function.

```
CREATE CONVERSION myconv FOR 'UTF8' TO 'LATIN1' FROM myfunc1;
```

Configure the PostgreSQL client character set.

```
psql \encoding SJIS

SET CLIENT_ENCODING TO 'value';
```

View the client character set and reset it back to the default value.

```
SHOW client_encoding;

RESET client_encoding;
```

### Table level collation
<a name="chap-oracle-aurora-pg.special.charset.pg.collation"></a>

PostgreSQL supports specifying the sort order and character classification behavior on a per-column level.

 **Example** 

Specify specific collations for individual table columns.

```
CREATE TABLE test1 (col1 text COLLATE "de_DE", col2 text COLLATE "es_ES");
```

## Summary
<a name="chap-oracle-aurora-pg.special.charset.summary"></a>


| Feature | Oracle |  Aurora PostgreSQL | 
| --- | --- | --- | 
| View database character set |  <pre>SELECT * FROM NLS_DATABASE_PARAMETERS;</pre>  |  <pre>select datname,<br />  pg_encoding_to_char(encoding),<br />  datcollate, datctype<br />  from pg_database;</pre>  | 
| Modify the database character set |  +  Full Export/Import. <br />+  When converting to Unicode, use the Oracle DMU utility.   |  +  Export the database. <br />+  Drop or rename the database. <br />+  Re-create the database with the desired new character set. <br />+  Import database data from the exported file into the new database.   | 
| Character set granularity |  +  Instance (11g \+ 12cR1) <br />+  Database (Oracle 12cR2)   | Database | 
| UTF8 | Supported by VARCHAR2 and NVARCHAR data types | Supported by VARCHAR datatype | 
| UTF16 | Supported by NVARCHAR2 datatype | Not Supported | 
| NCHAR/NVARCHAR data types | Supported | Not Supported | 

For more information, see [Character Set Support](https://www.postgresql.org/docs/10/multibyte.html) in the *PostgreSQL documentation*.