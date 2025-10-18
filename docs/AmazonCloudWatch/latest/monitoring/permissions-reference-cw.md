# Amazon CloudWatch permissions reference

The following table lists each CloudWatch API operation and the corresponding actions for
 which you can grant permissions to perform the action. You specify the actions in the
 policy's `Action` field, and you specify a wildcard character (\*) as the
 resource value in the policy's `Resource` field.

You can use AWS-wide condition keys in your CloudWatch policies to express conditions. For
 a complete list of AWS-wide keys, see [AWS Global and IAM
 Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html") in the *IAM User Guide*.

###### Note

To specify an action, use the `cloudwatch:` prefix followed by the API
 operation name. For example: `cloudwatch:GetMetricData`,
 `cloudwatch:ListMetrics`, or `cloudwatch:*` (for all CloudWatch
 actions).

###### Topics

* [CloudWatch API operations and required permissions
 for actions](#cw-permissions-table "#cw-permissions-table")
* [CloudWatch Application Signals
 API operations and required permissions for actions](#cw-application-signals-permissions-table "#cw-application-signals-permissions-table")
* [CloudWatch Contributor
 Insights API operations and required permissions for actions](#cw-contributor-insights-permissions-table "#cw-contributor-insights-permissions-table")
* [CloudWatch Events API operations and required
 permissions for actions](#cwe-permissions-table "#cwe-permissions-table")
* [CloudWatch Logs API operations and required
 permissions for actions](#cwl-permissions-table "#cwl-permissions-table")
* [Amazon EC2 API operations and required
 permissions for actions](#cw-ec2-permissions-table "#cw-ec2-permissions-table")
* [Amazon EC2 Auto Scaling API operations and required
 permissions for actions](#cw-as-permissions-table "#cw-as-permissions-table")

## CloudWatch API operations and required permissions
 for actions




| CloudWatch API operations | Required permissions (API actions) |
| --- | --- |
| [DeleteAlarms](../APIReference/API_DeleteAlarms.md "../APIReference/API_DeleteAlarms.md") | `cloudwatch:DeleteAlarms` Required to delete an alarm. |
| [DeleteDashboards](../APIReference/API_DeleteDashboards.md "../APIReference/API_DeleteDashboards.md") | `cloudwatch:DeleteDashboards` Required to delete a dashboard. |
| [DeleteMetricStream](../APIReference/API_DeleteMetricStream.md "../APIReference/API_DeleteMetricStream.md") | `cloudwatch:DeleteMetricStream` Required to delete a metric stream. |
| [DescribeAlarmHistory](../APIReference/API_DescribeAlarmHistory.md "../APIReference/API_DescribeAlarmHistory.md") | `cloudwatch:DescribeAlarmHistory` Required to view alarm history. To retrieve information about composite alarms, your `cloudwatch:DescribeAlarmHistory` permission must have a `*` scope. You can't return information about composite alarms if your `cloudwatch:DescribeAlarmHistory` permission has a narrower scope. |
| [DescribeAlarms](../APIReference/API_DescribeAlarms.md "../APIReference/API_DescribeAlarms.md") | `cloudwatch:DescribeAlarms` Required to retrieve information about alarms. To retrieve information about composite alarms, your `cloudwatch:DescribeAlarms` permission must have a `*` scope. You can't return information about composite alarms if your `cloudwatch:DescribeAlarms` permission has a narrower scope. |
| [DescribeAlarmsForMetric](../APIReference/API_DescribeAlarmsForMetric.md "../APIReference/API_DescribeAlarmsForMetric.md") | `cloudwatch:DescribeAlarmsForMetric` Required to view alarms for a metric. |
| [DisableAlarmActions](../APIReference/API_DisableAlarmActions.md "../APIReference/API_DisableAlarmActions.md") | `cloudwatch:DisableAlarmActions` Required to disable an alarm action. |
| [EnableAlarmActions](../APIReference/API_EnableAlarmActions.md "../APIReference/API_EnableAlarmActions.md") | `cloudwatch:EnableAlarmActions` Required to enable an alarm action. |
| [GetDashboard](../APIReference/API_GetDashboard.md "../APIReference/API_GetDashboard.md") | `cloudwatch:GetDashboard` Required to display data about existing dashboards. |
| [GetMetricData](../APIReference/API_GetMetricData.md "../APIReference/API_GetMetricData.md") | `cloudwatch:GetMetricData` Required to graph metric data in the CloudWatch console, to retrieve large batches of metric data, and perform metric math on that data. |
| [GetMetricStatistics](../APIReference/API_GetMetricStatistics.md "../APIReference/API_GetMetricStatistics.md") | `cloudwatch:GetMetricStatistics` Required to view graphs in other parts of the CloudWatch console and in dashboard widgets. |
| [GetMetricStream](../APIReference/API_GetMetricStream.md "../APIReference/API_GetMetricStream.md") | `cloudwatch:GetMetricStream` Required to view information about a metric stream. |
| [GetMetricWidgetImage](../APIReference/API_GetMetricWidgetImage.md "../APIReference/API_GetMetricWidgetImage.md") | `cloudwatch:GetMetricWidgetImage` Required to retrieve a snapshot graph of one or more CloudWatch metrics as a bitmap image. |
| [ListDashboards](../APIReference/API_ListDashboards.md "../APIReference/API_ListDashboards.md") | `cloudwatch:ListDashboards` Required to view the list of CloudWatch dashboards in your account. |
| ListEntitiesForMetric (CloudWatch console-only permission) | `cloudwatch:ListEntitiesForMetric` Required to find the entities associated with a metric. Required to explore related telemetry within the CloudWatch console. |
| [ListMetrics](../APIReference/API_ListMetrics.md "../APIReference/API_ListMetrics.md") | `cloudwatch:ListMetrics` Required to view or search metric names within the CloudWatch console and in the CLI. Required to select metrics on dashboard widgets. |
| [ListMetricStreams](../APIReference/API_ListMetricStreams.md "../APIReference/API_ListMetricStreams.md") | `cloudwatch:ListMetricStreams` Required to view or search the list of metric streams in the account. |
| [PutCompositeAlarm](../APIReference/API_PutCompositeAlarm.md "../APIReference/API_PutCompositeAlarm.md") | `cloudwatch:PutCompositeAlarm` Required to create a composite alarm. To create a composite alarm, your `cloudwatch:PutCompositeAlarm` permission must have a `*` scope. You can't return information about composite alarms if your `cloudwatch:PutCompositeAlarm` permission has a narrower scope. |
| [PutDashboard](../APIReference/API_PutDashboard.md "../APIReference/API_PutDashboard.md") | `cloudwatch:PutDashboard` Required to create a dashboard or update an existing dashboard. |
| [PutMetricAlarm](../APIReference/API_PutMetricAlarm.md "../APIReference/API_PutMetricAlarm.md") | `cloudwatch:PutMetricAlarm` Required to create or update an alarm. |
| [PutMetricData](../APIReference/API_PutMetricData.md "../APIReference/API_PutMetricData.md") | `cloudwatch:PutMetricData` Required to create metrics. |
| [PutMetricStream](../APIReference/API_PutMetricStream.md "../APIReference/API_PutMetricStream.md") | `cloudwatch:PutMetricStream` Required to create a metric stream. |
| [SetAlarmState](../APIReference/API_SetAlarmState.md "../APIReference/API_SetAlarmState.md") | `cloudwatch:SetAlarmState` Required to manually set an alarm's state. |
| [StartMetricStreams](../APIReference/API_StartMetricStreams.md "../APIReference/API_StartMetricStreams.md") | `cloudwatch:StartMetricStreams` Required to start the flow of metrics in a metric stream. |
| [StopMetricStreams](../APIReference/API_StartMetricStreams.md "../APIReference/API_StartMetricStreams.md") | `cloudwatch:StopMetricStreams` Required to temporarily stop the flow of metrics in a metric stream. |
| [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") | `cloudwatch:TagResource` Required to add or update tags on CloudWatch resources such as alarms and Contributor Insights rules. |
| [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") | `cloudwatch:UntagResource` Required to remove tags from CloudWatch resources . | ## CloudWatch Application Signals API operations and required permissions for actions
| CloudWatch Application Signals API operations | Required permissions (API actions) |
| --- | --- |
|  [BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html") | `application-signals:BatchGetServiceLevelObjectiveBudgetReport` Required to retrieve service level objective budget reports. |
|  [CreateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html") | `application-signals:CreateServiceLevelObjective` Required to create a service level objective (SLO). |
|  [DeleteServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html") | `application-signals:DeleteServiceLevelObjective` Required to delete a service level objective (SLO). |
|  [GetService](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html") | `application-signals:GetService` Required to retrieve information about a service discovered by Application Signals. |
|  [GetServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetServiceLevelObjective.html") | `application-signals:GetServiceLevelObjective` Required to retrieve information about a service level objective (SLO). |
| ListObservedEntities | `application-signals:ListObservedEntities` Grants permission to list entities that are associated with other entities. |
|  [ListServiceDependencies](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html") | `application-signals:ListServiceDependencies` Required to retrieve a list of service dependencies of a service that you specify. This service and the dependencies were discovered by Application Signals. |
|  [ListServiceDependents](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependents.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependents.html") | `application-signals:ListServiceDependents` Required to retrieve a list of dependents that invoked a service that you specify. This service and the dependents were discovered by Application Signals. |
|  [ListServiceLevelObjectives](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html") | `application-signals:ListServiceLevelObjectives` Required to retrieve a list of service level objectives (SLOs) in the account. |
|  [ListServiceOperations](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceOperations.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceOperations.html") | `application-signals:ListServiceOperations` Required to retrieve a list of service operations of a service that you specify. This service and the dependencies were discovered by Application Signals. |
|  [ListServices](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html") | `application-signals:ListServices` Required to retrieve a list of services discovered by Application Signals. |
|  [ListTagsForResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListTagsForResource.html") | `application-signals:ListTagsForResource` Required to retrieve a list of the tags associated with a resource. |
|  [StartDiscovery](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html") | `application-signals:StartDiscovery` Required to be able to enable Application Signals in the account and create the required service-linked role. |
|  [TagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_TagResource.html") | `application-signals:TagResource` Required to be able to add tags to resources. |
|  [UntagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html") | `application-signals:UntagResource` Required to be able to remove tags from resources. |
|  [UpdateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html") | `application-signals:UpdateServiceLevelObjective` Required to update an existing service level objective | ## CloudWatch Contributor Insights API operations and required permissions for actions ###### Important When you grant a user the `cloudwatch:PutInsightRule` permission, by default that user can create a rule that evaluates any log group in CloudWatch Logs. You can add IAM policy conditions that limit these permissions for a user to include and exclude specific log groups. For more information, see [Using condition keys to limit Contributor Insights users' access to log groups](iam-cw-condition-keys-contributor.md "iam-cw-condition-keys-contributor.md").
| CloudWatch Contributor Insights API operations | Required permissions (API actions) |
| --- | --- |
| [DeleteInsightRules](../APIReference/API_DeleteInsightRules.md "../APIReference/API_DeleteInsightRules.md") | `cloudwatch:DeleteInsightRules` Required to delete Contributor Insights rules. |
| [DescribeInsightRules](../APIReference/API_DescribeInsightRules.md "../APIReference/API_DescribeInsightRules.md") | `cloudwatch:DescribeInsightRules` Required to view the Contributor Insights rules in your account. |
| [EnableInsightRules](../APIReference/API_EnableInsightRules.md "../APIReference/API_EnableInsightRules.md") | `cloudwatch:EnableInsightRules` Required to enable Contributor Insights rules. |
| [GetInsightRuleReport](../APIReference/API_GetInsightRuleReport.md "../APIReference/API_GetInsightRuleReport.md") | `cloudwatch:GetInsightRuleReport` Required to retrieve time series data and other statistics collectd by Contributor Insights rules. |
| [PutInsightRule](../APIReference/API_PutInsightRule.md "../APIReference/API_PutInsightRule.md") | `cloudwatch:PutInsightRule` Required to create Contributor Insights rules. See the **Important** note at the beginning of this table. | ## CloudWatch Events API operations and required permissions for actions
| CloudWatch Events API operations | Required permissions (API actions) |
| --- | --- |
| [DeleteRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DeleteRule.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DeleteRule.html") | `events:DeleteRule` Required to delete a rule. |
| [DescribeRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DescribeRule.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DescribeRule.html") | `events:DescribeRule` Required to list the details about a rule. |
| [DisableRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DisableRule.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DisableRule.html") | `events:DisableRule` Required to disable a rule. |
| [EnableRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_EnableRule.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_EnableRule.html") | `events:EnableRule` Required to enable a rule. |
| [ListRuleNamesByTarget](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRuleNamesByTarget.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRuleNamesByTarget.html") | `events:ListRuleNamesByTarget` Required to list rules associated with a target. |
| [ListRules](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRules.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRules.html") | `events:ListRules` Required to list all rules in your account. |
| [ListTargetsByRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListTargetsByRule.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListTargetsByRule.html") | `events:ListTargetsByRule` Required to list all targets associated with a rule. |
| [PutEvents](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutEvents.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutEvents.html") | `events:PutEvents` Required to add custom events that can be matched to rules. |
| [PutRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutRule.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutRule.html") | `events:PutRule` Required to create or update a rule. |
| [PutTargets](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutTargets.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutTargets.html") | `events:PutTargets` Required to add targets to a rule. |
| [RemoveTargets](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_RemoveTargets.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_RemoveTargets.html") | `events:RemoveTargets` Required to remove a target from a rule. |
| [TestEventPattern](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_TestEventPattern.html "https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_TestEventPattern.html") | `events:TestEventPattern` Required to test an event pattern against a given event. | ## CloudWatch Logs API operations and required permissions for actions ###### Note CloudWatch Logs permissions can be found in the [CloudWatch Logs user guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html"). ## Amazon EC2 API operations and required permissions for actions
| Amazon EC2 API operations | Required permissions (API actions) |
| --- | --- |
| [DescribeInstanceStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html") | `ec2:DescribeInstanceStatus` Required to view EC2 instance status details. |
| [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html") | `ec2:DescribeInstances` Required to view EC2 instance details. |
| [RebootInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html") | `ec2:RebootInstances` Required to reboot an EC2 instance. |
| [StopInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html") | `ec2:StopInstances` Required to stop an EC2 instance. |
| [TerminateInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html") | `ec2:TerminateInstances` Required to terminate an EC2 instance. | ## Amazon EC2 Auto Scaling API operations and required permissions for actions
| Amazon EC2 Auto Scaling API operations | Required permissions (API actions) |
| --- | --- |
| Scaling | `autoscaling:Scaling` Required to scale an Auto Scaling group. |
| Trigger | `autoscaling:Trigger` Required to trigger an Auto Scaling action. |
