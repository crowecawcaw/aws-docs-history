For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Limitations of

customer-defined partition keys

As a Timestream for LiveAnalytics user, it's important to keep in mind the limitations around a customer
partition key. Firstly, it requires a good understanding of your workload and query
patterns. This means that you should have a clear idea of which dimensions are most
frequently use as main filtering conditions in queries and have high cardinality to make
the most effective use of partition keys.

Secondly, partition keys need to be defined at the time of table creation and cannot
be added to existing tables. This means that you should carefully consider your
partitioning strategy before creating a table to ensure that it aligns with your
business needs.

Lastly, it's important to note that once the table has been created, you cannot change
the partition key afterwards. This means that you should thoroughly test and evaluate
your partitioning strategy before committing to it. With these limitations in mind,
Timestream's customer-defined partition key can greatly improve query performance and
long term satisfaction.
