Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_INTEGRATION

SVV\_INTEGRATION displays details about the configuration of integrations.

SVV\_INTEGRATION is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about zero-ETL integrations, see [Zero-ETL integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md").

## Table columns

| Column name                           | Data type      | Description                                                                                                                                    |
| ------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| integration\_id                       | character(128) | The identifier associated with the integration.                                                                                                |
| target\_database                      | character(128) | The database in Amazon Redshift that receives the integration data.                                                                            |
| source                                | character(128) | The source data for the integration. Possible types include `MySQL`, `PostgreSQL`, and `S3_EVENT_NOTIFICATIONS`.                               |
| state                                 | character(128) | The state of the integration. Possible values include `PendingDbConnectState`, `SchemaDiscoveryState`, `CdcRefreshState`,<br>and `ErrorState`. |
| current\_lag                          | bigint         | The current lag time (milliseconds) between the source and destination of the integration.                                                     |
| last\_replicated\_checkpoint          | character(128) | The last replicated checkpoint.                                                                                                                |
| total\_tables\_replicated             | integer        | The number of total tables currently in the replicated state.                                                                                  |
| total\_tables\_failed                 | integer        | The number of total tables currently in the failed state.                                                                                      |
| creation\_time                        | timestamp      | The time (UTC) when the integration is created. It is defined as the time when the target database is created from the integration.            |
| refresh\_interval                     | integer        | The approximate time interval, in seconds, to refresh data from the zero-ETL source to the target database.                                    |
| source\_database                      | character(128) | The name of the source database.                                                                                                               |
| is\_history\_mode                     | boolean        | A `TRUE` value indicates that history mode is on. A `FALSE` indicates that history mode is off.                                                |
| latest\_detected\_change\_time        | timestamp      | The time (UTC) when the latest source change for this integration database was staged in the replication queue.                                |
| latest\_applied\_change\_time         | timestamp      | The time (UTC) of the last successful ingestion on Amazon Redshift for this target database.                                                   |
| auto\_remediation                     | boolean        | A `TRUE` value indicates that automatic remediation of duplicate rows is enabled. A `FALSE` value indicates that it is disabled.               |
| latest\_shipped\_source\_commit\_time | timestamp      | The time (UTC), on the source database clock, up to which source transactions have been shipped for this integration.                          |

## Sample queries

The following SQL command displays the currently defined integrations.

```
`select * from svv_integration;`
`integration_id | target_database | source | state | current_lag | last_replicated_checkpoint | total_tables_replicated | total_tables_failed | creation_time | refresh_interval | source_database | is_history_mode
---------------------------------------+-----------------+--------+-----------------+-------------+-------------------------------------+-------------------------+---------------------+---------------------------+--------------------+-----------------+-----------------
 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb | MySQL | CdcRefreshState | 56606106 | {"txn_seq":9834,"txn_id":126597515} | 152 | 0 | 2023-09-19 21:05:27.520299| 720 + mysourceetl | f`
```
