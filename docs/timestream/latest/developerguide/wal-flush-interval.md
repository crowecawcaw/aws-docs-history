For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `wal-flush-interval`

Parameter Details| **Default** | 100ms |
| **Allowed Values** | Fixed at 100ms |
| **Category** | WAL / Ingestion |
| **Customer Configurable** | No<br>• fixed by the service |

**Detailed Explanation:**

Controls how frequently the WAL flushes buffered write data to durable storage. The WAL accumulates incoming writes in memory and periodically flushes them to ensure durability. This parameter is set to 100ms and cannot be changed by customers.
