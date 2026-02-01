Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LAST_USER_QUERY_ID

Returns the query ID of the most recently completed user query in the current session. If
no queries have been run in the current session, last_user_query_id returns -1. The function
does not return the query ID for queries that run exclusively on the
leader node. For more information, see [Leader node–only
functions](c_SQL_functions_leader_node_only.md "c_SQL_functions_leader_node_only.md").

## Syntax

```
last_user_query_id()
```

## Return type

Returns an integer.

## Example

The following query returns the ID of the latest query run by a user completed in the current
session.

```
select last_user_query_id();

```

Results are the following.

```
last_user_query_id
-----------------------
    5437
(1 row)

```

The following query returns the query ID and text of the most recently completed
query run by a user in the current session.

```
select query_id, query_text from sys_query_history where query_id = last_user_query_id();
```

Results are the following.

```
 query_id, query_text
---------+-------------------------------------------------------------------------------------------------------------
 5556975 | select last_user_query_id() limit 100 --RequestID=<unique request ID>; TraceID=<unique trace ID>
```
