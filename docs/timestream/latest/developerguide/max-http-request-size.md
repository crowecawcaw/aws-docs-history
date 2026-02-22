For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `max-http-request-size`

Parameter Details| **Default** | 10,485,760 (10 MiB) |
| **Allowed Values** | Long: 1,024 – 16,777,216 (1 KiB – 16 MiB) |
| **Category** | Network |

**Detailed Explanation:**

Sets the maximum allowed size for any single incoming HTTP request body. This applies to all HTTP endpoints including write endpoint (Line protocol data batches), query endpoint (SQL/InfluxQL query strings), and API endpoints (Management operations).
