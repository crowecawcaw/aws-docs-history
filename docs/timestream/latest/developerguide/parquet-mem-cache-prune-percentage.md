

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `parquet-mem-cache-prune-percentage`
<a name="parquet-mem-cache-prune-percentage"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 0.1 | 
| Allowed Values | Float: 0 – 1 | 
| Category | Memory Management / Caching | 

**Detailed Explanation:**

When the Parquet memory cache is pruned, this parameter controls what percentage of the cache is evicted. A value of 0.1 means 10% of the cache is evicted during each prune cycle.

**Recommendation:** Keep at 0.1 (default) for all instance sizes.