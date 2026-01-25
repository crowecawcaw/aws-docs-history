# Transferring files between RDS for Oracle

and an Amazon EFS file system

To transfer files between an RDS for Oracle instance and an Amazon EFS file system, create at least
one Oracle directory and configure EFS file system permissions to control DB instance
access.

###### Topics

- [Creating an Oracle
  directory](#oracle-efs-integration.transferring.od "#oracle-efs-integration.transferring.od")
- [Transferring data to and
  from an EFS file system: examples](#oracle-efs-integration.transferring.upload "#oracle-efs-integration.transferring.upload")

## Creating an Oracle

directory

To create an Oracle directory, use the procedure
`rdsadmin.rdsadmin_util.create_directory_efs`. The procedure has the
following parameters.

| Parameter name     | Data type | Default | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | --------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_directory_name` | VARCHAR2  | –       | Yes      | The name of the Oracle directory.                                                                                                                                                                                                                                                                                                                                                                              |
| `p_path_on_efs`    | VARCHAR2  | –       | Yes      | The path on the EFS file system. The prefix of the path name uses<br>the pattern `/rdsefs-`fsid`/`,<br>where `fsid` is a placeholder for your EFS<br>file system ID.<br>For example, if your EFS file system is named<br>`fs-1234567890abcdef0`, and you create a subdirectory<br>on this file system named `mydir`, you could specify the<br>following value:<br>`<br>/rdsefs-fs-1234567890abcdef0/mydir<br>` |

Assume that you create a subdirectory named `/datapump1` on the EFS file
system `fs-1234567890abcdef0`. The following example creates an Oracle
directory `DATA_PUMP_DIR_EFS` that points to the `/datapump1`
directory on the EFS file system. The file system path value for the
`p_path_on_efs` parameter is prefixed with the string
`/rdsefs-`.

```
BEGIN
  rdsadmin.rdsadmin_util.create_directory_efs(
    p_directory_name => 'DATA_PUMP_DIR_EFS',
    p_path_on_efs    => '/rdsefs-`fs-1234567890abcdef0`/`datapump1`');
END;
/
```

## Transferring data to and

from an EFS file system: examples

The following example uses Oracle Data Pump to export the table named
`MY_TABLE` to file `datapump.dmp`. This file resides on an EFS
file system.

```
DECLARE
  v_hdnl NUMBER;
BEGIN
  v_hdnl := DBMS_DATAPUMP.OPEN(operation => 'EXPORT', job_mode => 'TABLE', job_name=>null);
  DBMS_DATAPUMP.ADD_FILE(
    handle    => v_hdnl,
    filename  => 'datapump.dmp',
    directory => 'DATA_PUMP_DIR_EFS',
    filetype  => dbms_datapump.ku$_file_type_dump_file);
  DBMS_DATAPUMP.ADD_FILE(
    handle    => v_hdnl,
    filename  => 'datapump-exp.log',
    directory => 'DATA_PUMP_DIR_EFS',
    filetype  => dbms_datapump.ku$_file_type_log_file);
  DBMS_DATAPUMP.METADATA_FILTER(v_hdnl,'NAME_EXPR','IN (''MY_TABLE'')');
  DBMS_DATAPUMP.START_JOB(v_hdnl);
END;
/
```

The following example uses Oracle Data Pump to import the table named
`MY_TABLE` from file `datapump.dmp`. This file resides on an
EFS file system.

```
DECLARE
  v_hdnl NUMBER;
BEGIN
  v_hdnl := DBMS_DATAPUMP.OPEN(
    operation => 'IMPORT',
    job_mode  => 'TABLE',
    job_name  => null);
  DBMS_DATAPUMP.ADD_FILE(
    handle    => v_hdnl,
    filename  => 'datapump.dmp',
    directory => 'DATA_PUMP_DIR_EFS',
    filetype  => dbms_datapump.ku$_file_type_dump_file );
  DBMS_DATAPUMP.ADD_FILE(
    handle    => v_hdnl,
    filename  => 'datapump-imp.log',
    directory => 'DATA_PUMP_DIR_EFS',
    filetype  => dbms_datapump.ku$_file_type_log_file);
  DBMS_DATAPUMP.METADATA_FILTER(v_hdnl,'NAME_EXPR','IN (''MY_TABLE'')');
  DBMS_DATAPUMP.START_JOB(v_hdnl);
END;
/
```

For more information, see [Importing data into Oracle on Amazon RDS](Oracle.Procedural.md "Oracle.Procedural.md").
