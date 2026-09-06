

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `parquet-mem-cache-query-path-duration`
<a name="parquet-mem-cache-query-path-duration"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 5 hours | 
| Allowed Values | Duration | 
| Category | Memory Management / Caching | 

**Detailed Explanation:**

Controls how long query access path information is retained for Parquet cache entries. This metadata helps the cache make intelligent eviction decisions.

**Recommendation:** Keep at 5 hours (default). Increase to 10–15 hours for periodic queries on infrequent schedules.