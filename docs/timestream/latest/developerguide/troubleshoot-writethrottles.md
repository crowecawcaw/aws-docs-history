For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Handling WriteRecords throttles

Your memory store write requests to Timestream may be throttled as Timestream scales
to adapt to the data ingestion needs of your application. If your applications encounter
throttling exceptions, you must continue to send data at the same (or higher) throughput
to allow Timestream to automatically scale to your application's needs.

Your magnetic store write requests to Timestream may be throttled if the maximum limit
of magnetic store partitions receiving ingestion. You will see a throttle message
directing you to check the `ActiveMagneticStorePartitions` Cloudwatch metric
for this database. This throttle may take up to 6 hours to resolve. To avoid this
throttle, you should use the memory store for any high throughput ingestion workload.
For magnetic store ingestion, you can target ingesting into fewer partitions by limiting
how many series and the time duration that you ingest into

For more information about data ingestion best practices, see [Writes](data-ingest.md "data-ingest.md").
