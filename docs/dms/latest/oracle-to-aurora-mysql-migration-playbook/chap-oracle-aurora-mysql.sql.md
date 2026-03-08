# Oracle Transaction Model and MySQL Transactions

Oracle Transaction Model and MySQL Transactions provide mechanisms for grouping SQL statements into logical units of work, ensuring atomicity, consistency, isolation, and durability (ACID properties) during database operations.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                                    | Key differences                                                                                        |
| ------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Four star feature compatibility | Four star automation level         | [Transaction Isolation](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.transactionisolation "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.transactionisolation") | In MySQL, the default isolation level is `REPEATABLE READ`. MySQL doesn’t support nested transactions. |

## Oracle usage

Database transactions are a logical, atomic units of processing containing one or more SQL statements that may run concurrently alongside other transactions. The primary purpose of a transaction is to ensure the ACID model is enforced.

- **Atomicity** — All statements in a transaction are processed as one logical unit, or none are processed. If a single part of a transaction fails, the entire transaction is aborted and no changes are persisted (all or nothing).
- **Consistency** — All data integrity constraints are checked and all triggers are processed before a transaction is processed. If any of the constraints are violated, the entire transaction fails.
- **Isolation** — One transaction isn’t affected by the behavior of other concurrent transactions. The effect of a transaction isn’t visible to other transactions until the transaction is committed.
- **Durability** — Once a transaction commits, its results will not be lost regardless of subsequent failures. After a transaction completes, changes made by committed transactions are permanent. The database ensures that committed transactions can’t be lost.

### Database transaction isolation levels

The ANSI/ISO SQL standard (SQL92) defines four levels of isolation. Each level provides a different approach for handling concurrent run of database transactions. Transaction isolation levels manage the visibility of changed data as seen by other running transactions. In addition, when accessing the same data with several concurrent transactions, the selected level of transaction isolation affects the way different transactions interact. For example, if a bank account is shared by two individuals, what will happen if both parties attempt to perform a transaction on the shared account at the same time? One checks the account balance while the other withdraws money. Oracle supports the following isolation levels:

- **Read-uncommitted** — A currently processed transaction can see uncommitted data made by the other transaction. If a rollback is performed, all data is restored to its previous state.
- **Read-committed** — A transaction only sees data changes that were committed. Uncommitted changes(“dirty reads”) aren’t possible.
- **Repeatable read** — A transaction can view changes made by the other transaction only after both transactions issue a COMMIT or both are rolled-back.
- **Serializable** — Any concurrent run of a set of serializable transactions is guaranteed to produce the same effect as running them sequentially in the same order.

Isolation levels affect the following database behavior.

- **Dirty reads** — A transaction can read data that was written by another transaction, but isn’t yet committed.
- **Non-repeatable or fuzzy reads** — When reading the same data several times, a transaction can find that the data has been modified by another transaction that has just committed. The same query executed twice can return different values for the same rows.
- **Phantom reads** — Similar to a non-repeatable read, but it is related to new data created by another transaction. The same query run twice can return a different numbers of records.

| Isolation level  | Dirty reads   | Non-repeatable reads | Phantom reads |
| ---------------- | ------------- | -------------------- | ------------- |
| Read-uncommitted | Permitted     | Permitted            | Permitted     |
| Read-committed   | Not permitted | Permitted            | Permitted     |
| Repeatable read  | Not permitted | Not permitted        | Permitted     |
| Serializable     | Not permitted | Not permitted        | Not permitted |

### Oracle isolation levels

Oracle supports the read-committed and serializable isolation levels. It also provides a Read-Only isolation level which isn’t a part of the ANSI/ISO SQL standard (SQL92). Read-committed is the default.

- **Read-committed** — Each query that you run within a transaction only sees data that was committed before the query itself. The Oracle database never allows reading dirty pages and uncommitted data. This is the default option.
- **Serializable** — Serializable transactions don’t experience non-repeatable reads or phantom reads because they are only able to see changes that were committed at the time the transaction began (in addition to the changes made by the transaction itself performing DML operations).
- **Read-only** — The read-only isolation level doesn’t allow any DML operations during the transaction and only sees data committed at the time the transaction began.

### Oracle and MySQL Multi-Version Concurrency Control

