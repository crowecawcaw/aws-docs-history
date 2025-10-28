For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Queries

Following are suggested best practices for queries with Amazon Timestream for LiveAnalytics.

- Include only the measure and dimension names essential to query. Adding
  extraneous columns will increase data scans, which impacts the performance of
  queries.
- Before deploying your query in production, we recommend that you review query insights to make sure that the spatial and temporal pruning is optimal. For more information, see [Using query insights to optimize queries in Amazon Timestream](using-query-insights.md "using-query-insights.md").
- Where possible, push the data computation to Timestream for LiveAnalytics using the built-in aggregates
  and scalar functions in the SELECT clause and WHERE clause as applicable to
  improve query performance and reduce cost. See [SELECT](supported-sql-constructs.md "supported-sql-constructs.md") and [Aggregate functions](aggregate-functions.md "aggregate-functions.md").
- Where possible, use approximate functions. E.g., use APPROX_DISTINCT instead
  of COUNT(DISTINCT column_name) to optimize query performance and reduce the
  query cost. See [Aggregate functions](aggregate-functions.md "aggregate-functions.md").
- Use a CASE expression to perform complex aggregations instead of selecting
  from the same table multiple times. See [The CASE statement](conditional-expressions.md "conditional-expressions.md").
- Where possible, include a time range in the WHERE clause of your query. This
  optimizes query performance and costs. For example, if you only need the last
  one hour of data in your dataset, then include a time predicate such as time
  > ago(1h). See [SELECT](supported-sql-constructs.md "supported-sql-constructs.md") and [Interval and duration](date-time-functions.md#date-time-functions-interval-duration "date-time-functions.md#date-time-functions-interval-duration").
- When a query accesses a subset of measures in a table, always include the
  measure names in the WHERE clause of the query.
- Where possible, use the equality operator when comparing dimensions and
  measures in the WHERE clause of a query. An equality predicate on dimensions and
  measure names allows for improved query performance and reduced query
  costs.
- Wherever possible, avoid using functions in the WHERE clause to optimize for
  cost.
- Refrain from using LIKE clause multiple times. Rather, use regular expressions
  when you are filtering for multiple values on a string column. See [Regular expression functions](regex-functions.md "regex-functions.md").
- Only use the necessary columns in the GROUP BY clause of a query.
- If the query result needs to be in a specific order, explicitly specify that
  order in the ORDER BY clause of the outermost query. If your query result does
  not require ordering, avoid using an ORDER BY clause to improve query
  performance.
- Use a LIMIT clause if you only need the first N rows in your query.
- If you are using an ORDER BY clause to look at the top or bottom N values, use
  a LIMIT clause to reduce the query costs.
- Use the pagination token from the returned response to retrieve the query
  results. For more information, see [Query](API_query_Query.md "API_query_Query.md").
- If you've started running a query and realize that the query will not return
  the results you're looking for, cancel the query to save cost. For more
  information, see [CancelQuery](API_query_CancelQuery.md "API_query_CancelQuery.md").
- If your application experiences throttling, continue sending data to Amazon Timestream for LiveAnalytics
  at the same rate to enable Amazon Timestream for LiveAnalytics to auto-scale to the satisfy the query
  throughput needs of your application.
- If the query concurrency requirements of your applications exceed the default
  limits of Timestream for LiveAnalytics, contact Support for limit increases.
