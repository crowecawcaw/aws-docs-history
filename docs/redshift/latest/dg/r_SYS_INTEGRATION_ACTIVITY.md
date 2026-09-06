

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_INTEGRATION\_ACTIVITY
<a name="r_SYS_INTEGRATION_ACTIVITY"></a>

SYS\_INTEGRATION\_ACTIVITY displays details about completed integration runs.

SYS\_INTEGRATION\_ACTIVITY is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For information about zero-ETL integrations, see [Working with zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html) in the Amazon Redshift Management Guide.

## Table columns
<a name="r_SYS_INTEGRATION_ACTIVITY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| integration\_id | character(128) | The identifier associated with the integration. | 
| target\_database | character(128) | The database in Amazon Redshift that receives the integration data. | 
| source | character(128) | The source data for the integration. Possible types includes MySQL and PostgreSQL. | 
| checkpoint\_name | character(128) | The name of the checkpoint replicating binlog coordinates. | 
| checkpoint\_type | character(16) | The type of checkpoint. Possible values include: snapshot, cdc. | 
| checkpoint\_bytes | bigint | The number of bytes in this checkpoint. | 
| last\_commit\_timestamp | timestamp | The timestamp when last commited in this checkpoint. | 
| modified\_tables | integer | The number of tables modified in the checkpoint. | 
| integration\_start\_time | time | The time (UTC) when integration started for this checkpoint. | 
| integration\_end\_time | time | The time (UTC) when integration ended for this checkpoint. | 

## Sample queries
<a name="r_SYS_INTEGRATION_ACTIVITY-sample-queries"></a>

The following SQL command displays the log of integrations. 

```
select * from sys_integration_activity;

          integration_id              | target_database | source |            checkpoint_name                  | checkpoint_type  | checkpoint_bytes | last_commit_timestamp   | modified_tables |   integration_start_time   |    integration_end_time
--------------------------------------+-----------------+--------+---------------------------------------------+------------------+------------------+-------------------------+-----------------+----------------------------+----------------------------
 76b15917-afae-4447-b7fd-08e2a5acce7b |   demo1         | MySQL  | checkpoints/checkpoint_3_241_3_510.json     |        cdc       |        762       | 2023-05-10 23:00:14.201 |         1       | 2023-05-10 23:00:45.054265 | 2023-05-10 23:00:46.339826
 76b15917-afae-4447-b7fd-08e2a5acce7b |   demo1         | MySQL  | checkpoints/checkpoint_3_16329_3_17839.json |        cdc       |       13488      | 2023-05-11 01:33:57.411 |         2       | 2023-05-11 02:19:09.440121 | 2023-05-11 02:19:16.090492
 76b15917-afae-4447-b7fd-08e2a5acce7b |   demo1         | MySQL  | checkpoints/checkpoint_3_5103_3_5532.json   |        cdc       |        1657      | 2023-05-10 23:13:14.205 |         2       | 2023-05-10 23:13:23.545487 | 2023-05-10 23:13:25.652144
```