

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_EXTERNAL\_QUERY\_DETAIL
<a name="SYS_EXTERNAL_QUERY_DETAIL"></a>

Use SYS\_EXTERNAL\_QUERY\_DETAIL to view details for queries at a segment level. Each row represents a segment from a particular WLM query with details like the number of rows processed, number of bytes processed, and partition info of external tables in Amazon S3. Each row in this view will also have a corresponding entry in the SYS\_QUERY\_DETAIL view, except this view has more detail information related to external query processing. 

SYS\_EXTERNAL\_QUERY\_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_EXTERNAL_QUERY_DETAIL-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | The identifier of the user who submitted the query. | 
| query\_id | bigint | The query identifier of the external query. | 
| transaction\_id | bigint | The transaction identifier. | 
| child\_query\_sequence | integer | The sequence of the rewritten user query. Starts with 0, similar to segment\_id. | 
| segment\_id | integer | The segment identifier of the query segment. | 
| source\_type | character(32) | The data source type of the query, it could be S3 for Redshift Spectrum, PG for federated query. | 
| start\_time | timestamp | The time when the query began.  | 
| end\_time | timestamp | The time when the query completed. | 
| duration | bigint | The amount of time (microseconds) spent on the query. | 
| total\_partitions | integer | The number of partitions an Amazon S3 query required. | 
| qualified\_partitions | integer | The number of partitions an Amazon S3 query scanned. | 
| scanned\_files | bigint | The number of Amazon S3 files scanned. | 
| returned\_rows | bigint | The number of scanned rows for an Amazon S3 query, or the number of returned rows for a federated query. | 
| returned\_bytes | bigint | The number of scanned bytes for an Amazon S3 query, or the number of returned bytes for a federated query. | 
| file\_format | text | The file format of Amazon S3 files. | 
| file\_location | text | The Amazon S3 location of external table. | 
| external\_query\_text | text | The segment level query text for a federated query. | 
| warning\_message | character(4000) | The warning message displayed when the query runs. | 
| table\_name | character(136) | The table name of the step that is being operated. | 
| is\_recursive | character(1) | Indicates whether there is recursive scan for subfolders. | 
| is\_nested | character(1) | Indicates whether the nested column data type is accessed. | 
| s3list\_time | bigint | The duration of file listing in milliseconds. | 
| get\_partition\_time | long | Time spent to list and qualify partitions for a given external object from the AWS Glue Data Catalog and Apache Hive. | 
| query\_uuid | character(36) | A globally unique identifier (UUID) of the query. | 

## Sample queries
<a name="SYS_EXTERNAL_QUERY_DETAIL-sample-queries"></a>

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