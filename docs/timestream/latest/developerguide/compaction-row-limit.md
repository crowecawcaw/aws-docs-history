

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `compaction-row-limit`
<a name="compaction-row-limit"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 1,000,000 | 
| Allowed Values | Integer: 1 – 100,000,000 | 
| Category | Compaction | 

**Detailed Explanation:**

Sets the maximum number of rows that a single compaction operation can process. This is a memory safety mechanism — each row being compacted must be held in memory during the merge operation.

**Recommendation:** Keep at 1,000,000 (default) for all instance sizes.