

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `last-value-cache-disable-from-history` *(Enterprise only)*
<a name="last-value-cache-disable-from-history"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | FALSE | 
| Allowed Values | FALSE, TRUE | 
| Category | Caching (Enterprise only) | 

**Detailed Explanation:**

Controls whether the last value cache is populated from historical Parquet files. When FALSE, the system reads historical files during startup to determine the last known value for each time series.

**Recommendation:** FALSE (default) for IoT/monitoring dashboards. TRUE for analytics-only workloads or very large series counts (millions).