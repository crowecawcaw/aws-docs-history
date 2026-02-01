Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_PROCEDURE_CALL

Use the SYS_PROCEDURE_CALL view to get information about stored procedure calls,
including start time, end time, status of a stored procedure call, and call hierarchy
for nested stored procedure calls. Each stored procedure call receives a query
ID.

SYS_PROCEDURE_CALL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name               | Data type  | Description                                                                                                                                                                                                                                                         |
| ------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| session_user_id           | integer    | The identifier of the user who created the session<br>and is the invoker of the top-level stored procedure call.                                                                                                                                                    |
| security_user_id          | integer    | The identifier of the user whose privileges were<br>used to run the statement within the stored procedure. If the stored<br>procedure was called from the outer DEFINER stored procedure, then<br>this will be the owner user_id of that outer stored<br>procedure. |
| query_id                  | integer    | The query identifier of the stored procedure<br>call.                                                                                                                                                                                                               |
| query_text                | char(4000) | The text of the stored procedure call<br>query.                                                                                                                                                                                                                     |
| start_time                | timestamp  | The time in UTC when the query started running.<br>The timestamp uses six digits of precision for fractional seconds,<br>for example. 2009-06-12 11:29:19.131358.                                                                                                   |
| end_time                  | timestamp  | The time in UTC when the query finished running.<br>The timestamp uses six digits of precision for fractional seconds,<br>for example: 2009-06-12 11:29:19.131358.                                                                                                  |
| status                    | char(10)   | The status of the stored procedure call. When the<br>stored procedure was stopped by the system or canceled by the user,<br>the value is canceled. If the stored procedure call runs to<br>completion, the value is success.                                        |
| caller_procedure_query_id | integer    | If the stored procedure call was invoked by<br>another stored procedure call, then this column contains the query<br>ID of the outer call. Otherwise, the field is NULL.                                                                                            |

## Sample queries

The following query returns a nested stored procedure call hierarchy.

```
select query_id, datediff(seconds, start_time, end_time) as elapsed_time, status, trim(query_text) as call, caller_procedure_query_id from sys_procedure_call;
```

Sample output.

```
 query_id | elapsed_time | status  |                       call                       | caller_procedure_query_id
----------+--------------+---------+--------------------------------------------------+---------------------------
     3087 |           18 | success | CALL proc_bd906c98c45443ffa165e9552056902d(1)    |          3085
     3085 |           18 | success | CALL proc_bd906c98c45443ffa165e9552056902d_2(1); |
(2 rows)
```
