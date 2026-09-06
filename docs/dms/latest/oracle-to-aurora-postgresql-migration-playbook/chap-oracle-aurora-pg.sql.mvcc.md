

# Multi-Version Concurrency Control
<a name="chap-oracle-aurora-pg.sql.mvcc"></a>

With AWS DMS, you can implement Multi-Version Concurrency Control (MVCC) to manage concurrent access to data during database migrations. MVCC is a concurrency control method that maintains multiple versions of database objects, allowing readers and writers to access the data simultaneously without blocking or causing conflicts.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-5.png)  | N/A | N/A | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.mvcc.ora"></a>

Two primary lock types exist in Oracle: exclusive locks and share locks, which implement the following high-level locking semantics:
+ Writers never block readers.
+ Readers never block writers.
+ Oracle never escalates locks from row to page and table level, which reduces potential deadlocks.
+ In Oracle, users can issue explicit locks on specific tables using the `LOCK TABLE` statement.

Lock types can be divided into four categories: DML locks, DDL locks, Explicit (Manual) data locking, and System locks. The following sections describe each category.

 **DML locks** 

DML locks preserve the integrity of data accessed concurrently by multiple users. DML statements acquire locks automatically both on row and table levels.
+  **Row Locks (TX)**. Obtained on a single row of a table by one the following statements: `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and `SELECT …​ FOR UPDATE`. If a transaction obtains a row lock, a table lock is also acquired to prevent DDL modifications to the table that might cause conflicts. The lock exists until the transaction ends with a `COMMIT` or `ROLLBACK`.
+  **Table Locks ™**. When performing one of the following DML operations: `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and `SELECT …​ FOR UPDATE`, a transaction automatically acquires a table lock to prevent DDL modifications to the table that might cause conflicts if the transaction did not issue a `COMMIT` or `ROLLBACK`.

The following table provides additional information regarding row and table locks.


| Statement | Row locks | Table lock mode | RS | RX | S | SRX | X | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| SELECT …​ FROM table…​ | — | none | Y | Y | Y | Y | Y | 
| INSERT INTO table…​ | Yes | SX | Y | Y | N | N | N | 
| UPDATE table …​ | Yes | SX | Y | Y | N | N | N | 
| MERGE INTO table …​ | Yes | SX | Y | Y | N | N | N | 
| DELETE FROM table…​ | Yes | SX | Y | Y | N | N | N | 
| SELECT …​ FROM table FOR UPDATE OF…​ | Yes | SX | Y | Y | N | N | N | 
| LOCK TABLE table IN…​ | — |  |  |  |  |  |  | 
| ROW SHARE MODE |  | SS | Y | Y | Y | Y | N | 
| ROW EXCLUSIVE MODE |  | SX | Y | Y | N | N | N | 
| SHARE MODE |  | S | Y | N | Y | N | N | 
| SHARE ROW EXCLUSIVE MODE |  | SSX | Y | N | N | N | N | 
| EXCLUSIVE MODE |  | X | N | N | N | N | N | 

 **DDL locks** 

The main purpose of a DDL lock is to protect the definition of a schema object while it is modified by an ongoing DDL operation such as `ALTER TABLE EMPLOYEES ADD <COLUMN>`.

 **Explicit (Manual) data locking** 

Users have the ability to explicitly create locks to achieve transaction-level read consistency for when an application requires transactional exclusive access to a resource without waiting for other transactions to complete. Explicit data locking can be performed at the transaction level or the session level:
+ Transaction level
  +  `SET TRANSACTION ISOLATION LEVEL` 
  +  `LOCK TABLE` 
  +  `SELECT … FOR UPDATE` 
+ Session level
  +  `ALTER SESSION SET ISOLATION LEVEL` 

 **System locks** 

System locks include latches, mutexes, and internal locks.

 **Examples** 

Explicitly lock data using the `LOCK TABLE` command.

```
-- Session 1
LOCK TABLE EMPLOYEES IN EXCLUSIVE MODE;
-- Session 2
UPDATE EMPLOYEES
SET SALARY=SALARY+1000
WHERE EMPLOYEE_ID=114;
-- Session 2 waits for session 1 to COMMIT or ROLLBACK
```

Explicitly lock data using the `SELECT… FOR UPDATE` command. Oracle obtains exclusive row-level locks on all the rows identified by the `SELECT FOR UPDATE` statement.

```
-- Session 1
SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID=114 FOR UPDATE;
-- Session 2
UPDATE EMPLOYEES
SET SALARY=SALARY+1000
WHERE EMPLOYEE_ID=114;
-- Session 2 waits for session 1 to COMMIT or ROLLBACK
```

