

# Oracle SecureFile LOBs and MySQL large objects
<a name="chap-oracle-aurora-mysql.special.lobs"></a>

With AWS DMS, you can migrate data from Oracle and MySQL databases to other database engines, including large object data types like Oracle SecureFile LOBs and MySQL large objects. Oracle SecureFile LOBs and MySQL large objects are data types that store large amounts of unstructured data, such as text, images, audio, and video files.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  | N/A | MySQL doesn’t support SecureFiles, automation and compatibility refer only to LOBs. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.lobs.oracle"></a>

Large objects (LOB) is a mechanism for storing binary data in a database. Oracle 11g introduced SecureFile LOBs that provide more efficient storage. They are created using the `SECUREFILE` keyword as part of the `CREATE TABLE` statement.

The Primary benefits of using `SECUREFILE` lobs include:
+  **Compression** — Uses Oracle advanced compression to analyze SecureFiles LOB data to save disk space.
+  **De-Duplication** — Automatically detects duplicate LOB data within a LOB column or partition and reduces storage space by removing duplicates of repeating binary data.
+  **Encryption** — Combined with Transparent Data Encryption (TDE).

### Examples
<a name="chap-oracle-aurora-mysql.special.lobs.oracle.examples"></a>

The following example creates a table using a SecureFiles LOB column.

```
CREATE TABLE sf_tab (COL1 NUMBER, COL2_CLOB CLOB) LOB(COL2_CLOB)
  STORE AS SECUREFILE;
```

The following example provides additional options for LOB compression during table creation.

```
CREATE TABLE sf_tab (COL1 NUMBER,COL2_CLOB CLOB) LOB(COL2_CLOB)
  STORE AS SECUREFILE COMPRESS_LOB(COMPRESS HIGH);
```

For more information, see [Introduction to Large Objects and SecureFiles](https://docs.oracle.com/en/database/oracle/oracle-database/19/adlob/introduction-to-large-objects.html#GUID-1A2B0023-9EE8-48AF-AA76-171D1FC5C241) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.lobs.mysql"></a>

MySQL doesn’t support the advanced storage, security, and encryption options of Oracle SecureFile LOBs. MySQL supports regular LOB datatypes and provides stream-style access.

The four Binary Large Object (BLOB) types are: `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, and `LONGBLOB`.

These types differ only in the maximum length of the values they can hold.

The four `TEXT` types are: `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, and `LONGTEXT`.

BLOB values are treated as binary or byte strings. They have the binary character set, collation, and comparison. Sorting is based on the numeric values of the bytes in column values.

 `TEXT` values are treated as non-binary or character strings. They have a character set other than binary. Values are sorted and compared based on the collation of the character set.

For `TEXT` columns, index entries are space-padded at the end. If the index requires unique values, duplicate-key errors occur for values that differ only in the number of trailing spaces. For example, if a table contains 'b', an attempt to store 'b ' causes a duplicate-key error.

Because BLOB and TEXT values can be extremely long, there are some constraints:
+ Only the first `max_sort_length` bytes (default is 1024) of the column are used when sorting. You can make more bytes significant in sorting or grouping by increasing its value at server startup or runtime. Clients can change the value of this variable.
+  `BLOB` or `TEXT` columns in the result of a query that is processed using a temporary table causes the server to use a table on disk rather than in memory because the MEMORY storage engine does not support those data types. Use of disk incurs a performance penalty. Therefore, include `BLOB` or `TEXT` columns in the query result only if they are essential.
+  `BLOB` or `TEXT` types determine the maximum size, but the largest value that can be transmitted between the client and server is determined by the amount of available memory and the size of the communications buffers. Message buffer size can be changed by the `max_allowed_packet` variable, but it must be done for both server and client.

### Example
<a name="chap-oracle-aurora-mysql.special.lobs.mysql.examples"></a>

The following example creates a table using a BLOB column with an index.

```
CREATE TABLE test (blob_col BLOB, INDEX(blob_col(10)));
```

For more information, see [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html) and [The BLOB and TEXT Types](https://dev.mysql.com/doc/refman/5.7/en/blob.html) in the *MySQL documentation*.