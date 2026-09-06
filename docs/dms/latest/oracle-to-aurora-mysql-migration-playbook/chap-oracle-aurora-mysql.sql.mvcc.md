

# Multi-Version Concurrency Control
<a name="chap-oracle-aurora-mysql.sql.mvcc"></a>

With AWS DMS, you can implement Multi-Version Concurrency Control (MVCC) to manage concurrent access to data during database migrations. MVCC is a concurrency control method that maintains multiple versions of database objects, allowing readers and writers to access the data simultaneously without blocking or causing conflicts.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-5.png)  | N/A | N/A | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.mvcc.oracle"></a>

Two primary lock types exist in Oracle: exclusive locks and share locks, which implement the following high-level locking semantics:
+ Writers never block readers.
+ Readers never block writers.
+ Oracle never escalates locks from row to page and table level, which reduces potential deadlocks.
+ In Oracle, users can issue explicit locks on specific tables using the `LOCK TABLE` statement.

Lock types can be divided into four categories: DML locks, DDL locks, Explicit (Manual) data locking, and System locks. The following sections describe each category.

### DML Locks
<a name="chap-oracle-aurora-mysql.sql.mvcc.oracle.dmllocks"></a>

DML locks preserve the integrity of data accessed concurrently by multiple users. DML statements acquire locks automatically both on row and table levels.
+  **Row locks or TX** — Obtained on a single row of a table by one the following statements: `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and `SELECT …​ FOR UPDATE`. If a transaction obtains a row lock, a table lock is also acquired to prevent DDL modifications to the table that might cause conflicts. The lock exists until the transaction ends with a `COMMIT` or `ROLLBACK`.
+  **Table locks or TM** — When performing one of the following DML operations: `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and `SELECT …​ FOR UPDATE`, a transaction automatically acquires a table lock to prevent DDL modifications to the table that might cause conflicts if the transaction did not issue a `COMMIT` or `ROLLBACK`.

All table lock types:
+  **Row share lock or RS** — Occurs when the transaction holding the lock on the table has locked some rows in the table before updating them.
+  **Row Exclusive lock or RX** — Occurs when the transaction holding the lock has updated table rows or used the `SELECT …​ FOR UPDATE` command.
+  **Share table lock or S** — One transaction locks the table and allows other transactions to query the table (exclude `SELECT …​ FOR UPDATE`), it also allows updates only if a single transaction holds the share table lock. Multiple transactions may hold a share table lock concurrently.
+  **Share row exclusive table lock or SRX** — Similar to S lock but with this lock, only a single transaction at a time can acquire this lock on a given table.
+  **Exclusive table lock or X** — Most restrictive lock type, it allows the transaction that holds the lock an exclusive write access to the table. Only one transaction can obtain an X lock for a table.

The following table provides additional information regarding row and table locks.


| Statement | Row locks | Table lock mode | RS | RX | S | SRX | X | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  `SELECT …​ FROM table …​`  | — | none | Y | Y | Y | Y | Y | 
|  `INSERT INTO table …​`  | Yes | SX | Y | Y | N | N | N | 
|  `UPDATE table …​`  | Yes | SX | Y | Y | N | N | N | 
|  `MERGE INTO table …​`  | Yes | SX | Y | Y | N | N | N | 
|  `DELETE FROM table …​`  | Yes | SX | Y | Y | N | N | N | 
|  `SELECT …​ FROM table FOR UPDATE OF…​`  | Yes | SX | Y | Y | N | N | N | 
|  `LOCK TABLE table IN…​`  | — |  |  |  |  |  |  | 
|  `ROW SHARE MODE`  |  | SS | Y | Y | Y | Y | N | 
|  `ROW EXCLUSIVE MODE`  |  | SX | Y | Y | N | N | N | 
|  `SHARE MODE`  |  | S | Y | N | Y | N | N | 
|  `SHARE ROW EXCLUSIVE MODE`  |  | SSX | Y | N | N | N | N | 
|  `EXCLUSIVE MODE`  |  | X | N | N | N | N | N | 

### DDL Locks
<a name="chap-oracle-aurora-mysql.sql.mvcc.oracle.ddllocks"></a>

The main purpose of a DDL lock is to protect the definition of a schema object while it is modified by an ongoing DDL operation such as `ALTER TABLE EMPLOYEES ADD <COLUMN>`.

### Explicit or manual data locking
<a name="chap-oracle-aurora-mysql.sql.mvcc.oracle.manual"></a>

Users have the ability to explicitly create locks to achieve transaction-level read consistency for when an application requires transactional exclusive access to a resource without waiting for other transactions to complete. Explicit data locking can be performed at the transaction level or the session level:
+ Transaction level
  +  `SET TRANSACTION ISOLATION LEVEL` 
  +  `LOCK TABLE` 
  +  `SELECT … FOR UPDATE` 
+ Session level
  +  `ALTER SESSION SET ISOLATION LEVEL` 

### System locks
<a name="chap-oracle-aurora-mysql.sql.mvcc.oracle.system"></a>

System locks include latches, mutexes, and internal locks.

### Examples
<a name="chap-oracle-aurora-mysql.sql.mvcc.oracle.examples"></a>

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

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql"></a>

When using InnoDB, MySQL provides various lock modes to control concurrent access to data in tables. Data consistency is maintained using a Multi-Version Concurrency Control (MVCC) mechanism. Most MySQL commands automatically acquire locks of appropriate modes to ensure that referenced tables are not dropped or modified in incompatible ways while the command runs.

The MVCC mechanism prevents viewing inconsistent data produced by concurrent transactions performing updates on the same rows. MVCC provides strong transaction isolation for each database session and minimizes lock-contention in multi-user environments.
+ Similar to Oracle, MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data. Reads never block writes and writes never blocks reads.
+ Similar to Oracle, MySQL does not escalate locks to table-level such as when an entire table is locked for writes when a certain threshold of row locks is exceeded.

