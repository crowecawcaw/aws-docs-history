For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `exec-mem-pool-bytes`

Parameter Details| **Default** | `20%` of system memory |
| **Allowed Values** | Percentage (e.g., `70%`) or absolute number (0 – 1,610,612,736,000) |
| **Category** | Memory Management |

**Detailed Explanation:**

Defines the maximum amount of memory that the query execution engine (DataFusion) can use for processing queries. This includes memory for sorting, aggregation, joins, and intermediate result sets. This is one of the most critical memory parameters. When specified as a percentage, it is calculated against the total instance memory.

**Impact:**

- **Too low:** Queries that require significant memory (large aggregations, sorts, joins) will fail or spill to disk, dramatically increasing latency. Concurrent queries compete for a small pool.
- **Too high:** Leaves insufficient memory for the Parquet cache, WAL buffers, OS page cache, and system processes, potentially causing OOM kills.
- **Optimal:** `20%` of total instance memory (the code default). If you are running query/reader-only nodes, you can set this up to 70%.
  **Recommendation:** Keep at `20%` (default) for all instance sizes.
