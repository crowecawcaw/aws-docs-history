

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `compaction-max-num-files-per-plan`
<a name="compaction-max-num-files-per-plan"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 500 | 
| Allowed Values | Integer: 1 – 10,000 | 
| Category | Compaction | 

**Detailed Explanation:**

Limits the maximum number of source files included in a single compaction plan.

**Recommendation:** 500 (default) for db.influx.medium through db.influx.xlarge. 500–1000 for db.influx.2xlarge. 1000–5000 for db.influx.4xlarge through db.influx.8xlarge. 5000–10000 for db.influx.12xlarge and above.