For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `num-datafusion-threads`

Parameter Details| **Default** | System logical core count (number of vCPUs) |
| **Allowed Values** | Integer: 1 – 2,048 |
| **Category** | Query Execution |

**Detailed Explanation:**

This parameter sets the number of worker threads that the DataFusion query engine uses for parallel query execution. Each thread can independently process query partitions, enabling parallelism within a single query as well as across multiple concurrent queries. This is one of the most impactful parameters for query performance.

**Impact:**

- **Too low:** Queries execute serially or with minimal parallelism, leading to high query latency, especially for analytical queries that scan large datasets. CPU resources remain underutilized.
- **Too high:** Excessive thread contention, context switching overhead, and potential memory pressure. Threads competing for CPU time can actually degrade performance. Also reduces resources available for ingestion and WAL operations.
- **Optimal:** **Set to the number of available vCPUs.** If you are using read-only nodes you can assign more than 1 thread per vCPU, but we recommend extensive testing based on real world query profiles and load.
  **Recommendations by Instance Size:**

| Instance Size Recommendations | Instance Type | vCPUs  | Recommended Value                     | Rationale |
| ----------------------------- | ------------- | ------ | ------------------------------------- | --------- |
| db.influx.medium              | 1             | **1**  | Single vCPU — no parallelism possible |
| db.influx.large               | 2             | **2**  | Use both vCPUs                        |
| db.influx.xlarge              | 4             | **4**  | Match vCPU count                      |
| db.influx.2xlarge             | 8             | **8**  | Match vCPU count                      |
| db.influx.4xlarge             | 16            | **16** | Match vCPU count                      |
| db.influx.8xlarge             | 32            | **32** | Match vCPU count                      |
| db.influx.12xlarge            | 48            | **48** | Match vCPU count                      |
| db.influx.16xlarge            | 64            | **64** | Match vCPU count                      |
| db.influx.24xlarge            | 96            | **96** | Match vCPU count                      |
