For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `retention-check-interval`

Parameter Details| **Default** | 30 minutes |
| **Allowed Values** | Duration |
| **Category** | Data Lifecycle |

**Detailed Explanation:**

Controls how frequently the system evaluates and enforces retention policies.

**Recommendation:** 10–15 minutes for strict retention compliance. 30 minutes (default) for standard production. 1–6 hours for relaxed retention.
