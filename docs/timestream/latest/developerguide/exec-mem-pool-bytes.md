

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `exec-mem-pool-bytes`
<a name="exec-mem-pool-bytes"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 20% of system memory | 
| Allowed Values | Percentage (e.g., 70%) or absolute number (0 – 1,610,612,736,000) | 
| Category | Memory Management | 

**Detailed Explanation:**

Defines the maximum amount of memory that the query execution engine (DataFusion) can use for processing queries. This includes memory for sorting, aggregation, joins, and intermediate result sets.

**Recommendation:** Keep at `20%` (default) for all instance sizes. For query/reader-only nodes, you can increase up to 70%.