For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# The NULLIF statement

The **IF** statement evaluates a condition to be true or false and returns
the appropriate value. Timestream supports the following two syntax representations for
**IF**:

**NULLIF** returns null if `value1` equals `value2`;
otherwise it returns `value1`. The syntax is as follows:

```
nullif(value1, value2)
```
