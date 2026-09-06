

# Neptune Analytics information in CloudTrail
<a name="monitoring-cloudtrail-info"></a>

 CloudTrail is enabled on your AWS account when you create the account. When supported event activity occurs in Neptune Analytics, that activity is recorded in a CloudTrail event along with other AWS service events in the **Event history** section. You can view, search, and download recent events in your AWS account. For more information, see [ Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

 For an ongoing record of events in your AWS account, including events for Neptune Analytics, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3. By default, when you create a trail in the console, the trail applies to all AWS regions. The trail logs events from all regions in the AWS partition and delivers the log files to the Amazon S3 that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+  [ Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) 
+  [ CloudTrail supported services and integrations ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations) 
+  [ Configuring Amazon SNS notifications for CloudTrail ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html) 
+  [ Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [ Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 

## Logging Neptune Analytics API calls using AWS CloudTrail
<a name="monitoring-cloudtrail"></a>

 Neptune Analytics is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Neptune Analytics. CloudTrail captures all API calls for Neptune Analytics as events. The calls captured include calls from the Neptune Analytics console and code calls to the Neptune Analytics API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Neptune Analytics. If you don't configure a trail, you can still view the most recent management events in the CloudTrail console in the **Event history** section. Using the information collected by CloudTrail, you can determine the request that was made to Neptune Analytics, the IP address from which the request was made, who made the request, when it was made, and additional details. 

 For robust monitoring and alerting, you can also integrate CloudTrail events with [Amazon CloudWatch logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). To enhance your analysis of Neptune Analytics service activity and identify changes in activities for an AWS account, you can query AWS CloudTrail logs using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html). For example, you can use queries to identify trends and further isolate activity by attributes such as source IP address or user. 

 To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail user guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/). 

## Control plane events in CloudTrail
<a name="monitoring-cloudtrail-info-cp"></a>

 The following control plane API actions are logged by default as events in CloudTrail: 
+  [ CreateGraph ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraph.html) 
+  [ ListGraphs ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListGraphs.html) 
+  [ GetGraph ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraph.html) 
+  [ UpdateGraph ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UpdateGraph.html) 
+  [ ResetGraph ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ResetGraph.html) 
+  [ DeleteGraph ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraph.html) 
+  [ CreateGraphUsingImportTask ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphUsingImportTask.html) 
+  [ ListImportTasks ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListImportTasks.html) 
+  [ GetImportTask ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetImportTask.html) 
+  [ CancelImportTask ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelImportTask.html) 
+  [ CreatePrivateGraphEndpoint ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreatePrivateGraphEndpoint.html) 
+  [ ListPrivateGraphEndpoints ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListPrivateGraphEndpoints.html) 
+  [ GetPrivateGraphEndpoint ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetPrivateGraphEndpoint.html) 
+  [ DeletePrivateGraphEndpoint ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeletePrivateGraphEndpoint.html) 
+  [ CreateGraphSnapshot ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphSnapshot.html) 
+  [ ListGraphSnapshots ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListGraphSnapshots.html) 
+  [ GetGraphSnapshot ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraphSnapshot.html) 
+  [ RestoreGraphFromSnapshot ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_RestoreGraphFromSnapshot.html) 
+  [ DeleteGraphSnapshot ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraphSnapshot.html) 
+  [ TagResource ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_TagResource.html) 
+  [ ListTagsForResource ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListTagsForResource.html) 
+  [ UntagResource ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UntagResource.html) 

## Data plane events in CloudTrail
<a name="monitoring-cloudtrail-info-dp"></a>

 To enable logging of the following API actions in CloudTrail, you'll need to enable logging of data plane API activity in CloudTrail. See [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) for more information. By default, CloudTrail doesn't log data events. 

**Note**  
 Additional charges apply for data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/). 

 Data plane events can be filtered by resource type for granular control over which Neptune Analytics API calls you want to selectively log and pay for in CloudTrail. For example, by specifying `AWS::NeptuneGraph::Graph` as a resource type, you can log only calls to the Neptune Analytics APIs. You can add an additional [filter](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) to exclude some events if you don't want them to be logged. For more information, see [AdvancedFieldSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the [AWS CloudTrail API reference](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/). 

 Neptune Analytics logs the following data plane API actions as data events: 
+  [ GetGraphSummary ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraphSummary.html) 
+  [ ExecuteQuery ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExecuteQuery.html) 
+  [ GetQuery ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetQuery.html) 
+  [ ListQueries ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListQueries.html) 
+  [ CancelQuery ](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelQuery.html) 