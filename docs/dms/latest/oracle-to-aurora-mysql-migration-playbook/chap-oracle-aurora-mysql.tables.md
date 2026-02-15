# Oracle and MySQL tablespaces and data files

Oracle and MySQL databases use tablespaces and data files to store data. A tablespace is a logical storage unit, while a data file is a physical file that stores data for the tablespace. The following sections provide details on working with tablespaces and data files during database migration.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                           |
| -------------------------------- | ---------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | Aurora MySQL doesn’t support tablespace for each file only and physical files attributes. |

## Oracle usage

The storage structure of an Oracle database contains both physical and logical elements.

- **Tablespaces** — Each Oracle database contains one or more tablespaces, which are logical storage groups used as containers for creating new tables and indexes.
- **Data files** — Each tablespace is made up of one or more data files, which are the physical elements of an Oracle database tablespace. Datafiles can be located on the local file system, located in raw partitions, managed by Oracle ASM, or located on a network file system.

### Storage hierarchy

- **Database** — Each Oracle database is composed of one or more tablespaces.
- **Tablespace** — Each Oracle tablespace is composed of one or more data files. Tablespaces are logical entities that have no physical manifestation on the file system.
- **Data files** — Physical files located on a file system. Each Oracle tablespace consists of one or more data files.
- **Segments** — Each segment represents a single database object that consumes storage such as tables, indexes, and undo segments.
- **Extent** — Each segment consists of one or more extents. Oracle uses extents to allocate contiguous sets of database blocks on disk.
- **Block** — The smallest unit of I/O for reads and writes. For blocks storing table data, each block can store one or more table rows.

### Types of Oracle database tablespaces

- **Permanent tablespaces** — Designated to store persistent schema objects for applications.
- **Undo tablespace** — A special type of system permanent tablespace used by Oracle to manage UNDO data when running the database in automatic undo management mode.
- **Temporary tablespace** — Contains schema objects valid for the duration of a session. It is also used for sort operations that can’t fit into memory.

### Tablespace privileges

Make sure that you meet the following criteria when you create a tablespace:

- The database user has the `CREATE TABLESAPCE` system privilege.
- The database is in `OPEN` mode.

### Examples

Create a `USERS` tablespace comprised of a single data file.

```
CREATE TABLESPACE USERS
  DATAFILE '/u01/app/oracle/oradata/orcl/users01.dbf' SIZE 5242880
  AUTOEXTEND ON NEXT 1310720 MAXSIZE 32767M
  LOGGING ONLINE PERMANENT BLOCKSIZE 8192
  EXTENT MANAGEMENT LOCAL AUTOALLOCATE DEFAULT
  NOCOMPRESS SEGMENT SPACE MANAGEMENT AUTO;
```

Drop a tablespace.

```
DROP TABLESPACE USERS;
  OR
DROP TABLESPACE USERS INCLUDING CONTENTS AND DATAFILES;
```

