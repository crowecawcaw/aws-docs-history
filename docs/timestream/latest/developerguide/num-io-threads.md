For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `num-io-threads`

Parameter Details| **Default** | System logical core count (number of vCPUs) |
| **Allowed Values** | Set automatically to match vCPU count on writer nodes |
| **Category** | Query Execution / I/O |
| **Customer Configurable** | No<br>• automatically set by the service |

**Detailed Explanation:**

This parameter sets the number of threads in the I/O runtime, which handles network I/O, object store operations, and other async I/O tasks. This is separate from the DataFusion query threads. On writer nodes, this value is automatically set to match the number of vCPUs and cannot be changed by customers.