Oracle uses the Oracle Multiversion Concurrency Controls (MVCC) mechanism to provide automatic read consistency across the entire database and all sessions. Using MVCC, database sessions see data based on a single point in time ensuring only committed changes are viewable. Oracle relies on the System Change Number (SCN) of the current transaction to obtain a consistent view of the database. Therefore, all database queries only return data committed with respect to the SCN at the time of query run.

### Setting isolation levels

Isolation levels can be changed at the transaction and session levels.

### Examples

Change the isolation level at the transaction-level.

```
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SET TRANSACTION READ ONLY;
```

Change the isolation-level at a session-level.

```
ALTER SESSION SET ISOLATION_LEVEL = SERIALIZABLE;
ALTER SESSION SET ISOLATION_LEVEL = READ COMMITTED;
```

For more information, see [Transactions](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/transactions.html#GUID-B97790CB-DF82-442D-B9D5-50CCE6BF9FBD "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/transactions.html#GUID-B97790CB-DF82-442D-B9D5-50CCE6BF9FBD") in the _Oracle documentation_.

## MySQL usage

Aurora MySQL supports all four transaction isolation levels described by the SQL:1992 standard: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`.

The default isolation level for Aurora MySQL is `REPEATABLE READ`. The simplified syntax for setting transaction boundaries in Aurora MySQL is:

```
SET [SESSION] TRANSACTION ISOLATION LEVEL
[READ WRITE | READ ONLY] |
REPEATABLE READ | READ COMMITTED |
READ UNCOMMITTED | SERIALIZABLE]
```

###### Note

Setting the `GLOBAL` isolation level is not supported in Aurora MySQL; only session scope can be changed. This behavior is similar to Oracle. Also, the default behavior of transactions is to use `REPEATABLE READ` and consistent reads. Applications designed to run with `READ COMMITTED` may need to be modified. Alternatively, explicitly change the default to `READ COMMITTED`.

To set the transaction isolation level, configure the `tx_isolation` parameter when using Aurora for MySQL. For more information, see [Oracle Instance Parameters and Aurora MySQL Parameter Groups](chap-oracle-aurora-mysql.configuration.md "chap-oracle-aurora-mysql.configuration.md").

In Aurora MySQL, a transaction intent can be optionally specified. Setting a transaction to `READ ONLY` disables the transaction’s ability to modify or lock both transactional and non-transactional tables visible to other transactions.

The transaction can still modify or lock temporary tables. This enables internal optimization to improve performance and concurrency. The default is `READ WRITE`.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL version 8, you can use a new `innodb_deadlock_detect` dynamic variable to disable deadlock detection. On high concurrency systems, deadlock detection can cause a slowdown when numerous threads wait for the same lock. At times it may be more efficient to disable deadlock detection and rely on the `innodb_lock_wait_timeout` setting for transaction rollback when a deadlock occurs.

###### Note

Starting from Amazon RDS for MySQL version 8, InnoDB supports `NOWAIT` and `SKIP LOCKED` options with `SELECT …​ FOR SHARE` and `SELECT …​ FOR UPDATE` locking read statements. `NOWAIT` causes the statement to return immediately if a requested row is locked by another transaction. `SKIP LOCKED` removes locked rows from the result set. `SELECT …​ FOR SHARE` replaces `SELECT …​ LOCK IN SHARE MODE` but `LOCK IN SHARE MODE` remains available for backward compatibility. The statements are equivalent. However, `FOR UPDATE` and `FOR SHARE` support `NOWAIT SKIP LOCKED` and `OF tbl_name` options. For more information, see [SELECT Statement](https://dev.mysql.com/doc/refman/8.0/en/select.html "https://dev.mysql.com/doc/refman/8.0/en/select.html") in the _MySQL documentation_.

### Defining the Beginning of a Transaction

```
START TRANSACTION WITH CONSISTENT SNAPSHOT | READ WRITE | READ ONLY

or

