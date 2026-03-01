# New temporary table behavior in Aurora MySQL version 3

Aurora MySQL version 3 handles temporary tables differently from earlier Aurora MySQL versions. This new behavior is inherited
from MySQL 8.0 Community Edition. There are two types of temporary tables that can be created with Aurora MySQL version 3:

- Internal (or _implicit_) temporary tables – Created by the Aurora MySQL engine to handle
  operations such as sorting aggregation, derived tables, or common table expressions (CTEs).
- User-created (or _explicit_) temporary tables – Created by the Aurora MySQL engine when you
  use the `CREATE TEMPORARY TABLE` statement.
  There are additional considerations for both internal and user-created temporary tables on Aurora reader DB instances. We
  discuss these changes in the following sections.

###### Topics

- [Storage engine for internal (implicit) temporary tables](#ams3-temptable-behavior-engine "#ams3-temptable-behavior-engine")
- [Limiting the size of internal, in-memory temporary tables](#ams3-temptable-behavior-limit "#ams3-temptable-behavior-limit")
- [Mitigating fullness issues for internal temporary tables on Aurora Replicas](#ams3-temptable-behavior-mitigate "#ams3-temptable-behavior-mitigate")
- [Optimizing the temptable_max_mmap parameter on Aurora MySQL DB instances](#ams-optimize-temptable_max_mmap "#ams-optimize-temptable_max_mmap")
- [User-created (explicit) temporary tables on reader DB instances](#ams3-temptable-behavior.user "#ams3-temptable-behavior.user")
- [Temporary table creation errors and mitigation](#ams3-temptable-behavior.errors "#ams3-temptable-behavior.errors")

## Storage engine for internal (implicit) temporary tables

When generating intermediate result sets, Aurora MySQL initially attempts to write
to in-memory temporary tables. This might be unsuccessful, because of either
incompatible data types or configured limits. If so, the temporary table is
converted to an on-disk temporary table rather than being held in memory. More
information on this can be found in the [Internal Temporary Table Use in MySQL](https://dev.mysql.com/doc/refman/8.0/en/internal-temporary-tables.html "https://dev.mysql.com/doc/refman/8.0/en/internal-temporary-tables.html") in the MySQL
documentation.

In Aurora MySQL version 3, the way internal temporary tables work is different from
earlier Aurora MySQL versions. Instead of choosing between the InnoDB and MyISAM
storage engines for such temporary tables, now you choose between the
`TempTable` and `MEMORY` storage engines.

With the `TempTable` storage engine, you can make an additional choice for how to handle certain data. The data
affected overflows the memory pool that holds all the internal temporary tables for the DB instance.

Those choices can influence the performance for queries that generate high volumes of temporary data, for example while
performing aggregations such as `GROUP BY` on large tables.

###### Tip

If your workload includes queries that generate internal temporary tables, confirm how your application performs with
this change by running benchmarks and monitoring performance-related metrics.

In some cases, the amount of temporary data fits within the `TempTable` memory pool or only overflows the
memory pool by a small amount. In these cases, we recommend using the `TempTable` setting for internal
temporary tables and memory-mapped files to hold any overflow data. This setting is the default.

The `TempTable` storage engine is the default. `TempTable` uses a common memory pool for all
temporary tables that use this engine, instead of a maximum memory limit per table. The size of this memory pool is
specified by the [temptable_max_ram](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_ram "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_ram") parameter. It defaults to 1 GiB on DB instances with 16 or more GiB of memory, and 16 MB on
DB instances with less than 16 GiB of memory. The size of the memory pool influences session-level memory
consumption.

In some cases when you use the `TempTable` storage engine, the
temporary data might exceed the size of the memory pool. If so, Aurora MySQL stores
the overflow data using a secondary mechanism.

You can set the [temptable_max_mmap](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_mmap "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_mmap") parameter to choose whether the data overflows to memory-mapped temporary files or to InnoDB
internal temporary tables on disk. The different data formats and overflow criteria of these overflow mechanisms can affect
query performance. They do so by influencing the amount of data written to disk and the demand on disk storage
throughput.

Aurora MySQL version 3 stores the overflow data in the following way:

- On the writer DB instance, data that overflows to InnoDB internal temporary tables or memory-mapped temporary files resides in local
  storage on the instance.
- On reader DB instances, overflow data always resides in memory-mapped temporary files in local storage.

Read-only instances can't store any data on the Aurora cluster volume.

The configuration parameters related to internal temporary tables apply differently to the writer and reader instances in
your cluster:

- On reader instances, Aurora MySQL always uses the `TempTable` storage engine.
- The size for `temptable_max_mmap` defaults to 1 GiB for both writer and reader instances, regardless of
  the DB instance memory size. You can adjust this value on both writer and reader instances.
- Setting `temptable_max_mmap` to `0` turns off the use of memory-mapped temporary files on
  writer instances.
- You can't set `temptable_max_mmap` to `0` on reader instances.

###### Note

We don't recommend using the [temptable_use_mmap](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_use_mmap "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_use_mmap") parameter. It has been deprecated, and support for it is expected to be removed in a
future MySQL release.

## Limiting the size of internal, in-memory temporary tables

As discussed in [Storage engine for internal (implicit) temporary tables](#ams3-temptable-behavior-engine "#ams3-temptable-behavior-engine"), you can
control temporary table resources globally by using the [temptable_max_ram](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_ram "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_ram") and [temptable_max_mmap](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_mmap "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_mmap") settings.

You can also limit the size of any individual internal, in-memory temporary table by using the [tmp_table_size](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size")
DB parameter. This limit is intended to prevent individual queries from consuming an inordinate amount of global temporary
table resources, which can affect the performance of concurrent queries that require these resources.

The `tmp_table_size` parameter defines the maximum size of temporary tables created by the `MEMORY`
storage engine in Aurora MySQL version 3.

In Aurora MySQL version 3.04 and higher, `tmp_table_size` also defines the maximum size of temporary tables
created by the `TempTable` storage engine when the `aurora_tmptable_enable_per_table_limit` DB
parameter is set to `ON`. This behavior is disabled by default (`OFF`), which is the same behavior as
in Aurora MySQL version 3.03 and lower versions.

- When `aurora_tmptable_enable_per_table_limit` is `OFF`, `tmp_table_size` isn't
  considered for internal, in-memory temporary tables created by the `TempTable` storage engine.

However, the global `TempTable` resources limit still applies. Aurora MySQL has the following behavior
when the global `TempTable` resources limit is reached:

    + Writer DB instances – Aurora MySQL automatically converts the in-memory temporary table to an InnoDB
     on-disk temporary table.
    + Reader DB instances – The query ends with an error.



    ```
    ERROR 1114 (HY000): The table '/rdsdbdata/tmp/#sql`xx_xxx`' is full
    ```

- When `aurora_tmptable_enable_per_table_limit` is `ON`, Aurora MySQL has the following behavior
  when the `tmp_table_size` limit is reached:
  - Writer DB instances – Aurora MySQL automatically converts the in-memory temporary table to an InnoDB
    on-disk temporary table.
  - Reader DB instances – The query ends with an error.

  ```
  ERROR 1114 (HY000): The table '/rdsdbdata/tmp/#sql`xx_xxx`' is full
  ```

  Both the global `TempTable` resources limit and the per-table limit apply in this case.

###### Note

The `aurora_tmptable_enable_per_table_limit` parameter has no effect when [internal_tmp_mem_storage_engine](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_internal_tmp_mem_storage_engine "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_internal_tmp_mem_storage_engine") is set to `MEMORY`. In this case, the maximum size of an
in-memory temporary table is defined by the [tmp_table_size](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size") or [max_heap_table_size](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_heap_table_size "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_heap_table_size") value, whichever is smaller.

The following examples show the behavior of the `aurora_tmptable_enable_per_table_limit` parameter for writer
and reader DB instances.

###### Example of writer DB instance with `aurora_tmptable_enable_per_table_limit` set to `OFF`

The in-memory temporary table isn't converted to an InnoDB on-disk temporary table.

```
mysql> set aurora_tmptable_enable_per_table_limit=0;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@innodb_read_only,@@aurora_version,@@aurora_tmptable_enable_per_table_limit,@@temptable_max_ram,@@temptable_max_mmap;
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
| @@innodb_read_only | @@aurora_version | @@aurora_tmptable_enable_per_table_limit | @@temptable_max_ram | @@temptable_max_mmap |
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
|                  0 | 3.04.0           |                                        0 |          1073741824 |           1073741824 |
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
1 row in set (0.00 sec)

mysql> show status like '%created_tmp_disk%';
+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| Created_tmp_disk_tables | 0     |
+-------------------------+-------+
1 row in set (0.00 sec)

mysql> set cte_max_recursion_depth=4294967295;
Query OK, 0 rows affected (0.00 sec)

mysql> WITH RECURSIVE cte (n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM cte WHERE n < 60000000) SELECT max(n) FROM cte;
+----------+
| max(n)   |
+----------+
| 60000000 |
+----------+
1 row in set (13.99 sec)

mysql> show status like '%created_tmp_disk%';
+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| **Created\_tmp\_disk\_tables** | **0**     |
+-------------------------+-------+
1 row in set (0.00 sec)
```

###### Example of writer DB instance with `aurora_tmptable_enable_per_table_limit` set to `ON`

The in-memory temporary table is converted to an InnoDB on-disk temporary table.

```
mysql> set aurora_tmptable_enable_per_table_limit=1;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@innodb_read_only,@@aurora_version,@@aurora_tmptable_enable_per_table_limit,@@tmp_table_size;
+--------------------+------------------+------------------------------------------+------------------+
| @@innodb_read_only | @@aurora_version | @@aurora_tmptable_enable_per_table_limit | @@tmp_table_size |
+--------------------+------------------+------------------------------------------+------------------+
|                  0 | 3.04.0           |                                        1 |         16777216 |
+--------------------+------------------+------------------------------------------+------------------+
1 row in set (0.00 sec)

mysql> set cte_max_recursion_depth=4294967295;
Query OK, 0 rows affected (0.00 sec)

mysql> show status like '%created_tmp_disk%';
+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| Created_tmp_disk_tables | 0     |
+-------------------------+-------+
1 row in set (0.00 sec)

mysql> WITH RECURSIVE cte (n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM cte WHERE n < 6000000) SELECT max(n) FROM cte;
+---------+
| max(n)  |
+---------+
| 6000000 |
+---------+
1 row in set (4.10 sec)

mysql> show status like '%created_tmp_disk%';
+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| **Created\_tmp\_disk\_tables** | **1**     |
+-------------------------+-------+
1 row in set (0.00 sec)
```

###### Example of reader DB instance with `aurora_tmptable_enable_per_table_limit` set to `OFF`

The query finishes without an error because `tmp_table_size` doesn't apply, and the global
`TempTable` resources limit hasn't been reached.

```
mysql> set aurora_tmptable_enable_per_table_limit=0;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@innodb_read_only,@@aurora_version,@@aurora_tmptable_enable_per_table_limit,@@temptable_max_ram,@@temptable_max_mmap;
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
| @@innodb_read_only | @@aurora_version | @@aurora_tmptable_enable_per_table_limit | @@temptable_max_ram | @@temptable_max_mmap |
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
|                  1 | 3.04.0           |                                        0 |          1073741824 |           1073741824 |
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
1 row in set (0.00 sec)

mysql> set cte_max_recursion_depth=4294967295;
Query OK, 0 rows affected (0.00 sec)

mysql> WITH RECURSIVE cte (n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM cte WHERE n < 60000000) SELECT max(n) FROM cte;
+----------+
| max(n)   |
+----------+
| **60000000** |
+----------+
1 row in set (14.05 sec)
```

###### Example of reader DB instance with `aurora_tmptable_enable_per_table_limit` set to `OFF`

This query reaches the global TempTable resources limit with `aurora_tmptable_enable_per_table_limit` set
to OFF. The query ends with an error on reader instances.

```
mysql> set aurora_tmptable_enable_per_table_limit=0;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@innodb_read_only,@@aurora_version,@@aurora_tmptable_enable_per_table_limit,@@temptable_max_ram,@@temptable_max_mmap;
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
| @@innodb_read_only | @@aurora_version | @@aurora_tmptable_enable_per_table_limit | @@temptable_max_ram | @@temptable_max_mmap |
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
|                  1 | 3.04.0           |                                        0 |          1073741824 |           1073741824 |
+--------------------+------------------+------------------------------------------+---------------------+----------------------+
1 row in set (0.00 sec)

mysql> set cte_max_recursion_depth=4294967295;
Query OK, 0 rows affected (0.01 sec)

mysql> WITH RECURSIVE cte (n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM cte WHERE n < 120000000) SELECT max(n) FROM cte;
**ERROR 1114 (HY000): The table '/rdsdbdata/tmp/#sqlfd\_1586\_2' is full**
```

###### Example of reader DB instance with `aurora_tmptable_enable_per_table_limit` set to `ON`

The query ends with an error when the `tmp_table_size` limit is reached.

```
mysql> set aurora_tmptable_enable_per_table_limit=1;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@innodb_read_only,@@aurora_version,@@aurora_tmptable_enable_per_table_limit,@@tmp_table_size;
+--------------------+------------------+------------------------------------------+------------------+
| @@innodb_read_only | @@aurora_version | @@aurora_tmptable_enable_per_table_limit | @@tmp_table_size |
+--------------------+------------------+------------------------------------------+------------------+
|                  1 | 3.04.0           |                                        1 |         16777216 |
+--------------------+------------------+------------------------------------------+------------------+
1 row in set (0.00 sec)

mysql> set cte_max_recursion_depth=4294967295;
Query OK, 0 rows affected (0.00 sec)

mysql> WITH RECURSIVE cte (n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM cte WHERE n < 6000000) SELECT max(n) FROM cte;
**ERROR 1114 (HY000): The table '/rdsdbdata/tmp/#sqlfd\_8\_2' is full**
```

## Mitigating fullness issues for internal temporary tables on Aurora Replicas

To avoid size limitation issues for temporary tables, set the `temptable_max_ram` and
`temptable_max_mmap` parameters to a combined value that can fit the requirements of your workload.

Be careful when setting the value of the `temptable_max_ram` parameter.
Setting the value too high reduces the available memory on the database instance,
which can cause an out-of-memory condition. Monitor the average freeable memory on
the DB instance. Then determine an appropriate value for
`temptable_max_ram` so that you will still have a reasonable amount
of free memory left on the instance. For more information, see [Freeable memory issues in Amazon Aurora](CHAP_Troubleshooting.md#Troubleshooting.FreeableMemory "CHAP_Troubleshooting.md#Troubleshooting.FreeableMemory").

It is also important to monitor the size of the local storage and the temporary table space consumption. You can monitor the temporary storage
available for a specific DB instance with the `FreeLocalStorage` Amazon CloudWatch metric, described in [Amazon CloudWatch metrics for Amazon Aurora](Aurora.AuroraMonitoring.md "Aurora.AuroraMonitoring.md").

###### Note

This procedure doesn't work when the `aurora_tmptable_enable_per_table_limit` parameter is set to
`ON`. For more information, see [Limiting the size of internal, in-memory temporary tables](#ams3-temptable-behavior-limit "#ams3-temptable-behavior-limit").

###### Example 1

You know that your temporary tables grow to a cumulative size of 20 GiB. You want to set in-memory temporary tables to
2 GiB and to grow to a maximum of 20 GiB on disk.

Set `temptable_max_ram` to `2,147,483,648` and `temptable_max_mmap` to
`21,474,836,480`. These values are in bytes.

These parameter settings make sure that your temporary tables can grow to a cumulative total of 22 GiB.

###### Example 2

Your current instance size is 16xlarge or larger. You don't know the total size of the temporary tables that you
might need. You want to be able to use up to 4 GiB in memory and up to the maximum available storage size on
disk.

Set `temptable_max_ram` to `4,294,967,296` and `temptable_max_mmap` to
`1,099,511,627,776`. These values are in bytes.

Here you're setting `temptable_max_mmap` to 1 TiB, which is less than the maximum local storage of 1.2
TiB on a 16xlarge Aurora DB instance.

On a smaller instance size, adjust the value of `temptable_max_mmap` so that it doesn't fill up the
available local storage. For example, a 2xlarge instance has only 160 GiB of local storage available. Hence, we
recommend setting the value to less than 160 GiB. For more information on the available local storage for DB instance
sizes, see [Temporary storage limits for Aurora MySQL](AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage "AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage").

## Optimizing the temptable_max_mmap parameter on Aurora MySQL DB instances

The `temptable_max_mmap` parameter in Aurora MySQL controls the maximum
amount of local disk space that can be used by memory mapped files before
overflowing to the on-disk InnoDB temporary tables (on writer DB instances) or causing an
error (on reader DB instances). Setting this DB instance parameter properly can help optimize
the performance of your DB instances.

**Prerequisites**

1. Make sure that the Performance Schema is enabled. You can verify this by running the following SQL command:

```
SELECT @@performance_schema;
```

An output value of `1` indicates that it's enabled. 2. Confirm that the temporary table memory instrumentation is enabled. You can verify this by running the following SQL
command:

```
SELECT name, enabled FROM performance_schema.setup_instruments WHERE name LIKE '%memory%temptable%';
```

The `enabled` column shows `YES` for the relevant temporary table memory instrumentation
entries.

**Monitoring temporary table usage**

When setting the initial value for `temptable_max_mmap`, we recommend that you start with 80% of the local storage size
for the DB instance class that you're using. This ensures that the temporary tables have enough disk space to operate efficiently, while
leaving room for other disk usage on the instance.

To find the local storage size for your DB instance class, see [Temporary storage limits for Aurora MySQL](AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage "AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage").

For example, if you're using the db.r5.large DB instance class, the local storage size is 32 GiB. In this case, you would initially set
the `temptable_max_mmap` parameter to 80% of 32 GiB, which is 25.6 GiB.

After setting the initial `temptable_max_mmap` value, run your peak workload on the Aurora MySQL instances. Monitor the
current and high temporary table disk usage using the following SQL query:

```
SELECT event_name, current_count, current_alloc, current_avg_alloc, high_count, high_alloc, high_avg_alloc
FROM sys.memory_global_by_current_bytes WHERE event_name LIKE 'memory/temptable/%';
```

This query retrieves the following information:

- `event_name` – The name of the temporary table memory or disk usage event.
- `current_count` – The current number of allocated temporary table memory or disk blocks.
- `current_alloc` – The current amount of memory or disk allocated for temporary tables.
- `current_avg_alloc` – The current average size of temporary table memory or disk blocks.
- `high_count` – The highest number of allocated temporary table memory or disk blocks.
- `high_alloc` – The highest amount of memory or disk allocated for temporary tables.
- `high_avg_alloc` – The highest average size of temporary table memory or disk blocks.

If your queries fail with a **`Table is full`** error using this setting, it indicates that your workload requires
more disk space for temporary table operations. In this case, consider increasing your DB instance size to one with more local storage
space.

**Setting the optimal `temptable_max_mmap` value**

Use the following procedure to monitor and set the right size for the `temptable_max_mmap` parameter.

1. Review the output of the previous query, and identify the peak temporary table disk usage, as indicated by the
   `high_alloc` column.
2. Based on the peak temporary table disk usage, adjust the `temptable_max_mmap` parameter in the DB parameter
   group for your Aurora MySQL DB instances.

Set the value to be slightly higher than the peak temporary table disk usage to accommodate future growth. 3. Apply the parameter group changes to your DB instances. 4. Monitor the temporary table disk usage again during your peak workload to make sure that the new
`temptable_max_mmap` value is appropriate. 5. Repeat the previous steps as needed to fine tune the `temptable_max_mmap` parameter.

## User-created (explicit) temporary tables on reader DB instances

You can create explicit temporary tables using the `TEMPORARY` keyword in your `CREATE TABLE`
statement. Explicit temporary tables are supported on the writer DB instance in an Aurora DB cluster. You can also use
explicit temporary tables on reader DB instances, but the tables can't enforce the use of the InnoDB storage
engine.

To avoid errors while creating explicit temporary tables on Aurora MySQL reader DB instances, make sure that you run all
`CREATE TEMPORARY TABLE` statements in either or both of the following ways:

- Don't specify the `ENGINE=InnoDB` clause.
- Don't set the SQL mode to `NO_ENGINE_SUBSTITUTION`.

## Temporary table creation errors and mitigation

The error that you receive is different depending on whether you use a plain `CREATE TEMPORARY TABLE` statement
or the variation `CREATE TEMPORARY TABLE AS SELECT`. The following examples show the different kinds of
errors.

This temporary table behavior only applies to read-only instances. This first example confirms that's the kind of
instance the session is connected to.

```
`mysql>` select @@innodb_read_only;
`+--------------------+
| @@innodb_read_only |
+--------------------+
| 1 |
+--------------------+`

```

For plain `CREATE TEMPORARY TABLE` statements, the statement fails when the `NO_ENGINE_SUBSTITUTION`
SQL mode is turned on. When `NO_ENGINE_SUBSTITUTION` is turned off (default), the appropriate engine substitution
is made, and the temporary table creation succeeds.

```
`mysql>` set sql_mode = 'NO_ENGINE_SUBSTITUTION';

`mysql>`  CREATE TEMPORARY TABLE tt2 (id int) ENGINE=InnoDB;
`ERROR 3161 (HY000): Storage engine InnoDB is disabled (Table creation is disallowed).`

`mysql>` SET sql_mode = '';

`mysql>` CREATE TEMPORARY TABLE tt4 (id int) ENGINE=InnoDB;

`mysql>` SHOW CREATE TABLE tt4\G
`*************************** 1. row ***************************
 Table: tt4
Create Table: CREATE TEMPORARY TABLE `tt4` (
 `id` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci`

```

For `CREATE TEMPORARY TABLE AS SELECT` statements, the statement fails when the
`NO_ENGINE_SUBSTITUTION` SQL mode is turned on. When `NO_ENGINE_SUBSTITUTION` is turned off
(default), the appropriate engine substitution is made, and the temporary table creation succeeds.

```
`mysql>` set sql_mode = 'NO_ENGINE_SUBSTITUTION';

`mysql>` CREATE TEMPORARY TABLE tt1 ENGINE=InnoDB AS SELECT * FROM t1;
`ERROR 3161 (HY000): Storage engine InnoDB is disabled (Table creation is disallowed).`

`mysql>` SET sql_mode = '';

mysql> show create table tt3;
`+-------+----------------------------------------------------------+
| Table | Create Table |
+-------+----------------------------------------------------------+
| tt3 | CREATE TEMPORARY TABLE `tt3` (
 `id` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+-------+----------------------------------------------------------+
1 row in set (0.00 sec)`
```

For more information about the storage aspects and performance implications of temporary tables in Aurora MySQL version 3,
see the blog post [Use the TempTable storage engine on Amazon RDS for MySQL and Amazon Aurora MySQL](https://aws.amazon.com/blogs/database/use-the-temptable-storage-engine-on-amazon-rds-for-mysql-and-amazon-aurora-mysql/ "https://aws.amazon.com/blogs/database/use-the-temptable-storage-engine-on-amazon-rds-for-mysql-and-amazon-aurora-mysql/").
