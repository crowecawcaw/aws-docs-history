

# KCL considerations
<a name="service-managed-pk-kpl-kcl-considerations"></a>

If you use the Kinesis Client Library (KCL) to consume from service-managed streams, no KCL changes are required. KCL continues to process records from shards in sequence as it does today, and handles records with a null partition key without modification.

The KCL itself requires no changes to consume from a service-managed stream, and you do not need to upgrade the KCL. However, if a producer writes KPL-aggregated records to a service-managed stream (for example, because aggregation was not disabled), the KCL de-aggregation path can silently drop those records, because the aggregation contract does not hold when the service places records by its own algorithm. Ensure producers disable aggregation, or upgrade the KPL and grant it the `kinesis:DescribeStreamSummary` permission, so that aggregated records are never written to a service-managed stream.