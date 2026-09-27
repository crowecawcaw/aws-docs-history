

# Amazon EventBridge Pipes with service-managed streams
<a name="service-managed-pk-integrations-eventbridge-pipes"></a>

Amazon EventBridge Pipes can use a Kinesis Data Streams stream as a target (Pipes writes records with the `PutRecords` API) and as a source (a Pipes poller reads records and forwards them). EventBridge Pipes uses the AWS SDK directly, without the KPL or KCL and without aggregation.
+ **Service-managed stream as a target** – Works without changes. EventBridge Pipes always sends a non-null partition key (the configured value, or the pipe execution ID). On a service-managed stream, the supplied key is ignored for routing and records are distributed evenly across shards.
+ **Service-managed stream as a source** – EventBridge Pipes consumes records from a service-managed stream, including records written without a partition key. Ensure any downstream targets or enrichment steps in your pipe do not require a partition key value.