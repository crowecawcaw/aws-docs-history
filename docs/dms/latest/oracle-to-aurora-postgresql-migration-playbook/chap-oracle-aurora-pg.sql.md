# Oracle transaction model and PostgreSQL transactions

Transactions are logical units of work that allow multiple database operations to be executed as a single atomic unit. The Oracle transaction model and PostgreSQL transactions define how transactions are handled, including features like atomicity, consistency, isolation, and durability (ACID properties).

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                      | Key differences                                                                     |
| ------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [Transaction Isolation](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.transaction "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.transaction") | PostgreSQL doesn’t support `SAVEPOINT`, `ROLLBACK TO SAVEPOINT` inside of functions |

## Oracle usage

Database transactions are a logical, atomic units of processing containing one or more SQL statements that may run concurrently alongside other transactions. The primary purpose of a transaction is to ensure the ACID model is enforced.

- **Atomicity** — All statements in a transaction are processed as one logical unit, or none are processed. If a single part of a transaction fails, the entire transaction is aborted and no changes are persisted (all or nothing).
- **Consistency** — All data integrity constraints are checked and all triggers are processed before a transaction is processed. If any of the constraints are violated, the entire transaction fails.
- **Isolation** — One transaction isn’t affected by the behavior of other concurrentl transactions. The effect of a transaction isn’t visible to other transactions until the transaction is committed.
- **Durability** — Once a transaction commits, its results will not be lost regardless of subsequent failures. After a transaction completes, changes made by committed transactions are permanent. The database ensures that committed transactions can’t be lost.

### Database transaction isolation levels

The ANSI/ISO SQL standard (SQL92) defines four levels of isolation. Each level provides a different approach for handling concurrent run of database transactions. Transaction isolation levels manage the visibility of changed data as seen by other running transactions. In addition, when accessing the same data with several concurrent transactions, the selected level of transaction isolation affects the way different transactions interact. For example, if a bank account is shared by two individuals, what will happen if both parties attempt to perform a transaction on the shared account at the same time? One checks the account balance while the other withdraws money. Oracle supports the following isolation levels:

- **Read-uncommitted** — A currently processed transaction can see uncommitted data made by the other transaction. If a rollback is performed, all data is restored to its previous state.
- **Read-committed** — A transaction only sees data changes that were committed. Uncommitted changes(“dirty reads”) aren’t possible.
- **Repeatable read** — A transaction can view changes made by the other transaction only after both transactions issue a COMMIT or both are rolled-back.
- **Serializable** — Any concurrent run of a set of serializable transactions is guaranteed to produce the same effect as running them sequentially in the same order.

Isolation levels affect the following database behavior.

- **Dirty reads** — A transaction can read data that was written by another transaction, but isn’t yet committed.
- **Non-repeatable (fuzzy) reads** — When reading the same data several times, a transaction can find that the data has been modified by another transaction that has just committed. The same query executed twice can return different values for the same rows.
- **Phantom reads** — Similar to a non-repeatable read, but it is related to new data created by another transaction. The same query run twice can return a different numbers of records.

| Isolation level  | Dirty reads   | Non-repeatable reads | Phantom reads |
| ---------------- | ------------- | -------------------- | ------------- |
| Read-uncommitted | Permitted     | Permitted            | Permitted     |
| Read-committed   | Not permitted | Permitted            | Permitted     |
| Repeatable read  | Not permitted | Not permitted        | Permitted     |
| Serializable     | Not permitted | Not permitted        | Not permitted |

### Oracle isolation levels

Oracle supports the read-committed and serializable isolation levels. It also provides a Read-Only isolation level which isn’t a part of the ANSI/ISO SQL standard (SQL92). Read-committed is the default.

- **Read-committed (default)** — Each query that you run within a transaction only sees data that was committed before the query itself. The Oracle database nevers allow reading “dirty pages” and uncommitted data.
- **Serializable** — Serializable transactions don’t experience non-repeatable reads or phantom reads because they are only able to “see” changes that were committed at the time the transaction began (in addition to the changes made by the transaction itself performing DML operations).
- **Read-only** — The read-only isolation level doesn’t allow any DML operations during the transaction and
  only sees data committed at the time the transaction began.

### Oracle Multiversion Concurrency Controls

