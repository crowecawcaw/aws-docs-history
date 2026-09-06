

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_QUERY\_INFLIGHT
<a name="r_SVV_QUERY_INFLIGHT"></a>

Use the SVV\_QUERY\_INFLIGHT view to determine what queries are currently running on the database. This view joins [STV\_INFLIGHT](r_STV_INFLIGHT.md) to [STL\_QUERYTEXT](r_STL_QUERYTEXT.md). SVV\_QUERY\_INFLIGHT does not show leader-node only queries. For more information, see [Leader node–only functions](c_SQL_functions_leader_node_only.md).

SVV\_QUERY\_INFLIGHT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
This view is only available when querying provisioned clusters.

## Table columns
<a name="sub-r_SVV_QUERY_INFLIGHT-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid  | integer  | ID of user who generated entry.  | 
| slice  | integer  | Slice where the query is running.  | 
| query  | integer  | Query ID. Can be used to join various other system tables and views.  | 
| pid  | integer  | Process ID. All of the queries in a session are run in the same process, so this value remains constant if you run a series of queries in the same session. You can use this column to join to the [STL\_ERROR](r_STL_ERROR.md) table.  | 
| starttime  | timestamp | Time that the query started.  | 
| suspended  | integer  | Whether the query is suspended: 0 = false; 1 = true.  | 
| text  | character(200)  | Query text, in 200-character increments.  | 
| sequence  | integer  | Sequence number for segments of query statements.  | 

## Sample queries
<a name="r_SVV_QUERY_INFLIGHT-sample-queries"></a>

The sample output below shows two queries currently running, the SVV\_QUERY\_INFLIGHT query itself and query 428, which is split into three rows in the table. (The starttime and statement columns are truncated in this sample output.) 

```
select slice, query, pid, starttime, suspended, trim(text) as statement, sequence
from svv_query_inflight
order by query, sequence;

slice|query| pid  |      starttime       |suspended| statement | sequence
-----+-----+------+----------------------+---------+-----------+---------
1012 | 428 | 1658 | 2012-04-10 13:53:... |       0 | select ...|    0
1012 | 428 | 1658 | 2012-04-10 13:53:... |       0 | enueid ...|    1
1012 | 428 | 1658 | 2012-04-10 13:53:... |       0 | atname,...|    2
1012 | 429 | 1608 | 2012-04-10 13:53:... |       0 | select ...|    0
(4 rows)
```