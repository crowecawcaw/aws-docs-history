For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using query insights to optimize queries in Amazon Timestream

Query insights is a performance tuning feature that helps you optimize your queries, improve their performance, and reduce costs. With query insights, you can assess the temporal, time-based, and spatial partition key-based pruning efficiency of your queries. Using query insights, you can also identify areas for improvement to enhance query performance. In addition, with query insights, you can evaluate how effectively your queries use time-based and partition key-based indexing to optimize data retrieval. To optimize query performance, it's essential to fine-tune both the temporal and spatial parameters that govern query execution.

###### Topics

- [Benefits of query insights](#query-insights-benefits "#query-insights-benefits")
- [Optimizing data access in Amazon Timestream](query-insights-optimize-data-access-pattern.md "query-insights-optimize-data-access-pattern.md")
- [Enabling query insights in Amazon Timestream](enable-query-insights.md "enable-query-insights.md")
- [Optimizing queries using query insights response](optimize-query-using-query-insights.md "optimize-query-using-query-insights.md")

## Benefits of query insights

The following are the key benefits of using query insights:

- **Identifying inefficient queries** – Query insights provides information on the time-based and attribute-based pruning of the tables accessed by the query. This information helps you identify the tables that are sub-optimally accessed.
- **Optimizing your data model and partitioning** – You can use the query insights information to access and fine-tune your data model and partitioning strategy.
- **Tuning queries** – Query insights highlights opportunities to use indexes more effectively.
