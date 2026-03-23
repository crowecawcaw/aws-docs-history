# Oracle and MySQL character sets

With AWS DMS, you can migrate databases between different platforms while preserving character set encodings and collations. Character sets define the encoding used to represent characters, while collations determine the sorting order and comparison rules. Properly configuring character sets and collations is crucial for applications that handle multilingual data or have specific sorting requirements.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                               |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | N/A                       | Different syntax. MySQL can have different collations for each database in the same instance. |

## Oracle usage

Oracle supports most national and international encoded character set standards including extensive support for Unicode.

Oracle provides two scalar string-specific data types:

- `VARCHAR2` — Stores variable-length character strings with a length between 1 and 4000 bytes. The Oracle database can be configured to use the `VARCHAR2` data type to store either Unicode or Non-Unicode characters.
- `NVARCHAR2` — Scalar data type used to store Unicode data. Supports AL16UTF16 or UTF8 and id specified during database creation.

Character sets in Oracle are defined at the instance level (Oracle 11g) or the pluggable database level (Oracle 12c R2). In Pre-12cR2 Oracle databases, the character set for the root container and all pluggable databases were required to be identical.

Oracle 18c updates AL32UTF8 and AL16UTF16 character sets to Unicode standard version 9.0.

### UTF8 Unicode

In Oracle, you can use the AL32UTF8 character set. Oracle provides encoding of ASCII characters as single-byte for Latin characters, two-bytes for some European and Middle-Eastern languages, and three-bytes for certain South and East-Asian characters. Therefore, Unicode storage requirements are usually higher when compared non-Unicode character sets.

### Character set migration

Two options exist for modifying existing Instance-level or database-level character sets:

- Export or import from the source Instance/PDB to a new Instance/PDB with a modified character set.
- Use the Database Migration Assistant for Unicode (DMU), which simplifies the migration process to the Unicode character set.

As of 2012, use of the `CSALTER` utility for character set migrations is deprecated.

Oracle Database 12c Release 1 (12.1.0.1) complies with version 6.1 of the Unicode standard.

Oracle Database 12c Release 2 (12.1.0.2) extends the compliance to version 6.2 of the Unicode standard.

UTF-8 is supported through the AL32UTF8 CS and is valid as both the client and database character sets.

UTF-16BE is supported through AL16UTF16 and is valid as the national (NCHAR) character set.

For more information, see [Choosing a Character Set](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/choosing-character-set.html#GUID-BF26E01D-AB92-48FC-855A-69A5B3AF9A92 "https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/choosing-character-set.html#GUID-BF26E01D-AB92-48FC-855A-69A5B3AF9A92"), [Locale Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/appendix-A-locale-data.html#GUID-A9E30C27-FD47-4552-B670-F41A95B11405 "https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/appendix-A-locale-data.html#GUID-A9E30C27-FD47-4552-B670-F41A95B11405"), and [Supporting Multilingual Databases with Unicode](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/supporting-multilingual-databases-with-unicode.html#GUID-AA09A60E-123E-457C-ACE1-89E4634E492C "https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/supporting-multilingual-databases-with-unicode.html#GUID-AA09A60E-123E-457C-ACE1-89E4634E492C") in the _Oracle documentation_.

## MySQL usage

MySQL supports a variety of different character sets including support for both single-byte and multi-byte languages. The default character set is specified when initializing a MySQL database cluster with `initdb`. Each individual database created on the MySQL cluster supports individual character sets defined as part of database creation.

To query the available character sets, use the `INFORMATION_SCHEMA CHARACTER_SETS` table or the `SHOW CHARACTER SET` statement.

All character sets have at least one collation, and most character sets have more. To list the display collations for a character set, use the `INFORMATION_SCHEMA COLLATIONS` table or the `SHOW COLLATION` statement.

Collations have these general characteristics:

- Two different character sets cannot have the same collation.
- Each character set has a default collation.
- Collation names start with the name of the character set with which they are associated and are generally followed by one or more suffixes indicating other collation characteristics.

### Examples

Create a database named test01 which uses the Korean EUC_KR Encoding the and the ko_KR locale.

```
CREATE DATABASE test01 CHARACTER SET = euckr COLLATE = euckr_korean_ci;
```

View the character sets configured for each database by querying the System Catalog.

```
SELECT SCHEMA_NAME,
    DEFAULT_CHARACTER_SET_NAME,
    DEFAULT_COLLATION_NAME
FROM INFORMATION_SCHEMA.SCHEMATA;
```

Convert a character set and collation using the `ALTER DATABASE` command.

```
ALTER DATABASE test01 CHARACTER SET = ucs2 COLLATE = ucs2_general_ci;
```

MySQL supports conversion of character sets between server and client for specific character set combinations with the parameter `character_set_client` and `character_set_connection`. For more information, see [Connection Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-connection.html "https://dev.mysql.com/doc/refman/5.7/en/charset-connection.html").

In MySQL, you can specify the sort order and character classification behavior on a per-column level. Specify specific collations for individual table columns.

```
CREATE TABLE lang(
latin1_col CHAR(10) CHARACTER SET latin1 COLLATE latin1_german1_ci,
latin2_col CHAR(10) CHARACTER SET latin2);
```

## Summary

| Feature                           | Oracle                                                                                                                          | Aurora MySQL                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| View database character set       | `<br>SELECT<br>• FROM NLS_DATABASE_PARAMETERS;<br>`                                                                             | `<br>SELECT SCHEMA_NAME,<br>DEFAULT_CHARACTER_SET_NAME,<br>DEFAULT_COLLATION_NAME<br>FROM INFORMATION_SCHEMA.SCHEMATA;<br>` |
| Modify the database character set | Choose one of the following options:<br>1. Full export or import.<br>2. When converting to Unicode, use the Oracle DMU utility. | `<br>ALTER DATABASE test01<br>CHARACTER SET = ucs2<br>COLLATE = ucs2_general_ci;<br>`                                       |
| Character set granularity         | Instance (11g + 12cR1)<br>Database (Oracle 12cR2)                                                                               | Column                                                                                                                      |
| UTF8                              | Supported by using `VARCHAR2` and `NVARCHAR`                                                                                    | Supported by using `CHAR` and `VARCHAR`                                                                                     |
| UTF16                             | Supported by using `NVARCHAR2`                                                                                                  | Supported by using `CHAR` and `VARCHAR`                                                                                     |
| `NCHAR` and `NVARCHAR` data types | Supported                                                                                                                       | Supported                                                                                                                   |

For more information, see [Character Sets, Collations, Unicode](https://dev.mysql.com/doc/refman/5.7/en/charset.html "https://dev.mysql.com/doc/refman/5.7/en/charset.html") and [Database Character Set and Collation](https://dev.mysql.com/doc/refman/5.7/en/charset-database.html "https://dev.mysql.com/doc/refman/5.7/en/charset-database.html") in the _MySQL documentation_.