Oracle uses the Oracle Multiversion Concurrency Controls (MVCC) mechanism to provide automatic read consistency across the entire database and all sessions. Using MVCC, database sessions see data based on a single point in time ensuring only committed changes are viewable. Oracle relies on the System Change Number (SCN) of the current transaction to obtain a consistent view of the database. Therefore, all database queries only return data committed with respect to the SCN at the time of query run.

### Setting isolation levels

Isolation levels can be changed at the transaction and session levels.

**Examples**

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

## PostgreSQL usage

The same ANSI/ISO SQL (SQL92) isolation levels apply to PostgreSQL, with several similarities and some differences:

| Isolation level  | Dirty reads                                 | Non-repeatable reads | Phantom reads                               |
| ---------------- | ------------------------------------------- | -------------------- | ------------------------------------------- |
| Read-uncommitted | Permitted but not implemented in PostgreSQL | Permitted            | Permitted                                   |
| Read-committed   | Not permitted                               | Permitted            | Permitted                                   |
| Repeatable read  | Not permitted                               | Not permitted        | Permitted but not implemented in PostgreSQL |
| Serializable     | Not permitted                               | Not permitted        | Not permitted                               |

PostgreSQL technically supports the use of any of the above four transaction isolation levels, but only three can practically be used. The read-uncommitted isolation level serves as read-committed.

The way the Repeatable-Read isolation-level is implemented doesn’t allow for phantom reads, which is similar to the serializable isolation level. The primary difference between repeatable read and serializable is that serializable guarantees that the result of concurrent transactions will be precisely the same as if they were run serially, which isn’t always true for repeatable reads.

Starting with PostgreSQL 12, you can add the `AND CHAIN` option to `COMMIT` or `ROLLBACK` commands to immediately start another transaction with the same parameters as preceding transaction.

### Isolation levels supported by PostgreSQL

PostgreSQL supports the read-committed, repeatable reads, and serializable isolation levels. Read-committed is the default isolation level (similar to the default isolation level in the Oracle database).

- **Read-committed** — The default PostgreSQL transaction isolation level. Preventing sessions from “seeing” data from concurrent transactions until it is committed. Dirty reads aren’t permitted.
- **Repeatable read** — Queries can only see rows committed before the first query or DML statement was run in the transaction.
- **Serializable** — Provides the strictest transaction isolation level. The Serializable isolation level assures that the result of the concurrent transactions will be the same as if they were executed serially. This isn’t always the case for the Repeatable-Read isolation level.

### Multiversion Concurrency Control

PostgreSQL implements a similar Multiversion Concurrency Control (MVCC) mechanism when compared to Oracle. In PostgreSQL, the MVCC mechanism allows transactions to work with a consistent snapshot of data ignoring changes made by other transactions which have not yet committed or rolled back. Each transaction “sees” a snapshot of accessed data accurate to its run start time, regardless of what other transactions are doing concurrently.

### Setting isolation levels in Aurora PostgreSQL

You can configure isolation levels at several levels:

- Session level.
- Transaction level.
- Instance level using Aurora Parameter Groups.

**Examples**

Configure the isolation level for a specific transaction.

```
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

Configure the isolation level for a specific session.

```
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

View the current isolation level.

```
SELECT CURRENT_SETTING('TRANSACTION_ISOLATION'); -- Session
SHOW DEFAULT_TRANSACTION_ISOLATION;              -- Instance
```

You can modify instance-level parameters for Aurora PostgreSQL by using parameter groups. For example, you can alter the `default_transaction_isolation` parameter using the AWS Console or the AWS CLI.

