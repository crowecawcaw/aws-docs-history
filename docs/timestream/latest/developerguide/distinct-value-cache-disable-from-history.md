

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `distinct-value-cache-disable-from-history` *(Enterprise only)*
<a name="distinct-value-cache-disable-from-history"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | FALSE | 
| Allowed Values | FALSE, TRUE | 
| Category | Caching (Enterprise only) | 

**Detailed Explanation:**

Controls whether the distinct value cache is populated from historical Parquet files in addition to real-time data. When FALSE, the system scans historical files for a complete picture of all distinct tag values.

**Recommendation:** FALSE (default) for query-heavy workloads. TRUE for write-heavy workloads or very high tag cardinality (millions).