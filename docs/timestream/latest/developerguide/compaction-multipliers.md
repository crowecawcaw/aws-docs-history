

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `compaction-multipliers`
<a name="compaction-multipliers"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 3,4,6,5 | 
| Allowed Values | Four comma-separated integers | 
| Category | Compaction | 

**Note**  
**IMMUTABLE AFTER INITIAL SETUP:** This parameter is persisted in the catalog. Changing it after the cluster's first start affects all higher generation durations and causes silent data divergence. Set this at cluster creation time only. When cloning parameter groups, this value must be copied unchanged.

**Detailed Explanation:**

Defines the size multipliers for each compaction generation level beyond Gen2. With the default `compaction-gen2-duration` of 20 minutes and multipliers of `3,4,6,5`: Gen2 = 20m, Gen3 = 20m × 3 = 1h, Gen4 = 1h × 4 = 4h, Gen5 = 4h × 6 = 24h, Gen6 = 24h × 5 = 5d.

**Recommendation:** Keep at `3,4,6,5` (default) for all instance sizes.