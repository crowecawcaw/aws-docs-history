

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `force-snapshot-mem-threshold`
<a name="force-snapshot-mem-threshold"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 50% | 
| Allowed Values | Percentage (e.g., 70%) or absolute number (0 – 1,610,612,736,000) | 
| Category | Memory Management | 

**Detailed Explanation:**

Defines the memory usage threshold at which the system forces a WAL snapshot to disk. When memory usage exceeds this threshold, in-memory WAL data is persisted to Parquet files, freeing memory.

**Recommendation:** 30% for all instance sizes.