# SQL statistics for Amazon RDS for SQL Server

Amazon RDS for SQL Server collects SQL statistics both at the statement and digest level. At the statement level, the ID column represents the
value of `sql_handle`. At the digest level, the ID column shows the value of `query_hash`.

SQL Server returns NULL values for `query_hash` for a few statements. For example, ALTER INDEX, CHECKPOINT,
UPDATE STATISTICS, COMMIT TRANSACTION, FETCH NEXT FROM Cursor, and a few INSERT statements, SELECT @<variable>, conditional statements,
and executable stored procedures. In this case, the `sql_handle` value is displayed as the ID at the digest level for that statement.

###### Topics

- [Per-second statistics for
  SQL Server](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-second "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-second")
- [Per-call statistics for SQL Server](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-call "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-call")
- [Primary statistics for
  SQL Server](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.primary "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.primary")

## Per-second statistics for

SQL Server

The following metrics provide per-second statistics for a SQL Server SQL query.

| Metric                                    | Unit                            |
| ----------------------------------------- | ------------------------------- |
| db.sql.stats.execution_count_per_sec      | Number of executions per second |
| db.sql.stats.total_elapsed_time_per_sec   | Total elapsed time per second   |
| db.sql.stats.total_rows_per_sec           | Total rows processed per second |
| db.sql.stats.total_logical_reads_per_sec  | Total logical reads per second  |
| db.sql.stats.total_logical_writes_per_sec | Total logical writes per second |
| db.sql.stats.total_physical_reads_per_sec | Total physical reads per second |
| db.sql.stats.total_worker_time_per_sec    | Total CPU time (in ms)          |

The following metrics provide per-second statistics for a SQL Server SQL digest
query.

| Metric                                              | Unit                            |
| --------------------------------------------------- | ------------------------------- |
| db.sql_tokenized.stats.execution_count_per_sec      | Number of execution per second  |
| db.sql_tokenized.stats.total_elapsed_time_per_sec   | Total elapsed time per second   |
| db.sql_tokenized.stats.total_rows_per_sec           | Total rows processed per second |
| db.sql_tokenized.stats.total_logical_reads_per_sec  | Total logical reads per second  |
| db.sql_tokenized.stats.total_logical_writes_per_sec | Total logical writes per second |
| db.sql_tokenized.stats.total_physical_reads_per_sec | Total physical reads per second |
| db.sql_tokenized.stats.total_worker_time_per_sec    | Total CPU time (in ms)          |

## Per-call statistics for SQL Server

The following metrics provide per-call statistics for a SQL Server SQL statement.

| Metric                                     | Unit                                     |
| ------------------------------------------ | ---------------------------------------- |
| db.sql.stats.total_elapsed_time_per_call   | Total elapsed time per execution (in ms) |
| db.sql.stats.total_rows_per_call           | Total rows processed per execution       |
| db.sql.stats.total_logical_reads_per_call  | Total logical reads per execution        |
| db.sql.stats.total_logical_writes_per_call | Total logical writes per execution       |
| db.sql.stats.total_physical_reads_per_call | Total physical reads per execution       |
| db.sql.stats.total_worker_time_per_call    | Total CPU time per execution (in ms)     |

The following metrics provide per-call statistics for a SQL Server SQL digest query.

| Metric                                               | Unit                                 |
| ---------------------------------------------------- | ------------------------------------ |
| db.sql_tokenized.stats.total_elapsed_time_per_call   | Total elapsed time per execution     |
| db.sql_tokenized.stats.total_rows_per_call           | Total rows processed per execution   |
| db.sql_tokenized.stats.total_logical_reads_per_call  | Total logical reads per execution    |
| db.sql_tokenized.stats.total_logical_writes_per_call | Total logical writes per execution   |
| db.sql_tokenized.stats.total_physical_reads_per_call | Total physical reads per execution   |
| db.sql_tokenized.stats.total_worker_time_per_call    | Total CPU time per execution (in ms) |

## Primary statistics for

SQL Server

The following metrics provide primary statistics for a SQL Server SQL query.

| Metric                            | Unit                       |
| --------------------------------- | -------------------------- |
| db.sql.stats.execution_count      | Number of executions       |
| db.sql.stats.total_elapsed_time   | Total elapsed time (in ms) |
| db.sql.stats.total_rows           | Total rows processed       |
| db.sql.stats.total_logical_reads  | Total logical reads        |
| db.sql.stats.total_logical_writes | Total logical writes       |
| db.sql.stats.total_physical_reads | Total physical reads       |
| db.sql.stats.total_worker_time    | Total CPU time (in ms)     |

The following metrics provide primary statistics for a SQL Server SQL digest query.

| Metric                                      | Unit                       |
| ------------------------------------------- | -------------------------- |
| db.sql_tokenized.stats.execution_count      | Number of execution        |
| db.sql_tokenized.stats.total_elapsed_time   | Total elapsed time (in ms) |
| db.sql_tokenized.stats.total_rows           | Total rows processed       |
| db.sql_tokenized.stats.total_logical_reads  | Total logical reads        |
| db.sql_tokenized.stats.total_logical_writes | Total logical writes       |
| db.sql_tokenized.stats.total_physical_reads | Total physical reads       |
| db.sql_tokenized.stats.total_worker_time    | Total CPU time (in ms)     |
