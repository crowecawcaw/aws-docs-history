

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_INFLIGHT
<a name="r_STV_INFLIGHT"></a>

Use the STV\_INFLIGHT table to determine what queries are currently running on the cluster. If you're troubleshooting, it's helpful for checking the status of long-running queries. 

STV\_INFLIGHT does not show leader-node only queries. For more information, see [Leader node–only functions](c_SQL_functions_leader_node_only.md). STV\_INFLIGHT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Troubleshooting with STV\_INFLIGHT
<a name="r_STV_INFLIGHT_troubleshooting"></a>

If you use STV\_INFLIGHT to troubleshoot performance for a query, or a collection of queries, note the following:
+ Long-running open transactions generally increase load. These open transactions can result in longer running times for other queries.
+ Long-running COPY and ETL jobs can affect other queries running on the cluster, if they're taking a lot of compute resources. In most cases, moving these long-running jobs to times of low use increases performance for reporting or analytics workloads.
+ There are views that provide related information to STV\_INFLIGHT. These include [STL\_QUERYTEXT](r_STL_QUERYTEXT.md), which captures the query text for SQL commands, and [SVV\_QUERY\_INFLIGHT](r_SVV_QUERY_INFLIGHT.md), which joins STV\_INFLIGHT to STL\_QUERYTEXT. You can also use [STV\_RECENTS](r_STV_RECENTS.md) with STV\_INFLIGHT for troubleshooting. For example, STV\_RECENTS can indicate if specific queries are in a *Running* or *Done* state. Combining this information with results from STV\_INFLIGHT can give you more information about a query's properties and compute-resource impact. 

You can also monitor running queries using the Amazon Redshift console.

## Table columns
<a name="r_STV_INFLIGHT-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid  | integer  | ID of user who generated entry.  | 
| slice  | integer  | Slice where the query is running.  | 
| query  | integer  | Query ID. Can be used to join various other system tables and views.  | 
| label  | character(320)  |  Either the name of the file used to run the query or a label defined with a SET QUERY\_GROUP command. If the query is not file-based or the QUERY\_GROUP parameter is not set, this field is blank.  | 
| xid  | bigint  | Transaction ID.  | 
| pid  | integer  | Process ID. All of the queries in a session are run in the same process, so this value remains constant if you run a series of queries in the same session. You can use this column to join to the [STL\_ERROR](r_STL_ERROR.md) table.  | 
| starttime  | timestamp  | Time that the query started.  | 
| text  | character(100)  | Query text, truncated to 100 characters if the statement exceeds that limit.  | 
| suspended  | integer  | Whether the query is suspended or not. 0 = false; 1 = true.  | 
| insert\_pristine  | integer  | Whether write queries are/were able to run while the current query is/was running. 1 = no write queries allowed. 0 = write queries allowed. This column is intended for use in debugging.  | 
| concurrency\_scaling\_status | integer  | Indicates whether the query ran on the main cluster or on a concurrency scaling cluster, Possible values are as follows: <br />0 - Ran on the main cluster <br />1 - Ran on a concurrency scaling cluster  | 

## Sample queries
<a name="r_STV_INFLIGHT-sample-queries"></a>

To view all active queries currently running on the database, type the following query: 

```
select * from stv_inflight;
```

The sample output below shows two queries currently running, including the STV\_INFLIGHT query itself and a query that was run from a script called `avgwait.sql`: 

```
select slice, query, trim(label) querylabel, pid,
starttime, substring(text,1,20) querytext
from stv_inflight;

slice|query|querylabel | pid |        starttime         |      querytext
-----+-----+-----------+-----+--------------------------+--------------------
1011 |  21 |           | 646 |2012-01-26 13:23:15.645503|select slice, query,
1011 |  20 |avgwait.sql| 499 |2012-01-26 13:23:14.159912|select avg(datediff(
(2 rows)
```

The following query selects several columns, including concurrency\_scaling\_status. This column indicates whether queries are being sent to the concurrency-scaling cluster. If the value is `1` for some results, it's an indication that concurrency-scaling compute resources are being used. For more information, see [Concurrency scaling](concurrency-scaling.md).

```
select userid, 
query,
pid,
starttime,
text,
suspended,
concurrency_scaling_status
 from STV_INFLIGHT;
```

The sample output shows one query being sent to the concurrency scaling cluster.

```
 query  | pid     |        starttime           |   text                 | suspended     |  concurrency_scaling_status
--------+---------+----------------------------|------------------------|---------------|-------------------------------
1234567 | 123456  | 2012-01-26 13:23:15.645503 | select userid, query...  0                1
2345678 | 234567  | 2012-01-26 13:23:14.159912 | select avg(datediff(...  0                0
(2 rows)
```

For more tips on troubleshooting query performance, see [Query troubleshooting](queries-troubleshooting.md).