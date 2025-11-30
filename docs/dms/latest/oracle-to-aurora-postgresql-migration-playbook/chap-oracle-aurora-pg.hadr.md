# Oracle SQL\*Loader and PostgreSQL pg_dump and pg_restore

With AWS DMS, you can efficiently migrate data from flat files into AWS databases using Oracle SQL\*Loader and PostgreSQL `pg_dump` and `pg_restore` commands. These utilities facilitate bulk data loading from external files into database tables.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                  |
| ------------------------------- | ---------------------------------- | ------------------------- | -------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | N/A                       | Not all functions are supported by PostgreSQL and may require to create manually |

## Oracle usage

SQL\*Loader is powerful utility that imports data from external files into database tables. It has strong parsing engine with few limitations on data formats.

You can use SQL\*Loader with or without a control file. A control file enables handling more complicated load environments. For simpler loads, use SQL\*Loader without a control file (also referred to as SQL\*Loader Express).

The outputs of SQL\*Loader include the imported database data, a log file, a bad file (rejected records), and a discard file (if enabled).

**Examples**

Oracle SQL\*Loader is well suited for large databases with a limited number of objects. The process of exporting from a source database and loading to a target database is very specific to the schema. The following example creates sample schema objects, exports from a source, and loads into a target database.

Create a source table.

```
CREATE TABLE customer_0 TABLESPACE users
  AS SELECT rownum id, o.* FROM all_objects o, all_objects x
    where rownum <= 1000000;
```

On the target Amazon RDS instance, create a destination table for the loaded data.

```
CREATE TABLE customer_1 TABLESPACE users
  AS select 0 as id, owner, object_name, created
    from all_objects where 1=2;
```

The data is exported from the source database to a flat file with delimiters. This example uses SQL\*Plus. For your data, you will likely need to generate a script that does the export for all the objects in the database.

```
alter session set nls_date_format = 'YYYY/MM/DD HH24:MI:SS';
set linesize 800
HEADING OFF FEEDBACK OFF array 5000 pagesize 0
spool customer_0.out
SET MARKUP HTML PREFORMAT ON SET COLSEP ',' SELECT id,
  owner, object_name, created FROM customer_0;
spool off
```

Create a control file describing the data. Depending on the data, you may need to build a script that provides this functionality.

```
cat << EOF > sqlldr_1.ctl
LOAD DATA
INFILE customer_0.out
into table customer_1
APPEND
fields terminated by "," optionally enclosed by '"'
(id POSITION(01:10) INTEGER EXTERNAL,
owner POSITION(12:41) CHAR,
object_name POSITION(43:72) CHAR,
created POSITION(74:92) date "YYYY/MM/DD HH24:MI:SS")
```

Import the data using SQL\*Loader. Use the appropriate username and password for the target database.

```
sqlldr cust_dba@targetdb control=sqlldr_1.ctl BINDSIZE=10485760 READSIZE=10485760 ROWSS=1000
```

For more information, see [SQL\*Loader](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-sql-loader.html#GUID-8D037494-07FA-4226-B507-E1B2ED10C144 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-sql-loader.html#GUID-8D037494-07FA-4226-B507-E1B2ED10C144") in the _Oracle documentation_.

## PostgreSQL usage

You can use the two following options as a replacement for the Oracle SQL\*Loader utility:

- **PostgreSQL Import** using an export file similar to a control file.
- **Load from Amazon S3 File** using a table-formatted file on Amazon S3 and loading it into a PostgreSQL database.

`pg_restore` is a good option when it’s required to use a tool from another server or a client. The `LOAD DATA` command can be combined with meta-data tables and `EVENT` objects to schedule loads.

Another option to export and import data from PostgreSQL database is to use `COPY TO` and `COPY FROM` commands. Starting with PostgreSQL 12, the `COPY FROM` command, that you can use to load data into DB, has support for filtering incoming rows with the `WHERE` condition.

```
CREATE TABLE tst_copy(v TEXT);

COPY tst_copy FROM '/home/postgres/file.csv' WITH (FORMAT CSV) WHERE v LIKE '%apple%';
```

For more information, see [PostgreSQL pg_dump and pg_restore](chap-oracle-aurora-pg.hadr.md#chap-oracle-aurora-pg.hadr.datapump.pg "chap-oracle-aurora-pg.hadr.md#chap-oracle-aurora-pg.hadr.datapump.pg").
