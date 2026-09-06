

# Oracle and MySQL temporary tables
<a name="chap-oracle-aurora-mysql.tables.temporary"></a>

Temporary tables are useful for storing intermediate results, handling large data sets, and improving query performance. The following sections will provide detailed instructions on migrating Oracle and MySQL temporary tables using AWS DMS, ensuring a smooth transition to AWS while preserving data and application behavior.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-3.png)  |  | MySQL doesn’t support `GLOBAL` temporary tables. MySQL can’t read from multiple sessions. MySQL drops tables after the session ends. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.temporary.oracle"></a>

In Oracle, you can create temporary tables for storing data that exists only for the duration of a session or transaction.

Use the `CREATE GLOBAL TEMPORARY TABLE` statement to create a temporary table. This type of table has a persistent DDL structure, but not persistent data. It doesn’t generate redo during DML. Two of the primary use-cases for temporary tables include:
+ Processing many rows as part of a batch operation while requiring staging tables to store intermediate results.
+ Storing data required only for the duration of a specific session. When the session ends, the session data is cleared.

When using temporary tables, the data is visible only to the session that inserts the data into the table.

Oracle 18c introduces private temporary tables which are temporary tables that are only available during session or transaction. After session or transaction ends they are automatically dropped.

### Oracle global temporary tables
<a name="chap-oracle-aurora-mysql.tables.temporary.oracle.global"></a>

Global temporary tables store data in the Oracle Temporary Tablespace.

DDL operations on a temporary table are permitted including `ALTER TABLE`, `DROP TABLE`, and `CREATE INDEX`.

Temporary tables can’t be partitioned, clustered, or created as index-organized tables. Also, they don’t support parallel `UPDATE`, `DELETE`, and `MERGE`.

Foreign key constraints can’t be created on temporary tables.

Processing DML operations on a temporary table doesn’t generate redo data. However, undo data for the rows and redo data for the undo data itself are generated.

Indexes can be created for a temporary table. They are treated as temporary indexes. Temporary tables also support triggers.

Temporary tables can’t be named after an existing table object and can’t be dropped while containing records, even from another session.

### Session-specific and transaction-specific temporary table syntax
<a name="chap-oracle-aurora-mysql.tables.temporary.oracle.specific"></a>

Use `ON COMMIT` to specifies whether the temporary table data persists for the duration of a transaction or a session.

Use `PRESERVE ROWS` when the session ends, all data is truncated but persists beyond the end of the transaction.

Use `DELETE ROWS` to truncate data after each commit. This is the default behavior.

### Oracle 12c temporary table enhancements
<a name="chap-oracle-aurora-mysql.tables.temporary.oracle.enhance"></a>

 **Global temporary table statistics** 

Prior to Oracle 12c, statistics on temporary tables were common to all sessions. Oracle 12c introduces session-specific statistics for temporary tables. Statistics can be configured using the `DBMS_STATS` preference `GLOBAL_TEMP_TABLE_STATS`, which can be set to `SHARED` or `SESSION`.

 **Global temporary table undo** 

Performing DML operations on a temporary table doesn’t generate Redo data, but does generate undo data that eventually, by itself, generates redo records. Oracle 12c provides an option to store the temporary undo data in the temporary tablespace itself. This feature is configured using the `temp_undo_enabled` parameter with the options `TRUE` or `FALSE`.

