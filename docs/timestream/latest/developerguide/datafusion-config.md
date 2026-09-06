

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `datafusion-config`
<a name="datafusion-config"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | (empty) | 
| Allowed Values | Colon-separated key:value pairs (e.g., batch\_size:16384,coalesce\_batches:true) | 
| Category | Query Execution | 

**Detailed Explanation:**

Allows passing additional key-value configuration parameters directly to the DataFusion engine. **Format is comma-separated `key:value` pairs using colons, not equals signs.**

**Recommendation:** Leave empty (default) unless you have specific DataFusion tuning requirements validated through testing.