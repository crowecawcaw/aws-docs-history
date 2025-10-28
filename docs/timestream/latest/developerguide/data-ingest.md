For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Writes

- Ensure that the timestamp of the incoming data is not earlier than data
  retention configured for the memory store and no later than the future ingestion
  period defined in [Quotas](ts-limits.md "ts-limits.md"). Sending
  data with a timestamp outside these bounds will result in the data being
  rejected by Timestream for LiveAnalytics unless you enable magnetic store writes for your table. If you
  enable magnetic store writes, ensure that the timestamp for incoming data is not
  earlier than data retention configured for the magnetic store.
- If you expect late arriving data, turn on magnetic store writes for your
  table. This will allow ingestion for data with timestamps that fall outside your
  memory store retention period but still within your magnetic store retention
  period. You can set this by updating the `EnableMagneticStoreWrites`
  flag in the `MagneticStoreWritesProperties` for your table. This
  property is false by default. Note that writes to the magnetic store will not be
  immediately available to query. They will be available within 6 hours.
- Target high throughput workloads to the memory store by ensuring the
  timestamps of the ingested data fall within the memory store retention bounds.
  Writes to the magnetic store are limited to a max number of active magnetic
  store partitions that can receive concurrent ingestion for a database. You can
  see this `ActiveMagneticStorePartitions` metric in CloudWatch. To reduce
  active magnetic store partitions, aim to reduce the number of series and
  duration of time you ingest into concurrently for magnetic store
  ingestion.
- While sending data to Timestream for LiveAnalytics, batch multiple records in a single request to
  optimize data ingestion performance.
  - It is beneficial to batch together records from the same time series
    and records with the same measure name.
  - Batch as many records as possible in a single request as long as the
    requests are within the service limits defined in [Quotas](ts-limits.md "ts-limits.md").
  - Use common attributes where possible to reduce data transfer and
    ingestion costs. For more information, see [WriteRecords API](API_WriteRecords.md "API_WriteRecords.md").

- If you encounter partial client-side failures while writing data to Timestream for LiveAnalytics, you
  can resend the batch of records that failed ingestion after you've addressed the
  rejection cause.
- Data ordered by timestamps has better write performance.
- Amazon Timestream for LiveAnalytics is designed to automatically scale to the needs of your application.
  When Timestream for LiveAnalytics notices spikes in write requests from your application, your
  application may experience some level of initial memory store throttling. If
  your application experiences memory store throttling, continue sending data to
  Timestream for LiveAnalytics at the same (or increased) rate to enable Timestream for LiveAnalytics to automatically scale to
  satisfy the needs of your application. If you see magnetic store throttling, you
  should decrease your rate of magnetic store ingestion until your number of
  `ActiveMagneticStorePartitions` falls.
