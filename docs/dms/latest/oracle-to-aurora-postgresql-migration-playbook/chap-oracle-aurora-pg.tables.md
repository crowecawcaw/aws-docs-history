# Oracle and PostgreSQL tablespaces and data files

With AWS DMS, you can migrate data between different database platforms, including Oracle and PostgreSQL, while maintaining the integrity of tablespaces and data files. Tablespaces in Oracle and PostgreSQL are logical storage units that group related data files, allowing for better management and administration of database objects. Data files are the physical files on disk that store the actual data.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                      |
| ------------------------------- | ---------------------------------- | ------------------------- | -------------------------------------------------------------------- |
| Four star feature compatibility | N/A                                | N/A                       | All supported by PostgreSQL except managing the physical data files. |

## Oracle usage

The storage structure of an Oracle database contains both physical and logical elements.

- **Tablespaces** — Each Oracle database contains one or more tablespaces, which are logical storage groups used as containers for creating new tables and indexes.
- **Data Files** — Each tablespace is made up of one or more data files, which are the physical elements of an Oracle database tablespace. Datafiles can be located on the local file system, located in raw partitions, managed by Oracle ASM, or located on a network file system.

### Storage Hierarchy

- **Database** — Each Oracle database is composed of one or more tablespaces.
- **Tablespace** — Each Oracle tablespace is composed of one or more datafiles. Tablespaces are logical entities that have no physical manifestation on the file system.
- **Data files** — Physical files located on a file system. Each Oracle tablespace consists of one or more data files.
- **Segments** — Each segment represents a single database object that consumes storage such as tables, indexes, and undo segments.
- **Extent** — Each segment consists of one or more extents. Oracle uses extents to allocate contiguous sets of database blocks on disk.
- **Block** — The smallest unit of I/O for reads and writes. For blocks storing table data, each block can store one or more table rows.

### Types of Oracle Database Tablespaces

- **Permanent tablespaces** — Designated to store persistent schema objects for applications.
- **Undo tablespace** — A special type of system permanent tablespace used by Oracle to manage UNDO data when running the database in automatic undo management mode.
- **Temporary tablespace** — Contains schema objects valid for the duration of a session. It is also used for sort operations that can’t fit into memory.

**Tablespace privileges**

The following criteria must be met to create a tablespace:

- The database user must have the CREATE TABLESAPCE system privilege.
- The database must be in OPEN MODE.

**Examples**

Create a USERS tablespace comprised of a single data file.

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

## PostgreSQL usage

The logical storage structure in PostgreSQL shares similar concepts as Oracle, utilizing tablespaces for storing database objects. Tablespaces in PostgreSQL are made from datafiles and are used to store different databases and database object.

- **Tablespace** — the directory where datafiles are stored.
- **Data files** — file-system files that are placed inside a tablespace (directory) and are used to store database objects such as tables or indexes. Created automatically by PostgreSQL. Similar to how Oracle-Managed-Files (OMF) behave.

###### Note

Unlike Oracle, a PostgreSQL tablespace doesn’t have user-configured segmentation into multiple and separate data files. When you create the tablespace, PostgreSQL automatically creates the necessary files to store the data.

Each table and index are stored in a separate O/S file, named after the table or index’s filenode number.

### Tablespaces in Amazon Aurora PostgreSQL

After an Amazon Aurora PostgreSQL cluster is created, two system tablespaces are automatically provisioned
and can’t be modified or dropped.

- `pg_global tablespace` is used for the shared system catalogs. Stores objects that are visible to all Cluster databases.
- `pg_default tablespace` is the default tablespace of the `template1` and `template0` databases. Serves as the default tablespace for other databases, by default, unless a different tablespace was explicitly specified during database creation.

One of the main advantages when using Amazon Aurora PostgreSQL is the absence of complexity for storage management. Therefore, creating tablespaces in Aurora PostgreSQL is simplified and has several advantages over a vanilla PostgreSQL database deployment:

When you create tablespaces, the superuser can specify an OS path (location) that doesn’t currently exist. The directory will be implicitly created.

A user-specified tablespace directory will be created under an embedded Amazon RDS/Aurora path. For example, every path specified in the LOCATION clause when creating a new tablespace will be created under the Amazon RDS path of: `/rdsdbdata/tablespaces/`.

