

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `num-datafusion-threads`
<a name="num-datafusion-threads"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | System logical core count (number of vCPUs) | 
| Allowed Values | Integer: 1 – 2,048 | 
| Category | Query Execution | 

**Detailed Explanation:**

Sets the number of worker threads that the DataFusion query engine uses for parallel query execution. Each thread can independently process query partitions, enabling parallelism within a single query as well as across multiple concurrent queries.

**Impact:**
+ **Too low:** Queries execute serially or with minimal parallelism, leading to high query latency. CPU resources remain underutilized.
+ **Too high:** Excessive thread contention, context switching overhead, and potential memory pressure.
+ **Optimal:** **Set to the number of available vCPUs.** If you are using read-only nodes you can assign more than 1 thread per vCPU, but we recommend extensive testing.

**Recommendation:** Set to the number of vCPUs on your instance.