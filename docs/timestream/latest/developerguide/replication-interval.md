For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `replication-interval`

Parameter Details| **Default** | 250 ms |
| **Allowed Values** | Duration |
| **Category** | Replication (Enterprise only) |

**Detailed Explanation:**

Controls how frequently data written to one node is replicated to other nodes in the Enterprise cluster. This determines the **replication lag** — the maximum delay between data being ingested on the primary node and being available for queries on replica nodes.
