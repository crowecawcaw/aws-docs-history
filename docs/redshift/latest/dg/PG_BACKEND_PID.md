Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_BACKEND_PID

Returns the process ID (PID) of the server process handling the current
session.

###### Note

The PID is not globally unique. It can be reused over time.

## Syntax

```
pg_backend_pid()
```

## Return type

Returns an integer.

## Example

You can correlate PG_BACKEND_PID with log tables to retrieve information for the
current session. For example, the following query returns the query ID and a portion
of the query text for queries completed in the current session.

```
select query, substring(text,1,40)
from stl_querytext
where pid =  PG_BACKEND_PID()
order by query desc;

 query |                substring
-------+------------------------------------------
 14831 | select query, substring(text,1,40) from
 14827 | select query, substring(path,0,80) as pa
 14826 | copy category from 's3://dw-tickit/manif
 14825 | Count rows in target table
 14824 | unload ('select * from category') to 's3
(5 rows)
```

You can correlate PG_BACKEND_PID with the pid column in the following log tables
(exceptions are noted in parentheses):

- [STL_CONNECTION_LOG](r_STL_CONNECTION_LOG.md "r_STL_CONNECTION_LOG.md")
- [STL_DDLTEXT](r_STL_DDLTEXT.md "r_STL_DDLTEXT.md")
- [STL_ERROR](r_STL_ERROR.md "r_STL_ERROR.md")
- [STL_QUERY](r_STL_QUERY.md "r_STL_QUERY.md")
- [STL_QUERYTEXT](r_STL_QUERYTEXT.md "r_STL_QUERYTEXT.md")
- [STL_SESSIONS](r_STL_SESSIONS.md "r_STL_SESSIONS.md")
  (process)
- [STL_TR_CONFLICT](r_STL_TR_CONFLICT.md "r_STL_TR_CONFLICT.md")
- [STL_UTILITYTEXT](r_STL_UTILITYTEXT.md "r_STL_UTILITYTEXT.md")
- [STV_ACTIVE_CURSORS](r_STV_ACTIVE_CURSORS.md "r_STV_ACTIVE_CURSORS.md")
- [STV_INFLIGHT](r_STV_INFLIGHT.md "r_STV_INFLIGHT.md")
- [STV_LOCKS](r_STV_LOCKS.md "r_STV_LOCKS.md")
  (lock_owner_pid)
- [STV_RECENTS](r_STV_RECENTS.md "r_STV_RECENTS.md")
  (process_id)
