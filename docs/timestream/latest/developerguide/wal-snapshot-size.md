For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `wal-snapshot-size`

Parameter Details| **Default** | 600 |
| **Allowed Values** | Integer: 1 – 10,000 |
| **Category** | WAL / Ingestion |

**Detailed Explanation:**

Controls the size threshold (in number of WAL operations) at which a WAL snapshot is triggered, persisting data to Parquet files.

**Recommendation:** 300–600 for db.influx.medium, 600 (default) for db.influx.large, 600–1000 for db.influx.xlarge, 1000–5000 for db.influx.2xlarge and above.
