

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `table-index-cache-concurrency-limit`
<a name="table-index-cache-concurrency-limit"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 20 | 
| Allowed Values | Integer: 1 – 100 | 
| Category | Table Index Cache | 

**Detailed Explanation:**

Limits the number of concurrent operations that can access the table index cache simultaneously. Acts as a concurrency semaphore to prevent cache contention under high query load.

**Recommendations by Instance Size:**


**Instance Size Recommendations**  

| Instance Type | vCPUs | Recommended Value | 
| --- | --- | --- | 
| db.influx.medium | 1 | 8–16 | 
| db.influx.large | 2 | 16–20 | 
| db.influx.xlarge | 4 | 20 | 
| db.influx.2xlarge | 8 | 20–24 | 
| db.influx.4xlarge | 16 | 24–32 | 
| db.influx.8xlarge | 32 | 32–48 | 
| db.influx.12xlarge\+ | 48\+ | 48–100 | 