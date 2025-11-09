Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Isolation levels in Amazon Redshift

Concurrent write operations are supported in Amazon Redshift in a protective way, using
write locks on tables and the principle of _serializable isolation_.
Serializable isolation preserves the illusion that a transaction running against a table
is the only transaction that is running against that table.

Amazon Redshift databases support concurrent write operations by having each operation use
the latest committed version, or snapshot, of their data at the start of the transaction.
A database snapshot is created within a transaction on the first occurrence of most
SELECT statements, DML commands such as COPY, DELETE, INSERT, UPDATE, and
TRUNCATE, and the following DDL commands:

- ALTER TABLE (to add or drop columns)
- CREATE TABLE
- DROP TABLE
- TRUNCATE TABLE
  No other transaction is able to change this snapshot, meaning transactions
  are isolated from one another. That is, concurrent transactions are invisible
  to each other and can’t detect each other's changes.

ny concurrent execution of transactions must produce the same results as
the serial execution of those transactions. If no serial execution of those
transactions can produce the same results, the transaction that runs a statement
that might break the ability to serialize is stopped and rolled back.

For example, suppose that a user attempts to run two concurrent transactions,
T1 and T2. Running T1 and T2 must produce the same results as at least one
of the following scenarios:

- T1 and T2 run serially in that order.
- T2 and T1 run serially in that order.

Isolation levels in Amazon Redshift prevent the following problems:

- Dirty reads ‐ A dirty read occurs when a transaction reads data
  that has not yet been committed. For example, suppose transaction 1
  updates a row. Transaction 2 reads the updated row before T1 commits the update.
  If T1 rolls back the change, T2 will have read data in uncommitted rows that
  Amazon Redshift now considers to never have existed.
- Non-repeatable reads ‐ A non-repeatable read occurs when a single
  transaction reads the same row twice but gets different data each time.
  For example, suppose transaction 1 reads a row. Transaction 2 updates
  or deletes that row and commits the update or delete. If T1
  rereads the row, it retrieves different row values or discovers that
  the row has been deleted.
- Phantoms – A phantom is a row that matches the search criteria but is
  not initially seen. For example, suppose transaction 1 reads a set
  of rows that satisfies its search criteria. Transaction 2 generates
  a new row in an UPDATE or INSERT statement that matches the
  search criteria for T1. If T1 reruns its search statement, it gets a different set of rows.

## SNAPSHOT

and SERIALIZABLE isolation

SNAPSHOT and SERIALIZABLE isolation are the two serializable isolation levels
available in Amazon Redshift.

SNAPSHOT isolation is the default isolation level when creating provisioned
clusters and serverless workgroups, letting you process larger volumes of data
than SERIALIZABLE isolation in less time.

SERIALIZABLE isolation takes more time, but implements stricter constraints on
concurrent transactions. This isolation level prevents problems such as write-skew
anomalies by only allowing one transaction to commit, while canceling all
other concurrent transaction with an serializable isolation violation error.

Following is a timeline example of how two concurrent write operations would be
handled when using SNAPSHOT isolation. Each user’s UPDATE statement is allowed
to commit because they don’t conflict by attempting to update the same rows.

| Time | User 1 action                                                       | User 2 action                                                       |
| ---- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 1    | BEGIN;                                                              |                                                                     |
| 2    |                                                                     | BEGIN;                                                              |
| 3    | SELECT \<br>• FROM Numbers;<br>`<br>digits<br>------<br>0<br>1<br>` |                                                                     |
| 4    |                                                                     | SELECT \<br>• FROM Numbers;<br>`<br>digits<br>------<br>0<br>1<br>` |
| 5    | UPDATE Numbers SET digits=0 WHERE<br>digits=1;                      |                                                                     |
| 6    | SELECT \<br>• FROM Numbers;<br>`<br>digits<br>------<br>0<br>0<br>` |                                                                     |
| 7    | COMMIT;                                                             |                                                                     |
| 8    |                                                                     | Update Numbers SET digits=1 WHERE<br>digits=0;                      |
| 9    |                                                                     | SELECT \<br>• FROM Numbers;<br>`<br>digits<br>------<br>1<br>1<br>` |
| 10   |                                                                     | COMMIT;                                                             |
| 11   | SELECT \<br>• FROM Numbers;<br>`<br>digits<br>------<br>1<br>0<br>` |                                                                     |
| 12   |                                                                     | SELECT \<br>• FROM Numbers;<br>`<br>digits<br>------<br>1<br>0<br>` |

If the same scenario is run using serializable isolation, then Amazon Redshift
terminates user 2 due to a serializable violation and returns error
`1023`. For more information, see [Troubleshooting serializable isolation errors](c_serial_isolation-serializable-isolation-troubleshooting.md "c_serial_isolation-serializable-isolation-troubleshooting.md").
In this case, only user 1 can commit successfully.

## Considerations

When using isolation levels in Amazon Redshift, consider the following:

- Query the STV_DB_ISOLATION_LEVEL catalog view to view which isolation level
  your database is using. For more information, see
  [STV_DB_ISOLATION_LEVEL](r_STV_DB_ISOLATION_LEVEL.md "r_STV_DB_ISOLATION_LEVEL.md").
- Query the PG_DATABASE_INFO view to see how many concurrent transactions are
  supported for your database. For more information, see
  [PG_DATABASE_INFO](r_PG_DATABASE_INFO.md "r_PG_DATABASE_INFO.md").
- System catalog tables (PG) and other Amazon Redshift system tables aren't locked
  in a transaction. Therefore, changes to database objects that arise
  from DDL and TRUNCATE operations are visible on commit to any
  concurrent transactions.

For example, suppose that table A exists in the database when
two concurrent transactions, T1 and T2, start. Suppose that T2
returns a list of tables by selecting from the PG_TABLES catalog
table. Then T1 drops table A and commits, and then T2 lists the
tables again. Table A is now no longer listed. If T2 tries to
query the dropped table, Amazon Redshift returns a "relation does not
exist" error. The catalog query that returns the list of tables
to T2 or checks that table A exists isn't subject to the same
isolation rules as operations performed on user tables.

Transactions for updates to these tables
run in a read committed isolation mode.

- PG-prefix catalog tables don't support SNAPSHOT isolation.
