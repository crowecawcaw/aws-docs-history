# Neptune Analytics information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported event activity occurs in Neptune Analytics,
that activity is recorded in a CloudTrail event along with other AWS service events in the
**Event history** section. You can view, search, and download recent events in
your AWS account. For more information, see
[Viewing events with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Neptune Analytics, create a trail. A trail enables
CloudTrail to deliver log files to an Amazon S3. By default, when you create a trail in the console, the trail applies to all
AWS regions. The trail logs events from all regions in the AWS partition and delivers the log files to the
Amazon S3 that you specify. Additionally, you can configure other AWS services to further analyze and act upon the
event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and
  [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## Logging Neptune Analytics API calls using AWS CloudTrail

Neptune Analytics is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service
in Neptune Analytics. CloudTrail captures all API calls for Neptune Analytics as events. The calls captured include calls from the Neptune Analytics console and
code calls to the Neptune Analytics API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for Neptune Analytics. If you don't configure a trail, you can still view the most recent management
events in the CloudTrail console in the **Event history** section. Using the information
collected by CloudTrail, you can determine the request that was made to Neptune Analytics, the IP address from which the request was
made, who made the request, when it was made, and additional details.

For robust monitoring and alerting, you can also integrate CloudTrail events with
[Amazon CloudWatch logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").
To enhance your analysis of Neptune Analytics service activity and identify changes in activities for an AWS account, you
can query AWS CloudTrail logs using [Amazon Athena](../../../athena/latest/ug/cloudtrail-logs.md "../../../athena/latest/ug/cloudtrail-logs.md").
For example, you can use queries to identify trends and further isolate activity by attributes such as source IP
address or user.

To learn more about CloudTrail, including how to configure and enable it, see the
[AWS CloudTrail user guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Control plane events in CloudTrail

The following control plane API actions are logged by default as events in CloudTrail:

- [CreateGraph](../apiref/API_CreateGraph.md "../apiref/API_CreateGraph.md")
- [ListGraphs](../apiref/API_ListGraphs.md "../apiref/API_ListGraphs.md")
- [GetGraph](../apiref/API_GetGraph.md "../apiref/API_GetGraph.md")
- [UpdateGraph](../apiref/API_UpdateGraph.md "../apiref/API_UpdateGraph.md")
- [ResetGraph](../apiref/API_ResetGraph.md "../apiref/API_ResetGraph.md")
- [DeleteGraph](../apiref/API_DeleteGraph.md "../apiref/API_DeleteGraph.md")
- [CreateGraphUsingImportTask](../apiref/API_CreateGraphUsingImportTask.md "../apiref/API_CreateGraphUsingImportTask.md")
- [ListImportTasks](../apiref/API_ListImportTasks.md "../apiref/API_ListImportTasks.md")
- [GetImportTask](../apiref/API_GetImportTask.md "../apiref/API_GetImportTask.md")
- [CancelImportTask](../apiref/API_CancelImportTask.md "../apiref/API_CancelImportTask.md")
- [CreatePrivateGraphEndpoint](../apiref/API_CreatePrivateGraphEndpoint.md "../apiref/API_CreatePrivateGraphEndpoint.md")
- [ListPrivateGraphEndpoints](../apiref/API_ListPrivateGraphEndpoints.md "../apiref/API_ListPrivateGraphEndpoints.md")
- [GetPrivateGraphEndpoint](../apiref/API_GetPrivateGraphEndpoint.md "../apiref/API_GetPrivateGraphEndpoint.md")
- [DeletePrivateGraphEndpoint](../apiref/API_DeletePrivateGraphEndpoint.md "../apiref/API_DeletePrivateGraphEndpoint.md")
- [CreateGraphSnapshot](../apiref/API_CreateGraphSnapshot.md "../apiref/API_CreateGraphSnapshot.md")
- [ListGraphSnapshots](../apiref/API_ListGraphSnapshots.md "../apiref/API_ListGraphSnapshots.md")
- [GetGraphSnapshot](../apiref/API_GetGraphSnapshot.md "../apiref/API_GetGraphSnapshot.md")
- [RestoreGraphFromSnapshot](../apiref/API_RestoreGraphFromSnapshot.md "../apiref/API_RestoreGraphFromSnapshot.md")
- [DeleteGraphSnapshot](../apiref/API_DeleteGraphSnapshot.md "../apiref/API_DeleteGraphSnapshot.md")
- [TagResource](../apiref/API_TagResource.md "../apiref/API_TagResource.md")
- [ListTagsForResource](../apiref/API_ListTagsForResource.md "../apiref/API_ListTagsForResource.md")
- [UntagResource](../apiref/API_UntagResource.md "../apiref/API_UntagResource.md")

## Data plane events in CloudTrail

To enable logging of the following API actions in CloudTrail, you'll need to enable logging of data plane API
activity in CloudTrail. See [Logging data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md")
for more information. By default, CloudTrail doesn't log data events.

###### Note

Additional charges apply for data events. For more information, see
[AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

Data plane events can be filtered by resource type for granular control over which Neptune Analytics API calls you want
to selectively log and pay for in CloudTrail. For example, by specifying `AWS::NeptuneGraph::Graph` as a
resource type, you can log only calls to the Neptune Analytics APIs. You can add an additional
[filter](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") to exclude some
events if you don't want them to be logged. For more information, see
[AdvancedFieldSelectors](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md")
in the
[AWS CloudTrail API reference](../../../awscloudtrail/latest/APIReference.md "../../../awscloudtrail/latest/APIReference.md").

Neptune Analytics logs the following data plane API actions as data events:

- [GetGraphSummary](../apiref/API_GetGraphSummary.md "../apiref/API_GetGraphSummary.md")
- [ExecuteQuery](../apiref/API_ExecuteQuery.md "../apiref/API_ExecuteQuery.md")
- [GetQuery](../apiref/API_GetQuery.md "../apiref/API_GetQuery.md")
- [ListQueries](../apiref/API_ListQueries.md "../apiref/API_ListQueries.md")
- [CancelQuery](../apiref/API_CancelQuery.md "../apiref/API_CancelQuery.md")
