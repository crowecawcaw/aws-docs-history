For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `datafusion-config`

Parameter Details| **Default** | _(empty)_ |
| **Allowed Values** | Colon-separated key:value pairs (e.g., `batch_size:16384,coalesce_batches:true`) |
| **Category** | Query Execution |

**Detailed Explanation:**

Allows passing additional key-value configuration parameters directly to the DataFusion engine. **Format is comma-separated `key:value` pairs using colons, not equals signs.**

**Recommendation:** Leave empty (default) unless you have specific DataFusion tuning requirements validated through testing.
