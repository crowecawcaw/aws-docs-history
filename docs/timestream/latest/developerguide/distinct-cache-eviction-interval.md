For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `distinct-cache-eviction-interval`

Parameter Details| **Default** | 10 seconds |
| **Allowed Values** | Duration |
| **Category** | Caching |

**Detailed Explanation:**

The distinct value cache stores the set of unique values for tag columns (e.g., all unique `host` names, all unique `region` values). This dramatically accelerates queries that use `SHOW TAG VALUES`, `DISTINCT`, or `GROUP BY` on tag columns. This parameter controls how frequently the cache is checked for stale entries that should be evicted.