BEGIN [WORK]
```

The `WITH CONSISTENT SNAPSHOT` option starts a consistent read Transaction. The effect is the same as issuing a `START TRANSACTION` followed by a `SELECT` from any table. `WITH CONSISTENT SNAPSHOT` doesn’t change the transaction isolation level.

A consistent read uses snapshot information to make query results available based on a point-in-time regardless of modifications performed by concurrent transactions. If queried data has been changed by another transaction, the original data is reconstructed using the undo log. This avoids locking issues that may reduce concurrency. With the `REPEATABLE READ` isolation level, the snapshot is based on the time the first read operation is performed. With the `READ COMMITTED` isolation level, the snapshot is reset to the time of each consistent read operation.

Commit work at the end of a transaction:

```
COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
```

Roll back work at the end of a transaction:

```
ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
```

One of the `ROLLBACK` options is `ROLLBACK TO SAVEPOINT <logical_name>`. This command will rollback all changes in current transaction up to the save point mentioned.

Create transaction save point during the transaction

```
SAVEPOINT <logical_name>
```

###### Note

If the current transaction has a save point with the same name, the old save point is deleted and a new one is set.

The `AND CHAIN` clause causes a new transaction to begin as soon as the current one ends using the same isolation level and access mode as the just-terminated transaction.

The `RELEASE` clause causes the server to disconnect the current session after terminating the current transaction. The `NO` keyword suppresses both CHAIN and RELEASE completion. This can be useful if the `completion_type` system variable is set to cause chaining or release completion.

Always run with the `autocommit` mode turned on. Set the `autocommit` parameter to 1 on the database side. This is the default value. Also, make sure that the `autocommit` parameter is set to 1 on the application side. This might not be the default value.

Always double-check the `autocommit` settings on the application side. For example, Python drivers such as MySQLdb and PyMySQL turn off `autocommit` by default.

Aurora MySQL supports auto commit and explicit commit modes. You can change the mode using the system variable `autocommit`, 1 is the default:

```
SET autocommit = {0 | 1}
```

### Examples

Run two DML statements within a serializable transaction.

```
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
INSERT INTO Table1 VALUES (1, 'A');

UPDATE Table2 SET Column1 = 'Done' WHERE KeyColumn = 1;
COMMIT;
```

## Summary

The following table summarizes the key differences in transaction support and syntax when migrating from Oracle to Aurora MySQL.

| Transaction property          | Oracle                                                                                         | Aurora MySQL                                                              | Comments                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------- | ------------- | ----------------- |
| Default isolation level       | `READ COMMITTED`                                                                               | `REPEATABLE READ`                                                         | The Aurora MySQL default isolation level is stricter than the Oracle. Evaluate application needs and set appropriately.       |
| Initialize transaction syntax | `START TRANSACTION`                                                                            | `START TRANSACTION`                                                       |                                                                                                                               |
| Commit transaction            | `COMMIT [WORK                                                                                  | FORCE]`                                                                   | `COMMIT [WORK]`                                                                                                               | If you use only `COMMIT` or `COMMIT WORK`, no changes are needed. Otherwise, rewrite `FORCE` to `WORK`. |
| Rollback transaction          | `ROLLBACK [WORK                                                                                | [ TO                                                                      | FORCE]`                                                                                                                       | `ROLLBACK [WORK]`                                                                                       | If you use only `ROLLBACK` or `ROLLBACK WORK`, no changes are needed. Otherwise, rewrite `TO` and `FORCE` to `WORK`. |
| Set `autocommit` off or on    | `SET AUTOCOMMIT ON                                                                             | OFF (SQL\*Plus)`                                                          | `SET autocommit = 0                                                                                                           | 1`                                                                                                      |                                                                                                                      |
| ANSI isolations               | `REPEATABLE READ                                                                               | READ COMMITTED                                                            | READ UNCOMMITTED                                                                                                              | SERIALIZABLE`                                                                                           | `REPEATABLE READ                                                                                                     | READ COMMITTED | READ UNCOMMITTED | SERIALIZABLE` | Compatible syntax |
| MVCC                          | `START TRANSACTION                                                                             | READ COMMITTED`                                                           | `WITH CONSISTENT SNAPSHOT`                                                                                                    | Aurora MySQL consistent read in `READ COMMITTED` isolation, is similar to `READ COMMITTED` in Oracle.   |
| Nested transactions           | Supported by starting new transaction or call a procedure or function after transaction start. | Not Supported                                                             | Starting a new transaction in Aurora MySQL while another transaction is active causes a `COMMIT` of the previous transaction. |
| Transaction chaining          | Not Supported                                                                                  | Causes a new transaction to open immediately upon transaction completion. |                                                                                                                               |
| Transaction release           | Not supported                                                                                  | Causes the client session to disconnect upon transaction completion       |                                                                                                                               |

For more information, see [Transaction Isolation Levels](https://dev.mysql.com/doc/refman/5.7/en/innodb-transaction-isolation-levels.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-transaction-isolation-levels.html") in the _MySQL documentation_.
