For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Conversion functions

Timestream for LiveAnalytics supports the following conversion functions.

###### Topics

- [cast()](#conversion-functions.cast "#conversion-functions.cast")
- [try_cast()](#conversion-functions.try-cast "#conversion-functions.try-cast")

## cast()

The syntax of the cast function to explicitly cast a value as a type is as follows.

```
cast(value AS type)
```

## try_cast()

Timestream for LiveAnalytics also supports the try_cast function that is similar to cast but returns null if
cast fails. The syntax is as follows.

```
try_cast(value AS type)
```