For more information, see [Automatic Locks in DDL Operations](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Automatic-Locks-in-DDL-Operations.html#GUID-84D392A3-94EC-444D-950F-7829DBCD43EE), [Automatic Locks in DML Operations](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Automatic-Locks-in-DML-Operations.html#GUID-3D57596F-8B73-4C80-8F4D-79A12F781EFD), and [Automatic and Manual Locking Mechanisms During SQL Operations](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Automatic-and-Manual-Locking-Mechanisms-During-SQL-Operations.html#GUID-0304C4AA-BD28-4C2A-B7F5-267532FB9499) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.mvcc.pg"></a>

PostgreSQL provides various lock modes to control concurrent access to data in tables. Data consistency is maintained using a Multi-Version Concurrency Control (MVCC) mechanism. Most PostgreSQL commands automatically acquire locks of appropriate modes to ensure that referenced tables aren’t dropped or modified in incompatible ways while the command runs.

The MVCC mechanism prevents viewing inconsistent data produced by concurrent transactions performing updates on the same rows. MVCC in PostgreSQL provides strong transaction isolation for each database session and minimizes lock-contention in multiuser environments.
+ Similar to Oracle, MVCC locks acquired for querying (reading) data don’t conflict with locks acquired for writing data. Reads will never block writes and writes never blocks reads.
+ Similar to Oracle, PostgreSQL doesn’t escalate locks to table-level, such as where an entire table is locked for writes when a certain threshold of row locks is exceeded.

### Implicit and explicit transactions (Auto-commit behavior)
<a name="chap-oracle-aurora-pg.sql.mvcc.pg.behavior"></a>

Unlike Oracle, PostgreSQL uses auto-commit for transactions by default. However, there are two options to support explicit transactions, which are similar to the default behavior in Oracle (non-auto-commit).
+ Use the `START TRANSACTION` (or `BEGIN TRANSACTION`) statements and then `COMMIT` or `ROLLBACK`.
+ Set `AUTOCOMMIT` to `OFF` at the session level.

```
\set AUTOCOMMIT off
```

With explicit transactions:
+ Users can explicitly issue a lock similar to the `LOCK TABLE` statement in Oracle.
+  `SELECT… FOR UPDATE` is supported.

Similar to Oracle, PostgreSQL automatically acquires the necessary locks to control concurrent access to data. PostgreSQL implements the following types of locks.

 **Table-level locks** 


| Requested and current lock modes | ACCESSSHARE | ROWSHARE | ROWEXCLUSIVE | SHAREUPDATEEXCLUSIVE | SHARE | SHAREROWEXCLUSIVE | EXCLUSIVE | ACCESSEXCLUSIVE | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| ACCESSSHARE |  |  |  |  |  |  |  | X | 
| ROWSHARE |  |  |  |  |  |  | X | X | 
| ROWEXCLUSIVE |  |  |  |  | X | X | X | X | 
| SHAREUPDATEEXCLUSIVE |  |  |  | X | X | X | X | X | 
| SHARE |  |  | X | X | X | X | X | X | 
| SHAREROWEXCLUSIVE |  |  | X | X | X | X | X | X | 
| EXCLUSIVE |  | X | X | X | X | X | X | X | 
| ACCESSEXCLUSIVE | X | X | X | X | X | X | X | X | 

 **Row-level locks** 


| Requested and current lock modes | FOR KEY SHARE | FOR SHARE | FOR NO KEY UPDATE | FOR UPDATE | 
| --- | --- | --- | --- | --- | 
| FOR KEY SHARE |  |  |  | X | 
| FOR SHARE |  |  | X | X | 
| FOR NO KEY UPDATE |  | X | X | X | 
| FOR UPDATE | X | X | X | X | 

 **Page-level locks** 

Shared or exclusive locks used to control read or write access to table pages in the shared buffer pool. They are released immediately after a row is fetched or updated.

 **Deadlocks** 

Occur when two or more transactions are waiting for one another to release each lock.

 **Transaction-level locking** 

PostgreSQL doesn’t support session isolation levels, although it can be controlled by transactions.
+  `SET TRANSACTION ISOLATION LEVEL` 
+  `LOCK TABLE` 
+  `SELECT … FOR UPDATE` 

 **PostgreSQL LOCK TABLE synopsis** 

```
LOCK [ TABLE ] [ ONLY ] name [ * ] [, ...] [ IN lockmode MODE ] [ NOWAIT ]
where lockmode is one of:
ACCESS SHARE | ROW SHARE | ROW EXCLUSIVE | SHARE UPDATE EXCLUSIVE | SHARE | SHARE ROW EXCLUSIVE | EXCLUSIVE | ACCESS EXCLUSIVE
```

If `ONLY` and `*` are specified, the command stops with an error.

There is no `UNLOCK TABLE` command. Locks are always released at the end of a transaction (`COMMIT` / `ROLLBACK`).

You can use the `LOCK TABLE` command inside a transaction and it should appear after the `START TRANSACTION` statement.

 **Examples** 

Obtain an explicit lock on a table using the `LOCK TABLE` command.

```
-- Session 1
START TRANSACTION;
LOCK TABLE EMPLOYEES IN EXCLUSIVE MODE;

-- Session 2
UPDATE EMPLOYEES
SET SALARY=SALARY+1000
WHERE EMPLOYEE_ID=114;

-- Session 2 waits for session 1 to COMMIT or ROLLBACK
```

Explicit lock by the `SELECT… FOR UPDATE` command. PostgreSQL obtains exclusive row-level locks on rows referenced by the `SELECT FOR UPDATE` statement. Must be ran inside a transaction.

```
-- Session 1
START TRANSACTION;
SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID=114 FOR UPDATE;

-- Session 2
UPDATE EMPLOYEES
SET SALARY=SALARY+1000
WHERE EMPLOYEE_ID=114;

-- Session 2 waits for session 1 to COMMIT or ROLLBACK
```

### PostgreSQL deadlocks
<a name="chap-oracle-aurora-pg.sql.mvcc.pg.deadlocks"></a>

Deadlocks occur when two or more transactions acquired locks on each other’s process resources (table or row). PostgreSQL can detect Deadlocks automatically and resolve the event by aborting one of the transactions, allowing the other transaction to complete.

Simulating a deadlock:

```
Session 1 - step1:
UPDATE accounts SET balance = balance + 100.00 WHERE acctnum = 11111;
Session 2 - step2:
UPDATE accounts SET balance = balance + 100.00 WHERE acctnum = 22222;
Session 2 step3:
UPDATE accounts SET balance = balance - 100.00 WHERE acctnum = 11111;
Session 1 - step4:
UPDATE accounts SET balance = balance - 100.00 WHERE acctnum = 22222;
```

Session 1 is waiting for Session 2 and Session 2 is waiting for Session 1 = deadlock.

Real-time monitoring of locks using catalog tables:
+  `pg_locks` 
+  `pg_stat_activity` 

Monitor locks using the following SQL query.

```
SELECT
block.pid AS block_pid,
block_stm.usename AS blocker_user,
block.mode AS block_mode,
block.locktype AS block_locktype,
block.relation::regclass AS block_table,
block_stm.query AS block_query,
block.GRANTED AS block_granted,
waiting.locktype AS waiting_locktype,
waiting_stm.usename AS waiting_user,
waiting.relation::regclass AS waiting_table,
waiting_stm.query AS waiting_query,
waiting.mode AS waiting_mode,
waiting.pid AS waiting_pid
from pg_catalog.pg_locks AS waiting JOIN
pg_catalog.pg_stat_activity AS waiting_stm
ON (waiting_stm.pid = waiting.pid)
join pg_catalog.pg_locks AS block
ON ((waiting."database" = block."database"
AND waiting.relation = block.relation)
OR waiting.transactionid = block.transactionid)
join pg_catalog.pg_stat_activity AS block_stm
ON (block_stm.pid = block.pid)
where NOT waiting.GRANTED
and waiting.pid <> block.pid;
```

Generate an explicit lock using the `SELECT… FOR UPDATE` statement.

```
-- Session 1
START TRANSACTION;
SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID=114 FOR UPDATE;

-- Session 2
UPDATE EMPLOYEES
SET SALARY=SALARY+1000
WHERE EMPLOYEE_ID=114;

-- Session 2 waits for session 1 to COMMIT or ROLLBACK
```

Run the SQL query from step \#1 monitoring locks while distinguishing between the “blocking” and “waiting” session.

```
-[ RECORD 1 ]-
block_pid        | 31743
blocker_user     | aurora_admin
block_mode       | ExclusiveLock
block_locktype   | transactionid
block_table      |
block_query      | SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID=114 FOR UPDATE;
block_granted    | t
waiting_locktype | transactionid
waiting_user     | aurora_admin
waiting_table    |
waiting_query    | UPDATE EMPLOYEES
                 | SET SALARY=SALARY+1000
                 | WHERE EMPLOYEE_ID=114;
waiting_mode     | ShareLock
waiting_pid      | 31996
```

## Summary
<a name="chap-oracle-aurora-pg.sql.mvcc.summary"></a>


| Description | Oracle | PostgreSQL | 
| --- | --- | --- | 
| Dictionary tables to obtain information about locks |  <pre>v$lock;<br />v$locked_object;<br />v$session_blockers;</pre>  |  <pre>pg_locks<br />pg_stat_activity</pre>  | 
| Lock a table |  <pre>BEGIN;<br />LOCK TABLE employees IN SHARE<br />ROW EXCLUSIVE MODE;</pre>  |  <pre>LOCK TABLE employees IN SHARE<br />ROW EXCLUSIVE MODE;</pre>  | 
| Explicit locking |  <pre>SELECT * FROM employees<br />WHERE employee_id=102 FOR UPDATE;</pre>  |  <pre>BEGIN;<br />SELECT * FROM employees WHERE<br />employee_id=102 FOR UPDATE;</pre>  | 
| Explicit locking, options |  <pre>SELECT…FOR UPDATE</pre>  |  <pre>SELECT … FOR…<br />KEY SHARE<br />SHARE<br />NO KEY UPDATE<br />UPDATE</pre>  | 

For more information, see [LOCK](https://www.postgresql.org/docs/13/sql-lock.html) and [Explicit Locking](https://www.postgresql.org/docs/13/explicit-locking.html) in the *PostgreSQL documentation*.