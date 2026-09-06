

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `preemptive-cache-age`
<a name="preemptive-cache-age"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 3 days | 
| Allowed Values | Duration | 
| Category | Memory Management / Caching | 

**Detailed Explanation:**

Controls the age threshold for preemptive cache warming after compaction. When new compacted files newer than this age are created, they are preemptively loaded into the Parquet memory cache.

**Recommendation:** Keep at 3 days (default). Reduce if cache memory pressure is an issue; increase if queries frequently access data older than 3 days.