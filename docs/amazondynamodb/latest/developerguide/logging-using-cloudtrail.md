# Logging DynamoDB operations by using AWS CloudTrail

DynamoDB is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in DynamoDB. CloudTrail captures all API calls for DynamoDB as events.
The calls captured include calls from the DynamoDB console and code calls to the DynamoDB API
operations, using both PartiQL and the classic API. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for DynamoDB. If you
don't configure a trail, you can still view the most recent events in the CloudTrail console in
**Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to DynamoDB, the IP address from which the request was
made, who made the request, when it was made, and additional details.

For robust monitoring and alerting, you can also integrate CloudTrail events with [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md"). To enhance your
analysis of DynamoDB service activity and identify changes in activities for an AWS account,
you can query AWS CloudTrail logs using [Amazon
Athena](../../../athena/latest/ug/cloudtrail-logs.md "../../../athena/latest/ug/cloudtrail-logs.md"). For example, you can use queries to identify trends and further isolate
activity by attributes such as source IP address or user.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [DynamoDB information in CloudTrail](#service-name-info-in-cloudtrail "#service-name-info-in-cloudtrail")
- [Understanding DynamoDB log file entries](understanding-ddb-log-entries.md "understanding-ddb-log-entries.md")

## DynamoDB information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity occurs in DynamoDB, that activity is recorded in a CloudTrail event along with
other AWS service events in **Event history**. You can view, search,
and download recent events in your AWS account. For more information, see [Working with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for DynamoDB,
create a trail. A _trail_ enables CloudTrail to deliver log files to an
Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to
all AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data collected
in CloudTrail logs. For more information, see the following:

- [Overview
  for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

### Control plane events in CloudTrail

The following API actions are logged by default as events in CloudTrail files:

**Amazon DynamoDB**

- [CreateBackup](../APIReference/API_CreateBackup.md "../APIReference/API_CreateBackup.md")
- [CreateGlobalTable](../APIReference/API_CreateGlobalTable.md "../APIReference/API_CreateGlobalTable.md")
- [CreateTable](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md")
- [DeleteBackup](../APIReference/API_DeleteBackup.md "../APIReference/API_DeleteBackup.md")
- [DeleteTable](../APIReference/API_DeleteTable.md "../APIReference/API_DeleteTable.md")
- [DescribeBackup](../APIReference/API_DescribeBackup.md "../APIReference/API_DescribeBackup.md")
- [DescribeContinuousBackups](../APIReference/API_DescribeContinuousBackups.md "../APIReference/API_DescribeContinuousBackups.md")
- [DescribeGlobalTable](../APIReference/API_DescribeGlobalTable.md "../APIReference/API_DescribeGlobalTable.md")
- [DescribeLimits](../APIReference/API_DescribeLimits.md "../APIReference/API_DescribeLimits.md")
- [DescribeTable](../APIReference/API_DescribeTable.md "../APIReference/API_DescribeTable.md")
- [DescribeTimeToLive](../APIReference/API_DescribeTimeToLive.md "../APIReference/API_DescribeTimeToLive.md")
- [ListBackups](../APIReference/API_ListBackups.md "../APIReference/API_ListBackups.md")
- [ListTables](../APIReference/API_ListTables.md "../APIReference/API_ListTables.md")
- [ListTagsOfResource](../APIReference/API_ListTagsOfResource.md "../APIReference/API_ListTagsOfResource.md")
- [ListGlobalTables](../APIReference/API_ListGlobalTables.md "../APIReference/API_ListGlobalTables.md")
- [RestoreTableFromBackup](../APIReference/API_RestoreTableFromBackup.md "../APIReference/API_RestoreTableFromBackup.md")
- [RestoreTableToPointInTime](../APIReference/API_RestoreTableToPointInTime.md "../APIReference/API_RestoreTableToPointInTime.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [UpdateGlobalTable](../APIReference/API_UpdateGlobalTable.md "../APIReference/API_UpdateGlobalTable.md")
- [UpdateTable](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md")
- [UpdateTimeToLive](../APIReference/API_UpdateTimeToLive.md "../APIReference/API_UpdateTimeToLive.md")
- [DescribeReservedCapacity](iam-policy-prevent-purchase-reserved-capacity.md "iam-policy-prevent-purchase-reserved-capacity.md")
- [DescribeReservedCapacityOfferings](iam-policy-prevent-purchase-reserved-capacity.md "iam-policy-prevent-purchase-reserved-capacity.md")
- [PurchaseReservedCapacityOfferings](iam-policy-prevent-purchase-reserved-capacity.md "iam-policy-prevent-purchase-reserved-capacity.md")
- [DescribeScalableTargets](../../../autoscaling/application/APIReference/API_DescribeScalableTargets.md "../../../autoscaling/application/APIReference/API_DescribeScalableTargets.md")
- [RegisterScalableTarget](../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md "../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md")

**DynamoDB Streams**

- [DescribeStream](../APIReference/API_streams_DescribeStream.md "../APIReference/API_streams_DescribeStream.md")
- [ListStreams](../APIReference/API_streams_ListStreams.md "../APIReference/API_streams_ListStreams.md")

**DynamoDB Accelerator (DAX)**

- [CreateCluster](../APIReference/API_dax_CreateCluster.md "../APIReference/API_dax_CreateCluster.md")
- [CreateParameterGroup](../APIReference/API_dax_CreateParameterGroup.md "../APIReference/API_dax_CreateParameterGroup.md")
- [CreateSubnetGroup](../APIReference/API_dax_CreateSubnetGroup.md "../APIReference/API_dax_CreateSubnetGroup.md")
- [DecreaseReplicationFactor](../APIReference/API_dax_DecreaseReplicationFactor.md "../APIReference/API_dax_DecreaseReplicationFactor.md")
- [DeleteCluster](../APIReference/API_dax_DeleteCluster.md "../APIReference/API_dax_DeleteCluster.md")
- [DeleteParameterGroup](../APIReference/API_dax_DeleteParameterGroup.md "../APIReference/API_dax_DeleteParameterGroup.md")
- [DeleteSubnetGroup](../APIReference/API_dax_DeleteSubnetGroup.md "../APIReference/API_dax_DeleteSubnetGroup.md")
- [DescribeClusters](../APIReference/API_dax_DescribeClusters.md "../APIReference/API_dax_DescribeClusters.md")
- [DescribeDefaultParameters](../APIReference/API_dax_DescribeDefaultParameters.md "../APIReference/API_dax_DescribeDefaultParameters.md")
- [DescribeEvents](../APIReference/API_dax_DescribeEvents.md "../APIReference/API_dax_DescribeEvents.md")
- [DescribeParameterGroups](../APIReference/API_dax_DescribeParameterGroups.md "../APIReference/API_dax_DescribeParameterGroups.md")
- [DescribeParameters](../APIReference/API_dax_DescribeParameters.md "../APIReference/API_dax_DescribeParameters.md")
- [DescribeSubnetGroups](../APIReference/API_dax_DescribeSubnetGroups.md "../APIReference/API_dax_DescribeSubnetGroups.md")
- [IncreaseReplicationFactor](../APIReference/API_dax_IncreaseReplicationFactor.md "../APIReference/API_dax_IncreaseReplicationFactor.md")
- [ListTags](../APIReference/API_dax_ListTags.md "../APIReference/API_dax_ListTags.md")
- [RebootNode](../APIReference/API_dax_RebootNode.md "../APIReference/API_dax_RebootNode.md")
- [TagResource](../APIReference/API_dax_TagResource.md "../APIReference/API_dax_TagResource.md")
- [UntagResource](../APIReference/API_dax_UntagResource.md "../APIReference/API_dax_UntagResource.md")
- [UpdateCluster](../APIReference/API_dax_UpdateCluster.md "../APIReference/API_dax_UpdateCluster.md")
- [UpdateParameterGroup](../APIReference/API_dax_UpdateParameterGroup.md "../APIReference/API_dax_UpdateParameterGroup.md")
- [UpdateSubnetGroup](../APIReference/API_dax_UpdateSubnetGroup.md "../APIReference/API_dax_UpdateSubnetGroup.md")

### DynamoDB data plane events in CloudTrail

To enable logging of the following API actions in CloudTrail files, you'll need to
enable logging of data plane API activity in CloudTrail.
See [Logging data events for trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") for more information.

Data plane events can be filtered by resource type, for granular control over which DynamoDB API calls you want to
selectively log and pay for in CloudTrail. For example, by specifying `AWS::DynamoDB::Stream` as a resource
type, you can log only calls to the DynamoDB streams APIs. For tables with streams enabled, the resource field in the
data plane event contains both `AWS::DynamoDB::Stream` and `AWS::DynamoDB::Table`. If you
specify `AWS::DynamoDB::Table` as a resource type, it will log both DynamoDB table and DynamoDB streams events
by default. You can add an additional [filter](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") to exclude the streams
events, if you don't want the streams events to be logged. For more information, see [DataResource](../../../awscloudtrail/latest/APIReference/API_DataResource.md "../../../awscloudtrail/latest/APIReference/API_DataResource.md") in the _AWS CloudTrail API Reference_.

**Amazon DynamoDB**

- [BatchExecuteStatement](../APIReference/API_BatchExecuteStatement.md "../APIReference/API_BatchExecuteStatement.md")
- [BatchGetItem](../APIReference/API_BatchGetItem.md "../APIReference/API_BatchGetItem.md")
- [BatchWriteItem](../APIReference/API_BatchWriteItem.md "../APIReference/API_BatchWriteItem.md")
- [DeleteItem](../APIReference/API_DeleteItem.md "../APIReference/API_DeleteItem.md")
- [ExecuteStatement](../APIReference/API_ExecuteStatement.md "../APIReference/API_ExecuteStatement.md")
- [ExecuteTransaction](../APIReference/API_ExecuteTransaction.md "../APIReference/API_ExecuteTransaction.md")
- [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md")
- [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md")
- [Query](../APIReference/API_Query.md "../APIReference/API_Query.md")
- [Scan](../APIReference/API_Scan.md "../APIReference/API_Scan.md")
- [TransactGetItems](../APIReference/API_TransactGetItems.md "../APIReference/API_TransactGetItems.md")
- [TransactWriteItems](../APIReference/API_TransactWriteItems.md "../APIReference/API_TransactWriteItems.md")
- [UpdateItem](../APIReference/API_UpdateItem.md "../APIReference/API_UpdateItem.md")

###### Note

DynamoDB Time to Live data plane actions are not logged by CloudTrail

**DynamoDB Streams**

- [GetRecords](../APIReference/API_streams_GetRecords.md "../APIReference/API_streams_GetRecords.md")
- [GetShardIterator](../APIReference/API_streams_GetShardIterator.md "../APIReference/API_streams_GetShardIterator.md")
