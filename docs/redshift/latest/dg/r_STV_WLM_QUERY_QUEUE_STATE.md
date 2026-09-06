

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_WLM\_QUERY\_QUEUE\_STATE
<a name="r_STV_WLM_QUERY_QUEUE_STATE"></a>

Records the current state of the query queues for the service classes.

STV\_WLM\_QUERY\_QUEUE\_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_STV_WLM_QUERY_QUEUE_STATE-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| service\_class  | integer  | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids).  | 
| position  | integer  | Position of the query in the queue. The query with the smallest position value runs next.  | 
| task  | integer  | ID used to track a query through the workload manager. Can be associated with multiple query IDs. If a query is restarted, the query is assigned a new query ID but not a new task ID.  | 
| query  | integer  | Query ID. If a query is restarted, the query is assigned a new query ID but not a new task ID.  | 
| slot\_count | integer | Number of WLM query slots. | 
| start\_time  | timestamp | Time that the query entered the queue.  | 
| queue\_time  | bigint  | Number of microseconds that the query has been in the queue.  | 

## Sample query
<a name="r_STV_WLM_QUERY_QUEUE_STATE-sample-query2"></a>

The following query shows the queries in the queue for service classes greater than 4. 

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