# Aurora DSQL and PostgreSQL

Aurora DSQL is a PostgreSQL-compatible, distributed relational database designed for transactional
workloads. Aurora DSQL uses core PostgreSQL components such as the parser, planner, optimizer, and type
system.

The Aurora DSQL design ensures that all supported PostgreSQL syntax provides compatible behavior and
yields identical query results. For example, Aurora DSQL provides type conversions, arithmetic
operations, and numerical precision and scale that are identical to PostgreSQL. Any deviations are
documented.

Aurora DSQL also introduces advanced capabilities such as optimistic concurrency control and
distributed schema management. With these features, you can use the familiar tooling of PostgreSQL
while benefiting from the performance and scalability of a modern, cloud-native,
distributed applications.

## PostgreSQL compatibility highlights

Aurora DSQL is currently based on PostgreSQL version 16. Key highlights include the
following:

**Wire protocol**

Aurora DSQL uses the standard PostgreSQL v3 wire protocol. This enables integration with
standard PostgreSQL clients, drivers, and tools. For example, Aurora DSQL is compatible with
`psql`, `pgjdbc`, and `psycopg`.

**SQL syntax**

Aurora DSQL supports a wide range of standard PostgreSQL expressions and functions commonly
used in transactional workloads. Supported SQL expressions yield identical results to
PostgreSQL, including the following:

- Handling of nulls
- Sort order behavior
- Scale and precision for numeric operations
- Equivalence for string operations

For more information, see [SQL feature compatibility in
Aurora DSQL](working-with-postgresql-compatibility.md "working-with-postgresql-compatibility.md").

**Transaction management**

Aurora DSQL preserves the primary characteristics of PostgreSQL, such as ACID transactions
and an isolation level equivalent to PostgreSQL Repeatable Read. For more information, see
[Concurrency control in Aurora DSQL](working-with-concurrency-control.md "working-with-concurrency-control.md").

## Distributed architecture benefits

The distributed, shared-nothing design of Aurora DSQL provides performance and scalability
benefits beyond traditional single-node databases. Key capabilities include the following:

**Optimistic Concurrency Control (OCC)**

Aurora DSQL uses an optimistic concurrency control model. This lock-free approach
prevents transactions from blocking one another, eliminates deadlocks, and enables
high-throughput parallel execution. These features make Aurora DSQL particularly valuable for
applications requiring consistent performance at scale. For more example, see [Concurrency control in Aurora DSQL](working-with-concurrency-control.md "working-with-concurrency-control.md").

**Asynchronous DDL operations**

Aurora DSQL runs DDL operations asynchronously, which allows uninterrupted reads and
writes during schema changes. Its distributed architecture allows Aurora DSQL to perform the
following actions:

- Run DDL operations as background tasks, minimizing disruption.
- Coordinate catalog changes as strongly consistent distributed transactions. This
  ensures atomic visibility across all nodes, even during failures or concurrent
  operations.
- Operate in a fully distributed, leaderless manner across multiple Availability
  Zones with decoupled compute and storage layers.

For more on using the EXPLAIN command in PostgreSQL, see [DDL and distributed transactions in Aurora DSQL](working-with-ddl.md "working-with-ddl.md").
