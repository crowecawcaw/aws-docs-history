

# Use `GetShardIterator` with an AWS SDK or CLI
<a name="example_kinesis_GetShardIterator_section"></a>

The following code examples show how to use `GetShardIterator`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_kinesis_Scenario_GettingStarted_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To obtain a shard iterator**  
The following `get-shard-iterator` example uses the `AT_SEQUENCE_NUMBER` shard iterator type and generates a shard iterator to start reading data records exactly from the position denoted by the specified sequence number.  

```
aws kinesis get-shard-iterator \
    --stream-name {{samplestream}} \
    --shard-id {{shardId-000000000001}} \
    --shard-iterator-type {{LATEST}}
```
Output:  

```
{
    "ShardIterator": "AAAAAAAAAAFEvJjIYI+3jw/4aqgH9FifJ+n48XWTh/IFIsbILP6o5eDueD39NXNBfpZ10WL5K6ADXk8w+5H+Qhd9cFA9k268CPXCz/kebq1TGYI7Vy+lUkA9BuN3xvATxMBGxRY3zYK05gqgvaIRn94O8SqeEqwhigwZxNWxID3Ej7YYYcxQi8Q/fIrCjGAy/n2r5Z9G864YpWDfN9upNNQAR/iiOWKs"
}
```
For more information, see [Developing Consumers Using the Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-sdk.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [GetShardIterator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-shard-iterator.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Returns a shard iterator for the specified shard and starting position. Details of the shard identifiers and sequence numbers can be obtained from the output of the Get-KINStream cmdlet, by referencing the Shards collection of the returned stream object. The returned iterator can be used with the Get-KINRecord cmdlet to pull data records in the shard.**  

```
Get-KINShardIterator -StreamName "mystream" -ShardId "shardId-000000000000" -ShardIteratorType AT_SEQUENCE_NUMBER -StartingSequenceNumber "495598645..."
```
**Output:**  

```
AAAAAAAAAAGIc....9VnbiRNaP
```
+  For API details, see [GetShardIterator](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Returns a shard iterator for the specified shard and starting position. Details of the shard identifiers and sequence numbers can be obtained from the output of the Get-KINStream cmdlet, by referencing the Shards collection of the returned stream object. The returned iterator can be used with the Get-KINRecord cmdlet to pull data records in the shard.**  

```
Get-KINShardIterator -StreamName "mystream" -ShardId "shardId-000000000000" -ShardIteratorType AT_SEQUENCE_NUMBER -StartingSequenceNumber "495598645..."
```
**Output:**  

```
AAAAAAAAAAGIc....9VnbiRNaP
```
+  For API details, see [GetShardIterator](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
    def get_shard_iterator(self, stream_name, shard_id, iterator_type="TRIM_HORIZON"):
        """
        Gets a shard iterator for reading data records from a shard.

        :param stream_name: The name of the stream.
        :param shard_id: The ID of the shard.
        :param iterator_type: The shard iterator type (e.g., TRIM_HORIZON, LATEST).
        :return: A shard iterator string.
        """
        try:
            response = self.kinesis_client.get_shard_iterator(
                StreamName=stream_name,
                ShardId=shard_id,
                ShardIteratorType=iterator_type,
            )
            shard_iterator = response.get("ShardIterator", None)
            logger.info(
                "Got shard iterator for shard '%s' of type '%s'.",
                shard_id,
                iterator_type,
            )
            return shard_iterator
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' or shard '%s' not found. Verify shard ID is correct.",
                    stream_name,
                    shard_id,
                )
            raise
```
+  For API details, see [GetShardIterator](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetShardIterator) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.