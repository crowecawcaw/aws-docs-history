

# Access records in CDC streams in Amazon Keyspaces
<a name="keyspaces-records-cdc"></a>

To access the records in a stream, you use the [Amazon Keyspaces Streams API](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/Welcome.html). The following section contains examples on how to access records using the AWS CLI.

For the required permissions, see [Configure permissions to work with CDC streams in Amazon Keyspaces](configure-cdc-permissions.md).

**Access records in a stream using the AWS CLI**

1. You can use the Amazon Keyspaces Streams API to access the change records of the stream. For more information, see [*Amazon Keyspaces Streams API Reference*](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/Welcome.html). To retrieve the shards within the stream, you can use the `get-stream` API as shown in the following example.

   ```
   aws keyspacesstreams get-stream \
   --stream-arn 'arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/mytable/stream/{{STREAM_LABEL}}'
   ```

   The following is an example of the output.

   ```
   {
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
   }
   ```

1. To retrieve records from the stream, you start with getting an iterator that provides you with the starting point for accessing records. To do this, you can use the shards within the CDC stream returned by the API in the previous step. To gather the iterator, you can use the `get-shard-iterator` API. For this example, you use an iterator of type `TRIM_HORIZON` that retrieves from the last trimmed point or beginning) of the shard.

   ```
   aws keyspacesstreams get-shard-iterator \
   --stream-arn 'arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/mytable/stream/{{STREAM_LABEL}}' \
   --shard-id '{{SHARD_ID}}' \
   --shard-iterator-type 'TRIM_HORIZON'
   ```

   The output of the command looks like in the following example.

   ```
   {
       "ShardIterator": "<SHARD_ITERATOR>" 
   }
   ```

1. To retrieve the CDC records using the `get-records` API, you can use the iterator returned in the last step. The following command is an example of this.

   ```
   aws keyspacesstreams get-records \
   --shard-iterator '{{SHARD_ITERATOR}}' \
   --limit 100
   ```

   The following is an example of the output.

   ```
   {
       "changeRecords": [...],
       "nextShardIterator": "<NEXT_SHARD_ITERATOR>",
       "iteratorDescription": {
           "iteratorPosition": "BEHIND_TIP"
       }
   }
   ```

## Optimize polling frequency with iterator position
<a name="keyspaces-cdc-polling-guidance"></a>

The `GetRecords` response includes an `iteratorDescription` field that indicates your consumer's current position within the shard:
+ `AT_TIP` — No more records are currently available. Consider reducing your polling frequency to optimize costs.
+ `BEHIND_TIP` — The stream tip advances continuously. Additional records may be available. Continue polling at your normal frequency.

`BEHIND_TIP` with an empty `changeRecords` list indicates the stream is progressing but no customer records are available at this position. Continue polling normally.