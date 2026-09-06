

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_RECENTS
<a name="r_STV_RECENTS"></a>

Use the STV\_RECENTS table to find out information about the currently active and recently run queries against a database. 

STV\_RECENTS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data). 

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Troubleshooting with STV\_RECENTS
<a name="r_STV_RECENTS_troubleshooting"></a>

STV\_RECENTS is particularly helpful for determining if a query or collection of queries is currently running or done. It also shows the duration a query has been running. This is helpful for getting a sense for which queries are long running.

You can join STV\_RECENTS to other system views, such as [STV\_INFLIGHT](r_STV_INFLIGHT.md), to gather additional metadata about running queries. (There's an example that shows how to do this in the sample queries section.) You can also use returned records from this view along with the monitoring features in the Amazon Redshift console for troubleshooting in real time.

System views that compliment STV\_RECENTS include [STL\_QUERYTEXT](r_STL_QUERYTEXT.md), which retrieves the query text for SQL commands, and [SVV\_QUERY\_INFLIGHT](r_SVV_QUERY_INFLIGHT.md), which joins STV\_INFLIGHT to STL\_QUERYTEXT.

## Table columns
<a name="r_STV_RECENTS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid  | integer  | ID of user who generated entry.  | 
| status  | character(20)  | Query status. Valid values are Running, Done.  | 
| starttime  | timestamp  | Time that the query started.  | 
| duration  | integer  | Number of microseconds since the session started.  | 
| user\_name  | character(50)  | User name who ran the process.  | 
| db\_name  | character(50)  | Name of the database.  | 
| query  | character(600)  | Query text, up to 600 characters. Any additional characters are truncated. | 
| pid  | integer  | Process ID for the session associated with the query, which is always -1 for queries that have completed.  | 

## Sample queries
<a name="r_STV_RECENTS-sample-queries"></a>

To determine which queries are currently running against the database, run the following query:

```
select user_name, db_name, pid, query
from stv_recents
where status = 'Running';
```

The sample output below shows a single query running on the TICKIT database: 

```
user_name | db_name |   pid   | query   
----------+---------+---------+-------------
dwuser    | tickit  |  19996  |select venuename, venueseats from 
venue where venueseats > 50000 order by venueseats desc;
```

The following example returns a list of queries (if any) that are running or waiting in a queue to run: 

```
select * from stv_recents where status<>'Done';

status |    starttime        | duration |user_name|db_name| query     | pid
-------+---------------------+----------+---------+-------+-----------+------
Running| 2010-04-21 16:11... | 281566454| dwuser  |tickit | select ...| 23347
```

This query does not return results unless you are running a number of concurrent queries and some of those queries are in a queue.

The following example extends the previous example. In this case, queries that are truly "in flight" (running, not waiting) are excluded from the result: 

```
select * from stv_recents where status<>'Done'
and pid not in (select pid from stv_inflight);
...
```

For more tips on troubleshooting query performance, see [Query troubleshooting](queries-troubleshooting.md).