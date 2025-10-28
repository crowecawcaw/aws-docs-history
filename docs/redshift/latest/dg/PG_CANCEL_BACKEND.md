Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_CANCEL_BACKEND

Cancels a query. PG_CANCEL_BACKEND is functionally equivalent to the [CANCEL](r_CANCEL.md "r_CANCEL.md") command. You can cancel queries
currently being run by your user. Superusers can cancel any query.

## Syntax

```
pg_cancel_backend( *pid* )
```

## Arguments

_pid_

The process ID (PID) of the query to be canceled. You cannot cancel a
query by specifying a query ID; you must specify the query's process ID.
Requires an `INTEGER` value.

## Return type

None

## Usage notes

If queries in multiple sessions hold locks on the same table, you can use the
[PG_TERMINATE_BACKEND](PG_TERMINATE_BACKEND.md "PG_TERMINATE_BACKEND.md")
function to terminate one of the sessions, which forces any currently running
transactions in the terminated session to release all locks and roll back the
transaction. Query the PG\_\_LOCKS catalog table to view currently held locks. If you
cannot cancel a query because it is in transaction block (BEGIN … END), you can
terminate the session in which the query is running by using the PG_TERMINATE_BACKEND
function.

## Examples

To cancel a currently running query, first retrieve the process ID for the query
that you want to cancel. To determine the process IDs for all currently running
queries, run the following command.

````
`SELECT pid, TRIM(starttime) AS start,
duration, TRIM(user_name) AS user,
SUBSTRING(query,1,40) AS querytxt
FROM stv_recents
WHERE status = 'Running';`

`+-----+------------------------+----------+--------+-----------------------------+
| pid | starttime | duration | user | querytxt | +-----+------------------------+----------+--------+-----------------------------+
| 802 | 2013-10-14 09:19:03.55 | 132 | dwuser | select venuename from venue |
| 834 | 2013-10-14 08:33:49.47 | 1250414 | dwuser | select * from listing; |
| 964 | 2013-10-14 08:30:43.29 | 326179 | dwuser | select sellerid from sales | +-----+------------------------+----------+--------+-----------------------------+` ``` To cancel the query with process ID 802, use the following example. ``` `SELECT PG_CANCEL_BACKEND(802);` ```
````
