Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_WLM_QUERY_QUEUE_STATE

Records the current state of the query queues for the service classes.

STV_WLM_QUERY_QUEUE_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name   | Data type | Description                                                                                                                                                                                                    |
| ------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| service_class | integer   | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids"). |
| position      | integer   | Position of the query in the queue. The query with<br>the smallest `position` value runs next.                                                                                                                 |
| task          | integer   | ID used to track a query through the workload<br>manager. Can be associated with multiple query IDs. If a query is<br>restarted, the query is assigned a new query ID but not a new task<br>ID.                |
| query         | integer   | Query ID. If a query is restarted, the query is<br>assigned a new query ID but not a new task ID.                                                                                                              |
| slot_count    | integer   | Number of WLM query slots.                                                                                                                                                                                     |
| start_time    | timestamp | Time that the query entered the queue.                                                                                                                                                                         |
| queue_time    | bigint    | Number of microseconds that the query has been in<br>the queue.                                                                                                                                                |

## Sample query

The following query shows the queries in the queue for service classes greater
than 4.

```
select * from stv_wlm_query_queue_state
where service_class > 4
order by service_class;
```

This query returns the following sample output.

```

 service_class | position | task | query | slot_count |        start_time          | queue_time
---------------+----------+------+-------+------------+----------------------------+------------
             5 |        0 |  455 |   476 |          5 | 2010-10-06 13:18:24.065838 |   20937257
             6 |        1 |  456 |   478 |          5 | 2010-10-06 13:18:26.652906 |   18350191
(2 rows)
```
