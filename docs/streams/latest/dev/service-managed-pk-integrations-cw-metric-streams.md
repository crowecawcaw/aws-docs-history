

# CloudWatch metric streams with service-managed streams
<a name="service-managed-pk-integrations-cw-metric-streams"></a>

Amazon CloudWatch metric streams can deliver metric data to a Kinesis Data Streams stream. The metric stream producer sets a partition key, and its consumer reads the partition key back for deduplication and routing. On a service-managed stream, the partition key is ignored only for shard placement and is still returned to consumers as supplied, so deduplication logic that reads the key back continues to work. No changes are required. Note that service-managed record distribution is available only for on-demand streams; metric streams that use provisioned streams continue to use user-managed partition keys.