

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_STREAM\_SCAN\_ERRORS
<a name="r_SYS_STREAM_SCAN_ERRORS"></a>

Records errors for records loaded through streaming ingestion.

SYS\_STREAM\_SCAN\_ERRORS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SYS_STREAM_SCAN_ERRORS-table-rows"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| external\_schema\_name | character(128)  | The name of the Kinesis stream or Amazon MSK topic's schema. It is case sensitive. | 
| stream\_name | character(255)  | The name of the stream or topic. It is case sensitive. | 
| mv\_name | character(128)  | The name of the associated materialized view. Empty if none. It is case sensitive. | 
| transaction\_id  | bigint  | The transaction ID.  | 
| query\_id  | bigint  | The query ID.  | 
| stream\_timestamp\_type | character(1) | The type of the stream timestamp. It is case sensitive. | 
| stream\_timestamp | timestamp without time zone | The time when the record arrived. | 
| record\_time | timestamp without time zone | The time when the error message was logged. | 
| partition\_id | character(128)  | The partition/shard id. It is case sensitive. | 
| position | character(128)  | The position of the record. This corresponds with the sequence number in Kinesis or the offset in Amazon MSK. It is case sensitive. | 
| error\_code | integer  | The error code. | 
| error\_reason | character(128)  | The error reason. It is case sensitive. | 