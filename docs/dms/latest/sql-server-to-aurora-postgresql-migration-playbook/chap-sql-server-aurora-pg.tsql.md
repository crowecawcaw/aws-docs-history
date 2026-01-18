# Transactions for T-SQL

This topic provides reference information about transaction handling in Microsoft SQL Server and Amazon Aurora PostgreSQL, focusing on their similarities and differences. It explores the fundamental principles of database transactions, including ACID properties and isolation levels, and how they are implemented in both database systems. The topic compares the default behaviors, syntax variations, and supported features for managing transactions in SQL Server and PostgreSQL.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                                        | Key differences                                                                             |
| -------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Three star feature compatibility | Three star automation level        | [Transaction Isolation](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.transactionisolation "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.transactionisolation") | Nested transactions aren’t supported and syntax differences for initializing a transaction. |

## SQL Server Usage

A transaction is a unit of work performed on a database and typically represents a change in the database. Transactions serve the following purposes:

- Provide units of work that enable recovery from logical or physical system failures while keeping the database in a consistent state.
- Provide units of work that enable recovery from failures while keeping a database in a consistent state when a logical or physical system failure occurs.
- Provide isolation between users and programs accessing a database concurrently.

Transactions are an all-or-nothing unit of work. Each transactional unit of work must either complete, or it must rollback all data changes. Also, transactions must be isolated from other transactions. The results of the view of data for each transaction must conform to the defined database isolation level.

Database transactions must comply with ACID properties.

- **Atomic** — Transactions are all or nothing. If any part of the transaction fails, the entire transaction fails and the database remains unchanged.

There are exceptions to this rule. For example, some constraint violations, for ANSI definitions, should not cause a transaction rollback.

- **Consistent** — All transactions must bring the database from one valid state to another valid state. Data must be valid according to all defined rules, constraints, triggers, and so on.
- **Isolation** — Concurrent run of transactions must result in a system state that would occur if transactions were run sequentially.

There are several exceptions to this rule based on the lenience of the required isolation level.

- **Durable** — After a transaction commits successfully and is acknowledged to the client, the engine must guarantee that its changes are persisted in the event of power loss, system crashes, or any other errors.

By default, SQL Server uses the auto commit or implicit transactions mode set to `ON`. Every statement is treated as a transaction on its own unless a transaction was explicitly defined. This behavior is different than other engines like Oracle where, by default, every DML requires an explicit `COMMIT` statement to be persisted.

### Syntax

The following examples show the simplified syntax for the commands defining transaction boundaries.

Define the beginning of a transaction.

```
BEGIN TRAN | TRANSACTION [<transaction name>]
```

Commit work and the end of a transaction.

```
COMMIT WORK | [ TRAN | TRANSACTION [<transaction name>]]
```

Rollback work at the end of a transaction.

```
ROLLBACK WORK | [ TRAN | TRANSACTION [<transaction name>]]
```

SQL Server supports the standard ANSI isolation levels defined by the ANSI/ISO SQL standard (SQL92).

Each level provides a different approach for managing the concurrent run of transactions. The main purpose of a transaction isolation level is to manage the visibility of changed data as seen by other running transactions. Additionally, when concurrent transactions access the same data, the level of transaction isolation affects the way they interact with each other.

- **Read uncommitted** — A current transaction can see uncommitted data from other transactions. If a transaction performs a rollback, all data is restored to its previous state.
- **Read committed** — A transaction only sees data changes that were committed. Therefore, dirty reads aren’t possible. However, after issuing a commit, it would be visible to the current transaction while it’s still in a running state.
- **Repeatable read** — A transaction sees data changes made by the other transactions only after both transactions issue a commit or are rolled back.
- **Serializable** — This isolation level is the strictest because it doesn’t permit transaction overwrites of another transaction’s actions. Concurrent run of a set of serializable transactions is guaranteed to produce the same effect as running them sequentially in the same order.

