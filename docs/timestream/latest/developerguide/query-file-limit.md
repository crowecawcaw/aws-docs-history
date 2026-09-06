

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `query-file-limit`
<a name="query-file-limit"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 432 | 
| Allowed Values | Integer: 0 – 1,024 | 
| Category | Query Execution | 

**Detailed Explanation:**

Sets the maximum number of Parquet files that can be included in a single query's execution plan. If a query would need to scan more files than this limit, it is rejected. A value of 0 disables the limit.

**Recommendations by Instance Size:**


**Instance Size Recommendations**  

| Instance Type | Memory (GiB) | Recommended Value | 
| --- | --- | --- | 
| db.influx.medium | 8 | 100–200 | 
| db.influx.large | 16 | 200–300 | 
| db.influx.xlarge | 32 | 300–432 | 
| db.influx.2xlarge | 64 | 432 | 
| db.influx.4xlarge | 128 | 432–600 | 
| db.influx.8xlarge\+ | 256\+ | 600–1024 | 