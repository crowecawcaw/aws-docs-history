Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_WLM_QUERY_TASK_STATE

Contains the current state of service class query tasks.

STV_WLM_QUERY_TASK_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type | Description                                                                                                                                                                                                    |
| ------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| service_class | integer   | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids"). |
| task          | integer   | ID used to track a query through the workload<br>manager. Can be associated with multiple query IDs. If a query is<br>restarted, the query is assigned a new query ID but not a new task<br>ID.                |
| query         | integer   | Query ID. If a query is restarted, the query is<br>assigned a new query ID but not a new task ID.                                                                                                              |
| slot_count    | integer   | Number of WLM query slots.                                                                                                                                                                                     |
| start_time    | timestamp | Time that the query began executing.                                                                                                                                                                           |
| exec_time     | bigint    | Number of microseconds that the query has been<br>executing.                                                                                                                                                   |

## Sample query

The following query displays the current
state of queries in service classes greater than 4. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids").

```
select * from stv_wlm_query_task_state
where service_class > 4;
```

This query returns the following sample output:

```

service_class | task | query |         start_time         | exec_time
--------------+------+-------+----------------------------+-----------
    5         |  466 |   491 | 2010-10-06 13:29:23.063787 | 357618748
(1 row)
```
