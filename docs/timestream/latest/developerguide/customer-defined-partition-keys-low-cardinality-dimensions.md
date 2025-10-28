For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Customer-defined partition keys and low cardinality dimensions

If you decide to use a partition key with very low cardinality, such as a specific
region or state, it is important to note that the data for for other entities such as
`customerID`, `ProductCategory`, and others, could end up
spread across too many partitions sometimes with little or no data present. This can
lead to inefficient query execution and decreased performance.

To avoid this, we recommend you choose dimensions that are not only part of your key
filtering condition but have higher cardinality. This will help ensure that the data is
evenly distributed across the partitions and improve query performance.
