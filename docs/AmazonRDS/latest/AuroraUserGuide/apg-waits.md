# Lock:transactionid

The `Lock:transactionid` event occurs when a transaction is waiting for a row-level lock.

###### Topics

- [Supported engine versions](#apg-waits.locktransactionid.context.supported "#apg-waits.locktransactionid.context.supported")
- [Context](#apg-waits.locktransactionid.context "#apg-waits.locktransactionid.context")
- [Likely causes of increased waits](#apg-waits.locktransactionid.causes "#apg-waits.locktransactionid.causes")
- [Actions](#apg-waits.locktransactionid.actions "#apg-waits.locktransactionid.actions")

## Supported engine versions

This wait event information is supported for all versions of Aurora PostgreSQL.

## Context

The event `Lock:transactionid` occurs when a transaction is trying
to acquire a row-level lock that has already been granted to a transaction that is
running at the same time. The session that shows the `Lock:transactionid`
wait event is blocked because of this lock. After the blocking transaction ends in
either a `COMMIT` or `ROLLBACK` statement, the blocked transaction
can proceed.

The multiversion concurrency control semantics of Aurora PostgreSQL guarantee that readers
don't block writers and writers don't block readers. For row-level conflicts to occur,
blocking and blocked transactions must issue conflicting statements of the following
types:

- `UPDATE`
- `SELECT … FOR UPDATE`
- `SELECT … FOR KEY SHARE`

The statement `SELECT … FOR KEY SHARE` is a special case. The database uses the clause `FOR KEY
 SHARE` to optimize the performance of referential integrity. A row-level lock on a row can block
`INSERT`, `UPDATE`, and `DELETE` commands on other tables that reference the
row.

## Likely causes of increased waits

When this event appears more than normal, the cause is typically `UPDATE`, `SELECT …
 FOR UPDATE`, or `SELECT … FOR KEY SHARE` statements combined with the following
conditions.

###### Topics

- [High concurrency](#apg-waits.locktransactionid.concurrency "#apg-waits.locktransactionid.concurrency")
- [Idle in transaction](#apg-waits.locktransactionid.idle "#apg-waits.locktransactionid.idle")
- [Long-running transactions](#apg-waits.locktransactionid.long-running "#apg-waits.locktransactionid.long-running")

### High concurrency

Aurora PostgreSQL can use granular row-level locking semantics. The probability of
row-level conflicts increases when the following conditions are met:

- A highly concurrent workload contends for the same rows.
- Concurrency increases.

### Idle in transaction

Sometimes the `pg_stat_activity.state` column shows the value
`idle in transaction`. This value appears for sessions that have
started a transaction, but haven't yet issued a `COMMIT` or
`ROLLBACK`. If the `pg_stat_activity.state` value isn't
`active`, the query shown in `pg_stat_activity` is the
most recent one to finish running. The blocking session isn't actively processing a
query because an open transaction is holding a lock.

If an idle transaction acquired a row-level lock, it might be preventing other
sessions from acquiring it. This condition leads to frequent occurrence of the wait
event `Lock:transactionid`. To diagnose the issue, examine the output
from `pg_stat_activity` and `pg_locks`.

### Long-running transactions

Transactions that run for a long time get locks for a long time. These long-held
locks can block other transactions from running.

## Actions

Row-locking is a conflict among `UPDATE`, `SELECT … FOR
 UPDATE`, or `SELECT … FOR KEY SHARE` statements. Before attempting
a solution, find out when these statements are running on the same row. Use this
information to choose a strategy described in the following sections.

###### Topics

- [Respond to high concurrency](#apg-waits.locktransactionid.actions.problem "#apg-waits.locktransactionid.actions.problem")
- [Respond to idle transactions](#apg-waits.locktransactionid.actions.find-blocker "#apg-waits.locktransactionid.actions.find-blocker")
- [Respond to long-running
  transactions](#apg-waits.locktransactionid.actions.concurrency "#apg-waits.locktransactionid.actions.concurrency")

### Respond to high concurrency

If concurrency is the issue, try one of the following techniques:

- Lower the concurrency in the application. For example, decrease the number of active
  sessions.
- Implement a connection pool. To learn how to pool connections with RDS Proxy, see [Amazon RDS Proxy for Aurora](rds-proxy.md "rds-proxy.md").
- Design the application or data model to avoid contending `UPDATE` and `SELECT … FOR
UPDATE` statements. You can also decrease the number of foreign keys accessed by
  `SELECT … FOR KEY SHARE` statements.

### Respond to idle transactions

If `pg_stat_activity.state` shows `idle in transaction`, use the following
strategies:

- Turn on autocommit wherever possible. This approach prevents transactions
  from blocking other transactions while waiting for a `COMMIT` or
  `ROLLBACK`.
- Search for code paths that are missing `COMMIT`, `ROLLBACK`, or
  `END`.
- Make sure that the exception handling logic in your application always has a path to a valid
  `end of transaction`.
- Make sure that your application processes query results after ending the transaction with
  `COMMIT` or `ROLLBACK`.

### Respond to long-running

transactions

If long-running transactions are causing the frequent occurrence of `Lock:transactionid`, try
the following strategies:

- Keep row locks out of long-running transactions.
- Limit the length of queries by implementing autocommit whenever possible.
