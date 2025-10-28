# Use `GetShardIterator` with a CLI

The following code examples show how to use `GetShardIterator`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_kinesis_Scenario_GettingStarted_section.md "example_kinesis_Scenario_GettingStarted_section.md")

CLI

**AWS CLI**

**To obtain a shard iterator**

The following `get-shard-iterator` example uses the `AT_SEQUENCE_NUMBER` shard iterator type and generates a shard iterator to start reading data records exactly from the position denoted by the specified sequence number.

```
`aws kinesis get-shard-iterator \
 --stream-name `samplestream` \
 --shard-id `shardId-000000000001` \
 --shard-iterator-type `LATEST``

```

Output:

```
{
    "ShardIterator": "AAAAAAAAAAFEvJjIYI+3jw/4aqgH9FifJ+n48XWTh/IFIsbILP6o5eDueD39NXNBfpZ10WL5K6ADXk8w+5H+Qhd9cFA9k268CPXCz/kebq1TGYI7Vy+lUkA9BuN3xvATxMBGxRY3zYK05gqgvaIRn94O8SqeEqwhigwZxNWxID3Ej7YYYcxQi8Q/fIrCjGAy/n2r5Z9G864YpWDfN9upNNQAR/iiOWKs"
}
```

For more information, see [Developing Consumers Using the Kinesis Data Streams API with the AWS SDK for Java](developing-consumers-with-sdk.md "developing-consumers-with-sdk.md") in the _Amazon Kinesis Data Streams Developer Guide_.

- For API details, see
  [GetShardIterator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-shard-iterator.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-shard-iterator.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns a shard iterator for the specified shard and starting position. Details of the shard identifiers and sequence numbers can be obtained from the output of the Get-KINStream cmdlet, by referencing the Shards collection of the returned stream object. The returned iterator can be used with the Get-KINRecord cmdlet to pull data records in the shard.**

```
Get-KINShardIterator -StreamName "mystream" -ShardId "shardId-000000000000" -ShardIteratorType AT_SEQUENCE_NUMBER -StartingSequenceNumber "495598645..."

```

**Output:**

```
AAAAAAAAAAGIc....9VnbiRNaP
```

- For API details, see
  [GetShardIterator](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns a shard iterator for the specified shard and starting position. Details of the shard identifiers and sequence numbers can be obtained from the output of the Get-KINStream cmdlet, by referencing the Shards collection of the returned stream object. The returned iterator can be used with the Get-KINRecord cmdlet to pull data records in the shard.**

```
Get-KINShardIterator -StreamName "mystream" -ShardId "shardId-000000000000" -ShardIteratorType AT_SEQUENCE_NUMBER -StartingSequenceNumber "495598645..."

```

**Output:**

```
AAAAAAAAAAGIc....9VnbiRNaP
```

- For API details, see
  [GetShardIterator](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
