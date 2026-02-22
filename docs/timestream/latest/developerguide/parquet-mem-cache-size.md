For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `parquet-mem-cache-size`

Parameter Details| **Default** | `20%` of system memory |
| **Allowed Values** | Percentage (e.g., `20%`) or absolute number (0 – 1,610,612,736,000) |
| **Category** | Memory Management / Caching |

**Detailed Explanation:**

Sets the maximum amount of memory dedicated to caching Parquet file data in memory. This cache stores recently accessed Parquet data blocks, dramatically reducing read latency for repeated queries over the same data. This is one of the most impactful parameters for read/query performance.

**Impact:**

- **Too low:** Frequent cache misses force reads from object storage, significantly increasing query latency (network I/O vs. memory access).
- **Too high:** Leaves insufficient memory for query execution, WAL buffers, and system processes.
- **Optimal:** Typically 15–25% of total instance memory, depending on working set size.
  **Recommendations by Instance Size:**

| Instance Size Recommendations | Instance Type | Memory (GiB)                    | Recommended Value | Approx. GiB                        | Rationale |
| ----------------------------- | ------------- | ------------------------------- | ----------------- | ---------------------------------- | --------- |
| db.influx.medium              | 8             | \*_`15%`_<br>• or 1,073,741,824 | ~1.2              | Minimal cache; memory is scarce    |
| db.influx.large               | 16            | **`20%`**                       | ~3.2              | Default is appropriate             |
| db.influx.xlarge              | 32            | **`20%`**                       | ~6.4              | Meaningful cache size              |
| db.influx.2xlarge             | 64            | **`20%`**                       | ~12.8             | Good working set coverage          |
| db.influx.4xlarge             | 128           | **`25%`**                       | ~32               | Large cache for analytics          |
| db.influx.8xlarge             | 256           | **`25%`**                       | ~64               | Substantial cache                  |
| db.influx.12xlarge            | 384           | **`25%`**                       | ~96               | Very large working set support     |
| db.influx.16xlarge            | 512           | **`25%`**                       | ~128              | Massive cache capacity             |
| db.influx.24xlarge            | 768           | **`25%`**                       | ~192              | Maximum cache for largest instance |
