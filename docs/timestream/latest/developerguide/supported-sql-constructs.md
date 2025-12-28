For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DESCRIBE statements

You can view the metadata for a table by using the `DESCRIBE` statement. The
syntax is as follows:

```
DESCRIBE database.table
```

where `table` contains the table name. The describe statement returns the column
names and data types for the table.
