# Access records in CDC streams in Amazon Keyspaces

To access the records in a stream, you use the [Amazon Keyspaces Streams API](../StreamsAPIReference/Welcome.md "../StreamsAPIReference/Welcome.md").
The following section contains examples on how to access records using the AWS CLI.

For the required permissions, see [Configure permissions to work with CDC streams in Amazon Keyspaces](configure-cdc-permissions.md "configure-cdc-permissions.md").

###### Access records in a stream using the AWS CLI

1. You can use the Amazon Keyspaces Streams API to access the change records of the stream. For more information, see
   [_Amazon Keyspaces Streams API Reference_](../StreamsAPIReference/Welcome.md "../StreamsAPIReference/Welcome.md").
   To retrieve the shards
   within the stream, you can use the `get-stream` API as shown in the following example.

```
aws keyspacesstreams get-stream \
--stream-arn 'arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/table/mytable/stream/`STREAM_LABEL`'
```

The following is an example of the output.

```
`{
 "StreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable/stream/2023-05-11T21:21:33.291",
 "StreamStatus": "ENABLED",
 "StreamViewType": "NEW_AND_OLD_IMAGES",
 "CreationRequestDateTime": "<CREATION_TIME>",
 "KeyspaceName": "mykeyspace",
 "TableName": "mytable",
 "StreamLabel": "2023-05-11T21:21:33.291",
 "Shards": [
 {
 "SequenceNumberRange": {
 "EndingSequenceNumber": "<END_SEQUENCE_NUMBER>",
 "StartingSequenceNumber": "<START_SEQUENCE_NUMBER>"
 },
 "ShardId": "<SHARD_ID>"
 },
 ]
}`
```

2. To retrieve records from the stream, you start with getting an iterator
   that provides you with the starting point for accessing records. To do this, you can
   use the shards within the CDC stream returned by the API in the previous step.
   To gather the iterator, you can use the `get-shard-iterator` API. For this
   example, you use an iterator of type `TRIM_HORIZON` that retrieves from the
   last trimmed point or beginning) of the shard.

```
aws keyspacesstreams get-shard-iterator \
--stream-arn 'arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/table/mytable/stream/`STREAM_LABEL`' \
--shard-id '`SHARD_ID`' \
--shard-iterator-type 'TRIM_HORIZON'
```

The output of the command looks like in the following example.

```
`{
 "ShardIterator": "<SHARD_ITERATOR>"
}`
```

3. To retrieve the CDC records using the `get-records` API, you
   can use the iterator returned in the last step. The following command is an example
   of this.

```
aws keyspacesstreams get-records \
--shard-iterator '`SHARD_ITERATOR`' \
--limit 100
```
