Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_WLM_SERVICE_CLASS_STATE

Contains the current state of the service classes.

STV_WLM_SERVICE_CLASS_STATE is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name                     | Data type | Description                                                                                                                                                                                                           |
| ------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------------------- | --- | ----- | --- | ----- | --- | --------------- |
| service_class                   | integer   | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids").        |
| num_queued_queries              | integer   | Number of queries currently in the queue.                                                                                                                                                                             |
| num_executing_queries           | integer   | Number of queries currently executing.                                                                                                                                                                                |
| num_serviced_queries            | integer   | Number of queries that have ever been in the service class.                                                                                                                                                           |
| num_executed_queries            | integer   | Number of queries that have run since Amazon Redshift was restarted.                                                                                                                                                  |
| num_evicted_queries             | integer   | Number of queries that have been evicted since Amazon Redshift was restarted. Some of the reasons for an evicted query include a WLM timeout, a QMR hop action, and a query failing on a concurrency scaling cluster. |
| num_concurrency_scaling_queries | integer   | Number of queries run on a concurrency scaling cluster since Amazon Redshift was restarted.                                                                                                                           | ## Sample query The following query displays the state for service classes greater than 5. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids"). `select service_class, num_executing_queries, num_executed_queries from stv_wlm_service_class_state where service_class > 5 order by service_class;` ``` service_class | num_executing_queries | num_executed_queries ---------------+-----------------------+---------------------- 6 | 1   | 222 7 | 0   | 135 8 | 1   | 39 (3 rows) ``` |
