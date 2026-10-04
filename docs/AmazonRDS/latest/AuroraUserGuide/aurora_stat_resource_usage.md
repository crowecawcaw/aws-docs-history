

# aurora\_stat\_resource\_usage
<a name="aurora_stat_resource_usage"></a>

Reports the real-time resource utilization which consists of backend resource metrics and cpu usage for all Aurora PostgreSQL backend processes.

## Syntax
<a name="aurora_stat_resource_usage-syntax"></a>

```
aurora_stat_resource_usage()
```

## Arguments
<a name="aurora_stat_resource_usage-arguments"></a>

None

## Return type
<a name="aurora_stat_resource_usage-return-type"></a>

SETOF record with columns:
+ pid - Process identifier
+ allocated\_memory - Total memory allocated by process in bytes
+ used\_memory - Actually used memory by process in bytes
+ cpu\_usage\_percent - CPU usage percentage of the process (all threads)
+ worker\_threads\_cpu\_usage\_percent - CPU usage percentage of the worker threads (all threads except the main thread) of the process. For backend processes that don't use worker threads, this value is 0.

## Usage notes
<a name="aurora_stat_resource_usage-usage-notes"></a>

This function displays the backend resource usage for each Aurora PostgreSQL backend process.

This function is available starting with the following Aurora PostgreSQL versions:
+ Aurora PostgreSQL 17.5 and higher 17 versions
+ Aurora PostgreSQL 16.9 and higher 16 versions
+ Aurora PostgreSQL 15.13 and higher 15 versions
+ Aurora PostgreSQL 14.18 and higher 14 versions
+ Aurora PostgreSQL 13.21 and higher 13 versions

The `worker_threads_cpu_usage_percent` column is available starting with the following Aurora PostgreSQL versions:
+ Aurora PostgreSQL 18.6 and higher 18 versions
+ Aurora PostgreSQL 17.11 and higher 17 versions
+ Aurora PostgreSQL 16.15 and higher 16 versions
+ Aurora PostgreSQL 15.19 and higher 15 versions
+ Aurora PostgreSQL 14.24 and higher 14 versions

In earlier versions, the function returns only the first four columns.

## Examples
<a name="aurora_stat_resource_usage-examples"></a>

The following example shows the output of the `aurora_stat_resource_usage` function.

```
=> select * from aurora_stat_resource_usage();
 pid  | allocated_memory | used_memory |   cpu_usage_percent   | worker_threads_cpu_usage_percent
------+------------------+-------------+-----------------------+----------------------------------
  666 |          1074032 |      333544 |   0.00729274882897963 |                                0
  668 |          3076776 |     1563488 |  0.006013116835953961 |                                0
 2401 |          1232992 |      943144 |                     0 |                                0
  664 |          1161616 |      797584 |     81.19999999999999 |                             67.8
  671 |          1087888 |      789352 |                  62.4 |                             52.4
(5 rows)
```

*The last two rows show backend processes whose worker threads consume CPU. For backend processes that don't use worker threads, the value is 0.*