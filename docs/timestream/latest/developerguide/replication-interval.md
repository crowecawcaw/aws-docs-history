

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `replication-interval`
<a name="replication-interval"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 250 ms | 
| Allowed Values | Duration | 
| Category | Replication | 

**Detailed Explanation:**

Controls how frequently data written to one node is replicated to other nodes in the Enterprise cluster. This determines the replication lag.

**Recommendation:** 250ms – 1 second for real-time alerting. 1 second for dashboard monitoring. 5–10 seconds for batch analytics. 5–30 seconds for cost-sensitive bandwidth.