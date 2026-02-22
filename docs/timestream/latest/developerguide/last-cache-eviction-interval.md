For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `last-cache-eviction-interval`

Parameter Details| **Default** | 10 seconds |
| **Allowed Values** | Duration |
| **Category** | Caching |

**Detailed Explanation:**

The last value cache stores the most recent data point for each unique time series (combination of measurement + tag set). This is extremely valuable for IoT and monitoring use cases where dashboards frequently display "current value" for thousands of sensors/hosts. This parameter controls how frequently stale entries are evicted from this cache.
