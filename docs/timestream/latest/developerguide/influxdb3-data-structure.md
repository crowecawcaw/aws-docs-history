For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# InfluxDB data structure in Timestream for InfluxDB 3

InfluxDB 3 Enterprise organizes time-series data into databases and tables:

- Database: A named location where time-series data is stored (equivalent to a bucket in
  InfluxDB Cloud Serverless).
- Table: A logical grouping for time-series data. (equivalent to a measurement in InfluxDB
  Cloud Serverless)
- Tags: Key-value pairs storing metadata as string values.
- Fields: Key-value pairs storing actual measurement data.
- Timestamp: Nanosecond-scale UTC Unix timestamp associated with each data point .

## Primary keys

The primary key for a row is the combination of the point's timestamp and tag set. The
primary key does not include tags with null values.

## Tags and fields

- Tags: Store metadata or identifying information about the data source.
  - Can only be string values.
  - Used for filtering and grouping data.

- Fields: Store measured values.
  - Support multiple data types: Integer, Unsigned integer, Float, String, Boolean.

## Schema restrictions

- No Duplicate Names: Tags and fields within the same table must have unique names.
- Column Limit: Tables have a maximum number of columns (including time column).
