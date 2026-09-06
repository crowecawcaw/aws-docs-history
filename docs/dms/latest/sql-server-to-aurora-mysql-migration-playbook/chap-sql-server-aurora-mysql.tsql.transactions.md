

# Transactions for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.transactions"></a>

This topic provides reference information about transaction handling when migrating from Microsoft SQL Server 2019 to Amazon Aurora MySQL. You can gain insights into the key differences in transaction support, isolation levels, and syntax between these two database systems.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  [Transaction Isolation](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.transactionisolation)  | Default isolation level is set to `REPEATABLE READ`. Default mechanism `CONSISTENT SNAPSHOT` is similar to `READ COMMITTED SNAPSHOT` isolation in SQL Server. Syntax and option differences. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.transactions.sqlserver"></a>

A *transaction* is a unit of work performed against a database and typically represents a change in the database. Transactions serve the following purposes:
+ Provide units of work that enable recovery from logical or physical system failures while keeping the database in a consistent state.
+ Provide units of work that enable recovery from failures while keeping a database in a consistent state when a logical or physical system failure occurs.
+ Provide isolation between users and programs accessing a database concurrently.

Transactions are an all-or-nothing unit of work. Each transactional unit of work must either complete, or it must rollback all data changes. Also, transactions must be isolated from other transactions. The results of the view of data for each transaction must conform to the defined database isolation level.

Database transactions must comply with ACID properties:
+  **Atomic** — Transactions are all-or-nothing. If any part of the transaction fails, the entire transaction fails and the database remains unchanged.
**Note**  
There are exceptions to this rule. For example, some constraint violations, for each ANSI definitions, shouldn’t cause a transaction rollback.
+  **Consistent** — All transactions must bring the database from one valid state to another valid state. Data must be valid according to all defined rules, constraints, triggers, and so on.
+  **Isolation** — Concurrent run of transactions must result in a system state that would occur if transactions were run sequentially.
**Note**  
There are several exceptions to this rule based on the lenience of the required isolation level.
+  **Durable** — After a transaction commits successfully and is acknowledged to the client, the engine must guarantee that its changes are persisted even in the event of power loss, system crashes, or any other errors.
**Note**  
By default, SQL Server uses the auto commit or implicit transactions mode set to ON. Every statement is treated as a transaction on its own unless a transaction was explicitly defined. This behavior is different than other engines like Oracle where, by default, every DML requires an explicit `COMMIT` statement to be persisted.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.transactions.sqlserver.syntax"></a>

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
+  **Read uncommitted** — A current transaction can see uncommitted data from other transactions. If a transaction performs a rollback, all data is restored to its previous state.
+  **Read committed** — A transaction only sees data changes that were committed. Therefore, dirty reads aren’t possible. However, after issuing a commit, it would be visible to the current transaction while it’s still in a running state.
+  **Repeatable read** — A transaction sees data changes made by the other transactions only after both transactions issue a commit or are rolled back.
+  **Serializable** — This isolation level is the strictest because it doesn’t permit transaction overwrites of another transaction’s actions. Concurrent run of a set of serializable transactions is guaranteed to produce the same effect as running them sequentially in the same order.

The main difference between isolation levels is the phenomena they prevent from appearing. The three preventable phenomena are:
+  **Dirty reads** — A transaction can read data written by another transaction but not yet committed.
+  **Non-repeatable or fuzzy reads** — When reading the same data several times, a transaction can find the data has been modified by another transaction that has just committed. The same query ran twice can return different values for the same rows.
+  **Phantom or ghost reads** — Similar to a non-repeatable read, but it is related to new data created by another transaction. The same query ran twice can return different numbers of records.

The following table summarizes the four ANSI/ISO SQL standard (SQL92) isolation levels and indicates which phenomena are allowed or disallowed.


| Transaction isolation level | Dirty reads | Non-repeatable reads | Phantom reads | 
| --- | --- | --- | --- | 
| Read uncommitted | Allowed | Allowed | Allowed | 
| Read committed | Disallowed | Allowed | Allowed | 
| Repeatable read | Disallowed | Disallowed | Allowed | 
| Serializable | Disallowed | Disallowed | Disallowed | 

There are two common implementations for transaction isolation:
+  **Pessimistic isolation or locking** — Resources accessed by a transaction are locked for the duration of the transaction. Depending on the operation, resource, and transaction isolation level, other transactions can see changes made by the locking transaction, or they must wait for it to complete. With this mechanism, there is only one copy of the data for all transactions, which minimizes memory and disk resource consumption at the expense of transaction lock waits.
+  **Optimistic isolation (MVCC)** — Every transaction owns a set of the versions of the resources (typically rows) that it accessed. In this mode, transactions don’t have to wait for one another at the expense of increased memory and disk utilization. In this isolation mechanism, there is a chance that conflicts will arise when transactions attempt to commit. In case of a conflict, the application needs to be able to handle the rollback, and attempt a retry.

