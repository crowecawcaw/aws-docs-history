

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `disable-parquet-mem-cache`
<a name="disable-parquet-mem-cache"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | FALSE | 
| Allowed Values | FALSE, TRUE | 
| Category | Memory Management / Caching | 

**Detailed Explanation:**

When set to TRUE, completely disables the Parquet memory cache. All Parquet data reads go directly to object storage.

**Recommendation:** Keep as FALSE (default). Only set to TRUE for dedicated write-only ingestion nodes.