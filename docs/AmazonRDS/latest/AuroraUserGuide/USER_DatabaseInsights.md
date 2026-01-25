# Configuring your database to monitor slow SQL queries with Database Insights for Amazon Aurora

To monitor slow SQL queries for your database, you can use the **Slow SQL Queries** section in the Database Insights dashboard. Before configuring your database to monitor slow SQL queries, the **Slow SQL Queries** section is blank.

For more information about monitoring slow SQL queries in the Database Insights dashboard, see [Viewing the Database Instance Dashboard for CloudWatch Database Insights](../../../AmazonCloudWatch/latest/monitoring/Database-Insights-Database-Instance-Dashboard.md "../../../AmazonCloudWatch/latest/monitoring/Database-Insights-Database-Instance-Dashboard.md") in the _Amazon CloudWatch User Guide_.

To configure your database to monitor slow SQL queries with Database Insights, complete the following steps:

1. Enable log exports to CloudWatch Logs.
2. Create or modify the DB cluster parameter group for your DB cluster.
   For information about configuring log exports, see [Publishing database logs to Amazon CloudWatch Logs](USER_LogAccess.md#USER_LogAccess.Procedural.UploadtoCloudWatch "USER_LogAccess.md#USER_LogAccess.Procedural.UploadtoCloudWatch") in the _Amazon Aurora User Guide_.

To create or modify your DB cluster parameter group, see the following topics.

- [Creating a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Modifying parameters in a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")

Amazon Aurora MySQL
To configure your Amazon Aurora MySQL DB cluster to monitor slow SQL queries, you can use the following parameter combination as an example:

- `slow_query_log` – set to `1`
- `long_query_time` – set to `1.0`
- `log_output` – set to `FILE`

This is one possible configuration. For a comprehensive guide to MySQL slow query log parameters and additional configuration options, see the [MySQL documentation for the slow query log](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html "https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html").

Amazon Aurora PostgreSQL
To configure your Amazon Aurora PostgreSQL DB cluster to monitor slow SQL queries, you can use the following parameter combination as an example. Note that setting these parameters might reduce the performance of your DB cluster.

- `log_min_duration_statement` – set to `1000`
- `log_statement` – set to `none`
- `log_destination` – set to `stderr`

This is one possible configuration. For a comprehensive guide to PostgreSQL logging parameters and additional configuration options, see the [PostgreSQL documentation for logging configuration](https://www.postgresql.org/docs/current/runtime-config-logging.html "https://www.postgresql.org/docs/current/runtime-config-logging.html").

###### Note

For Aurora MySQL, you can configure the parameter `long_query_time` with 1‐microsecond granularity. For example, you can set this parameter to `0.000001`. Depending on the amount of queries on the DB instance, the value of the parameter `long_query_time` can reduce performance. Start with the value `1.0`, and adjust it based on your workload. When you set this parameter to `0`, Database Insights logs all queries.

For information about Aurora MySQL and Aurora PostgreSQL logs, see the following.

- [Aurora MySQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md")
- [Aurora PostgreSQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md")
