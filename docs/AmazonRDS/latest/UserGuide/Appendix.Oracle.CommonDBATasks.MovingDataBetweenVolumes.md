

# Moving data between storage volumes in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.MovingDataBetweenVolumes"></a>

You can move data files and database objects between your primary and additional storage volumes. Before you move data, consider the following points:
+ The source and target volumes must have sufficient free space.
+ Data movement operations consume I/O on both volumes.
+ Large data movements can impact database performance.
+ If you restore a snapshot, moving data between storage volumes might be slow if it is affected by EBS lazy loading.

**Topics**
+ [Moving data files between volumes in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.MovingDatafiles)
+ [Moving table data and indexes between volumes in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.MovingTableData)
+ [Managing LOB storage using additional volumes](#Appendix.Oracle.CommonDBATasks.ManagingLargeLOBStorage)

## Moving data files between volumes in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.MovingDatafiles"></a>

To move data files between storage volumes, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.move_datafile`. Note the following requirements:
+ You must use Oracle Enterprise Edition to run the `move_datafile` procedure.
+ You can't move tablespace `SYSTEM` and `RDSADMIN`.

The `move_datafile` procedure has the following parameters.



| Parameter name | Data type | Required | Description | 
| --- | --- | --- | --- | 
| `p_data_file_id` | number | Yes | The ID of the data file to be moved. | 
| `p_location` | varchar2 | Yes | The storage volume to which you want to move the data file. | 

The following example moves a tablespace from the default volume `rdsdbdata` to the additional volume `rdsdbdata2`.

```
SQL> SELECT tablespace_name,file_id,file_name FROM dba_data_files
 WHERE tablespace_name = 'MYNEWTABLESPACE';

TABLESPACE_NAME              FILE_ID FILE_NAME
------------------------- ---------- --------------------------------------------------------------------------------
MYNEWTABLESPACE                    6 /rdsdbdata/db/ORCL_A/datafile/o1_mf_mynewtab_n123abcd_.dbf

EXECUTE rdsadmin.rdsadmin_util.move_datafile( 6, 'rdsdbdata2');

PL/SQL procedure successfully completed.

SQL> SELECT tablespace_name,file_id,file_name FROM dba_data_files
  WHERE tablespace_name = 'MYNEWTABLESPACE';

TABLESPACE_NAME              FILE_ID FILE_NAME
------------------------- ---------- --------------------------------------------------------------------------------
MYNEWTABLESPACE                    6 /rdsdbdata2/db/ORCL_A/datafile/o1_mf_mynewtab_n356efgh_.dbf
```

## Moving table data and indexes between volumes in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.MovingTableData"></a>

You can optimize database storage by creating tablespaces on additional storage volumes. Then you can move objects such as tables, indexes, and partitions to these tablespaces using standard Oracle SQL. This approach is valuable for performance tuning when your database contains data with different access patterns. For example, you could store frequently accessed operational data on high-performance storage volumes while moving rarely accessed historical data to lower-cost storage volumes.

In the following example, you create a new tablespace on high-performance volume `rdsdbdata2`. Then you move a table to your additional storage volume while the table is online. You also move the index to the same volume. Moving tables and rebuilding indexes while online requires Oracle Enterprise Edition.

```
ALTER SESSION SET db_create_file_dest = '/rdsdbdata2/db';
CREATE TABLESPACE perf_tbs DATAFILE SIZE 10G;

ALTER TABLE employees
  MOVE TABLESPACE perf_tbs ONLINE;

ALTER INDEX employees_idx
  REBUILD ONLINE TABLESPACE perf_tbs;
```

In the following example, you create a tablespace on a low-cost volume. Then you move a table partition to your low-cost storage volume using an online operation.

```
ALTER SESSION SET db_create_file_dest = '/rdsdbdata3/db';
CREATE TABLESPACE hist_tbs DATAFILE SIZE 10G;

ALTER TABLE orders
  MOVE PARTITION orders_2022
  TABLESPACE hist_tbs ONLINE;
```

In the following example, you query active sessions long operations.

```
SELECT sid,opname,sofar,totalwork,time_remaining,elapsed_seconds 
  FROM v$session_longops 
  WHERE time_remaining > 0;
```

You can check your tablespaces usage with the following query.

```
SELECT tablespace_name, used_percent
  FROM dba_tablespace_usage_metrics
  ORDER BY used_percent DESC;
```

## Managing LOB storage using additional volumes
<a name="Appendix.Oracle.CommonDBATasks.ManagingLargeLOBStorage"></a>

Your database might contains tables with BLOB or CLOB objects that consume substantial storage but are infrequently accessed. To optimize storage, you can relocate these LOB segments to a tablespace on an additional storage volume.

In the following example, you create a tablespace for LOB data on a low-cost volume that is intended for low-access data. Then you create a table that stores data on this volume.

```
ALTER SESSION SET db_create_file_dest = '/rdsdbdata3/db';
CREATE TABLESPACE lob_data DATAFILE SIZE 5G AUTOEXTEND ON NEXT 1G;

CREATE TABLE documents (
    doc_id NUMBER PRIMARY KEY,
    doc_date DATE,
    doc_content CLOB
) TABLESPACE user_data
LOB(doc_content) STORE AS (TABLESPACE lob_data);
```