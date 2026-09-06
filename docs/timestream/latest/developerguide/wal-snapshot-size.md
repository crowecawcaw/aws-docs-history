

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `wal-snapshot-size`
<a name="wal-snapshot-size"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 600 | 
| Allowed Values | Integer: 1 – 10,000 | 
| Category | WAL / Ingestion | 

**Detailed Explanation:**

Controls the size threshold (in number of WAL operations) at which a WAL snapshot is triggered, persisting data to Parquet files.

**Recommendation:** 300 for all instance sizes.