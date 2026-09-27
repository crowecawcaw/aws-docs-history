

# Amazon Kinesis Agent with service-managed streams
<a name="service-managed-pk-integrations-kinesis-agent"></a>

The Amazon Kinesis Agent is a producer-only application that reads text files and writes records to a stream with the `PutRecords` API. It always sets a non-null partition key (a random value by default, or an MD5 hash of the record) and uses the AWS SDK directly without the KPL or aggregation. On a service-managed stream, the supplied partition key is ignored for routing and the agent's writes flow through unchanged. No changes are required.