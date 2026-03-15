# Transaction isolation levels in Babelfish

Babelfish supports transaction isolation levels `READ UNCOMMITTED`, `READ COMMITTED` and `SNAPSHOT`. Starting from Babelfish 3.4 version
additional isolation levels `REPEATABLE READ` and `SERIALIZABLE` are supported. All the isolation levels in Babelfish are supported with
the behavior of corresponding isolation levels in PostgreSQL. SQL Server and Babelfish use different underlying mechanisms for implementing
transaction isolation levels (blocking for concurrent access, locks held by transactions, error handling etc). And, there are some subtle
differences in how concurrent access may work out for different workloads. For more information on this PostgreSQL behavior, see
[Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html "https://www.postgresql.org/docs/current/transaction-iso.html").

###### Topics

- [Overview of the transaction isolation levels](#babelfish-transaction.overview "#babelfish-transaction.overview")
- [Setting up the transaction isolation levels](#babelfish-transaction.setting "#babelfish-transaction.setting")
- [Enabling or disabling transaction isolation levels](#babelfish-transaction.enabling "#babelfish-transaction.enabling")
- [Comparing Babelfish and SQL Server isolation levels](babelfish-transaction.md "babelfish-transaction.md")

## Overview of the transaction isolation levels

The original SQL Server transaction isolation levels are based on pessimistic locking where only one copy of data
exists and queries must lock resources such as rows before accessing them. Later, a variation of the `READ COMMITTED`
isolation level was introduced. This enables the use of row versions to provide better concurrency between readers and
writers using non-blocking access. In addition, a new isolation level called `SNAPSHOT` is available. It also
uses row versions to provide better concurrency than `REPEATABLE READ` isolation level by avoiding shared locks on read data
that are held till the end of the transaction.

Unlike SQL Server, all transaction isolation levels in Babelfish are based on
optimistic Locking (MVCC). Each transaction sees a snapshot of the data either at the beginning of the statement
(`READ COMMITTED`) or at the beginning of the transaction (`REPEATABLE READ`, `SERIALIZABLE`), regardless of the current state of the
underlying data. Therefore, the execution behavior of concurrent transactions in Babelfish might differ from SQL Server.

For example, consider a transaction with isolation level `SERIALIZABLE` that is initially blocked in SQL Server but succeeds later.
It may end up failing in Babelfish due to a serialization conflict with a concurrent transaction that reads or updates the same rows. There
could also be cases where executing multiple concurrent transactions yields a different final result in Babelfish as compared to SQL Server.
Applications that use isolation levels, should be thoroughly tested for concurrency scenarios.

| Isolation levels in SQL Server | Babelfish isolation level | PostgreSQL isolation level | Comments                                                                                                         |
| ------------------------------ | ------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `READ UNCOMMITTED`             | `READ UNCOMMITTED`        | `READ UNCOMMITTED`         | `READ UNCOMMITTED` is same as `READ COMMITTED` in Babelfish or PostgreSQL                                        |
| `READ COMMITTED`               | `READ COMMITTED`          | `READ COMMITTED`           | SQL Server `READ COMMITTED` is pessimistic locking based, Babelfish `READ COMMITTED` is snapshot (MVCC) based.   |
| `READ COMMITTED SNAPSHOT`      | `READ COMMITTED`          | `READ COMMITTED`           | Both are snapshot (MVCC) based but not exactly same.                                                             |
| `SNAPSHOT`                     | `SNAPSHOT`                | `REPEATABLE READ`          | Exactly same.                                                                                                    |
| `REPEATABLE READ`              | `REPEATABLE READ`         | `REPEATABLE READ`          | SQL Server `REPEATABLE READ` is pessimistic locking based, Babelfish `REPEATABLE READ` is snapshot (MVCC) based. |
| `SERIALIZABLE`                 | `SERIALIZABLE`            | `SERIALIZABLE`             | SQL Server `SERIALIZABLE` is pessimistic isolation, Babelfish `SERIALIZABLE` is snapshot (MVCC) based.           |

###### Note

The table hints are not currently supported and their behavior is controlled by using the Babelfish predefined escape hatch `escape_hatch_table_hints`.

## Setting up the transaction isolation levels

Use the following command to set transaction isolation level:

###### Example

```

SET TRANSACTION ISOLATION LEVEL { READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SNAPSHOT | SERIALIZABLE }

```

## Enabling or disabling transaction isolation levels

Transaction isolation levels `REPEATABLE READ` and `SERIALIZABLE` are disabled by default in Babelfish and you have to explicitly enable them by
setting the `babelfishpg_tsql.isolation_level_serializable` or `babelfishpg_tsql.isolation_level_repeatable_read` escape hatch to `pg_isolation` using
`sp_babelfish_configure`. For more information, see [Managing Babelfish error handling with escape hatches](babelfish-strict.md "babelfish-strict.md").

Below are examples for enabling or disabling the use of `REPEATABLE READ` and `SERIALIZABLE` in the current session by setting their respective escape hatches.
Optionally include `server` parameter to set the escape hatch for the current session as well as for all subsequent new sessions.

To enable the use of `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ` in current session only.

###### Example

```
EXECUTE sp_babelfish_configure 'isolation_level_repeatable_read', 'pg_isolation'

```

To enable the use of `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ` in current session and all consequent new sessions.

###### Example

```
EXECUTE sp_babelfish_configure 'isolation_level_repeatable_read', 'pg_isolation', 'server'

```

To disable the use of `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ` in current session and consequent new sessions.

###### Example

```
EXECUTE sp_babelfish_configure 'isolation_level_repeatable_read', 'off', 'server'

```

To enable the use of `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE` in current session only.

###### Example

```
EXECUTE sp_babelfish_configure 'isolation_level_serializable', 'pg_isolation'

```

To enable the use of `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE` in current session and all consequent new sessions.

###### Example

```
EXECUTE sp_babelfish_configure 'isolation_level_serializable', 'pg_isolation', 'server'

```

To disable the use of `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE` in current session and consequent new sessions.

###### Example

```
EXECUTE sp_babelfish_configure 'isolation_level_serializable', 'off', 'server'

```
