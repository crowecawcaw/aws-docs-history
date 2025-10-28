Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CANCEL

Cancels a database query that is currently running.

The CANCEL command requires the process ID or session ID of the running query and
displays a confirmation message to verify that the query was canceled.

## Required privileges

Following are required privileges for CANCEL:

- Superuser canceling their own query
- Superuser canceling a user's query
- Users with the CANCEL privilege canceling a user's query
- User canceling their own query

## Syntax

```
CANCEL *process\_id* [ '*message*' ]
```

## Parameters

_process_id_

To cancel a query running in an Amazon Redshift cluster, use the `pid`
(Process ID) from [STV_RECENTS](r_STV_RECENTS.md "r_STV_RECENTS.md")
that corresponds to the query that you want to cancel.

To cancel a query running in an Amazon Redshift Serverless workgroup, use the
`session_id` from [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md") that corresponds to the query that you
want to cancel.

'_message_'

An optional confirmation message that displays when the query cancellation
completes. If you don't specify a message, Amazon Redshift displays the default
message as verification. You must enclose the message in single quotation
marks.

## Usage notes

You can't cancel a query by specifying a _query ID_; you must
specify the query's _process ID_ (PID) or _Session
ID_. You can only cancel queries currently being run by your user.
Superusers can cancel all queries.

If queries in multiple sessions hold locks on the same table, you can use the [PG_TERMINATE_BACKEND](PG_TERMINATE_BACKEND.md "PG_TERMINATE_BACKEND.md") function to
terminate one of the sessions. Doing this forces any currently running transactions in
the terminated session to release all locks and roll back the transaction. To view
currently held locks, query the [STV_LOCKS](r_STV_LOCKS.md "r_STV_LOCKS.md") system table.

Following certain internal events, Amazon Redshift might restart an active session and assign a
new PID. If the PID has changed, you might receive the following error message.

```
Session <PID> does not exist. The session PID might have changed. Check the stl_restarted_sessions system table for details.
```

To find the new PID, query the [STL_RESTARTED_SESSIONS](r_STL_RESTARTED_SESSIONS.md "r_STL_RESTARTED_SESSIONS.md") system table and filter on the
`oldpid` column.

```
select oldpid, newpid from stl_restarted_sessions where oldpid = 1234;
```

## Examples

To cancel a currently running query in a Amazon Redshift cluster, first retrieve the process ID
for the query that you want to cancel. To determine the process IDs for all currently
running queries, type the following command:

```
select pid, starttime, duration,
trim(user_name) as user,
trim (query) as querytxt
from stv_recents
where status = 'Running';

pid |         starttime          | duration |   user   |    querytxt
-----+----------------------------+----------+----------+-----------------
802 | 2008-10-14 09:19:03.550885 |      132 | dwuser | select
venuename from venue where venuestate='FL', where venuecity not in
('Miami' , 'Orlando');
834 | 2008-10-14 08:33:49.473585 |  1250414 | dwuser | select *
from listing;
964 | 2008-10-14 08:30:43.290527 |   326179 | dwuser | select
sellerid from sales where qtysold in (8, 10);
```

Check the query text to determine which process id (PID) corresponds to the query
that you want to cancel.

Type the following command to use PID 802 to cancel that query:

```
cancel 802;

```

The session where the query was running displays the following message:

```
ERROR:  Query (168) cancelled on user's request
```

where `168` is the query ID (not the process ID used to cancel the
query).

Alternatively, you can specify a custom confirmation message to display instead of
the default message. To specify a custom message, include your message in single
quotation marks at the end of the CANCEL command:

```
cancel 802 'Long-running query';

```

The session where the query was running displays the following message:

```
ERROR:  Long-running query
```
