For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using customer-defined partition

keys

If you have a well-defined query pattern with high cardinality dimensions and require
low query latency, a Timestream for LiveAnalytics customer-defined partition key can be a useful tool to enhance
your data model. For instance, if you are a retail company tracking customer
interactions on your website, the main access patterns would likely be by customer ID
and timestamp. By defining customer ID as the partition key, your data can be
distributed evenly, allowing for reduced latency, ultimately improving the user
experience.

Another example is in the healthcare industry, where wearable devices collect sensor
data to track patients' vital signs. The main access pattern would be by Device ID and
timestamp, with high cardinality on both dimensions. By defining Device ID as the
partition key, can optimize your query execution and ensure a sustained long term query
performance.

In summary, Timestream for LiveAnalytics customer-defined partition keys are most useful when you have a clear
query pattern, high cardinality dimensions, and need low latency for your queries. By
defining a partition key that aligns with your query pattern, you can optimize your
query execution and ensure a sustained long term performance query performance.
