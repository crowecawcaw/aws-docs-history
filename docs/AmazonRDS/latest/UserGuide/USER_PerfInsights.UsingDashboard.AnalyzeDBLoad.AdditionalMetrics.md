# SQL statistics for Amazon RDS for Oracle

Amazon RDS for Oracle collects SQL statistics both at the statement and digest level. At the statement level, the ID column represents the
value of `V$SQL.SQL_ID`. At the digest level, the ID column shows the value of `V$SQL.FORCE_MATCHING_SIGNATURE`.

If the ID is `0` at the digest level, Oracle Database has determined that this statement is not suitable for reuse. In this
case, the child SQL statements could belong to different digests. However, the statements are grouped together under the
`digest_text` for the first SQL statement collected.

###### Topics

- [Per-second statistics for
  Oracle](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.per-second "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.per-second")
- [Per-call statistics for
  Oracle](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.per-call "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.per-call")
- [Primary statistics for
  Oracle](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.primary "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.primary")

## Per-second statistics for

Oracle

The following metrics provide per-second statistics for an Oracle SQL query.

| Metric                                       | Unit                                         |
| -------------------------------------------- | -------------------------------------------- |
| db.sql.stats.executions_per_sec              | Number of executions per second              |
| db.sql.stats.elapsed_time_per_sec            | Average active executions (AAE)              |
| db.sql.stats.rows_processed_per_sec          | Rows processed per second                    |
| db.sql.stats.buffer_gets_per_sec             | Buffer gets per second                       |
| db.sql.stats.physical_read_requests_per_sec  | Physical reads per second                    |
| db.sql.stats.physical_write_requests_per_sec | Physical writes per second                   |
| db.sql.stats.total_sharable_mem_per_sec      | Total shareable memory per second (in bytes) |
| db.sql.stats.cpu_time_per_sec                | CPU time per second (in ms)                  |

The following metrics provide per-second statistics for an Oracle SQL digest query.

| Metric                                                 | Unit                                         |
| ------------------------------------------------------ | -------------------------------------------- |
| db.sql_tokenized.stats.executions_per_sec              | Number of executions per second              |
| db.sql_tokenized.stats.elapsed_time_per_sec            | Average active executions (AAE)              |
| db.sql_tokenized.stats.rows_processed_per_sec          | Rows processed per second                    |
| db.sql_tokenized.stats.buffer_gets_per_sec             | Buffer gets per second                       |
| db.sql_tokenized.stats.physical_read_requests_per_sec  | Physical reads per second                    |
| db.sql_tokenized.stats.physical_write_requests_per_sec | Physical writes per second                   |
| db.sql_tokenized.stats.total_sharable_mem_per_sec      | Total shareable memory per second (in bytes) |
| db.sql_tokenized.stats.cpu_time_per_sec                | CPU time per second (in ms)                  |

## Per-call statistics for

Oracle

The following metrics provide per-call statistics for an Oracle SQL statement.

| Metric                                        | Unit                                            |
| --------------------------------------------- | ----------------------------------------------- |
| db.sql.stats.elapsed_time_per_exec            | Elapsed time per executions (in ms)             |
| db.sql.stats.rows_processed_per_exec          | Rows processed per execution                    |
| db.sql.stats.buffer_gets_per_exec             | Buffer gets per execution                       |
| db.sql.stats.physical_read_requests_per_exec  | Physical reads per execution                    |
| db.sql.stats.physical_write_requests_per_exec | Physical writes per execution                   |
| db.sql.stats.total_sharable_mem_per_exec      | Total shareable memory per execution (in bytes) |
| db.sql.stats.cpu_time_per_exec                | CPU time per execution (in ms)                  |

The following metrics provide per-call statistics for an Oracle SQL digest query.

| Metric                                                  | Unit                                            |
| ------------------------------------------------------- | ----------------------------------------------- |
| db.sql_tokenized.stats.elapsed_time_per_exec            | Elapsed time per executions (in ms)             |
| db.sql_tokenized.stats.rows_processed_per_exec          | Rows processed per execution                    |
| db.sql_tokenized.stats.buffer_gets_per_exec             | Buffer gets per execution                       |
| db.sql_tokenized.stats.physical_read_requests_per_exec  | Physical reads per execution                    |
| db.sql_tokenized.stats.physical_write_requests_per_exec | Physical writes per execution                   |
| db.sql_tokenized.stats.total_sharable_mem_per_exec      | Total shareable memory per execution (in bytes) |
| db.sql_tokenized.stats.cpu_time_per_exec                | CPU time per execution (in ms)                  |

## Primary statistics for

Oracle

The following metrics provide primary statistics for an Oracle SQL query.

| Metric                               | Unit                              |
| ------------------------------------ | --------------------------------- |
| db.sql.stats.executions              | Number of executions              |
| db.sql.stats.elapsed_time            | Elapsed time (in ms)              |
| db.sql.stats.rows_processed          | Rows processed                    |
| db.sql.stats.buffer_gets             | Buffer gets                       |
| db.sql.stats.physical_read_requests  | Physical reads                    |
| db.sql.stats.physical_write_requests | Physical writes                   |
| db.sql.stats.total_sharable_mem      | Total shareable memory (in bytes) |
| db.sql.stats.cpu_time                | CPU time (in ms)                  |

The following metrics provide primary statistics for an Oracle SQL digest query.

| Metric                                         | Unit                              |
| ---------------------------------------------- | --------------------------------- |
| db.sql_tokenized.stats.executions              | Number of executions              |
| db.sql_tokenized.stats.elapsed_time            | Elapsed time (in ms)              |
| db.sql_tokenized.stats.rows_processed          | Rows processed                    |
| db.sql_tokenized.stats.buffer_gets             | Buffer gets                       |
| db.sql_tokenized.stats.physical_read_requests  | Physical reads                    |
| db.sql_tokenized.stats.physical_write_requests | Physical writes                   |
| db.sql_tokenized.stats.total_sharable_mem      | Total shareable memory (in bytes) |
| db.sql_tokenized.stats.cpu_time                | CPU time (in ms)                  |
