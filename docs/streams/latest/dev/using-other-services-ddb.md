

# Write to Kinesis Data Streams using Amazon DynamoDB
<a name="using-other-services-ddb"></a>

You can use Amazon Kinesis Data Streams to capture changes to Amazon DynamoDB. Kinesis Data Streams captures item-level modifications in any DynamoDB table and replicates them to a Kinesis data stream. Your consumer applications can access this stream to view item-level changes in real time and deliver those changes downstream or take action based on the content.

For more information, see [how Kinesis Data Streams work with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds.html) in the *Amazon DynamoDB Developer Guide*. 