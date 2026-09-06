

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `catalog-sync-interval`
<a name="catalog-sync-interval"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 1 second | 
| Allowed Values | Duration | 
| Category | Catalog Synchronization | 

**Detailed Explanation:**

In Enterprise clusters with multiple nodes, the catalog (metadata about databases, tables, columns, retention policies) must be kept in sync. This parameter controls how frequently each node checks for catalog updates.

**Recommendation:** 1 second (default) for frequent schema changes. 5–10 seconds for stable schemas. 2–5 seconds for high node counts.