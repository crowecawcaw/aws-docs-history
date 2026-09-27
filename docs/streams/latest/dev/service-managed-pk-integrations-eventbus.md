

# Amazon EventBridge event bus with service-managed streams
<a name="service-managed-pk-integrations-eventbus"></a>

An Amazon EventBridge event bus can deliver events to a Kinesis Data Streams stream as a target and consume from a stream as a source. As a producer, an event bus always sends a non-null partition key (it generates a random value when no Kinesis parameters are configured) and uses the AWS SDK directly without the KPL or aggregation. As a consumer, it has no logic that depends on the partition key value or shard placement. On a service-managed stream, the supplied partition key is ignored for routing and null partition key records are consumed cleanly. No changes are required.