For more information, see [TEMP\_UNDO\_ENABLED](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TEMP_UNDO_ENABLED.html#GUID-E2A01A84-2D63-401F-B64E-C96B18C5DCA6) in the *Oracle documentation*.

### Examples
<a name="chap-oracle-aurora-mysql.tables.temporary.oracle.examples"></a>

Create an Oracle global temporary table with `ON COMMIT PRESERVE ROWS`.

```
CREATE GLOBAL TEMPORARY TABLE EMP_TEMP (
  EMP_ID NUMBER PRIMARY KEY,
  EMP_FULL_NAME VARCHAR2(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL)
  ON COMMIT PRESERVE ROWS;

CREATE INDEX IDX_EMP_TEMP_FN ON EMP_TEMP(EMP_FULL_NAME);

INSERT INTO EMP_TEMP VALUES(1, 'John Smith', '5000');

COMMIT;

SELECT * FROM SCT.EMP_TEMP;

EMP_ID EMP_FULL_NAME AVG_SALARY
1      John Smith    5000
```

Create an Oracle global temporary table with `ON COMMIT DELETE ROWS`.

```
CREATE GLOBAL TEMPORARY TABLE EMP_TEMP (
  EMP_ID NUMBER PRIMARY KEY,
  EMP_FULL_NAME VARCHAR2(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL)
  ON COMMIT DELETE ROWS;

INSERT INTO EMP_TEMP VALUES(1, 'John Smith', '5000');

COMMIT;

SELECT * FROM SCT.EMP_TEMP;
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TEMP_UNDO_ENABLED.html#GUID-E2A01A84-2D63-401F-B64E-C96B18C5DCA6) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.temporary.mysql"></a>

MySQL temporary tables share many similarities with Oracle global temporary tables. From a syntax perspective, MySQL temporary tables are referred to as temporary tables without global definition. The implementation is mostly identical.

In terms of differences, Oracle stores the temporary table structure (DDL) for repeated use — even after a database restart — but doesn’t store rows persistently. MySQL implements temporary tables differently: the table structure (DDL) isn’t stored in the database. When a session ends, the temporary table is dropped.

In MySQL, every session is required to create its own temporary tables. Each session can create its own private temporary tables, using identical table names.

In Oracle, the default behavior when the `ON COMMIT` clause is omitted is `ON COMMIT DELETE ROWS`. In MySQL, the default is `ON COMMIT PRESERVE ROWS` and you can’t change it.

**Note**  
In Amazon Relational Database Service (Amazon RDS) for MySQL version 8.0.13, the user-created temporary tables and internal temporary tables created by the optimizer are stored in session temporary tablespaces that are allocated to a session from a pool of temporary tablespaces. When a session disconnects its temporary tablespaces are truncated and released back to the pool. In previous releases temporary tables were created in the global temporary tablespace `ibtmp1` which did not return disk space to the operating system after temporary tables were dropped. The `innodb_temp_tablespaces_dir` variable defines the location where session temporary tablespaces are created. The default location is the `#innodb_temp` directory in the data directory. The `INNODB_SESSION_TEMP_TABLESPACES` table provides metadata about session temporary tablespaces. The global temporary tablespace `ibtmp1` now stores rollback segments for changes made to user-created temporary tables.

### Example
<a name="chap-oracle-aurora-mysql.tables.temporary.mysql.example"></a>

```
CREATE TEMPORARY TABLE EMP_TEMP (
  EMP_ID INT PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY INT NOT NULL1;
```

## Summary
<a name="chap-oracle-aurora-mysql.tables.temporary.summary"></a>


| Feature | Oracle |  Aurora MySQL | 
| --- | --- | --- | 
| Semantic | Global Temporary Table | Temporary Table | 
| Create table |  `CREATE GLOBAL TEMPORARY…​`  |  `CREATE TEMPORARY…​`  | 
| Accessible from multiple sessions | Yes | No | 
| Temp table DDL persist after session end or database restart user-managed data files | Yes | No (dropped at the end of the session) | 
| Create index support | Yes | Yes | 
| Foreign key support | Yes | No | 
|  `ON COMMIT` default |  `COMMIT DELETE ROWS`  |  `ON COMMIT PRESERVE ROWS`  | 
|  `ON COMMIT PRESERVE ROWS`  | Yes | Yes | 
|  `ON COMMIT DELETE ROWS`  | Yes | No | 
| Alter table support | Yes | Yes | 
| Gather statistics |  `dbms_stats.gather_table_stats`  |  `ANALYZE`  | 
| Oracle 12c `GLOBAL_TEMP_TABLE_STATS`  |  `dbms_stats.set_table_prefs`  |  `ANALYZE`  | 

For more information, see [CREATE TEMPORARY TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-temporary-table.html) in the *MySQL documentation*.