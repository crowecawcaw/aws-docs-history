# Importing transported tablespaces to your DB instance

Use the procedure `rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces` to
restore tablespaces that you have previously exported from a source DB instance. In the transport
phase, you back up your read-only tablespaces, export Data Pump metadata, transfer these
files to your target DB instance, and then import the tablespaces. For more information, see [Phase 4: Transport the tablespaces](oracle-migrating-tts.md#oracle-migrating-tts.final-br-phase "oracle-migrating-tts.md#oracle-migrating-tts.final-br-phase").

## Syntax

```
FUNCTION import_xtts_tablespaces(
    p_tablespace_list IN CLOB,
    p_directory_name  IN VARCHAR2,
    p_platform_id     IN NUMBER DEFAULT 13,
    p_parallel        IN INTEGER DEFAULT 0) RETURN VARCHAR2;
```

## Parameters

| Parameter name      | Data type  | Default | Required | Description                                                                                                                                                                                                             |
| ------------------- | ---------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_tablespace_list` | `CLOB`     | —       | Yes      | The list of tablespaces to import.                                                                                                                                                                                      |
| `p_directory_name`  | `VARCHAR2` | —       | Yes      | The directory that contains the tablespace backups.                                                                                                                                                                     |
| `p_platform_id`     | `NUMBER`   | `13`    | No       | Provide a platform ID that matches the one specified during the<br>backup phase. To find a list of platforms, query<br>`V$TRANSPORTABLE_PLATFORM`. The default platform is<br>Linux x86 64-bit, which is little endian. |
| `p_parallel`        | `INTEGER`  | `0`     | No       | The degree of parallelism. By default, parallelism is<br>disabled.                                                                                                                                                      |

## Examples

The following example imports the tablespaces `TBS1`,
`TBS2`, and `TBS3` from the directory
`DATA_PUMP_DIR`. The source platform is AIX-Based Systems
(64-bit), which has the platform ID of `6`. You can find the platform IDs by
querying `V$TRANSPORTABLE_PLATFORM`.

```
VAR task_id CLOB

BEGIN
  :task_id:=rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces(
        '`TBS1,TBS2,TBS3`',
        '`DATA_PUMP_DIR`',
        p_platform_id => 6);
END;
/

PRINT task_id
```
