Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_FEDERATED_QUERY

Use the SVL_FEDERATED_QUERY view to view information about a federated query
call.

SVL_FEDERATED_QUERY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_EXTERNAL_QUERY_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type        | Description                                                                                                                                           |
| ----------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer          | The ID of the user running the query.                                                                                                                 |
| xid         | bigint           | The transaction ID.                                                                                                                                   |
| pid         | integer          | The ID of the leader process running the query.                                                                                                       |
| query       | integer          | The query ID of a federated call.                                                                                                                     |
| sourcetype  | character (32)   | The federated call source type, for example "PG".                                                                                                     |
| recordtime  | timestamp        | The time when a query is sent for federation. UTC is used.                                                                                            |
| querytext   | character (4000) | The query string sent to the remote PostgreSQL engine for execution.                                                                                  |
| num_rows    | bigint           | The number of rows returned by the federated query.                                                                                                   |
| num_bytes   | bigint           | The number of bytes returned by the federated query.                                                                                                  |
| duration    | bigint           | The time (microseconds) spent fetching rows from cursor calls.<br>It is the time spent running the federated query, as well as, getting results back. |

## Sample queries

To show information about federated query calls, run the following query.

```
select query, trim(sourcetype) as type, recordtime, trim(querytext) as "PG Subquery" from svl_federated_query where query = 4292;

 query | type |         recordtime         |                          pg subquery
-------+------+----------------------------+---------------------------------------------------------------
  4292 | PG   | 2020-03-27 04:29:58.485126 | SELECT "level" FROM functional.employees WHERE ("level" >= 6)
(1 row)
```
