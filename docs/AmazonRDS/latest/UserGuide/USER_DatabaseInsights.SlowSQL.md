

# Configuring your database to monitor slow SQL queries with Database Insights for Amazon RDS
<a name="USER_DatabaseInsights.SlowSQL"></a>

To monitor slow SQL queries for your database, you can use the **Slow SQL Queries** section in the Database Insights dashboard. Before configuring your database to monitor slow SQL queries, the **Slow SQL Queries** section is blank.

For more information about monitoring slow SQL queries in the Database Insights dashboard, see [Viewing the Database Instance Dashboard for CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Database-Instance-Dashboard.html) in the *Amazon CloudWatch User Guide*.

To configure your database to monitor slow SQL queries with Database Insights, complete the following steps:

1. Enable log exports to CloudWatch Logs.

1. Create or modify the DB parameter group for your DB instance.

For information about configuring log exports, see [Publishing database logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.

To create or modify your DB parameter group, see the following topics.
+ [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Creating.md)
+ [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md)

------
#### [ RDS for MariaDB ]

To configure your RDS for MariaDB DB instance to monitor slow SQL queries, you can use the following parameter combination as an example:
+ `log_slow_query` – set to `1`
+ `log_slow_query_time` – set to `1.0`
+ `log_output` – set to `FILE`

This is one possible configuration. For a comprehensive guide to MariaDB slow query log parameters and additional configuration options, see the [MariaDB documentation for the slow query log](https://mariadb.com/kb/en/slow-query-log-overview/).

------
#### [ RDS for MySQL ]

To configure your RDS for MySQL DB instance to monitor slow SQL queries, you can use the following parameter combination as an example:
+ `slow_query_log` – set to `1`
+ `long_query_time` – set to `1.0`
+ `log_output` – set to `FILE`

This is one possible configuration. For a comprehensive guide to MySQL slow query log parameters and additional configuration options, see the [MySQL documentation for the slow query log](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html).

------
#### [ RDS for PostgreSQL ]

To configure your RDS for PostgreSQL DB instance to monitor slow SQL queries, you can use the following parameter combination as an example. Note that setting these parameters might reduce the performance of your DB instance.
+ `log_min_duration_statement` – set to `1000`
+ `log_statement` – set to `none`
+ `log_destination` – set to `stderr`

This is one possible configuration. For a comprehensive guide to PostgreSQL logging parameters and additional configuration options, see the [PostgreSQL documentation for logging configuration](https://www.postgresql.org/docs/current/runtime-config-logging.html).

------

**Note**  
For RDS for MySQL, you can configure the parameter `long_query_time` with 1‐microsecond granularity. For example, you can set this parameter to `0.000001`. Depending on the amount of queries on the DB instance, the value of the parameter `long_query_time` can reduce performance. Start with the value `1.0`, and adjust it based on your workload. When you set this parameter to `0`, Database Insights logs all queries.

For information about RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL logs, see the following.
+ [MariaDB database log files](USER_LogAccess.Concepts.MariaDB.md)
+ [MySQL database log files](USER_LogAccess.Concepts.MySQL.md)
+ [ RDS for PostgreSQL database log files](USER_LogAccess.Concepts.PostgreSQL.md)