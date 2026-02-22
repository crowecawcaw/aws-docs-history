For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `catalog-sync-interval`

Parameter Details| **Default** | 1 second |
| **Allowed Values** | Duration |
| **Category** | Catalog Synchronization (Enterprise only) |

**Detailed Explanation:**

In Enterprise clusters with multiple nodes, the catalog (metadata about databases, tables, columns, retention policies, and schema definitions) must be kept in sync across all nodes. This parameter controls how frequently each node checks for catalog updates from the central catalog store.
