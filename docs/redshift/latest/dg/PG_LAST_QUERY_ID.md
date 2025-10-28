Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_LAST_QUERY_ID

Returns the query ID of the most recently completed query in the current session. If
no queries have been run in the current session, PG_LAST_QUERY_ID returns -1.
PG_LAST_QUERY_ID does not return the query ID for queries that run exclusively on the
leader node. For more information, see [Leader node–only
functions](c_SQL_functions_leader_node_only.md "c_SQL_functions_leader_node_only.md").

## Syntax

```
pg_last_query_id()
```

## Return type

Returns an integer.

## Example

The following query returns the ID of the latest query completed in the current
session.

```
select pg_last_query_id();

```

Results are the following.

```
pg_last_query_id
----------------
           5437
(1 row)

```

The following query returns the query ID and text of the most recently completed
query in the current session.

```
select query, trim(querytxt) as sqlquery
from stl_query
where query = pg_last_query_id();
```

Results are the following.

```
query | sqlquery
------+--------------------------------------------------
 5437 | select name, loadtime from stl_file_scan where loadtime > 1000000;
(1 rows)
```
