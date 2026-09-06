

# Resizing tablespaces, data files, and tempfiles in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.ResizeTempSpaceReadReplica"></a>

By default, Oracle tablespaces are created with auto-extend turned on and no maximum size. Because of these default settings, tablespaces can sometimes grow too large. We recommend that you specify an appropriate maximum size on permanent and temporary tablespaces, and that you carefully monitor space usage.

## Resizing permanent tablespaces
<a name="resizing-perm-tbs"></a>

To resize a permanent tablespace in an RDS for Oracle DB instance, use any of the following Amazon RDS procedures:
+ `rdsadmin.rdsadmin_util.resize_datafile`
+ `rdsadmin.rdsadmin_util.autoextend_datafile`

The `resize_datafile` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_data_file_id` | number | — | Yes | The identifier of the data file to resize. | 
| `p_size` | varchar2 | — | Yes | The size of the data file. Specify the size in bytes (the default), kilobytes (K), megabytes (M), or gigabytes (G).  | 

The `autoextend_datafile` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_data_file_id` | number | — | Yes | The identifier of the data file to resize. | 
| `p_autoextend_state` | varchar2 | — | Yes | The state of the autoextension feature. Specify `ON` to extend the data file automatically and `OFF` to turn off autoextension.  | 
| `p_next` | varchar2 | — | No | The size of the next data file increment. Specify the size in bytes (the default), kilobytes (K), megabytes (M), or gigabytes (G). | 
| `p_maxsize` | varchar2 | — | No | The maximum disk space allowed for automatic extension. Specify the size in bytes (the default), kilobytes (K), megabytes (M), or gigabytes (G). You can specify `UNLIMITED` to remove the file size limit. | 

The following example resizes data file 4 to 500 MB.

```
EXEC rdsadmin.rdsadmin_util.resize_datafile(4,'500M');
```

The following example turns off autoextension for data file 4. It also turns on autoextension for data file 5, with an increment of 128 MB and no maximum size.

```
EXEC rdsadmin.rdsadmin_util.autoextend_datafile(4,'OFF');
EXEC rdsadmin.rdsadmin_util.autoextend_datafile(5,'ON','128M','UNLIMITED');
```

## Resizing temporary tablespaces
<a name="resizing-temp-tbs"></a>

To resize a temporary tablespaces in an RDS for Oracle DB instance, including a read replica, use any of the following Amazon RDS procedures:
+ `rdsadmin.rdsadmin_util.resize_temp_tablespace`
+ `rdsadmin.rdsadmin_util.resize_tempfile`
+ `rdsadmin.rdsadmin_util.autoextend_tempfile`

The `resize_temp_tablespace` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_temp_tablespace_name` | varchar2 | — | Yes | The name of the temporary tablespace to resize. | 
| `p_size` | varchar2 | — | Yes | The size of the tablespace. Specify the size in bytes (the default), kilobytes (K), megabytes (M), or gigabytes (G).  | 

The `resize_tempfile` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_temp_file_id` | number | — | Yes | The identifier of the temp file to resize. | 
| `p_size` | varchar2 | — | Yes | The size of the temp file. Specify the size in bytes (the default), kilobytes (K), megabytes (M), or gigabytes (G).  | 

The `autoextend_tempfile` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_temp_file_id` | number | — | Yes | The identifier of the temp file to resize. | 
| `p_autoextend_state` | varchar2 | — | Yes | The state of the autoextension feature. Specify `ON` to extend the temp file automatically and `OFF` to turn off autoextension.  | 
| `p_next` | varchar2 | — | No | The size of the next temp file increment. Specify the size in bytes (the default), kilobytes (K), megabytes (M), or gigabytes (G). | 
| `p_maxsize` | varchar2 | — | No | The maximum disk space allowed for automatic extension. Specify the size in bytes (the default), kilobytes (K), megabytes (M), or gigabytes (G). You can specify `UNLIMITED` to remove the file size limit. | 

The following examples resize a temporary tablespace named `TEMP` to the size of 4 GB.

```
EXEC rdsadmin.rdsadmin_util.resize_temp_tablespace('TEMP','4G');
```

```
EXEC rdsadmin.rdsadmin_util.resize_temp_tablespace('TEMP','4294967296');
```

The following example resizes a temporary tablespace based on the temp file with the file identifier `1` to the size of 2 MB.

```
EXEC rdsadmin.rdsadmin_util.resize_tempfile(1,'2M');
```

The following example turns off autoextension for temp file 1. It also sets the maximum autoextension size of temp file 2 to 10 GB, with an increment of 100 MB.

```
EXEC rdsadmin.rdsadmin_util.autoextend_tempfile(1,'OFF');
EXEC rdsadmin.rdsadmin_util.autoextend_tempfile(2,'ON','100M','10G');
```

For more information about read replicas for Oracle DB instances see [Working with read replicas for Amazon RDS for Oracle](oracle-read-replicas.md).