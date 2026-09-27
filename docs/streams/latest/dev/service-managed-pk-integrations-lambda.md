

# AWS Lambda triggers with service-managed streams
<a name="service-managed-pk-integrations-lambda"></a>

AWS Lambda event source mappings work with service-managed streams without modification. Lambda continues to poll shards and invoke your function with batches of records. The `partitionKey` field in the event record may be `null` for records written without a partition key. Ensure your Lambda function handles null partition keys gracefully.