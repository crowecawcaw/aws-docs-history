

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `table-index-cache-max-entries`
<a name="table-index-cache-max-entries"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 1000 | 
| Allowed Values | Integer: 0\+ (0 disables the limit) | 
| Category | Table Index Cache | 

**Detailed Explanation:**

Sets the maximum number of table index entries that can be held in the cache. Each entry corresponds to one table's index structure. If your database has more tables than this limit, the least-recently-used table indexes are evicted.

**Recommendation:** Keep at 1000 (default). If your database has more than 1000 tables, increase to match your table count.