For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `wal-max-write-buffer-size`

Parameter Details| **Default** | 100,000 |
| **Allowed Values** | Integer: 1 – 1,000,000 |
| **Category** | WAL / Ingestion |

**Detailed Explanation:**

Sets the maximum number of write operations that can be buffered in the WAL write buffer before being flushed. This buffer accumulates incoming writes and flushes them in batches for efficiency.

**Impact:**

- **Lower values:** More frequent WAL flushes, lower risk of data loss on failure, but higher I/O overhead and reduced write throughput.
- **Higher values:** Larger batches are flushed less frequently, improving write throughput but increasing the amount of data at risk during a failure and consuming more memory.
