For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Queries

Queries are charged based on the duration of [Timestream compute units (TCUs)](tcu.md "tcu.md") used by your application in TCU-hours as specified on the [Amazon Timestream pricing](https://aws.amazon.com/timestream/pricing/ "https://aws.amazon.com/timestream/pricing/") page. Amazon Timestream for LiveAnalytics' query engine prunes irrelevant data while processing a query. Queries with projections and predicates including time ranges, measure names, and/or dimension names enable the query processing engine to prune a significant amount of data and help with lowering query costs.
