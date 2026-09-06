

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_STREAM\_SCAN\_STATES
<a name="r_SYS_STREAM_SCAN_STATES"></a>

Records scan states for records loaded through streaming ingestion.

SYS\_STREAM\_SCAN\_STATES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SYS_STREAM_SCAN_STATES-table-rows"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| external\_schema\_name  | character(128)  | The external schema name. It is case sensitive. | 
| stream\_name  | character(255)  | The stream name. It is case sensitive. | 
| mv\_name | character(128)  | The name of the associated materialized view. Empty if none. It is case sensitive. | 
| transaction\_id | bigint  | The transaction ID. | 
| query\_id  | bigint  | The query ID.  | 
| record\_time | timestamp without time zone | The time when the data was logged. | 
| partition\_id | character(128)  | The partition or shard id. It is case sensitive. | 
| latest\_position | character(128)  | The position of the last record read in the batch. This corresponds with the sequence number in Kinesis or the offset in Amazon MSK. It is case sensitive. | 
| scanned\_rows | bigint | The number of records that were scanned in the batch. | 
| skipped\_rows | bigint | The number of records that were skipped in the batch. | 
| scanned\_bytes | bigint | The number of bytes that were scanned in the batch. | 
| stream\_record\_time\_min | timestamp without time zone | Kinesis or Amazon MSK arrival time for the earliest record in the batch. | 
| stream\_record\_time\_max | timestamp without time zone | Kinesis or Amazon MSK arrival time for the latest record in the batch. | 

The following query shows stream and topic data for specific queries.

```
select query_id,mv_name::varchar,external_schema_name::varchar,stream_name::varchar,sum(scanned_rows) total_records,
sum(scanned_bytes) total_bytes from sys_stream_scan_states where query in (5401180,8601939) group by 1,2,3,4;

  query_id  |    mv_name     | external_schema_name |   stream_name   | total_records |  total_bytes
------------+----------------+----------------------+-----------------+---------------+----------------
 5401180    | kinesistest    | kinesis              | kinesisstream   |    1493255696 | 3209006490704
 8601939    | msktest        | msk                  | mskstream       |      14677023 |   31056580668
(2 rows)
```