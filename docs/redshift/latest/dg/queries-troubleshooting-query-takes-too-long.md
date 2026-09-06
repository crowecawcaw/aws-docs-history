

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Query takes too long
<a name="queries-troubleshooting-query-takes-too-long"></a>

Your query can take too long for the following reasons. We suggest the following troubleshooting approaches.

**Tables are not optimized**  
Set the sort key, distribution style, and compression encoding of the tables to take full advantage of parallel processing. For more information, see [Automatic table optimization](t_Creating_tables.md) 

**Query is writing to disk**  
Your queries might be writing to disk for at least part of the query execution. For more information, see [Query performance improvement](query-performance-improvement-opportunities.md).

**Query must wait for other queries to finish**  
You might be able to improve overall system performance by creating query queues and assigning different types of queries to the appropriate queues. For more information, see [Workload management](cm-c-implementing-workload-management.md). 

**Queries are not optimized**  
Analyze the explain plan to find opportunities for rewriting queries or optimizing the database. For more information, see [Creating and interpreting a query plan](c-the-query-plan.md).

**Query needs more memory to run**  
If a specific query needs more memory, you can increase the available memory by increasing the [wlm\_query\_slot\_count](r_wlm_query_slot_count.md). 

**Database requires a VACUUM command to be run**  
Run the VACUUM command whenever you add, delete, or modify a large number of rows, unless you load your data in sort key order. The VACUUM command reorganizes your data to maintain the sort order and restore performance. For more information, see [Vacuuming tables](t_Reclaiming_storage_space202.md).

## Additional resources for troubleshooting long-running queries
<a name="queries-troubleshooting-cross-refs"></a>

The following are system-view topics and other documentation sections that are helpful for query tuning:
+ The [STV\_INFLIGHT](r_STV_INFLIGHT.md) system view shows which queries are running on the cluster. It can be helpful to use it together with [STV\_RECENTS](r_STV_RECENTS.md) to determine which queries are currently running or recently completed.
+ [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md) is useful for troubleshooting. It shows DDL and DML queries with relevant properties like their current status, such as `running` or `failed`, the time it took each to run, and whether a query ran on a concurrency-scaling cluster.
+ [STL\_QUERYTEXT](r_STL_QUERYTEXT.md) captures the query text for SQL commands. Additionally, [SVV\_QUERY\_INFLIGHT](r_SVV_QUERY_INFLIGHT.md), which joins STL\_QUERYTEXT to STV\_INFLIGHT, shows more query metadata.
+ A transaction-lock conflict can be a possible source of query-performance issues. For information about transactions that currently hold locks on tables, see [SVV\_TRANSACTIONS](r_SVV_TRANSACTIONS.md).
+ [Identifying queries that are top candidates for tuning](https://docs.aws.amazon.com/redshift/latest/dg/diagnostic-queries-for-query-tuning.html#identify-queries-that-are-top-candidates-for-tuning) provides a troubleshooting query that helps you determine which recently-run queries were the most time consuming. This can help you focus your efforts on queries that need improvement.
+ If you want to explore query management further and understand how to manage query queues, [Workload management](cm-c-implementing-workload-management.md) shows how to do it. Workload management is an advanced feature and we recommend automated workload management in most cases.