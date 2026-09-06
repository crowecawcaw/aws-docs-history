

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `delete-grace-period`
<a name="delete-grace-period"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 24 hours | 
| Allowed Values | Duration | 
| Category | Data Lifecycle | 

**Detailed Explanation:**

When data is marked for deletion, this parameter defines the grace period before the deletion is physically applied. During this period, the data remains queryable (soft delete).

**Recommendation:** 15 minutes for dev/test. 1 hour for standard production. 4–24 hours for compliance-sensitive environments.