For more information, see [CREATE TABLESPACE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLESPACE.html#GUID-51F07BF5-EFAF-4910-9040-C473B86A8BF9 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLESPACE.html#GUID-51F07BF5-EFAF-4910-9040-C473B86A8BF9"), [file_specification](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/file_specification.html#GUID-580FA726-F712-4410-90CF-783A2DA89688 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/file_specification.html#GUID-580FA726-F712-4410-90CF-783A2DA89688"), and [DROP TABLESPACE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-TABLESPACE.html#GUID-C91F3E94-4503-48DE-9BCA-42E495E6BE11 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-TABLESPACE.html#GUID-C91F3E94-4503-48DE-9BCA-42E495E6BE11") in the _Oracle documentation_.

## MySQL usage

Aurora MySQL logical storage structure is similar to Oracle. It uses tablespaces for storing database objects, but the General Tablespace isn’t supported. Only InnoDB file-per-table is provided.

###### Note

Starting from Amazon Relational Database Service (Amazon RDS) for MySQL version 8, you can rename a general tablespace using the `ALTER TABLESPACE …​ RENAME TO` syntax.

- **Tablespace** — the directory where data files are stored.
- **Data files** — file-system files that are placed inside a tablespace (directory) and are used to store database objects such as tables or indexes. Created automatically by MySQL,. Similar to how Oracle-Managed-Files (OMF) behave.

The InnoDB file-per-table feature applies to each InnoDB table. Its indexes are stored in a separate `.ibd` data file. Each `.ibd` data file represents an individual tablespace.

### Tablespaces

After you create an Amazon Aurora MySQL cluster, three system tablespaces are automatically provisioned. You can’t modify or drop them. These tablespaces hold database metadata or provide temporary storage for sorting and calculations:

- `innodb_system`
- `innodb_temporary`
- `innodb_file_per_table_n`

One of the main advantages when using Aurora MySQL is the reduced complexity of storage management. You don’t need to create tablespaces because Aurora MySQL uses a unique, self-managed shared storage architecture. Database administrators don’t need to manage most storage aspects of databases.

### Example

View all tablespaces.

```
SELECT * FROM INFORMATION_SCHEMA.FILES;
```

## Summary

| Feature                                                | Oracle                                                                                                                                                                                                                                                                                                                                                                                                | Amazon Aurora MySQL                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tablespace                                             | Exists as a logical object and made from one or more user-specified or system-generated data files.                                                                                                                                                                                                                                                                                                   | Exists as a logical object and consists of one data file.                                                                                                                                                                                                                                      |
| Data file                                              | Can be explicitly created and resized by the user. Oracle-Managed-Files (OMF) support automatically created data files.<br>Each data file can contain one or more tables and/or indexes.                                                                                                                                                                                                              | The behavior is more like Oracle Managed Files (OMF).<br>• Created automatically in the directory assigned to the tablespace.<br>• A single data file stores information for a specific table or index. Multiple data files can exist for a table or index.                                    |
| Create a new tablespace with system-managed data files | `<br>CREATE TABLESPACE sales_tbs<br>DATAFILE SIZE 400M;<br>`                                                                                                                                                                                                                                                                                                                                          | Not supported                                                                                                                                                                                                                                                                                  |
| Create a new tablespace with user-managed data files   | `<br>CREATE TABLESPACE sales_tbs<br>DATAFILE '/oradata/sales01.dbf' SIZE 1M<br>AUTOEXTEND ON NEXT 1M;<br>`                                                                                                                                                                                                                                                                                            | Not supported                                                                                                                                                                                                                                                                                  |
| Alter the size of a datafile                           | `<br>ALTER DATABASE DATAFILE<br>'/oradata/-sales01.dbf'<br>RESIZE 100M;<br>`                                                                                                                                                                                                                                                                                                                          | `<br>ALTER TABLE EMPLOYEES FORCE;<br>`<br>Reclaims free space in the data file, which can reduce and tablespace size.                                                                                                                                                                          |
| Add a datafile to an existing tablespace               | `<br>ALTER TABLESPACE sales_tbs<br>ADD DATAFILE '/oradata/sales02.dbf'<br>SIZE 10M;<br>`                                                                                                                                                                                                                                                                                                              | Not supported                                                                                                                                                                                                                                                                                  |
| Per-database tablespace                                | Supported as part of the Oracle 12c Multi-Tenant architecture. You can create different dedicated tablespaces for different pluggable databases and set as the default tablespace for a PDB:<br>`<br>ALTER SESSION SET CONTAINER = 'sales';<br>CREATE TABLESPACE sales_tbs<br>DATAFILE '/oradata/sales01.dbf' SIZE 1M<br>AUTOEXTEND ON NEXT 1M;<br>ALTER DATABASE sales TABLESPACE<br>sales_tds;<br>` | Not supported                                                                                                                                                                                                                                                                                  |
| Metadata tables                                        | Data Dictionary tables are stored in the `SYSTEM` tablespace.                                                                                                                                                                                                                                                                                                                                         | Data Dictionary tables are stored in the `innodb_system` tablespace.                                                                                                                                                                                                                           |
| Tablespace data encryption                             | **Supported**<br>• Supported using transparent data encryption.<br>• Encryption and decryption are handled seamlessly. Users don’t have to modify the application to access the data.                                                                                                                                                                                                                 | **Supported**<br>• Encrypt using keys managed through AWS KMS.<br>• Encryption and decryption are handled seamlessly. Users doesn’t have to modify the application to access the data.<br>• Enable encryption while deploying a new cluster with the AWS Management Console or API operations. |

For more information, see [Encrypting Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in the _Amazon Relational Database Service User Guide_.
