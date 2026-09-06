

# Actions, resources, and condition keys for Amazon CloudWatch Logs
<a name="list_logs"></a>

Amazon CloudWatch Logs (service prefix: `logs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/logs/logs.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudWatch Logs](#list_logs-operations)
+ [Actions defined by Amazon CloudWatch Logs](#list_logs-actions-as-permissions)
+ [Permission-only actions for Amazon CloudWatch Logs](#list_logs-permission-only-actions)
+ [Resource types defined by Amazon CloudWatch Logs](#list_logs-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Logs](#list_logs-policy-keys)

## API operations defined by Amazon CloudWatch Logs
<a name="list_logs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_logs-actions-as-permissions).




- **   AssociateKmsKey  **
  - **IAM action:**  [logs:AssociateKmsKey](#list_logs-action-AssociateKmsKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateSourceToS3TableIntegration  **
  - **IAM action:**  [logs:AssociateSourceToS3TableIntegration](#list_logs-action-AssociateSourceToS3TableIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelExportTask  **
  - **IAM action:**  [logs:CancelExportTask](#list_logs-action-CancelExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelImportTask  **
  - **IAM action:**  [logs:CancelImportTask](#list_logs-action-CancelImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDelivery  **
  - **IAM action:**  [logs:CreateDelivery](#list_logs-action-CreateDelivery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateExportTask  **
  - **IAM action:**  [logs:CreateExportTask](#list_logs-action-CreateExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateImportTask  **
  - **IAM action:**  [logs:CreateImportTask](#list_logs-action-CreateImportTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudtrail.amazonaws.com, logs.amazonaws.com / **Access level:** Write

- **   CreateLogAnomalyDetector  **
  - **IAM action:**  [logs:CreateLogAnomalyDetector](#list_logs-action-CreateLogAnomalyDetector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLogGroup  **
  - **IAM action:**  [logs:CreateLogGroup](#list_logs-action-CreateLogGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:TagLogGroup](#list_logs-action-TagLogGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLogStream  **
  - **IAM action:**  [logs:CreateLogStream](#list_logs-action-CreateLogStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLookupTable  **
  - **IAM action:**  [logs:CreateLookupTable](#list_logs-action-CreateLookupTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:GetQueryResults](#list_logs-action-GetQueryResults)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateScheduledQuery  **
  - **IAM action:**  [logs:CreateScheduledQuery](#list_logs-action-CreateScheduledQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com / **Access level:** Write

- **   DeleteAccountPolicy  **
  - **IAM action:**  [logs:DeleteAccountPolicy](#list_logs-action-DeleteAccountPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:DeleteDataProtectionPolicy](#list_logs-action-DeleteDataProtectionPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:DeleteIndexPolicy](#list_logs-action-DeleteIndexPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:DeleteRetentionPolicy](#list_logs-action-DeleteRetentionPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:DeleteSubscriptionFilter](#list_logs-action-DeleteSubscriptionFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:DeleteTransformer](#list_logs-action-DeleteTransformer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDataProtectionPolicy  **
  - **IAM action:**  [logs:DeleteDataProtectionPolicy](#list_logs-action-DeleteDataProtectionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDelivery  **
  - **IAM action:**  [logs:DeleteDelivery](#list_logs-action-DeleteDelivery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeliveryDestination  **
  - **IAM action:**  [logs:DeleteDeliveryDestination](#list_logs-action-DeleteDeliveryDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeliveryDestinationPolicy  **
  - **IAM action:**  [logs:DeleteDeliveryDestinationPolicy](#list_logs-action-DeleteDeliveryDestinationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeliverySource  **
  - **IAM action:**  [logs:DeleteDeliverySource](#list_logs-action-DeleteDeliverySource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDestination  **
  - **IAM action:**  [logs:DeleteDestination](#list_logs-action-DeleteDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIndexPolicy  **
  - **IAM action:**  [logs:DeleteIndexPolicy](#list_logs-action-DeleteIndexPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **IAM action:**  [logs:DeleteIntegration](#list_logs-action-DeleteIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLogAnomalyDetector  **
  - **IAM action:**  [logs:DeleteLogAnomalyDetector](#list_logs-action-DeleteLogAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLogGroup  **
  - **IAM action:**  [logs:DeleteLogGroup](#list_logs-action-DeleteLogGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLogStream  **
  - **IAM action:**  [logs:DeleteLogStream](#list_logs-action-DeleteLogStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLookupTable  **
  - **IAM action:**  [logs:DeleteLookupTable](#list_logs-action-DeleteLookupTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMetricFilter  **
  - **IAM action:**  [logs:DeleteMetricFilter](#list_logs-action-DeleteMetricFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueryDefinition  **
  - **IAM action:**  [logs:DeleteQueryDefinition](#list_logs-action-DeleteQueryDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [logs:DeleteResourcePolicy](#list_logs-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteRetentionPolicy  **
  - **IAM action:**  [logs:DeleteRetentionPolicy](#list_logs-action-DeleteRetentionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScheduledQuery  **
  - **IAM action:**  [logs:DeleteScheduledQuery](#list_logs-action-DeleteScheduledQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscriptionFilter  **
  - **IAM action:**  [logs:DeleteSubscriptionFilter](#list_logs-action-DeleteSubscriptionFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSyslogConfiguration  **
  - **IAM action:**  [logs:DeleteSyslogConfiguration](#list_logs-action-DeleteSyslogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTransformer  **
  - **IAM action:**  [logs:DeleteTransformer](#list_logs-action-DeleteTransformer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountPolicies  **
  - **IAM action:**  [logs:DescribeAccountPolicies](#list_logs-action-DescribeAccountPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeConfigurationTemplates  **
  - **IAM action:**  [logs:DescribeConfigurationTemplates](#list_logs-action-DescribeConfigurationTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDeliveries  **
  - **IAM action:**  [logs:DescribeDeliveries](#list_logs-action-DescribeDeliveries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDeliveryDestinations  **
  - **IAM action:**  [logs:DescribeDeliveryDestinations](#list_logs-action-DescribeDeliveryDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDeliverySources  **
  - **IAM action:**  [logs:DescribeDeliverySources](#list_logs-action-DescribeDeliverySources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDestinations  **
  - **IAM action:**  [logs:DescribeDestinations](#list_logs-action-DescribeDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeExportTasks  **
  - **IAM action:**  [logs:DescribeExportTasks](#list_logs-action-DescribeExportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeFieldIndexes  **
  - **IAM action:**  [logs:DescribeFieldIndexes](#list_logs-action-DescribeFieldIndexes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeImportTaskBatches  **
  - **IAM action:**  [logs:DescribeImportTaskBatches](#list_logs-action-DescribeImportTaskBatches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeImportTasks  **
  - **IAM action:**  [logs:DescribeImportTasks](#list_logs-action-DescribeImportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeIndexPolicies  **
  - **IAM action:**  [logs:DescribeIndexPolicies](#list_logs-action-DescribeIndexPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLogGroups  **
  - **IAM action:**  [logs:DescribeLogGroups](#list_logs-action-DescribeLogGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLogStreams  **
  - **IAM action:**  [logs:DescribeLogStreams](#list_logs-action-DescribeLogStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLookupTables  **
  - **IAM action:**  [logs:DescribeLookupTables](#list_logs-action-DescribeLookupTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMetricFilters  **
  - **IAM action:**  [logs:DescribeMetricFilters](#list_logs-action-DescribeMetricFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeQueries  **
  - **IAM action:**  [logs:DescribeQueries](#list_logs-action-DescribeQueries)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [logs:FilterLogEvents](#list_logs-action-FilterLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeQueryDefinitions  **
  - **IAM action:**  [logs:DescribeQueryDefinitions](#list_logs-action-DescribeQueryDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeResourcePolicies  **
  - **IAM action:**  [logs:DescribeResourcePolicies](#list_logs-action-DescribeResourcePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeSubscriptionFilters  **
  - **IAM action:**  [logs:DescribeSubscriptionFilters](#list_logs-action-DescribeSubscriptionFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateKmsKey  **
  - **IAM action:**  [logs:DisassociateKmsKey](#list_logs-action-DisassociateKmsKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateSourceFromS3TableIntegration  **
  - **IAM action:**  [logs:DisassociateSourceFromS3TableIntegration](#list_logs-action-DisassociateSourceFromS3TableIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FilterLogEvents  **
  - **IAM action:**  [logs:FilterLogEvents](#list_logs-action-FilterLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:Unmask](#list_logs-action-Unmask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetDataProtectionPolicy  **
  - **IAM action:**  [logs:GetDataProtectionPolicy](#list_logs-action-GetDataProtectionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDelivery  **
  - **IAM action:**  [logs:GetDelivery](#list_logs-action-GetDelivery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeliveryDestination  **
  - **IAM action:**  [logs:GetDeliveryDestination](#list_logs-action-GetDeliveryDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeliveryDestinationPolicy  **
  - **IAM action:**  [logs:GetDeliveryDestinationPolicy](#list_logs-action-GetDeliveryDestinationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeliverySource  **
  - **IAM action:**  [logs:GetDeliverySource](#list_logs-action-GetDeliverySource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegration  **
  - **IAM action:**  [logs:GetIntegration](#list_logs-action-GetIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLogAnomalyDetector  **
  - **IAM action:**  [logs:GetLogAnomalyDetector](#list_logs-action-GetLogAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLogEvents  **
  - **IAM action:**  [logs:GetLogEvents](#list_logs-action-GetLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:Unmask](#list_logs-action-Unmask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetLogFields  **
  - **IAM action:**  [logs:GetLogFields](#list_logs-action-GetLogFields) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLogGroupFields  **
  - **IAM action:**  [logs:FilterLogEvents](#list_logs-action-FilterLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:GetLogGroupFields](#list_logs-action-GetLogGroupFields)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetLogRecord  **
  - **IAM action:**  [logs:FilterLogEvents](#list_logs-action-FilterLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:GetLogRecord](#list_logs-action-GetLogRecord)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:Unmask](#list_logs-action-Unmask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetLookupTable  **
  - **IAM action:**  [logs:GetLookupTable](#list_logs-action-GetLookupTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResults  **
  - **IAM action:**  [logs:FilterLogEvents](#list_logs-action-FilterLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:GetQueryResults](#list_logs-action-GetQueryResults)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:Unmask](#list_logs-action-Unmask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetScheduledQuery  **
  - **IAM action:**  [logs:GetScheduledQuery](#list_logs-action-GetScheduledQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScheduledQueryHistory  **
  - **IAM action:**  [logs:GetScheduledQueryHistory](#list_logs-action-GetScheduledQueryHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStorageTierPolicy  **
  - **IAM action:**  [logs:GetStorageTierPolicy](#list_logs-action-GetStorageTierPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTransformer  **
  - **IAM action:**  [logs:GetTransformer](#list_logs-action-GetTransformer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAggregateLogGroupSummaries  **
  - **IAM action:**  [logs:ListAggregateLogGroupSummaries](#list_logs-action-ListAggregateLogGroupSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAnomalies  **
  - **IAM action:**  [logs:ListAnomalies](#list_logs-action-ListAnomalies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntegrations  **
  - **IAM action:**  [logs:ListIntegrations](#list_logs-action-ListIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLogAnomalyDetectors  **
  - **IAM action:**  [logs:ListLogAnomalyDetectors](#list_logs-action-ListLogAnomalyDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLogGroups  **
  - **IAM action:**  [logs:DescribeLogGroups](#list_logs-action-DescribeLogGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [logs:ListLogGroups](#list_logs-action-ListLogGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListLogGroupsForQuery  **
  - **IAM action:**  [logs:ListLogGroupsForQuery](#list_logs-action-ListLogGroupsForQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScheduledQueries  **
  - **IAM action:**  [logs:ListScheduledQueries](#list_logs-action-ListScheduledQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourcesForS3TableIntegration  **
  - **IAM action:**  [logs:ListSourcesForS3TableIntegration](#list_logs-action-ListSourcesForS3TableIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSyslogConfigurations  **
  - **IAM action:**  [logs:ListSyslogConfigurations](#list_logs-action-ListSyslogConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [logs:ListTagsForResource](#list_logs-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsLogGroup  **
  - **IAM action:**  [logs:ListTagsLogGroup](#list_logs-action-ListTagsLogGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAccountPolicy  **
  - **IAM action:**  [logs:PutAccountPolicy](#list_logs-action-PutAccountPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:PutDataProtectionPolicy](#list_logs-action-PutDataProtectionPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:PutIndexPolicy](#list_logs-action-PutIndexPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:PutRetentionPolicy](#list_logs-action-PutRetentionPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:PutSubscriptionFilter](#list_logs-action-PutSubscriptionFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:PutTransformer](#list_logs-action-PutTransformer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com / **Access level:** Write

- **   PutBearerTokenAuthentication  **
  - **IAM action:**  [logs:PutBearerTokenAuthentication](#list_logs-action-PutBearerTokenAuthentication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDataProtectionPolicy  **
  - **IAM action:**  [logs:PutDataProtectionPolicy](#list_logs-action-PutDataProtectionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDeliveryDestination  **
  - **IAM action:**  [logs:PutDeliveryDestination](#list_logs-action-PutDeliveryDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutDeliveryDestinationPolicy  **
  - **IAM action:**  [logs:PutDeliveryDestinationPolicy](#list_logs-action-PutDeliveryDestinationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDeliverySource  **
  - **IAM action:**  [logs:PutDeliverySource](#list_logs-action-PutDeliverySource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutDestination  **
  - **IAM action:**  [logs:PutDestination](#list_logs-action-PutDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com / **Access level:** Write

- **   PutDestinationPolicy  **
  - **IAM action:**  [logs:PutDestinationPolicy](#list_logs-action-PutDestinationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutIndexPolicy  **
  - **IAM action:**  [logs:PutIndexPolicy](#list_logs-action-PutIndexPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutIntegration  **
  - **IAM action:**  [logs:PutIntegration](#list_logs-action-PutIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutLogEvents  **
  - **IAM action:**  [logs:PutLogEvents](#list_logs-action-PutLogEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutLogGroupDeletionProtection  **
  - **IAM action:**  [logs:PutLogGroupDeletionProtection](#list_logs-action-PutLogGroupDeletionProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMetricFilter  **
  - **IAM action:**  [logs:PutMetricFilter](#list_logs-action-PutMetricFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutQueryDefinition  **
  - **IAM action:**  [logs:PutQueryDefinition](#list_logs-action-PutQueryDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [logs:PutResourcePolicy](#list_logs-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutRetentionPolicy  **
  - **IAM action:**  [logs:PutRetentionPolicy](#list_logs-action-PutRetentionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutStorageTierPolicy  **
  - **IAM action:**  [logs:PutStorageTierPolicy](#list_logs-action-PutStorageTierPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSubscriptionFilter  **
  - **IAM action:**  [logs:PutSubscriptionFilter](#list_logs-action-PutSubscriptionFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com / **Access level:** Write

- **   PutSyslogConfiguration  **
  - **IAM action:**  [logs:PutSyslogConfiguration](#list_logs-action-PutSyslogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTransformer  **
  - **IAM action:**  [logs:PutTransformer](#list_logs-action-PutTransformer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQuery  **
  - **IAM action:**  [logs:DescribeLogGroups](#list_logs-action-DescribeLogGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [logs:DescribeQueryDefinitions](#list_logs-action-DescribeQueryDefinitions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [logs:FilterLogEvents](#list_logs-action-FilterLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:StartQuery](#list_logs-action-StartQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:Unmask](#list_logs-action-Unmask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   StopQuery  **
  - **IAM action:**  [logs:FilterLogEvents](#list_logs-action-FilterLogEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:StopQuery](#list_logs-action-StopQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   TagLogGroup  **
  - **IAM action:**  [logs:TagLogGroup](#list_logs-action-TagLogGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [logs:TagResource](#list_logs-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestMetricFilter  **
  - **IAM action:**  [logs:TestMetricFilter](#list_logs-action-TestMetricFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TestTransformer  **
  - **IAM action:**  [logs:TestTransformer](#list_logs-action-TestTransformer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UntagLogGroup  **
  - **IAM action:**  [logs:UntagLogGroup](#list_logs-action-UntagLogGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [logs:UntagResource](#list_logs-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAnomaly  **
  - **IAM action:**  [logs:UpdateAnomaly](#list_logs-action-UpdateAnomaly) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDeliveryConfiguration  **
  - **IAM action:**  [logs:UpdateDeliveryConfiguration](#list_logs-action-UpdateDeliveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLogAnomalyDetector  **
  - **IAM action:**  [logs:UpdateLogAnomalyDetector](#list_logs-action-UpdateLogAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLookupTable  **
  - **IAM action:**  [logs:GetQueryResults](#list_logs-action-GetQueryResults)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [logs:UpdateLookupTable](#list_logs-action-UpdateLookupTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateScheduledQuery  **
  - **IAM action:**  [logs:UpdateScheduledQuery](#list_logs-action-UpdateScheduledQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com / **Access level:** Write



## Actions defined by Amazon CloudWatch Logs
<a name="list_logs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateKmsKey](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AssociateKmsKey.html)  **
  - **Description:** Grants permission to associate the specified AWS Key Management Service (AWS KMS) customer master key (CMK) with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateSourceToS3TableIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AssociateSourceToS3TableIntegration.html)  **
  - **Description:** Grants permission to associate a log source to an S3 Tables integration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelExportTask](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.html)  **
  - **Description:** Grants permission to cancel an export task if it is in PENDING or RUNNING state
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelImportTask](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CancelImportTask.html)  **
  - **Description:** Grants permission to cancel an import from CloudTrail Lake to CloudWatch
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html)  **
  - **Description:** Grants permission to create a delivery connecting a delivery source to a delivery destination
  - **Resource types (\*required):** [delivery\*](#list_logs-resource-delivery) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-source\*](#list_logs-resource-delivery-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExportTask](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateExportTask.html)  **
  - **Description:** Grants permission to create an ExportTask which allows you to efficiently export data from a Log Group to your Amazon S3 bucket
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateImportTask](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateImportTask.html)  **
  - **Description:** Grants permission to start an asynchronous process to import data from a CloudTrail Lake event data store into a managed log group in CloudWatch
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.html)  **
  - **Description:** Grants permission to create a log anomaly detector
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html)  **
  - **Description:** Grants permission to create a new log group with the specified name
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLogStream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html)  **
  - **Description:** Grants permission to create a new log stream with the specified name
  - **Resource types (\*required):** [log-stream\*](#list_logs-resource-log-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLookupTable](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLookupTable.html)  **
  - **Description:** Grants permission to create a lookup table
  - **Resource types (\*required):** [lookup-table\*](#list_logs-resource-lookup-table)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateScheduledQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateScheduledQuery.html)  **
  - **Description:** Grants permission to create a scheduled query
  - **Resource types (\*required):** [scheduled-query\*](#list_logs-resource-scheduled-query)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccountPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteAccountPolicy.html)  **
  - **Description:** Grants permission to delete an account policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataProtectionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDataProtectionPolicy.html)  **
  - **Description:** Grants permission to delete a data protection policy attached to a log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.html)  **
  - **Description:** Grants permission to delete a delivery
  - **Resource types (\*required):** [delivery\*](#list_logs-resource-delivery)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestination.html)  **
  - **Description:** Grants permission to delete a delivery destination after all associated deliveries are deleted
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestinationPolicy.html)  **
  - **Description:** Grants permission to delete a delivery destination policy associated with a delivery destination
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.html)  **
  - **Description:** Grants permission to delete a delivery source after all associated deliveries are deleted
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDestination.html)  **
  - **Description:** Grants permission to delete the destination with the specified name
  - **Resource types (\*required):** [destination\*](#list_logs-resource-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteIndexPolicy.html)  **
  - **Description:** Grants permission to delete an index policy attached to a log group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete the integration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogAnomalyDetector.html)  **
  - **Description:** Grants permission to delete a log anomaly detector
  - **Resource types (\*required):** [anomaly-detector\*](#list_logs-resource-anomaly-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.html)  **
  - **Description:** Grants permission to delete the log group with the specified name
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLogStream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogStream.html)  **
  - **Description:** Grants permission to delete a log stream
  - **Resource types (\*required):** [log-stream\*](#list_logs-resource-log-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLookupTable](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLookupTable.html)  **
  - **Description:** Grants permission to delete a lookup table
  - **Resource types (\*required):** [lookup-table\*](#list_logs-resource-lookup-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMetricFilter](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteMetricFilter.html)  **
  - **Description:** Grants permission to delete a metric filter associated with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQueryDefinition](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteQueryDefinition.html)  **
  - **Description:** Grants permission to delete a saved CloudWatch Logs Insights query definition
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy from this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeleteRetentionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html)  **
  - **Description:** Grants permission to delete the retention policy of the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScheduledQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteScheduledQuery.html)  **
  - **Description:** Grants permission to delete a scheduled query
  - **Resource types (\*required):** [scheduled-query\*](#list_logs-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSubscriptionFilter](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteSubscriptionFilter.html)  **
  - **Description:** Grants permission to delete a subscription filter associated with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSyslogConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteSyslogConfiguration.html)  **
  - **Description:** Grants permission to delete syslog configuration for the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteTransformer.html)  **
  - **Description:** Grants permission to delete a transformer associated with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountPolicies](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeAccountPolicies.html)  **
  - **Description:** Grants permission to retrieve account policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeConfigurationTemplates](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html)  **
  - **Description:** Grants permission to retrieve a list of configuration templates of available log types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDeliveries](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.html)  **
  - **Description:** Grants permission to retrieve a list of deliveries an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDeliveryDestinations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.html)  **
  - **Description:** Grants permission to retrieve a list of delivery destinations an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDeliverySources](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliverySources.html)  **
  - **Description:** Grants permission to retrieve a list of delivery sources in an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDestinations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDestinations.html)  **
  - **Description:** Grants permission to return all the destinations that are associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeExportTasks](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.html)  **
  - **Description:** Grants permission to return all the export tasks that are associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeFieldIndexes](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeFieldIndexes.html)  **
  - **Description:** Grants permission to return all the indexing attributes that are attached with the log groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeImportTaskBatches](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeImportTaskBatches.html)  **
  - **Description:** Grants permission to return detailed information about the individual batches within an import task, including status and any error
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeImportTasks](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeImportTasks.html)  **
  - **Description:** Grants permission to return all the import tasks associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeIndexPolicies](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeIndexPolicies.html)  **
  - **Description:** Grants permission to return all the index policies that are attached with the log groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLogGroups](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html)  **
  - **Description:** Grants permission to return all the log groups that are associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLogStreams](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.html)  **
  - **Description:** Grants permission to return all the log streams that are associated with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeLookupTables](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLookupTables.html)  **
  - **Description:** Grants permission to return all lookup tables
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMetricFilters](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeMetricFilters.html)  **
  - **Description:** Grants permission to return all the metrics filters associated with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeQueries](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueries.html)  **
  - **Description:** Grants permission to return a list of CloudWatch Logs Insights queries that are scheduled, executing, or have been executed recently in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeQueryDefinitions](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html)  **
  - **Description:** Grants permission to return a paginated list of your saved CloudWatch Logs Insights query definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeResourcePolicies](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeResourcePolicies.html)  **
  - **Description:** Grants permission to return all the resource policies in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeSubscriptionFilters](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.html)  **
  - **Description:** Grants permission to return all the subscription filters associated with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DisassociateKmsKey](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DisassociateKmsKey.html)  **
  - **Description:** Grants permission to disassociate the associated AWS Key Management Service (AWS KMS) customer master key (CMK) from the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSourceFromS3TableIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DisassociateSourceFromS3TableIntegration.html)  **
  - **Description:** Grants permission to disassociate a log source from an S3 Tables integration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [FilterLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html)  **
  - **Description:** Grants permission to retrieve log events, optionally filtered by a filter pattern from the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataProtectionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDataProtectionPolicy.html)  **
  - **Description:** Grants permission to retrieve a data protection policy attached to a log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDelivery.html)  **
  - **Description:** Grants permission to retrieve a single delivery
  - **Resource types (\*required):** [delivery\*](#list_logs-resource-delivery)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestination.html)  **
  - **Description:** Grants permission to retrieve a single delivery destination
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestinationPolicy.html)  **
  - **Description:** Grants permission to retrieve a delivery destination policy attached to a delivery destination
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDeliverySource.html)  **
  - **Description:** Grants permission to retrieve a single delivery source
  - **Resource types (\*required):** [delivery-source\*](#list_logs-resource-delivery-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetIntegration.html)  **
  - **Description:** Grants permission to retrieve a single integration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogAnomalyDetector.html)  **
  - **Description:** Grants permission to get a log anomaly detector
  - **Resource types (\*required):** [anomaly-detector\*](#list_logs-resource-anomaly-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html)  **
  - **Description:** Grants permission to retrieve log events from the specified log stream
  - **Resource types (\*required):** [log-stream\*](#list_logs-resource-log-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLogFields](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogFields.html)  **
  - **Description:** Grants permission to retrieve a list of log fields for a data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLogGroupFields](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.html)  **
  - **Description:** Grants permission to return a list of the fields that are included in log events in the specified log group, along with the percentage of log events that contain each field
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLogRecord](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.html)  **
  - **Description:** Grants permission to retrieve all the fields and values of a single log event
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLookupTable](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLookupTable.html)  **
  - **Description:** Grants permission to retrieve a lookup table
  - **Resource types (\*required):** [lookup-table\*](#list_logs-resource-lookup-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResults](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html)  **
  - **Description:** Grants permission to return the results from the specified query
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetScheduledQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetScheduledQuery.html)  **
  - **Description:** Grants permission to retrieve information about a specified scheduled query
  - **Resource types (\*required):** [scheduled-query\*](#list_logs-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetScheduledQueryHistory](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetScheduledQueryHistory.html)  **
  - **Description:** Grants permission to return the execution history for a specified scheduled query
  - **Resource types (\*required):** [scheduled-query\*](#list_logs-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStorageTierPolicy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cwl_intelligent_tier.html)  **
  - **Description:** Grants permission to retrieve the storage tier policy for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetTransformer.html)  **
  - **Description:** Grants permission to return transformer associated with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAggregateLogGroupSummaries](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAggregateLogGroupSummaries.html)  **
  - **Description:** Grants permission to return an aggregate summary of all log groups in the region grouped by specified data-source characteristics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAnomalies](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html)  **
  - **Description:** Grants permission to list all anomalies detected in the AWS account making the request
  - **Resource types (\*required):** [anomaly-detector](#list_logs-resource-anomaly-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntegrations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html)  **
  - **Description:** Grants permission to list all integrations associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLogAnomalyDetectors](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogAnomalyDetectors.html)  **
  - **Description:** Grants permission to return all the anomaly detectors that are associated with the AWS account making the request
  - **Resource types (\*required):** [anomaly-detector](#list_logs-resource-anomaly-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLogGroups](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogGroups.html)  **
  - **Description:** Grants permission to return all the log groups that are associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLogGroupsForQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogGroupsForQuery.html)  **
  - **Description:** Grants permission to return all the log groups that are associated with the specified query
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListScheduledQueries](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListScheduledQueries.html)  **
  - **Description:** Grants permission to return all scheduled queries that are associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSourcesForS3TableIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListSourcesForS3TableIntegration.html)  **
  - **Description:** Grants permission to return all log sources associated with an S3 Tables integration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSyslogConfigurations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListSyslogConfigurations.html)  **
  - **Description:** Grants permission to return all syslog configurations associated with the AWS account making the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified resource
  - **Resource types (\*required):** [anomaly-detector](#list_logs-resource-anomaly-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [delivery](#list_logs-resource-delivery) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [delivery-destination](#list_logs-resource-delivery-destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [delivery-source](#list_logs-resource-delivery-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [destination](#list_logs-resource-destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [log-group](#list_logs-resource-log-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [lookup-table](#list_logs-resource-lookup-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsLogGroup.html)  **
  - **Description:** Grants permission to list the tags for the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutAccountPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html)  **
  - **Description:** Grants permission to attach an account policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutBearerTokenAuthentication](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutBearerTokenAuthentication.html)  **
  - **Description:** Grants permission to enable or disable bearer token based authentication for the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDataProtectionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html)  **
  - **Description:** Grants permission to attach a data protection policy to detect and redact sensitive information from log events
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html)  **
  - **Description:** Grants permission to create/update a delivery destination
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)<br />[logs:DeliveryDestinationResourceArn](#list_logs-logs_DeliveryDestinationResourceArn)
  - **Access level:** Write

- **   [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html)  **
  - **Description:** Grants permission to attach a delivery destination policy to a delivery destination
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html)  **
  - **Description:** Grants permission to create/update a delivery source
  - **Resource types (\*required):** [delivery-source\*](#list_logs-resource-delivery-source)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)<br />[logs:LogGeneratingResourceArns](#list_logs-logs_LogGeneratingResourceArns)
  - **Access level:** Write

- **   [PutDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html)  **
  - **Description:** Grants permission to create or update a Destination
  - **Resource types (\*required):** [destination\*](#list_logs-resource-destination)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Write

- **   [PutDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.html)  **
  - **Description:** Grants permission to create or update an access policy associated with an existing Destination
  - **Resource types (\*required):** [destination\*](#list_logs-resource-destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html)  **
  - **Description:** Grants permission to attach an index policy at log group level to optimize search and query
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIntegration.html)  **
  - **Description:** Grants permission to create integration between cloudwatch logs and opensearch
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)  **
  - **Description:** Grants permission to upload a batch of log events to the specified log stream
  - **Resource types (\*required):** [log-stream\*](#list_logs-resource-log-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutLogGroupDeletionProtection](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogGroupDeletionProtection.html)  **
  - **Description:** Grants permission to enable or disable deletion protection for the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutMetricFilter](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutMetricFilter.html)  **
  - **Description:** Grants permission to create or update a metric filter and associates it with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutQueryDefinition](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.html)  **
  - **Description:** Grants permission to create or update a query definition
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update a resource policy allowing other AWS services to put log events to this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutRetentionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.html)  **
  - **Description:** Grants permission to set the retention of the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutStorageTierPolicy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cwl_intelligent_tier.html)  **
  - **Description:** Grants permission to set the storage tier policy for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutSubscriptionFilter](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.html)  **
  - **Description:** Grants permission to create or update a subscription filter and associates it with the specified log group
  - **Resource types (\*required):** [destination](#list_logs-resource-destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutSyslogConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutSyslogConfiguration.html)  **
  - **Description:** Grants permission to add syslog configuration for the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html)  **
  - **Description:** Grants permission to create or update a transformer and associates it with the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartLiveTail](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartLiveTail.html)  **
  - **Description:** Grants permission to start a Live Tail session in CloudWatch Logs
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html)  **
  - **Description:** Grants permission to schedule a query of a log group using CloudWatch Logs Insights
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StopQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StopQuery.html)  **
  - **Description:** Grants permission to stop a CloudWatch Logs Insights query that is in progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagLogGroup.html)  **
  - **Description:** Grants permission to add or update the specified tags for the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or update the specified tags for the specified resource
  - **Resource types (\*required):** [anomaly-detector](#list_logs-resource-anomaly-detector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery](#list_logs-resource-delivery) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-destination](#list_logs-resource-delivery-destination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-source](#list_logs-resource-delivery-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [destination](#list_logs-resource-destination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [log-group](#list_logs-resource-log-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [lookup-table](#list_logs-resource-lookup-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [scheduled-query](#list_logs-resource-scheduled-query) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestMetricFilter](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TestMetricFilter.html)  **
  - **Description:** Grants permission to test the filter pattern of a metric filter against a sample of log event messages
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TestTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TestTransformer.html)  **
  - **Description:** Grants permission to test the transformer against a sample of log event messages
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [UntagLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagLogGroup.html)  **
  - **Description:** Grants permission to remove the specified tags from the specified log group
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the specified resource
  - **Resource types (\*required):** [anomaly-detector](#list_logs-resource-anomaly-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery](#list_logs-resource-delivery) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-destination](#list_logs-resource-delivery-destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-source](#list_logs-resource-delivery-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [destination](#list_logs-resource-destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [log-group](#list_logs-resource-log-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [lookup-table](#list_logs-resource-lookup-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [scheduled-query](#list_logs-resource-scheduled-query) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAnomaly](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateAnomaly.html)  **
  - **Description:** Grants permission to update an anomaly reported by a log anomaly detector
  - **Resource types (\*required):** [anomaly-detector\*](#list_logs-resource-anomaly-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html)  **
  - **Description:** Grants permission to update configuration related to a delivery
  - **Resource types (\*required):** [delivery\*](#list_logs-resource-delivery) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-destination\*](#list_logs-resource-delivery-destination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Resource types (\*required):** [delivery-source\*](#list_logs-resource-delivery-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_logs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_logs-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateLogAnomalyDetector.html)  **
  - **Description:** Grants permission to update a log anomaly detector
  - **Resource types (\*required):** [anomaly-detector\*](#list_logs-resource-anomaly-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLookupTable](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateLookupTable.html)  **
  - **Description:** Grants permission to update a lookup table
  - **Resource types (\*required):** [lookup-table\*](#list_logs-resource-lookup-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateScheduledQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateScheduledQuery.html)  **
  - **Description:** Grants permission to update a scheduled query
  - **Resource types (\*required):** [scheduled-query\*](#list_logs-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon CloudWatch Logs
<a name="list_logs-permission-only-actions"></a>

The following actions are defined by Amazon CloudWatch Logs but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CallWithBearerToken](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)  **
  - **Description:** Grants permission to authenticate requests using bearer token
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateLogDelivery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)  **
  - **Description:** Grants permission to create the log delivery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLogDelivery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)  **
  - **Description:** Grants permission to delete the log delivery information for specified log delivery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePipelineRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html)  **
  - **Description:** Grants permission to delete telemetry pipeline
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetLogDelivery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)  **
  - **Description:** Grants permission to get the log delivery information for specified log delivery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [IntegrateWithS3Table](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html)  **
  - **Description:** Grants permission to deliver log events to S3 Tables
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[logs:data\_source\_name](#list_logs-logs_data_source_name)<br />[logs:data\_source\_type](#list_logs-logs_data_source_type)
  - **Access level:** Write

- **   [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html#CloudWatch-Unified-Cross-Account-Setup-permissions)  **
  - **Description:** Grants permission to share CloudWatch resources with a monitoring account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListEntitiesForLogGroup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html)  **
  - **Description:** Grants permission to retrieve all the entities that are associated with log group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLogDeliveries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)  **
  - **Description:** Grants permission to list all the log deliveries for specified account and/or log source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLogGroupsForEntity](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html)  **
  - **Description:** Grants permission to retrieve all the log groups that are associated with entity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ProcessWithPipeline](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html)  **
  - **Description:** Grants permission to process and transform log events through pipeline transformers before storage
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)<br />[logs:data\_source\_name](#list_logs-logs_data_source_name)<br />[logs:data\_source\_type](#list_logs-logs_data_source_type)
  - **Access level:** Write

- **   [PutPipelineRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html)  **
  - **Description:** Grants permission to create telemetry pipeline
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopLiveTail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html)  **
  - **Description:** Grants permission to stop a Live Tail session that is in progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [Unmask](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html)  **
  - **Description:** Grants permission to fetch unmasked log events that have been redacted with a data protection policy
  - **Resource types (\*required):** [log-group\*](#list_logs-resource-log-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UpdateLogDelivery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)  **
  - **Description:** Grants permission to update the log delivery information for specified log delivery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon CloudWatch Logs
<a name="list_logs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [anomaly-detector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AnomalyDetector.html)  | arn:${Partition}:logs:${Region}:${Account}:anomaly-detector:${DetectorId} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [delivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html)  | arn:${Partition}:logs:${Region}:${Account}:delivery:${DeliveryName} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [delivery-destination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliveryDestination.html)  | arn:${Partition}:logs:${Region}:${Account}:delivery-destination:${DeliveryDestinationName} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [delivery-source](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliverySource.html)  | arn:${Partition}:logs:${Region}:${Account}:delivery-source:${DeliverySourceName} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [destination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Destination.html)  | arn:${Partition}:logs:${Region}:${Account}:destination:${DestinationName} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [log-group](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogGroup.html)  | arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [log-stream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogStream.html)  | arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [lookup-table](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LookupTable.html)  | arn:${Partition}:logs:${Region}:${Account}:lookup-table:${LookupTableName} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 
|  [scheduled-query](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ScheduledQuery.html)  | arn:${Partition}:logs:${Region}:${Account}:scheduled-query:${ScheduledQueryId} | [aws:ResourceTag/${TagKey}](#list_logs-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Logs
<a name="list_logs-policy-keys"></a>

Amazon CloudWatch Logs defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [logs:DeliveryDestinationResourceArn](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html)  | Filters access by the Log Destination ARN passed in the request | ARN | 
|   [logs:LogGeneratingResourceArns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html)  | Filters access by the Log Generating Resource ARNs passed in the request | ArrayOfARN | 
|   [logs:data\_source\_name](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html)  | Filters access by the data source name passed in the request | String | 
|   [logs:data\_source\_type](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html)  | Filters access by the data source type passed in the request | String | 