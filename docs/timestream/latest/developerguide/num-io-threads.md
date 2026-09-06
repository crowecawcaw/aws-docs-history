

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `num-io-threads`
<a name="num-io-threads"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | System logical core count (number of vCPUs) | 
| Allowed Values | Integer: 1 – 2,048 | 
| Category | Query Execution / I/O | 

**Detailed Explanation:**

Sets the number of threads in the I/O runtime, which handles network I/O, object store operations, and other async I/O tasks. This is separate from the DataFusion query threads.

**Recommendation:** Set to the number of vCPUs on your instance.