

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `wal-max-write-buffer-size`
<a name="wal-max-write-buffer-size"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 100,000 | 
| Allowed Values | Integer: 1 – 1,000,000 | 
| Category | WAL / Ingestion | 

**Detailed Explanation:**

Sets the maximum number of write operations that can be buffered in the WAL write buffer before being flushed.

**Recommendations by Instance Size:**


**Instance Size Recommendations**  

| Instance Type | Memory (GiB) | Recommended Value | 
| --- | --- | --- | 
| db.influx.medium | 8 | 50,000–100,000 | 
| db.influx.large | 16 | 100,000 | 
| db.influx.xlarge | 32 | 100,000–200,000 | 
| db.influx.2xlarge | 64 | 200,000–300,000 | 
| db.influx.4xlarge | 128 | 300,000–500,000 | 
| db.influx.8xlarge\+ | 256\+ | 500,000–1,000,000 | 