The main difference between isolation levels is the phenomena they prevent from appearing. The three preventable phenomena are:

- **Dirty reads** — A transaction can read data written by another transaction but not yet committed.
- **Non-repeatable or fuzzy reads** — When reading the same data several times, a transaction can find the data has been modified by another transaction that has just committed. The same query ran twice can return different values for the same rows.
- **Phantom or ghost reads** — Similar to a non-repeatable read, but it is related to new data created by another transaction. The same query ran twice can return different numbers of records.

The following table summarizes the four ANSI/ISO SQL standard (SQL92) isolation levels and indicates which phenomena are allowed or disallowed.

| Transaction isolation level | Dirty reads | Non-repeatable reads | Phantom reads |
| --------------------------- | ----------- | -------------------- | ------------- |
| Read uncommitted            | Allowed     | Allowed              | Allowed       |
| Read committed              | Disallowed  | Allowed              | Allowed       |
| Repeatable read             | Disallowed  | Disallowed           | Allowed       |
| Serializable                | Disallowed  | Disallowed           | Disallowed    |

There are two common implementations for transaction isolation:

- **Pessimistic isolation or locking** — Resources accessed by a transaction are locked for the duration of the transaction. Depending on the operation, resource, and transaction isolation level, other transactions can see changes made by the locking transaction, or they must wait for it to complete. With this mechanism, there is only one copy of the data for all transactions, which minimizes memory and disk resource consumption at the expense of transaction lock waits.
- **Optimistic isolation (MVCC)** — Every transaction owns a set of the versions of the resources (typically rows) that it accessed. In this mode, transactions don’t have to wait for one another at the expense of increased memory and disk utilization. In this isolation mechanism, there is a chance that conflicts will arise when transactions attempt to commit. In case of a conflict, the application needs to be able to handle the rollback, and attempt a retry.

SQL Server implements both mechanisms. You can use them concurrently.

For optimistic isolation, SQL Server introduced two additional isolation levels: read-committed snapshot and snapshot.

Set the transaction isolation level using `SET` command. It affects the current run scope only.

```
SET TRANSACTION ISOLATION LEVEL { READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SNAPSHOT | SERIALIZABLE }
```

### Examples

The following example runs two DML statements within a serializable transaction.

```
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
INSERT INTO Table1
VALUES (1, 'A');
UPDATE Table2
  SET Column1 = 'Done'
WHERE KeyColumn = 1;
COMMIT TRANSACTION;
```

