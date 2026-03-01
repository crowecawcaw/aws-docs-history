For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `datafusion-use-cached-parquet-loader`

Parameter Details| **Default** | TRUE |
| **Allowed Values** | FALSE, TRUE |
| **Category** | Query Execution |

**Detailed Explanation:**

When enabled, DataFusion uses a cached Parquet loader that keeps parsed Parquet file metadata and footer information in memory, avoiding re-parsing on subsequent reads.

**Recommendation:** Keep as TRUE (default) for all instance sizes. Set to FALSE only if memory is extremely constrained.
