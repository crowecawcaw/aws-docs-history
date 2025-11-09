# Troubleshooting memory usage issues for Aurora MySQL databases

While CloudWatch, Enhanced Monitoring, and Performance Insights provide a good overview of memory usage at the operating system level, such as how much memory the database process
is using, they don't allow you to break down what connections or components within the engine might be causing this memory usage.

To troubleshoot this, you can use the Performance Schema and `sys` schema. In Aurora MySQL version 3, memory instrumentation is
enabled by default when the Performance Schema is enabled. In Aurora MySQL version 2, only memory instrumentation for Performance Schema memory
usage is enabled by default. For information on tables available in the Performance Schema to track memory usage and enabling Performance Schema
memory instrumentation, see [Memory summary
tables](https://dev.mysql.com/doc/refman/8.3/en/performance-schema-memory-summary-tables.html "https://dev.mysql.com/doc/refman/8.3/en/performance-schema-memory-summary-tables.html") in the MySQL documentation. For more information on using the Performance Schema with Performance Insights, see [Overview of the Performance Schema for Performance Insights on Aurora MySQL](USER_PerfInsights.md "USER_PerfInsights.md").

While detailed information is available in the Performance Schema to track current memory usage, the MySQL [sys schema](https://dev.mysql.com/doc/refman/8.0/en/sys-schema.html "https://dev.mysql.com/doc/refman/8.0/en/sys-schema.html") has views on top of Performance Schema tables that you can
use to quickly pinpoint where memory is being used.

In the `sys` schema, the following views are available to track memory usage by connection, component, and query.

| View                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [memory_by_host_by_current_bytes](https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-host-by-current-bytes.html "https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-host-by-current-bytes.html")       | Provides information on engine memory usage by host. This can be useful for identifying which application servers or<br>client hosts are consuming memory.                                                                                                                                                                                                                                                                                                                                                                                                      |
| [memory_by_thread_by_current_bytes](https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-thread-by-current-bytes.html "https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-thread-by-current-bytes.html") | Provides information on engine memory usage by thread ID. The thread ID in MySQL can be a client connection or a<br>background thread. You can map thread IDs to MySQL connection IDs by using the [sys.processlist](https://dev.mysql.com/doc/refman/8.0/en/sys-processlist.html "https://dev.mysql.com/doc/refman/8.0/en/sys-processlist.html") view or [performance_schema.threads](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-threads-table.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-threads-table.html")<br>table. |
| [memory_by_user_by_current_bytes](https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-user-by-current-bytes.html "https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-user-by-current-bytes.html")       | Provides information on engine memory usage by user. This can be useful for identifying which user accounts or clients are<br>consuming memory.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [memory_global_by_current_bytes](https://dev.mysql.com/doc/refman/8.0/en/sys-memory-global-by-current-bytes.html "https://dev.mysql.com/doc/refman/8.0/en/sys-memory-global-by-current-bytes.html")          | Provides information on engine memory usage by engine component. This can be useful for identifying memory usage globally<br>by engine buffers or components. For example, you might see the `memory/innodb/buf_buf_pool` event for the InnoDB<br>buffer pool, or the `memory/sql/Prepared_statement::main_mem_root` event for prepared statements.                                                                                                                                                                                                             |
| [memory_global_total](https://dev.mysql.com/doc/refman/8.0/en/sys-memory-global-total.html "https://dev.mysql.com/doc/refman/8.0/en/sys-memory-global-total.html")                                           | Provides an overview of total tracked memory usage in the database engine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

In Aurora MySQL version 3.05 and higher, you can also track maximum memory usage by statement digest in the [Performance Schema statement summary
tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html"). The statement summary tables contain normalized statement digests and aggregated statistics on their execution. The
`MAX_TOTAL_MEMORY` column can help you identify maximum memory used by query digest since the statistics were last reset, or
since the database instance was restarted. This can be useful in identifying specific queries that might be consuming a lot of memory.

###### Note

The Performance Schema and `sys` schema show you the current memory usage on the server, and the high-water marks for memory
consumed per connection and engine component. Because the Performance Schema is maintained in memory, information is reset when the DB
instance restarts. To maintain a history over time, we recommend that you configure retrieval and storage of this data outside of the
Performance Schema.

###### Topics

- [Example 1: Continuous high memory usage](#ams-workload-memory.example1 "#ams-workload-memory.example1")
- [Example 2: Transient memory spikes](#ams-workload-memory.example2 "#ams-workload-memory.example2")
- [Example 3: Freeable memory drops continuously and isn't reclaimed](#ams-workload-memory.example3 "#ams-workload-memory.example3")

## Example 1: Continuous high memory usage

Looking globally at `FreeableMemory` in CloudWatch, we can see that memory usage greatly increased at 2024-03-26 02:59 UTC.

![FreeableMemory graph showing high memory usage.](images/ams-freeable-memory.png)

This doesn't tell us the whole picture. To determine which component is using the most memory, you can log into the database and look at
`sys.memory_global_by_current_bytes`. This table contains a list of memory events that MySQL tracks, along with information
on memory allocation per event. Each memory tracking event starts with `memory/%`, followed by other information on which engine
component/feature the event is associated with.

For example, `memory/performance_schema/%` is for memory events related to the Performance Schema, `memory/innodb/%`
is for InnoDB, and so on. For more information on event naming conventions, see [Performance Schema instrument naming
conventions](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-instrument-naming.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-instrument-naming.html") in the MySQL documentation.

From the following query, we can find the likely culprit based on `current_alloc`, but we can also see many
`memory/performance_schema/%` events.

```
mysql> SELECT * FROM sys.memory_global_by_current_bytes LIMIT 10;

+-----------------------------------------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| event_name                                                                  | current_count | current_alloc | current_avg_alloc | high_count | high_alloc | high_avg_alloc |
+-----------------------------------------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| memory/sql/Prepared_statement::main_mem_root                                |        512817 | 4.91 GiB      | 10.04 KiB         |     512823 | 4.91 GiB   | 10.04 KiB      |
| memory/performance_schema/prepared_statements_instances                     |           252 | 488.25 MiB    | 1.94 MiB          |        252 | 488.25 MiB | 1.94 MiB       |
| memory/innodb/hash0hash                                                     |             4 | 79.07 MiB     | 19.77 MiB         |          4 | 79.07 MiB  | 19.77 MiB      |
| memory/performance_schema/events_errors_summary_by_thread_by_error          |          1028 | 52.27 MiB     | 52.06 KiB         |       1028 | 52.27 MiB  | 52.06 KiB      |
| memory/performance_schema/events_statements_summary_by_thread_by_event_name |             4 | 47.25 MiB     | 11.81 MiB         |          4 | 47.25 MiB  | 11.81 MiB      |
| memory/performance_schema/events_statements_summary_by_digest               |             1 | 40.28 MiB     | 40.28 MiB         |          1 | 40.28 MiB  | 40.28 MiB      |
| memory/performance_schema/memory_summary_by_thread_by_event_name            |             4 | 31.64 MiB     | 7.91 MiB          |          4 | 31.64 MiB  | 7.91 MiB       |
| memory/innodb/memory                                                        |         15227 | 27.44 MiB     | 1.85 KiB          |      20619 | 33.33 MiB  | 1.66 KiB       |
| memory/sql/String::value                                                    |         74411 | 21.85 MiB     |  307 bytes        |      76867 | 25.54 MiB  |  348 bytes     |
| memory/sql/TABLE                                                            |          8381 | 21.03 MiB     | 2.57 KiB          |       8381 | 21.03 MiB  | 2.57 KiB       |
+-----------------------------------------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
10 rows in set (0.02 sec)
```

We mentioned previously that the Performance Schema is stored in memory, which means that it's also tracked in the
`performance_schema` memory instrumentation.

###### Note

If you find that the Performance Schema is using a lot of memory, and want to limit its memory usage, you can tune database parameters
based on your requirements. For more information, see [The Performance Schema memory-allocation
model](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-memory-model.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-memory-model.html") in the MySQL documentation.

For readability, you can rerun the same query but exclude Performance Schema events. The output shows the following:

- The main memory consumer is `memory/sql/Prepared_statement::main_mem_root`.
- The `current_alloc` column tells us that MySQL has 4.91 GiB currently allocated to this event.
- The `high_alloc column` tells us that 4.91 GiB is the high-water mark of `current_alloc` since the stats
  were last reset or since the server restarted. This means that `memory/sql/Prepared_statement::main_mem_root` is at its
  highest value.

```
mysql> SELECT * FROM sys.memory_global_by_current_bytes WHERE event_name NOT LIKE 'memory/performance_schema/%' LIMIT 10;

+-----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| event_name                                    | current_count | current_alloc | current_avg_alloc | high_count | high_alloc | high_avg_alloc |
+-----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| memory/sql/Prepared_statement::main_mem_root  |        512817 | 4.91 GiB      | 10.04 KiB         |     512823 | 4.91 GiB   | 10.04 KiB      |
| memory/innodb/hash0hash                       |             4 | 79.07 MiB     | 19.77 MiB         |          4 | 79.07 MiB  | 19.77 MiB      |
| memory/innodb/memory                          |         17096 | 31.68 MiB     | 1.90 KiB          |      22498 | 37.60 MiB  | 1.71 KiB       |
| memory/sql/String::value                      |        122277 | 27.94 MiB     |  239 bytes        |     124699 | 29.47 MiB  |  247 bytes     |
| memory/sql/TABLE                              |          9927 | 24.67 MiB     | 2.55 KiB          |       9929 | 24.68 MiB  | 2.55 KiB       |
| memory/innodb/lock0lock                       |          8888 | 19.71 MiB     | 2.27 KiB          |       8888 | 19.71 MiB  | 2.27 KiB       |
| memory/sql/Prepared_statement::infrastructure |        257623 | 16.24 MiB     |   66 bytes        |     257631 | 16.24 MiB  |   66 bytes     |
| memory/mysys/KEY_CACHE                        |             3 | 16.00 MiB     | 5.33 MiB          |          3 | 16.00 MiB  | 5.33 MiB       |
| memory/innodb/sync0arr                        |             3 | 7.03 MiB      | 2.34 MiB          |          3 | 7.03 MiB   | 2.34 MiB       |
| memory/sql/THD::main_mem_root                 |           815 | 6.56 MiB      | 8.24 KiB          |        849 | 7.19 MiB   | 8.67 KiB       |
+-----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
10 rows in set (0.06 sec)
```

From the name of the event, we can tell that this memory is being used for prepared statements. If you want to see which connections are
using this memory, you can check [memory_by_thread_by_current_bytes](https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-thread-by-current-bytes.html "https://dev.mysql.com/doc/refman/8.0/en/sys-memory-by-thread-by-current-bytes.html").

In the following example, each connection has approximately 7 MiB allocated, with a high-water mark of approximately 6.29 MiB
(`current_max_alloc`). This makes sense, because the example is using `sysbench` with 80 tables and 800
connections with prepared statements. If you want to reduce memory usage in this scenario, you can optimize your application's usage of
prepared statements to reduce memory consumption.

```
mysql> SELECT * FROM sys.memory_by_thread_by_current_bytes;

+-----------+-------------------------------------------+--------------------+-------------------+-------------------+-------------------+-----------------+
| thread_id | user                                      | current_count_used | current_allocated | current_avg_alloc | current_max_alloc | total_allocated |
+-----------+-------------------------------------------+--------------------+-------------------+-------------------+-------------------+-----------------+
|        46 | rdsadmin@localhost                        |                405 | 8.47 MiB          | 21.42 KiB         | 8.00 MiB          | 155.86 MiB      |
|        61 | reinvent@10.0.4.4                         |               1749 | 6.72 MiB          | 3.93 KiB          | 6.29 MiB          | 14.24 MiB       |
|       101 | reinvent@10.0.4.4                         |               1845 | 6.71 MiB          | 3.72 KiB          | 6.29 MiB          | 14.50 MiB       |
|        55 | reinvent@10.0.4.4                         |               1674 | 6.68 MiB          | 4.09 KiB          | 6.29 MiB          | 14.13 MiB       |
|        57 | reinvent@10.0.4.4                         |               1416 | 6.66 MiB          | 4.82 KiB          | 6.29 MiB          | 13.52 MiB       |
|       112 | reinvent@10.0.4.4                         |               1759 | 6.66 MiB          | 3.88 KiB          | 6.29 MiB          | 14.17 MiB       |
|        66 | reinvent@10.0.4.4                         |               1428 | 6.64 MiB          | 4.76 KiB          | 6.29 MiB          | 13.47 MiB       |
|        75 | reinvent@10.0.4.4                         |               1389 | 6.62 MiB          | 4.88 KiB          | 6.29 MiB          | 13.40 MiB       |
|       116 | reinvent@10.0.4.4                         |               1333 | 6.61 MiB          | 5.08 KiB          | 6.29 MiB          | 13.21 MiB       |
|        90 | reinvent@10.0.4.4                         |               1448 | 6.59 MiB          | 4.66 KiB          | 6.29 MiB          | 13.58 MiB       |
|        98 | reinvent@10.0.4.4                         |               1440 | 6.57 MiB          | 4.67 KiB          | 6.29 MiB          | 13.52 MiB       |
|        94 | reinvent@10.0.4.4                         |               1433 | 6.57 MiB          | 4.69 KiB          | 6.29 MiB          | 13.49 MiB       |
|        62 | reinvent@10.0.4.4                         |               1323 | 6.55 MiB          | 5.07 KiB          | 6.29 MiB          | 13.48 MiB       |
|        87 | reinvent@10.0.4.4                         |               1323 | 6.55 MiB          | 5.07 KiB          | 6.29 MiB          | 13.25 MiB       |
|        99 | reinvent@10.0.4.4                         |               1346 | 6.54 MiB          | 4.98 KiB          | 6.29 MiB          | 13.24 MiB       |
|       105 | reinvent@10.0.4.4                         |               1347 | 6.54 MiB          | 4.97 KiB          | 6.29 MiB          | 13.34 MiB       |
|        73 | reinvent@10.0.4.4                         |               1335 | 6.54 MiB          | 5.02 KiB          | 6.29 MiB          | 13.23 MiB       |
|        54 | reinvent@10.0.4.4                         |               1510 | 6.53 MiB          | 4.43 KiB          | 6.29 MiB          | 13.49 MiB       |
.                                                                                                                                                          .
.                                                                                                                                                          .
.                                                                                                                                                          .
|       812 | reinvent@10.0.4.4                         |               1259 | 6.38 MiB          | 5.19 KiB          | 6.29 MiB          | 13.05 MiB       |
|       214 | reinvent@10.0.4.4                         |               1279 | 6.38 MiB          | 5.10 KiB          | 6.29 MiB          | 12.90 MiB       |
|       325 | reinvent@10.0.4.4                         |               1254 | 6.38 MiB          | 5.21 KiB          | 6.29 MiB          | 12.99 MiB       |
|       705 | reinvent@10.0.4.4                         |               1273 | 6.37 MiB          | 5.13 KiB          | 6.29 MiB          | 13.03 MiB       |
|       530 | reinvent@10.0.4.4                         |               1268 | 6.37 MiB          | 5.15 KiB          | 6.29 MiB          | 12.92 MiB       |
|       307 | reinvent@10.0.4.4                         |               1263 | 6.37 MiB          | 5.17 KiB          | 6.29 MiB          | 12.87 MiB       |
|       738 | reinvent@10.0.4.4                         |               1260 | 6.37 MiB          | 5.18 KiB          | 6.29 MiB          | 13.00 MiB       |
|       819 | reinvent@10.0.4.4                         |               1252 | 6.37 MiB          | 5.21 KiB          | 6.29 MiB          | 13.01 MiB       |
|        31 | innodb/srv_purge_thread                   |              17810 | 3.14 MiB          |  184 bytes        | 2.40 MiB          | 205.69 MiB      |
|        38 | rdsadmin@localhost                        |                599 | 1.76 MiB          | 3.01 KiB          | 1.00 MiB          | 25.58 MiB       |
|         1 | sql/main                                  |               3756 | 1.32 MiB          |  367 bytes        | 355.78 KiB        | 6.19 MiB        |
|       854 | rdsadmin@localhost                        |                 46 | 1.08 MiB          | 23.98 KiB         | 1.00 MiB          | 5.10 MiB        |
|        30 | innodb/clone_gtid_thread                  |               1596 | 573.14 KiB        |  367 bytes        | 254.91 KiB        | 970.69 KiB      |
|        40 | rdsadmin@localhost                        |                235 | 245.19 KiB        | 1.04 KiB          | 128.88 KiB        | 808.64 KiB      |
|       853 | rdsadmin@localhost                        |                 96 | 94.63 KiB         | 1009 bytes        | 29.73 KiB         | 422.45 KiB      |
|        36 | rdsadmin@localhost                        |                 33 | 36.29 KiB         | 1.10 KiB          | 16.08 KiB         | 74.15 MiB       |
|        33 | sql/event_scheduler                       |                  3 | 16.27 KiB         | 5.42 KiB          | 16.04 KiB         | 16.27 KiB       |
|        35 | sql/compress_gtid_table                   |                  8 | 14.20 KiB         | 1.77 KiB          | 8.05 KiB          | 18.62 KiB       |
|        25 | innodb/fts_optimize_thread                |                 12 | 1.86 KiB          |  158 bytes        |  648 bytes        | 1.98 KiB        |
|        23 | innodb/srv_master_thread                  |                 11 | 1.23 KiB          |  114 bytes        |  361 bytes        | 24.40 KiB       |
|        24 | innodb/dict_stats_thread                  |                 11 | 1.23 KiB          |  114 bytes        |  361 bytes        | 1.35 KiB        |
|         5 | innodb/io_read_thread                     |                  1 |  144 bytes        |  144 bytes        |  144 bytes        |  144 bytes      |
|         6 | innodb/io_read_thread                     |                  1 |  144 bytes        |  144 bytes        |  144 bytes        |  144 bytes      |
|         2 | sql/aws_oscar_log_level_monitor           |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|         4 | innodb/io_ibuf_thread                     |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|         7 | innodb/io_write_thread                    |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|         8 | innodb/io_write_thread                    |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|         9 | innodb/io_write_thread                    |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        10 | innodb/io_write_thread                    |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        11 | innodb/srv_lra_thread                     |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        12 | innodb/srv_akp_thread                     |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        18 | innodb/srv_lock_timeout_thread            |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |  248 bytes      |
|        19 | innodb/srv_error_monitor_thread           |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        20 | innodb/srv_monitor_thread                 |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        21 | innodb/buf_resize_thread                  |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        22 | innodb/btr_search_sys_toggle_thread       |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        32 | innodb/dict_persist_metadata_table_thread |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
|        34 | sql/signal_handler                        |                  0 |    0 bytes        |    0 bytes        |    0 bytes        |    0 bytes      |
+-----------+-------------------------------------------+--------------------+-------------------+-------------------+-------------------+-----------------+
831 rows in set (2.48 sec)
```

As mentioned earlier, the thread ID (`thd_id`) value here can refer to server background threads or database connections. If
you want to map thread ID values to database connection IDs, you can use the `performance_schema.threads` table or the
`sys.processlist` view, where `conn_id` is the connection ID.

```
mysql> SELECT thd_id,conn_id,user,db,command,state,time,last_wait FROM sys.processlist WHERE user='reinvent@10.0.4.4';

+--------+---------+-------------------+----------+---------+----------------+------+-------------------------------------------------+
| thd_id | conn_id | user              | db       | command | state          | time | last_wait                                       |
+--------+---------+-------------------+----------+---------+----------------+------+-------------------------------------------------+
|    590 |     562 | reinvent@10.0.4.4 | sysbench | Execute | closing tables |    0 | wait/io/redo_log_flush                          |
|    578 |     550 | reinvent@10.0.4.4 | sysbench | Sleep   | NULL           |    0 | idle                                            |
|    579 |     551 | reinvent@10.0.4.4 | sysbench | Execute | closing tables |    0 | wait/io/redo_log_flush                          |
|    580 |     552 | reinvent@10.0.4.4 | sysbench | Execute | updating       |    0 | wait/io/table/sql/handler                       |
|    581 |     553 | reinvent@10.0.4.4 | sysbench | Execute | updating       |    0 | wait/io/table/sql/handler                       |
|    582 |     554 | reinvent@10.0.4.4 | sysbench | Sleep   | NULL           |    0 | idle                                            |
|    583 |     555 | reinvent@10.0.4.4 | sysbench | Sleep   | NULL           |    0 | idle                                            |
|    584 |     556 | reinvent@10.0.4.4 | sysbench | Execute | updating       |    0 | wait/io/table/sql/handler                       |
|    585 |     557 | reinvent@10.0.4.4 | sysbench | Execute | closing tables |    0 | wait/io/redo_log_flush                          |
|    586 |     558 | reinvent@10.0.4.4 | sysbench | Execute | updating       |    0 | wait/io/table/sql/handler                       |
|    587 |     559 | reinvent@10.0.4.4 | sysbench | Execute | closing tables |    0 | wait/io/redo_log_flush                          |
.                                                                                                                                     .
.                                                                                                                                     .
.                                                                                                                                     .
|    323 |     295 | reinvent@10.0.4.4 | sysbench | Sleep   | NULL           |    0 | idle                                            |
|    324 |     296 | reinvent@10.0.4.4 | sysbench | Execute | updating       |    0 | wait/io/table/sql/handler                       |
|    325 |     297 | reinvent@10.0.4.4 | sysbench | Execute | closing tables |    0 | wait/io/redo_log_flush                          |
|    326 |     298 | reinvent@10.0.4.4 | sysbench | Execute | updating       |    0 | wait/io/table/sql/handler                       |
|    438 |     410 | reinvent@10.0.4.4 | sysbench | Execute | System lock    |    0 | wait/lock/table/sql/handler                     |
|    280 |     252 | reinvent@10.0.4.4 | sysbench | Sleep   | starting       |    0 | wait/io/socket/sql/client_connection            |
|     98 |      70 | reinvent@10.0.4.4 | sysbench | Query   | freeing items  |    0 | NULL                                            |
+--------+---------+-------------------+----------+---------+----------------+------+-------------------------------------------------+
804 rows in set (5.51 sec)
```

Now we stop the `sysbench` workload, which closes the connections and released the memory. Checking the events again, we can
confirm that memory is released, but `high_alloc` still tells us what the high-water mark is. The `high_alloc` column
can be very useful in identifying short spikes in memory usage, where you might not be able to immediately identify usage from
`current_alloc`, which shows only currently allocated memory.

```
mysql> SELECT * FROM sys.memory_global_by_current_bytes WHERE event_name='memory/sql/Prepared_statement::main_mem_root' LIMIT 10;

+----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| event_name                                   | current_count | current_alloc | current_avg_alloc | high_count | high_alloc | high_avg_alloc |
+----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| memory/sql/Prepared_statement::main_mem_root |            17 | 253.80 KiB    | 14.93 KiB         |     512823 | 4.91 GiB   | 10.04 KiB      |
+----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
1 row in set (0.00 sec)
```

If you want to reset `high_alloc`, you can truncate the `performance_schema` memory summary tables, but this resets
all memory instrumentation. For more information, see [Performance Schema general table
characteristics](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-table-characteristics.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-table-characteristics.html") in the MySQL documentation.

In the following example, we can see that `high_alloc` is reset after truncation.

```
mysql> TRUNCATE `performance_schema`.`memory_summary_global_by_event_name`;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM sys.memory_global_by_current_bytes WHERE event_name='memory/sql/Prepared_statement::main_mem_root' LIMIT 10;

+----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| event_name                                   | current_count | current_alloc | current_avg_alloc | high_count | high_alloc | high_avg_alloc |
+----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| memory/sql/Prepared_statement::main_mem_root |            17 | 253.80 KiB    | 14.93 KiB         |         17 | 253.80 KiB | 14.93 KiB      |
+----------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
1 row in set (0.00 sec)
```

## Example 2: Transient memory spikes

Another common occurrence is short spikes in memory usage on a database server. These can be periodic drops in freeable memory that are
difficult to troubleshoot using `current_alloc` in `sys.memory_global_by_current_bytes`, because the memory has
already been freed.

###### Note

If Performance Schema statistics have been reset, or the database instance has been restarted, this information won't be available in
`sys` or p`erformance_schema`. To retain this information, we recommend that you configure external metrics
collection.

The following graph of the `os.memory.free` metric in Enhanced Monitoring shows brief 7-second spikes in memory usage. Enhanced Monitoring allows you to
monitor at intervals as short as 1 second, which is perfect for catching transient spikes like these.

![Graph showing transient memory usage spikes over time with periodic pattern indicating potential memory management issues.](images/ams-free-memory-spikes.png)

To help diagnose the cause of the memory usage here, we can use a combination of `high_alloc` in the `sys` memory
summary views and [Performance Schema
statement summary tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html") to try to identify offending sessions and connections.

As expected, because memory usage isn't currently high, we can't see any major offenders in the `sys` schema view under
`current_alloc`.

```
mysql> SELECT * FROM sys.memory_global_by_current_bytes LIMIT 10;

+-----------------------------------------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| event_name                                                                  | current_count | current_alloc | current_avg_alloc | high_count | high_alloc | high_avg_alloc |
+-----------------------------------------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
| memory/innodb/hash0hash                                                     |             4 | 79.07 MiB     | 19.77 MiB         |          4 | 79.07 MiB  | 19.77 MiB      |
| memory/innodb/os0event                                                      |        439372 | 60.34 MiB     |  144 bytes        |     439372 | 60.34 MiB  |  144 bytes     |
| memory/performance_schema/events_statements_summary_by_digest               |             1 | 40.28 MiB     | 40.28 MiB         |          1 | 40.28 MiB  | 40.28 MiB      |
| memory/mysys/KEY_CACHE                                                      |             3 | 16.00 MiB     | 5.33 MiB          |          3 | 16.00 MiB  | 5.33 MiB       |
| memory/performance_schema/events_statements_history_long                    |             1 | 14.34 MiB     | 14.34 MiB         |          1 | 14.34 MiB  | 14.34 MiB      |
| memory/performance_schema/events_errors_summary_by_thread_by_error          |           257 | 13.07 MiB     | 52.06 KiB         |        257 | 13.07 MiB  | 52.06 KiB      |
| memory/performance_schema/events_statements_summary_by_thread_by_event_name |             1 | 11.81 MiB     | 11.81 MiB         |          1 | 11.81 MiB  | 11.81 MiB      |
| memory/performance_schema/events_statements_summary_by_digest.digest_text   |             1 | 9.77 MiB      | 9.77 MiB          |          1 | 9.77 MiB   | 9.77 MiB       |
| memory/performance_schema/events_statements_history_long.digest_text        |             1 | 9.77 MiB      | 9.77 MiB          |          1 | 9.77 MiB   | 9.77 MiB       |
| memory/performance_schema/events_statements_history_long.sql_text           |             1 | 9.77 MiB      | 9.77 MiB          |          1 | 9.77 MiB   | 9.77 MiB       |
+-----------------------------------------------------------------------------+---------------+---------------+-------------------+------------+------------+----------------+
10 rows in set (0.01 sec)
```

Expanding the view to order by `high_alloc`, we can now see that the `memory/temptable/physical_ram` component is a
very good candidate here. At its highest, it consumed 515.00 MiB.

As its name suggests, `memory/temptable/physical_ram` instruments memory usage for the `TEMP` storage engine in
MySQL, which was introduced in MySQL 8.0. For more information on how MySQL uses temporary tables, see [Internal temporary table use in MySQL](https://dev.mysql.com/doc/refman/8.0/en/internal-temporary-tables.html "https://dev.mysql.com/doc/refman/8.0/en/internal-temporary-tables.html") in the MySQL
documentation.

###### Note

We're using the `sys.x$memory_global_by_current_bytes` view in this example.

```
mysql> SELECT event_name, format_bytes(current_alloc) AS "currently allocated", sys.format_bytes(high_alloc) AS "high-water mark"
FROM sys.x$memory_global_by_current_bytes ORDER BY high_alloc DESC LIMIT 10;

+-----------------------------------------------------------------------------+---------------------+-----------------+
| event_name                                                                  | currently allocated | high-water mark |
+-----------------------------------------------------------------------------+---------------------+-----------------+
| memory/temptable/physical_ram                                               | 4.00 MiB            | 515.00 MiB      |
| memory/innodb/hash0hash                                                     | 79.07 MiB           | 79.07 MiB       |
| memory/innodb/os0event                                                      | 63.95 MiB           | 63.95 MiB       |
| memory/performance_schema/events_statements_summary_by_digest               | 40.28 MiB           | 40.28 MiB       |
| memory/mysys/KEY_CACHE                                                      | 16.00 MiB           | 16.00 MiB       |
| memory/performance_schema/events_statements_history_long                    | 14.34 MiB           | 14.34 MiB       |
| memory/performance_schema/events_errors_summary_by_thread_by_error          | 13.07 MiB           | 13.07 MiB       |
| memory/performance_schema/events_statements_summary_by_thread_by_event_name | 11.81 MiB           | 11.81 MiB       |
| memory/performance_schema/events_statements_summary_by_digest.digest_text   | 9.77 MiB            | 9.77 MiB        |
| memory/performance_schema/events_statements_history_long.sql_text           | 9.77 MiB            | 9.77 MiB        |
+-----------------------------------------------------------------------------+---------------------+-----------------+
10 rows in set (0.00 sec)
```

In [Example 1: Continuous high memory usage](#ams-workload-memory.example1 "#ams-workload-memory.example1"), we checked the current memory usage for
each connection to determine which connection is responsible for using the memory in question. In this example, the memory is already freed,
so checking the memory usage for current connections isn't useful.

To dig deeper and find the offending statements, users, and hosts, we use the Performance Schema. The Performance Schema contains multiple
statement summary tables that are sliced by different dimensions such as event name, statement digest, host, thread, and user. Each view
will allow you dig deeper into where certain statements are being run and what they are doing. This section is focused on
`MAX_TOTAL_MEMORY`, but you can find more information on all of the columns available in the [Performance Schema statement summary
tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html") documentation.

```
mysql> SHOW TABLES IN performance_schema LIKE 'events_statements_summary_%';

+------------------------------------------------------------+
| Tables_in_performance_schema (events_statements_summary_%) |
+------------------------------------------------------------+
| events_statements_summary_by_account_by_event_name         |
| events_statements_summary_by_digest                        |
| events_statements_summary_by_host_by_event_name            |
| events_statements_summary_by_program                       |
| events_statements_summary_by_thread_by_event_name          |
| events_statements_summary_by_user_by_event_name            |
| events_statements_summary_global_by_event_name             |
+------------------------------------------------------------+
7 rows in set (0.00 sec)
```

First we check `events_statements_summary_by_digest` to see `MAX_TOTAL_MEMORY`.

From this we can see the following:

- The query with digest `20676ce4a690592ff05debcffcbc26faeb76f22005e7628364d7a498769d0c4a` seems to be a good candidate
  for this memory usage. The `MAX_TOTAL_MEMORY` is 537450710, which matches the high-water mark we saw for the
  `memory/temptable/physical_ram` event in `sys.x$memory_global_by_current_bytes`.
- It has been run four times (`COUNT_STAR`), first at 2024-03-26 04:08:34.943256, and last at 2024-03-26
  04:43:06.998310.

```
mysql> SELECT SCHEMA_NAME,DIGEST,COUNT_STAR,MAX_TOTAL_MEMORY,FIRST_SEEN,LAST_SEEN
FROM performance_schema.events_statements_summary_by_digest ORDER BY MAX_TOTAL_MEMORY DESC LIMIT 5;

+-------------+------------------------------------------------------------------+------------+------------------+----------------------------+----------------------------+
| SCHEMA_NAME | DIGEST                                                           | COUNT_STAR | MAX_TOTAL_MEMORY | FIRST_SEEN                 | LAST_SEEN                  |
+-------------+------------------------------------------------------------------+------------+------------------+----------------------------+----------------------------+
| sysbench    | 20676ce4a690592ff05debcffcbc26faeb76f22005e7628364d7a498769d0c4a |          4 |        537450710 | 2024-03-26 04:08:34.943256 | 2024-03-26 04:43:06.998310 |
| NULL        | f158282ea0313fefd0a4778f6e9b92fc7d1e839af59ebd8c5eea35e12732c45d |          4 |          3636413 | 2024-03-26 04:29:32.712348 | 2024-03-26 04:36:26.269329 |
| NULL        | 0046bc5f642c586b8a9afd6ce1ab70612dc5b1fd2408fa8677f370c1b0ca3213 |          2 |          3459965 | 2024-03-26 04:31:37.674008 | 2024-03-26 04:32:09.410718 |
| NULL        | 8924f01bba3c55324701716c7b50071a60b9ceaf17108c71fd064c20c4ab14db |          1 |          3290981 | 2024-03-26 04:31:49.751506 | 2024-03-26 04:31:49.751506 |
| NULL        | 90142bbcb50a744fcec03a1aa336b2169761597ea06d85c7f6ab03b5a4e1d841 |          1 |          3131729 | 2024-03-26 04:15:09.719557 | 2024-03-26 04:15:09.719557 |
+-------------+------------------------------------------------------------------+------------+------------------+----------------------------+----------------------------+
5 rows in set (0.00 sec)
```

Now that we know the offending digest, we can get more details such as the query text, the user who ran it, and where it was run. Based on
the digest text returned, we can see that this is a common table expression (CTE) that creates four temporary tables and performs four table
scans, which is very inefficient.

```
mysql> SELECT SCHEMA_NAME,DIGEST_TEXT,QUERY_SAMPLE_TEXT,MAX_TOTAL_MEMORY,SUM_ROWS_SENT,SUM_ROWS_EXAMINED,SUM_CREATED_TMP_TABLES,SUM_NO_INDEX_USED
FROM performance_schema.events_statements_summary_by_digest
WHERE DIGEST='20676ce4a690592ff05debcffcbc26faeb76f22005e7628364d7a498769d0c4a'\G;

*************************** 1. row ***************************
           SCHEMA_NAME: sysbench
           DIGEST_TEXT: WITH RECURSIVE `cte` ( `n` ) AS ( SELECT ? FROM `sbtest1` UNION ALL SELECT `id` + ? FROM `sbtest1` ) SELECT * FROM `cte`
     QUERY_SAMPLE_TEXT: WITH RECURSIVE cte (n) AS (   SELECT 1  from sbtest1 UNION ALL   SELECT id + 1 FROM sbtest1) SELECT * FROM cte
      MAX_TOTAL_MEMORY: 537450710
         SUM_ROWS_SENT: 80000000
     SUM_ROWS_EXAMINED: 80000000
SUM_CREATED_TMP_TABLES: 4
     SUM_NO_INDEX_USED: 4
1 row in set (0.01 sec)
```

For more information on the `events_statements_summary_by_digest` table and other Performance Schema statement summary tables,
see [Statement summary tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-statement-summary-tables.html")
in the MySQL documentation.

You can also run an [EXPLAIN](https://dev.mysql.com/doc/refman/8.0/en/explain.html "https://dev.mysql.com/doc/refman/8.0/en/explain.html") or [EXPLAIN ANALYZE](https://dev.mysql.com/doc/refman/8.0/en/explain.html#explain-analyze "https://dev.mysql.com/doc/refman/8.0/en/explain.html#explain-analyze") statement to see more details.

###### Note

`EXPLAIN ANALYZE` can provide more information than `EXPLAIN`, but it also runs the query, so be careful.

```
-- EXPLAIN
mysql> EXPLAIN WITH RECURSIVE cte (n) AS (SELECT 1  FROM sbtest1 UNION ALL SELECT id + 1 FROM sbtest1) SELECT * FROM cte;

+----+-------------+------------+------------+-------+---------------+------+---------+------+----------+----------+-------------+
| id | select_type | table      | partitions | type  | possible_keys | key  | key_len | ref  | rows     | filtered | Extra       |
+----+-------------+------------+------------+-------+---------------+------+---------+------+----------+----------+-------------+
|  1 | PRIMARY     | <derived2> | NULL       | ALL   | NULL          | NULL | NULL    | NULL | 19221520 |   100.00 | NULL        |
|  2 | DERIVED     | sbtest1    | NULL       | index | NULL          | k_1  | 4       | NULL |  9610760 |   100.00 | Using index |
|  3 | UNION       | sbtest1    | NULL       | index | NULL          | k_1  | 4       | NULL |  9610760 |   100.00 | Using index |
+----+-------------+------------+------------+-------+---------------+------+---------+------+----------+----------+-------------+
3 rows in set, 1 warning (0.00 sec)

-- EXPLAIN format=tree
mysql> EXPLAIN format=tree WITH RECURSIVE cte (n) AS (SELECT 1 FROM sbtest1 UNION ALL SELECT id + 1 FROM sbtest1) SELECT * FROM cte\G;

*************************** 1. row ***************************
EXPLAIN: -> Table scan on cte  (cost=4.11e+6..4.35e+6 rows=19.2e+6)
    -> Materialize union CTE cte  (cost=4.11e+6..4.11e+6 rows=19.2e+6)
        -> Index scan on sbtest1 using k_1  (cost=1.09e+6 rows=9.61e+6)
        -> Index scan on sbtest1 using k_1  (cost=1.09e+6 rows=9.61e+6)
1 row in set (0.00 sec)

-- EXPLAIN ANALYZE
mysql> EXPLAIN ANALYZE WITH RECURSIVE cte (n) AS (SELECT 1 from sbtest1 UNION ALL SELECT id + 1 FROM sbtest1) SELECT * FROM cte\G;

*************************** 1. row ***************************
EXPLAIN: -> Table scan on cte  (cost=4.11e+6..4.35e+6 rows=19.2e+6) (actual time=6666..9201 rows=20e+6 loops=1)
    -> Materialize union CTE cte  (cost=4.11e+6..4.11e+6 rows=19.2e+6) (actual time=6666..6666 rows=20e+6 loops=1)
        -> Covering index scan on sbtest1 using k_1  (cost=1.09e+6 rows=9.61e+6) (actual time=0.0365..2006 rows=10e+6 loops=1)
        -> Covering index scan on sbtest1 using k_1  (cost=1.09e+6 rows=9.61e+6) (actual time=0.0311..2494 rows=10e+6 loops=1)
1 row in set (10.53 sec)
```

But who ran it? We can see in the Performance Schema that the `destructive_operator` user had `MAX_TOTAL_MEMORY` of
537450710, which again matches the previous results.

###### Note

The Performance Schema is stored in memory, so should not be relied upon as the sole source for auditing. If you need to maintain a
history of statements run, and from which users, we recommend that you enable [Aurora Advanced
Auditing](AuroraMySQL.md "AuroraMySQL.md"). If you also need to maintain information on memory usage, we recommend that you configure monitoring to export and
store these values.

```
mysql> SELECT USER,EVENT_NAME,COUNT_STAR,MAX_TOTAL_MEMORY FROM performance_schema.events_statements_summary_by_user_by_event_name
ORDER BY MAX_CONTROLLED_MEMORY DESC LIMIT 5;

+----------------------+---------------------------+------------+------------------+
| USER                 | EVENT_NAME                | COUNT_STAR | MAX_TOTAL_MEMORY |
+----------------------+---------------------------+------------+------------------+
| destructive_operator | statement/sql/select      |          4 |        537450710 |
| rdsadmin             | statement/sql/select      |       4172 |          3290981 |
| rdsadmin             | statement/sql/show_tables |          2 |          3615821 |
| rdsadmin             | statement/sql/show_fields |          2 |          3459965 |
| rdsadmin             | statement/sql/show_status |         75 |          1914976 |
+----------------------+---------------------------+------------+------------------+
5 rows in set (0.00 sec)

mysql> SELECT HOST,EVENT_NAME,COUNT_STAR,MAX_TOTAL_MEMORY FROM performance_schema.events_statements_summary_by_host_by_event_name
WHERE HOST != 'localhost' AND COUNT_STAR>0 ORDER BY MAX_CONTROLLED_MEMORY DESC LIMIT 5;

+------------+----------------------+------------+------------------+
| HOST       | EVENT_NAME           | COUNT_STAR | MAX_TOTAL_MEMORY |
+------------+----------------------+------------+------------------+
| 10.0.8.231 | statement/sql/select |          4 |        537450710 |
+------------+----------------------+------------+------------------+
1 row in set (0.00 sec)
```

## Example 3: Freeable memory drops continuously and isn't reclaimed

The InnoDB database engine employs a range of specialized memory tracking events for different components. These specific events allow for
granular tracking of memory usage in key InnoDB subsystems, for example:

- `memory/innodb/buf0buf` – Dedicated to monitoring memory allocations for the InnoDB buffer pool.
- `memory/innodb/ibuf0ibuf` – Specifically tracks memory changes related to the InnoDB change buffer.

To identify the top consumers of memory, we can query `sys.memory_global_by_current_bytes`:

```
mysql> SELECT event_name,current_alloc FROM sys.memory_global_by_current_bytes LIMIT 10;

+-----------------------------------------------------------------+---------------+
| event_name                                                      | current_alloc |
+-----------------------------------------------------------------+---------------+
| memory/innodb/memory                                            | 5.28 GiB      |
| memory/performance_schema/table_io_waits_summary_by_index_usage | 495.00 MiB    |
| memory/performance_schema/table_shares                          | 488.00 MiB    |
| memory/sql/TABLE_SHARE::mem_root                                | 388.95 MiB    |
| memory/innodb/std                                               | 226.88 MiB    |
| memory/innodb/fil0fil                                           | 198.49 MiB    |
| memory/sql/binlog_io_cache                                      | 128.00 MiB    |
| memory/innodb/mem0mem                                           | 96.82 MiB     |
| memory/innodb/dict0dict                                         | 96.76 MiB     |
| memory/performance_schema/rwlock_instances                      | 88.00 MiB     |
+-----------------------------------------------------------------+---------------+
10 rows in set (0.00 sec)
```

The results show that `memory/innodb/memory` is the top consumer, using 5.28 GiB of currently allocated memory. This event
serves as a category for memory allocations across various InnoDB components not associated with more specific wait events, such as
`memory/innodb/buf0buf` mentioned previously.

Having established that InnoDB components are the primary consumers of memory, we can dive deeper into the specifics using the following
MySQL command:

```
SHOW ENGINE INNODB STATUS \G;
```

The [SHOW ENGINE INNODB STATUS](https://dev.mysql.com/doc/refman/8.4/en/show-engine.html "https://dev.mysql.com/doc/refman/8.4/en/show-engine.html") command provides a
comprehensive status report for the InnoDB storage engine, including detailed memory usage statistics for different InnoDB components. It
can help identify which specific InnoDB structures or operations are consuming the most memory. For more information, see [InnoDB in-memory structures](https://dev.mysql.com/doc/refman/8.0/en/innodb-in-memory-structures.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-in-memory-structures.html") in the MySQL
documentation.

Analyzing the `BUFFER POOL AND MEMORY` section of the InnoDB status report, we see that 5,051,647,748 bytes (4.7 GiB) is
allocated to the [dictionary object cache](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-object-cache.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-object-cache.html"),
which accounts for 89% of the memory tracked by `memory/innodb/memory`.

```
----------------------
BUFFER POOL AND MEMORY
----------------------
Total large memory allocated 0
**`Dictionary memory allocated 5051647748`**
Buffer pool size 170512
Free buffers 142568
Database pages 27944
Old database pages 10354
Modified db pages 6
Pending reads 0
```

The dictionary object cache is a shared global cache that stores previously accessed data dictionary objects in memory to enable object
reuse and improve performance. The high memory allocation to the dictionary object cache suggests a large number of database objects in the
data dictionary cache.

Now that we know that the data dictionary cache is a primary consumer, we proceed to inspect the data dictionary cache for open tables. To
find the number of tables in the table definition cache, query the global status variable [open_table_definitions](https://dev.mysql.com/doc/refman/8.4/en/server-status-variables.html#statvar_Open_table_definitions "https://dev.mysql.com/doc/refman/8.4/en/server-status-variables.html#statvar_Open_table_definitions").

```
mysql> show global status like 'open_table_definitions';

+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| Open_table_definitions | 20000 |
+------------------------+-------+
1 row in set (0.00 sec)
```

For more information, see [How MySQL opens and closes tables](https://dev.mysql.com/doc/refman/8.0/en/table-cache.html "https://dev.mysql.com/doc/refman/8.0/en/table-cache.html")
in the MySQL documentation.

You can limit the number of table definitions in the data dictionary cache by limiting the `table_definition_cache` parameter
in the DB cluster or DB instance parameter group. For Aurora MySQL, this value serves as a soft limit for the number of tables in the table
definition cache. The default value is dependent on the instance class and is set to the following:

```
LEAST({DBInstanceClassMemory/393040}, 20000)
```

When the number of tables exceeds the `table_definition_cache` limit, a least recently used (LRU) mechanism evicts and remove
tables from the cache. However, tables involved in foreign key relationships aren't placed in the LRU list, preventing their removal.

In our current scenario, we run [FLUSH TABLES](https://dev.mysql.com/doc/refman/8.4/en/flush.html "https://dev.mysql.com/doc/refman/8.4/en/flush.html") to clear the table
definition cache. This action results in a significant drop in the [Open_table_definitions](https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html#statvar_Open_table_definitions "https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html#statvar_Open_table_definitions")
global status variable, from 20,000 to 12, as shown here:

```
mysql> show global status like 'open_table_definitions';

+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| Open_table_definitions | 12    |
+------------------------+-------+
1 row in set (0.00 sec)
```

Despite this reduction, we observe that the memory allocation for `memory/innodb/memory` remains high at 5.18 GiB, and the
dictionary memory allocated also remains unchanged. This is evident from the following query results:

```
mysql> SELECT event_name,current_alloc FROM sys.memory_global_by_current_bytes LIMIT 10;

+-----------------------------------------------------------------+---------------+
| event_name                                                      | current_alloc |
+-----------------------------------------------------------------+---------------+
| memory/innodb/memory                                            | 5.18 GiB      |
| memory/performance_schema/table_io_waits_summary_by_index_usage | 495.00 MiB    |
| memory/performance_schema/table_shares                          | 488.00 MiB    |
| memory/sql/TABLE_SHARE::mem_root                                | 388.95 MiB    |
| memory/innodb/std                                               | 226.88 MiB    |
| memory/innodb/fil0fil                                           | 198.49 MiB    |
| memory/sql/binlog_io_cache                                      | 128.00 MiB    |
| memory/innodb/mem0mem                                           | 96.82 MiB     |
| memory/innodb/dict0dict                                         | 96.76 MiB     |
| memory/performance_schema/rwlock_instances                      | 88.00 MiB     |
+-----------------------------------------------------------------+---------------+
10 rows in set (0.00 sec)
```

```
----------------------
BUFFER POOL AND MEMORY
----------------------
Total large memory allocated 0
**`Dictionary memory allocated 5001599639`**
Buffer pool size 170512
Free buffers 142568
Database pages 27944
Old database pages 10354
Modified db pages 6
Pending reads 0
```

This persistently high memory usage can be attributed to tables involved in foreign key relationships. These tables aren't placed in the
LRU list for removal, explaining why the memory allocation remains high even after flushing the table definition cache.

To address this issue:

1. Review and optimize your database schema, particularly foreign key relationships.
2. Consider moving to a larger DB instance class that has more memory to accommodate your dictionary objects.

By following these steps and understanding the memory allocation patterns, you can better manage memory usage in your Aurora MySQL DB
instance and prevent potential performance issues due to memory pressure.
