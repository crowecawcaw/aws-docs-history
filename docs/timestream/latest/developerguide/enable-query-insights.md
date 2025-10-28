For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Enabling query insights in Amazon Timestream

You can enable query insights for your queries with insights delivered directly through the query response. Enabling query insights doesn't require additional infrastructure or incur any additional costs. When you enable query insights, it returns query performance related metadata fields in addition to query results as part of your query response. You can use this information to tune your queries to improve query performance and reduce query cost.

For information about enabling query insights, see [Run a query](console_timestream.md#console_timestream.queries.using-console "console_timestream.md#console_timestream.queries.using-console").

To view examples of the responses returned by enabling query insights, see [Examples for scheduled queries](API_query_ExecuteScheduledQuery.md#API_query_ExecuteScheduledQuery_Examples "API_query_ExecuteScheduledQuery.md#API_query_ExecuteScheduledQuery_Examples").

###### Note

- When you enable query insights, it rate limits the query to 1 query per second (QPS). To avoid performance impacts, we strongly recommend that you enable query insights only during the evaluation phase of your queries, before deploying them to production.
- The insights provided in query insights are eventually consistent, which means they might change as new data is continuously ingested into the tables.
