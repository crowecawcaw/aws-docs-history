Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_QUERY

Returns execution information about a database query.

###### Note

The STL_QUERY and STL_QUERYTEXT views only contain information about queries, not
other utility and DDL commands. For a listing and information on all statements
run by Amazon Redshift, you can also query the STL_DDLTEXT and STL_UTILITYTEXT views.
For a complete listing of all statements run by Amazon Redshift, you can query the
SVL_STATEMENTTEXT view.

STL_QUERY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

Note that when your query text length is over 4000 characters, STL_QUERY only
displays truncated data. To get the full query text, you can use UNION on the query text
across rows.

###### Note

To verify whether a transaction containing the executed query was successfully
committed, you need to perform a join operation between system tables and the
`sys_transaction_history` table. For example:

```
SELECT
    stlq.xid AS transaction_id,
    stlq.query AS query_id,
    TRIM(stlq.querytxt) AS query_text,
    th.status AS transaction_status
FROM
    stl_query stlq
LEFT JOIN
    sys_transaction_history th ON stlq.xid = th.transaction_id;
```

## Table columns

| Column name                | Data type       | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                     | integer         | ID of the user who generated the entry.                                                                                                                                                                                                                                                                                                                                                                           |
| query                      | integer         | Query ID. The query column can be used to join other system tables and views.                                                                                                                                                                                                                                                                                                                                     |
| label                      | character(320)  | Either the name of the file used to run the query<br>or a label defined with a SET QUERY_GROUP command. If the query is<br>not file-based or the QUERY_GROUP parameter is not set, this field<br>value is `default`.                                                                                                                                                                                              |
| xid                        | bigint          | Transaction ID.                                                                                                                                                                                                                                                                                                                                                                                                   |
| pid                        | integer         | Process ID. Normally, all of the queries in a<br>session are run in the same process, so this value usually remains<br>constant if you run a series of queries in the same session.<br>Following certain internal events, Amazon Redshift might restart an active<br>session and assign a new PID. For more information, see [STL_RESTARTED_SESSIONS](r_STL_RESTARTED_SESSIONS.md "r_STL_RESTARTED_SESSIONS.md"). |
| database                   | character(32)   | The name of the database the user was connected to<br>when the query was issued.                                                                                                                                                                                                                                                                                                                                  |
| querytxt                   | character(4000) | Actual query text for the query.                                                                                                                                                                                                                                                                                                                                                                                  |
| starttime                  | timestamp       | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.                                                                                                                                                                                                                                      |
| endtime                    | timestamp       | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.                                                                                                                                                                                                                                     |
| aborted                    | integer         | If a query was stopped by the system or canceled<br>by the user, this column contains `1`. If the<br>query ran to completion (including returning results to the client),<br>this column contains `0`. If a client<br>disconnects before receiving the results, the query will be marked<br>as canceled (`1`), even if it completed<br>successfully in the backend.                                               |
| insert_pristine            | integer         | Whether write queries are/were able to run while<br>the current query is/was running. 1 = no write queries allowed. 0 =<br>write queries allowed. This column is intended for use in debugging.                                                                                                                                                                                                                   |
| concurrency_scaling_status | integer         | Indicates whether the query ran on the main<br>cluster or on a concurrency scaling cluster.<br>Possible values are as follows:<br>0<br>• Ran on the main cluster<br>1<br>• Ran on a concurrency scaling cluster<br>Greater than 1<br>• Ran on the main cluster                                                                                                                                                    |

## Sample queries

The following query lists the five most recent queries.

```
select query, trim(querytxt) as sqlquery
from stl_query
order by query desc limit 5;

query |                                   sqlquery
------+--------------------------------------------------
129 | select query, trim(querytxt) from stl_query order by query;
128 | select node from stv_disk_read_speeds;
127 | select system_status from stv_gui_status
126 | select * from systable_topology order by slice
125 | load global dict registry
(5 rows)
```

The following query returns the time elapsed in descending order for queries that
ran on February 15, 2013.

```
select query, datediff(seconds, starttime, endtime),
trim(querytxt) as sqlquery
from stl_query
where starttime >= '2013-02-15 00:00' and endtime < '2013-02-16 00:00'
order by date_diff desc;

 query | date_diff |  sqlquery
-------+-----------+-------------------------------------------
 55    |       119 | padb_fetch_sample: select count(*) from category
121    |         9 | select * from svl_query_summary;
181    |         6 | select * from svl_query_summary where query in(179,178);
172    |         5 | select * from svl_query_summary where query=148;
...
(189 rows)
```

The following query shows the queue time and execution time for queries. Queries
with `concurrency_scaling_status = 1` ran on a concurrency scaling cluster. All other
queries ran on the main cluster.

```
SELECT w.service_class AS queue
     , q.concurrency_scaling_status
     , COUNT( * ) AS queries
     , SUM( q.aborted )  AS aborted
     , SUM( ROUND( total_queue_time::NUMERIC / 1000000,2 ) ) AS queue_secs
     , SUM( ROUND( total_exec_time::NUMERIC / 1000000,2 ) )  AS exec_secs
FROM stl_query q
     JOIN stl_wlm_query w
          USING (userid,query)
WHERE q.userid > 1
  AND service_class > 5
  AND q.starttime > '2019-03-01 16:38:00'
  AND q.endtime   < '2019-03-01 17:40:00'
GROUP BY 1,2
ORDER BY 1,2;
```
