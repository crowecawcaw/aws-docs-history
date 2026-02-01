Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_INTEGRATION_ACTIVITY

SYS_INTEGRATION_ACTIVITY displays details about completed integration runs.

SYS_INTEGRATION_ACTIVITY is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about zero-ETL integrations, see [Working with zero-ETL
integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md") in the Amazon Redshift Management Guide.

## Table columns

| Column name            | Data type      | Description                                                                                  |
| ---------------------- | -------------- | -------------------------------------------------------------------------------------------- |
| integration_id         | character(128) | The identifier associated with the<br>integration.                                           |
| target_database        | character(128) | The database in Amazon Redshift that receives the integration<br>data.                       |
| source                 | character(128) | The source data for the integration. Possible<br>types includes `MySQL` and<br>`PostgreSQL`. |
| checkpoint_name        | character(128) | The name of the checkpoint replicating binlog<br>coordinates.                                |
| checkpoint_type        | character(16)  | The type of checkpoint. Possible values include:<br>`snapshot`, `cdc`.                       |
| checkpoint_bytes       | bigint         | The number of bytes in this checkpoint.                                                      |
| last_commit_timestamp  | timestamp      | The timestamp when last commited in this<br>checkpoint.                                      |
| modified_tables        | integer        | The number of tables modified in the<br>checkpoint.                                          |
| integration_start_time | time           | The time (UTC) when integration started for this<br>checkpoint.                              |
| integration_end_time   | time           | The time (UTC) when integration ended for this<br>checkpoint.                                |

## Sample queries

The following SQL command displays the log of integrations.

```
select * from sys_integration_activity;

          integration_id              | target_database | source |            checkpoint_name                  | checkpoint_type  | checkpoint_bytes | last_commit_timestamp   | modified_tables |   integration_start_time   |    integration_end_time
--------------------------------------+-----------------+--------+---------------------------------------------+------------------+------------------+-------------------------+-----------------+----------------------------+----------------------------
 76b15917-afae-4447-b7fd-08e2a5acce7b |   demo1         | MySQL  | checkpoints/checkpoint_3_241_3_510.json     |        cdc       |        762       | 2023-05-10 23:00:14.201 |         1       | 2023-05-10 23:00:45.054265 | 2023-05-10 23:00:46.339826
 76b15917-afae-4447-b7fd-08e2a5acce7b |   demo1         | MySQL  | checkpoints/checkpoint_3_16329_3_17839.json |        cdc       |       13488      | 2023-05-11 01:33:57.411 |         2       | 2023-05-11 02:19:09.440121 | 2023-05-11 02:19:16.090492
 76b15917-afae-4447-b7fd-08e2a5acce7b |   demo1         | MySQL  | checkpoints/checkpoint_3_5103_3_5532.json   |        cdc       |        1657      | 2023-05-10 23:13:14.205 |         2       | 2023-05-10 23:13:23.545487 | 2023-05-10 23:13:25.652144
```
