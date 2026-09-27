

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
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DeleteAlarmMuteRule](#list_cloudwatch-action-DeleteAlarmMuteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAlarms  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DeleteAlarms](#list_cloudwatch-action-DeleteAlarms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnomalyDetector  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DeleteAnomalyDetector](#list_cloudwatch-action-DeleteAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDashboards  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DeleteDashboards](#list_cloudwatch-action-DeleteDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInsightRules  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DeleteInsightRules](#list_cloudwatch-action-DeleteInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMetricStream  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DeleteMetricStream](#list_cloudwatch-action-DeleteMetricStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAlarmHistory  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DescribeAlarmHistory](#list_cloudwatch-action-DescribeAlarmHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAlarms  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DescribeAlarms](#list_cloudwatch-action-DescribeAlarms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAlarmsForMetric  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DescribeAlarmsForMetric](#list_cloudwatch-action-DescribeAlarmsForMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAnomalyDetectors  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DescribeAnomalyDetectors](#list_cloudwatch-action-DescribeAnomalyDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInsightRules  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DescribeInsightRules](#list_cloudwatch-action-DescribeInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableAlarmActions  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DisableAlarmActions](#list_cloudwatch-action-DisableAlarmActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableInsightRules  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:DisableInsightRules](#list_cloudwatch-action-DisableInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableAlarmActions  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:EnableAlarmActions](#list_cloudwatch-action-EnableAlarmActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableInsightRules  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:EnableInsightRules](#list_cloudwatch-action-EnableInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAlarmMuteRule  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetAlarmMuteRule](#list_cloudwatch-action-GetAlarmMuteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDashboard  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetDashboard](#list_cloudwatch-action-GetDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataset  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetDataset](#list_cloudwatch-action-GetDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightRuleReport  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetInsightRuleReport](#list_cloudwatch-action-GetInsightRuleReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricData  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetMetricData](#list_cloudwatch-action-GetMetricData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricStatistics  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetMetricStatistics](#list_cloudwatch-action-GetMetricStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricStream  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetMetricStream](#list_cloudwatch-action-GetMetricStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricWidgetImage  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetMetricWidgetImage](#list_cloudwatch-action-GetMetricWidgetImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOTelEnrichment  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:GetOTelEnrichment](#list_cloudwatch-action-GetOTelEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAlarmMuteRules  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:ListAlarmMuteRules](#list_cloudwatch-action-ListAlarmMuteRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDashboards  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:ListDashboards](#list_cloudwatch-action-ListDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedInsightRules  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:ListManagedInsightRules](#list_cloudwatch-action-ListManagedInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMetricStreams  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:ListMetricStreams](#list_cloudwatch-action-ListMetricStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetrics  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:ListMetrics](#list_cloudwatch-action-ListMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:ListTagsForResource](#list_cloudwatch-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [oam:ListTagsForResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListTagsForResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   PutAlarmMuteRule  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutAlarmMuteRule](#list_cloudwatch-action-PutAlarmMuteRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutAnomalyDetector  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutAnomalyDetector](#list_cloudwatch-action-PutAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutCompositeAlarm  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutCompositeAlarm](#list_cloudwatch-action-PutCompositeAlarm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutDashboard  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutDashboard](#list_cloudwatch-action-PutDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutInsightRule  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutInsightRule](#list_cloudwatch-action-PutInsightRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutLogAlarm  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutLogAlarm](#list_cloudwatch-action-PutLogAlarm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudwatch.amazonaws.com / **Access level:** Write

- **   PutManagedInsightRules  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutManagedInsightRules](#list_cloudwatch-action-PutManagedInsightRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMetricAlarm  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutMetricAlarm](#list_cloudwatch-action-PutMetricAlarm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutMetricData  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutMetricData](#list_cloudwatch-action-PutMetricData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMetricStream  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:PutMetricStream](#list_cloudwatch-action-PutMetricStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** streams.metrics.cloudwatch.amazonaws.com / **Access level:** Write

- **   SetAlarmState  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:SetAlarmState](#list_cloudwatch-action-SetAlarmState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetricStreams  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:StartMetricStreams](#list_cloudwatch-action-StartMetricStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartOTelEnrichment  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:StartOTelEnrichment](#list_cloudwatch-action-StartOTelEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopMetricStreams  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:StopMetricStreams](#list_cloudwatch-action-StopMetricStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopOTelEnrichment  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:StopOTelEnrichment](#list_cloudwatch-action-StopOTelEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [oam:TagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** cloudwatch
  - **IAM action:**  [cloudwatch:UntagResource](#list_cloudwatch-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [oam:UntagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UntagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAccessGrant  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateAccessGrant](#list_cloudwatch-action-CreateAccessGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAccessProfile  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateAccessProfile](#list_cloudwatch-action-CreateAccessProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAlert  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateAlert](#list_cloudwatch-action-CreateAlert) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomain  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateDomain](#list_cloudwatch-action-CreateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDomainAccessGrantForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateDomainAccessGrantForOrganization](#list_cloudwatch-action-CreateDomainAccessGrantForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDomainForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateDomainForOrganization](#list_cloudwatch-action-CreateDomainForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudwatch.amazonaws.com / **Access level:** Write

- **   CreateIntegration  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateIntegration](#list_cloudwatch-action-CreateIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudwatch.amazonaws.com / **Access level:** Write

- **   CreateOmniDashboard  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateOmniDashboard](#list_cloudwatch-action-CreateOmniDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOneTimeDeepLinkCode  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateOneTimeDeepLinkCode](#list_cloudwatch-action-CreateOneTimeDeepLinkCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSpace  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateSpace](#list_cloudwatch-action-CreateSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:TagResource](#list_cloudwatch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudwatch.amazonaws.com / **Access level:** Write

- **   CreateView  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:CreateView](#list_cloudwatch-action-CreateView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccessGrant  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteAccessGrant](#list_cloudwatch-action-DeleteAccessGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteAccessProfile  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteAccessProfile](#list_cloudwatch-action-DeleteAccessProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteDomain  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteDomain](#list_cloudwatch-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainAccessGrantForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteDomainAccessGrantForOrganization](#list_cloudwatch-action-DeleteDomainAccessGrantForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteDomainForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteDomainForOrganization](#list_cloudwatch-action-DeleteDomainForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteIntegration](#list_cloudwatch-action-DeleteIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOmniDashboard  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteOmniDashboard](#list_cloudwatch-action-DeleteOmniDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSpace  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteSpace](#list_cloudwatch-action-DeleteSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteView  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:DeleteView](#list_cloudwatch-action-DeleteView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessGrant  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetAccessGrant](#list_cloudwatch-action-GetAccessGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessProfile  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetAccessProfile](#list_cloudwatch-action-GetAccessProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAlert  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetAlert](#list_cloudwatch-action-GetAlert) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContextGraph  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetContextGraph](#list_cloudwatch-action-GetContextGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomain  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetDomain](#list_cloudwatch-action-GetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainAccessGrantForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetDomainAccessGrantForOrganization](#list_cloudwatch-action-GetDomainAccessGrantForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetDomainForOrganization](#list_cloudwatch-action-GetDomainForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegration  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetIntegration](#list_cloudwatch-action-GetIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntelligenceConfiguration  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetIntelligenceConfiguration](#list_cloudwatch-action-GetIntelligenceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOmniDashboard  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetOmniDashboard](#list_cloudwatch-action-GetOmniDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSpace  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetSpace](#list_cloudwatch-action-GetSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSpaceCredentialsForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetSpaceCredentialsForOrganization](#list_cloudwatch-action-GetSpaceCredentialsForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryQueryResults  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetTelemetryQueryResults](#list_cloudwatch-action-GetTelemetryQueryResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetView  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetView](#list_cloudwatch-action-GetView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessGrants  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListAccessGrants](#list_cloudwatch-action-ListAccessGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccessProfiles  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListAccessProfiles](#list_cloudwatch-action-ListAccessProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAlerts  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListAlerts](#list_cloudwatch-action-ListAlerts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainAccessGrantsForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListDomainAccessGrantsForOrganization](#list_cloudwatch-action-ListDomainAccessGrantsForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomains  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListDomains](#list_cloudwatch-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntegrations  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListIntegrations](#list_cloudwatch-action-ListIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOmniDashboards  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListOmniDashboards](#list_cloudwatch-action-ListOmniDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpaces  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListSpaces](#list_cloudwatch-action-ListSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpacesForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListSpacesForOrganization](#list_cloudwatch-action-ListSpacesForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTelemetryFields  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetRecords](#list_cloudwatch-action-GetRecords)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudwatch:ListMetrics](#list_cloudwatch-action-ListMetrics)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [cloudwatch:ListTelemetryFields](#list_cloudwatch-action-ListTelemetryFields)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTelemetryQuerySessions  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListTelemetryQuerySessions](#list_cloudwatch-action-ListTelemetryQuerySessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListViews  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:ListViews](#list_cloudwatch-action-ListViews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutIntelligenceConfiguration  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:PutIntelligenceConfiguration](#list_cloudwatch-action-PutIntelligenceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchPrincipals  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:SearchPrincipals](#list_cloudwatch-action-SearchPrincipals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTelemetryQuery  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:GetMetricData](#list_cloudwatch-action-GetMetricData)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudwatch:GetRecords](#list_cloudwatch-action-GetRecords)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudwatch:ListMetrics](#list_cloudwatch-action-ListMetrics)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   StartTelemetryQuerySession  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:StartTelemetryQuerySession](#list_cloudwatch-action-StartTelemetryQuerySession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTelemetryQuery  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:StopTelemetryQuery](#list_cloudwatch-action-StopTelemetryQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTelemetryQuerySession  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:StopTelemetryQuerySession](#list_cloudwatch-action-StopTelemetryQuerySession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccessProfile  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateAccessProfile](#list_cloudwatch-action-UpdateAccessProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateAlert  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateAlert](#list_cloudwatch-action-UpdateAlert) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomain  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateDomain](#list_cloudwatch-action-UpdateDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainForOrganization  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateDomainForOrganization](#list_cloudwatch-action-UpdateDomainForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntegration  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateIntegration](#list_cloudwatch-action-UpdateIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudwatch.amazonaws.com / **Access level:** Write

- **   UpdateOmniDashboard  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateOmniDashboard](#list_cloudwatch-action-UpdateOmniDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSpace  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateSpace](#list_cloudwatch-action-UpdateSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateView  **
  - **SDK client:** cloudwatchomni
  - **IAM action:**  [cloudwatch:UpdateView](#list_cloudwatch-action-UpdateView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon CloudWatch
<a name="list_cloudwatch-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssumeAccessProfile](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AssumeAccessProfile.html)  **
  - **Description:** Grants permission to assume an access profile
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

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

- **   [CreateAccessGrant](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateAccessGrant.html)  **
  - **Description:** Grants permission to create an access grant
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

- **   [CreateAccessProfile](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateAccessProfile.html)  **
  - **Description:** Grants permission to create an access profile
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

- **   [CreateAlert](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateAlert.html)  **
  - **Description:** Grants permission to create an alert
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create a domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDomainAccessGrantForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateDomainAccessGrantForOrganization.html)  **
  - **Description:** Grants permission to create a domain access grant for an organization
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

- **   [CreateDomainForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateDomainForOrganization.html)  **
  - **Description:** Grants permission to create a domain for an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIngestionEndpoint](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateIngestionEndpoint.html)  **
  - **Description:** Grants permission to create an ingestion endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateIntegration.html)  **
  - **Description:** Grants permission to create an integration
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [CreateOmniDashboard](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateOmniDashboard.html)  **
  - **Description:** Grants permission to create an omni dashboard
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [CreateOmniThread](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateOmniThread.html)  **
  - **Description:** Grants permission to create an omni thread
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [CreateOneTimeDeepLinkCode](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateOneTimeDeepLinkCode.html)  **
  - **Description:** Grants permission to create a one-time deep link code
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to create a service level objective
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSpace](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateSpace.html)  **
  - **Description:** Grants permission to create a space
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateView](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateView.html)  **
  - **Description:** Grants permission to create a view
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [DeleteAccessGrant](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteAccessGrant.html)  **
  - **Description:** Grants permission to delete an access grant
  - **Resource types (\*required):** [access-grant\*](#list_cloudwatch-resource-access-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

- **   [DeleteAccessProfile](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteAccessProfile.html)  **
  - **Description:** Grants permission to delete an access profile
  - **Resource types (\*required):** [access-profile\*](#list_cloudwatch-resource-access-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

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

- **   [DeleteAlert](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteAlert.html)  **
  - **Description:** Grants permission to delete an alert
  - **Resource types (\*required):** [alert\*](#list_cloudwatch-resource-alert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [DeleteDomain](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a domain
  - **Resource types (\*required):** [domain\*](#list_cloudwatch-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainAccessGrantForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteDomainAccessGrantForOrganization.html)  **
  - **Description:** Grants permission to delete a domain access grant for an organization
  - **Resource types (\*required):** [organization-access-grant\*](#list_cloudwatch-resource-organization-access-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

- **   [DeleteDomainForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteDomainForOrganization.html)  **
  - **Description:** Grants permission to delete a domain for an organization
  - **Resource types (\*required):** [organization-domain\*](#list_cloudwatch-resource-organization-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIngestionEndpoint](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteIngestionEndpoint.html)  **
  - **Description:** Grants permission to delete an ingestion endpoint
  - **Resource types (\*required):** [ingestion-endpoint\*](#list_cloudwatch-resource-ingestion-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteInsightRules.html)  **
  - **Description:** Grants permission to delete a collection of insight rules
  - **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete an integration
  - **Resource types (\*required):** [integration\*](#list_cloudwatch-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [DeleteMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteMetricStream.html)  **
  - **Description:** Grants permission to delete the CloudWatch metric stream that you specify
  - **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOmniDashboard](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteOmniDashboard.html)  **
  - **Description:** Grants permission to delete an omni dashboard
  - **Resource types (\*required):** [omni-dashboard\*](#list_cloudwatch-resource-omni-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [DeleteOmniThread](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteOmniThread.html)  **
  - **Description:** Grants permission to delete an omni thread
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [DeleteServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to delete a service level objective
  - **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSpace](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteSpace.html)  **
  - **Description:** Grants permission to delete a space
  - **Resource types (\*required):** [space\*](#list_cloudwatch-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteView](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteView.html)  **
  - **Description:** Grants permission to delete a view
  - **Resource types (\*required):** [view\*](#list_cloudwatch-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [GetAccessGrant](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAccessGrant.html)  **
  - **Description:** Grants permission to get an access grant
  - **Resource types (\*required):** [access-grant\*](#list_cloudwatch-resource-access-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetAccessProfile](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAccessProfile.html)  **
  - **Description:** Grants permission to get an access profile
  - **Resource types (\*required):** [access-profile\*](#list_cloudwatch-resource-access-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetAgentGraph](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAgentGraph.html)  **
  - **Description:** Grants permission to get an agent graph
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetAlarmMuteRule.html)  **
  - **Description:** Grants permission to get an alarm mute rule
  - **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAlert](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAlert.html)  **
  - **Description:** Grants permission to get an alert
  - **Resource types (\*required):** [alert\*](#list_cloudwatch-resource-alert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetContextGraph](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetContextGraph.html)  **
  - **Description:** Grants permission to get a context graph
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [GetDomain](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomain.html)  **
  - **Description:** Grants permission to get a domain
  - **Resource types (\*required):** [domain\*](#list_cloudwatch-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetDomainAccessGrantForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomainAccessGrantForOrganization.html)  **
  - **Description:** Grants permission to get a domain access grant for an organization
  - **Resource types (\*required):** [organization-access-grant\*](#list_cloudwatch-resource-organization-access-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetDomainForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomainForOrganization.html)  **
  - **Description:** Grants permission to get a domain for an organization
  - **Resource types (\*required):** [organization-domain\*](#list_cloudwatch-resource-organization-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIngestionEndpoint](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetIngestionEndpoint.html)  **
  - **Description:** Grants permission to get an ingestion endpoint
  - **Resource types (\*required):** [ingestion-endpoint\*](#list_cloudwatch-resource-ingestion-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html)  **
  - **Description:** Grants permission to return the top-N report of unique contributors over a time range for a given insight rule
  - **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetIntegration.html)  **
  - **Description:** Grants permission to get an integration
  - **Resource types (\*required):** [integration\*](#list_cloudwatch-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetIntelligenceConfiguration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetIntelligenceConfiguration.html)  **
  - **Description:** Grants permission to get an intelligence configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html)  **
  - **Description:** Grants permission to retrieve batch amounts of CloudWatch classic metric data and perform metric math on retrieved data; and grants permission to retrieve OTLP metric data using PromQL
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [GetOmniDashboard](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetOmniDashboard.html)  **
  - **Description:** Grants permission to get an omni dashboard
  - **Resource types (\*required):** [omni-dashboard\*](#list_cloudwatch-resource-omni-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetOmniThread](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetOmniThread.html)  **
  - **Description:** Grants permission to get an omni thread
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetPreferences](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetPreferences.html)  **
  - **Description:** Grants permission to get preferences
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetRecords](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetRecords.html)  **
  - **Description:** Grants permission to fetch logs, metrics, and traces
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [GetSpace](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpace.html)  **
  - **Description:** Grants permission to get a space
  - **Resource types (\*required):** [space\*](#list_cloudwatch-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetSpaceCredentials](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpaceCredentials.html)  **
  - **Description:** Grants permission to get space credentials
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSpaceCredentialsForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpaceCredentialsForOrganization.html)  **
  - **Description:** Grants permission to get space credentials for an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTelemetryQueryResults](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetTelemetryQueryResults.html)  **
  - **Description:** Grants permission to get telemetry query results
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [GetTopologyMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to retrieve a CloudWatch topology map
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetView](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetView.html)  **
  - **Description:** Grants permission to get a view
  - **Resource types (\*required):** [view\*](#list_cloudwatch-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Read

- **   [InvokeIntegration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_InvokeIntegration.html)  **
  - **Description:** Grants permission to invoke an integration
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [ListAccessGrants](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAccessGrants.html)  **
  - **Description:** Grants permission to list access grants
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListAccessProfiles](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAccessProfiles.html)  **
  - **Description:** Grants permission to list access profiles
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListAlarmMuteRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListAlarmMuteRules.html)  **
  - **Description:** Grants permission to retrieve a list of alarm mute rules owned by the user's account
  - **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAlertContributors](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAlertContributors.html)  **
  - **Description:** Grants permission to list alert contributors
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListAlerts](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAlerts.html)  **
  - **Description:** Grants permission to list alerts
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html)  **
  - **Description:** Grants permission to return a list of all CloudWatch dashboards in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomainAccessGrantsForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListDomainAccessGrantsForOrganization.html)  **
  - **Description:** Grants permission to list domain access grants for an organization
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to list domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIngestionEndpoints](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListIngestionEndpoints.html)  **
  - **Description:** Grants permission to list ingestion endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIntegrations](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListIntegrations.html)  **
  - **Description:** Grants permission to list integrations
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListOmniDashboards](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListOmniDashboards.html)  **
  - **Description:** Grants permission to list omni dashboards
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListOmniThreads](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListOmniThreads.html)  **
  - **Description:** Grants permission to list omni threads
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [ListSpaceAccess](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpaceAccess.html)  **
  - **Description:** Grants permission to list access to a space
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListSpaces](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpaces.html)  **
  - **Description:** Grants permission to list spaces
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListSpacesForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpacesForOrganization.html)  **
  - **Description:** Grants permission to list spaces for an organization
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an Amazon CloudWatch resource / **Resource types (\*required):** [alarm](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant) / **Access level:** List
  - **Resource types (\*required):** [alarm-mute-rule](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [dashboard](#list_cloudwatch-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [insight-rule](#list_cloudwatch-resource-insight-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [metric-stream](#list_cloudwatch-resource-metric-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [service](#list_cloudwatch-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [slo](#list_cloudwatch-resource-slo) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Description:** **SCENARIO: **CloudWatch-Alarm / **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-AlarmMuteRule / **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-InsightRule / **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-ServiceLevelObjective / **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dashboard / **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dataset / **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-MetricStream / **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Service / **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service) / **Condition keys:**  / **Access level:** 

- **   [ListTelemetryFields](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListTelemetryFields.html)  **
  - **Description:** Grants permission to list telemetry fields
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListTelemetryQuerySessions](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListTelemetryQuerySessions.html)  **
  - **Description:** Grants permission to list telemetry query sessions
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

- **   [ListViews](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListViews.html)  **
  - **Description:** Grants permission to list views
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** List

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

- **   [PutIntelligenceConfiguration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_PutIntelligenceConfiguration.html)  **
  - **Description:** Grants permission to configure an intelligence configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [QueryTraces](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_QueryTraces.html)  **
  - **Description:** Grants permission to query traces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchPrincipals](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_SearchPrincipals.html)  **
  - **Description:** Grants permission to search principals
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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

- **   [StartOmniThreadSession](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StartOmniThreadSession.html)  **
  - **Description:** Grants permission to start an omni thread session
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [StartTelemetryQuery](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StartTelemetryQuery.html)  **
  - **Description:** Grants permission to start a telemetry query
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [StartTelemetryQuerySession](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StartTelemetryQuerySession.html)  **
  - **Description:** Grants permission to start a telemetry query session
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [StopMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StopMetricStreams.html)  **
  - **Description:** Grants permission to stop all CloudWatch metric streams that you specify
  - **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTelemetryQuery](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StopTelemetryQuery.html)  **
  - **Description:** Grants permission to stop a telemetry query
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [StopTelemetryQuerySession](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StopTelemetryQuerySession.html)  **
  - **Description:** Grants permission to stop a telemetry query session
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [SubmitFeedback](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_SubmitFeedback.html)  **
  - **Description:** Grants permission to submit feedback
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to an Amazon CloudWatch resource / **Resource types (\*required):** [alarm](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant) / **Access level:** Tagging, Write
  - **Resource types (\*required):** [alarm-mute-rule](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [dashboard](#list_cloudwatch-resource-dashboard) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [insight-rule](#list_cloudwatch-resource-insight-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [metric-stream](#list_cloudwatch-resource-metric-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [service](#list_cloudwatch-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [slo](#list_cloudwatch-resource-slo) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudwatch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Description:** **SCENARIO: **CloudWatch-Alarm / **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-AlarmMuteRule / **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-InsightRule / **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-ServiceLevelObjective / **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dashboard / **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dataset / **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-MetricStream / **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Service / **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service) / **Condition keys:**  / **Access level:** 

- **   [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from an Amazon CloudWatch resource / **Resource types (\*required):** [alarm](#list_cloudwatch-resource-alarm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant) / **Access level:** Tagging, Write
  - **Resource types (\*required):** [alarm-mute-rule](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [dashboard](#list_cloudwatch-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [dataset](#list_cloudwatch-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [insight-rule](#list_cloudwatch-resource-insight-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [metric-stream](#list_cloudwatch-resource-metric-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [service](#list_cloudwatch-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Resource types (\*required):** [slo](#list_cloudwatch-resource-slo) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudwatch-aws_TagKeys)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Description:** **SCENARIO: **CloudWatch-Alarm / **Resource types (\*required):** [alarm\*](#list_cloudwatch-resource-alarm) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-AlarmMuteRule / **Resource types (\*required):** [alarm-mute-rule\*](#list_cloudwatch-resource-alarm-mute-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-InsightRule / **Resource types (\*required):** [insight-rule\*](#list_cloudwatch-resource-insight-rule) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-ServiceLevelObjective / **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dashboard / **Resource types (\*required):** [dashboard\*](#list_cloudwatch-resource-dashboard) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Dataset / **Resource types (\*required):** [dataset\*](#list_cloudwatch-resource-dataset) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-MetricStream / **Resource types (\*required):** [metric-stream\*](#list_cloudwatch-resource-metric-stream) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **CloudWatch-Service / **Resource types (\*required):** [service\*](#list_cloudwatch-resource-service) / **Condition keys:**  / **Access level:** 

- **   [UpdateAccessProfile](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateAccessProfile.html)  **
  - **Description:** Grants permission to update an access profile
  - **Resource types (\*required):** [access-profile\*](#list_cloudwatch-resource-access-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Permissions management, Write

- **   [UpdateAlert](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateAlert.html)  **
  - **Description:** Grants permission to update an alert
  - **Resource types (\*required):** [alert\*](#list_cloudwatch-resource-alert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [UpdateDomain](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateDomain.html)  **
  - **Description:** Grants permission to update a domain
  - **Resource types (\*required):** [domain\*](#list_cloudwatch-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateDomainForOrganization.html)  **
  - **Description:** Grants permission to update a domain for an organization
  - **Resource types (\*required):** [organization-domain\*](#list_cloudwatch-resource-organization-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIngestionEndpoint](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateIngestionEndpoint.html)  **
  - **Description:** Grants permission to update an ingestion endpoint
  - **Resource types (\*required):** [ingestion-endpoint\*](#list_cloudwatch-resource-ingestion-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntegration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateIntegration.html)  **
  - **Description:** Grants permission to update an integration
  - **Resource types (\*required):** [integration\*](#list_cloudwatch-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [UpdateOmniDashboard](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateOmniDashboard.html)  **
  - **Description:** Grants permission to update an omni dashboard
  - **Resource types (\*required):** [omni-dashboard\*](#list_cloudwatch-resource-omni-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [UpdateOmniThread](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateOmniThread.html)  **
  - **Description:** Grants permission to update an omni thread
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [UpdatePreferences](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdatePreferences.html)  **
  - **Description:** Grants permission to update preferences
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [UpdateServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK)  **
  - **Description:** Grants permission to update a service level objective
  - **Resource types (\*required):** [slo\*](#list_cloudwatch-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSpace](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateSpace.html)  **
  - **Description:** Grants permission to update a space
  - **Resource types (\*required):** [space\*](#list_cloudwatch-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
  - **Access level:** Write

- **   [UpdateView](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateView.html)  **
  - **Description:** Grants permission to update a view
  - **Resource types (\*required):** [view\*](#list_cloudwatch-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_)<br />[cloudwatch:HasAccessGrant](#list_cloudwatch-cloudwatch_HasAccessGrant)
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
|  [access-grant](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:access-grant/${GrantId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [access-profile](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:access-profile/${ProfileId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:alarm:${AlarmName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [alarm-mute-rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:alarm-mute-rule:${AlarmMuteRuleName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [alert](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:alert/${AlertId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch::${Account}:dashboard/${DashboardName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:dataset/${DatasetId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [domain](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:domain/${DomainId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [ingestion-endpoint](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:ingestion-endpoint/${IngestionEndpointName}/${IngestionEndpointId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [insight-rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:insight-rule/${InsightRuleName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [integration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:integration/${IntegrationId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [metric-stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:metric-stream/${MetricStreamName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [omni-dashboard](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:omni-dashboard/${DashboardId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [organization-access-grant](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:organization-access-grant/${GrantId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [organization-domain](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:organization-domain/${DomainId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:service/${ServiceName}-${UniqueAttributesHex} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [slo](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:slo/${SloName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [space](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:space/${SpaceId} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 
|  [view](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html)  | arn:${Partition}:cloudwatch:${Region}:${Account}:view/${ViewName} | [aws:ResourceTag/${TagKey}](#list_cloudwatch-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch
<a name="list_cloudwatch-policy-keys"></a>

Amazon CloudWatch defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tags in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tags in the request | ArrayOfString | 
|   [cloudwatch:AlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-alarm-actions.html)  | Filters access by defined alarm actions | ArrayOfString | 
|   [cloudwatch:HasAccessGrant](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.html)  | Filters access by the presence of access grants associated with the request | String | 
|   [cloudwatch:namespace](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-namespace.html)  | Filters access by the presence of optional namespace values | String | 
|   [cloudwatch:requestInsightRuleLogGroups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-contributor.html)  | Filters access by the Log Groups specified in an Insight Rule | ArrayOfString | 
|   [cloudwatch:requestManagedResourceARNs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-contributor.html)  | Filters access by the Resource ARNs specified in a managed Insight Rule | ArrayOfARN | 