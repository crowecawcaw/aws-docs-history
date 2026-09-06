

# Amazon CloudWatch permissions reference
<a name="permissions-reference-cw"></a>

The following table lists each CloudWatch API operation and the corresponding actions for which you can grant permissions to perform the action. You specify the actions in the policy's `Action` field, and you specify a wildcard character (\*) as the resource value in the policy's `Resource` field.

You can use AWS-wide condition keys in your CloudWatch policies to express conditions. For a complete list of AWS-wide keys, see [AWS Global and IAM Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

**Note**  
To specify an action, use the `cloudwatch:` prefix followed by the API operation name. For example: `cloudwatch:GetMetricData`, `cloudwatch:ListMetrics`, or `cloudwatch:*` (for all CloudWatch actions).

**Topics**
+ [CloudWatch API operations and required permissions for actions](#cw-permissions-table)
+ [CloudWatch Application Signals API operations and required permissions for actions](#cw-application-signals-permissions-table)
+ [CloudWatch Contributor Insights API operations and required permissions for actions](#cw-contributor-insights-permissions-table)
+ [CloudWatch Events API operations and required permissions for actions](#cwe-permissions-table)
+ [CloudWatch Logs API operations and required permissions for actions](#cwl-permissions-table)
+ [Amazon EC2 API operations and required permissions for actions](#cw-ec2-permissions-table)
+ [Amazon EC2 Auto Scaling API operations and required permissions for actions](#cw-as-permissions-table)

## CloudWatch API operations and required permissions for actions
<a name="cw-permissions-table"></a>


| CloudWatch API operations | Required permissions (API actions) | 
| --- | --- | 
| [DeleteAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarms.html) | `cloudwatch:DeleteAlarms`<br />Required to delete an alarm. | 
| [DeleteDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteDashboards.html) | `cloudwatch:DeleteDashboards`<br />Required to delete a dashboard. | 
| [DeleteMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteMetricStream.html) | `cloudwatch:DeleteMetricStream`<br />Required to delete a metric stream. | 
| [DescribeAlarmHistory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html) | `cloudwatch:DescribeAlarmHistory`<br />Required to view alarm history. To retrieve information about composite alarms, your `cloudwatch:DescribeAlarmHistory` permission must have a `*` scope. You can't return information about composite alarms if your `cloudwatch:DescribeAlarmHistory` permission has a narrower scope. | 
| [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) | `cloudwatch:DescribeAlarms`<br />Required to retrieve information about alarms.<br />To retrieve information about composite alarms, your `cloudwatch:DescribeAlarms` permission must have a `*` scope. You can't return information about composite alarms if your `cloudwatch:DescribeAlarms` permission has a narrower scope. | 
| [DescribeAlarmsForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html) | `cloudwatch:DescribeAlarmsForMetric`<br />Required to view alarms for a metric. | 
| [DisableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableAlarmActions.html) | `cloudwatch:DisableAlarmActions`<br />Required to disable an alarm action. | 
| [EnableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableAlarmActions.html) | `cloudwatch:EnableAlarmActions`<br />Required to enable an alarm action. | 
| [GetDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDashboard.html) | `cloudwatch:GetDashboard`<br />Required to display data about existing dashboards. | 
| [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) | `cloudwatch:GetMetricData`<br />Required to graph metric data in the CloudWatch console, to retrieve large batches of metric data, and perform metric math on that data. | 
| [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) | `cloudwatch:GetMetricStatistics`<br />Required to view graphs in other parts of the CloudWatch console and in dashboard widgets. | 
| [GetMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStream.html) | `cloudwatch:GetMetricStream`<br />Required to view information about a metric stream. | 
| [GetMetricWidgetImage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricWidgetImage.html) | `cloudwatch:GetMetricWidgetImage`<br />Required to retrieve a snapshot graph of one or more CloudWatch metrics as a bitmap image. | 
| [GetOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetOTelEnrichment.html) | `cloudwatch:GetOTelEnrichment`<br />Required to retrieve the status of OpenTelemetry enrichment for vended metrics. | 
| [ListDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html) | `cloudwatch:ListDashboards`<br />Required to view the list of CloudWatch dashboards in your account. | 
| ListEntitiesForMetric<br />(CloudWatch console-only permission) | `cloudwatch:ListEntitiesForMetric`<br />Required to find the entities associated with a metric. Required to explore related telemetry within the CloudWatch console. | 
| [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) | `cloudwatch:ListMetrics`<br />Required to view or search metric names within the CloudWatch console and in the CLI. Required to select metrics on dashboard widgets. | 
| [ListMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetricStreams.html) | `cloudwatch:ListMetricStreams`<br />Required to view or search the list of metric streams in the account. | 
| [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.html) | `cloudwatch:ListTagsForResource`<br />Required to list the tags associated with a CloudWatch resource. | 
| [PutCompositeAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html) | `cloudwatch:PutCompositeAlarm`<br />Required to create a composite alarm.<br />To create a composite alarm, your `cloudwatch:PutCompositeAlarm` permission must have a `*` scope. You can't return information about composite alarms if your `cloudwatch:PutCompositeAlarm` permission has a narrower scope. | 
| [PutDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutDashboard.html) | `cloudwatch:PutDashboard`<br />Required to create a dashboard or update an existing dashboard. | 
| [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) | `cloudwatch:PutMetricAlarm`<br />Required to create or update an alarm. | 
| [PutMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html) | `cloudwatch:PutMetricData`<br />Required to create metrics. | 
| [PutMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricStream.html) | `cloudwatch:PutMetricStream`<br />Required to create a metric stream. | 
| [SetAlarmState](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_SetAlarmState.html) | `cloudwatch:SetAlarmState`<br />Required to manually set an alarm's state. | 
| [StartMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartMetricStreams.html) | `cloudwatch:StartMetricStreams`<br />Required to start the flow of metrics in a metric stream. | 
| [StartOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html) | `cloudwatch:StartOTelEnrichment`<br />Required to enable OpenTelemetry enrichment for vended metrics, making them queryable via PromQL. | 
| [StopMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartMetricStreams.html) | `cloudwatch:StopMetricStreams`<br />Required to temporarily stop the flow of metrics in a metric stream. | 
| [StopOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StopOTelEnrichment.html) | `cloudwatch:StopOTelEnrichment`<br />Required to disable OpenTelemetry enrichment for vended metrics. | 
| [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) | `cloudwatch:TagResource`<br />Required to add or update tags on CloudWatch resources such as alarms and Contributor Insights rules. | 
| [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html) | `cloudwatch:UntagResource`<br />Required to remove tags from CloudWatch resources . | 

## CloudWatch Application Signals API operations and required permissions for actions
<a name="cw-application-signals-permissions-table"></a>


| CloudWatch Application Signals API operations | Required permissions (API actions) | 
| --- | --- | 
| [ BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html) | `application-signals:BatchGetServiceLevelObjectiveBudgetReport`<br />Required to retrieve service level objective budget reports. | 
| [ CreateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html) | `application-signals:CreateServiceLevelObjective`<br />Required to create a service level objective (SLO). | 
| [ DeleteServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html) | `application-signals:DeleteServiceLevelObjective`<br />Required to delete a service level objective (SLO). | 
| [ GetService](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html) | `application-signals:GetService`<br />Required to retrieve information about a service discovered by Application Signals. | 
| [ GetServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetServiceLevelObjective.html) | `application-signals:GetServiceLevelObjective`<br />Required to retrieve information about a service level objective (SLO). | 
| ListObservedEntities | `application-signals:ListObservedEntities`<br />Grants permission to list entities that are associated with other entities. | 
| [ ListServiceDependencies](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html) | `application-signals:ListServiceDependencies`<br />Required to retrieve a list of service dependencies of a service that you specify. This service and the dependencies were discovered by Application Signals. | 
| [ ListServiceDependents](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependents.html) | `application-signals:ListServiceDependents`<br />Required to retrieve a list of dependents that invoked a service that you specify. This service and the dependents were discovered by Application Signals. | 
| [ ListServiceLevelObjectives](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html) | `application-signals:ListServiceLevelObjectives`<br />Required to retrieve a list of service level objectives (SLOs) in the account. | 
| [ ListServiceOperations](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceOperations.html) | `application-signals:ListServiceOperations`<br />Required to retrieve a list of service operations of a service that you specify. This service and the dependencies were discovered by Application Signals. | 
| [ ListServices](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html) | `application-signals:ListServices`<br />Required to retrieve a list of services discovered by Application Signals. | 
| [ ListTagsForResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListTagsForResource.html) | `application-signals:ListTagsForResource`<br />Required to retrieve a list of the tags associated with a resource. | 
| [ StartDiscovery](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html) | `application-signals:StartDiscovery`<br />Required to be able to enable Application Signals in the account and create the required service-linked role. | 
| [ TagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_TagResource.html) | `application-signals:TagResource`<br />Required to be able to add tags to resources. | 
| [ UntagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html) | `application-signals:UntagResource`<br />Required to be able to remove tags from resources. | 
| [ UpdateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html) | `application-signals:UpdateServiceLevelObjective`<br />Required to update an existing service level objective | 

## CloudWatch Contributor Insights API operations and required permissions for actions
<a name="cw-contributor-insights-permissions-table"></a>

**Important**  
When you grant a user the `cloudwatch:PutInsightRule` permission, by default that user can create a rule that evaluates any log group in CloudWatch Logs. You can add IAM policy conditions that limit these permissions for a user to include and exclude specific log groups. For more information, see [Condition keys for Contributor Insights log group access](iam-cw-condition-keys-contributor.md).


| CloudWatch Contributor Insights API operations | Required permissions (API actions) | 
| --- | --- | 
| [DeleteInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteInsightRules.html) | `cloudwatch:DeleteInsightRules`<br />Required to delete Contributor Insights rules. | 
| [DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html) | `cloudwatch:DescribeInsightRules`<br />Required to view the Contributor Insights rules in your account. | 
| [EnableInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableInsightRules.html) | `cloudwatch:EnableInsightRules`<br />Required to enable Contributor Insights rules. | 
| [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html) | `cloudwatch:GetInsightRuleReport`<br />Required to retrieve time series data and other statistics collectd by Contributor Insights rules. | 
| [PutInsightRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutInsightRule.html) | `cloudwatch:PutInsightRule`<br />Required to create Contributor Insights rules. See the **Important** note at the beginning of this table. | 

## CloudWatch Events API operations and required permissions for actions
<a name="cwe-permissions-table"></a>


| CloudWatch Events API operations | Required permissions (API actions) | 
| --- | --- | 
| [DeleteRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DeleteRule.html) | `events:DeleteRule`<br />Required to delete a rule. | 
| [DescribeRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DescribeRule.html) | `events:DescribeRule`<br />Required to list the details about a rule. | 
| [DisableRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DisableRule.html) | `events:DisableRule`<br />Required to disable a rule. | 
| [EnableRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_EnableRule.html) | `events:EnableRule`<br />Required to enable a rule. | 
| [ListRuleNamesByTarget](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRuleNamesByTarget.html) | `events:ListRuleNamesByTarget`<br />Required to list rules associated with a target. | 
| [ListRules](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRules.html) | `events:ListRules`<br />Required to list all rules in your account. | 
| [ListTargetsByRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListTargetsByRule.html) | `events:ListTargetsByRule`<br />Required to list all targets associated with a rule. | 
| [PutEvents](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutEvents.html) | `events:PutEvents`<br />Required to add custom events that can be matched to rules. | 
| [PutRule](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutRule.html) | `events:PutRule`<br />Required to create or update a rule. | 
| [PutTargets](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutTargets.html) | `events:PutTargets`<br />Required to add targets to a rule. | 
| [RemoveTargets](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_RemoveTargets.html) | `events:RemoveTargets`<br />Required to remove a target from a rule. | 
| [TestEventPattern](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_TestEventPattern.html) | `events:TestEventPattern`<br />Required to test an event pattern against a given event. | 

## CloudWatch Logs API operations and required permissions for actions
<a name="cwl-permissions-table"></a>

**Note**  
CloudWatch Logs permissions can be found in the [CloudWatch Logs user guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html).

## Amazon EC2 API operations and required permissions for actions
<a name="cw-ec2-permissions-table"></a>


| Amazon EC2 API operations | Required permissions (API actions) | 
| --- | --- | 
| [DescribeInstanceStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html) | `ec2:DescribeInstanceStatus`<br />Required to view EC2 instance status details. | 
| [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) | `ec2:DescribeInstances`<br />Required to view EC2 instance details. | 
| [RebootInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html) | `ec2:RebootInstances`<br />Required to reboot an EC2 instance. | 
| [StopInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html) | `ec2:StopInstances`<br />Required to stop an EC2 instance. | 
| [TerminateInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html) | `ec2:TerminateInstances`<br />Required to terminate an EC2 instance. | 

## Amazon EC2 Auto Scaling API operations and required permissions for actions
<a name="cw-as-permissions-table"></a>


| Amazon EC2 Auto Scaling API operations | Required permissions (API actions) | 
| --- | --- | 
| Scaling | `autoscaling:Scaling`<br />Required to scale an Auto Scaling group. | 
| Trigger | `autoscaling:Trigger`<br />Required to trigger an Auto Scaling action. | 