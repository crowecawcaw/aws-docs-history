# Transaction timeout in Amazon Aurora MySQL

The `aurora_transaction_timeout` parameter sets the maximum duration for a
transaction. This parameter can help prevent long-running transactions (active or idle)
from blocking [InnoDB purge](https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_purge "https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_purge"), which can lead to performance issues. This parameter is
available in Aurora MySQL version 8.4.8 and higher.

###### Topics

- [Parameter details](#AuroraMySQL.TransactionTimeout.parameter-details "#AuroraMySQL.TransactionTimeout.parameter-details")
- [Timeout behavior](#AuroraMySQL.TransactionTimeout.behavior "#AuroraMySQL.TransactionTimeout.behavior")
- [Examples](#AuroraMySQL.TransactionTimeout.examples "#AuroraMySQL.TransactionTimeout.examples")
- [Key notes](#AuroraMySQL.TransactionTimeout.key-notes "#AuroraMySQL.TransactionTimeout.key-notes")
- [Client error](#AuroraMySQL.TransactionTimeout.client-error "#AuroraMySQL.TransactionTimeout.client-error")
- [Error log](#AuroraMySQL.TransactionTimeout.error-log "#AuroraMySQL.TransactionTimeout.error-log")
- [Monitoring transaction timeouts](#AuroraMySQL.TransactionTimeout.monitoring "#AuroraMySQL.TransactionTimeout.monitoring")
- [Interaction with other timeouts](#AuroraMySQL.TransactionTimeout.interaction "#AuroraMySQL.TransactionTimeout.interaction")

## Parameter details

The `aurora_transaction_timeout` parameter terminates any InnoDB
transaction that spans longer than the specified duration, including read-only
transactions. You specify the value in seconds. A value of zero (the default)
disables the timeout.

The following table summarizes the parameter details.

| Property | Value                                        |
| -------- | -------------------------------------------- |
| Name     | `aurora_transaction_timeout`                 |
| Scope    | Session, Global                              |
| Default  | 0 (disabled)                                 |
| Unit     | Seconds                                      |
| Dynamic  | Yes, applies to new InnoDB transactions only |

You can set the `aurora_transaction_timeout` parameter at the cluster,
instance, or session level. For more information about working with parameter groups,
see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Timeout behavior

The `aurora_transaction_timeout` parameter applies to InnoDB transactions
that execute DML statements, including read-only transactions. All [implicit commit
statements](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html "https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html"), except `CREATE TABLE .. AS SELECT` (CTAS) and
`LOAD DATA`, are excluded from the timeout. The timeout value is
captured when the first InnoDB statement runs. The value remains fixed for the
lifetime of that transaction.

When the timeout expires, the outcome depends on the transaction state:

- If there is an active query in the transaction, the query is interrupted
  and the transaction is rolled back. The connection remains usable.
- If there is no active query (that is, the transaction is idle), the
  connection is terminated.

## Examples

The following examples show when the timer starts for different transaction
scenarios.

### Explicit transaction

```
BEGIN;                    -- Does NOT start InnoDB transaction. No timer.
SELECT * FROM t1;         -- Starts InnoDB transaction. Timer starts HERE (at statement 2).
```

The timer starts at statement 2 (the first InnoDB statement).

### autocommit=0

```
SET SESSION autocommit=0;  -- No transaction yet
SELECT * FROM t1;          -- Starts InnoDB transaction. Timer starts HERE.
INSERT INTO t1 ...;        -- Same transaction, timer still running from step 2.
```

The timer starts at statement 2 (the first InnoDB statement after autocommit
is disabled).

### Stored procedures

A stored procedure runs within the caller's transaction context. If the caller
already has an active InnoDB transaction, the timer was already started before
the procedure call. If the procedure is the first thing to touch InnoDB, the
timer starts at the first InnoDB statement inside the procedure.

```
BEGIN;
CALL my_proc();  -- If my_proc() does SELECT/INSERT, timer starts at that first InnoDB statement inside the proc
```

## Key notes

- **Timeout is captured at transaction start**
  – The timeout value is captured when the first InnoDB statement
  executes. Changing `aurora_transaction_timeout` in the middle of a
  transaction takes effect on the next transaction, not the current one. No
  warning is raised.
- **XA PREPARED transactions are excluded**
  – Prepared transactions are not subject to
  `aurora_transaction_timeout`.
- **Write forwarding sessions are not subject to
  transaction timeout** – When write forwarding is enabled,
  any statement or transaction that contains a forwarded statement is not subject
  to `aurora_transaction_timeout`. Subsequent transactions on the
  same session that do not include forwarded statements are subject to timeout
  as normal. To control idle timeout for forwarded transactions, you can use the
  `aurora_fwd_writer_idle_timeout` parameter. For more
  information, see [Configuration parameters for write forwarding in Aurora MySQL](aurora-global-database-write-forwarding-ams.md#aurora-global-database-write-forwarding-params-ams "aurora-global-database-write-forwarding-ams.md#aurora-global-database-write-forwarding-params-ams").
- **Use caution with high timeout values**
  – When a long-running transaction is rolled back, the rollback
  can take several times longer than the original data change operations.
  Killing the database process does not help because the rollback restarts
  on server startup. Choose a timeout value that balances your workload
  needs against rollback cost. For more information, see [Optimizing InnoDB Transaction Management](https://dev.mysql.com/doc/refman/8.4/en/optimizing-innodb-transaction-management.html "https://dev.mysql.com/doc/refman/8.4/en/optimizing-innodb-transaction-management.html") in the MySQL
  documentation.

## Client error

When a transaction with an active query exceeds the timeout, the client receives
the following error:

```
ERROR 63952 (40001): Transaction exceeded maximum allowed duration of <N> seconds and was rolled back. See aurora_transaction_timeout for configuring this behavior.
```

When an idle transaction exceeds the timeout, the subsequent query receives the
same error as the MySQL "server gone away" error. For more information, see [MySQL server has
gone away](https://dev.mysql.com/doc/refman/8.4/en/gone-away.html "https://dev.mysql.com/doc/refman/8.4/en/gone-away.html") in the MySQL documentation.

## Error log

An informational message is written to the database error log when a transaction
timeout occurs:

```
[Note] Transaction breached timeout threshold and will be rolled back, if still in progress. If idle, the connection will be aborted. Check response for confirmation. connection_id: 4821, trx_id: 28193, user: app_user, timeout: 5 seconds, duration: 7 seconds
```

###### Note

This log message is for diagnostic purposes only. Rely on the client response
as the definitive indicator of a timed-out transaction.

## Monitoring transaction timeouts

Use the `Aurora_transaction_timeouts` status variable to track how many
transactions have timed out since the DB instance restarted.

```
SHOW GLOBAL STATUS LIKE 'Aurora_transaction_timeouts';
```

When `performance_schema` is enabled, the timeout error
(`ER_AURORA_TRANSACTION_TIMEOUT_ERROR`) is also tracked in
`performance_schema.events_errors_summary_global_by_error` and related
tables. Note that only active transaction timeouts increment this counter; idle
transaction timeouts terminate the connection without raising the
`ER_AURORA_TRANSACTION_TIMEOUT_ERROR` error.

## Interaction with other timeouts

The `aurora_transaction_timeout` works alongside existing timeout
parameters. If a transaction remains open longer than the configured
`aurora_transaction_timeout`, it is terminated regardless of other
timeout settings. Whether other timeouts also roll back the transaction depends on
their own implementation. For details on these parameters, see the MySQL
documentation.
