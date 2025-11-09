Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_QLOG

The SVL_QLOG view contains a log of all queries run against the database.

Amazon Redshift creates the SVL_QLOG view as a readable subset of information from the [STL_QUERY](r_STL_QUERY.md "r_STL_QUERY.md") table. Use this table to find
the query ID for a recently run query or to see how long it took a query to
complete.

SVL_QLOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name                    | Data type      | Description                                                                                                                                                                                                                                                                                     |
| ------------------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                         | integer        | ID of the user who generated the entry.                                                                                                                                                                                                                                                         |
| query                          | integer        | Query ID. You can use this ID to join various<br>other system tables and views.                                                                                                                                                                                                                 |
| xid                            | bigint         | Transaction ID.                                                                                                                                                                                                                                                                                 |
| pid                            | integer        | Process ID associated with the query.                                                                                                                                                                                                                                                           |
| starttime                      | timestamp      | Exact time when the statement started executing,<br>with six digits of precision for fractional seconds—for<br>example: `2009-06-12 11:29:19.131358`                                                                                                                                            |
| endtime                        | timestamp      | Exact time when the statement finished executing,<br>with six digits of precision for fractional seconds—for<br>example: `2009-06-12 11:29:19.193640`                                                                                                                                           |
| elapsed                        | bigint         | Length of time that it took the query to run<br>(in microseconds).                                                                                                                                                                                                                              |
| aborted                        | integer        | If a query was stopped by the system or canceled<br>by the user, this column contains `1`. If the<br>query ran to completion, this column contains<br>`0`. Queries that are canceled for workload<br>management purposes and subsequently restarted also have a value of<br>`1` in this column. |
| label                          | character(320) | Either the name of the file used to run the query,<br>or a label defined with a SET QUERY_GROUP command. If the query is<br>not file-based or the QUERY_GROUP parameter is not set, this field<br>value is `default`.                                                                           |
| substring                      | character(60)  | Truncated query text.                                                                                                                                                                                                                                                                           |
| source_query                   | integer        | If the query used result caching, the query ID of<br>the query that was the source of the cached results. If result<br>caching was not used, this field value is `NULL`.                                                                                                                        |
| concurrency_scaling_status_txt | text           | A description of whether the query ran on the main cluster or concurrency scaling cluster.                                                                                                                                                                                                      |
| from_sp_call                   | integer        | If the query was called from a stored procedure,<br>the query ID of the procedure call. If the query wasn't run as<br>part of a stored procedure, this field is `NULL`.                                                                                                                         |

## Sample queries

The following example returns the query ID, execution time, and truncated query
text for the five most recent database queries run by the user with
`userid = 100`.

```
select query, pid, elapsed, substring from svl_qlog
where userid = 100
order by starttime desc
limit 5;

 query  |  pid  | elapsed  |           substring
--------+-------+----------+-----------------------------------------------
 187752 | 18921 | 18465685 | select query, elapsed, substring from svl_...
 204168 |  5117 |    59603 | insert into testtable values (100);
 187561 | 17046 |  1003052 | select * from pg_table_def where tablename...
 187549 | 17046 |  1108584 | select * from STV_WLM_SERVICE_CLASS_CONFIG
 187468 | 17046 |  5670661 | select * from pg_table_def where schemaname...
(5 rows)

```

The following example returns the SQL script name (LABEL column) and elapsed time
for a query that was cancelled (`aborted=1`):

```
select query, elapsed, trim(label) querylabel
from svl_qlog where aborted=1;

 query | elapsed  |       querylabel
-------+----------+-------------------------
    16 |  6935292 | alltickittablesjoin.sql
(1 row)
```
