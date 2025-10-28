Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_INTEGRATION_TABLE_STATE_CHANGE

SYS_INTEGRATION_TABLE_STATE_CHANGE displays details about table state change logs for
integrations.

A superuser can see all rows in this table.

For more information, see [Working with Zero-ETL
integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md").

## Table

columns

| Column name                      | Data type      | Description                                                                                                                          |
| -------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------- | ---------- | --------- | -------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----------- | -------- | ------ | ----------------------------------- | --- | --------------------------------------------------------------- | ------ | ----------- | -------- | ------ | ----------------------------------- | --- | -------------------------------------------------------------- | ------ | ----------- | -------- | ------ | ----------------------------------- | --- | --------------------------------------------------------------- | ------ | ----------- | -------- | ------ | ----------------------------------- | --- | --------------------------------------------------------------- | ------ | ----------- | -------- | ------ | ----------------------------------- | --- | ------------------------------- |
| integration_id                   | character(128) | The identifier associated with the integration.                                                                                      |
| database_name                    | character(128) | The name of the Amazon Redshift database.                                                                                            |
| schema_name                      | character(128) | The name of the Amazon Redshift schema.                                                                                              |
| table_name                       | character(128) | The name of the table.                                                                                                               |
| new_state                        | character(128) | The state of the table. Possible values are `Synced`, `ResyncRequired`, `ResyncInitiated`, `Deleted`, `Failed`, and `ResyncDeleted`. |
| table_last_replicated_checkpoint | character(128) | The current synced log coordinates.                                                                                                  |
| state_change_reason              | character(256) | The reason for the last state transition.                                                                                            |
| record_time                      | timestamp      | The time (UTC) when this record was updated.                                                                                         | ## Sample queries The following SQL command displays the log of integrations. ``` `select \* from sys_integration_table_state_change;` `integration_id | database_name | schema_name | table_name | new_state | table_last_replicated_checkpoint | state_change_reason | record_time --------------------------------------+---------------+-------------+------------+-----------+-------------------------------------+---------------------+---------------------------- 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb | sbtest80t3s | sbtest79 | Synced | {"txn_seq":9834,"txn_id":126597515} |     | 2023-09-20 19:39:50.087868 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb | sbtest80t3s | sbtest56 | Synced | {"txn_seq":9834,"txn_id":126597515} |     | 2023-09-20 19:39:45.54005 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb | sbtest80t3s | sbtest50 | Synced | {"txn_seq":9834,"txn_id":126597515} |     | 2023-09-20 19:40:20.362504 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb | sbtest80t3s | sbtest18 | Synced | {"txn_seq":9834,"txn_id":126597515} |     | 2023-09-20 19:40:32.544084 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb | sbtest40t3s | sbtest23 | Synced | {"txn_seq":9834,"txn_id":126597515} |     | 2023-09-20 15:49:05.186209` ``` |
