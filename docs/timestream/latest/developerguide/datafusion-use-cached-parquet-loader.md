

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `datafusion-use-cached-parquet-loader`
<a name="datafusion-use-cached-parquet-loader"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | TRUE | 
| Allowed Values | FALSE, TRUE | 
| Category | Query Execution | 

**Detailed Explanation:**

When enabled, DataFusion uses a cached Parquet loader that keeps parsed Parquet file metadata and footer information in memory, avoiding re-parsing on subsequent reads.

**Recommendation:** Keep as TRUE (default) for all instance sizes. Set to FALSE only if memory is extremely constrained.