Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STV\_WLM\_SERVICE\_CLASS\_STATE

Contains the current state of the service classes.

STV\_WLM\_SERVICE\_CLASS\_STATE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name                        | Data type | Description                                                                                                                                                                                                              |
| ---------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| service\_class                     | integer   | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids").           |
| num\_queued\_queries               | integer   | Number of queries currently in the queue.                                                                                                                                                                                |
| num\_executing\_queries            | integer   | Number of queries currently executing.                                                                                                                                                                                   |
| num\_serviced\_queries             | integer   | Number of queries that have ever been in the<br>service class.                                                                                                                                                           |
| num\_executed\_queries             | integer   | Number of queries that have run since Amazon Redshift<br>was restarted.                                                                                                                                                  |
| num\_evicted\_queries              | integer   | Number of queries that have been evicted since<br>Amazon Redshift was restarted. Some of the reasons for an evicted query include a WLM timeout, a QMR hop action, and a query failing on a concurrency scaling cluster. |
| num\_concurrency\_scaling\_queries | integer   | Number of queries run on a concurrency scaling cluster since<br>Amazon Redshift was restarted.                                                                                                                           |

## Sample query

The following query displays the state
for service classes greater than 5. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids").

```
select service_class, num_executing_queries,
num_executed_queries
from stv_wlm_service_class_state
where service_class > 5
order by service_class;
```

```
 service_class | num_executing_queries | num_executed_queries
---------------+-----------------------+----------------------
             6 |                     1 |                  222
             7 |                     0 |                  135
             8 |                     1 |                   39
(3 rows)
```
