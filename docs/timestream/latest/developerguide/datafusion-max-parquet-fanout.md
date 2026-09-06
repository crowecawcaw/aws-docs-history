

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `datafusion-max-parquet-fanout`
<a name="datafusion-max-parquet-fanout"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 1000 | 
| Allowed Values | Integer: 1 – 1,000,000 | 
| Category | Query Execution | 

**Detailed Explanation:**

Controls the maximum number of Parquet files that can be read in parallel during a single query operation. A high fanout value does not mean all files are read simultaneously — the thread pool still controls actual parallelism. The fanout value controls how the query plan is structured.

**Recommendations by Instance Size:**


**Instance Size Recommendations**  

| Instance Type | vCPUs | Memory (GiB) | Recommended Value | 
| --- | --- | --- | --- | 
| db.influx.medium | 1 | 8 | 250–500 | 
| db.influx.large | 2 | 16 | 500 | 
| db.influx.xlarge | 4 | 32 | 500–1000 | 
| db.influx.2xlarge | 8 | 64 | 1000 | 
| db.influx.4xlarge | 16 | 128 | 1000–2000 | 
| db.influx.8xlarge | 32 | 256 | 2000–5000 | 
| db.influx.12xlarge\+ | 48\+ | 384\+ | 5000–10000 | 