For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `max-http-request-size`

Parameter Details| **Default** | 10,485,760 (10 MiB) |
| **Allowed Values** | Long: 1,024 – 16,777,216 (1 KiB – 16 MiB) |
| **Category** | Network |

**Detailed Explanation:**

Sets the maximum allowed size for any single incoming HTTP request body. Applies to write, query, and API endpoints. Requests exceeding this size are rejected with HTTP 413.

**Recommendation:** 5 MiB for db.influx.medium. 10 MiB (default) for db.influx.large through db.influx.xlarge. 10–16 MiB for db.influx.2xlarge and above if clients send large batches.
