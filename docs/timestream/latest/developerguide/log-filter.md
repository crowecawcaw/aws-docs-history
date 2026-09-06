

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `log-filter`
<a name="log-filter"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | (empty) | 
| Allowed Values | String, max 1,024 characters | 
| Category | Logging | 

**Detailed Explanation:**

Configures log filtering using the Rust `tracing` subscriber filter syntax. Examples: `info`, `warn`, `influxdb3_write=debug`, `influxdb3_write=debug,influxdb3_server=info`.

**Recommendation:** Leave empty (default) for production. Use component-specific filters (e.g., `influxdb3_write=debug`) for targeted troubleshooting. Never leave debug/trace enabled in production long-term.