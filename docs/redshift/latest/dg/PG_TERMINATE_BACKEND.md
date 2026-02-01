Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_TERMINATE_BACKEND

Terminates a session. You can terminate a session owned by your user. A superuser can
terminate any session.

## Syntax

```
pg_terminate_backend( *pid* )
```

## Arguments

_pid_

The process ID of the session to be terminated. Requires an `INTEGER`
value.

## Return type

None

## Usage notes

If you are close to reaching the limit for concurrent connections, use
PG_TERMINATE_BACKEND to terminate idle sessions and free up the connections. For more
information, see [Limits in
Amazon Redshift](../mgmt/amazon-redshift-limits.md "../mgmt/amazon-redshift-limits.md").

If queries in multiple sessions hold locks on the same table, you can use
PG_TERMINATE_BACKEND to terminate one of the sessions, which forces any currently
running transactions in the terminated session to release all locks and roll back the
transaction. Query the PG_LOCKS catalog table to view currently held locks.

If a query is not in a transaction block (BEGIN … END), you can cancel the query
by using the [CANCEL](r_CANCEL.md "r_CANCEL.md") command or the [PG_CANCEL_BACKEND](PG_CANCEL_BACKEND.md "PG_CANCEL_BACKEND.md") function.

## Examples

To query the SVV_TRANSACTIONS table to view all locks in
effect for current transactions, use the following example.

```
`SELECT * FROM svv_transactions;`

`+-----------+--------+-------+------+---------------------+-----------------+----------------------+----------+---------+
| txn_owner | txn_db | xid | pid | txn_start | lock_mode | lockable_object_type | relation | granted |
+-----------+--------+-------+------+---------------------+-----------------+----------------------+----------+---------+
| rsuser | dev | 96178 | 8585 | 2017-04-12 20:13:07 | AccessShareLock | relation | 51940 | true |
| rsuser | dev | 96178 | 8585 | 2017-04-12 20:13:07 | AccessShareLock | relation | 52000 | true |
| rsuser | dev | 96178 | 8585 | 2017-04-12 20:13:07 | AccessShareLock | relation | 108623 | true |
| rsuser | dev | 96178 | 8585 | 2017-04-12 20:13:07 | ExclusiveLock | transactionid | | true |
+-----------+--------+-------+------+---------------------+-----------------+----------------------+----------+---------+`
```

TO terminate the session holding the locks, use the following example.

```
`SELECT PG_TERMINATE_BACKEND(8585);`
```
