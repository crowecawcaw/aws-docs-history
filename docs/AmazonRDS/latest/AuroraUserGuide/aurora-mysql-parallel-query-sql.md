# SQL constructs for parallel query in Aurora MySQL

In the following section, you can find more detail about why particular SQL statements use or don't use
parallel query. This section also details how Aurora MySQL features interact with parallel query. This
information can help you diagnose performance issues for a cluster that uses parallel query or understand how
parallel query applies for your particular workload.

The decision to use parallel query relies on many factors that occur at the moment that the statement
runs. Thus, parallel query might be used for certain queries always, never, or only under certain
conditions.

###### Tip

When you view these examples in HTML, you can use the **Copy** widget in the
upper-right corner of each code listing to copy the SQL code to try yourself. Using the
**Copy** widget avoids copying the extra characters around the
`mysql>` prompt and `->` continuation lines.

###### Topics

- [EXPLAIN statement](#aurora-mysql-parallel-query-sql-explain "#aurora-mysql-parallel-query-sql-explain")
- [WHERE clause](#aurora-mysql-parallel-query-sql-where "#aurora-mysql-parallel-query-sql-where")
- [Data definition language (DDL)](#aurora-mysql-parallel-query-sql-ddl "#aurora-mysql-parallel-query-sql-ddl")
- [Column data types](#aurora-mysql-parallel-query-sql-datatypes "#aurora-mysql-parallel-query-sql-datatypes")
- [Partitioned tables](#aurora-mysql-parallel-query-sql-partitioning "#aurora-mysql-parallel-query-sql-partitioning")
- [Aggregate functions, GROUP BY clauses, and HAVING clauses](#aurora-mysql-parallel-query-sql-aggregation "#aurora-mysql-parallel-query-sql-aggregation")
- [Function calls in WHERE clause](#aurora-mysql-parallel-query-sql-functions "#aurora-mysql-parallel-query-sql-functions")
- [LIMIT clause](#aurora-mysql-parallel-query-sql-limit "#aurora-mysql-parallel-query-sql-limit")
- [Comparison operators](#aurora-mysql-parallel-query-sql-comparisons "#aurora-mysql-parallel-query-sql-comparisons")
- [Joins](#aurora-mysql-parallel-query-sql-joins "#aurora-mysql-parallel-query-sql-joins")
- [Subqueries](#aurora-mysql-parallel-query-sql-subqueries "#aurora-mysql-parallel-query-sql-subqueries")
- [UNION](#aurora-mysql-parallel-query-sql-union "#aurora-mysql-parallel-query-sql-union")
- [Views](#aurora-mysql-parallel-query-sql-views "#aurora-mysql-parallel-query-sql-views")
- [Data manipulation language (DML) statements](#aurora-mysql-parallel-query-sql-dml "#aurora-mysql-parallel-query-sql-dml")
- [Transactions and locking](#aurora-mysql-parallel-query-sql-transactions "#aurora-mysql-parallel-query-sql-transactions")
- [B-tree indexes](#aurora-mysql-parallel-query-sql-indexes "#aurora-mysql-parallel-query-sql-indexes")
- [Full-text search (FTS) indexes](#aurora-mysql-parallel-query-sql-fts "#aurora-mysql-parallel-query-sql-fts")
- [Virtual columns](#aurora-mysql-parallel-query-sql-virtual-column "#aurora-mysql-parallel-query-sql-virtual-column")
- [Built-in caching mechanisms](#aurora-mysql-parallel-query-sql-caching "#aurora-mysql-parallel-query-sql-caching")
- [Optimizer hints](#aurora-mysql-parallel-query-hints "#aurora-mysql-parallel-query-hints")
- [MyISAM temporary tables](#aurora-mysql-parallel-query-sql-myisam "#aurora-mysql-parallel-query-sql-myisam")

## EXPLAIN statement

As shown in examples throughout this section, the `EXPLAIN` statement indicates whether
each stage of a query is currently eligible for parallel query. It also indicates which aspects of a
query can be pushed down to the storage layer. The most important items in the query plan are the
following:

- A value other than `NULL` for the `key` column
  suggests that the query can be performed efficiently using index
  lookups, and parallel query is unlikely.
- A small value for the `rows` column (a value not in the
  millions) suggests that the query isn't accessing enough data to make
  parallel query worthwhile. This means that parallel query is unlikely.
- The `Extra` column shows you if parallel query is expected to be used. This output
  looks like the following example.

```
Using parallel query (`A` columns, `B` filters, `C` exprs; `D` extra)

```

The `columns` number represents how many columns are referred to in the query block.

The `filters` number represents the number of `WHERE` predicates
representing a simple comparison of a column value to a constant. The comparison can be for
equality, inequality, or a range. Aurora can parallelize these kinds of predicates most
effectively.

The `exprs` number represents the number of expressions such as function calls,
operators, or other expressions that can also be parallelized, though not as effectively as a
filter condition.

The `extra` number represents how many expressions can't be pushed down and are
performed by the head node.

For example, consider the following `EXPLAIN` output.

```
`mysql>` explain select p_name, p_mfgr from part
    `->` where p_brand is not null
    `->` and upper(p_type) is not null
    `->` and round(p_retailprice) is not null;
`+----+-------------+-------+...+----------+----------------------------------------------------------------------------+
| id | select_type | table |...| rows | Extra |
+----+-------------+-------+...+----------+----------------------------------------------------------------------------+
| 1 | SIMPLE | part |...| 20427936 | **Using where; Using parallel query (5 columns, 1 filters, 2 exprs; 0 extra)** |
+----+-------------+-------+...+----------+----------------------------------------------------------------------------+`

```

The information from the `Extra` column shows that five columns are extracted from each row to
evaluate the query conditions and construct the result set. One `WHERE` predicate involves a filter, that is,
a column that is directly tested in the `WHERE` clause. Two `WHERE` clauses require evaluating
more complicated expressions, in this case involving function calls. The `0 extra` field confirms that all the
operations in the `WHERE` clause are pushed down to the storage layer as part of parallel query processing.

In cases where parallel query isn't chosen, you can typically deduce the reason from
the other columns of the `EXPLAIN` output. For example, the `rows`
value might be too small, or the `possible_keys` column might indicate that the
query can use an index lookup instead of a data-intensive scan. The following example shows a query where
the optimizer can estimate that the query will scan only a small number of rows. It does so based on the
characteristics of the primary key. In this case, parallel query isn't required.

```
`mysql>` explain select count(*) from part where p_partkey between 1 and 100;
`+----+-------------+-------+-------+---------------+---------+---------+------+------+--------------------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+----+-------------+-------+-------+---------------+---------+---------+------+------+--------------------------+
| 1 | SIMPLE | part | range | **PRIMARY** | PRIMARY | 4 | NULL | **99** | Using where; **Using index** |
+----+-------------+-------+-------+---------------+---------+---------+------+------+--------------------------+`

```

The output showing whether parallel query will be used takes into account all available factors at
the moment that the `EXPLAIN` statement is run. The optimizer might make a different
choice when the query is actually run, if the situation changed in the meantime. For example,
`EXPLAIN` might report that a statement will use parallel query. But when the query is
actually run later, it might not use parallel query based on the conditions then. Such conditions
can include several other parallel queries running concurrently. They can also include rows being
deleted from the table, a new index being created, too much time passing within an open transaction, and so on.

## WHERE clause

For a query to use the parallel query optimization, it
_must_ include a `WHERE` clause.

The parallel query optimization speeds up many kinds of expressions used in the
`WHERE` clause:

- Simple comparisons of a column value to a constant, known as
  _filters_. These comparisons benefit the most from being pushed
  down to the storage layer. The number of filter expressions in a query is reported in the
  `EXPLAIN` output.
- Other kinds of expressions in the `WHERE` clause are also pushed down to the storage
  layer where possible. The number of such expressions in a query is reported in the
  `EXPLAIN` output. These expressions can be function calls, `LIKE`
  operators, `CASE` expressions, and so on.
- Certain functions and operators aren't currently pushed down by parallel query. The number of
  such expressions in a query is reported as the `extra` counter in the
  `EXPLAIN` output. The rest of the query can still use parallel query.
- While expressions in the select list aren't pushed down, queries containing such functions
  can still benefit from reduced network traffic for the intermediate results of parallel queries.
  For example, queries that call aggregation functions in the select list can benefit from
  parallel query, even though the aggregation functions aren't pushed down.

For example, the following query does a full-table scan and processes all
the values for the `P_BRAND` column. However, it doesn't use parallel
query because the query doesn't include any `WHERE` clause.

```
`mysql>` explain select count(*), p_brand from part group by p_brand;
`+----+-------------+-------+------+---------------+------+---------+------+----------+---------------------------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+----+-------------+-------+------+---------------+------+---------+------+----------+---------------------------------+
| 1 | SIMPLE | part | ALL | NULL | NULL | NULL | NULL | 20427936 | Using temporary; Using filesort |
+----+-------------+-------+------+---------------+------+---------+------+----------+---------------------------------+`

```

In contrast, the following query includes `WHERE` predicates that filter the results,
so parallel query can be applied:

```
`mysql>` explain select count(*), p_brand from part where p_name is not null
 `->` and p_mfgr in ('Manufacturer#1', 'Manufacturer#3') and p_retailprice > 1000
 `->` group by p_brand;
`+----+...+----------+-------------------------------------------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+----------+-------------------------------------------------------------------------------------------------------------+
| 1 |...| 20427936 | Using where; Using temporary; Using filesort; **Using parallel query (5 columns, 1 filters, 2 exprs; 0 extra)** |
+----+...+----------+-------------------------------------------------------------------------------------------------------------+`

```

If the optimizer estimates that the number of returned rows for a query block is small, parallel query
isn't used for that query block. The following example shows a case where a greater-than operator on the
primary key column applies to millions of rows, which causes parallel query to be used. The
converse less-than test is estimated to apply to only a few rows and doesn't use parallel query.

```
`mysql>` explain select count(*) from part where p_partkey > 10;
`+----+...+----------+----------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+----------+----------------------------------------------------------------------------+
| 1 |...| 20427936 | Using where; **Using parallel query (1 columns, 1 filters, 0 exprs; 0 extra)** |
+----+...+----------+----------------------------------------------------------------------------+`

`mysql>` explain select count(*) from part where p_partkey < 10;
`+----+...+------+--------------------------+
| id |...| rows | Extra |
+----+...+------+--------------------------+
| 1 |...| 9 | Using where; Using index |
+----+...+------+--------------------------+`

```

## Data definition language (DDL)

In Aurora MySQL version 2, parallel query is only available for tables for which no fast data definition language (DDL)
operations are pending. In Aurora MySQL version 3, you can use parallel query on a table at the same time as an instant DDL
operation.

Instant DDL in Aurora MySQL version 3 replaces the fast DDL feature in Aurora MySQL version 2. For information about instant
DDL, see [Instant DDL (Aurora MySQL version 3)](AuroraMySQL.Managing.md#AuroraMySQL.mysql80-instant-ddl "AuroraMySQL.Managing.md#AuroraMySQL.mysql80-instant-ddl").

## Column data types

In Aurora MySQL version 3, parallel query can work with tables containing columns with
data types `TEXT`, `BLOB`, `JSON`, and `GEOMETRY`. It
can also work with `VARCHAR` and `CHAR` columns with a maximum declared length
longer than 768 bytes. If your query refers to any columns containing such large object types, the
additional work to retrieve them does add some overhead to query processing. In that case, check if
the query can omit the references to those columns. If not, run benchmarks to confirm if such queries
are faster with parallel query turned on or turned off.

In Aurora MySQL version 2, parallel query has these limitations for large object types:

- `TEXT`, `BLOB`, `JSON`, and `GEOMETRY` data types aren't
  supported with parallel query. A query that refers to any columns of these types can't use parallel
  query.
- Variable-length columns (`VARCHAR` and `CHAR` data types) are compatible with parallel query
  up to a maximum declared length of 768 bytes. A query that refers to any columns of the types declared with a longer
  maximum length can't use parallel query. For columns that use multibyte character sets, the byte limit takes
  into account the maximum number of bytes in the character set. For example, for the character set
  `utf8mb4` (which has a maximum character length of 4 bytes), a `VARCHAR(192)` column is
  compatible with parallel query but a `VARCHAR(193)` column isn't.

## Partitioned tables

You can use partitioned tables with parallel query in Aurora MySQL version 3. Because partitioned tables
are represented internally as multiple smaller tables, a query that uses parallel query on a nonpartitioned
table might not use parallel query on an identical partitioned table. Aurora MySQL considers whether each partition
is large enough to qualify for the parallel query optimization, instead of evaluating the size of the entire table.
Check whether the `Aurora_pq_request_not_chosen_small_table` status variable is incremented if a query
on a partitioned table doesn't use parallel query when you expect it to.

For example, consider one table partitioned with
`PARTITION BY HASH (`column`) PARTITIONS 2`
and another table partitioned with
`PARTITION BY HASH (`column`) PARTITIONS 10`.
In the table with two partititions, the partitions are five times as large as the
table with ten partitions. Thus, parallel query is more likely to be used for
queries against the table with fewer partitions. In the following example,
the table `PART_BIG_PARTITIONS` has two partitions and
`PART_SMALL_PARTITIONS` has ten partitions. With identical data,
parallel query is more likely to be used for the table with fewer big partitions.

```

mysql> explain select count(*), p_brand from part_big_partitions where p_name is not null
    ->   and p_mfgr in ('Manufacturer#1', 'Manufacturer#3') and p_retailprice > 1000 group by p_brand;
+----+-------------+---------------------+------------+-------------------------------------------------------------------------------------------------------------------+
| id | select_type | table               | partitions | Extra                                                                                                             |
+----+-------------+---------------------+------------+-------------------------------------------------------------------------------------------------------------------+
|  1 | SIMPLE      | part_big_partitions | p0,p1      | Using where; Using temporary; Using parallel query (4 columns, 1 filters, 1 exprs; 0 extra; 1 group-bys, 1 aggrs) |
+----+-------------+---------------------+------------+-------------------------------------------------------------------------------------------------------------------+

mysql> explain select count(*), p_brand from part_small_partitions where p_name is not null
    ->   and p_mfgr in ('Manufacturer#1', 'Manufacturer#3') and p_retailprice > 1000 group by p_brand;
+----+-------------+-----------------------+-------------------------------+------------------------------+
| id | select_type | table                 | partitions                    | Extra                        |
+----+-------------+-----------------------+-------------------------------+------------------------------+
|  1 | SIMPLE      | part_small_partitions | p0,p1,p2,p3,p4,p5,p6,p7,p8,p9 | Using where; Using temporary |
+----+-------------+-----------------------+-------------------------------+------------------------------+

```

## Aggregate functions, GROUP BY clauses, and HAVING clauses

Queries involving aggregate functions are often good candidates for parallel query, because they
involve scanning large numbers of rows within large tables.

In Aurora MySQL 3, parallel query can optimize aggregate function calls in the select
list and the `HAVING` clause.

Before Aurora MySQL 3, aggregate function calls in the select list or the `HAVING` clause
aren't pushed down to the storage layer. However, parallel query can still improve the performance
of such queries with aggregate functions. It does so by first extracting column values from the raw data pages
in parallel at the storage layer. It then transmits those values back to the head node in a compact tuple format
instead of as entire data pages. As always, the query requires at least one `WHERE` predicate for
parallel query to be activated.

The following simple examples illustrate the kinds of aggregate queries that can benefit from
parallel query. They do so by returning intermediate results in compact form to the head node,
filtering nonmatching rows from the intermediate results, or both.

```
`mysql>` explain select sql_no_cache count(distinct p_brand) from part where p_mfgr = 'Manufacturer#5';
`+----+...+----------------------------------------------------------------------------+
| id |...| Extra |
+----+...+----------------------------------------------------------------------------+
| 1 |...| Using where; **Using parallel query (2 columns, 1 filters, 0 exprs; 0 extra)** |
+----+...+----------------------------------------------------------------------------+`

`mysql>` explain select sql_no_cache p_mfgr from part where p_retailprice > 1000 group by p_mfgr having count(*) > 100;
`+----+...+-------------------------------------------------------------------------------------------------------------+
| id |...| Extra |
+----+...+-------------------------------------------------------------------------------------------------------------+
| 1 |...| Using where; Using temporary; Using filesort; **Using parallel query (3 columns, 0 filters, 1 exprs; 0 extra)** |
+----+...+-------------------------------------------------------------------------------------------------------------+`

```

## Function calls in WHERE clause

Aurora can apply the parallel query optimization to calls to most built-in functions
in the `WHERE` clause. Parallelizing these function calls offloads some CPU work
from the head node. Evaluating the predicate functions in parallel during the earliest query
stage helps Aurora minimize the amount of data transmitted and processed during later stages.

Currently, the parallelization doesn't apply to function calls in the select list.
Those functions are evaluated by the head node, even if identical function calls appear in
the `WHERE` clause. The original values from relevant columns are included in the
tuples transmitted from the storage nodes back to the head node. The head node performs any
transformations such as `UPPER`, `CONCATENATE`, and so on to
produce the final values for the result set.

In the following example, parallel query parallelizes the call to `LOWER` because it
appears in the `WHERE` clause. Parallel query doesn't affect the calls to
`SUBSTR` and `UPPER` because they appear in the select list.

```
`mysql>` explain select sql_no_cache distinct substr(upper(p_name),1,5) from part
 `->` where lower(p_name) like '%cornflower%' or lower(p_name) like '%goldenrod%';
`+----+...+---------------------------------------------------------------------------------------------+
| id |...| Extra |
+----+...+---------------------------------------------------------------------------------------------+
| 1 |...| Using where; Using temporary; Using parallel query (2 columns, 0 filters, **1 exprs**; 0 extra) |
+----+...+---------------------------------------------------------------------------------------------+`

```

The same considerations apply to other expressions, such as `CASE` expressions or
`LIKE` operators. For example, the following example shows that parallel query evaluates
the `CASE` expression and `LIKE` operators in the `WHERE` clause.

```
`mysql>` explain select p_mfgr, p_retailprice from part
 `->` where p_retailprice > case p_mfgr
 `->`   when 'Manufacturer#1' then 1000
 `->`   when 'Manufacturer#2' then 1200
 `->`   else 950
 `->` end
 `->` and p_name like '%vanilla%'
 `->` group by p_retailprice;
`+----+...+-------------------------------------------------------------------------------------------------------------+
| id |...| Extra |
+----+...+-------------------------------------------------------------------------------------------------------------+
| 1 |...| Using where; Using temporary; Using filesort; Using parallel query (4 columns, 0 filters, **2 exprs**; 0 extra) |
+----+...+-------------------------------------------------------------------------------------------------------------+`

```

## LIMIT clause

Currently, parallel query isn't used for any query block that includes a `LIMIT`
clause. Parallel query might still be used for earlier query phases with `GROUP` by,
`ORDER BY`, or joins.

## Comparison operators

The optimizer estimates how many rows to scan to evaluate comparison operators, and determines
whether to use parallel query based on that estimate.

The first example following shows that an equality comparison against the primary key column can be
performed efficiently without parallel query. The second example following shows that a similar
comparison against an unindexed column requires scanning millions of rows and therefore can benefit
from parallel query.

```
`mysql>` explain select * from part where p_partkey = 10;
`+----+...+------+-------+
| id |...| rows | Extra |
+----+...+------+-------+
| 1 |...| 1 | NULL |
+----+...+------+-------+`

`mysql>` explain select * from part where p_type = 'LARGE BRUSHED BRASS';
`+----+...+----------+----------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+----------+----------------------------------------------------------------------------+
| 1 |...| 20427936 | Using where; Using parallel query (9 columns, 1 filters, 0 exprs; 0 extra) |
+----+...+----------+----------------------------------------------------------------------------+`

```

The same considerations apply for not-equals tests and for range comparisons such as less than,
greater than or equal to, or `BETWEEN`. The optimizer estimates the number of rows to
scan, and determines whether parallel query is worthwhile based on the overall volume of I/O.

## Joins

Join queries with large tables typically involve data-intensive operations that benefit from the
parallel query optimization. The comparisons of column values between multiple tables (that is, the
join predicates themselves) currently aren't parallelized. However, parallel query can push down
some of the internal processing for other join phases, such as constructing the Bloom filter during
a hash join. Parallel query can apply to join queries even without a `WHERE` clause.
Therefore, a join query is an exception to the rule that a `WHERE` clause is required to
use parallel query.

Each phase of join processing is evaluated to check if it is eligible for parallel query. If more
than one phase can use parallel query, these phases are performed in sequence. Thus, each join query
counts as a single parallel query session in terms of concurrency limits.

For example, when a join query includes `WHERE` predicates to filter the rows from one of
the joined tables, that filtering option can use parallel query. As another example, suppose that a
join query uses the hash join mechanism, for example to join a big table with a small table. In this
case, the table scan to produce the Bloom filter data structure might be able to use parallel query.

###### Note

Parallel query is typically used for the kinds of resource-intensive queries that benefit from the hash join optimization.
The method for turning on the hash join optimization depends on the Aurora MySQL version. For details for each version, see
[Turning on hash join for parallel query clusters](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join").
For information about how to use hash joins effectively, see
[Optimizing large Aurora MySQL join queries with hash joins](AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin "AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin").

```
`mysql>` explain select count(*) from orders join customer where o_custkey = c_custkey;
`+----+...+----------+-------+---------------+-------------+...+-----------+-----------------------------------------------------------------------------------------------------------------+
| id |...| table | type | possible_keys | key |...| rows | Extra |
+----+...+----------+-------+---------------+-------------+...+-----------+-----------------------------------------------------------------------------------------------------------------+
| 1 |...| customer | index | PRIMARY | c_nationkey |...| 15051972 | Using index |
| 1 |...| orders | ALL | o_custkey | NULL |...| 154545408 | Using join buffer (Hash Join Outer table orders); Using parallel query (1 columns, 0 filters, 1 exprs; 0 extra) |
+----+...+----------+-------+---------------+-------------+...+-----------+-----------------------------------------------------------------------------------------------------------------+`

```

For a join query that uses the nested loop mechanism, the outermost nested loop block might use parallel query.
The use of parallel query depends on the same factors as usual, such as the presence of additional filter conditions
in the `WHERE` clause.

```
`mysql>` -- Nested loop join with extra filter conditions can use parallel query.
`mysql>` explain select count(*) from part, partsupp where p_partkey != ps_partkey and p_name is not null and ps_availqty > 0;
`+----+-------------+----------+...+----------+----------------------------------------------------------------------------+
| id | select_type | table |...| rows | Extra |
+----+-------------+----------+...+----------+----------------------------------------------------------------------------+
| 1 | SIMPLE | part |...| 20427936 | Using where; Using parallel query (2 columns, 1 filters, 0 exprs; 0 extra) |
| 1 | SIMPLE | partsupp |...| 78164450 | Using where; Using join buffer (Block Nested Loop) |
+----+-------------+----------+...+----------+----------------------------------------------------------------------------+`

```

## Subqueries

The outer query block and inner subquery block might each use parallel query, or not. Whether they do is based on the
usual characteristics of the table, `WHERE` clause, and so on, for each block. For
example, the following query uses parallel query for the subquery block but not the outer block.

```
`mysql>` explain select count(*) from part where
 `-->` p_partkey < (select max(p_partkey) from part where p_name like '%vanilla%');
`+----+-------------+...+----------+----------------------------------------------------------------------------+
| id | select_type |...| rows | Extra |
+----+-------------+...+----------+----------------------------------------------------------------------------+
| 1 | PRIMARY |...| NULL | Impossible WHERE noticed after reading const tables |
| 2 | SUBQUERY |...| 20427936 | Using where; Using parallel query (2 columns, 0 filters, 1 exprs; 0 extra) |
+----+-------------+...+----------+----------------------------------------------------------------------------+`

```

Currently, correlated subqueries can't use the parallel query optimization.

## UNION

Each query block in a `UNION` query can use parallel query, or not, based on the usual
characteristics of the table, `WHERE` clause, and so on, for each part of the
`UNION`.

```
`mysql>` explain select p_partkey from part where p_name like '%choco_ate%'
 `->` union select p_partkey from part where p_name like '%vanil_a%';
`+----+----------------+...+----------+----------------------------------------------------------------------------+
| id | select_type |...| rows | Extra |
+----+----------------+...+----------+----------------------------------------------------------------------------+
| 1 | PRIMARY |...| 20427936 | Using where; Using parallel query (2 columns, 0 filters, 1 exprs; 0 extra) |
| 2 | UNION |...| 20427936 | Using where; Using parallel query (2 columns, 0 filters, 1 exprs; 0 extra) |
| NULL | UNION RESULT | <union1,2> |...| NULL | Using temporary |
+----+--------------+...+----------+----------------------------------------------------------------------------+`

```

###### Note

Each `UNION` clause within the query is run sequentially. Even if the
query includes multiple stages that all use parallel query, it only runs a single parallel
query at any one time. Therefore, even a complex multistage query only counts as 1 toward
the limit of concurrent parallel queries.

## Views

The optimizer rewrites any query using a view as a longer query using the underlying tables. Thus,
parallel query works the same whether table references are views or real tables. All the same
considerations about whether to use parallel query for a query, and which parts are pushed down,
apply to the final rewritten query.

For example, the following query plan shows a view definition that usually doesn't use parallel
query. When the view is queried with additional `WHERE` clauses, Aurora MySQL uses parallel
query.

```
`mysql>` create view part_view as select * from part;
`mysql>` explain select count(*) from part_view where p_partkey is not null;
`+----+...+----------+----------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+----------+----------------------------------------------------------------------------+
| 1 |...| 20427936 | Using where; Using parallel query (1 columns, 0 filters, 0 exprs; 1 extra) |
+----+...+----------+----------------------------------------------------------------------------+`

```

## Data manipulation language (DML) statements

The `INSERT` statement can use parallel query for the `SELECT`
phase of processing, if the `SELECT` part meets the other conditions for
parallel query.

```
`mysql>` create table part_subset like part;
`mysql>` explain insert into part_subset select * from part where p_mfgr = 'Manufacturer#1';
`+----+...+----------+----------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+----------+----------------------------------------------------------------------------+
| 1 |...| 20427936 | Using where; Using parallel query (9 columns, 1 filters, 0 exprs; 0 extra) |
+----+...+----------+----------------------------------------------------------------------------+`

```

###### Note

Typically, after an `INSERT` statement, the data for the newly inserted rows is in the
buffer pool. Therefore, a table might not be eligible for parallel query immediately after
inserting a large number of rows. Later, after the data is evicted from the buffer pool during
normal operation, queries against the table might begin using parallel query again.

The `CREATE TABLE AS SELECT` statement doesn't use parallel query, even if the
`SELECT` portion of the statement would otherwise be eligible for parallel query. The DDL
aspect of this statement makes it incompatible with parallel query processing. In contrast, in the
`INSERT ... SELECT` statement, the `SELECT` portion can use parallel query.

Parallel query is never used for `DELETE` or `UPDATE` statements,
regardless of the size of the table and predicates in the `WHERE` clause.

```
`mysql>` explain delete from part where p_name is not null;
`+----+-------------+...+----------+-------------+
| id | select_type |...| rows | Extra |
+----+-------------+...+----------+-------------+
| 1 | SIMPLE |...| 20427936 | Using where |
+----+-------------+...+----------+-------------+`

```

## Transactions and locking

You can use all the isolation levels on the Aurora primary instance.

On Aurora reader DB instances, parallel query applies to statements performed under the `REPEATABLE READ`
isolation level. Aurora MySQL version 2.09 or higher can also use the `READ COMMITTED` isolation level on reader DB
instances. `REPEATABLE READ` is the default isolation level for Aurora reader DB instances. To use `READ
 COMMITTED` isolation level on reader DB instances requires setting the
`aurora_read_replica_read_committed` configuration option at the session level. The `READ
 COMMITTED` isolation level for reader instances complies with SQL standard behavior. However, the isolation is
less strict on reader instances than when queries use `READ COMMITTED` isolation level on the writer
instance.

For more information about Aurora isolation levels, especially the differences in `READ COMMITTED`
between writer and reader instances, see
[Aurora MySQL isolation levels](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md").

After a big transaction is finished, the table statistics might be stale. Such stale statistics
might require an `ANALYZE TABLE` statement before Aurora can accurately estimate
the number of rows. A large-scale DML statement might also bring a substantial portion of the table
data into the buffer pool. Having this data in the buffer pool can lead to parallel query being
chosen less frequently for that table until the data is evicted from the pool.

When your session is inside a long-running transaction (by default, 10 minutes), further queries
inside that session don't use parallel query. A timeout can also occur during a single long-running
query. This type of timeout might happen if the query runs for longer than the maximum interval
(currently 10 minutes) before the parallel query processing starts.

You can reduce the chance of starting long-running transactions accidentally by setting
`autocommit=1` in `mysql` sessions where you perform ad hoc (one-time)
queries. Even a `SELECT` statement against a table begins a transaction by creating a
read view. A _read view_ is a consistent set of data for subsequent
queries that remains until the transaction is committed. Be aware of this restriction also when
using JDBC or ODBC applications with Aurora, because such applications might run with the
`autocommit` setting turned off.

The following example shows how, with the `autocommit` setting turned off, running a
query against a table creates a read view that implicitly begins a transaction. Queries that are run
shortly afterward can still use parallel query. However, after a pause of several minutes, queries
are no longer eligible for parallel query. Ending the transaction with `COMMIT` or
`ROLLBACK` restores parallel query eligibility.

```
`mysql>` set autocommit=0;

`mysql>` explain select sql_no_cache count(*) from part where p_retailprice > 10.0;
`+----+...+---------+----------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+---------+----------------------------------------------------------------------------+
| 1 |...| 2976129 | Using where; Using parallel query (1 columns, 1 filters, 0 exprs; 0 extra) |
+----+...+---------+----------------------------------------------------------------------------+`

`mysql>` select sleep(720); explain select sql_no_cache count(*) from part where p_retailprice > 10.0;
`+------------+
| sleep(720) |
+------------+
| 0 |
+------------+
1 row in set (12 min 0.00 sec)

+----+...+---------+-------------+
| id |...| rows | Extra |
+----+...+---------+-------------+
| 1 |...| 2976129 | Using where |
+----+...+---------+-------------+`

`mysql>` commit;

`mysql>` explain select sql_no_cache count(*) from part where p_retailprice > 10.0;
`+----+...+---------+----------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+---------+----------------------------------------------------------------------------+
| 1 |...| 2976129 | Using where; **Using parallel query** (1 columns, 1 filters, 0 exprs; 0 extra) |
+----+...+---------+----------------------------------------------------------------------------+`

```

To see how many times queries weren't eligible for parallel query because they were inside
long-running transactions, check the status variable `Aurora_pq_request_not_chosen_long_trx`.

```
`mysql>` show global status like '%pq%trx%';
`+---------------------------------------+-------+
| Variable_name | Value |
+---------------------------------------+-------+
| Aurora_pq_request_not_chosen_long_trx | 4 |
+-------------------------------+-------+`

```

Any `SELECT` statement that acquires locks, such as the
`SELECT FOR UPDATE` or `SELECT LOCK IN SHARE MODE` syntax, can't use parallel query.

Parallel query can work for a table that is locked by a `LOCK TABLES` statement.

```
`mysql>` explain select o_orderpriority, o_shippriority from orders where o_clerk = 'Clerk#000095055';
`+----+...+-----------+----------------------------------------------------------------------------+
| id |...| rows | Extra |
+----+...+-----------+----------------------------------------------------------------------------+
| 1 |...| 154545408 | Using where; Using parallel query (3 columns, 1 filters, 0 exprs; 0 extra) |
+----+...+-----------+----------------------------------------------------------------------------+`

`mysql>` explain select o_orderpriority, o_shippriority from orders where o_clerk = 'Clerk#000095055' for update;
`+----+...+-----------+-------------+
| id |...| rows | Extra |
+----+...+-----------+-------------+
| 1 |...| 154545408 | Using where |
+----+...+-----------+-------------+`

```

## B-tree indexes

The statistics gathered by the `ANALYZE TABLE` statement help the optimizer to decide
when to use parallel query or index lookups, based on the characteristics of the data for each
column. Keep statistics current by running `ANALYZE TABLE` after DML operations that make
substantial changes to the data within a table.

If index lookups can perform a query efficiently without a data-intensive scan, Aurora might use
index lookups. Doing so avoids the overhead of parallel query processing. There are also concurrency
limits on the number of parallel queries that can run simultaneously on any Aurora DB cluster. Make
sure to use best practices for indexing your tables, so that your most frequent and most highly
concurrent queries use index lookups.

## Full-text search (FTS) indexes

Currently, parallel query isn't used for tables that contain a full-text search index,
regardless of whether the query refers to such indexed columns or uses the
`MATCH` operator.

## Virtual columns

Currently, parallel query isn't used for tables that contain a virtual column,
regardless of whether the query refers to any virtual columns.

## Built-in caching mechanisms

Aurora includes built-in caching mechanisms, namely the buffer pool and the query cache. The Aurora
optimizer chooses between these caching mechanisms and parallel query depending on which one is most
effective for a particular query.

When a parallel query filters rows and transforms and extracts column values, data is transmitted
back to the head node as tuples rather than as data pages. Therefore, running a parallel query
doesn't add any pages to the buffer pool, or evict pages that are already in the buffer pool.

Aurora checks the number of pages of table data that are present in the buffer pool, and what
proportion of the table data that number represents. Aurora uses that information to determine
whether it is more efficient to use parallel query (and bypass the data in the buffer pool).
Alternatively, Aurora might use the nonparallel query processing path, which uses data cached in the
buffer pool. Which pages are cached and how data-intensive queries affect caching and eviction
depends on configuration settings related to the buffer pool. Therefore, it can be hard to predict
whether any particular query uses parallel query, because the choice depends on the ever-changing
data within the buffer pool.

Also, Aurora imposes concurrency limits on parallel queries. Because not every query uses parallel query,
tables that are accessed by multiple queries simultaneously typically have a substantial portion of their data
in the buffer pool. Therefore, Aurora often doesn't choose these tables for parallel queries.

When you run a sequence of nonparallel queries on the same table, the first query might be slow due
to the data not being in the buffer pool. Then the second and subsequent queries are much faster
because the buffer pool is now "warmed up". Parallel queries typically show consistent
performance from the very first query against the table. When conducting performance tests,
benchmark the nonparallel queries with both a cold and a warm buffer pool. In some cases, the
results with a warm buffer pool can compare well to parallel query times. In these cases, consider
factors such as the frequency of queries against that table. Also consider whether it is worthwhile
to keep the data for that table in the buffer pool.

The query cache avoids rerunning a query when an identical query is submitted and the underlying
table data hasn't changed. Queries optimized by parallel query feature can go into the query cache,
effectively making them instantaneous when run again.

###### Note

When conducting performance comparisons, the query cache can produce artificially
low timing numbers. Therefore, in benchmark-like situations, you can use the
`sql_no_cache` hint. This hint prevents the result from being served from the
query cache, even if the same query had been run previously. The hint comes immediately
after the `SELECT` statement in a query. Many parallel query examples in this
topic include this hint, to make query times comparable between versions of the query for
which parallel query is turned on and turned off.

Make sure that you remove this hint from your source when you move to production use of parallel query.

## Optimizer hints

Another way to control the optimizer is by using optimizer hints, which can be specified within individual statements. For
example, you can turn on an optimization for one table in a statement, and then turn off the optimization for a different
table. For more information about these hints, see [Optimizer Hints](https://dev.mysql.com/doc/refman/8.0/en/optimizer-hints.html "https://dev.mysql.com/doc/refman/8.0/en/optimizer-hints.html") in the _MySQL Reference Manual_.

You can use SQL hints with Aurora MySQL queries to fine-tune performance. You can also use hints to prevent execution plans
for important queries from changing because of unpredictable conditions.

We have extended the SQL hints feature to help you control optimizer choices for your query plans. These hints apply to
queries that use parallel query optimization. For more information, see [Aurora MySQL hints](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md").

## MyISAM temporary tables

The parallel query optimization only applies to InnoDB tables. Because Aurora MySQL
uses MyISAM behind the scenes for temporary tables, internal query phases involving
temporary tables never use parallel query. These query phases are indicated by `Using
 temporary` in the `EXPLAIN` output.
