For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# `datafusion-max-parquet-fanout`

Parameter Details| **Default** | 1000 |
| **Allowed Values** | Integer: 1 – 1,000,000 |
| **Category** | Query Execution |

**Detailed Explanation:**

Controls the maximum number of Parquet files that can be read in parallel during a single query operation. When a query needs to scan data across multiple Parquet files, this parameter limits how many files are opened and read simultaneously.

**Impact:**

- **Lower values:** Fewer files read in parallel, reducing memory pressure and I/O contention but increasing query latency for queries spanning many files.
- **Higher values:** More files read in parallel, improving query throughput for wide-spanning queries but increasing memory consumption and I/O load.
  **Recommendations by Instance Size:**

| Instance Size Recommendations | Instance Type | vCPUs | Memory (GiB)   | Recommended Value                    | Rationale |
| ----------------------------- | ------------- | ----- | -------------- | ------------------------------------ | --------- |
| db.influx.medium              | 1             | 8     | **250–500**    | Limited resources; keep conservative |
| db.influx.large               | 2             | 16    | **500**        | Moderate parallelism                 |
| db.influx.xlarge              | 4             | 32    | **500–1000**   | Can handle moderate parallelism      |
| db.influx.2xlarge             | 8             | 64    | **1000**       | Default is appropriate               |
| db.influx.4xlarge             | 16            | 128   | **1000–2000**  | Strong parallel read capacity        |
| db.influx.8xlarge             | 32            | 256   | **2000–5000**  | High parallel I/O capacity           |
| db.influx.12xlarge            | 48            | 384   | **5000–10000** | Very high capacity                   |
| db.influx.16xlarge            | 64            | 512   | **5000–10000** | Near-maximum parallelism             |
| db.influx.24xlarge            | 96            | 768   | **5000–10000** | Maximum parallel read capacity       |
