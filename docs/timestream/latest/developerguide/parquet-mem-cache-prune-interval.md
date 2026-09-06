

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `parquet-mem-cache-prune-interval`
<a name="parquet-mem-cache-prune-interval"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 1 second | 
| Allowed Values | Duration | 
| Category | Memory Management / Caching | 

**Detailed Explanation:**

Controls how frequently the system checks whether the Parquet memory cache has exceeded its size limit and needs pruning.

**Recommendation:** Keep at 1 second (default) for all instance sizes.