# Best practices for data delivery

The following best practices help you get the most out of data delivery in Amazon Kinesis Data Streams.
For the complete list of delivery metrics referenced in these recommendations, see
[Monitoring data delivery](data-delivery-monitoring.md "data-delivery-monitoring.md").

## Throughput and data freshness

- Set the `DataFreshnessInSeconds` parameter based on your stream throughput.
  Lower values increase delivery frequency but might result in smaller output files.
  Higher values allow more data to accumulate for each delivery cycle.
- Create a Amazon CloudWatch alarm on the `DataFreshness` metric to detect when
  delivery latency exceeds your acceptable threshold.
- You can create multiple deliveries from the same Kinesis Data Streams stream. Each
  delivery operates independently, allowing you to deliver data to multiple destinations
  simultaneously.

## Schema management (streaming tables on Apache Iceberg)

- Register your schemas in AWS Glue Schema Registry before creating a delivery.
  The delivery uses the registered schema to define the destination
  table structure.
- Deliveries do not support schema evolution. If your schema changes, you must
  delete and recreate the delivery with the updated schema.
- Use producer-side schema validation to ensure all records conform to the registered
  schema before they are written to the stream. This minimizes failed record delivery.

## S3 object layout (general purpose Amazon S3 buckets)

- Choose an output key template that matches the query patterns of your downstream
  consumers. For example, use date-based prefixes if your queries frequently filter
  by time range.
- Enable GZIP or ZSTD compression to reduce storage costs and improve read performance
  for downstream analytics workloads.
- Choose the appropriate Amazon S3 storage class based on your data access patterns. Use
  STANDARD for frequently accessed data, INTELLIGENT\_TIERING to let Amazon S3 move
  objects between access tiers automatically, or GLACIER\_IR for rarely accessed
  data that still needs millisecond retrieval.

## Security

- Scope your IAM policy to the specific bucket or table that the delivery
  writes to. Avoid using wildcard resource ARNs.
- Include the `aws:SourceArn` and `aws:SourceAccount`
  condition keys in the trust policy of the IAM role used by the delivery.
  This prevents the confused deputy problem by
  ensuring only your specific delivery can assume the role.
- Enable AWS CloudTrail logging to audit all delivery API calls and configuration
  changes.
- Use a customer-managed AWS KMS key for sensitive data. This gives you full control
  over key rotation, access policies, and audit trails.

## Dead-letter queue

- Always configure a dead-letter queue for your delivery. Records that cannot be
  delivered to the destination are sent to the dead-letter queue for later inspection.
- Monitor the `DLQDeliverySuccess` metric
  (`DeliveryToS3.DLQDeliverySuccess` or
  `DeliveryToIceberg.DLQDeliverySuccess`) in CloudWatch to detect when
  records are being routed to the dead-letter queue.
- Inspect dead-letter queue entries regularly to identify patterns in delivery failures
  and take corrective action at the producer or delivery configuration level.

## Monitoring

- Create CloudWatch alarms on the delivery's `DataFreshness` and failed-record
  metrics (`DeliveryToS3.FailedRecordCount` or
  `DeliveryToIceberg.FailedRowCount`) to proactively detect delivery
  issues.
- Enable CloudWatch Logs for your delivery to capture detailed delivery diagnostics
  and error messages.
- Track the delivered-bytes metric (`DeliveryToS3.BytesOut` or
  `DeliveryToIceberg.BytesOut`) to monitor throughput and identify
  unexpected drops in data volume.
