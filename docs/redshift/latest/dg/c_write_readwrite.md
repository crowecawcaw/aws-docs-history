Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Write and read/write operations

You can manage the specific behavior of concurrent write operations by deciding when
and how to run different types of commands. The following commands are relevant to this
discussion:

- COPY commands, which perform loads (initial or incremental)
- INSERT commands that append one or more rows at a time
- UPDATE commands, which modify existing rows
- DELETE commands, which remove rows
  COPY and INSERT operations are pure write operations. DELETE and UPDATE operations
  are read/write operations (for rows to be deleted or updated, they have to be read first).
  The results of concurrent write operations depend on the specific commands that are being
  run concurrently.

UPDATE and DELETE operations behave differently because they rely on an initial table
read before they do any writes. Given that concurrent transactions are invisible to each other,
both UPDATEs and DELETEs have to read a snapshot of the data from the last commit. When
the first UPDATE or DELETE releases its lock, the second UPDATE or DELETE needs to determine
whether the data that it is going to work with is potentially stale. It will not be stale,
because the second transaction does not obtain its snapshot of data until after the
first transaction has released its lock.

## Potential deadlock situation

for concurrent write transactions involving multiple tables

When transactions involve updates of more than one table, there is always the
possibility of concurrently running transactions becoming deadlocked when they both
try to write to the same set of tables. A transaction releases all of its table
locks at once when it either commits or rolls back; it doesn't relinquish
locks one at a time.

For example, suppose that transactions T1 and T2 start at roughly the same time.
If T1 starts writing to table A and T2 starts writing to table B, both transactions
can proceed without conflict. However, if T1 finishes writing to table A and needs
to start writing to table B, it won’t be able to proceed because T2 still holds
the lock on B. Similarly, if T2 finishes writing to table B and needs to start writing
to table A, it will not be able to proceed either because T1 still holds the lock on A.
Because neither transaction can release its locks until all its write operations are
committed, neither transaction can proceed. To avoid this kind of deadlock,
you need to schedule concurrent write operations carefully. For example, you should
always update tables in the same order in transactions and, if specifying locks,
lock tables in the same order before you perform any DML operations.

## Potential deadlock situation

for concurrent write transactions involving a single table

In a snapshot isolation environment, deadlocks can occur when running concurrent
write transactions on the same table. The snapshot isolation deadlock happens when concurrent
INSERT or COPY statements are sharing a lock and making progress, and another statement needs
to perform an operation (UPDATE, DELETE, MERGE, or DDL operation) that requires an exclusive
lock on the same table.

Consider the following scenario:

Transaction 1 (T1):

```
INSERT/COPY INTO table_A;
```

Transaction 2 (T2):

```
INSERT/COPY INTO table_A;
            <UPDATE/DELETE/MERGE/DDL statement> table_A
```

A deadlock can occur when multiple transactions with INSERT or COPY
operations are running concurrently on the same table with a shared
lock, and one of those transactions follows its pure write operation
with an operation that requires an exclusive lock, such as an UPDATE,
MERGE, DELETE, or DDL statement.

To avoid the deadlock in these situations, you can separate statements
requiring an exclusive lock (UPDATE/MERGE/DELETE/DDL statements) to a
different transaction so that any INSERT/COPY statements can progress
simultaneously, and the statements requiring exclusive locks can execute
after them. Alternatively, for transactions with INSERT/COPY statements
and MERGE/UPDATE/MERGE statements on same table, you can include retry
logic in your applications to work around potential deadlocks.
