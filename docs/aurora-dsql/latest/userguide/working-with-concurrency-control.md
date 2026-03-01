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

## Transaction conflicts

Aurora DSQL uses optimistic concurrency control (OCC), which works differently from
traditional lock-based systems. Instead of using locks, OCC evaluates conflicts at commit
time. When multiple transactions conflict while updating the same row, Aurora DSQL manages
transactions as follows:

- The transaction with the earliest commit time is processed by Aurora DSQL.
- Conflicting transactions receive a PostgreSQL serialization error, indicating the need
  to be retried.

Design your applications to implement retry logic to handle conflicts. The ideal design
pattern is idempotent, enabling transaction retry as a first recourse whenever possible. The
recommended logic is similar to the abort and retry logic in a standard PostgreSQL lock timeout
or deadlock situation. However, OCC requires your applications to exercise this logic more
frequently.

## Guidelines for optimizing transaction performance

To optimize performance, minimize high contention on single keys or small key ranges. To
achieve this goal, design your schema to spread updates over your cluster key range by using
the following guidelines:

- Choose a random primary key for your tables.
- Avoid patterns that increase contention on single keys. This approach ensures
  optimal performance even as transaction volume grows.
