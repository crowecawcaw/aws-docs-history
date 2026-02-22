For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `compaction-gen2-duration`

Parameter Details| **Default** | 20 minutes |
| **Allowed Values** | Duration |
| **Category** | Compaction (Enterprise only) |
| **Customer Configurable** | No<br>• not accessible to customers at this time |

###### Note

**Not Currently Accessible:** This parameter is not accessible to customers at this time. It is managed by the service with a default value of 20 minutes.

**Detailed Explanation:**

Defines the time span that each generation 2 (Gen2) compacted file should cover. InfluxDB 3 uses a tiered compaction strategy:

- **Gen0:** Raw WAL snapshots (very small, covering seconds to minutes)
- **Gen1:** First-level compaction (controlled by `gen1-duration`, default 10 minutes)
- **Gen2:** Second-level compaction (controlled by this parameter, default 20 minutes)
- **Gen3+:** Higher-level compaction (controlled by `compaction-multipliers`)
