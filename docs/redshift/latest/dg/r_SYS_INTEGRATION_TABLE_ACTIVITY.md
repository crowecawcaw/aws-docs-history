Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_INTEGRATION_TABLE_ACTIVITY

SYS_INTEGRATION_TABLE_ACTIVITY displays details of insert, delete, and update activity of zero-ETL integrations.
There is one row added for each completed ingestion.

A superuser can see all rows in this table.

For more information, see [zero-ETL integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md").

## Table

columns

| Column name     | Data type      | Description                                     |
| --------------- | -------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | --------------- | ----------- | ---------- | -------- | ----------- | -------------- | ------------- | ------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------ | ------ | ----------------- | ------ | -------------------------- | ---- | --- | --- | --- | -------- |
| integration_id  | character(128) | The identifier associated with the integration. |
| checkpoint_name | character(128) | The name of the checkpoint.                     |
| target_database | character(128) | The name of the Amazon Redshift database.       |
| schema_name     | character(128) | The name of the Amazon Redshift schema.         |
| table_name      | character(128) | The name of the table.                          |
| table_id        | integer        | The identifier of the table.                    |
| record_time     | timestamp      | The time (UTC) when this change completed.      |
| transaction_id  | bigint         | The transaction identifier.                     |
| inserted_rows   | bigint         | The number of rows inserted by the ingestion.   |
| deleted_rows    | bigint         | The number of rows deleted by the ingestion.    |
| updated_rows    | bigint         | The number of rows updated by the ingestion.    |
| bytes_ingested  | bigint         | The number of bytes ingested.                   | ## Sample queries The following SQL command displays activity of the integration. ``` `select \* from sys_integration_table_activity;` `integration_id | checkpoint_name | target_database | schema_name | table_name | table_id | record_time | transaction_id | inserted_rows | deleted_rows | updated_rows | bytes_ingested --------------------------------------+-----------------+-----------------+-------------+-------------------+--------------+----------------------------+-----------------+----------------+--------------+--------------+--------------- 4798e675-8f9f-4686-b05f-92c538e19629 |     | sample_test2 | sample | SampleTestChannel | 111276 | 2023-05-12 12:40:30.656625 | 7736 | 2   | 0   | 0   | 125` ``` |