Amazon Aurora PostgreSQL uses a unique self-managed shared storage architecture. The DBA doesn’t need to micro-manage most storage aspects of the database.

**Examples**

Creating a tablespace with Amazon Aurora PostgreSQL and view its associated directory.

```
CREATE TABLESPACE TBS_01 LOCATION '/app_data/tbs_01';

\du

Name         Owner      Location
pg_default   rdsadmin
pg_global    rdsadmin
tbs_01       rdsadmin   /rdsdbdata/tablespaces/app_data/tbs_01
```

###### Note

The newly specified path was created under the embedded base path for Amazon Aurora: `/rdsdbdata/tablespaces/`.

View current tablespaces and associated directories.

```
select spcname, pg_tablespace_location(oid) from pg_tablespace;
```

Drop the PostgreSQL `TBS_01` tablespace.

```
DROP TABLESPACE TBS_01;
```

Alter a tablespace.

```
ALTER TABLESPACE TBS_01 RENAME TO IDX_TBS_01;

ALTER TABLESPACE TO IDX_TBS_01 OWNER TO USER1;
```

Assign a database with a specific tablespace.

```
CREATE DATABASE DB1 TABLESPACE TBS_01;

SELECT DATNAME, PG_TABLESPACE_LOCATION(DATTABLESPACE) FROM PG_DATABASE
WHERE DATNAME='db1';

datname  pg_tablespace_location
db1      /rdsdbdata/tablespaces/app_data/tbs_0
```

Assign a table with a specific tablespace.

```
CREATE TABLE TBL(COL1 NUMERIC, COL2 VARCHAR(10))
TABLESPACE TBS_01;

SELECT SCHEMANAME, TABLENAME, TABLESPACE FROM PG_TABLES
WHERE TABLENAME='tbl';

schemaname  tablename  tablespace
public      tbl        tbs_01
```

Assign an index with a specific tablespace.

```
CREATE INDEX IDX_TBL ON TBL(COL1)
TABLESPACE TBS_01;

SELECT SCHEMANAME, TABLENAME, INDEXNAME, TABLESPACE FROM PG_INDEXES
WHERE INDEXNAME='idx_tbl';

schemaname  tablename  indexname  tablespace
public      tbl        idx_tbl    tbs_01
```

Alter a table to use a different tablespace.

```
ALTER TABLE TBL SET TABLESPACE TBS_02;
```

**Tablespace exceptions**

`CREATE TABLESPACE` can’t be run inside a transaction block.

A tablespace can’t be dropped until all objects in all databases using the tablespace have been removed or moved.

**Privileges**

The creation of a tablespace in the PostgreSQL database must be performed by a database superuser.

After you create a tablespace, you can use it from any database, provided that the requesting user has sufficient privileges.

**Tablespace Parameters**

The default_tablespace parameter controls the system default location for newly created database objects. By default, this parameter is set to an empty value and any newly created database object will be stored in the default tablespace (pg_default).

The default_tablespace parameter can be altered by using the cluster parameter group.

To verify and to set the default_tablespace variable.

```
SHOW DEFAULT_TABLESPACE; -- No value
default_tablespace

SET DEFAULT_TABLESPACE=TBS_01;
SHOW DEFAULT_TABLESPACE;
default_tablespace

tbs_01
```

## Summary

