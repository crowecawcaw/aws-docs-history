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
time. When Aurora DSQL detects a conflict, it returns a PostgreSQL serialization failure with
SQLSTATE code `40001`. The response message includes an OCC code that identifies
the type of conflict:

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

## Guidelines for optimizing transaction performance

To optimize performance, minimize high contention on single keys or small key ranges. To
achieve this goal, design your schema to spread updates over your cluster key range by using
the following guidelines:

- Choose a random primary key for your tables.
- Avoid patterns that increase contention on single keys. This approach ensures
  optimal performance even as transaction volume grows.
