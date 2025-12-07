# Best practices for Aurora MySQL performance and scaling

You can apply the following best practices to improve the performance and scalability of
your Aurora MySQL clusters.

###### Topics

- [Using T instance classes for development and testing](#AuroraMySQL.BestPractices.T2Medium "#AuroraMySQL.BestPractices.T2Medium")
- [Optimizing Aurora MySQL indexed join queries with asynchronous key prefetch](#Aurora.BestPractices.AKP "#Aurora.BestPractices.AKP")
- [Optimizing large Aurora MySQL join queries with hash joins](#Aurora.BestPractices.HashJoin "#Aurora.BestPractices.HashJoin")
- [Using Amazon Aurora to scale reads for
  your MySQL database](#AuroraMySQL.BestPractices.ReadScaling "#AuroraMySQL.BestPractices.ReadScaling")
- [Optimizing timestamp operations](#AuroraMySQL.BestPractices.Performance.TimeZone "#AuroraMySQL.BestPractices.Performance.TimeZone")
- [Virtual index ID overflow errors](#AuroraMySQL.BestPractices.Performance.VirtualIndexIDOverflow "#AuroraMySQL.BestPractices.Performance.VirtualIndexIDOverflow")

## Using T instance classes for development and testing

Amazon Aurora MySQL instances that use the `db.t2`, `db.t3`, or `db.t4g` DB instance classes are
best suited for applications that do not support a high workload for an extended amount of time. The T instances are
designed to provide moderate baseline performance and the capability to burst to significantly higher performance as
required by your workload. They are intended for workloads that don't use the full CPU often or consistently, but
occasionally need to burst. We recommend using the T DB instance classes only for development and test servers, or other
non-production servers. For more details on the T instance classes, see [Burstable performance instances](../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md "../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md").

If your Aurora cluster is larger than 40 TB, don't use the T instance classes. When your database has a
large volume of data, the memory overhead for managing schema objects can exceed the capacity of a T instance.

Don't enable the MySQL Performance Schema on Amazon Aurora MySQL T instances. If the
Performance Schema is enabled, the instance might run out of memory.

###### Tip

If your database is sometimes idle but at other times has a substantial workload,
you can use Aurora Serverless v2 as an alternative to T instances. With Aurora Serverless v2, you
define a capacity range and Aurora automatically scales your database up or down depending on
the current workload. For usage details, see [Using Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").
For the database engine versions that you can use with Aurora Serverless v2, see
[Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

When you use a T instance as a DB instance in an Aurora MySQL DB cluster, we recommend the
following:

- Use the same DB instance class for all instances in your DB cluster. For example, if you use `db.t2.medium`
  for your writer instance, then we recommend that you use `db.t2.medium` for your reader instances also.
- Don't adjust any memory-related configuration settings, such as `innodb_buffer_pool_size`.
  Aurora uses a highly tuned set of default values for memory buffers on T instances. These special defaults
  are needed for Aurora to run on memory-constrained instances. If you change any memory-related settings on
  a T instance, you are much more likely to encounter out-of-memory conditions, even if your change is intended
  to increase buffer sizes.
- Monitor your CPU Credit Balance (`CPUCreditBalance`) to ensure that
  it is at a sustainable level. That is, CPU credits are being accumulated at the
  same rate as they are being used.

When you have exhausted the CPU credits for an instance, you see an immediate
drop in the available CPU and an increase in the read and write latency for the
instance. This situation results in a severe decrease in the overall performance
of the instance.

If your CPU credit balance is not at a sustainable level, then we recommend
that you modify your DB instance to use a one of the supported R DB instance
classes (scale compute).

For more information on monitoring metrics, see
[Viewing metrics in the Amazon RDS console](USER_Monitoring.md "USER_Monitoring.md").

- Monitor the replica lag (`AuroraReplicaLag`) between the writer instance and the reader instances.

If a reader instance runs out of CPU credits before the writer instance does, the
resulting lag can cause the reader instance to restart frequently. This result is
common when an application has a heavy load of read operations distributed among
reader instances, at the same time that the writer instance has a minimal load of write
operations.

If you see a sustained increase in replica lag, make sure that your CPU credit
balance for the reader instances in your DB cluster is not being
exhausted.

If your CPU credit balance is not at a sustainable level, then we recommend
that you modify your DB instance to use one of the supported R DB instance
classes (scale compute).

- Keep the number of inserts per transaction below 1 million for DB clusters
  that have binary logging enabled.

If the DB cluster parameter group for your DB cluster has the
`binlog_format` parameter set to a value other than
`OFF`, then your DB cluster might experience out-of-memory
conditions if the DB cluster receives transactions that contain over 1 million
rows to insert. You can monitor the freeable memory
(`FreeableMemory`) metric to determine if your DB cluster is running
out of available memory. You then check the write operations
(`VolumeWriteIOPS`) metric to see if a writer instance is
receiving a heavy load of write operations. If this is the case, then we
recommend that you update your application to limit the number of inserts in a
transaction to less than 1 million. Alternatively, you can modify your instance
to use one of the supported R DB instance classes (scale compute).

## Optimizing Aurora MySQL indexed join queries with asynchronous key prefetch

Aurora MySQL can use the asynchronous key prefetch (AKP) feature to improve the performance of queries that join tables
across indexes. This feature improves performance by anticipating the rows needed to run queries in which a JOIN query
requires use of the Batched Key Access (BKA) Join algorithm and Multi-Range Read (MRR) optimization features. For more
information about BKA and MRR, see [Block
nested-loop and batched key access joins](https://dev.mysql.com/doc/refman/5.6/en/bnl-bka-optimization.html "https://dev.mysql.com/doc/refman/5.6/en/bnl-bka-optimization.html") and [Multi-range read optimization](https://dev.mysql.com/doc/refman/5.6/en/mrr-optimization.html "https://dev.mysql.com/doc/refman/5.6/en/mrr-optimization.html") in the MySQL
documentation.

To take advantage of the AKP feature, a query must use both BKA and MRR. Typically, such a query occurs when the JOIN
clause of a query uses a secondary index, but also needs some columns from the primary index. For example, you can use AKP
when a JOIN clause represents an equijoin on index values between a small outer and large inner table, and the index is
highly selective on the larger table. AKP works in concert with BKA and MRR to perform a secondary to primary index lookup
during the evaluation of the JOIN clause. AKP identifies the rows required to run the query during the evaluation of
the JOIN clause. It then uses a background thread to asynchronously load the pages containing those rows into memory
before running the query.

AKP is available for Aurora MySQL version 2.10 and higher, and version 3. For more information about Aurora MySQL versions, see
[Database engine updates for Amazon Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md").

### Enabling asynchronous key prefetch

You can enable the AKP feature by setting `aurora_use_key_prefetch`, a MySQL server variable, to
`on`. By default, this value is set to `on`. However, AKP can't be enabled until you also
enable the BKA Join algorithm and disable cost-based MRR functionality. To do so, you must set the following values for
`optimizer_switch`, a MySQL server variable:

- Set `batched_key_access` to `on`. This value controls the use of the BKA Join
  algorithm. By default, this value is set to `off`.
- Set `mrr_cost_based` to `off`. This value controls the use of cost-based
  MRR functionality. By default, this value is set to `on`.

Currently, you can set these values only at the session level. The following example illustrates how to set
these values to enable AKP for the current session by executing SET statements.

```

`mysql>` set @@session.aurora_use_key_prefetch=on;
`mysql>` set @@session.optimizer_switch='batched_key_access=on,mrr_cost_based=off';

```

Similarly, you can use SET statements to disable AKP and the BKA Join algorithm and re-enable cost-based MRR
functionality for the current session, as shown in the following example.

```

`mysql>` set @@session.aurora_use_key_prefetch=off;
`mysql>` set @@session.optimizer_switch='batched_key_access=off,mrr_cost_based=on';

```

For more information about the **batched_key_access** and
**mrr_cost_based** optimizer switches, see [Switchable optimizations](https://dev.mysql.com/doc/refman/5.6/en/switchable-optimizations.html "https://dev.mysql.com/doc/refman/5.6/en/switchable-optimizations.html") in the MySQL documentation.

### Optimizing queries for asynchronous key prefetch

You can confirm whether a query can take advantage of the AKP feature. To do so, use the `EXPLAIN` statement to
profile the query before running it. The `EXPLAIN` statement provides information about the execution plan to
use for a specified query.

In the output for the `EXPLAIN` statement, the `Extra` column describes additional information
included with the execution plan. If the AKP feature applies to a table used in the query, this column includes one of
the following values:

- `Using Key Prefetching`
- `Using join buffer (Batched Key Access with Key Prefetching)`

The following example shows the use of `EXPLAIN` to view the execution plan for a query that can take advantage
of AKP.

```

`mysql>` explain select sql_no_cache
 `->`     ps_partkey,
 `->`     sum(ps_supplycost * ps_availqty) as value
 `->` from
 `->`     partsupp,
 `->`     supplier,
 `->`     nation
 `->` where
 `->`     ps_suppkey = s_suppkey
 `->`     and s_nationkey = n_nationkey
 `->`     and n_name = 'ETHIOPIA'
 `->` group by
 `->`     ps_partkey having
 `->`         sum(ps_supplycost * ps_availqty) > (
 `->`             select
 `->`                 sum(ps_supplycost * ps_availqty) * 0.0000003333
 `->`             from
 `->`                 partsupp,
 `->`                 supplier,
 `->`                 nation
 `->`             where
 `->`                 ps_suppkey = s_suppkey
 `->`                 and s_nationkey = n_nationkey
 `->`                 and n_name = 'ETHIOPIA'
 `->`         )
 `->` order by
 `->`     value desc;
`+----+-------------+----------+------+-----------------------+---------------+---------+----------------------------------+------+----------+-------------------------------------------------------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | filtered | Extra |
+----+-------------+----------+------+-----------------------+---------------+---------+----------------------------------+------+----------+-------------------------------------------------------------+
| 1 | PRIMARY | nation | ALL | PRIMARY | NULL | NULL | NULL | 25 | 100.00 | Using where; Using temporary; Using filesort |
| 1 | PRIMARY | supplier | ref | PRIMARY,i_s_nationkey | i_s_nationkey | 5 | dbt3_scale_10.nation.n_nationkey | 2057 | 100.00 | Using index |
| 1 | PRIMARY | partsupp | ref | i_ps_suppkey | i_ps_suppkey | 4 | dbt3_scale_10.supplier.s_suppkey | 42 | 100.00 | Using join buffer (Batched Key Access with Key Prefetching) |
| 2 | SUBQUERY | nation | ALL | PRIMARY | NULL | NULL | NULL | 25 | 100.00 | Using where |
| 2 | SUBQUERY | supplier | ref | PRIMARY,i_s_nationkey | i_s_nationkey | 5 | dbt3_scale_10.nation.n_nationkey | 2057 | 100.00 | Using index |
| 2 | SUBQUERY | partsupp | ref | i_ps_suppkey | i_ps_suppkey | 4 | dbt3_scale_10.supplier.s_suppkey | 42 | 100.00 | Using join buffer (Batched Key Access with Key Prefetching) |
+----+-------------+----------+------+-----------------------+---------------+---------+----------------------------------+------+----------+-------------------------------------------------------------+
6 rows in set, 1 warning (0.00 sec)`

```

For more information about the `EXPLAIN` output format, see
[Extended EXPLAIN output format](https://dev.mysql.com/doc/refman/8.0/en/explain-extended.html "https://dev.mysql.com/doc/refman/8.0/en/explain-extended.html")
in the MySQL documentation.

## Optimizing large Aurora MySQL join queries with hash joins

When you need to join a large amount of data by using an equijoin, a hash join can
improve query performance. You can enable hash joins for Aurora MySQL.

A hash join column can be any complex expression. In a hash join column, you can
compare across data types in the following ways:

- You can compare anything across the category of precise numeric data types,
  such as `int`, `bigint`, `numeric`, and
  `bit`.
- You can compare anything across the category of approximate numeric data
  types, such as `float` and `double`.
- You can compare items across string types if the string types have the same
  character set and collation.
- You can compare items with date and timestamp data types if the types are the
  same.

###### Note

You can't compare data types in different categories.

The following restrictions apply to hash joins for Aurora MySQL:

- Left-right outer joins aren't supported for Aurora MySQL version 2, but are supported for version 3.
- Semijoins such as subqueries aren't supported, unless the subqueries are materialized first.
- Multiple-table updates or deletes aren't supported.

###### Note

Single-table updates or deletes are supported.

- BLOB and spatial data type columns can't be join columns in a hash join.

### Enabling hash joins

To enable hash joins:

- Aurora MySQL version 2 – Set the DB parameter or DB cluster parameter
  `aurora_disable_hash_join` to `0`. Turning off `aurora_disable_hash_join`
  sets the value of `optimizer_switch` to `hash_join=on`.
- Aurora MySQL version 3 – Set the MySQL server parameter `optimizer_switch` to
  `block_nested_loop=on`.

Hash joins are turned on by default in Aurora MySQL version 3 and turned off by default in Aurora MySQL version 2. The
following example illustrates how to enable hash joins for Aurora MySQL version 3. You can issue the statement
`select @@optimizer_switch` first to see what other settings are present in the `SET`
parameter string. Updating one setting in the `optimizer_switch` parameter doesn't erase or modify the
other settings.

```
`mysql>` SET optimizer_switch='block_nested_loop=on';
```

###### Note

For Aurora MySQL version 3, hash join support is available in all minor versions and is turned on by default.

For Aurora MySQL version 2, hash join support is available in all minor versions. In Aurora MySQL version 2, the hash
join feature is always controlled by the `aurora_disable_hash_join` value.

With this setting, the optimizer chooses to use a hash join based on cost, query
characteristics, and resource availability. If the cost estimation is incorrect, you
can force the optimizer to choose a hash join. You do so by setting
`hash_join_cost_based`, a MySQL server variable, to `off`.
The following example illustrates how to force the optimizer to choose a hash
join.

```

`mysql>` SET optimizer_switch='hash_join_cost_based=off';

```

###### Note

This setting overrides the decisions of the cost-based optimizer. While the setting can be useful for testing and
development, we recommend that you not use it in production.

### Optimizing queries for hash joins

To find out whether a query can take advantage of a hash join, use the `EXPLAIN`
statement to profile the query first. The `EXPLAIN` statement provides information
about the execution plan to use for a specified query.

In the output for the `EXPLAIN` statement, the `Extra` column
describes additional information included with the execution plan. If a hash join
applies to the tables used in the query, this column includes values similar to the following:

- `Using where; Using join buffer (Hash Join Outer table `table1_name`)`
- `Using where; Using join buffer (Hash Join Inner table `table2_name`)`

The following example shows the use of EXPLAIN
to view the execution plan for a hash join query.

```

`mysql>` explain SELECT sql_no_cache * FROM hj_small, hj_big, hj_big2
 `->`     WHERE hj_small.col1 = hj_big.col1 and hj_big.col1=hj_big2.col1 ORDER BY 1;
`+----+-------------+----------+------+---------------+------+---------+------+------+----------------------------------------------------------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+----+-------------+----------+------+---------------+------+---------+------+------+----------------------------------------------------------------+
| 1 | SIMPLE | hj_small | ALL | NULL | NULL | NULL | NULL | 6 | Using temporary; Using filesort |
| 1 | SIMPLE | hj_big | ALL | NULL | NULL | NULL | NULL | 10 | Using where; Using join buffer (Hash Join Outer table hj_big) |
| 1 | SIMPLE | hj_big2 | ALL | NULL | NULL | NULL | NULL | 15 | Using where; Using join buffer (Hash Join Inner table hj_big2) |
+----+-------------+----------+------+---------------+------+---------+------+------+----------------------------------------------------------------+
3 rows in set (0.04 sec)`

```

In the output, the `Hash Join Inner table` is the table used to build
hash table, and the `Hash Join Outer table` is the table that is used
to probe the hash table.

For more information about the extended `EXPLAIN` output format, see [Extended EXPLAIN Output Format](https://dev.mysql.com/doc/refman/8.0/en/explain-extended.html "https://dev.mysql.com/doc/refman/8.0/en/explain-extended.html") in the
MySQL product documentation.

In Aurora MySQL 2.08 and higher, you can use SQL hints to influence whether a query uses
hash join or not, and which tables to use for the build and probe sides of the join.
For details, see [Aurora MySQL hints](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md").

## Using Amazon Aurora to scale reads for

your MySQL database

You can use Amazon Aurora with your MySQL DB instance to take advantage of the read
scaling capabilities of Amazon Aurora and expand the read workload for your MySQL DB
instance. To use Aurora to read scale your MySQL DB instance, create an Aurora MySQL
DB cluster and make it a read replica of your MySQL DB instance. Then connect to
the Aurora MySQL cluster to process the read queries. The source database can be an
RDS for MySQL DB instance, or a MySQL database running external to Amazon RDS. For more information,
see [Scaling reads for your MySQL database with Amazon Aurora](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

## Optimizing timestamp operations

When the value of the system variable `time_zone` is set to `SYSTEM`, each MySQL function call that
requires a time zone calculation makes a system library call. When you run SQL statements that return or change such
`TIMESTAMP` values at high concurrency, you might experience increased latency, lock contention, and CPU
usage. For more information, see [time_zone](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_time_zone "https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_time_zone") in the
MySQL documentation.

To avoid this behavior, we recommend that you change the value of the `time_zone` DB cluster parameter to
`UTC`. For more information, see [Modifying parameters in a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

While the `time_zone` parameter is dynamic (doesn't require a database server restart), the new value is used
only for new connections. To make sure that all connections are updated to use the new `time_zone` value, we
recommend that you recycle your application connections after updating the DB cluster parameter.

## Virtual index ID overflow errors

Aurora MySQL limits values for virtual index IDs to 8 bits prevent an issue caused by the undo format in MySQL. If an index
exceeds the virtual index ID limit, your cluster might not be available. When an index approaches the virtual index ID limit or when you
attempt to create an index above the virtual index ID limit, RDS might throw error code `63955` or warning code
`63955`. To address a virtual index ID limit error, we recommend you recreate your database with a logical dump
and restore.

For more information about logical dump and restore for Amazon Aurora MySQL, see [Migrate very large databases to Amazon Aurora MySQL using MyDumper and MyLoader](https://aws.amazon.com/blogs/database/migrate-very-large-databases-to-amazon-aurora-mysql-using-mydumper-and-myloader/ "https://aws.amazon.com/blogs/database/migrate-very-large-databases-to-amazon-aurora-mysql-using-mydumper-and-myloader/"). Fore more information about
accessing error logs in Amazon Aurora, see [Monitoring Amazon Aurora log files](USER_LogAccess.md "USER_LogAccess.md").
