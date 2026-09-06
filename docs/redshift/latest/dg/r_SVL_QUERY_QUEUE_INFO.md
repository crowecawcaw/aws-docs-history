

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_QUERY\_QUEUE\_INFO
<a name="r_SVL_QUERY_QUEUE_INFO"></a>

Summarizes details for queries that spent time in a workload management (WLM) query queue or a commit queue. 

The SVL\_QUERY\_QUEUE\_INFO view filters queries performed by the system and shows only queries performed by a user. 

The SVL\_QUERY\_QUEUE\_INFO view summarizes information from the [STL\_QUERY](r_STL_QUERY.md), [STL\_WLM\_QUERY](r_STL_WLM_QUERY.md), and [STL\_COMMIT\_STATS](r_STL_COMMIT_STATS.md) system tables. 

SVL\_QUERY\_QUEUE\_INFO is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVL_QUERY_QUEUE_INFO-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| database | text | The name of the database the user was connected to when the query was issued. | 
| query | integer | Query ID.  | 
| xid  | bigint  | Transaction ID.  | 
| userid | integer | ID of the user that generated the query.  | 
| querytxt | text | First 100 characters of the query text. | 
| queue\_start\_time | timestamp | Time in UTC when the query entered the WLM queue.  | 
| exec\_start\_time | timestamp | Time in UTC when query execution started. | 
| service\_class | integer | ID for the service class. Service classes are defined in the WLM configuration file. | 
| slots | integer | Number of WLM query slots. | 
| queue\_elapsed | bigint | Time that the query spent waiting in a WLM queue (in seconds). | 
| exec\_elapsed | bigint | Time spent executing the query (in seconds). | 
| wlm\_total\_elapsed | bigint | Time that the query spent in a WLM queue (queue\_elapsed), plus time spent executing the query (exec\_elapsed).  | 
| commit\_queue\_elapsed | bigint | Time that the query spent waiting in the commit queue (in seconds). | 
| commit\_exec\_time | bigint | Time that the query spent in the commit operation (in seconds). | 
| service\_class\_name | character(64) | The name of the service class. | 

## Sample queries
<a name="r_SVL_QUERY_QUEUE_INFO-sample-queries"></a>

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