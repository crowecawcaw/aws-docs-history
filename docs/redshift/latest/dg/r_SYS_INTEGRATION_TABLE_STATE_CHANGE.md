

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_INTEGRATION\_TABLE\_STATE\_CHANGE
<a name="r_SYS_INTEGRATION_TABLE_STATE_CHANGE"></a>

SYS\_INTEGRATION\_TABLE\_STATE\_CHANGE displays details about table state change logs for integrations.

A superuser can see all rows in this table.

For more information, see [Working with Zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html).

## Table columns
<a name="r_SYS_INTEGRATION_TABLE_STATE_CHANGE-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| integration\_id | character(128) | The identifier associated with the integration. | 
| database\_name | character(128) | The name of the Amazon Redshift database. | 
| schema\_name | character(128) | The name of the Amazon Redshift schema. | 
| table\_name | character(128) | The name of the table. | 
| new\_state | character(128) | The state of the table. Possible values are Synced, ResyncRequired, ResyncInitiated, Deleted, Failed, and ResyncDeleted. | 
| table\_last\_replicated\_checkpoint | character(128) | The current synced log coordinates. | 
| state\_change\_reason | character(256) | The reason for the last state transition. | 
| record\_time | timestamp | The time (UTC) when this record was updated. | 

## Sample queries
<a name="r_SYS_INTEGRATION_TABLE_STATE_CHANGE-sample-queries"></a>

The following SQL command displays the log of integrations. 

```
select * from sys_integration_table_state_change;
                
            integration_id            | database_name | schema_name | table_name | new_state |  table_last_replicated_checkpoint   | state_change_reason |        record_time
--------------------------------------+---------------+-------------+------------+-----------+-------------------------------------+---------------------+----------------------------
 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb        | sbtest80t3s | sbtest79   | Synced    | {"txn_seq":9834,"txn_id":126597515} |                     | 2023-09-20 19:39:50.087868
 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb        | sbtest80t3s | sbtest56   | Synced    | {"txn_seq":9834,"txn_id":126597515} |                     | 2023-09-20 19:39:45.54005
 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb        | sbtest80t3s | sbtest50   | Synced    | {"txn_seq":9834,"txn_id":126597515} |                     | 2023-09-20 19:40:20.362504
 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb        | sbtest80t3s | sbtest18   | Synced    | {"txn_seq":9834,"txn_id":126597515} |                     | 2023-09-20 19:40:32.544084
 99108e72-1cfd-414f-8cc0-0216acefac77 | perfdb        | sbtest40t3s | sbtest23   | Synced    | {"txn_seq":9834,"txn_id":126597515} |                     | 2023-09-20 15:49:05.186209
```