

# Oracle DBMS\_DATAPUMP and MySQL integration with Amazon S3
<a name="chap-oracle-aurora-mysql.sql.datapump"></a>

With AWS DMS, you can migrate data from Oracle databases to Amazon S3 using Oracle `DBMS_DATAPUMP`, and load data from Amazon S3 into MySQL-compatible databases. Oracle `DBMS_DATAPUMP` provides a way to transfer data objects between Oracle databases or export them to an operating system file. MySQL integration with Amazon S3 lets you use an Amazon S3 bucket as a data source or destination for loading and unloading data.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-1.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  | N/A | No equivalent tool | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.datapump.oracle"></a>

The `DBMS_DATAPUMP` package provides Oracle Data Pump functionality that can be run within the database.

The `DBMS_DATAPUMP` package subprograms are:
+  `ADD_FILE` — Adds a relevant file to the dump file set.
+  `ATTACH` — Connects the DATAPUMP job.
+  `DATA_FILTER` — Filters rows.
+  `DETACH` — Disconnects from a DATAPUMP operation.
+  `GET_DUMPFILE_INFO` — Retrieves information about a specified dump file.
+  `GET_STATUS` — Retrieves status of the running DATAPUMP operation.
+  `LOG_ENTRY` — Writes a message into the log file.
+  `METADATA_FILTER` — Filters the items to be include in the operation.
+  `METADATA_REMAP` — Remaps the object to new names.
+  `METADATA_TRANSFORM` — Specifies transformations to be applied to objects.
+  `OPEN` — Declares a new job.
+  `SET_PARALLEL` — Set the parallelism of the job.
+  `SET_PARAMETER` — Specifies job processing options.
+  `START_JOB` — Runs a job.
+  `STOP_JOB` — Terminates a job.
+  `WAIT_FOR_JOB` — Runs a job until it either completes normally or stops.

### Examples
<a name="chap-oracle-aurora-mysql.sql.datapump.oracle.examples"></a>

The following example shows how to export the `HR` schema. It assumes all directories have already been created and the user has all required privileges.

```
DECLARE
loopidx NUMBER;
job_handle NUMBER;
percent_done NUMBER;
job_state VARCHAR2(30);
err ku$_LogEntry;
job_status ku$_JobStatus;
job_desc ku$_JobDesc;
obj_stat ku$_Status;
BEGIN

job_handle := DBMS_DATAPUMP.OPEN('EXPORT','SCHEMA',NULL,'EXP_SAMP','LATEST');

DBMS_DATAPUMP.ADD_FILE(job_handle,'hr.dmp','DMPDIR');

DBMS_DATAPUMP.METADATA_FILTER(job_handle,'SCHEMA_EXPR','IN (''HR'')');

DBMS_DATAPUMP.START_JOB(job_handle);

percent_done := 0;
job_state := 'UNDEFINED';
while (job_state != 'COMPLETED') and (job_state != 'STOPPED') loop
dbms_datapump.get_status(job_handle,
dbms_datapump.ku$_status_job_error +
dbms_datapump.ku$_status_job_status +
dbms_datapump.ku$_status_wip,-1,job_state,obj_stat);
job_status := obj_stat.job_status;

/* HERE YOU CAN PRINT THE STATUS */

if job_status.percent_done != percent_done then
  percent_done := job_status.percent_done;
end if;

if (bitand(obj_stat.mask,dbms_datapump.ku$_status_wip) != 0) then
  err := obj_stat.wip;
else
  if (bitand(obj_stat.mask,dbms_datapump.ku$_status_job_error) != 0)
  then
    err := obj_stat.error;
    else
    err := null;
  end if;
end if;

if err is not null then
  loopidx := err.FIRST;
  while loopidx is not null loop
    loopidx := err.NEXT(loopidx);
  end loop;
end if;
end loop;

dbms_datapump.detach(job_handle);
END;
/
```

For more information, see [Overview of Oracle Data Pump](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-overview.html#GUID-17FAE261-0972-4220-A2E4-44D479F519D4) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.datapump.mysql"></a>

There is no feature in MySQL fully equivalent to the Oracle `DBMS_DATAPUMP` package, but there are tools and features that achieve the same functionality.

To export data from the database to the file system, use the `SELECT INTO OUTFILE S3` command. To import data from the filesystem, use the `LOAD DATA FROM S3` command.

To achieve the most functionality, this feature can be mixed with metadata tables and events to handle the operations.

For more information, see [Oracle External Tables and MySQL Integration with Amazon S3](chap-oracle-aurora-mysql.special.external.md).

## Summary
<a name="chap-oracle-aurora-mysql.sql.datapump.summary"></a>


| Feature | Oracle DBMS\_DATAPUMP | Aurora integration with S3 | 
| --- | --- | --- | 
| Add a relevant file to the dump file set |  `ADD_FILE`  | Use metadata table | 
| Connect the `DATAPUMP` job |  `ATTACH`  | Query session status | 
| Filter rows to be handled |  `DATA_FILTER`  | Use `WHERE` clause in your `SELECT`  | 
| Disconnect from `DATAPUMP` operation |  `DETACH`  | Not required | 
| Retrieve information about a specified dump file |  `GET_DUMPFILE_INFO`  | Use metadata table | 
| Retrieve the status of the running `DATAPUMP` operation |  `GET_STATUS`  | Query session status | 
| Write a message into the log file |  `LOG_ENTRY`  | Write to metadata tables | 
| Filter the items included in the operation |  `METADATA_FILTER`  | Export the objects | 
| Remap the object to new names |  `METADATA_REMAP`  |  `LOAD DATA INTO` different table name | 
| Specified transformations to be applied to objects |  `METADATA_TRANSFORM`  | Not required | 
| Declare a new job |  `OPEN`  | Use `LOAD DATA` or `SAVE OUTFILE`  | 
| Set the parallelism of the job |  `SET_PARALLEL`  | Use parallel in your `SELECT`  | 
| Specify job-processing options |  `SET_PARAMETER`  | Not required | 
| Run a job |  `START_JOB`  | Use `LOAD DATA` or `SAVE OUTFILE`  | 
| Terminate a job |  `STOP_JOB`  | Kill session | 
| Run a job until it either completes normally or stops |  `WAIT_FOR_JOB`  | Use `LOAD DATA` or `SAVE OUTFILE`  | 