

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `parquet-mem-cache-size`
<a name="parquet-mem-cache-size"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 20% of system memory | 
| Allowed Values | Percentage (e.g., 20%) or absolute number (0 – 1,610,612,736,000) | 
| Category | Memory Management / Caching | 

**Detailed Explanation:**

Sets the maximum amount of memory dedicated to caching Parquet file data in memory. This cache stores recently accessed Parquet data blocks, dramatically reducing read latency for repeated queries.

**Recommendation:** 15% for db.influx.medium, 20% for db.influx.large through db.influx.2xlarge, 25% for db.influx.4xlarge and above.