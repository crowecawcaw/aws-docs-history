Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_INTEGRATION\_TABLE\_STATE

SVV\_INTEGRATION\_TABLE\_STATE displays details about table-level integration information.

SVV\_INTEGRATION\_TABLE\_STATE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For more information, see [Zero-ETL integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md").

## Table columns

| Column name                         | Data type                   | Description                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| integration\_id                     | character(128)              | The identifier associated with the<br>integration.                                                                                                                                                                                                                                                                                                 |
| target\_database                    | character(128)              | The name of the Amazon Redshift database.                                                                                                                                                                                                                                                                                                          |
| schema\_name                        | character(128)              | The name of the Amazon Redshift schema.                                                                                                                                                                                                                                                                                                            |
| table\_name                         | character(128)              | The name of the table.                                                                                                                                                                                                                                                                                                                             |
| table\_state                        | character(128)              | The state of the table. Possible values are<br>`Synced`, `Failed`, `Deleted`, `ResyncRequired`, `ResyncInitiated` and `DroppedSource`.<br>The `DroppedSource` state indicates that the source of a history mode table was dropped at the source.                                                                                                   |
| table\_last\_replicated\_checkpoint | character(128)              | The current synced log coordinates.                                                                                                                                                                                                                                                                                                                |
| reason                              | character(256)              | The reason for the last state transition. Common reasons can be unsupported data types in tables, tables don't have primary keys.<br>To learn more about how to troubleshoot common issues, see [Troubleshooting zero-ETL integrations in Amazon Redshift](../mgmt/zero-etl-using.troubleshooting.md "../mgmt/zero-etl-using.troubleshooting.md"). |
| last\_updated\_timestamp            | timestamp without time zone | The time (UTC) when the table is last<br>updated.                                                                                                                                                                                                                                                                                                  |
| table\_rows                         | bigint                      | The total number of rows in the table.                                                                                                                                                                                                                                                                                                             |
| table\_size                         | bigint                      | The size of the table in megabytes (MB).                                                                                                                                                                                                                                                                                                           |
| is\_history\_mode                   | boolean                     | A `TRUE` value indicates that history mode is on. A `FALSE` indicates that history mode is off.                                                                                                                                                                                                                                                    |

## Sample queries

The following SQL command displays the columns of the log of integrations.

```
`select * from svv_integration_table_state;`
`integration_id | target_database | schema_name | table_name | table_state |table_last_replicated_checkpoint | reason | last_updated_timestamp |table_rows | table_size | is_history_mode
--------------------------------------+-----------------+-------------+-------------------+--------------+---------------------------------+--------+----------------------------+------------+------------+-----------------
 4798e675-8f9f-4686-b05f-92c538e19629 | sample_test2 | sample | SampleTestChannel | Synced | {"txn_seq":3,"txn_id":3122} | | 2023-05-12 12:40:30.656625 | 2 | 16 | f`
```
