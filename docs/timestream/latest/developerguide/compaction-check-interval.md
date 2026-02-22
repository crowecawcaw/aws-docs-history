For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `compaction-check-interval`

Parameter Details| **Default** | 10 seconds |
| **Allowed Values** | Duration |
| **Category** | Compaction (Enterprise only) |

**Detailed Explanation:**

Controls how frequently the compactor evaluates whether compaction work is needed. During each check, the compactor examines file counts, sizes, and generation levels across all tables and databases to build compaction plans. If no compaction is needed, the check completes quickly with minimal overhead.

**Impact:**

- **Shorter intervals (5–10 seconds):** The compactor responds faster to accumulating small files, keeping the total file count lower. This benefits query performance (fewer files to scan) but adds overhead from more frequent evaluation cycles. Best for high-ingestion workloads that generate many small files rapidly.
- **Longer intervals (30–300 seconds):** Less evaluation overhead, but files accumulate between checks. Queries may temporarily slow down as they scan more small files before compaction catches up. Best for low-ingestion workloads or batch ingestion patterns.
