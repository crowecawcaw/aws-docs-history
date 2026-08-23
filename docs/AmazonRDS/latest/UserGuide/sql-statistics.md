# SQL statistics for Performance Insights

_SQL statistics_ are performance-related metrics about SQL queries. These detailed
per-query metrics are exposed through the Performance Insights API, which gathers statistics for each second that a query
is running and for each SQL call. The SQL statistics are an average for the selected time range.

A SQL digest is a composite of all queries having a given pattern but not necessarily having the same literal values.
The digest replaces literal values with a question mark. For example, `SELECT * FROM emp WHERE lname= ?`.
This digest might consist of the following child queries:

```
SELECT * FROM emp WHERE lname = 'Sanchez'
SELECT * FROM emp WHERE lname = 'Olagappan'
SELECT * FROM emp WHERE lname = 'Wu'
```

All engines support SQL statistics for digest queries.

For the region, DB engine, and instance class support information for this feature, see
[Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md").

###### Topics

- [SQL statistics for MariaDB and MySQL](USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.md "USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.md")
- [SQL statistics for Amazon RDS for Oracle](USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.md "USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.md")
- [SQL statistics for Amazon RDS for SQL Server](USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.md "USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.md")
- [SQL statistics for RDS PostgreSQL](USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.md "USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.md")
