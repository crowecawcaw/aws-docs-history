Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_INTEGRATION

SVV_INTEGRATION displays details about the configuration of integrations.

SVV_INTEGRATION is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about zero-ETL integrations, see [Zero-ETL integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md").

## Table columns

| Column name                | Data type      | Description                                                                                                                                    |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| integration_id             | character(128) | The identifier associated with the integration.                                                                                                |
| target_database            | character(128) | The database in Amazon Redshift that receives the integration data.                                                                            |
| source                     | character(128) | The source data for the integration. Possible types include `MySQL`, `PostgreSQL`, and `S3_EVENT_NOTIFICATIONS`.                               |
| state                      | character(128) | The state of the integration. Possible values include `PendingDbConnectState`, `SchemaDiscoveryState`, `CdcRefreshState`,<br>and `ErrorState`. |
| current_lag                | bigint         | The current lag time (milliseconds) between the source and destination of the integration.                                                     |
| last_replicated_checkpoint | character(128) | The last replicated checkpoint.                                                                                                                |
| total_tables_replicated    | integer        | The number of total tables currently in the replicated state.                                                                                  |
| total_tables_failed        | integer        | The number of total tables currently in the failed state.                                                                                      |
| creation_time              | timestamp      | The time (UTC) when the integration is created. It is defined as the time when the target database is created from the integration.            |
| refresh_interval           | integer        | The approximate time interval, in seconds, to refresh data from the zero-ETL source to the target database.                                    |
| source_database            | character(128) | The name of the source database.                                                                                                               |
| is_history_mode            | boolean        | A `TRUE` value indicates that history mode is on. A `FALSE` indicates that history mode is off.                                                |

## Sample queries

The following SQL command displays the currently defined integrations.

```
`select * from svv_integration;`
`integration_id | target_database | source | state | current_lag | last_replicated_checkpoint | total_tables_replicated | total_tables_failed | creation_time | refresh_interval | source_database | is_history_mode
---------------------------------------+-----------------+--------+-----------------+-------------+-------------------------------------+-------------------------+---------------------+---------------------------+--------------------+-----------------+-----------------
 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb | MySQL | CdcRefreshState | 56606106 | {"txn_seq":9834,"txn_id":126597515} | 152 | 0 | 2023-09-19 21:05:27.520299| 720 + mysourceetl | f`
```
