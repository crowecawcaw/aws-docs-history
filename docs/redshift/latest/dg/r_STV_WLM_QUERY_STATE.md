

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_WLM\_QUERY\_STATE
<a name="r_STV_WLM_QUERY_STATE"></a>

Records the current state of queries being tracked by WLM. 

STV\_WLM\_QUERY\_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_STV_WLM_QUERY_STATE-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| xid  | integer  | Transaction ID of the query or subquery.  | 
| task  | integer  | ID used to track a query through the workload manager. Can be associated with multiple query IDs. If a query is restarted, the query is assigned a new query ID but not a new task ID.  | 
| query  | integer  | Query ID. If a query is restarted, the query is assigned a new query ID but not a new task ID.  | 
| service\_class  | integer  | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids).  | 
| slot\_count | integer | Number of WLM query slots. | 
| wlm\_start\_time  | timestamp  | Time that the query entered the system table queue or short query queue.  | 
| state  | character(16)  | Current state of the query or subquery. Possible values are the following:+  `Classified` – Query has been assigned to a service class. <br />+  `Completed` – Query is finished running. The query either ran successfully or was canceled. For the final state, check the results of [STL\_QUERY](r_STL_QUERY.md). <br />+  `Dequeued` – Internal use only. <br />+  `Evicted` – Query has been evicted from the service class for restart. <br />+  `Evicting` – Query is being evicted from the service class for restart. <br />+  `Initialized` – Internal use only. <br />+  `Invalid` – Internal use only. <br />+  `Queued` – Query was sent to the query queue because no slots were available to run it. <br />+  `QueuedWaiting` – Query is waiting in the query queue. <br />+  `Rejected` – Internal use only. <br />+  `Returning` – Query is returning results to the client. <br />+  `Running` – Query is running. <br />+  `TaskAssigned` – Internal use only.  | 
| queue\_time  | bigint  | Number of microseconds that the query has spent in the queue.  | 
| exec\_time  | bigint  | Number of microseconds that the query has been running.  | 
| query\_priority  | char(20)  | The priority of the query. Possible values are n/a, lowest, low, normal, high, and highest, where n/a means that query priority isn't supported.  | 

## Sample query
<a name="r_STV_WLM_QUERY_STATE-sample-query"></a>

The following query displays all currently executing queries in service classes greater than 4. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids).

```
select xid, query, trim(state) as state, queue_time, exec_time
from stv_wlm_query_state
where service_class > 4;
```

This query returns the following sample output: 

```
xid    | query | state   | queue_time | exec_time 
-------+-------+---------+------------+-----------
100813 | 25942 | Running |          0 |    1369029
100074 | 25775 | Running |          0 | 2221589242
```