For more information, see [Modifying parameters in a DB parameter group](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md#USER_WorkingWithParamGroups.Modifying "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md#USER_WorkingWithParamGroups.Modifying") in the _Amazon RDS documentation_.

### PostgreSQL Transaction Synopsis

```
SET TRANSACTION transaction_mode [...]
SET TRANSACTION SNAPSHOT snapshot_id
SET SESSION CHARACTERISTICS AS TRANSACTION transaction_mode [...]

where transaction_mode is one of:

ISOLATION LEVEL {
SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED
}
READ WRITE | READ ONLY [ NOT ] DEFERRABLE
```

| Database feature                       | Oracle                  | PostgreSQL                                                                                                                                                                                                                                                  |
| -------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AutoCommit                             | Off                     | Depends. Autocommit is turned off by default, however, some client tools such as psql and more are setting this to ON by default. Check your client tool defaults or run the following command to check current configuration in psql: `\echo :AUTOCOMMIT`. |
| MVCC                                   | Yes                     | Yes                                                                                                                                                                                                                                                         |
| Default Isolation Level                | Read-committed          | Read-committed                                                                                                                                                                                                                                              |
| Supported Isolation Levels             | Serializable, Read-only | Repeatable Reads, Serializable, Read-only                                                                                                                                                                                                                   |
| Configure Session Isolation Levels     | Yes                     | Yes                                                                                                                                                                                                                                                         |
| Configure Transaction Isolation Levels | Yes                     | Yes                                                                                                                                                                                                                                                         |
| Nested Transaction Support             | Yes                     | No. Consider using `SAVEPOINT` instead.                                                                                                                                                                                                                     |
| Support for transaction `SAVEPOINT`s   | Yes                     | Yes                                                                                                                                                                                                                                                         |

**Read-committed isolation level.**

| TX1                                                                                                                              | TX2                                                                                                                              | Comment                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | `<br>select employee_id, salary<br>from EMPLOYEES<br>where employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | Same results returned from both sessions                                                                    |
| `<br>begin;<br>UPDATE employees<br>SET salary=27000<br>WHERE employee_id=100;<br>`                                               | `<br>begin;<br>set transaction isolation<br>level read committed;<br>`                                                           | TX1 starts a transaction; performs an update. TX2 starts a transaction with read-committed isolation level. |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | TX1 will “see” the modified results (27000.00) while TX2 “sees” the original data (24000.00).               |
|                                                                                                                                  | `<br>UPDATE employees<br>SET salary=29000<br>WHERE employee_id=100;<br>`                                                         | Waits because TX2 is blocked by TX1.                                                                        |
| `<br>Commit;<br>`                                                                                                                |                                                                                                                                  | TX1 issues a commit, and the lock is released.                                                              |
|                                                                                                                                  | `<br>Commit;<br>`                                                                                                                | TX2 issues a commit.                                                                                        |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          29000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          29000.00<br>` | Both queries return the value<br>• 29000.00.                                                                |

**Serializable isolation level.**

| TX1                                                                                                                              | TX2                                                                                                                              | Comment                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | `<br>select employee_id, salary<br>from EMPLOYEES<br>where employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | Same results returned from both sessions                                                                                      |
| `<br>begin;<br>UPDATE employees<br>SET salary=27000<br>WHERE employee_id=100;<br>`                                               | `<br>begin;<br>set transaction isolation<br>level serializable;<br>`                                                             | TX1 starts a transaction and performs an update. TX2 starts a transaction with serializable isolation level.                  |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | TX1 will “see” the modified results (27000.00) while TX2 “sees” the original data (24000.00).                                 |
|                                                                                                                                  | `<br>UPDATE employees<br>SET salary=29000<br>WHERE employee_id=100;<br>`                                                         | Waits because TX2 is blocked by TX1.                                                                                          |
| `<br>Commit;<br>`                                                                                                                |                                                                                                                                  | TX1 issues a commit, and the lock is released.                                                                                |
|                                                                                                                                  | ERROR: could not serialize access due to concurrent update.                                                                      | TX2 received an error message.                                                                                                |
|                                                                                                                                  | `<br>Commit;<br>ROLLBACK<br>`                                                                                                    | TX2 trying to issue a commit but receives a rollback message, the transaction failed due to the serializable isolation level. |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | Both queries will return the data updated according to TX1.                                                                   |

For more information, see [Transactions](https://www.postgresql.org/docs/13/tutorial-transactions.html "https://www.postgresql.org/docs/13/tutorial-transactions.html"), [Transaction Isolation](https://www.postgresql.org/docs/13/transaction-iso.html "https://www.postgresql.org/docs/13/transaction-iso.html"), and [SET TRANSACTION](https://www.postgresql.org/docs/13/sql-set-transaction.html "https://www.postgresql.org/docs/13/sql-set-transaction.html") in the _PostgreSQL documentation_.
