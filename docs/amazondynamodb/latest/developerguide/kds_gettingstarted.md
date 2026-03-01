# Getting started with Kinesis Data Streams for Amazon DynamoDB

This section describes how to use Kinesis Data Streams for Amazon DynamoDB tables with the Amazon DynamoDB console,
the AWS Command Line Interface (AWS CLI), and the API.

## Creating an active Amazon Kinesis data stream

All of these examples use the `Music` DynamoDB table that was created as part
of the [Getting
started with DynamoDB](GettingStartedDynamoDB.md "GettingStartedDynamoDB.md") tutorial.

To learn more about how to build consumers and connect your Kinesis data stream to other
AWS services, see [Reading data from Kinesis Data Streams](../../../streams/latest/dev/building-consumers.md "../../../streams/latest/dev/building-consumers.md") in
the _Amazon Kinesis Data Streams developer guide_.

###### Note

When you're first using KDS shards, we recommend setting your shards to scale up
and down with usage patterns. After you have accumulated more data on usage
patterns, you can adjust the shards in your stream to match.

Console

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis/](https://console.aws.amazon.com/kinesis/ "https://console.aws.amazon.com/kinesis/").
2. Choose **Create data stream** and follow the
   instructions to create a stream called `samplestream`.
3. Open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
4. In the navigation pane on the left side of the console, choose
   **Tables**.
5. Choose the **Music** table.
6. Choose the **Exports and streams** tab.
7. (Optional) Under **Amazon Kinesis data stream
   details**, you can change the record timestamp precision
   from microsecond (default) to millisecond.
8. Choose **samplestream** from the dropdown
   list.
9. Choose the **Turn On** button.

AWS CLI

1. Create a Kinesis Data Streams named `samplestream` by using the [create-stream command](../../../cli/latest/reference/kinesis/create-stream.md "../../../cli/latest/reference/kinesis/create-stream.md").

```
aws kinesis create-stream --stream-name samplestream --shard-count 3
```

See [Shard management considerations for Kinesis Data Streams](kds_using-shards-and-metrics.md#kds_using-shards-and-metrics.shardmanagment "kds_using-shards-and-metrics.md#kds_using-shards-and-metrics.shardmanagment")
before setting the number of shards for the Kinesis data stream. 2. Check that the Kinesis stream is active and ready for use by using
the [describe-stream command](../../../cli/latest/reference/kinesis/describe-stream.md "../../../cli/latest/reference/kinesis/describe-stream.md").

```
aws kinesis describe-stream --stream-name samplestream
```

3. Enable Kinesis streaming on the DynamoDB table by using the DynamoDB
   `enable-kinesis-streaming-destination` command.
   Replace the `stream-arn` value with the one that was
   returned by `describe-stream` in the previous step.
   Optionally, enable streaming with a more granular (microsecond)
   precision of timestamp values returned on each record.

Enable streaming with microsecond timestamp precision:

```
aws dynamodb enable-kinesis-streaming-destination \
  --table-name Music \
  --stream-arn arn:aws:kinesis:us-west-2:12345678901:stream/samplestream
  --enable-kinesis-streaming-configuration ApproximateCreationDateTimePrecision=MICROSECOND
```

Or enable streaming with default timestamp precision
(millisecond):

```
aws dynamodb enable-kinesis-streaming-destination \
  --table-name Music \
  --stream-arn arn:aws:kinesis:us-west-2:12345678901:stream/samplestream
```

4. Check if Kinesis streaming is active on the table by using the DynamoDB
   `describe-kinesis-streaming-destination`
   command.

```
aws dynamodb describe-kinesis-streaming-destination --table-name Music
```

5. Write data to the DynamoDB table by using the `put-item`
   command, as described in the [DynamoDB Developer Guide](getting-started-step-2.md "getting-started-step-2.md").

```
aws dynamodb put-item \
    --table-name Music  \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "1"}}'

aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}, "AlbumTitle": {"S": "Songs About Life"}, "Awards": {"N": "10"} }'
```

6. Use the Kinesis [get-records](../../../cli/latest/reference/kinesis/get-records.md "../../../cli/latest/reference/kinesis/get-records.md") CLI command to retrieve the Kinesis stream
   contents. Then use the following code snippet to deserialize the
   stream content.

```
/**
 * Takes as input a Record fetched from Kinesis and does arbitrary processing as an example.
 */
public void processRecord(Record kinesisRecord) throws IOException {
    ByteBuffer kdsRecordByteBuffer = kinesisRecord.getData();
    JsonNode rootNode = OBJECT_MAPPER.readTree(kdsRecordByteBuffer.array());
    JsonNode dynamoDBRecord = rootNode.get("dynamodb");
    JsonNode oldItemImage = dynamoDBRecord.get("OldImage");
    JsonNode newItemImage = dynamoDBRecord.get("NewImage");
    Instant recordTimestamp = fetchTimestamp(dynamoDBRecord);

    /**
     * Say for example our record contains a String attribute named "stringName" and we want to fetch the value
     * of this attribute from the new item image. The following code fetches this value.
     */
    JsonNode attributeNode = newItemImage.get("stringName");
    JsonNode attributeValueNode = attributeNode.get("S"); // Using DynamoDB "S" type attribute
    String attributeValue = attributeValueNode.textValue();
    System.out.println(attributeValue);
}

private Instant fetchTimestamp(JsonNode dynamoDBRecord) {
    JsonNode timestampJson = dynamoDBRecord.get("ApproximateCreationDateTime");
    JsonNode timestampPrecisionJson = dynamoDBRecord.get("ApproximateCreationDateTimePrecision");
    if (timestampPrecisionJson != null && timestampPrecisionJson.equals("MICROSECOND")) {
        return Instant.EPOCH.plus(timestampJson.longValue(), ChronoUnit.MICROS);
    }
    return Instant.ofEpochMilli(timestampJson.longValue());
}
```

Java

1. Follow the instructions in the Kinesis Data Streams developer guide to [create](../../../streams/latest/dev/kinesis-using-sdk-java-create-stream.md "../../../streams/latest/dev/kinesis-using-sdk-java-create-stream.md") a Kinesis data stream named
   `samplestream` using Java.

See [Shard management considerations for Kinesis Data Streams](kds_using-shards-and-metrics.md#kds_using-shards-and-metrics.shardmanagment "kds_using-shards-and-metrics.md#kds_using-shards-and-metrics.shardmanagment")
before setting the number of shards for the Kinesis data stream. 2. Use the following code snippet to enable Kinesis streaming on the
DynamoDB table. Optionally, enable streaming with a more granular
(microsecond) precision of timestamp values returned on each record.

Enable streaming with microsecond timestamp precision:

```
EnableKinesisStreamingConfiguration enableKdsConfig = EnableKinesisStreamingConfiguration.builder()
  .approximateCreationDateTimePrecision(ApproximateCreationDateTimePrecision.MICROSECOND)
  .build();

EnableKinesisStreamingDestinationRequest enableKdsRequest = EnableKinesisStreamingDestinationRequest.builder()
  .tableName(tableName)
  .streamArn(kdsArn)
  .enableKinesisStreamingConfiguration(enableKdsConfig)
  .build();

EnableKinesisStreamingDestinationResponse enableKdsResponse = ddbClient.enableKinesisStreamingDestination(enableKdsRequest);
```

Or enable streaming with default timestamp precision
(millisecond):

```
EnableKinesisStreamingDestinationRequest enableKdsRequest = EnableKinesisStreamingDestinationRequest.builder()
  .tableName(tableName)
  .streamArn(kdsArn)
  .build();

EnableKinesisStreamingDestinationResponse enableKdsResponse = ddbClient.enableKinesisStreamingDestination(enableKdsRequest);
```

3. Follow the instructions in the _Kinesis Data Streams developer
   guide_ to [read](../../../streams/latest/dev/building-consumers.md "../../../streams/latest/dev/building-consumers.md")
   from the created data stream.
4. Use the following code snippet to deserialize the stream
   content

```
/**
 * Takes as input a Record fetched from Kinesis and does arbitrary processing as an example.
 */
public void processRecord(Record kinesisRecord) throws IOException {
    ByteBuffer kdsRecordByteBuffer = kinesisRecord.getData();
    JsonNode rootNode = OBJECT_MAPPER.readTree(kdsRecordByteBuffer.array());
    JsonNode dynamoDBRecord = rootNode.get("dynamodb");
    JsonNode oldItemImage = dynamoDBRecord.get("OldImage");
    JsonNode newItemImage = dynamoDBRecord.get("NewImage");
    Instant recordTimestamp = fetchTimestamp(dynamoDBRecord);

    /**
     * Say for example our record contains a String attribute named "stringName" and we wanted to fetch the value
     * of this attribute from the new item image, the below code would fetch this.
     */
    JsonNode attributeNode = newItemImage.get("stringName");
    JsonNode attributeValueNode = attributeNode.get("S"); // Using DynamoDB "S" type attribute
    String attributeValue = attributeValueNode.textValue();
    System.out.println(attributeValue);
}

private Instant fetchTimestamp(JsonNode dynamoDBRecord) {
    JsonNode timestampJson = dynamoDBRecord.get("ApproximateCreationDateTime");
    JsonNode timestampPrecisionJson = dynamoDBRecord.get("ApproximateCreationDateTimePrecision");
    if (timestampPrecisionJson != null && timestampPrecisionJson.equals("MICROSECOND")) {
        return Instant.EPOCH.plus(timestampJson.longValue(), ChronoUnit.MICROS);
    }
    return Instant.ofEpochMilli(timestampJson.longValue());
}
```

## Making changes to an active Amazon Kinesis data stream

This section describes how to make changes to an active Kinesis Data Streams for DynamoDB setup by using
the console, AWS CLI and the API.

**AWS Management Console**

1. Open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/")
2. Go to your table.
3. Choose **Exports and Streams**.

**AWS CLI**

1. Call `describe-kinesis-streaming-destination` to confirm that the
   stream is `ACTIVE`.
2. Call `UpdateKinesisStreamingDestination`, such as in this
   example:

```
aws dynamodb update-kinesis-streaming-destination --table-name enable_test_table --stream-arn arn:aws:kinesis:us-east-1:12345678901:stream/enable_test_stream --update-kinesis-streaming-configuration ApproximateCreationDateTimePrecision=MICROSECOND
```

3. Call `describe-kinesis-streaming-destination` to confirm that the
   stream is `UPDATING`.
4. Call `describe-kinesis-streaming-destination` periodically until
   the streaming status is `ACTIVE` again. It typically takes up to 5
   minutes for the timestamp precision updates to take effect. Once this status
   updates, that indicates that the update is complete and the new precision value
   will be applied on future records.
5. Write to the table using `putItem`.
6. Use the Kinesis `get-records` command to get the stream
   contents.
7. Confirm that the `ApproximateCreationDateTime` of the writes have
   the desired precision.

**Java API**

1. Provide a code snippet that constructs an
   `UpdateKinesisStreamingDestination` request and an
   `UpdateKinesisStreamingDestination` response.
2. Provide a code snippet that constructs a
   `DescribeKinesisStreamingDestination` request and a
   `DescribeKinesisStreamingDestination response`.
3. Call `describe-kinesis-streaming-destination` periodically until
   the streaming status is `ACTIVE` again, indicating that the update is
   complete and the new precision value will be applied on future records.
4. Perform writes to the table.
5. Read from the stream and deserialize the stream content.
6. Confirm that the `ApproximateCreationDateTime` of the writes have
   the desired precision.
