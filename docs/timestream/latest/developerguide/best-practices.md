For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Best practices

To fully realize the benefits of the Amazon Timestream for LiveAnalytics, follow the best practices described
below.

###### Note

When running proof-of-concept applications, consider the amount of data your
application will accumulate over a few months or years while evaluating the performance
and scale of Timestream for LiveAnalytics. As your data grows over time, you'll notice that the performance of
Timestream for LiveAnalytics remains mostly unchanged because its serverless architecture can leverage massive
amounts of parallelism for processing larger data volumes and automatically scale to
match needs of your application.

###### Topics

- [Data modeling](data-modeling.md "data-modeling.md")
- [Security](security-bp.md "security-bp.md")
- [Configuring Amazon Timestream for LiveAnalytics](configuration.md "configuration.md")
- [Writes](data-ingest.md "data-ingest.md")
- [Queries](queries-bp.md "queries-bp.md")
- [Scheduled queries](scheduledqueries-bp.md "scheduledqueries-bp.md")
- [Client applications and supported
  integrations](client-integrations.md "client-integrations.md")
- [General](general.md "general.md")
