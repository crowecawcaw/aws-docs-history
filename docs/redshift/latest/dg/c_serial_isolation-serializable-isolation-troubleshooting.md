Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting serializable isolation errors

## ERROR:1023

DETAIL: Serializable isolation violation on a table in Redshift

When Amazon Redshift detects a serializable isolation error, you see an error message such
as the following.

```
ERROR:1023 DETAIL: Serializable isolation violation on table in Redshift
```

To address a serializable isolation error, you can try the following
methods:

- Retry the canceled transaction.

Amazon Redshift detected that a concurrent workload is not serializable. It
suggests gaps in the application logic, which can usually be worked around
by retrying the transaction that encountered the error. If the issue
persists, try one of the other methods.

- Move any operations that don't have to be in the same atomic
  transaction outside of the transaction.

This method applies when individual operations inside two transactions
cross-reference each other in a way that can affect the outcome of the other
transaction. For example, the following two sessions each start a
transaction.

```
Session1_Redshift=# begin;
```

```
Session2_Redshift=# begin;
```

The result of a SELECT statement in each transaction might be affected by
an INSERT statement in the other. In other words, suppose that you run the
following statements serially, in any order. In every case, the result is
one of the SELECT statements returning one more row than if the transactions
were run concurrently. There is no order in which the operations can run
serially that produces the same result as when run concurrently. Thus, the
last operation that is run results in a serializable isolation error.

```
Session1_Redshift=# select * from tab1;
Session1_Redshift=# insert into tab2 values (1);
```

```
Session2_Redshift=# insert into tab1 values (1);
Session2_Redshift=# select * from tab2;
```

In many cases, the result of the SELECT statements isn't important.
In other words, the atomicity of the operations in the transactions
isn't important. In these cases, move the SELECT statements outside of
their transactions, as shown in the following examples.

```
Session1_Redshift=# begin;
Session1_Redshift=# insert into tab1 values (1)
Session1_Redshift=# end;
Session1_Redshift=# select * from tab2;
```

```
Session2_Redshift # select * from tab1;
Session2_Redshift=# begin;
Session2_Redshift=# insert into tab2 values (1)
Session2_Redshift=# end;
```

In these examples, there are no cross-references in the transactions. The
two INSERT statements don't affect each other. In these examples, there
is at least one order in which the transactions can run serially and produce
the same result as if run concurrently. This means that the transactions are
serializable.

- Force serialization by locking all tables in each session.

The [LOCK](r_LOCK.md "r_LOCK.md") command blocks
operations that can result in serializable isolation errors. When you use
the LOCK command, be sure to do the following:

    + Lock all tables affected by the transaction, including those
     affected by read-only SELECT statements inside the transaction.
    + Lock tables in the same order, regardless of the order that
     operations are performed in.
    + Lock all tables at the beginning of the transaction, before
     performing any operations.

- Use snapshot isolation for concurrent transactions

Use an ALTER DATABASE command with snapshot isolation. For more information about
the SNAPSHOT parameter for ALTER DATABASE, see
[Parameters](r_ALTER_DATABASE.md#r_ALTER_DATABASE-parameters "r_ALTER_DATABASE.md#r_ALTER_DATABASE-parameters").

## ERROR:1018

DETAIL: Relation does not exist

When you run concurrent Amazon Redshift operations in different sessions, you see an
error message such as the following.

```
ERROR: 1018 DETAIL: Relation does not exist.
```

Transactions in Amazon Redshift follow snapshot isolation. After a transaction begins,
Amazon Redshift takes a snapshot of the database. For the entire lifecycle of the
transaction, the transaction operates on the state of the database as reflected in
the snapshot. If the transaction reads from a table that doesn't exist in the
snapshot, it throws the 1018 error message shown previously. Even when another
concurrent transaction creates a table after the transaction has taken the
snapshot, the transaction can't read from the newly created table.

To address this serialization isolation error, you can try to move the start of
the transaction to a point where you know the table exists.

If the table is created by another transaction, this point is at least after
that transaction has been committed. Also, ensure that no concurrent transaction
has been committed that might have dropped the table.

```
session1 = # BEGIN;
session1 = # DROP TABLE A;
session1 = # COMMIT;
```

```
session2 = # BEGIN;
```

```
session3 = # BEGIN;
session3 = # CREATE TABLE A (id INT);
session3 = # COMMIT;
```

```
session2 = # SELECT * FROM A;
```

The last operation that is run as the read operation by session2 results in a
serializable isolation error. This error happens when session2 takes a snapshot
and the table has already been dropped by a committed session1. In other words,
even though a concurrent session3 has created the table, session2 doesn't see the
table because it's not in the snapshot.

To resolve this error, you can reorder the sessions as follows.

```
session1 = # BEGIN;
session1 = # DROP TABLE A;
session1 = # COMMIT;
```

```
session3 = # BEGIN;
session3 = # CREATE TABLE A (id INT);
session3 = # COMMIT;
```

```
session2 = # BEGIN;
session2 = # SELECT * FROM A;
```

Now when session2 takes its snapshot, session3 has already been committed, and
the table is in the database. Session2 can read from the table without any
error.