SQL Server implements both mechanisms. You can use them concurrently.

For optimistic isolation, SQL Server introduced two additional isolation levels: read-committed snapshot and snapshot.

Set the transaction isolation level using `SET` command. It affects the current run scope only.

```
SET TRANSACTION ISOLATION LEVEL { READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SNAPSHOT | SERIALIZABLE }
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.transactions.sqlserver.examples"></a>

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

For more information, see [Transaction Isolation Levels (ODBC)](https://docs.microsoft.com/en-us/sql/odbc/reference/develop-app/transaction-isolation-levels?view=sql-server-ver15) and [SET TRANSACTION ISOLATION LEVEL (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.transactions.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports the four transaction isolation levels specified in the SQL:1992 standard: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`.

The simplified syntax for setting transaction boundaries in Aurora MySQL is shown following:

```
SET [SESSION] TRANSACTION ISOLATION LEVEL [READ WRITE | READ ONLY] | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED | SERIALIZABLE]
```

**Note**  
Setting the `GLOBAL` isolation level isn’t supported in Aurora MySQL; only session scope can be changed. This behavior is similar to Oracle. Also, the default behavior of transactions is to use `REPEATABLE READ` and consistent reads. Applications designed to run with `READ COMMITTED` may need to be modified. Alternatively, explicitly change the default to `READ COMMITTED`.

The default isolation level for Aurora MySQL is `REPEATABLE READ`.

To set the transaction isolation level, you will need to set the `tx_isolation` parameter when using Aurora MySQL. For more information, see [Server Options](chap-sql-server-aurora-mysql.configuration.serveroptions.md).

**Note**  
 Amazon Relational Database Service (Amazon RDS) for MySQL 8 supports a new `innodb_deadlock_detect` dynamic variable. You can use this variable to turn off the deadlock detection. On high concurrency systems deadlock detection can cause a slowdown when numerous threads wait for the same lock. At times it may be more efficient to turn off deadlock detection and rely on the `innodb_lock_wait_timeout` setting for transaction rollback when a deadlock occurs.

