

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_RESTORE\_LOG
<a name="SYS_RESTORE_LOG"></a>

Use SYS\_RESTORE\_LOG to monitor the migration progress of each table in the cluster during a classic resize to RG or RA3 nodes. It captures the historic throughput of data migration during the resize operation. For more information about classic resize to RG or RA3 nodes, see [Classic resize](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html#classic-resize-faster). 

SYS\_RESTORE\_LOG is visible only to superusers.

## Table columns
<a name="SYS_RESTORE_LOG-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| event\_time | timestamp | A timestamp that indicates when the log entry is recorded. | 
| database\_name | char(128) | The name of the database. | 
| schema\_name | char(128) | The name of the schema. | 
| table\_name | char(128) | The name of the table. | 
| table\_id | integer | The ID of the table. | 
| action | char(128) | The action taken at the time of the entry. Values can include: Migration started, checkpoint, resumed, completed, cancelled, or reset. | 
| table\_size | long | The size of the table. | 
| total\_data\_processed | long | The size of the data in MB processed up to this point for the table. | 
| delta\_data\_processed | long | Size of data processed since the last event\_time update, in MB. This helps you determine how much of the data has been processed since the previous recorded time interval. You can compare this with the table\_size to get a sense of how quickly data processing is going. | 
| message | char(512) | A detailed explanation for the value in the action column. | 
| redistribution\_type | char(32) | The redistribution type for the table. Either KEY conversion or an EVEN rebalancing task. For more information about distribution styles, see [Distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html). | 

## Sample queries
<a name="SYS_RESTORE_LOG-sample-queries"></a>

The following query calculates the throughput of data processing, using SYS\_RESTORE\_LOG.

```
SELECT
    ROUND(sum(delta_data_processed) / 1024.0, 2) as data_processed_gb,
    ROUND(datediff(sec, min(event_time), max(event_time)) / 3600.0, 2) as duration_hr,
    ROUND(data_processed_gb/duration_hr, 2) as throughput_gb_per_hr
from sys_restore_log;
```

Sample output.

```
 data_processed_gb | duration_hr | throughput_gb_per_hr 
-------------------+-------------+----------------------
              0.91 |        8.37 |                 0.11
(1 row)
```

The following query that shows all redistribution types.

```
SELECT * from sys_restore_log ORDER BY event_time;
```

```
 database_name |     schema_name      |      table_name      | table_id |          action             | total_data_processed | delta_data_processed |         event_time         | table_size | message |   redistribution_type    
---------------+----------------------+----------------------+----------+-----------------------------+----------------------+----------------------+----------------------------+------------+---------+--------------------------
 dev           | schemaaaa877096d844d | customer_key         |   106424 | Redistribution started      |                    0 |                      | 2024-01-05 02:18:00.744977 |        325 |         | Restore Distkey Table
 dev           | schemaaaa877096d844d | dp30907_t2_autokey   |   106430 | Redistribution started      |                    0 |                      | 2024-01-05 02:18:02.756675 |         90 |         | Restore Distkey Table
 dev           | schemaaaa877096d844d | dp30907_t2_autokey   |   106430 | Redistribution completed    |                   90 |                   90 | 2024-01-05 02:23:30.643718 |         90 |         | Restore Distkey Table
 dev           | schemaaaa877096d844d | customer_key         |   106424 | Redistribution completed    |                  325 |                  325 | 2024-01-05 02:23:45.998249 |        325 |         | Restore Distkey Table
 dev           | schemaaaa877096d844d | dp30907_t1_even      |   106428 | Redistribution started      |                    0 |                      | 2024-01-05 02:23:46.083849 |         30 |         | Rebalance Disteven Table
 dev           | schemaaaa877096d844d | dp30907_t5_auto_even |   106436 | Redistribution started      |                    0 |                      | 2024-01-05 02:23:46.855728 |         45 |         | Rebalance Disteven Table
 dev           | schemaaaa877096d844d | dp30907_t5_auto_even |   106436 | Redistribution completed    |                   45 |                   45 | 2024-01-05 02:24:16.343029 |         45 |         | Rebalance Disteven Table
 dev           | schemaaaa877096d844d | dp30907_t1_even      |   106428 | Redistribution completed    |                   30 |                   30 | 2024-01-05 02:24:20.584703 |         30 |         | Rebalance Disteven Table
 dev           | schemaefd028a2a48a4c | customer_even        |   130512 | Redistribution started      |                    0 |                      | 2024-01-05 04:54:55.641741 |        190 |         | Restore Disteven Table
 dev           | schemaefd028a2a48a4c | customer_even        |   130512 | Redistribution checkpointed |     29.4342113157737 |     29.4342113157737 | 2024-01-05 04:55:04.770696 |        190 |         | Restore Disteven Table
(8 rows)
```