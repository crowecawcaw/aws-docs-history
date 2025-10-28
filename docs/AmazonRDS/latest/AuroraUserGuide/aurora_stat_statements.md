# aurora_stat_statements

Displays all `pg_stat_statements` columns and adds more columns in the end.

## Syntax

```
aurora_stat_statements(`showtext boolean`)
```

## Arguments

_showtext boolean_

## Return type

SETOF record with all `pg_stat_statements` columns and the following
additional columns. For more information on `pg_stat_statements` columns,
see [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html "https://www.postgresql.org/docs/current/pgstatstatements.html").

You can reset stats for this function using
`pg_stat_statements_reset()`.

- `storage_blks_read` – Total number of shared blocks read
  from aurora storage by this statement.
- `orcache_blks_hit` – Total number of optimized reads
  cache hits by this statement.
- `storage_blk_read_time` – If
  `track_io_timing` is enabled, it tracks the total time the
  statement spent reading shared blocks from aurora storage, in milliseconds,
  otherwise the value is zero. For more information, see [track_io_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING "https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING").
- `local_blk_read_time` – If `track_io_timing`
  is enabled, it tracks the total time the statement spent reading local
  blocks, in milliseconds, otherwise the value is zero. For more information,
  see [track_io_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING "https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING").
- `orcache_blk_read_time` – If
  `track_io_timing` is enabled, it tracks the total time the
  statement spent reading shared blocks from optimized reads cache, in
  milliseconds, otherwise the value is zero. For more information, see [track_io_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING "https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING").
- `total_plan_peakmem` – Total sum of peak memory values
  during planning phase for all calls to this statement. To see the average
  peak memory during planning for the statement, divide this value by the
  number of calls.
- `min_plan_peakmem` – Smallest peak memory value seen
  during planning across all calls to this statement.
- `max_plan_peakmem` – Largest peak memory value during
  planning seen across all calls to this statement.
- `total_exec_peakmem` – Total sum of peak memory values
  during execution phase for all calls to this statement. To see the average
  peak memory during execution for the statement, divide this value by the
  number of calls.
- `min_exec_peakmem` –Smallest peak memory value, in
  bytes, seen during execution across all calls to this statement.
- `max_exec_peakmem` – Largest peak memory value, in
  bytes, seen during execution across all calls to this statement.

###### Note

`total_plan_peakmen`, `min_plan_peakmem`, and
`max_plan_peakmem` are only monitored when the setting
`pg_stat_statements.track_planning` is turned on.

## Usage notes

To use the aurora_stat_statements() function, you must include
`pg_stat_statements` extension in the
`shared_preload_libraries` parameter.

This function is available in the following Aurora PostgreSQL versions:

- 15.4 and higher 15 versions
- 14.9 and higher 14 versions

The columns showing peak memory are available from the following versions:

- 16.3 and higher versions
- 15.7 and higher versions
- 14.12 and higher versions

## Examples

The following example shows how it carries all the pg_stat_statements columns and
append 11 new columns in the end:

```
`=>` `select * from aurora_stat_statements(true) where query like 'with window_max%';`
-[ RECORD 1 ]----------+------------------------------------------------------------------------------------------------
userid                 | 16409
dbid                   | 5
toplevel               | t
queryid                | -8347523682669847482
query                  | with window_max as (select custid, max(scratch) over (order by scratch rows between $1 preceding
and $2 following) wmax from ts) select sum(wmax), max(custid) from window_max
plans                  | 0
total_plan_time        | 0
min_plan_time          | 0
max_plan_time          | 0
mean_plan_time         | 0
stddev_plan_time       | 0
calls                  | 4
total_exec_time        | 254.105121
min_exec_time          | 57.503164000000005
max_exec_time          | 68.687418
mean_exec_time         | 63.52628025
stddev_exec_time       | 5.150765359979643
rows                   | 4
shared_blks_hit        | 200192
shared_blks_read       | 0
shared_blks_dirtied    | 0
shared_blks_written    | 0
local_blks_hit         | 0
local_blks_read        | 0
local_blks_dirtied     | 0
local_blks_written     | 0
temp_blks_read         | 0
temp_blks_written      | 0
blk_read_time          | 0
blk_write_time         | 0
temp_blk_read_time     | 0
temp_blk_write_time    | 0
wal_records            | 0
wal_fpi                | 0
wal_bytes              | 0
jit_functions          | 0
jit_generation_time    | 0
jit_inlining_count     | 0
jit_inlining_time      | 0
jit_optimization_count | 0
jit_optimization_time  | 0
jit_emission_count     | 0
jit_emission_time      | 0
storage_blks_read      | 0
orcache_blks_hit       | 0
storage_blk_read_time  | 0
local_blk_read_time    | 0
orcache_blk_read_time  | 0
total_plan_peakmem     | 0
min_plan_peakmem       | 0
max_plan_peakmem       | 0
total_exec_peakmem     | 6356224
min_exec_peakmem       | 1589056
max_exec_peakmem       | 1589056

```
