

# Use `ListShards` with an AWS SDK or CLI
<a name="example_kinesis_ListShards_section"></a>

The following code examples show how to use `ListShards`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_kinesis_Scenario_GettingStarted_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To list shards in a data stream**  
The following `list-shards` example lists all shards in the specified stream starting with the shard whose ID immediately follows the specified `exclusive-start-shard-id` of `shardId-000000000000`.  

```
aws kinesis list-shards \
    --stream-name {{samplestream}} \
    --exclusive-start-shard-id {{shardId-000000000000}}
```
Output:  

```
{
    "Shards": [
        {
            "ShardId": "shardId-000000000001",
            "HashKeyRange": {
                "StartingHashKey": "113427455640312821154458202477256070485",
                "EndingHashKey": "226854911280625642308916404954512140969"
            },
            "SequenceNumberRange": {
                "StartingSequenceNumber": "49600871682979337187563555549332609155523708941634633746"
            }
        },
        {
            "ShardId": "shardId-000000000002",
            "HashKeyRange": {
                "StartingHashKey": "226854911280625642308916404954512140970",
                "EndingHashKey": "340282366920938463463374607431768211455"
            },
            "SequenceNumberRange": {
                "StartingSequenceNumber": "49600871683001637932762086172474144873796357303140614178"
            }
        }
    ]
}
```
For more information, see [Listing Shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-shards.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [ListShards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-shards.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
    def list_shards(self, stream_name, max_wait=30, poll_interval=2):
        """
        Lists the shards in a Kinesis data stream.

        A freshly created stream can report ACTIVE via DescribeStreamSummary
        before its shards are listable. Because ListShards is eventually
        consistent, it may briefly raise ResourceInUseException ("in state
        CREATING") or ResourceNotFoundException. This method retries on those
        errors until the shards become available or ``max_wait`` elapses.

        :param stream_name: The name of the stream whose shards to list.
        :param max_wait: Maximum seconds to retry while the stream is still
                         settling after creation.
        :param poll_interval: Seconds between retries.
        :return: A list of shard dictionaries.
        """
        elapsed = 0
        while True:
            try:
                shards = list()
                response = self.kinesis_client.list_shards(StreamName=stream_name)
                shards.extend(response.get("Shards", list()))
                while "NextToken" in response:
                    response = self.kinesis_client.list_shards(
                        NextToken=response["NextToken"]
                    )
                    shards.extend(response.get("Shards", list()))
                logger.info(
                    "Listed %s shard(s) for stream '%s'.", len(shards), stream_name
                )
                return shards
            except ClientError as err:
                code = err.response["Error"]["Code"]
                retryable = ("ResourceInUseException", "ResourceNotFoundException")
                if code in retryable and elapsed < max_wait:
                    logger.info(
                        "Stream '%s' not ready for ListShards yet. Retrying...",
                        stream_name,
                    )
                    time.sleep(poll_interval)
                    elapsed += poll_interval
                    continue
                if code == "ResourceNotFoundException":
                    logger.error(
                        "Stream '%s' not found. Verify the stream is ACTIVE.",
                        stream_name,
                    )
                raise
```
+  For API details, see [ListShards](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListShards) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.