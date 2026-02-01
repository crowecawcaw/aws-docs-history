Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_QUERY_QUEUE_INFO

Summarizes details for queries that spent time in a workload management (WLM) query
queue or a commit queue.

The SVL_QUERY_QUEUE_INFO view filters queries performed by the system and shows only
queries performed by a user.

The SVL_QUERY_QUEUE_INFO view summarizes information from the [STL_QUERY](r_STL_QUERY.md "r_STL_QUERY.md"), [STL_WLM_QUERY](r_STL_WLM_QUERY.md "r_STL_WLM_QUERY.md"), and [STL_COMMIT_STATS](r_STL_COMMIT_STATS.md "r_STL_COMMIT_STATS.md") system tables.

SVL_QUERY_QUEUE_INFO is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name          | Data type     | Description                                                                                                      |
| -------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| database             | text          | The name of the database the user was connected to<br>when the query was issued.                                 |
| query                | integer       | Query ID.                                                                                                        |
| xid                  | bigint        | Transaction ID.                                                                                                  |
| userid               | integer       | ID of the user that generated the query.                                                                         |
| querytxt             | text          | First 100 characters of the query text.                                                                          |
| queue_start_time     | timestamp     | Time in UTC when the query entered the WLM queue.                                                                |
| exec_start_time      | timestamp     | Time in UTC when query execution started.                                                                        |
| service_class        | integer       | ID for the service class. Service classes are<br>defined in the WLM configuration file.                          |
| slots                | integer       | Number of WLM query slots.                                                                                       |
| queue_elapsed        | bigint        | Time that the query spent waiting in a WLM queue<br>(in seconds).                                                |
| exec_elapsed         | bigint        | Time spent executing the query (in<br>seconds).                                                                  |
| wlm_total_elapsed    | bigint        | Time that the query spent in a WLM queue<br>(queue_elapsed), plus time spent executing the query (exec_elapsed). |
| commit_queue_elapsed | bigint        | Time that the query spent waiting in the commit<br>queue (in seconds).                                           |
| commit_exec_time     | bigint        | Time that the query spent in the commit operation<br>(in seconds).                                               |
| service_class_name   | character(64) | The name of the service class.                                                                                   |

## Sample queries

The following example shows the time that queries spent in WLM queues.

```
select query, service_class, queue_elapsed, exec_elapsed, wlm_total_elapsed
from svl_query_queue_info
where wlm_total_elapsed > 0;

  query  | service_class | queue_elapsed | exec_elapsed | wlm_total_elapsed
---------+---------------+---------------+--------------+-------------------
 2742669 |             6 |             2 |          916 |                918
 2742668 |             6 |             4 |          197 |                201
(2 rows)

```
