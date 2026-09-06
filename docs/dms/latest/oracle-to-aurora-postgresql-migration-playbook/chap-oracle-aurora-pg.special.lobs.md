

# Oracle SecureFile LOBs and PostgreSQL large objects
<a name="chap-oracle-aurora-pg.special.lobs"></a>

With AWS DMS, you can efficiently migrate data from Oracle SecureFile LOBs and PostgreSQL large objects to target databases. Oracle SecureFile LOBs and PostgreSQL large objects are data types used to store large binary data or character data, such as documents, images, and multimedia files.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  | N/A | PostgreSQL doesn’t support SecureFiles, automation and compatibility refer only to LOBs. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.special.lobs.ora"></a>

Large Objects (LOB) is a mechanism for storing binary data in a database. Oracle 11g introduced Secure File LOBS that provide more efficiently storage. They are created using the SECUREFILE keyword as part of the `CREATE TABLE` statement.

The Primary benefits of using `SECUREFILE` lobs include:
+  **Compression** — Uses Oracle advanced compression to analyze SecureFiles LOB data to save disk space.
+  **De-Duplication** — Automatically detects duplicate LOB data within a LOB column or partition and reduces storage space by removing duplicates of repeating binary data.
+  **Encryption** — Combined with Transparent Data Encryption (TDE).

 **Examples** 

Create a table using a SecureFiles LOB column.

```
CREATE TABLE sf_tab (COL1 NUMBER, COL2_CLOB CLOB) LOB(COL2_CLOB)
  STORE AS SECUREFILE;
```

Provide additional options for LOB compression during table creation.

```
CREATE TABLE sf_tab (COL1 NUMBER,COL2_CLOB CLOB) LOB(COL2_CLOB)
  STORE AS SECUREFILE COMPRESS_LOB(COMPRESS HIGH);
```

For more information, see [Introduction to Large Objects and SecureFiles](https://docs.oracle.com/en/database/oracle/oracle-database/19/adlob/introduction-to-large-objects.html#GUID-1A2B0023-9EE8-48AF-AA76-171D1FC5C241) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.special.lobs.pg"></a>

PostgreSQL doesn’t support the advanced storage, security, and encryption options of Oracle SecureFile LOBs. Regular Large Objects datatypes (LOBs) are supported by PostgreSQL and provides stream-style access.

Although not designed specifically from LOB columns, for compression PostgreSQL uses an internal TOAST mechanism (The Oversized-Attribute Storage Technique).

For more information, see [TOAST](https://www.postgresql.org/docs/13/storage-toast.html) in the *PostgreSQL documentation*.

### Large object data types supported by PostgreSQL
<a name="chap-oracle-aurora-pg.special.lobs.pg.dt"></a>

 **BYTEA** 
+ Stores a LOB within the table limited to 1GB.
+ The storage is octal and supports non-printable characters.
+ The input / output format is HEX.
+ Can be used to store a URL references to an Amazon S3 objects used by the database. For example, storing the URL for pictures stored on Amazon S3 on a database table.

 **TEXT** 
+ Data type for storing strings with unlimited length.
+ When not specifying the (n) integer for specifying the varchar data type, the TEXT datatype behaves as the text data type.

For data encryption purposes (not only for LOB columns), consider using [AWS Key Management Service](https://aws.amazon.com/kms).

For more information, see [Large Objects](https://www.postgresql.org/docs/13/largeobjects.html) in the *PostgreSQL documentation*.