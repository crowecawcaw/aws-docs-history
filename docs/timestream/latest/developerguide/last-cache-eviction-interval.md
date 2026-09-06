

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `last-cache-eviction-interval`
<a name="last-cache-eviction-interval"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 10 seconds | 
| Allowed Values | Duration | 
| Category | Caching | 

**Detailed Explanation:**

The last value cache stores the most recent data point for each unique time series. This parameter controls how frequently stale entries are evicted.

**Recommendation:** Keep at 10 seconds (default). Reduce to 5 seconds if you have high time series churn.