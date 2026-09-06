

# Actions, resources, and condition keys for Amazon CloudWatch
<a name="list_cloudwatch"></a>

Amazon CloudWatch (service prefix: `cloudwatch`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudwatch/cloudwatch.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudWatch](#list_cloudwatch-operations)
+ [Actions defined by Amazon CloudWatch](#list_cloudwatch-actions-as-permissions)
+ [Permission-only actions for Amazon CloudWatch](#list_cloudwatch-permission-only-actions)
+ [Resource types defined by Amazon CloudWatch](#list_cloudwatch-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch](#list_cloudwatch-policy-keys)

## API operations defined by Amazon CloudWatch
<a name="list_cloudwatch-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudwatch-actions-as-permissions).




- **   DeleteAlarmMuteRule  **
  - **IAM action:**  [cloudwatch:DeleteAlarmMuteRule](#list_cloudwatch-action-DeleteAlarmMuteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAlarms  **
  - **IAM action:**  [cloudwatch:DeleteAlarms](#list_cloudwatch-action-DeleteAlarms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnomalyDetector  **
  - **IAM action:**  [cloudwatch:DeleteAnomalyDetector](#list_cloudwatch-action-DeleteAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDashboards  **
  - **IAM action:**  [cloudwatch:DeleteDashboards](#list_cloudwatch-action-DeleteDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInsightRules  **
  - **IAM action:**  [cloudwatch:DeleteInsightRules](#list_cloudwatch-action-DeleteInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMetricStream  **
  - **IAM action:**  [cloudwatch:DeleteMetricStream](#list_cloudwatch-action-DeleteMetricStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAlarmHistory  **
  - **IAM action:**  [cloudwatch:DescribeAlarmHistory](#list_cloudwatch-action-DescribeAlarmHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAlarms  **
  - **IAM action:**  [cloudwatch:DescribeAlarms](#list_cloudwatch-action-DescribeAlarms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAlarmsForMetric  **
  - **IAM action:**  [cloudwatch:DescribeAlarmsForMetric](#list_cloudwatch-action-DescribeAlarmsForMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAnomalyDetectors  **
  - **IAM action:**  [cloudwatch:DescribeAnomalyDetectors](#list_cloudwatch-action-DescribeAnomalyDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInsightRules  **
  - **IAM action:**  [cloudwatch:DescribeInsightRules](#list_cloudwatch-action-DescribeInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableAlarmActions  **
  - **IAM action:**  [cloudwatch:DisableAlarmActions](#list_cloudwatch-action-DisableAlarmActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableInsightRules  **
  - **IAM action:**  [cloudwatch:DisableInsightRules](#list_cloudwatch-action-DisableInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableAlarmActions  **
  - **IAM action:**  [cloudwatch:EnableAlarmActions](#list_cloudwatch-action-EnableAlarmActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableInsightRules  **
  - **IAM action:**  [cloudwatch:EnableInsightRules](#list_cloudwatch-action-EnableInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAlarmMuteRule  **
  - **IAM action:**  [cloudwatch:GetAlarmMuteRule](#list_cloudwatch-action-GetAlarmMuteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDashboard  **
  - **IAM action:**  [cloudwatch:GetDashboard](#list_cloudwatch-action-GetDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataset  **
  - **IAM action:**  [cloudwatch:GetDataset](#list_cloudwatch-action-GetDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightRuleReport  **
  - **IAM action:**  [cloudwatch:GetInsightRuleReport](#list_cloudwatch-action-GetInsightRuleReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricData  **
  - **IAM action:**  [cloudwatch:GetMetricData](#list_cloudwatch-action-GetMetricData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricStatistics  **
  - **IAM action:**  [cloudwatch:GetMetricStatistics](#list_cloudwatch-action-GetMetricStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricStream  **
  - **IAM action:**  [cloudwatch:GetMetricStream](#list_cloudwatch-action-GetMetricStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricWidgetImage  **
  - **IAM action:**  [cloudwatch:GetMetricWidgetImage](#list_cloudwatch-action-GetMetricWidgetImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOTelEnrichment  **
  - **IAM action:**  [cloudwatch:GetOTelEnrichment](#list_cloudwatch-action-GetOTelEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAlarmMuteRules  **
  - **IAM action:**  [cloudwatch:ListAlarmMuteRules](#list_cloudwatch-action-ListAlarmMuteRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDashboards  **
  - **IAM action:**  [cloudwatch:ListDashboards](#list_cloudwatch-action-ListDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedInsightRules  **
  - **IAM action:**  [cloudwatch:ListManagedInsightRules](#list_cloudwatch-action-ListManagedInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMetricStreams  **
  - **IAM action:**  [cloudwatch:ListMetricStreams](#list_cloudwatch-action-ListMetricStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetrics  **
  - **IAM action:**  [cloudwatch:ListMetrics](#list_cloudwatch-action-ListMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [cloudwatch:ListTagsForResource](#list_cloudwatch-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [oam:ListTagsForResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListTagsForResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   PutAlarmMuteRule  **
  - **IAM action:**  [cloudwatch:PutAlarmMuteRule](#list_cloudwatch-action-PutAlarmMuteRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutAnomalyDetector  **
  - **IAM action:**  [cloudwatch:PutAnomalyDetector](#list_cloudwatch-action-PutAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutCompositeAlarm  **
  - **IAM action:**  [cloudwatch:PutCompositeAlarm](#list_cloudwatch-action-PutCompositeAlarm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutDashboard  **
  - **IAM action:**  [cloudwatch:PutDashboard](#list_cloudwatch-action-PutDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutInsightRule  **
  - **IAM action:**  [cloudwatch:PutInsightRule](#list_cloudwatch-action-PutInsightRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutLogAlarm  **
  - **IAM action:**  [cloudwatch:PutLogAlarm](#list_cloudwatch-action-PutLogAlarm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudwatch.amazonaws.com / **Access level:** Write

- **   PutManagedInsightRules  **
  - **IAM action:**  [cloudwatch:PutManagedInsightRules](#list_cloudwatch-action-PutManagedInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMetricAlarm  **
  - **IAM action:**  [cloudwatch:PutMetricAlarm](#list_cloudwatch-action-PutMetricAlarm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutMetricData  **
  - **IAM action:**  [cloudwatch:PutMetricData](#list_cloudwatch-action-PutMetricData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMetricStream  **
  - **IAM action:**  [cloudwatch:PutMetricStream](#list_cloudwatch-action-PutMetricStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** streams.metrics.cloudwatch.amazonaws.com / **Access level:** Write

- **   SetAlarmState  **
  - **IAM action:**  [cloudwatch:SetAlarmState](#list_cloudwatch-action-SetAlarmState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetricStreams  **
  - **IAM action:**  [cloudwatch:StartMetricStreams](#list_cloudwatch-action-StartMetricStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartOTelEnrichment  **
  - **IAM action:**  [cloudwatch:StartOTelEnrichment](#list_cloudwatch-action-StartOTelEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopMetricStreams  **
  - **IAM action:**  [cloudwatch:StopMetricStreams](#list_cloudwatch-action-StopMetricStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopOTelEnrichment  **
  - **IAM action:**  [cloudwatch:StopOTelEnrichment](#list_cloudwatch-action-StopOTelEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [oam:TagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [cloudwatch:UntagResource](#list_cloudwatch-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [oam:UntagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UntagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write



## Actions defined by Amazon CloudWatch
<a name="list_cloudwatch-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetServiceLevelIndicatorReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to batch get service level indicator report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to batch retrieve a service level objective budget report
  - **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to create a service level objective
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarmMuteRule.html)  **
  - **Description:** Grants permission to delete an alarm mute rule
  - **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarms.html)  **
  - **Description:** Grants permission to delete a collection of alarms
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAnomalyDetector.html)  **
  - **Description:** Grants permission to delete the specified anomaly detection model from your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteDashboards.html)  **
  - **Description:** Grants permission to delete all CloudWatch dashboards that you specify
  - **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteInsightRules.html)  **
  - **Description:** Grants permission to delete a collection of insight rules
  - **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteMetricStream.html)  **
  - **Description:** Grants permission to delete the CloudWatch metric stream that you specify
  - **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to delete a service level objective
  - **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAlarmHistory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html)  **
  - **Description:** Grants permission to retrieve the history for the specified alarm
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html)  **
  - **Description:** Grants permission to describe all alarms, currently owned by the user's account
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAlarmsForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html)  **
  - **Description:** Grants permission to describe all alarms configured on the specified metric, currently owned by the user's account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAnomalyDetectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAnomalyDetectors.html)  **
  - **Description:** Grants permission to list the anomaly detection models that you have created in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html)  **
  - **Description:** Grants permission to describe all insight rules, currently owned by the user's account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableAlarmActions.html)  **
  - **Description:** Grants permission to disable actions for a collection of alarms
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableInsightRules.html)  **
  - **Description:** Grants permission to disable a collection of insight rules
  - **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableAlarmActions.html)  **
  - **Description:** Grants permission to enable actions for a collection of alarms
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableInsightRules.html)  **
  - **Description:** Grants permission to enable a collection of insight rules
  - **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableTopologyDiscovery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to enable a CloudWatch topology discovery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GenerateQuery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-query-assist.html)  **
  - **Description:** Grants permission to generate a Metrics Insights or Logs Insights query string from a natural language prompt
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GenerateQueryResultsSummary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html)  **
  - **Description:** Grants permission to generate a summary of CloudWatch LogInsights query results in natural language using generative AI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetAlarmMuteRule.html)  **
  - **Description:** Grants permission to get an alarm mute rule
  - **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDashboard.html)  **
  - **Description:** Grants permission to display the details of the CloudWatch dashboard you specify
  - **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataset](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDataset.html)  **
  - **Description:** Grants permission to get a dataset
  - **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html)  **
  - **Description:** Grants permission to return the top-N report of unique contributors over a time range for a given insight rule
  - **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html)  **
  - **Description:** Grants permission to retrieve batch amounts of CloudWatch classic metric data and perform metric math on retrieved data; and grants permission to retrieve OTLP metric data using PromQL
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html)  **
  - **Description:** Grants permission to retrieve statistics for the specified metric
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStream.html)  **
  - **Description:** Grants permission to return the details of a CloudWatch metric stream
  - **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMetricWidgetImage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricWidgetImage.html)  **
  - **Description:** Grants permission to retrieve snapshots of metric widgets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to retrieve information about a service
  - **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to retrieve information about service level objective
  - **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTopologyMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to retrieve a CloudWatch topology map
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAlarmMuteRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListAlarmMuteRules.html)  **
  - **Description:** Grants permission to retrieve a list of alarm mute rules owned by the user's account
  - **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html)  **
  - **Description:** Grants permission to return a list of all CloudWatch dashboards in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListManagedInsightRules.html)  **
  - **Description:** Grants permission to list available managed Insight Rules for a given Resource ARN
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:requestManagedResourceARNs](#list_cloudwatch-cloudwatch_requestManagedResourceARNs)
  - **Access level:** Read

- **   [ListMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetricStreams.html)  **
  - **Description:** Grants permission to return a list of all CloudWatch metric streams in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html)  **
  - **Description:** Grants permission to retrieve a list of valid metrics stored for the AWS account owner
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceLevelObjectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to list service level objectives
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServices](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to list services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an Amazon CloudWatch resource / **Resource types (\*required):** [alarm](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) / **Access level:** List
  - **Resource types (\*required):** [alarm-mute-rule](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_cloudwatch-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [insight-rule](#list_cloudwatch-resource-insight-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [metric-stream](#list_cloudwatch-resource-metric-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service](#list_cloudwatch-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [slo](#list_cloudwatch-resource-slo) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Description:** **SCENARIO: **CloudWatch-Alarm / **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-AlarmMuteRule / **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-InsightRule / **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-ServiceLevelObjective / **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dashboard / **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dataset / **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-MetricStream / **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Service / **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service) / **Condition keys:**  / **Access level:** 

- **   [PutAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutAlarmMuteRule.html)  **
  - **Description:** Grants permission to create or update an alarm mute rule
  - **Resource types (\*required):** [alarm](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Access level:** Write

- **   [PutAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutAnomalyDetector.html)  **
  - **Description:** Grants permission to create or update an anomaly detection model for a CloudWatch metric
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutCompositeAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html)  **
  - **Description:** Grants permission to create or update a composite alarm
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:AlarmActions](#list_cloudwatch-cloudwatch_AlarmActions)
  - **Access level:** Write

- **   [PutDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutDashboard.html)  **
  - **Description:** Grants permission to create a CloudWatch dashboard, or update an existing dashboard if it already exists
  - **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Access level:** Write

- **   [PutInsightRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutInsightRule.html)  **
  - **Description:** Grants permission to create a new insight rule or replace an existing insight rule
  - **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:requestInsightRuleLogGroups](#list_cloudwatch-cloudwatch_requestInsightRuleLogGroups)
  - **Access level:** Write

- **   [PutLogAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutLogAlarm.html)  **
  - **Description:** Grants permission to create or update a log-based alarm and associate it with a CloudWatch Logs Insights scheduled query
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:AlarmActions](#list_cloudwatch-cloudwatch_AlarmActions)
  - **Access level:** Write

- **   [PutManagedInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutManagedInsightRules.html)  **
  - **Description:** Grants permission to create managed Insight Rules
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:requestManagedResourceARNs](#list_cloudwatch-cloudwatch_requestManagedResourceARNs)
  - **Access level:** Write

- **   [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html)  **
  - **Description:** Grants permission to create or update an alarm and associates it with the specified Amazon CloudWatch metric
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:AlarmActions](#list_cloudwatch-cloudwatch_AlarmActions)
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:AlarmActions](#list_cloudwatch-cloudwatch_AlarmActions)
  - **Access level:** Write

- **   [PutMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html)  **
  - **Description:** Grants permission to publish metric data points to Amazon CloudWatch using CloudWatch and OTLP formats
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:namespace](#list_cloudwatch-cloudwatch_namespace)
  - **Access level:** Write

- **   [PutMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricStream.html)  **
  - **Description:** Grants permission to create a CloudWatch metric stream, or update an existing metric stream if it already exists
  - **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Access level:** Write

- **   [SetAlarmState](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_SetAlarmState.html)  **
  - **Description:** Grants permission to temporarily set the state of an alarm for testing purposes
  - **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartMetricStreams.html)  **
  - **Description:** Grants permission to start all CloudWatch metric streams that you specify
  - **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StopMetricStreams.html)  **
  - **Description:** Grants permission to stop all CloudWatch metric streams that you specify
  - **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to an Amazon CloudWatch resource / **Resource types (\*required):** [alarm](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys) / **Access level:** Tagging, Write
  - **Resource types (\*required):** [alarm-mute-rule](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_cloudwatch-resource-dashboard) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [insight-rule](#list_cloudwatch-resource-insight-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [metric-stream](#list_cloudwatch-resource-metric-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_cloudwatch-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [slo](#list_cloudwatch-resource-slo) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Description:** **SCENARIO: **CloudWatch-Alarm / **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-AlarmMuteRule / **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-InsightRule / **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-ServiceLevelObjective / **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dashboard / **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dataset / **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-MetricStream / **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Service / **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service) / **Condition keys:**  / **Access level:** 

- **   [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from an Amazon CloudWatch resource / **Resource types (\*required):** [alarm](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys) / **Access level:** Tagging, Write
  - **Resource types (\*required):** [alarm-mute-rule](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_cloudwatch-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [insight-rule](#list_cloudwatch-resource-insight-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [metric-stream](#list_cloudwatch-resource-metric-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_cloudwatch-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Resource types (\*required):** [slo](#list_cloudwatch-resource-slo) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Description:** **SCENARIO: **CloudWatch-Alarm / **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-AlarmMuteRule / **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-InsightRule / **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-ServiceLevelObjective / **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dashboard / **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dataset / **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-MetricStream / **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Service / **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service) / **Condition keys:**  / **Access level:** 

- **   [UpdateServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to update a service level objective
  - **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon CloudWatch
<a name="list_cloudwatch-permission-only-actions"></a>

The following actions are defined by Amazon CloudWatch but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CallWithBearerToken](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to make API calls to CloudWatch using bearer token authentication
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePipelineRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to delete a pipeline rule for CloudWatch pipelines for OTel metric processing
  - **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to retrieve the status of OTel Enrichment of vended metrics for PromQL querying
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to retrieve service data
  - **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTopologyDiscoveryStatus](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to retrieve a CloudWatch topology discovery status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html#CloudWatch-Unified-Cross-Account-Setup-permissions)  **
  - **Description:** Grants permission to share CloudWatch resources with a monitoring account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListEntitiesForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to retrieve all the entities that are emitting a given metric
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutPipelineRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to create or update a pipeline rule for CloudWatch pipelines for OTel metric processing
  - **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to enable OTel Enrichment of vended metrics for PromQL querying
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  **
  - **Description:** Grants permission to disable OTel Enrichment of vended metrics for PromQL querying
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon CloudWatch
<a name="list_cloudwatch-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:alarm:${AlarmName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [alarm-mute-rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:alarm-mute-rule:${AlarmMuteRuleName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch::${Account}:dashboard/${DashboardName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:dataset/${DatasetId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [insight-rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:insight-rule/${InsightRuleName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [metric-stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:metric-stream/${MetricStreamName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:service/${ServiceName}-${UniqueAttributesHex} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [slo](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:slo/${SloName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch
<a name="list_cloudwatch-policy-keys"></a>

Amazon CloudWatch defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tags in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tags in the request | ArrayOfString | 
|   [cloudwatch:AlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-alarm-actions.html)  | Filters access by defined alarm actions | ArrayOfString | 
|   [cloudwatch:namespace](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-namespace.html)  | Filters access by the presence of optional namespace values | String | 
|   [cloudwatch:requestInsightRuleLogGroups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-contributor.html)  | Filters access by the Log Groups specified in an Insight Rule | ArrayOfString | 
|   [cloudwatch:requestManagedResourceARNs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-contributor.html)  | Filters access by the Resource ARNs specified in a managed Insight Rule | ArrayOfARN | 