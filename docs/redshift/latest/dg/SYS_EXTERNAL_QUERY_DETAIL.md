Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_EXTERNAL_QUERY_DETAIL

Use SYS_EXTERNAL_QUERY_DETAIL to view details for queries at a segment level. Each row
represents a segment from a particular WLM query with details like the number of rows
processed, number of bytes processed, and partition info of external tables in Amazon S3.
Each row in this view will also have a corresponding entry in the SYS_QUERY_DETAIL view,
except this view has more detail information related to external query processing.

SYS_EXTERNAL_QUERY_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name          | Data type       | Description                                                                                                              |
| -------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------ |
| user_id              | integer         | The identifier of the user who submitted the<br>query.                                                                   |
| query_id             | bigint          | The query identifier of the external<br>query.                                                                           |
| transaction_id       | bigint          | The transaction identifier.                                                                                              |
| child_query_sequence | integer         | The sequence of the rewritten user query. Starts<br>with 0, similar to segment_id.                                       |
| segment_id           | integer         | The segment identifier of the query<br>segment.                                                                          |
| source_type          | character(32)   | The data source type of the query, it could be<br>`S3` for Redshift Spectrum, `PG` for federated<br>query.               |
| start_time           | timestamp       | The time when the query began.                                                                                           |
| end_time             | timestamp       | The time when the query completed.                                                                                       |
| duration             | bigint          | The amount of time (microseconds) spent on the<br>query.                                                                 |
| total_partitions     | integer         | The number of partitions an Amazon S3 query<br>required.                                                                 |
| qualified_partitions | integer         | The number of partitions an Amazon S3 query<br>scanned.                                                                  |
| scanned_files        | bigint          | The number of Amazon S3 files scanned.                                                                                   |
| returned_rows        | bigint          | The number of scanned rows for an Amazon S3 query, or<br>the number of returned rows for a federated query.              |
| returned_bytes       | bigint          | The number of scanned bytes for an Amazon S3 query, or<br>the number of returned bytes for a federated query.            |
| file_format          | text            | The file format of Amazon S3 files.                                                                                      |
| file_location        | text            | The Amazon S3 location of external table.                                                                                |
| external_query_text  | text            | The segment level query text for a federated<br>query.                                                                   |
| warning_message      | character(4000) | The warning message displayed when the query<br>runs.                                                                    |
| table_name           | character(136)  | The table name of the step that is being<br>operated.                                                                    |
| is_recursive         | character(1)    | Indicates whether there is recursive scan for<br>subfolders.                                                             |
| is_nested            | character(1)    | Indicates whether the nested column data type is<br>accessed.                                                            |
| s3list_time          | bigint          | The duration of file listing in<br>milliseconds.                                                                         |
| get_partition_time   | long            | Time spent to list and qualify partitions for a<br>given external object from the AWS Glue Data Catalog and Apache Hive. |

## Sample queries

The following query shows the external query details.

```
SELECT query_id,
       segment_id,
       start_time,
       end_time,
       total_partitions,
       qualified_partitions,
       scanned_files,
       returned_rows,
       returned_bytes,
       trim(external_query_text) query_text,
       trim(file_location) file_location
FROM sys_external_query_detail
ORDER BY query_id, start_time DESC
LIMIT 2;
```

Sample output.

```
 query_id | segment_id |         start_time         |          end_time          | total_partitions | qualified_partitions | scanned_files | returned_rows | returned_bytes | query_text | file_location
----------+------------+----------------------------+----------------------------+------------------+----------------------+---------------+---------------+----------------+------------+---------------
   763251 |          0 | 2022-02-15 22:32:23.312448 | 2022-02-15 22:32:24.036023 |                3 |                    3 |             3 |         38203 |        2683414 |            |
   763254 |          0 | 2022-02-15 22:32:40.17103  | 2022-02-15 22:32:40.839313 |                3 |                    3 |             3 |         38203 |        2683414 |            |
```
