For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `gen1-duration`

Parameter Details| **Default** | 10 minutes |
| **Allowed Values** | Duration |
| **Category** | Data Lifecycle |
| **Customer Configurable** | No<br>• not accessible to customers at this time |

###### Note

**Not Currently Accessible:** This parameter is not accessible to customers at this time. It is managed by the service with a default value of 10 minutes.

**Detailed Explanation:**

Controls the time span covered by generation 1 (Gen1) Parquet files. When WAL data is snapshotted to persistent storage, the system creates Gen1 files that each cover this time duration. Gen1 is the first tier of persistent storage — data flows from WAL → Gen1 → Gen2 (via compaction) → Gen3+.
