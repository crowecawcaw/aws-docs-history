

# Actions, resources, and condition keys for Amazon Kinesis Data Streams
<a name="list_kinesis"></a>

Amazon Kinesis Data Streams (service prefix: `kinesis`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/streams/latest/dev/introduction.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/kinesis/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kinesis/kinesis.json) for this service.

**Topics**
+ [API operations defined by Amazon Kinesis Data Streams](#list_kinesis-operations)
+ [Actions defined by Amazon Kinesis Data Streams](#list_kinesis-actions-as-permissions)
+ [Permission-only actions for Amazon Kinesis Data Streams](#list_kinesis-permission-only-actions)
+ [Resource types defined by Amazon Kinesis Data Streams](#list_kinesis-resources-for-iam-policies)
+ [Condition keys for Amazon Kinesis Data Streams](#list_kinesis-policy-keys)

## API operations defined by Amazon Kinesis Data Streams
<a name="list_kinesis-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kinesis-actions-as-permissions).




- **   AddTagsToStream  **
  - **IAM action:**  [kinesis:AddTagsToStream](#list_kinesis-action-AddTagsToStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CreateChannel  **
  - **IAM action:**  [kinesis:AssociateStreamsWithChannel](#list_kinesis-action-AssociateStreamsWithChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kinesis:CreateChannel](#list_kinesis-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [kinesis:TagResource](#list_kinesis-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesis.amazonaws.com / **Access level:** Write

- **   CreateStream  **
  - **IAM action:**  [kinesis:AddTagsToStream](#list_kinesis-action-AddTagsToStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [kinesis:CreateStream](#list_kinesis-action-CreateStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DecreaseStreamRetentionPeriod  **
  - **IAM action:**  [kinesis:DecreaseStreamRetentionPeriod](#list_kinesis-action-DecreaseStreamRetentionPeriod) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChannel  **
  - **IAM action:**  [kinesis:DeleteChannel](#list_kinesis-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [kinesis:DeleteResourcePolicy](#list_kinesis-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStream  **
  - **IAM action:**  [kinesis:DeleteStream](#list_kinesis-action-DeleteStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterStreamConsumer  **
  - **IAM action:**  [kinesis:DeregisterStreamConsumer](#list_kinesis-action-DeregisterStreamConsumer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountSettings  **
  - **IAM action:**  [kinesis:DescribeAccountSettings](#list_kinesis-action-DescribeAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeChannel  **
  - **IAM action:**  [kinesis:DescribeChannel](#list_kinesis-action-DescribeChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLimits  **
  - **IAM action:**  [kinesis:DescribeLimits](#list_kinesis-action-DescribeLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStream  **
  - **IAM action:**  [kinesis:DescribeStream](#list_kinesis-action-DescribeStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStreamConsumer  **
  - **IAM action:**  [kinesis:DescribeStreamConsumer](#list_kinesis-action-DescribeStreamConsumer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStreamSummary  **
  - **IAM action:**  [kinesis:DescribeStreamSummary](#list_kinesis-action-DescribeStreamSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableEnhancedMonitoring  **
  - **IAM action:**  [kinesis:DisableEnhancedMonitoring](#list_kinesis-action-DisableEnhancedMonitoring) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableEnhancedMonitoring  **
  - **IAM action:**  [kinesis:EnableEnhancedMonitoring](#list_kinesis-action-EnableEnhancedMonitoring) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetRecords  **
  - **IAM action:**  [kinesis:GetRecords](#list_kinesis-action-GetRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [kinesis:GetResourcePolicy](#list_kinesis-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetShardIterator  **
  - **IAM action:**  [kinesis:GetShardIterator](#list_kinesis-action-GetShardIterator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   IncreaseStreamRetentionPeriod  **
  - **IAM action:**  [kinesis:IncreaseStreamRetentionPeriod](#list_kinesis-action-IncreaseStreamRetentionPeriod) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListChannels  **
  - **IAM action:**  [kinesis:ListChannels](#list_kinesis-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListShards  **
  - **IAM action:**  [kinesis:ListShards](#list_kinesis-action-ListShards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreamConsumers  **
  - **IAM action:**  [kinesis:ListStreamConsumers](#list_kinesis-action-ListStreamConsumers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreams  **
  - **IAM action:**  [kinesis:ListStreams](#list_kinesis-action-ListStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [kinesis:ListTagsForResource](#list_kinesis-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForStream  **
  - **IAM action:**  [kinesis:ListTagsForStream](#list_kinesis-action-ListTagsForStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   MergeShards  **
  - **IAM action:**  [kinesis:MergeShards](#list_kinesis-action-MergeShards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRecord  **
  - **IAM action:**  [kinesis:PutRecord](#list_kinesis-action-PutRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRecords  **
  - **IAM action:**  [kinesis:PutRecords](#list_kinesis-action-PutRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [kinesis:PutResourcePolicy](#list_kinesis-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterStreamConsumer  **
  - **IAM action:**  [kinesis:RegisterStreamConsumer](#list_kinesis-action-RegisterStreamConsumer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kinesis:TagResource](#list_kinesis-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RemoveTagsFromStream  **
  - **IAM action:**  [kinesis:RemoveTagsFromStream](#list_kinesis-action-RemoveTagsFromStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   SplitShard  **
  - **IAM action:**  [kinesis:SplitShard](#list_kinesis-action-SplitShard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartStreamEncryption  **
  - **IAM action:**  [kinesis:StartStreamEncryption](#list_kinesis-action-StartStreamEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopStreamEncryption  **
  - **IAM action:**  [kinesis:StopStreamEncryption](#list_kinesis-action-StopStreamEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubscribeToShard  **
  - **IAM action:**  [kinesis:SubscribeToShard](#list_kinesis-action-SubscribeToShard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [kinesis:TagResource](#list_kinesis-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kinesis:UntagResource](#list_kinesis-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountSettings  **
  - **IAM action:**  [kinesis:UpdateAccountSettings](#list_kinesis-action-UpdateAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannel  **
  - **IAM action:**  [kinesis:UpdateChannel](#list_kinesis-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMaxRecordSize  **
  - **IAM action:**  [kinesis:UpdateMaxRecordSize](#list_kinesis-action-UpdateMaxRecordSize) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateShardCount  **
  - **IAM action:**  [kinesis:UpdateShardCount](#list_kinesis-action-UpdateShardCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStreamMode  **
  - **IAM action:**  [kinesis:UpdateStreamMode](#list_kinesis-action-UpdateStreamMode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStreamWarmThroughput  **
  - **IAM action:**  [kinesis:UpdateStreamWarmThroughput](#list_kinesis-action-UpdateStreamWarmThroughput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Kinesis Data Streams
<a name="list_kinesis-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTagsToStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_AddTagsToStream.html)  **
  - **Description:** Grants permission to add or update tags for the specified Amazon Kinesis stream. Each stream can have up to 50 tags
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [AssociateStreamsWithChannel](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateChannel.html)  **
  - **Description:** Grants permission to associate a stream with a channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateChannel.html)  **
  - **Description:** Grants permission to create a channel that delivers data from a selected single stream to a destination
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [CreateStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html)  **
  - **Description:** Grants permission to create a Amazon Kinesis stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Access level:** Write

- **   [DecreaseStreamRetentionPeriod](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DecreaseStreamRetentionPeriod.html)  **
  - **Description:** Grants permission to decrease the stream's retention period, which is the length of time data records are accessible after they are added to the stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteChannel.html)  **
  - **Description:** Grants permission to delete the specified channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy associated with a specified stream or consumer
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteStream.html)  **
  - **Description:** Grants permission to delete a stream and all its shards and data
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeregisterStreamConsumer.html)  **
  - **Description:** Grants permission to deregister a stream consumer with a Kinesis data stream
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountSettings](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeAccountSettings.html)  **
  - **Description:** Grants permission to describe the account-level settings for Amazon Kinesis Data Streams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeChannel](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeChannel.html)  **
  - **Description:** Grants permission to describe the specified channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLimits](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeLimits.html)  **
  - **Description:** Grants permission to describe the shard limits and usage for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html)  **
  - **Description:** Grants permission to describe the specified stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamConsumer.html)  **
  - **Description:** Grants permission to get the description of a registered stream consumer
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStreamSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html)  **
  - **Description:** Grants permission to provide a summarized description of the specified Kinesis data stream without the shard list
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableEnhancedMonitoring](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DisableEnhancedMonitoring.html)  **
  - **Description:** Grants permission to disables enhanced monitoring
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableEnhancedMonitoring](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_EnableEnhancedMonitoring.html)  **
  - **Description:** Grants permission to enable enhanced Kinesis data stream monitoring for shard-level metrics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html)  **
  - **Description:** Grants permission to get data records from a shard
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get a resource policy associated with a specified stream or consumer
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetShardIterator](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html)  **
  - **Description:** Grants permission to get a shard iterator. A shard iterator expires five minutes after it is returned to the requester
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [IncreaseStreamRetentionPeriod](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_IncreaseStreamRetentionPeriod.html)  **
  - **Description:** Grants permission to increase the stream's retention period, which is the length of time data records are accessible after they are added to the stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListChannels](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListChannels.html)  **
  - **Description:** Grants permission to list the channels in the account, optionally filtered by stream
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListShards](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html)  **
  - **Description:** Grants permission to list the shards in a stream and provides information about each shard
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStreamConsumers](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreamConsumers.html)  **
  - **Description:** Grants permission to list the stream consumers registered to receive data from a Kinesis stream using enhanced fan-out, and provides information about each consumer
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html)  **
  - **Description:** Grants permission to list your streams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified Amazon Kinesis resource
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForStream.html)  **
  - **Description:** Grants permission to list the tags for the specified Amazon Kinesis stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [MergeShards](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MergeShards.html)  **
  - **Description:** Grants permission to merge two adjacent shards in a stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html)  **
  - **Description:** Grants permission to write a single data record from a producer into an Amazon Kinesis stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html)  **
  - **Description:** Grants permission to write multiple data records from a producer into an Amazon Kinesis stream in a single call (also referred to as a PutRecords request)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to a specified stream or consumer
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RegisterStreamConsumer.html)  **
  - **Description:** Grants permission to register a stream consumer with a Kinesis data stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Access level:** Write

- **   [RemoveTagsFromStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RemoveTagsFromStream.html)  **
  - **Description:** Grants permission to remove tags from the specified Kinesis data stream. Removed tags are deleted and cannot be recovered after this operation successfully completes
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [SplitShard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SplitShard.html)  **
  - **Description:** Grants permission to split a shard into two new shards in the Kinesis data stream, to increase the stream's capacity to ingest and transport data
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartStreamEncryption](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StartStreamEncryption.html)  **
  - **Description:** Grants permission to enable or update server-side encryption using an AWS KMS key for a specified stream
  - **Resource types (\*required):** [kmsKey\*](#list_kinesis-resource-kmsKey) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopStreamEncryption](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StopStreamEncryption.html)  **
  - **Description:** Grants permission to disable server-side encryption for a specified stream
  - **Resource types (\*required):** [kmsKey\*](#list_kinesis-resource-kmsKey) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubscribeToShard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html)  **
  - **Description:** Grants permission to listen to a specific shard with enhanced fan-out
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or update tags for the specified Amazon Kinesis resource. Each resource can have up to 50 tags
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified Kinesis data resource. Removed tags are deleted and cannot be recovered after this operation successfully completes
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Resource types (\*required):** [consumer\*](#list_kinesis-resource-consumer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to update the account-level settings for Amazon Kinesis Data Streams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateChannel](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateChannel.html)  **
  - **Description:** Grants permission to update the logging configuration and destination data freshness for the specified channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMaxRecordSize](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateMaxRecordSize.html)  **
  - **Description:** Grants permission to update the maximum record size for a Kinesis data stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateShardCount](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateShardCount.html)  **
  - **Description:** Grants permission to update the shard count of the specified stream to the specified number of shards
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateStreamMode](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamMode.html)  **
  - **Description:** Grants permission to update the capacity mode of the data stream
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateStreamWarmThroughput](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamWarmThroughput.html)  **
  - **Description:** Grants permission to update the warm throughput for a Kinesis on-demand data stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Kinesis Data Streams
<a name="list_kinesis-permission-only-actions"></a>

The following actions are defined by Amazon Kinesis Data Streams but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [InjectApiError](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)  | Grants permission to temporarily inject errors for target API requests |  | [kinesis:FisActionId](#list_kinesis-kinesis_FisActionId)<br />[kinesis:FisInjectPercentage](#list_kinesis-kinesis_FisInjectPercentage)<br />[kinesis:FisTargetArns](#list_kinesis-kinesis_FisTargetArns) | Write | 

## Resource types defined by Amazon Kinesis Data Streams
<a name="list_kinesis-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#data-delivery-concept)  | arn:${Partition}:kinesis:${Region}:${Account}:channel/${ChannelId} | [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_) | 
|  [consumer](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#enabled-application)  | arn:${Partition}:kinesis:${Region}:${Account}:${StreamType}/${StreamName}/consumer/${ConsumerName}:${ConsumerCreationTimpstamp} | [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_) | 
|  [kmsKey](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html)  | arn:${Partition}:kms:${Region}:${Account}:key/${KeyId} | [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_) | 
|  [stream](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#stream)  | arn:${Partition}:kinesis:${Region}:${Account}:stream/${StreamName} | [aws:ResourceTag/${TagKey}](#list_kinesis-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Kinesis Data Streams
<a name="list_kinesis-policy-keys"></a>

Amazon Kinesis Data Streams defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [kinesis:FisActionId](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)  | Filters access by the ID of an AWS FIS action | String | 
|   [kinesis:FisInjectPercentage](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)  | Filters access by the percentage of calls being affected by an AWS FIS action | Numeric | 
|   [kinesis:FisTargetArns](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)  | Filters access by the ARN of an AWS FIS target | ArrayOfARN | 