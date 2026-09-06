

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `compaction-check-interval`
<a name="compaction-check-interval"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 10 seconds | 
| Allowed Values | Duration | 
| Category | Compaction | 

**Detailed Explanation:**

Controls how frequently the compactor evaluates whether compaction work is needed.

**Recommendation:** 10 seconds (default) for most instances. Reduce to 5 seconds for db.influx.4xlarge and above with high ingestion rates.