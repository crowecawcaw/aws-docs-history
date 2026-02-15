# Querying Aurora PostgreSQL Limitless Database

Aurora PostgreSQL Limitless Database is compatible with PostgreSQL syntax for queries. You can query your Limitless Database using `psql` or any
other connection utility that works with PostgreSQL. To run queries, you connect to the limitless endpoint as shown in [Connecting to your Aurora PostgreSQL Limitless Database DB cluster](limitless-shard.md#limitless-endpoint "limitless-shard.md#limitless-endpoint").

All PostgreSQL `SELECT` queries are supported in Aurora PostgreSQL Limitless Database. However, queries are performed on two layers:

1. Router to which the client sends the query
2. Shards where the data is located
   Performance depends on querying the database in a way that allows it to achieve a high degree of simultaneous processing of different queries on
   different shards. Queries are first parsed in the distributed transaction layer (router). Before planning the query execution, there's an analysis phase
   to identify the location for all relations participating in the query. If all relations are sharded tables with a filtered shard key on the same shard,
   or reference tables, then query planning is skipped on the router layer and completely pushed down to the shard for planning and execution. This process
   reduces the number of round trips between different nodes (router and shard) and results in better performance in most cases. For more information, see
   [Single-shard queries in Aurora PostgreSQL Limitless Database](limitless-query.md "limitless-query.md").

###### Note

There can be specific cases, such as a [Cartesian product](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-FROM "https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-FROM")
(cross join), where the query performs better by retrieving data separately from the shard.

For more information on query execution plans, see [EXPLAIN](limitless-reference.md#limitless-reference.DML-limitations.EXPLAIN "limitless-reference.md#limitless-reference.DML-limitations.EXPLAIN") in the [Aurora PostgreSQL Limitless Database reference](limitless-reference.md "limitless-reference.md"). For general information on queries, see [Queries](https://www.postgresql.org/docs/current/queries-overview.html "https://www.postgresql.org/docs/current/queries-overview.html") in the PostgreSQL documentation.

###### Topics

- [Single-shard queries in Aurora PostgreSQL Limitless Database](limitless-query.md "limitless-query.md")
- [Distributed queries in Aurora PostgreSQL Limitless Database](limitless-query.md "limitless-query.md")
- [Distributed query tracing in PostgreSQL logs in Aurora PostgreSQL Limitless Database](limitless-query.md "limitless-query.md")
- [Distributed deadlocks in Aurora PostgreSQL Limitless Database](limitless-query.md "limitless-query.md")
