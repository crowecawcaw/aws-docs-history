For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Batching writes with WriteRecords

API

Amazon Timestream for Live Analytics enables you to write data points from a single time series
and/or data points from many series in a single write request. Batching multiple
data points in a single write operation is beneficial from a performance and cost
perspective. See [Writes](metering-and-pricing.md "metering-and-pricing.md") in the Metering and Pricing
section for more details.

###### Note

Your write requests to Timestream for Live Analytics may be throttled as Timestream for Live Analytics scales
to adapt to the data ingestion needs of your application. If your applications
encounter throttling exceptions, you must continue to send data at the same (or
higher) throughput to allow Timestream for Live Analytics to automatically scale to your
application's needs.
