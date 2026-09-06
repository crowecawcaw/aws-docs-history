

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `hard-delete-default-duration`
<a name="hard-delete-default-duration"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 72 hours (3 days) | 
| Allowed Values | Duration | 
| Category | Data Lifecycle | 

**Detailed Explanation:**

After the delete-grace-period expires and data is soft-deleted, this parameter controls how long the physical data remains on storage before being permanently removed (hard deleted).

**Recommendation:** 72 hours (default) for cost-sensitive workloads. 72 hours – 7 days for standard production. 30–90 days for compliance requirements.