| Feature                                                | Oracle                                                                                                                                                                                                                                                                                                                                                                                                | Aurora PostgreSQL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tablespace                                             | Exists as a logical object and made from one or more user-specified or system-generated data files.                                                                                                                                                                                                                                                                                                   | Logical object that is tied to a specific directory on the disk where datafiles will be created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Data file                                              | Can be explicitly created and resized by the user. Oracle-Managed-Files (OMF) allow for automatically created data files.<br>Each data file can contain one or more tables and/or indexes.                                                                                                                                                                                                            | Behavior is more akin to Oracle Managed Files (OMF).<br>Created automatically in the directory assigned to the tablespace.<br>Single data file stores information for a specific table or index. Multiple data files can exist for a table or index.<br>Additional files are created:<br>• **Freespace map file** exists in addition to the datafiles themselves. The free space map is stored as a file named with the filenode<br>number plus the \_fsm suffix.<br>• **Visibility map file** is stored with the \_vm suffix and used to track which pages are known to have no dead tuples. |
| Creates a new tablespace with system-managed datafiles | `<br>CREATE TABLESPACE sales_tbs<br>DATAFILE SIZE 400M;<br>`                                                                                                                                                                                                                                                                                                                                          | `<br>create tablespace sales_tbs LOCATION<br>'/postgresql/data';<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Create a new tablespace with user-managed datafiles    | `<br>CREATE TABLESPACE sales_tbs<br>DATAFILE '/oradata/sales01.dbf' SIZE 1M<br>AUTOEXTEND ON NEXT 1M;<br>`                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Alter the size of a datafile                           | `<br>ALTER DATABASE DATAFILE<br>'/oradata/-sales01.dbf'<br>RESIZE 100M;<br>`                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Add a datafile to an existing tablespace               | `<br>ALTER TABLESPACE sales_tbs<br>ADD DATAFILE '/oradata/sales02.dbf'<br>SIZE 10M;<br>`                                                                                                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Per-database tablespace                                | Supported as part of the Oracle 12c Multi-Tenant architecture. Different dedicated tablespaces can be created for different pluggable databases and set as the default tablespace for a PDB:<br>`<br>ALTER SESSION SET CONTAINER = 'sales';<br>CREATE TABLESPACE sales_tbs<br>DATAFILE '/oradata/sales01.dbf' SIZE 1M<br>AUTOEXTEND ON NEXT 1M;<br>ALTER DATABASE sales TABLESPACE<br>sales_tds;<br>` | Tablespaces are shared across all databases but a default tablespace can be created and configured for the database:<br>`<br>create tablespace sales_tbs LOCATION<br>'/postgresql/data';<br>CREATE DATABASE sales OWNER<br>sales_app TABLESPACE sales_tbs;<br>`                                                                                                                                                                                                                                                                                                                               |
| Metadata tables                                        | Data Dictionary tables are stored in the SYSTEM tablespace.                                                                                                                                                                                                                                                                                                                                           | System Catalog tables are stored in the pg_global tablespace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Tablespace data encryption                             | **Supported**<br>• Supported using transparent data encryption.<br>• Encryption and decryption are handled seamlessly. Users don’t have to modify the application to access the data.                                                                                                                                                                                                                 | **Supported**<br>• Encrypt using keys managed through AWS KMS.<br>• Encryption and decryption are handled seamlessly. Users doesn’t have to modify the application to access the data.<br>• Enable encryption while deploying a new cluster with the AWS Management Console or API operations.<br>For more information, see [Encrypting Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in the _Amazon Relational Database Service User Guide_.                                                                      |

For more information, see [Tablespaces](https://www.postgresql.org/docs/13/static/manage-ag-tablespaces.html "https://www.postgresql.org/docs/13/static/manage-ag-tablespaces.html"), [CREATE TABLESPACE](https://www.postgresql.org/docs/13/static/sql-createtablespace.html "https://www.postgresql.org/docs/13/static/sql-createtablespace.html"), [Database File Layout](https://www.postgresql.org/docs/13/static/storage-file-layout.html "https://www.postgresql.org/docs/13/static/storage-file-layout.html"), [Free Space Map](https://www.postgresql.org/docs/13/static/storage-fsm.html "https://www.postgresql.org/docs/13/static/storage-fsm.html"), [System Catalog Information Functions](https://www.postgresql.org/docs/13/static/functions-info.html#FUNCTIONS-INFO-CATALOG-TABLE "https://www.postgresql.org/docs/13/static/functions-info.html#FUNCTIONS-INFO-CATALOG-TABLE"), [DROP TABLESPACE](https://www.postgresql.org/docs/13/static/sql-droptablespace.html "https://www.postgresql.org/docs/13/static/sql-droptablespace.html"), and [ALTER TABLESPACE](https://www.postgresql.org/docs/13/static/sql-altertablespace.html "https://www.postgresql.org/docs/13/static/sql-altertablespace.html") in the _PostgreSQL documentation_.
