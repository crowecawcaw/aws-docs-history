Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_STREAM_SCAN_ERRORS

Records errors for records loaded via streaming ingestion.

SYS_STREAM_SCAN_ERRORS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name           | Data type                   | Description                                                                                                                               |
| --------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| external_schema_name  | character(128)              | The name of the Kinesis stream or Amazon MSK topic's<br>schema. It is case sensitive.                                                     |
| stream_name           | character(255)              | The name of the stream or topic. It is case<br>sensitive.                                                                                 |
| mv_name               | character(128)              | The name of the associated materialized view.<br>Empty if none. It is case sensitive.                                                     |
| transaction_id        | bigint                      | The transaction ID.                                                                                                                       |
| query_id              | bigint                      | The query ID.                                                                                                                             |
| stream_timestamp_type | character(1)                | The type of the stream timestamp. It is case<br>sensitive.                                                                                |
| stream_timestamp      | timestamp without time zone | The time when the record arrived.                                                                                                         |
| record_time           | timestamp without time zone | The time when the error message was<br>logged.                                                                                            |
| partition_id          | character(128)              | The partition/shard id. It is case<br>sensitive.                                                                                          |
| position              | character(128)              | The position of the record. This corresponds with<br>the sequence number in Kinesis or the offset in Amazon MSK. It is case<br>sensitive. |
| error_code            | integer                     | The error code.                                                                                                                           |
| error_reason          | character(128)              | The error reason. It is case sensitive.                                                                                                   |
