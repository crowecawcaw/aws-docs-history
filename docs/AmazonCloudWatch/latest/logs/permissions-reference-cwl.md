# CloudWatch Logs permissions reference

When you are setting up [Access control](auth-and-access-control-cwl.md#access-control-cwl "auth-and-access-control-cwl.md#access-control-cwl") and writing permissions policies that you
can attach to an IAM identity (identity-based policies), you can use the following
table as a reference. The table lists each CloudWatch Logs API operation and the corresponding
actions for which you can grant permissions to perform the action. You specify the
actions in the policy's `Action` field. For the `Resource`
field, you can specify the ARN of a log group or log stream, or specify
`*` to represent all CloudWatch Logs resources.

You can use AWS-wide condition keys in your CloudWatch Logs policies to express
conditions. For a complete list of AWS-wide keys, see [AWS Global and
IAM Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

###### Note

To specify an action, use the `logs:` prefix followed by the API
operation name. For example: `logs:CreateLogGroup`,
`logs:CreateLogStream`, or `logs:*` (for all CloudWatch Logs
actions).

CloudWatch Logs API operations and required
permissions for actions| CloudWatch Logs API operations | Required permissions (API actions) |
| --- | --- |
| [CancelExportTask](../../../AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.md") | `logs:CancelExportTask` Required to cancel a pending or running export task. |
| [CreateExportTask](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateExportTask.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateExportTask.md") | `logs:CreateExportTask` Required to export data from a log group to an Amazon S3 bucket. |
| [CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md") | `logs:CreateLogGroup` Required to create a new log group. |
| [CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md") | `logs:CreateLogStream` Required to create a new log stream in a log group. |
| [DeleteDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDestination.md") | `logs:DeleteDestination` Required to delete a log destination and disables any subscription filters to it. |
| [DeleteLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.md") | `logs:DeleteLogGroup` Required to delete a log group and any associated archived log events. |
| [DeleteLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogStream.md") | `logs:DeleteLogStream` Required to delete a log stream and any associated archived log events. |
| [DeleteMetricFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteMetricFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteMetricFilter.md") | `logs:DeleteMetricFilter` Required to delete a metric filter associated with a log group. |
| [DeleteQueryDefinition](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteQueryDefinition.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteQueryDefinition.md") | `logs:DeleteQueryDefinition` Required to delete a saved query definition in CloudWatch Logs Insights. |
| [DeleteResourcePolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.md") | `logs:DeleteResourcePolicy` Required to delete a CloudWatch Logs resource policy. |
| [DeleteRetentionPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.md") | `logs:DeleteRetentionPolicy` Required to delete a log group's retention policy. |
| [DeleteSubscriptionFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteSubscriptionFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteSubscriptionFilter.md") | `logs:DeleteSubscriptionFilter` Required to delete the subscription filter associated with a log group. |
| [DescribeDestinations](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDestinations.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDestinations.md") | `logs:DescribeDestinations` Required to view all destinations associated with the account. |
| [DescribeExportTasks](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.md") | `logs:DescribeExportTasks` Required to view all export tasks associated with the account. |
| [DescribeLogGroups](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.md") | `logs:DescribeLogGroups` Required to view all log groups associated with the account. |
| [DescribeLogStreams](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.md") | `logs:DescribeLogStreams` Required to view all log streams associated with a log group. |
| [DescribeMetricFilters](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeMetricFilters.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeMetricFilters.md") | `logs:DescribeMetricFilters` Required to view all metrics associated with a log group. |
| [DescribeQueryDefinitions](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.md") | `logs:DescribeQueryDefinitions` Required to see the list of saved query definitions in CloudWatch Logs Insights. |
| [DescribeQueries](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueries.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueries.md") | `logs:DescribeQueries` Required to see the list of CloudWatch Logs Insights queries that are scheduled, executing, or have recently excecuted. |
| [DescribeResourcePolicies](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeResourcePolicies.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeResourcePolicies.md") | `logs:DescribeResourcePolicies` Required to view a list of CloudWatch Logs resource policies. |
| [DescribeSubscriptionFilters](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.md") | `logs:DescribeSubscriptionFilters` Required to view all subscription filters associated with a log group. |
| [FilterLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.md") | `logs:FilterLogEvents` Required to sort log events by log group filter pattern. |
| [GetLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.md") | `logs:GetLogEvents` Required to retrieve log events from a log stream. |
| [GetLogGroupFields](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.md") | `logs:GetLogGroupFields` Required to retrieve the list of fields that are included in the log events in a log group. |
| [GetLogRecord](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.md") | `logs:GetLogRecord` Required to retrieve the details from a single log event. |
| [GetLogObject](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogObject.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogObject.md") | `logs:GetLogRecord` Required to fetch the content of large portions of log events that have been ingested through the PutOpenTelemetryLogs API. |
| [GetQueryResults](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.md") | `logs:GetQueryResults` Required to retrieve the results of CloudWatch Logs Insights queries. |
| ListEntitiesForLogGroup (CloudWatch console-only permission) | `logs:ListEntitiesForLogGroup` Required to find the entities associated with a log group. Required to explore related logs within the CloudWatch console. |
| ListLogGroupsForEntity (CloudWatch console-only permission) | `logs:ListLogGroupsForEntity` Required to find the log groups associated with an entity. Required to explore related logs within the CloudWatch console. |
| [ListTagsLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsLogGroup.md") | `logs:ListTagsLogGroup` Required to list the tags associated with a log group. |
| [ListLogGroups](../APIReference/API_API_ListLogGroups.md "../APIReference/API_API_ListLogGroups.md") | `logs:DescribeLogGroups` Required to view all log groups associated with the account. |
| [PutDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.md") | `logs:PutDestination` Required to create or update a destination log stream (such as an Kinesis stream). |
| [PutDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.md") | `logs:PutDestinationPolicy` Required to create or update an access policy associated with an existing log destination. |
| [PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md") | `logs:PutLogEvents` Required to upload a batch of log events to a log stream. |
| [PutMetricFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutMetricFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutMetricFilter.md") | `logs:PutMetricFilter` Required to create or update a metric filter and associate it with a log group. |
| [PutQueryDefinition](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.md") | `logs:PutQueryDefinition` Required to save a query in CloudWatch Logs Insights. |
| [PutResourcePolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md") | `logs:PutResourcePolicy` Required to create a CloudWatch Logs resource policy. |
| [PutRetentionPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.md") | `logs:PutRetentionPolicy` Required to set the number of days to keep log events (retention) in a log group. |
| [PutSubscriptionFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.md") | `logs:PutSubscriptionFilter` Required to create or update a subscription filter and associate it with a log group. |
| [StartQuery](../../../AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.md") | `logs:StartQuery` Required to start CloudWatch Logs Insights queries. |
| [StopQuery](../../../AmazonCloudWatchLogs/latest/APIReference/API_StopQuery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_StopQuery.md") | `logs:StopQuery` Required to stop a CloudWatch Logs Insights query that is in progress. |
| [TagLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_TagLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_TagLogGroup.md") | `logs:TagLogGroup` Required to add or update log group tags. |
| [TestMetricFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_TestMetricFilter.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_TestMetricFilter.md") | `logs:TestMetricFilter` Required to test a filter pattern against a sampling of log event messages. |
