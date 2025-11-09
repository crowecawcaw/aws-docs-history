Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_UNLOAD_HISTORY

Use SYS_UNLOAD_HISTORY to view details of UNLOAD commands. Each row represents a
UNLOAD command with accumulated statistics for some of the fields. It contains both
running and finished UNLOAD commands.

SYS_UNLOAD_HISTORY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name          | Data type | Description                                                                                                     |
| -------------------- | --------- | --------------------------------------------------------------------------------------------------------------- |
| user_id              | integer   | The identifier of the user who submitted the<br>unload.                                                         |
| query_id             | bigint    | The query identifier of the UNLOAD<br>command.                                                                  |
| transaction_id       | bigint    | The transaction identifier.                                                                                     |
| session_id           | integer   | The process identifier of the process running the<br>unload.                                                    |
| database_name        | text      | The name of the database the user was connected to<br>when the operation was issued.                            |
| status               | text      | The status of the UNLOAD command. Valid values<br>include: `running`, `completed`,<br>`aborted`, and `unknown`. |
| start_time           | timestamp | The time when the unload began.                                                                                 |
| end_time             | timestamp | The time when the unload completed.                                                                             |
| duration             | bigint    | The amount of time (microseconds) spent in the<br>UNLOAD command.                                               |
| file_format          | text      | The file format of the output files.                                                                            |
| compression_type     | text      | The compression type.                                                                                           |
| unloaded_location    | text      | The Amazon S3 location of unloaded files.                                                                       |
| unloaded_rows        | bigint    | The number of rows.                                                                                             |
| unloaded_files_count | bigint    | The file count of the output file.                                                                              |
| unloaded_files_size  | bigint    | The file size of the output file.                                                                               |
| error_message        | text      | The error message of the UNLOAD command.                                                                        |

## Sample queries

The following query shows the unloaded query details, including format, rows, and
file count of unload command.

```
SELECT query_id,
       file_format,
       start_time,
       duration,
       unloaded_rows,
       unloaded_files_count
FROM sys_unload_history
ORDER BY query_id,
file_format limit 100;
```

Sample output.

```
 query_id | file_format |         start_time         | duration | unloaded_rows | unloaded_files_count
----------+-------------+----------------------------+----------+---------------+----------------------
   527067 | Text        | 2022-02-09 05:18:35.844452 |  5932478 |            10 |                    1
```