Starting from MySQL 8, InnoDB supports `NOWAIT` and `SKIP LOCKED` options with `SELECT …​ FOR SHARE` and `SELECT …​ FOR UPDATE` locking read statements. `NOWAIT` causes the statement to return immediately if a requested row is locked by another transaction.

 `SKIP LOCKED` removes locked rows from the result set. `SELECT …​ FOR SHARE` replaces `SELECT …​ LOCK IN SHARE MODE` but `LOCK IN SHARE MODE` remains available for backward compatibility. The statements are equivalent. However, `FOR UPDATE` and `FOR SHARE` support `NOWAIT SKIP LOCKED` and `OF tbl_name` options. For more information, see [SELECT Statement](https://dev.mysql.com/doc/refman/8.0/en/select.html) in the *MySQL documentation*.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.transactions.mysql.syntax"></a>

Simplified syntax for setting transaction boundaries:

```
SET [SESSION] TRANSACTION ISOLATION LEVEL [READ WRITE | READ ONLY] | REPEATABLE READ |
READ COMMITTED | READ UNCOMMITTED | SERIALIZABLE]
```

**Note**  
Setting a `GLOBAL` isolation level isn’t supported in Aurora MySQL. You can only change the session scope; similar to SQL Server `SET` scope. The default behavior of transactions is to use `REPEATABLE READ` and consistent reads. Applications designed to run with `READ COMMITTED` may need to be modified. Alternatively, they can explicitly change the default to `READ COMMITTED`.

In Aurora MySQL, you can optionally specify a transaction intent. Setting a transaction to `READ ONLY` turns off the transaction’s ability to modify or lock both transactional and non-transactional tables visible to other transactions, but the transaction can still modify or lock temporary tables. It also enables internal optimization to improve performance and concurrency. The default is `READ WRITE`.

Simplified syntax for the commands defining transaction boundaries:

```
START TRANSACTION WITH CONSISTENT SNAPSHOT | READ WRITE | READ ONLY
```

Or

```
BEGIN [WORK]
```

The `WITH CONSISTENT SNAPSHOT` option starts a consistent read transaction. The effect is the same as issuing a `START TRANSACTION` followed by a `SELECT` from any table. `WITH CONSISTENT SNAPSHOT` doesn’t change the transaction isolation level.

A consistent read uses snapshot information to make query results available based on a point in time regardless of modifications performed by concurrent transactions. If queried data has been changed by another transaction, the original data is reconstructed using the undo log. Consistent reads avoid locking issues that may reduce concurrency. With the `REPEATABLE READ` isolation level, the snapshot is based on the time the first read operation is performed. With the `READ COMMITTED` isolation level, the snapshot is reset to the time of each consistent read operation.

Use the following statement to commit work at the end of a transaction.

```
COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
```

Use the following statement to rollback work at the end of a transaction.

```
ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
```

One of the `ROLLBACK` options is `ROLLBACK TO SAVEPOINT<logical_name>`. This command will rollback all changes in current transaction up to the save point mentioned.

Create transaction save point during the transaction

```
SAVEPOINT <logical_name>
```

**Note**  
If the current transaction has a save point with the same name, the old save point is deleted and a new one is set.

 Aurora MySQL supports both auto commit and explicit commit modes. You can change mode using the `autocommit` system variable.

```
SET autocommit = {0 | 1}
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.transactions.mysql.examples"></a>

The following example runs two DML statements within a serializable transaction.

```
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
INSERT INTO Table1
VALUES (1, 'A');
UPDATE Table2
SET Column1 = 'Done'
WHERE KeyColumn = 1;
COMMIT;
```

## Summary
<a name="chap-sql-server-aurora-mysql.tsql.transactions.summary"></a>

The following table summarizes the key differences in transaction support and syntax when migrating from SQL Server to Aurora MySQL.


| Transaction property | SQL Server |  Aurora MySQL  | Comments | 
| --- | --- | --- | --- | 
| Default isolation level |  `READ COMMITTED`  |  `REPEATABLE READ`  | The Aurora MySQL default isolation level is stricter than SQL Server. Evaluate application needs and set appropriately. | 
| Initialize transaction syntax |  `BEGIN TRAN` or `BEGIN TRANSACTION`  |  `START TRANSACTION`  | Code rewrite is required from `BEGIN` to `START`. If using the shorthand `TRAN`, rewrite to `TRANSACTION`. | 
| Default isolation mechanism | Pessimistic lock based | Lock based for writes, consistent read for `SELECT` statements. | The Aurora MySQL default mode is similar to the `READ COMMITTED SNAPSHOT` isolation in SQL Server. | 
| Commit transaction |  `COMMIT [WORK\|TRAN\|TRANSACTION]`  |  `COMMIT [WORK]`  | If you only use `COMMIT` or `COMMIT WORK`, no change is needed. Otherwise, rewrite `TRAN` and `TRANSACTION` to `WORK`. | 
| Rollback transaction |  `ROLLBACK [WORK \|[ TRAN \| TRANSACTION]`  |  `ROLLBACK [WORK]`  | If you only use `ROLLBACK` or `ROLLBACK WORK`, no change is needed. Otherwise, rewrite `TRAN` and `TRANSACTION` to `WORK`. | 
| Set autocommit off or on |  `SET IMPLICIT_TRANSACTIONS OFF \| ON`  |  `SET autocommit = 0 \| 1`  | For more information, see [Session Options](chap-sql-server-aurora-mysql.configuration.sessionoptions.md). | 
| ANSI isolation |  `REPEATABLE READ` \| `READ COMMITTED` \| `READ UNCOMMITTED` \| `SERIALIZABLE`  |  `REPEATABLE READ` \| `READ COMMITTED` \| `READ UNCOMMITTED` \| `SERIALIZABLE`  | Compatible syntax. | 
| MVCC |  `SNAPSHOT` and `READ COMMITTED SNAPSHOT`  |  `WITH CONSISTENT SNAPSHOT`  |  Aurora MySQL consistent read in `READ COMMITTED` isolation is similar to `READ COMMITTED SNAPSHOT` in SQL Server. | 
| Nested transactions | Supported, view level with `@@trancount`  | Not supported | Starting a new transaction in Aurora MySQL while another transaction is active causes a `COMMIT` of the previous transaction. | 
| Transaction chaining | Not supported | Causes a new transaction to open immediately upon transaction completion. |  | 
| Transaction release | Not supported | Causes the client session to disconnect upon transaction completion. |  | 

For more information, see [Transaction Isolation Levels](https://dev.mysql.com/doc/refman/5.7/en/innodb-transaction-isolation-levels.html) in the *MySQL documentation*.