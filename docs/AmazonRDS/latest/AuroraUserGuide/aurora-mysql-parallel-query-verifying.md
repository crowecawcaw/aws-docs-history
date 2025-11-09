# Verifying which statements use parallel query for Aurora MySQL

In typical operation, you don't need to perform any special actions to take advantage of parallel
query. After a query meets the essential requirements for parallel query, the query optimizer
automatically decides whether to use parallel query for each specific query.

If you run experiments in a development or test environment, you might find that parallel
query isn't used because your tables are too small in number of rows or overall data
volume. The data for the table might also be entirely in the buffer pool, especially for
tables that you created recently to perform experiments.

As you monitor or tune cluster performance, make sure to decide whether parallel query is being used in the
appropriate contexts. You might adjust the database schema, settings, SQL queries, or even the cluster
topology and application connection settings to take advantage of this feature.

To check if a query is using parallel query, check the query plan (also known as the "explain
plan") by running the
[EXPLAIN](https://dev.mysql.com/doc/refman/5.7/en/execution-plan-information.html "https://dev.mysql.com/doc/refman/5.7/en/execution-plan-information.html")
statement. For examples of how SQL statements, clauses, and expressions affect `EXPLAIN` output
for parallel query,
see [SQL constructs for parallel query in Aurora MySQL](aurora-mysql-parallel-query-sql.md "aurora-mysql-parallel-query-sql.md").

The following example demonstrates the difference between a traditional query plan and a parallel query
plan. This explain plan is from Query 3 from the TPC-H benchmark. Many of the sample queries throughout this section
use the tables from the TPC-H dataset. You can get the table definitions, queries, and the `dbgen` program
that generates sample data from [the TPC-h website](http://www.tpc.org/tpch/ "http://www.tpc.org/tpch/").

```
EXPLAIN SELECT l_orderkey,
  sum(l_extendedprice * (1 - l_discount)) AS revenue,
  o_orderdate,
  o_shippriority
FROM customer,
  orders,
  lineitem
WHERE c_mktsegment = 'AUTOMOBILE'
AND c_custkey = o_custkey
AND l_orderkey = o_orderkey
AND o_orderdate < date '1995-03-13'
AND l_shipdate > date '1995-03-13'
GROUP BY l_orderkey,
  o_orderdate,
  o_shippriority
ORDER BY revenue DESC,
  o_orderdate LIMIT 10;

```

By default, the query might have a plan like the following. If you don't see hash
join used in the query plan, make sure that optimization is turned on first.

```
+----+-------------+----------+------------+------+---------------+------+---------+------+----------+----------+----------------------------------------------------+
| id | select_type | table    | partitions | type | possible_keys | key  | key_len | ref  | rows     | filtered | Extra                                              |
+----+-------------+----------+------------+------+---------------+------+---------+------+----------+----------+----------------------------------------------------+
|  1 | SIMPLE      | customer | NULL       | ALL  | NULL          | NULL | NULL    | NULL |  1480234 |    10.00 | Using where; Using temporary; Using filesort       |
|  1 | SIMPLE      | orders   | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 14875240 |     3.33 | Using where; Using join buffer (Block Nested Loop) |
|  1 | SIMPLE      | lineitem | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 59270573 |     3.33 | Using where; Using join buffer (Block Nested Loop) |
+----+-------------+----------+------------+------+---------------+------+---------+------+----------+----------+----------------------------------------------------+

```

For Aurora MySQL version 3, you turn on hash join at the session level by issuing the following statement.

```
SET optimizer_switch='block_nested_loop=on';
```

For Aurora MySQL version 2.09 and higher, you set the `aurora_disable_hash_join` DB parameter or DB cluster parameter
to `0` (off). Turning off `aurora_disable_hash_join` sets the value of `optimizer_switch` to
`hash_join=on`.

After you turn on hash join, try running the `EXPLAIN` statement again. For information about how to use hash joins
effectively, see [Optimizing large Aurora MySQL join queries with hash joins](AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin "AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin").

With hash join turned on but parallel query turned off, the query might have a plan
like the following, which uses hash join but not parallel query.

```
+----+-------------+----------+...+-----------+-----------------------------------------------------------------+
| id | select_type | table    |...| rows      | Extra                                                           |
+----+-------------+----------+...+-----------+-----------------------------------------------------------------+
|  1 | SIMPLE      | customer |...|   5798330 | Using where; Using index; Using temporary; Using filesort       |
|  1 | SIMPLE      | orders   |...| 154545408 | Using where; Using join buffer (Hash Join Outer table orders)   |
|  1 | SIMPLE      | lineitem |...| 606119300 | Using where; Using join buffer (Hash Join Outer table lineitem) |
+----+-------------+----------+...+-----------+-----------------------------------------------------------------+

```

After parallel query is turned on, two steps in this query plan can use the parallel
query optimization, as shown under the `Extra` column in the `EXPLAIN`
output. The I/O-intensive and CPU-intensive processing for those steps is pushed down to the
storage layer.

```
+----+...+--------------------------------------------------------------------------------------------------------------------------------+
| id |...| Extra                                                                                                                          |
+----+...+--------------------------------------------------------------------------------------------------------------------------------+
|  1 |...| Using where; Using index; Using temporary; Using filesort                                                                      |
|  1 |...| Using where; Using join buffer (Hash Join Outer table orders); **Using parallel query (4 columns, 1 filters, 1 exprs; 0 extra)**   |
|  1 |...| Using where; Using join buffer (Hash Join Outer table lineitem); **Using parallel query (4 columns, 1 filters, 1 exprs; 0 extra)** |
+----+...+--------------------------------------------------------------------------------------------------------------------------------+

```

For information about how to interpret `EXPLAIN` output for a parallel query and the parts of
SQL statements that parallel query can apply to, see
[SQL constructs for parallel query in Aurora MySQL](aurora-mysql-parallel-query-sql.md "aurora-mysql-parallel-query-sql.md").

The following example output shows the results of running the preceding query on a db.r4.2xlarge
instance with a cold buffer pool. The query runs substantially faster when using parallel query.

###### Note

Because timings depend on many environmental factors,
your results might be different. Always conduct your own performance tests
to confirm the findings with your own environment, workload, and so on.

```
-- Without parallel query
+------------+-------------+-------------+----------------+
| l_orderkey | revenue     | o_orderdate | o_shippriority |
+------------+-------------+-------------+----------------+
|   92511430 | 514726.4896 | 1995-03-06  |              0 |
.
.
|   28840519 | 454748.2485 | 1995-03-08  |              0 |
+------------+-------------+-------------+----------------+
10 rows in set (**24 min 49.99 sec**)

```

```
-- With parallel query
+------------+-------------+-------------+----------------+
| l_orderkey | revenue     | o_orderdate | o_shippriority |
+------------+-------------+-------------+----------------+
|   92511430 | 514726.4896 | 1995-03-06  |              0 |
.
.
|   28840519 | 454748.2485 | 1995-03-08  |              0 |
+------------+-------------+-------------+----------------+
10 rows in set (**1 min 49.91 sec**)

```

Many of the sample queries throughout this section use the tables from this TPC-H dataset, particularly
the `PART` table, which has 20 million rows and the following definition.

```
+---------------+---------------+------+-----+---------+-------+
| Field         | Type          | Null | Key | Default | Extra |
+---------------+---------------+------+-----+---------+-------+
| p_partkey     | int(11)       | NO   | PRI | NULL    |       |
| p_name        | varchar(55)   | NO   |     | NULL    |       |
| p_mfgr        | char(25)      | NO   |     | NULL    |       |
| p_brand       | char(10)      | NO   |     | NULL    |       |
| p_type        | varchar(25)   | NO   |     | NULL    |       |
| p_size        | int(11)       | NO   |     | NULL    |       |
| p_container   | char(10)      | NO   |     | NULL    |       |
| p_retailprice | decimal(15,2) | NO   |     | NULL    |       |
| p_comment     | varchar(23)   | NO   |     | NULL    |       |
+---------------+---------------+------+-----+---------+-------+

```

Experiment with your workload to get a sense of whether individual SQL statements can take advantage of
parallel query. Then use the following monitoring techniques to help verify how often parallel query is
used in real workloads over time. For real workloads, extra factors such as concurrency limits apply.
