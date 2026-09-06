

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Schema design FAQ for Amazon Timestream for InfluxDB 3
<a name="faq-schema-design"></a>

Questions about designing schemas for Amazon Timestream for InfluxDB 3, including tags, fields, and best practices for performance. For detailed guidance, see [Schema design recommendations for Timestream for InfluxDB 3](influxdb-schema-design-recommendations.md).

**What is the difference between tags and fields?**  
Tags are indexed metadata used for grouping and filtering. Fields contain the actual measured values. Tags are part of the primary key and are stored as strings. Fields support multiple data types (float, integer, string, boolean) and are not indexed. Use tags for values you frequently filter or group by, and fields for measured data.

**How does InfluxDB 3 handle high-cardinality data?**  
InfluxDB 3's columnar Parquet storage and Apache Arrow processing are specifically designed for high-cardinality workloads. Unlike previous versions, InfluxDB 3 does not suffer from performance degradation with high-cardinality tag values because it uses a fundamentally different storage architecture.

**What are the schema design best practices?**  
Key recommendations include: keep tag cardinality manageable, use meaningful measurement names, avoid encoding data in measurement names, use consistent tag naming conventions, and design your schema around your most common query patterns. See [Schema design recommendations for Timestream for InfluxDB 3](influxdb-schema-design-recommendations.md) for detailed guidance, and the [InfluxDB 3 schema design best practices](https://docs.influxdata.com/influxdb3/enterprise/write-data/best-practices/schema-design/) for additional recommendations.