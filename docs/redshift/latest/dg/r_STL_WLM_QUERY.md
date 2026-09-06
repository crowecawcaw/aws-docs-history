

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_WLM\_QUERY
<a name="r_STL_WLM_QUERY"></a>

Contains a record of each attempted execution of a query in a service class handled by WLM.

STL\_WLM\_QUERY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_STL_WLM_QUERY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| xid  | integer  | Transaction ID of the query or subquery.  | 
| task  | integer  | ID used to track a query through the workload manager. Can be associated with multiple query IDs. If a query is restarted, the query is assigned a new query ID but not a new task ID.  | 
| query  | integer | Query ID. If a query is restarted, the query is assigned a new query ID but not a new task ID.  | 
| service\_class  | integer  | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids).  | 
| slot\_count | integer | Number of WLM query slots that a query uses according to the concurrency level set for the queue. Default is 1. For more information, see [ wlm\_query\_slot\_count](https://docs.aws.amazon.com/redshift/latest/dg/r_wlm_query_slot_count.html). | 
| service\_class\_start\_time  | timestamp  | Time that the query was assigned to the service class. This time is in the UTC time zone. | 
| queue\_start\_time  | timestamp  | Time that the query entered the queue for the service class. This time is in the UTC time zone. | 
| queue\_end\_time  | timestamp  | Time when the query left the queue for the service class. This time is in the UTC time zone. | 
| total\_queue\_time  | bigint  | Total number of microseconds that the query spent in the queue | 
| exec\_start\_time  | timestamp  | Time that the query began executing in the service class. This time is in the UTC time zone. | 
| exec\_end\_time  | timestamp  | Time that the query completed execution in the service class. This time is in the UTC time zone. | 
| total\_exec\_time  | bigint  | Number of microseconds that the query spent executing.  | 
| service\_class\_end\_time  | timestamp  | Time that the query left the service class. This time is in the UTC time zone.  | 
| final\_state  | character(16)  | Reserved for system use. | 
| est\_peak\_mem | bigint | Reserved for system use. | 
| query\_priority | char(20) | The priority of the query. Possible values are n/a, lowest, low, normal, high, and highest, where n/a means that query priority isn't supported.  | 
| service\_class\_name | character(64) | The service class name. For more information about service classes, see [WLM system tables and views](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-system-tables-and-views.html). | 

## Sample queries
<a name="r_STL_WLM_QUERY-sample-queries"></a>

 **View average query Time in queues and executing** 

The following queries display the current configuration for service classes greater than 4. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids).

The following query returns the average time (in microseconds) that each query spent in query queues and executing for each service class. 

```
select service_class as svc_class, count(*),
avg(datediff(microseconds, queue_start_time, queue_end_time)) as avg_queue_time,
avg(datediff(microseconds, exec_start_time, exec_end_time )) as avg_exec_time
from stl_wlm_query
where service_class > 4
group by service_class
order by service_class;
```

This query returns the following sample output: 

```
 svc_class | count | avg_queue_time | avg_exec_time
-----------+-------+----------------+---------------
         5 | 20103 |              0 |         80415
         5 |  3421 |          34015 |        234015
         6 |    42 |              0 |        944266
         7 |   196 |           6439 |       1364399
(4 rows)
```

 **View maximum query time in queues and executing** 

The following query returns the maximum amount of time (in microseconds) that a query spent in any query queue and executing for each service class.

```
select service_class as svc_class, count(*),
max(datediff(microseconds, queue_start_time, queue_end_time)) as max_queue_time,
max(datediff(microseconds, exec_start_time, exec_end_time )) as max_exec_time
from stl_wlm_query
where svc_class > 5  
group by service_class
order by service_class;
```

```
 svc_class | count | max_queue_time | max_exec_time
-----------+-------+----------------+---------------
         6 |    42 |              0 |       3775896
         7 |   197 |          37947 |      16379473
(4 rows)
```