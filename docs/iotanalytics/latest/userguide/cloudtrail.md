End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Logging AWS IoT Analytics API calls with AWS CloudTrail

AWS IoT Analytics is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in AWS IoT Analytics. CloudTrail captures a subset of API calls for AWS IoT Analytics as
events, including calls from the AWS IoT Analytics console and from code calls to the AWS IoT Analytics APIs. If you
create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including
events for AWS IoT Analytics. If you don't configure a trail, you can still view the most recent events in
the CloudTrail console in **Event history**. Using the information collected by CloudTrail,
you can determine the request that was made to AWS IoT Analytics, the IP address from which the request was
made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## AWS IoT Analytics information in AWS CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
AWS IoT Analytics, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent
events in your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS IoT Analytics, create a
trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create
a trail in the console, the trail applies to all Regions. The trail logs events from all Regions
in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon the event
data collected in CloudTrail logs. For more information, see:

- [Overview for creating
  a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

AWS IoT Analytics supports logging the following actions as events in CloudTrail log files:

- [CancelPipelineReprocessing](../APIReference/API_CancelPipelineReprocessing.md "../APIReference/API_CancelPipelineReprocessing.md")
- [CreateChannel](../APIReference/API_CreateChannel.md "../APIReference/API_CreateChannel.md")
- [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md")
- [CreateDatasetContent](../APIReference/API_CreateDatasetContent.md "../APIReference/API_CreateDatasetContent.md")
- [CreateDatastore](../APIReference/API_CreateDatastore.md "../APIReference/API_CreateDatastore.md")
- [CreatePipeline](../APIReference/API_CreatePipeline.md "../APIReference/API_CreatePipeline.md")
- [DeleteChannel](../APIReference/API_DeleteChannel.md "../APIReference/API_DeleteChannel.md")
- [DeleteDataset](../APIReference/API_DeleteDataset.md "../APIReference/API_DeleteDataset.md")
- [DeleteDatasetContent](../APIReference/API_DeleteDatasetContent.md "../APIReference/API_DeleteDatasetContent.md")
- [DeleteDatastore](../APIReference/API_DeleteDatastore.md "../APIReference/API_DeleteDatastore.md")
- [DeletePipeline](../APIReference/API_DeletePipeline.md "../APIReference/API_DeletePipeline.md")
- [DescribeChannel](../APIReference/API_DescribeChannel.md "../APIReference/API_DescribeChannel.md")
- [DescribeDataset](../APIReference/API_DescribeDataset.md "../APIReference/API_DescribeDataset.md")
- [DescribeDatastore](../APIReference/API_DescribeDatastore.md "../APIReference/API_DescribeDatastore.md")
- [DescribeLoggingOptions](../APIReference/API_DescribeLoggingOptions.md "../APIReference/API_DescribeLoggingOptions.md")
- [DescribePipeline](../APIReference/API_DescribePipeline.md "../APIReference/API_DescribePipeline.md")
- [GetDatasetContent](../APIReference/API_GetDatasetContent.md "../APIReference/API_GetDatasetContent.md")
- [ListChannels](../APIReference/API_ListChannels.md "../APIReference/API_ListChannels.md")
- [ListDatasets](../APIReference/API_ListDatasets.md "../APIReference/API_ListDatasets.md")
- [ListDatastores](../APIReference/API_ListDatastores.md "../APIReference/API_ListDatastores.md")
- [ListPipelines](../APIReference/API_ListPipelines.md "../APIReference/API_ListPipelines.md")
- [PutLoggingOptions](../APIReference/API_PutLoggingOptions.md "../APIReference/API_PutLoggingOptions.md")
- [RunPipelineActivity](../APIReference/API_RunPipelineActivity.md "../APIReference/API_RunPipelineActivity.md")
- [SampleChannelData](../APIReference/API_SampleChannelData.md "../APIReference/API_SampleChannelData.md")
- [StartPipelineReprocessing](../APIReference/API_StartPipelineReprocessing.md "../APIReference/API_StartPipelineReprocessing.md")
- [UpdateChannel](../APIReference/API_UpdateChannel.md "../APIReference/API_UpdateChannel.md")
- [UpdateDataset](../APIReference/API_UpdateDataset.md "../APIReference/API_UpdateDataset.md")
- [UpdateDatastore](../APIReference/API_UpdateDatastore.md "../APIReference/API_UpdateDatastore.md")
- [UpdatePipeline](../APIReference/API_UpdatePipeline.md "../APIReference/API_UpdatePipeline.md")

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management user credentials.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding AWS IoT Analytics log file

entries

A trail is a configuration that enables delivery of events as log files to an S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files are not an ordered stack trace of
the public API calls, so they do not appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreateChannel` action.

```
{
"eventVersion": "1.05",
"userIdentity": {
"type": "AssumedRole",
"principalId": "ABCDE12345FGHIJ67890B:AnalyticsChannelTestFunction",
"arn": "arn:aws:sts::123456789012:assumed-role/AnalyticsRole/AnalyticsChannelTestFunction",
"accountId": "123456789012",
"accessKeyId": "ABCDE12345FGHIJ67890B",
"sessionContext": {
"attributes": {
	"mfaAuthenticated": "false",
	"creationDate": "2018-02-14T23:43:12Z"
},
"sessionIssuer": {
	"type": "Role",
	"principalId": "ABCDE12345FGHIJ67890B",
	"arn": "arn:aws:iam::123456789012:role/AnalyticsRole",
	"accountId": "123456789012",
	"userName": "AnalyticsRole"
}
}
},
"eventTime": "2018-02-14T23:55:14Z",
"eventSource": "iotanalytics.amazonaws.com",
"eventName": "CreateChannel",
"awsRegion": "us-east-1",
"sourceIPAddress": "198.162.1.0",
"userAgent": "aws-internal/3 exec-env/AWS_Lambda_java8",
"requestParameters": {
"channelName": "channel_channeltest"
},
"responseElements": {
"retentionPeriod": {
"unlimited": true
},
"channelName": "channel_channeltest",
"channelArn": "arn:aws:iotanalytics:us-east-1:123456789012:channel/channel_channeltest"
},
"requestID": "7f871429-11e2-11e8-9eee-0781b5c0ac59",
"eventID": "17885899-6977-41be-a6a0-74bb95a78294",
"eventType": "AwsApiCall",
"recipientAccountId": "123456789012"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`CreateDataset` action.

```
{
"eventVersion": "1.05",
"userIdentity": {
"type": "AssumedRole",
"principalId": "ABCDE12345FGHIJ67890B:AnalyticsDatasetTestFunction",
"arn": "arn:aws:sts::123456789012:assumed-role/AnalyticsRole/AnalyticsDatasetTestFunction",
"accountId": "123456789012",
"accessKeyId": "ABCDE12345FGHIJ67890B",
"sessionContext": {
"attributes": {
	"mfaAuthenticated": "false",
	"creationDate": "2018-02-14T23:41:36Z"
},
"sessionIssuer": {
	"type": "Role",
	"principalId": "ABCDE12345FGHIJ67890B",
	"arn": "arn:aws:iam::123456789012:role/AnalyticsRole",
	"accountId": "123456789012",
	"userName": "AnalyticsRole"
}
}
},
"eventTime": "2018-02-14T23:53:39Z",
"eventSource": "iotanalytics.amazonaws.com",
"eventName": "CreateDataset",
"awsRegion": "us-east-1",
"sourceIPAddress": "198.162.1.0",
"userAgent": "aws-internal/3 exec-env/AWS_Lambda_java8",
"requestParameters": {
"datasetName": "dataset_datasettest"
},
"responseElements": {
"datasetArn": "arn:aws:iotanalytics:us-east-1:123456789012:dataset/dataset_datasettest",
"datasetName": "dataset_datasettest"
},
"requestID": "46ee8dd9-11e2-11e8-979a-6198b668c3f0",
"eventID": "5abe21f6-ee1a-48ef-afc5-c77211235303",
"eventType": "AwsApiCall",
"recipientAccountId": "123456789012"
}
```
