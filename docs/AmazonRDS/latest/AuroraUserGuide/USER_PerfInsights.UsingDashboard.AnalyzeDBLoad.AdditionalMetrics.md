# SQL statistics for Aurora PostgreSQL

For each SQL call and for each second that a query runs, Performance Insights collects
SQL statistics. All Aurora engines collect statistics only at the digest-level.

Following, you can find information about digest-level statistics for
Aurora PostgreSQL.

###### Topics

- [Digest statistics for Aurora PostgreSQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.digest "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.digest")
- [Per-second digest statistics
  for Aurora PostgreSQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.per-second "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.per-second")
- [Per-call digest statistics for
  Aurora PostgreSQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.per-call "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.per-call")
- [Primary statistics
  for Aurora PostgreSQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.primary "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.primary")

## Digest statistics for Aurora PostgreSQL

To view SQL digest statistics, the `pg_stat_statements` library must be loaded. For Aurora PostgreSQL
DB clusters that are compatible with PostgreSQL 10, this library is loaded by default. For Aurora PostgreSQL DB clusters that are
compatible with PostgreSQL 9.6, you enable this library manually. To enable it manually, add `pg_stat_statements` to
`shared_preload_libraries` in the DB parameter group associated with the DB instance. Then reboot your DB instance. For
more information, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### Note

Performance Insights can only collect statistics for queries in `pg_stat_activity` that aren't truncated. By
default, PostgreSQL databases truncate queries longer than 1,024 bytes. To increase the query size, change the
`track_activity_query_size` parameter in the DB parameter group associated with your DB instance. When you change
this parameter, a DB instance reboot is required.

## Per-second digest statistics

for Aurora PostgreSQL

The following SQL digest statistics are available for Aurora PostgreSQL DB instances.

| Metric                                             | Unit                                       |
| -------------------------------------------------- | ------------------------------------------ |
| db.sql_tokenized.stats.calls_per_sec               | Calls per second                           |
| db.sql_tokenized.stats.rows_per_sec                | Rows per second                            |
| db.sql_tokenized.stats.total_time_per_sec          | Average active executions per second (AAE) |
| db.sql_tokenized.stats.shared_blks_hit_per_sec     | Block hits per second                      |
| db.sql_tokenized.stats.shared_blks_read_per_sec    | Block reads per second                     |
| db.sql_tokenized.stats.shared_blks_dirtied_per_sec | Blocks dirtied per second                  |
| db.sql_tokenized.stats.shared_blks_written_per_sec | Block writes per second                    |
| db.sql_tokenized.stats.local_blks_hit_per_sec      | Local block hits per second                |
| db.sql_tokenized.stats.local_blks_read_per_sec     | Local block reads per second               |
| db.sql_tokenized.stats.local_blks_dirtied_per_sec  | Local block dirtied per second             |
| db.sql_tokenized.stats.local_blks_written_per_sec  | Local block writes per second              |
| db.sql_tokenized.stats.temp_blks_written_per_sec   | Temporary writes per second                |
| db.sql_tokenized.stats.temp_blks_read_per_sec      | Temporary reads per second                 |
| db.sql_tokenized.stats.blk_read_time_per_sec       | Average concurrent reads per second        |
| db.sql_tokenized.stats.blk_write_time_per_sec      | Average concurrent writes per second       |

## Per-call digest statistics for

Aurora PostgreSQL

The following metrics provide per call statistics for a SQL statement.

| Metric                                              | Unit                             |
| --------------------------------------------------- | -------------------------------- |
| db.sql_tokenized.stats.rows_per_call                | Rows per call                    |
| db.sql_tokenized.stats.avg_latency_per_call         | Average latency per call (in ms) |
| db.sql_tokenized.stats.shared_blks_hit_per_call     | Block hits per call              |
| db.sql_tokenized.stats.shared_blks_read_per_call    | Block reads per call             |
| db.sql_tokenized.stats.shared_blks_written_per_call | Block writes per call            |
| db.sql_tokenized.stats.shared_blks_dirtied_per_call | Blocks dirtied per call          |
| db.sql_tokenized.stats.local_blks_hit_per_call      | Local block hits per call        |
| db.sql_tokenized.stats.local_blks_read_per_call     | Local block reads per call       |
| db.sql_tokenized.stats.local_blks_dirtied_per_call  | Local block dirtied per call     |
| db.sql_tokenized.stats.local_blks_written_per_call  | Local block writes per call      |
| db.sql_tokenized.stats.temp_blks_written_per_call   | Temporary block writes per call  |
| db.sql_tokenized.stats.temp_blks_read_per_call      | Temporary block reads per call   |
| db.sql_tokenized.stats.blk_read_time_per_call       | Read time per call (in ms)       |
| db.sql_tokenized.stats.blk_write_time_per_call      | Write time per call (in ms)      |

## Primary statistics

for Aurora PostgreSQL

The following SQL statistics are available for Aurora PostgreSQL DB instances.

| Metric                                     | Unit                              |
| ------------------------------------------ | --------------------------------- |
| db.sql_tokenized.stats.calls               | Calls                             |
| db.sql_tokenized.stats.rows                | Rows                              |
| db.sql_tokenized.stats.total_time          | Total time (in ms)                |
| db.sql_tokenized.stats.shared_blks_hit     | Block hits                        |
| db.sql_tokenized.stats.shared_blks_read    | Block reads                       |
| db.sql_tokenized.stats.shared_blks_dirtied | Blocks dirtied                    |
| db.sql_tokenized.stats.shared_blks_written | Block writes                      |
| db.sql_tokenized.stats.local_blks_hit      | Local block hits                  |
| db.sql_tokenized.stats.local_blks_read     | Local block reads                 |
| db.sql_tokenized.stats.local_blks_dirtied  | Local blocks dirtied              |
| db.sql_tokenized.stats.local_blks_written  | Local block writes                |
| db.sql_tokenized.stats.temp_blks_written   | Temporary writes                  |
| db.sql_tokenized.stats.temp_blks_read      | Temporary reads                   |
| db.sql_tokenized.stats.blk_read_time       | Average concurrent reads (in ms)  |
| db.sql_tokenized.stats.blk_write_time      | Average concurrent writes (in ms) |

For more information about these metrics, see [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html "https://www.postgresql.org/docs/current/pgstatstatements.html") in the PostgreSQL documentation.