InnoDB uses three additional fields for each row:
+  `DB_TRX_ID` — Indicates the transaction identifier for the last transaction that inserted or updated the row.
+  `DB_ROLL_PTR` — Points to an undo log record written to the rollback segment.
+  `DB_ROW_ID` — Contains a row ID that increases monotonically as new rows are inserted.

### Implicit and explicit transactions (Auto-commit behavior)
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.behavior"></a>

Unlike Oracle, MySQL uses auto-commit for transactions by default. However, there are two options to support explicit transactions, which are similar to the default behavior in Oracle (non-auto-commit).
+ Use the `START TRANSACTION` (or `BEGIN TRANSACTION`) statements and then `COMMIT` or `ROLLBACK`.
+ Set `AUTOCOMMIT` to `OFF` at the session level.

With explicit transactions:
+ Users can explicitly issue a lock similar to the `LOCK TABLE` statement in Oracle.
+  `SELECT… FOR UPDATE` is supported.

Unlike Oracle there are only two types of table-level locks when using the `LOCK TABLE` command: read lock and write lock.

### Read lock or shared S lock
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.readlock"></a>
+ The session that holds the lock can only read the table.
+ Multiple sessions can acquire a `READ` lock for the table at the same time.
+ Other sessions can read the table without explicitly acquiring a `READ` lock.
+ For InnoDB tables, `READ LOCAL` is the same as `READ`.

### Write lock or exclusive X lock
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.writelock"></a>
+ The session that holds the lock can read and write the table.
+ Only the session that holds the lock can access the table. No other session can access it until the lock is released.
+ Lock requests for the table by other sessions block while the `WRITE` lock is held.
+ The `LOW_PRIORITY` modifier is deprecated and has no effect.

For row-level locking:
+  **Intention shared IS lock** — Indicates that a transaction intends to set a shared lock.
+  **Intention exclusive IX lock** — Indicates that a transaction intends to set an exclusive lock.


|  | X | IX | S | IS | 
| --- | --- | --- | --- | --- | 
| X | Not permitted | Not permitted | Not permitted | Not permitted | 
| IX | Not permitted | Permitted | Not permitted | Permitted | 
| S | Not permitted | Not permitted | Permitted | Permitted | 
| IS | Not permitted | Permitted | Permitted | Permitted | 

### Records lock
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.records"></a>

A record lock is a lock on an index record. For example, the `SELECT id FROM emps WHERE id = 50 FOR UPDATE` query prevents any other transaction from inserting, updating, or deleting rows where the value of `emps.id` is 50.

Record locks always lock index records, even if a table is defined with no indexes. For such cases, InnoDB creates a hidden clustered index and uses it for record locking.

### Gaps lock
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.gaps"></a>

A gap lock is a lock on a gap between index records, before the first index record, or after the last index record. For example, `SELECT id FROM emps WHERE id BETWEEN 50 and 80 FOR UPDATE` prevents other transactions from inserting a value of 60 into the `emps.id` column whether or not there was already any value in the column because the gaps between all existing values in the range are locked.

### Transaction-level locking
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.transaction"></a>
+  `SET TRANSACTION ISOLATION LEVEL` 
+  `LOCK TABLE` 
+  `SELECT …​ FOR UPDATE` 

### Syntax
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.syntax"></a>

```
LOCK TABLES
tbl_name [[AS] alias] lock_type [, tbl_name [[AS] alias] lock_type] ...

lock_type:
READ [LOCAL] | [LOW_PRIORITY] WRITE
```

### MySQL deadlocks
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.deadlocks"></a>

Deadlocks occur when two or more transactions acquired locks on each other’s process resources such as table or row. MySQL can detect deadlocks automatically and resolve the event by aborting one of the transactions and allowing the other transaction to complete.

### Examples
<a name="chap-oracle-aurora-mysql.sql.mvcc.mysql.examples"></a>

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

Explicit lock by the `SELECT… FOR UPDATE` command. MySQL obtains exclusive row-level locks on rows referenced by the `SELECT FOR UPDATE` statement. Make sure that this statement runs inside a transaction.

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

## Summary
<a name="chap-oracle-aurora-mysql.sql.mvcc.summary"></a>


| Description | Oracle | MySQL | 
| --- | --- | --- | 
| Dictionary tables to obtain information about locks |  <pre>v$lock;<br />v$locked_object;<br />v$session_blockers;</pre>  |  <pre>SHOW OPEN TABLES WHERE in_use = 1;</pre>  | 
| Lock a table |  <pre>BEGIN;<br />LOCK TABLE employees IN<br />SHARE ROW EXCLUSIVE MODE;</pre>  |  <pre>LOCK TABLE employees READ</pre>  | 
| Explicit locking |  <pre>SELECT * FROM employees<br />WHERE employee_id=102 FOR UPDATE;</pre>  |  <pre>SELECT * FROM employees<br />WHERE employee_id=102 FOR UPDATE;</pre>  | 
| Explicit locking, options |  <pre>SELECT ... FOR UPDATE</pre>  |  <pre>SELECT ... FOR UPDATE</pre>  | 

For more information, see [InnoDB Multi-Versioning](https://dev.mysql.com/doc/refman/5.7/en/innodb-multi-versioning.html), [LOCK TABLES and UNLOCK TABLES Statements](https://dev.mysql.com/doc/refman/5.7/en/lock-tables.html), and [SET TRANSACTION Statement](https://dev.mysql.com/doc/refman/5.7/en/set-transaction.html) in the *MySQL documentation*.