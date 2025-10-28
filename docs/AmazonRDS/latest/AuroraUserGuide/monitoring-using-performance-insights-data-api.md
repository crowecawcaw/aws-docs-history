# Monitoring RDS Data API queries with Performance Insights

If your Aurora cluster is running Aurora Serverless v2 or provisioned instances, you can use Performance Insights with RDS Data
API.

For more information about how to use Performance Insights with Aurora, see
[Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").

## How RDS Data API queries are represented in Performance Insights

With Data API, your Aurora cluster processes queries based on Data API calls that you submit from your
application. Data API also performs some SQL statements as part of its own internal workings, such as
canceling queries that exceed the timeout threshold. Both kinds of SQL operations are shown in Performance Insights statistics
and charts.

- For Data API queries that you submit to an Aurora cluster, the **Host** field in the PI
  dashboard is marked as **RDS Data API**. For Aurora PostgreSQL, the
  **application_name** field has the value `rds-data-api`. Look for these labels
  when you analyze database load using **Top hosts** or **Top
  Applications** as a dimension.
- All internal queries that Data API runs to manage database aspects such as the connection pool and query
  timeouts are annotated with a prefix **RDS Data API**. Example: `/* RDS Data API
*/ select * from my_table;` Looks for these prefixes when you analyze database load by
  **Top SQL** as a dimension. statements are annotated with a SQL comment of `/* RDS
Data API */`.
