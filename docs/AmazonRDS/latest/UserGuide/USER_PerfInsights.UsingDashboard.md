# Accessing more SQL text in the Performance Insights dashboard

By default, each row in the **Top SQL** table shows 500 bytes of SQL text for each SQL statement.

![500 bytes of SQL](images/perf-insights-top-sql-bytes.png)
When a SQL statement exceeds 500 bytes, you can view more text in the **SQL text** section below the **Top
SQL** table. In this case, the maximum length for the text displayed in **SQL text** is 4 KB. This limit is
introduced by the console and is subject to the limits set by the database engine. To save the text shown in **SQL text**,
choose **Download**.

###### Topics

- [Text size limits for Amazon RDS engines](#sql-text-engine-limits "#sql-text-engine-limits")
- [Setting the SQL text limit for Amazon RDS for PostgreSQL DB
  instances](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
- [Viewing and downloading SQL text in the Performance Insights
  dashboard](view-download-text.md "view-download-text.md")

## Text size limits for Amazon RDS engines

When you download SQL text, the database engine determines its maximum length. You can download SQL text up to the following per-engine
limits.

| DB engine                           | Maximum length of downloaded text                                                                                                                        |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon RDS for MySQL and MariaDB    | The length is fixed at 4,096 bytes when the Performance Schema is enabled. If the Performance Schema isn't enabled, the length is fixed at 65,535 bytes. |
| Amazon RDS for Microsoft SQL Server | 4,096 characters                                                                                                                                         |
| Amazon RDS for Oracle               | 1,000 bytes                                                                                                                                              |

The **SQL text** section of the Performance Insights console displays up to the maximum that the engine returns. For example,
if MySQL returns at most 1 KB to Performance Insights, it can only collect and show 1 KB, even
if the original query is larger. Thus, when you view the query in **SQL text** or download it, Performance Insights
returns the same number of bytes.

If you use the AWS CLI or API, Performance Insights doesn't have the 4 KB limit enforced by the console.
`DescribeDimensionKeys` and `GetResourceMetrics` return at most 500 bytes.

###### Note

`GetDimensionKeyDetails` returns the full query, but the size is subject to the engine limit.
