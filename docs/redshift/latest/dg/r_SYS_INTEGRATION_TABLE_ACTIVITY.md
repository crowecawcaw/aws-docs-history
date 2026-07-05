Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_INTEGRATION\_TABLE\_ACTIVITY

SYS\_INTEGRATION\_TABLE\_ACTIVITY displays details of insert, delete, and update activity of zero-ETL integrations.
There is one row added for each completed ingestion.

A superuser can see all rows in this table.

For more information, see [zero-ETL integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md").

## Table columns

| Column name      | Data type      | Description                                     |
| ---------------- | -------------- | ----------------------------------------------- |
| integration\_id  | character(128) | The identifier associated with the integration. |
| checkpoint\_name | character(128) | The name of the checkpoint.                     |
| target\_database | character(128) | The name of the Amazon Redshift database.       |
| schema\_name     | character(128) | The name of the Amazon Redshift schema.         |
| table\_name      | character(128) | The name of the table.                          |
| table\_id        | integer        | The identifier of the table.                    |
| record\_time     | timestamp      | The time (UTC) when this change completed.      |
| transaction\_id  | bigint         | The transaction identifier.                     |
| inserted\_rows   | bigint         | The number of rows inserted by the ingestion.   |
| deleted\_rows    | bigint         | The number of rows deleted by the ingestion.    |
| updated\_rows    | bigint         | The number of rows updated by the ingestion.    |
| bytes\_ingested  | bigint         | The number of bytes ingested.                   |

## Sample queries

The following SQL command displays activity of the integration.

```
`select * from sys_integration_table_activity;`
`integration_id | checkpoint_name | target_database | schema_name | table_name | table_id | record_time | transaction_id | inserted_rows | deleted_rows | updated_rows | bytes_ingested
--------------------------------------+-----------------+-----------------+-------------+-------------------+--------------+----------------------------+-----------------+----------------+--------------+--------------+---------------
 4798e675-8f9f-4686-b05f-92c538e19629 | | sample_test2 | sample | SampleTestChannel | 111276 | 2023-05-12 12:40:30.656625 | 7736 | 2 | 0 | 0 | 125`
```
