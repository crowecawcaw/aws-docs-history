# Concurrency control in Aurora DSQL

_Concurrency_ allows multiple sessions to access and modify data
simultaneously without compromising data integrity and consistency. Aurora DSQL provides [PostgreSQL
compatibility](working-with-postgresql-compatibility.md "working-with-postgresql-compatibility.md") while implementing a modern, lock-free concurrency control mechanism.
It maintains full ACID compliance through snapshot isolation, ensuring data consistency and
reliability.

A key advantage of Aurora DSQL is its lock-free architecture, which eliminates common database
performance bottlenecks. Aurora DSQL prevents slow transactions from blocking other operations and
eliminates the risk of deadlocks. This approach makes Aurora DSQL particularly valuable for
high-throughput applications where performance and scalability are critical.

## Concurrency control responses

Aurora DSQL uses optimistic concurrency control (OCC), which works differently from
traditional lock-based systems. Instead of using locks, OCC evaluates conflicts at commit
time. This process of commit time conflict evaluation is also called adjudication.
When Aurora DSQL detects a conflict, it returns a PostgreSQL serialization failure with SQLSTATE code
`40001`. The response message includes an OCC code that identifies the type of conflict:

**OC000 — Data conflict**

Two transactions attempted to modify the same row. The transaction with the
earliest commit time succeeds, and the conflicting transaction receives the OC000
response:

```
ERROR: change conflicts with another transaction (OC000) (SQLSTATE 40001)
```

**OC001 — Schema conflict**

The session's cached schema catalog is out of date. When Aurora DSQL detects that the
catalog version has changed since the session loaded its cache, and the transaction
can't safely rebase to the current version, the transaction receives the OC001
response:

```
ERROR: schema has been updated by another transaction (OC001) (SQLSTATE 40001)
```

Any operation that modifies the schema catalog can cause an OC001 response,
including DDL statements such as `CREATE TABLE` and `ALTER
 TABLE`, as well as `GRANT` and `REVOKE` statements.
For more information, see [DDL and distributed transactions in Aurora DSQL](working-with-ddl.md "working-with-ddl.md").

Design your applications to implement retry logic to handle these responses. The ideal
design pattern is idempotent, enabling transaction retry as a first recourse whenever
possible. The recommended logic is similar to the abort and retry logic in a standard PostgreSQL
lock timeout or deadlock situation. However, OCC requires your applications to exercise this
logic more frequently.

## Data conflict types

Because of the Aurora DSQL concurrency control mechanism, the `SELECT ... FOR
 UPDATE` and `SELECT ... FOR KEY SHARE` clauses produce results through
optimistic conflict detection at commit time rather than locking. In Aurora DSQL, when one
transaction writes a row and another reads it with one of the preceding clauses, a conflict
might surface at commit time depending on which columns the transactions use. The following
clauses determine how Aurora DSQL detects these conflicts.

###### Key column definition

**Key columns** are columns that are members of a unique,
non-partial, non-expression index. All other columns are non-key columns.

**`SELECT ... FOR UPDATE`**

Declares that Aurora DSQL adjudicates the selected rows as if the transaction writes to
them. If another transaction runs `UPDATE`, `DELETE`, `SELECT
 ... FOR UPDATE`, or `SELECT ... FOR KEY SHARE` on the same row and
commits first, the transaction that ran `SELECT ... FOR UPDATE` fails with an
`OC000` response. This clause conflicts with any concurrent write to the row, and with
concurrent `FOR UPDATE` or `FOR KEY SHARE` reads.

**`SELECT ... FOR KEY SHARE`**

Declares that the transaction depends on the key columns of the selected rows.
If another transaction deletes the row, changes its key columns, or runs `SELECT
 ... FOR UPDATE` and commits first, the transaction that ran `SELECT ... FOR
 KEY SHARE` fails with an `OC000` response. A concurrent `UPDATE` to
non-key columns doesn't conflict.

Aurora DSQL doesn't support the `NO KEY UPDATE` or `FOR SHARE` clauses.
However, DML implicitly uses the `NO KEY UPDATE` mechanism. The following matrix
summarizes when two concurrent transactions that access the same row conflict. An `X`
indicates that the two operations conflict: whichever transaction commits last fails with an
`OC000` response. A blank cell indicates that both transactions can commit.

| Operation                                                                 | `INSERT`, `DELETE`, `UPDATE` (key columns), or<br>`SELECT ... FOR UPDATE` | `UPDATE` (non-key columns only) | `SELECT ... FOR KEY SHARE` |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------- | -------------------------- |
| `INSERT`, `DELETE`, `UPDATE` (key columns), or<br>`SELECT ... FOR UPDATE` | X                                                                         | X                               | X                          |
| `UPDATE` (non-key columns only)                                           | X                                                                         | X                               |                            |
| `SELECT ... FOR KEY SHARE`                                                | X                                                                         |                                 |                            |

## Guidelines for optimizing transaction performance

To optimize performance, minimize high contention on single keys or small key ranges. To
achieve this goal, design your schema to spread updates over your cluster key range by using
the following guidelines:

- Choose a random primary key for your tables.
- Avoid patterns that increase contention on single keys. This approach ensures
  optimal performance even as transaction volume grows.
