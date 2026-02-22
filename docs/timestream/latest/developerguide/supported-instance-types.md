For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Supported Instance Types and Specifications

The following table lists all supported instance types for Amazon Timestream, along with their hardware specifications. These specifications are critical for determining the optimal parameter group values for your workload.

| Supported Instance Types | Instance Type | vCPUs | Memory (GiB)    | Memory (Bytes)                   | Use Case Profile |
| ------------------------ | ------------- | ----- | --------------- | -------------------------------- | ---------------- |
| **db.influx.medium**     | 1             | 8     | 8,589,934,592   | Dev/test, low-volume workloads   |
| **db.influx.large**      | 2             | 16    | 17,179,869,184  | Light production, small datasets |
| **db.influx.xlarge**     | 4             | 32    | 34,359,738,368  | Small production workloads       |
| **db.influx.2xlarge**    | 8             | 64    | 68,719,476,736  | Medium production workloads      |
| **db.influx.4xlarge**    | 16            | 128   | 137,438,953,472 | Large production workloads       |
| **db.influx.8xlarge**    | 32            | 256   | 274,877,906,944 | High-throughput production       |
| **db.influx.12xlarge**   | 48            | 384   | 412,316,860,416 | Heavy analytics workloads        |
| **db.influx.16xlarge**   | 64            | 512   | 549,755,813,888 | Maximum r7g capacity             |
| **db.influx.24xlarge**   | 96            | 768   | 824,633,720,832 | Extreme-scale workloads          |