For more information, see [Transaction Isolation Levels (ODBC)](https://docs.microsoft.com/en-us/sql/odbc/reference/develop-app/transaction-isolation-levels?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/odbc/reference/develop-app/transaction-isolation-levels?view=sql-server-ver15") and [SET TRANSACTION ISOLATION LEVEL (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

As with SQL Server, the same ANSI/ISO SQL (SQL92) isolation levels apply to PostgreSQL, but with several similarities and some differences.

| Transaction isolation level | Dirty reads                   | Non-repeatable reads | Phantom reads                 |
| --------------------------- | ----------------------------- | -------------------- | ----------------------------- |
| Read uncommitted            | Permitted but not implemented | Permitted            | Permitted                     |
| Read committed              | Not permitted                 | Permitted            | Permitted                     |
| Repeatable read             | Not permitted                 | Not permitted        | Permitted but not implemented |
| Serializable                | Not permitted                 | Not permitted        | Not permitted                 |

PostgreSQL technically supports the use of any of the four transaction isolation levels, but only three can practically be used. The Read-Uncommitted isolation level serves as read-committed.

The way the repeatable-read isolation-level is implemented doesn’t allow for phantom reads, which is similar to the Serializable isolation-level. The primary difference between repeatable-read and serializable is that serializable guarantees that the result of concurrent transactions are precisely the same as if they were run serially, which isn’t always true for repeatable-reads.

Starting with PostgreSQL 12, you can add the `AND CHAIN` option to `COMMIT` or `ROLLBACK` commands to immediately start another transaction with the same parameters as preceding transaction.

### Multiversion Concurrency Control

In PostgreSQL, the multiversion concurrency control (MVCC) mechanism allows transactions to work with a consistent snapshot of data ignoring changes made by other transactions that have not yet committed or rolled back. Each transaction sees a snapshot of accessed data accurate to its run start time regardless of what other transactions are doing concurrently.

### Isolation Levels

PostgreSQL supports the read-committed, repeatable reads, and serializable isolation levels. Read-committed is the default isolation level.

- **Read-committed** — The default PostgreSQL transaction isolation level. It prevents sessions from seeing data from concurrent transactions until it is committed. Dirty reads aren’t permitted.
- **Repeatable read** — Queries can only see rows committed before the first query or DML statement was run in the transaction.
- **Serializable** — Provides the strictest transaction isolation level. The Serializable isolation level assures that the result of the concurrent transactions will be the same as if they run serially. This isn’t always the case for the repeatable read isolation level.

### Setting Isolation Levels in Aurora PostgreSQL

You can configure isolation levels at several levels.

- Session level.
- Transaction level.
- Instance level using Aurora parameter groups.

### Syntax

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

### Examples

The following example configures the isolation level for a specific transaction.

```
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

The following example configures the isolation level for a specific session.

```
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

Use the following example to view the current isolation level.

```
SELECT CURRENT_SETTING('TRANSACTION_ISOLATION'); -- Session
SHOW DEFAULT_TRANSACTION_ISOLATION; -- Instance
```

You can use parameter groups to modify instance-level parameters for Aurora PostgreSQL. For example, you can alter the `default_transaction_isolation` parameter using the AWS Console or the AWS CLI. For more information, see [Working with parameter groups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md#USER_WorkingWithParamGroups.Modifying "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md#USER_WorkingWithParamGroups.Modifying").

### Comparison table of relevant database features related to transactions

| Database feature                       | SQL Server                                                      | PostgreSQL                                                                                                                                                                                                                                         |
| -------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AutoCommit                             | Off                                                             | Autocommit is turned off by default, however, some client tools like psql and more are setting this to ON by default.<br>Check your client tool defaults or run the following command to check current configuration in psql: `\echo :AUTOCOMMIT`. |
| MVCC                                   | Yes                                                             | Yes                                                                                                                                                                                                                                                |
| Default isolation level                | Read-committed                                                  | Read-committed                                                                                                                                                                                                                                     |
| Supported isolation levels             | REPEATABLE READ, READ COMMITTED, READ UNCOMMITTED, SERIALIZABLE | Repeatable reads, serializable, read-only                                                                                                                                                                                                          |
| Configure session isolation levels     | Yes                                                             | Yes                                                                                                                                                                                                                                                |
| Configure transaction isolation levels | Yes                                                             | Yes                                                                                                                                                                                                                                                |

### Read-Committed Isolation Level

| TX1                                                                                                                              | TX2                                                                                                                              | Comment                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | `<br>select employee_id, salary from<br>EMPLOYEES<br>where employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | Same results returned from both sessions.                                                                      |
| `<br>begin;<br>UPDATE employees<br>SET salary=27000<br>WHERE employee_id=100;<br>`                                               | `<br>begin;<br>set transaction isolation level<br>read committed;<br>`                                                           | TX1 starts a transaction and performs an update. TX2 starts a transaction with read-committed isolation level. |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | TX1 will see the modified results while TX2 sees the original data.                                            |
|                                                                                                                                  | `<br>UPDATE employees<br>SET salary=29000<br>WHERE employee_id=100;<br>`                                                         | Waits because TX2 is blocked by TX1.                                                                           |
| `<br>Commit;<br>`                                                                                                                |                                                                                                                                  | TX1 issues a commit, and the lock is released.                                                                 |
|                                                                                                                                  | `<br>Commit;<br>`                                                                                                                | TX2 issues a commit.                                                                                           |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          29000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          29000.00<br>` | Both queries return the updated value.                                                                         |

### Serializable Isolation Level

| TX1                                                                                                                              | TX2                                                                                                                              | Comment                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | Same results returned from both sessions.                                                                                     |
| `<br>begin;<br>UPDATE employees<br>SET salary=27000<br>WHERE employee_id=100;<br>`                                               | `<br>begin;<br>set transaction isolation level serializable;<br>`                                                                | TX1 starts a transaction and performs an update. TX2 starts a transaction with isolation level of serializable.               |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          24000.00<br>` | TX1 will see the modified results while TX2 sees the original data.                                                           |
|                                                                                                                                  | `<br>update employees<br>set salary=29000<br>where employee_id=100;<br>`                                                         | Waits because TX2 is blocked by TX1.                                                                                          |
| `<br>Commit;<br>`                                                                                                                |                                                                                                                                  | TX1 issues a commit, and the lock is released.                                                                                |
|                                                                                                                                  | ERROR: couldn’t serialize access due to concurrent update.                                                                       | TX2 received an error message.                                                                                                |
|                                                                                                                                  | `<br>Commit;<br>ROLLBACK<br>`                                                                                                    | TX2 trying to issue a commit but receives a rollback message, the transaction failed due to the serializable isolation level. |
| `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | `<br>SELECT employee_id, salary<br>FROM EMPLOYEES<br>WHERE employee_id=100;<br>employee_id  salary<br>100          27000.00<br>` | Both queries return the value updated according to TX1.                                                                       |

## Summary

| Transaction property          | SQL Server                                        | Aurora PostgreSQL                                  |
| ----------------------------- | ------------------------------------------------- | -------------------------------------------------- | ------------------------- | ----------------------- | ---------------------- | -------------- | ---------------- | ------------------- |
| Default isolation level       | `READ COMMITTED`                                  | `READ COMMITTED`                                   |
| Initialize transaction syntax | `BEGIN TRAN` or `TRANSACTION`                     | `SET TRANSACTION`                                  |
| Default isolation mechanism   | Pessimistic lock based                            | Lock based for writes, consistent read for selects |
| Commit transaction            | ```<br>COMMIT<br>[WORK                            | TRAN                                               | TRANSACTION]<br>```       | ```<br>COMMIT<br>[ WORK | TRANSACTION ]<br>```   |
| Rollback transaction          | ```<br>ROLLBACK [WORK                             | [ TRAN                                             | TRANSACTION]<br>```       | ```<br>ROLLBACK [ WORK  | TRANSACTION ]<br>```   |
| Set autocommit off/on         | ```<br>SET IMPLICIT_TRANSACTIONS OFF              | ON<br>```                                          | ```<br>SET AUTOCOMMIT { = | TO } { ON               | OFF }<br>```           |
| ANSI isolation                | ```<br>REPEATABLE READ                            | READ COMMITTED                                     | READ UNCOMMITTED          | SERIALIZABLE<br>```     | ```<br>REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED | SERIALIZABLE<br>``` |
| MVCC                          | `<br>SNAPSHOT and READ<br>COMMITTED SNAPSHOT<br>` | `<br>READ COMMITTED SNAPSHOT<br>`                  |
| Nested transactions           | Supported, view level with `@@trancount`          | Not Supported                                      |

For more information, see [Transactions](https://www.postgresql.org/docs/13/tutorial-transactions.html "https://www.postgresql.org/docs/13/tutorial-transactions.html"), [Transaction Isolation](https://www.postgresql.org/docs/13/transaction-iso.html "https://www.postgresql.org/docs/13/transaction-iso.html"), and [SET TRANSACTION](https://www.postgresql.org/docs/13/sql-set-transaction.html "https://www.postgresql.org/docs/13/sql-set-transaction.html") in the _PostgreSQL documentation_.
