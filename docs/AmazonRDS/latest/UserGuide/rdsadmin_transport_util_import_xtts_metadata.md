# Importing transportable

tablespace metadata into your DB instance

Use the procedure `rdsadmin.rdsadmin_transport_util.import_xtts_metadata` to
import transportable tablespace metadata into your RDS for Oracle DB instance. During the operation, the
status of the metadata import is shown in the table
`rdsadmin.rds_xtts_operation_info`. For more information, see [Step 5: Import
tablespace metadata on your target DB instance](oracle-migrating-tts.md#oracle-migrating-tts.transport.import-dmp "oracle-migrating-tts.md#oracle-migrating-tts.transport.import-dmp").

## Syntax

```
PROCEDURE import_xtts_metadata(
    p_datapump_metadata_file IN SYS.DBA_DATA_FILES.FILE_NAME%TYPE,
    p_directory_name         IN VARCHAR2,
    p_exclude_stats          IN BOOLEAN DEFAULT FALSE,
    p_remap_tablespace_list  IN CLOB DEFAULT NULL,
    p_remap_user_list        IN CLOB DEFAULT NULL);
```

## Parameters

| Parameter name             | Data type                           | Default | Required | Description                                                                                                                                                                 |
| -------------------------- | ----------------------------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_datapump_metadata_file` | `SYS.DBA_DATA_FILES.FILE_NAME%TYPE` | —       | Yes      | The name of the Oracle Data Pump file that contains the metadata<br>for your transportable tablespaces.                                                                     |
| `p_directory_name`         | `VARCHAR2`                          | —       | Yes      | The directory that contains the Data Pump file.                                                                                                                             |
| `p_exclude_stats`          | `BOOLEAN`                           | `FALSE` | No       | Flag that indicates whether to exclude statistics.                                                                                                                          |
| `p_remap_tablespace_list`  | `CLOB`                              | NULL    | No       | A list of tablespaces to be remapped during the metadata import.<br>Use the format<br>``from_tbs`:`to_tbs``.<br>For example, specify `users:user_data`.                     |
| `p_remap_user_list`        | `CLOB`                              | NULL    | No       | A list of user schemas to be remapped during the metadata import.<br>Use the format<br>``from_schema_name`:`to_schema_name``.<br>For example, specify `hr:human_resources`. |

## Examples

The example imports the tablespace metadata from the file
`xttdump.dmp`, which is located in directory
`DATA_PUMP_DIR`.

```
BEGIN
  rdsadmin.rdsadmin_transport_util.import_xtts_metadata('`xttdump.dmp`','`DATA_PUMP_DIR`');
END;
/
```
