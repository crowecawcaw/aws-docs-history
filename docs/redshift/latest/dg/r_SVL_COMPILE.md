

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_COMPILE
<a name="r_SVL_COMPILE"></a>

Records compile time and location for each query segment of queries.

SVL\_COMPILE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
SVL\_COMPILE only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

For information about SVCS\_COMPILE, see [SVCS\_COMPILE](r_SVCS_COMPILE.md).

## Table columns
<a name="r_SVL_COMPILE-table-rows"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| xid  | bigint  | Transaction ID associated with the statement.  | 
| pid  | integer  | Process ID associated with the statement.  | 
| query | integer  | Query ID. Can be used to join various other system tables and views.  | 
| segment  | integer  | The query segment to be compiled.  | 
| locus  | integer  | Location where the segment runs. 1 if on a compute node and 2 if on the leader node.  | 
| starttime | timestamp | Time in UTC that the compile started. | 
| endtime | timestamp | Time in UTC that the compile ended. | 
| compile  | integer  | 0 if the compile was reused, 1 if the segment was compiled. | 

## Sample queries
<a name="r_SVL_COMPILE-sample-queries"></a>

In this example, queries 35878 and 35879 ran the same SQL statement. The compile column for query 35878 shows `1` for four query segments, which indicates that the segments were compiled. Query 35879 shows `0` in the compile column for every segment, indicating that the segments did not need to be compiled again.

```
select userid, xid,  pid, query, segment, locus,  
datediff(ms, starttime, endtime) as duration, compile 
from svl_compile 
where query = 35878 or query = 35879
order by query, segment;

 userid |  xid   |  pid  | query | segment | locus | duration | compile
--------+--------+-------+-------+---------+-------+----------+---------
    100 | 112780 | 23028 | 35878 |       0 |     1 |        0 |       0
    100 | 112780 | 23028 | 35878 |       1 |     1 |        0 |       0
    100 | 112780 | 23028 | 35878 |       2 |     1 |        0 |       0
    100 | 112780 | 23028 | 35878 |       3 |     1 |        0 |       0
    100 | 112780 | 23028 | 35878 |       4 |     1 |        0 |       0
    100 | 112780 | 23028 | 35878 |       5 |     1 |        0 |       0
    100 | 112780 | 23028 | 35878 |       6 |     1 |     1380 |       1
    100 | 112780 | 23028 | 35878 |       7 |     1 |     1085 |       1
    100 | 112780 | 23028 | 35878 |       8 |     1 |     1197 |       1
    100 | 112780 | 23028 | 35878 |       9 |     2 |      905 |       1
    100 | 112782 | 23028 | 35879 |       0 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       1 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       2 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       3 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       4 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       5 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       6 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       7 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       8 |     1 |        0 |       0
    100 | 112782 | 23028 | 35879 |       9 |     2 |        0 |       0
(20 rows)
```