

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_UNLOAD\_HISTORY
<a name="SYS_UNLOAD_HISTORY"></a>

Use SYS\_UNLOAD\_HISTORY to view details of UNLOAD commands. Each row represents a UNLOAD command with accumulated statistics for some of the fields. It contains both running and finished UNLOAD commands.

SYS\_UNLOAD\_HISTORY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_UNLOAD_HISTORY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | The identifier of the user who submitted the unload. | 
| query\_id | bigint | The query identifier of the UNLOAD command. | 
| transaction\_id | bigint | The transaction identifier. | 
| session\_id | integer | The process identifier of the process running the unload. | 
| database\_name | text | The name of the database the user was connected to when the operation was issued. | 
| status | text | The status of the UNLOAD command. Valid values include: running, completed, aborted, and unknown. | 
| start\_time | timestamp | The time when the unload began. | 
| end\_time | timestamp | The time when the unload completed. | 
| duration | bigint | The amount of time (microseconds) spent in the UNLOAD command. | 
| file\_format | text | The file format of the output files. | 
| compression\_type | text | The compression type. | 
| unloaded\_location | text | The Amazon S3 location of unloaded files. | 
| unloaded\_rows | bigint  | The number of rows. | 
| unloaded\_files\_count | bigint | The file count of the output file. | 
| unloaded\_files\_size | bigint | The file size of the output file. | 
| error\_message | text | The error message of the UNLOAD command. | 

## Sample queries
<a name="SYS_UNLOAD_HISTORY-sample-queries"></a>

The following query shows the unloaded query details, including format, rows, and file count of unload command.

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