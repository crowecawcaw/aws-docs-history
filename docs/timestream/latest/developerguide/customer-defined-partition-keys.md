For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Customer-defined partition keys

Amazon Timestream for LiveAnalytics customer-defined partition keys is a feature in Timestream for LiveAnalytics that enables customers to
define their own partition keys for their tables. Partitioning is a technique used to
distribute data across multiple physical storage units, allowing for faster and more
efficient data retrieval. With customer-defined partition keys, customers can create a
partitioning schema that better aligns with their query patterns and use cases.

With Timestream for LiveAnalytics customer-defined partition keys, customers can choose one dimension names as a
partition key for their tables. This allows for more flexibility in defining the
partitioning schema for their data. By selecting the right partition key, customers can
optimize their data model, improving their query performance, and reduce query
latency.

###### Topics

- [Using customer-defined partition
  keys](customer-defined-partition-keys-using.md "customer-defined-partition-keys-using.md")
- [Getting started with
  customer-defined partition keys](customer-defined-partition-keys-getting-started.md "customer-defined-partition-keys-getting-started.md")
- [Checking
  partitioning schema configuration](customer-defined-partition-keys-checking-configuration.md "customer-defined-partition-keys-checking-configuration.md")
- [Updating
  partitioning schema configuration](customer-defined-partition-keys-updating-configuration.md "customer-defined-partition-keys-updating-configuration.md")
- [Advantages of
  customer-defined partition keys](customer-defined-partition-keys-advantages.md "customer-defined-partition-keys-advantages.md")
- [Limitations of
  customer-defined partition keys](customer-defined-partition-keys-limitations.md "customer-defined-partition-keys-limitations.md")
- [Customer-defined partition keys and low cardinality dimensions](customer-defined-partition-keys-low-cardinality-dimensions.md "customer-defined-partition-keys-low-cardinality-dimensions.md")
- [Creating partition keys for
  existing tables](customer-defined-partition-keys-creating.md "customer-defined-partition-keys-creating.md")
- [Timestream for LiveAnalytics schema
  validation with custom composite partition keys](customer-defined-partition-keys-schema-validation.md "customer-defined-partition-keys-schema-validation.md")
