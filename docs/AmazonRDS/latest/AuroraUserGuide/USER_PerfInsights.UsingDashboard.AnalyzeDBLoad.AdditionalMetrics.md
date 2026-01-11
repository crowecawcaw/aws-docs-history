# SQL statistics for Aurora MySQL

Aurora MySQL collect SQL statistics only at
the digest level. No statistics are shown at the statement level.

###### Topics

- [Digest statistics for Aurora MySQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.truncation "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.truncation")
- [Per-second statistics for Aurora MySQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.per-second "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.per-second")
- [Per-call statistics for
  Aurora MySQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.truncation.per-call "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.truncation.per-call")
- [Primary statistics for Aurora MySQL](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.primary "#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.primary")

## Digest statistics for Aurora MySQL

Performance Insights collects SQL digest statistics from the `events_statements_summary_by_digest` table. The
`events_statements_summary_by_digest` table is managed by your database.

The digest table doesn't have an eviction policy. When the table is full, the AWS Management Console shows the following message:

```
Performance Insights is unable to collect SQL Digest statistics on new queries because the table events_statements_summary_by_digest is full.
Please truncate events_statements_summary_by_digest table to clear the issue. Check the User Guide for more details.
```

In this situation, Aurora MySQL
doesn't track SQL queries. To address this issue, Performance Insights automatically truncates the digest table when both
of the following conditions are met:

- The table is full.
- Performance Insights manages the Performance Schema automatically.

For automatic management, the `performance_schema` parameter must be set to `0` and the
**Source** must not be set to `user`. If Performance Insights isn't managing the Performance
Schema automatically, see [Overview of the Performance Schema for Performance Insights on Aurora MySQL](USER_PerfInsights.md "USER_PerfInsights.md").

In the AWS CLI, check the source of a parameter value by running the [describe-db-parameters](../../../cli/latest/reference/rds/describe-db-parameters.md "../../../cli/latest/reference/rds/describe-db-parameters.md") command.

## Per-second statistics for Aurora MySQL

The following SQL statistics are available for Aurora MySQL DB clusters.

| Metric                                                     | Unit                                     |
| ---------------------------------------------------------- | ---------------------------------------- |
| db.sql_tokenized.stats.count_star_per_sec                  | Calls per second                         |
| db.sql_tokenized.stats.sum_timer_wait_per_sec              | Average latency per second (in ms)       |
| db.sql_tokenized.stats.sum_select_full_join_per_sec        | Select full join per second              |
| db.sql_tokenized.stats.sum_select_range_check_per_sec      | Select range check per second            |
| db.sql_tokenized.stats.sum_select_scan_per_sec             | Select scan per second                   |
| db.sql_tokenized.stats.sum_sort_merge_passes_per_sec       | Sort merge passes per second             |
| db.sql_tokenized.stats.sum_sort_scan_per_sec               | Sort scans per second                    |
| db.sql_tokenized.stats.sum_sort_range_per_sec              | Sort ranges per second                   |
| db.sql_tokenized.stats.sum_sort_rows_per_sec               | Sort rows per second                     |
| db.sql_tokenized.stats.sum_rows_affected_per_sec           | Rows affected per second                 |
| db.sql_tokenized.stats.sum_rows_examined_per_sec           | Rows examined per second                 |
| db.sql_tokenized.stats.sum_rows_sent_per_sec               | Rows sent per second                     |
| db.sql_tokenized.stats.sum_created_tmp_disk_tables_per_sec | Created temporary disk tables per second |
| db.sql_tokenized.stats.sum_created_tmp_tables_per_sec      | Created temporary tables per second      |
| db.sql_tokenized.stats.sum_lock_time_per_sec               | Lock time per second (in ms)             |

## Per-call statistics for

Aurora MySQL

The following metrics provide per call statistics for a SQL statement.

| Metric                                                      | Unit                                   |
| ----------------------------------------------------------- | -------------------------------------- |
| db.sql_tokenized.stats.sum_timer_wait_per_call              | Average latency per call (in ms)       |
| db.sql_tokenized.stats.sum_select_full_join_per_call        | Select full joins per call             |
| db.sql_tokenized.stats.sum_select_range_check_per_call      | Select range check per call            |
| db.sql_tokenized.stats.sum_select_scan_per_call             | Select scans per call                  |
| db.sql_tokenized.stats.sum_sort_merge_passes_per_call       | Sort merge passes per call             |
| db.sql_tokenized.stats.sum_sort_scan_per_call               | Sort scans per call                    |
| db.sql_tokenized.stats.sum_sort_range_per_call              | Sort ranges per call                   |
| db.sql_tokenized.stats.sum_sort_rows_per_call               | Sort rows per call                     |
| db.sql_tokenized.stats.sum_rows_affected_per_call           | Rows affected per call                 |
| db.sql_tokenized.stats.sum_rows_examined_per_call           | Rows examined per call                 |
| db.sql_tokenized.stats.sum_rows_sent_per_call               | Rows sent per call                     |
| db.sql_tokenized.stats.sum_created_tmp_disk_tables_per_call | Created temporary disk tables per call |
| db.sql_tokenized.stats.sum_created_tmp_tables_per_call      | Created temporary tables per call      |
| db.sql_tokenized.stats.sum_lock_time_per_call               | Lock time per call (in ms)             |

## Primary statistics for Aurora MySQL

The following SQL statistics are available for Aurora MySQL DB clusters.

| Metric                                             | Unit                          |
| -------------------------------------------------- | ----------------------------- |
| db.sql_tokenized.stats.count_star                  | Calls                         |
| db.sql_tokenized.stats.sum_timer_wait              | Wait time (in ms)             |
| db.sql_tokenized.stats.sum_select_full_join        | Select full join              |
| db.sql_tokenized.stats.sum_select_range_check      | Select range checks           |
| db.sql_tokenized.stats.sum_select_scan             | Select scans                  |
| db.sql_tokenized.stats.sum_sort_merge_passes       | Sort merge passes             |
| db.sql_tokenized.stats.sum_sort_scan               | Sort scans                    |
| db.sql_tokenized.stats.sum_sort_range              | Sort ranges                   |
| db.sql_tokenized.stats.sum_sort_rows               | Sort rows                     |
| db.sql_tokenized.stats.sum_rows_affected           | Rows affected                 |
| db.sql_tokenized.stats.sum_rows_examined           | Rows examined                 |
| db.sql_tokenized.stats.sum_rows_sent               | Rows sent                     |
| db.sql_tokenized.stats.sum_created_tmp_disk_tables | Created temporary disk tables |
| db.sql_tokenized.stats.sum_created_tmp_tables      | Created temporary tables      |
| db.sql_tokenized.stats.sum_lock_time               | Lock time (in ms)             |
