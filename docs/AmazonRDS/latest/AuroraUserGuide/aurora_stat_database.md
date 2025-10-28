# aurora_stat_database

It carries all columns of pg_stat_database and adds new columns in the end.

## Syntax

```
aurora_stat_database()
```

## Arguments

None

## Return type

SETOF record with all `pg_stat_database` columns and the following
additional columns. For more information on `pg_stat_database` columns,
see [`pg_stat_database`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW "https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW").

- `storage_blks_read` – Total number of shared blocks read
  from aurora storage in this database.
- `orcache_blks_hit` – Total number of optimized reads
  cache hits in this database.
- `local_blks_read` – Total number of local blocks read in
  this database.
- `storage_blk_read_time` – If
  `track_io_timing` is enabled, it tracks the total time spent
  reading data file blocks from aurora storage, in milliseconds, otherwise the
  value is zero. For more information, see [track_io_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING "https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING").
- `local_blk_read_time` – If `track_io_timing`
  is enabled, it tracks the total time spent reading local data file blocks,
  in milliseconds, otherwise the value is zero. For more information, see
  [track_io_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING "https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING").
- `orcache_blk_read_time` – If
  `track_io_timing` is enabled, it tracks the total time spent
  reading data file blocks from optimized reads cache, in milliseconds,
  otherwise the value is zero. For more information, see [track_io_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING "https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING").

###### Note

The value of `blks_read` is the sum of
`storage_blks_read`, `orcache_blks_hit`, and
`local_blks_read`.

The value of `blk_read_time` is the sum of
`storage_blk_read_time`, `orcache_blk_read_time`, and
`local_blk_read_time`.

## Usage notes

This function is available in the following Aurora PostgreSQL versions:

- 15.4 and higher 15 versions
- 14.9 and higher 14 versions

## Examples

The following example shows how it carries all the `pg_stat_database`
columns and appends 6 new columns in the end:

```
`=>` `select * from aurora_stat_database() where datid=14717;` `-[ RECORD 1 ]------------+------------------------------
datid | 14717
datname | postgres
numbackends | 1
xact_commit | 223
xact_rollback | 4
blks_read | 1059
blks_hit | 11456
tup_returned | 27746
tup_fetched | 5220
tup_inserted | 165
tup_updated | 42
tup_deleted | 91
conflicts | 0
temp_files | 0
temp_bytes | 0
deadlocks | 0
checksum_failures |
checksum_last_failure |
blk_read_time | 3358.689
blk_write_time | 0
session_time | 1076007.997
active_time | 3684.371
idle_in_transaction_time | 0
sessions | 10
sessions_abandoned | 0
sessions_fatal | 0
sessions_killed | 0
stats_reset | 2023-01-12 20:15:17.370601+00
orcache_blks_hit | 425
orcache_blk_read_time | 89.934
storage_blks_read | 623
storage_blk_read_time | 3254.914
local_blks_read | 0
local_blk_read_time | 0`
```
