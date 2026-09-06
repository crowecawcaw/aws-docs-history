

# Actions, resources, and condition keys for AWS Config
<a name="list_config"></a>

AWS Config (service prefix: `config`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/config/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/config/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/config/latest/developerguide/example-policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/config/config.json) for this service.

**Topics**
+ [API operations defined by AWS Config](#list_config-operations)
+ [Actions defined by AWS Config](#list_config-actions-as-permissions)
+ [Resource types defined by AWS Config](#list_config-resources-for-iam-policies)
+ [Condition keys for AWS Config](#list_config-policy-keys)

## API operations defined by AWS Config
<a name="list_config-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_config-actions-as-permissions).




- **   AssociateResourceTypes  **
  - **IAM action:**  [config:AssociateResourceTypes](#list_config-action-AssociateResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetAggregateResourceConfig  **
  - **IAM action:**  [config:BatchGetAggregateResourceConfig](#list_config-action-BatchGetAggregateResourceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetResourceConfig  **
  - **IAM action:**  [config:BatchGetResourceConfig](#list_config-action-BatchGetResourceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DeleteAggregationAuthorization  **
  - **IAM action:**  [config:DeleteAggregationAuthorization](#list_config-action-DeleteAggregationAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigRule  **
  - **IAM action:**  [config:DeleteConfigRule](#list_config-action-DeleteConfigRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationAggregator  **
  - **IAM action:**  [config:DeleteConfigurationAggregator](#list_config-action-DeleteConfigurationAggregator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationRecorder  **
  - **IAM action:**  [config:DeleteConfigurationRecorder](#list_config-action-DeleteConfigurationRecorder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConformancePack  **
  - **IAM action:**  [config:DeleteConformancePack](#list_config-action-DeleteConformancePack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnector  **
  - **IAM action:**  [config:DeleteConnector](#list_config-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeliveryChannel  **
  - **IAM action:**  [config:DeleteDeliveryChannel](#list_config-action-DeleteDeliveryChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEvaluationResults  **
  - **IAM action:**  [config:DeleteEvaluationResults](#list_config-action-DeleteEvaluationResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOrganizationConfigRule  **
  - **IAM action:**  [config:DeleteOrganizationConfigRule](#list_config-action-DeleteOrganizationConfigRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOrganizationConformancePack  **
  - **IAM action:**  [config:DeleteOrganizationConformancePack](#list_config-action-DeleteOrganizationConformancePack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePendingAggregationRequest  **
  - **IAM action:**  [config:DeletePendingAggregationRequest](#list_config-action-DeletePendingAggregationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRemediationConfiguration  **
  - **IAM action:**  [config:DeleteRemediationConfiguration](#list_config-action-DeleteRemediationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRemediationExceptions  **
  - **IAM action:**  [config:DeleteRemediationExceptions](#list_config-action-DeleteRemediationExceptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceConfig  **
  - **IAM action:**  [config:DeleteResourceConfig](#list_config-action-DeleteResourceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRetentionConfiguration  **
  - **IAM action:**  [config:DeleteRetentionConfiguration](#list_config-action-DeleteRetentionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceLinkedConfigurationRecorder  **
  - **IAM action:**  [config:DeleteServiceLinkedConfigurationRecorder](#list_config-action-DeleteServiceLinkedConfigurationRecorder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStoredQuery  **
  - **IAM action:**  [config:DeleteStoredQuery](#list_config-action-DeleteStoredQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeliverConfigSnapshot  **
  - **IAM action:**  [config:DeliverConfigSnapshot](#list_config-action-DeliverConfigSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAggregateComplianceByConfigRules  **
  - **IAM action:**  [config:DescribeAggregateComplianceByConfigRules](#list_config-action-DescribeAggregateComplianceByConfigRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAggregateComplianceByConformancePacks  **
  - **IAM action:**  [config:DescribeAggregateComplianceByConformancePacks](#list_config-action-DescribeAggregateComplianceByConformancePacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAggregationAuthorizations  **
  - **IAM action:**  [config:DescribeAggregationAuthorizations](#list_config-action-DescribeAggregationAuthorizations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeComplianceByConfigRule  **
  - **IAM action:**  [config:DescribeComplianceByConfigRule](#list_config-action-DescribeComplianceByConfigRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeComplianceByResource  **
  - **IAM action:**  [config:DescribeComplianceByResource](#list_config-action-DescribeComplianceByResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigRuleEvaluationStatus  **
  - **IAM action:**  [config:DescribeConfigRuleEvaluationStatus](#list_config-action-DescribeConfigRuleEvaluationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigRules  **
  - **IAM action:**  [config:DescribeConfigRules](#list_config-action-DescribeConfigRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeConfigurationAggregatorSourcesStatus  **
  - **IAM action:**  [config:DescribeConfigurationAggregatorSourcesStatus](#list_config-action-DescribeConfigurationAggregatorSourcesStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigurationAggregators  **
  - **IAM action:**  [config:DescribeConfigurationAggregators](#list_config-action-DescribeConfigurationAggregators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeConfigurationRecorderStatus  **
  - **IAM action:**  [config:DescribeConfigurationRecorderStatus](#list_config-action-DescribeConfigurationRecorderStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigurationRecorders  **
  - **IAM action:**  [config:DescribeConfigurationRecorders](#list_config-action-DescribeConfigurationRecorders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConformancePackCompliance  **
  - **IAM action:**  [config:DescribeConformancePackCompliance](#list_config-action-DescribeConformancePackCompliance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConformancePackStatus  **
  - **IAM action:**  [config:DescribeConformancePackStatus](#list_config-action-DescribeConformancePackStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConformancePacks  **
  - **IAM action:**  [config:DescribeConformancePacks](#list_config-action-DescribeConformancePacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDeliveryChannelStatus  **
  - **IAM action:**  [config:DescribeDeliveryChannelStatus](#list_config-action-DescribeDeliveryChannelStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDeliveryChannels  **
  - **IAM action:**  [config:DescribeDeliveryChannels](#list_config-action-DescribeDeliveryChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOrganizationConfigRuleStatuses  **
  - **IAM action:**  [config:DescribeOrganizationConfigRuleStatuses](#list_config-action-DescribeOrganizationConfigRuleStatuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationConfigRules  **
  - **IAM action:**  [config:DescribeOrganizationConfigRules](#list_config-action-DescribeOrganizationConfigRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOrganizationConformancePackStatuses  **
  - **IAM action:**  [config:DescribeOrganizationConformancePackStatuses](#list_config-action-DescribeOrganizationConformancePackStatuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationConformancePacks  **
  - **IAM action:**  [config:DescribeOrganizationConformancePacks](#list_config-action-DescribeOrganizationConformancePacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePendingAggregationRequests  **
  - **IAM action:**  [config:DescribePendingAggregationRequests](#list_config-action-DescribePendingAggregationRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeRemediationConfigurations  **
  - **IAM action:**  [config:DescribeRemediationConfigurations](#list_config-action-DescribeRemediationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeRemediationExceptions  **
  - **IAM action:**  [config:DescribeRemediationExceptions](#list_config-action-DescribeRemediationExceptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeRemediationExecutionStatus  **
  - **IAM action:**  [config:DescribeRemediationExecutionStatus](#list_config-action-DescribeRemediationExecutionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRetentionConfigurations  **
  - **IAM action:**  [config:DescribeRetentionConfigurations](#list_config-action-DescribeRetentionConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateResourceTypes  **
  - **IAM action:**  [config:DisassociateResourceTypes](#list_config-action-DisassociateResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAggregateComplianceDetailsByConfigRule  **
  - **IAM action:**  [config:GetAggregateComplianceDetailsByConfigRule](#list_config-action-GetAggregateComplianceDetailsByConfigRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAggregateConfigRuleComplianceSummary  **
  - **IAM action:**  [config:GetAggregateConfigRuleComplianceSummary](#list_config-action-GetAggregateConfigRuleComplianceSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAggregateConformancePackComplianceSummary  **
  - **IAM action:**  [config:GetAggregateConformancePackComplianceSummary](#list_config-action-GetAggregateConformancePackComplianceSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAggregateDiscoveredResourceCounts  **
  - **IAM action:**  [config:GetAggregateDiscoveredResourceCounts](#list_config-action-GetAggregateDiscoveredResourceCounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAggregateResourceConfig  **
  - **IAM action:**  [config:GetAggregateResourceConfig](#list_config-action-GetAggregateResourceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComplianceDetailsByConfigRule  **
  - **IAM action:**  [config:GetComplianceDetailsByConfigRule](#list_config-action-GetComplianceDetailsByConfigRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComplianceDetailsByResource  **
  - **IAM action:**  [config:GetComplianceDetailsByResource](#list_config-action-GetComplianceDetailsByResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComplianceSummaryByConfigRule  **
  - **IAM action:**  [config:GetComplianceSummaryByConfigRule](#list_config-action-GetComplianceSummaryByConfigRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComplianceSummaryByResourceType  **
  - **IAM action:**  [config:GetComplianceSummaryByResourceType](#list_config-action-GetComplianceSummaryByResourceType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConformancePackComplianceDetails  **
  - **IAM action:**  [config:GetConformancePackComplianceDetails](#list_config-action-GetConformancePackComplianceDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConformancePackComplianceSummary  **
  - **IAM action:**  [config:GetConformancePackComplianceSummary](#list_config-action-GetConformancePackComplianceSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnector  **
  - **IAM action:**  [config:GetConnector](#list_config-action-GetConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomRulePolicy  **
  - **IAM action:**  [config:GetCustomRulePolicy](#list_config-action-GetCustomRulePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDiscoveredResourceCounts  **
  - **IAM action:**  [config:GetDiscoveredResourceCounts](#list_config-action-GetDiscoveredResourceCounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrganizationConfigRuleDetailedStatus  **
  - **IAM action:**  [config:GetOrganizationConfigRuleDetailedStatus](#list_config-action-GetOrganizationConfigRuleDetailedStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrganizationConformancePackDetailedStatus  **
  - **IAM action:**  [config:GetOrganizationConformancePackDetailedStatus](#list_config-action-GetOrganizationConformancePackDetailedStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrganizationCustomRulePolicy  **
  - **IAM action:**  [config:GetOrganizationCustomRulePolicy](#list_config-action-GetOrganizationCustomRulePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceConfigHistory  **
  - **IAM action:**  [config:GetResourceConfigHistory](#list_config-action-GetResourceConfigHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceEvaluationSummary  **
  - **IAM action:**  [config:GetResourceEvaluationSummary](#list_config-action-GetResourceEvaluationSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStoredQuery  **
  - **IAM action:**  [config:GetStoredQuery](#list_config-action-GetStoredQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAggregateDiscoveredResources  **
  - **IAM action:**  [config:ListAggregateDiscoveredResources](#list_config-action-ListAggregateDiscoveredResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationRecorders  **
  - **IAM action:**  [config:ListConfigurationRecorders](#list_config-action-ListConfigurationRecorders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConformancePackComplianceScores  **
  - **IAM action:**  [config:ListConformancePackComplianceScores](#list_config-action-ListConformancePackComplianceScores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectors  **
  - **IAM action:**  [config:ListConnectors](#list_config-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDiscoveredResources  **
  - **IAM action:**  [config:ListDiscoveredResources](#list_config-action-ListDiscoveredResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceEvaluations  **
  - **IAM action:**  [config:ListResourceEvaluations](#list_config-action-ListResourceEvaluations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStoredQueries  **
  - **IAM action:**  [config:ListStoredQueries](#list_config-action-ListStoredQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [config:ListTagsForResource](#list_config-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAggregationAuthorization  **
  - **IAM action:**  [config:PutAggregationAuthorization](#list_config-action-PutAggregationAuthorization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutConfigRule  **
  - **IAM action:**  [config:PutConfigRule](#list_config-action-PutConfigRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutConfigurationAggregator  **
  - **IAM action:**  [config:PutConfigurationAggregator](#list_config-action-PutConfigurationAggregator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** config.amazonaws.com / **Access level:** Write

- **   PutConfigurationRecorder  **
  - **IAM action:**  [config:PutConfigurationRecorder](#list_config-action-PutConfigurationRecorder)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** config.amazonaws.com / **Access level:** Write

- **   PutConformancePack  **
  - **IAM action:**  [config:PutConformancePack](#list_config-action-PutConformancePack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   PutConnector  **
  - **IAM action:**  [config:PutConnector](#list_config-action-PutConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutDeliveryChannel  **
  - **IAM action:**  [config:PutDeliveryChannel](#list_config-action-PutDeliveryChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEvaluations  **
  - **IAM action:**  [config:PutEvaluations](#list_config-action-PutEvaluations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutExternalEvaluation  **
  - **IAM action:**  [config:PutExternalEvaluation](#list_config-action-PutExternalEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutOrganizationConfigRule  **
  - **IAM action:**  [config:PutOrganizationConfigRule](#list_config-action-PutOrganizationConfigRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutOrganizationConformancePack  **
  - **IAM action:**  [config:PutOrganizationConformancePack](#list_config-action-PutOrganizationConformancePack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   PutRemediationConfigurations  **
  - **IAM action:**  [config:PutRemediationConfigurations](#list_config-action-PutRemediationConfigurations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   PutRemediationExceptions  **
  - **IAM action:**  [config:PutRemediationExceptions](#list_config-action-PutRemediationExceptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourceConfig  **
  - **IAM action:**  [config:PutResourceConfig](#list_config-action-PutResourceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRetentionConfiguration  **
  - **IAM action:**  [config:PutRetentionConfiguration](#list_config-action-PutRetentionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutServiceLinkedConfigurationRecorder  **
  - **IAM action:**  [config:PutServiceLinkedConfigurationRecorder](#list_config-action-PutServiceLinkedConfigurationRecorder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutStoredQuery  **
  - **IAM action:**  [config:PutStoredQuery](#list_config-action-PutStoredQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutThirdPartyServiceLinkedConfigurationRecorder  **
  - **IAM action:**  [config:GetConnector](#list_config-action-GetConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [config:PutThirdPartyServiceLinkedConfigurationRecorder](#list_config-action-PutThirdPartyServiceLinkedConfigurationRecorder)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SelectAggregateResourceConfig  **
  - **IAM action:**  [config:SelectAggregateResourceConfig](#list_config-action-SelectAggregateResourceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SelectResourceConfig  **
  - **IAM action:**  [config:SelectResourceConfig](#list_config-action-SelectResourceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartConfigRulesEvaluation  **
  - **IAM action:**  [config:StartConfigRulesEvaluation](#list_config-action-StartConfigRulesEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartConfigurationRecorder  **
  - **IAM action:**  [config:StartConfigurationRecorder](#list_config-action-StartConfigurationRecorder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRemediationExecution  **
  - **IAM action:**  [config:StartRemediationExecution](#list_config-action-StartRemediationExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartResourceEvaluation  **
  - **IAM action:**  [config:StartResourceEvaluation](#list_config-action-StartResourceEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopConfigurationRecorder  **
  - **IAM action:**  [config:StopConfigurationRecorder](#list_config-action-StopConfigurationRecorder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [config:TagResource](#list_config-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [config:UntagResource](#list_config-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Config
<a name="list_config-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html)  **
  - **Description:** Grants permission to add all specified resource types to the RecordingGroup of configuration recorder and includes those resource types when recording
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_BatchGetAggregateResourceConfig.html)  **
  - **Description:** Grants permission to return the current configuration items for resources that are present in your AWS Config aggregator
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_BatchGetResourceConfig.html)  **
  - **Description:** Grants permission to return the current configuration for one or more requested resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DeleteAggregationAuthorization](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteAggregationAuthorization.html)  **
  - **Description:** Grants permission to delete the authorization granted to the specified configuration aggregator account in a specified region
  - **Resource types (\*required):** [AggregationAuthorization\*](#list_config-resource-AggregationAuthorization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigRule.html)  **
  - **Description:** Grants permission to delete the specified AWS Config rule and all of its evaluation results
  - **Resource types (\*required):** [ConfigRule\*](#list_config-resource-ConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfigurationAggregator](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationAggregator.html)  **
  - **Description:** Grants permission to delete the specified configuration aggregator and the aggregated data associated with the aggregator
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationRecorder.html)  **
  - **Description:** Grants permission to delete the customer managed configuration recorder
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConformancePack.html)  **
  - **Description:** Grants permission to delete the specified conformance pack and all the AWS Config rules and all evaluation results within that conformance pack
  - **Resource types (\*required):** [ConformancePack\*](#list_config-resource-ConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete a connector configuration
  - **Resource types (\*required):** [Connector\*](#list_config-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeliveryChannel](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html)  **
  - **Description:** Grants permission to delete the delivery channel
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEvaluationResults](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteEvaluationResults.html)  **
  - **Description:** Grants permission to delete the evaluation results for the specified Config rule
  - **Resource types (\*required):** [ConfigRule\*](#list_config-resource-ConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConfigRule.html)  **
  - **Description:** Grants permission to delete the specified organization config rule and all of its evaluation results from all member accounts in that organization
  - **Resource types (\*required):** [OrganizationConfigRule\*](#list_config-resource-OrganizationConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConformancePack.html)  **
  - **Description:** Grants permission to delete the specified organization conformance pack and all of its evaluation results from all member accounts in that organization
  - **Resource types (\*required):** [OrganizationConformancePack\*](#list_config-resource-OrganizationConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePendingAggregationRequest](https://docs.aws.amazon.com/config/latest/APIReference/API_DeletePendingAggregationRequest.html)  **
  - **Description:** Grants permission to delete pending authorization requests for a specified aggregator account in a specified region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRemediationConfiguration](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRemediationConfiguration.html)  **
  - **Description:** Grants permission to delete the remediation configuration
  - **Resource types (\*required):** [RemediationConfiguration\*](#list_config-resource-RemediationConfiguration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRemediationExceptions](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRemediationExceptions.html)  **
  - **Description:** Grants permission to delete one or more remediation exceptions for specific resource keys for a specific AWS Config Rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteResourceConfig.html)  **
  - **Description:** Grants permission to record the configuration state for a custom resource that has been deleted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRetentionConfiguration](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRetentionConfiguration.html)  **
  - **Description:** Grants permission to delete the retention configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html)  **
  - **Description:** Grants permission to delete the service-linked configuration recorder
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[config:ConfigurationRecorderServicePrincipal](#list_config-config_ConfigurationRecorderServicePrincipal)
  - **Access level:** Write

- **   [DeleteStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteStoredQuery.html)  **
  - **Description:** Grants permission to delete the stored query for an AWS account in an AWS Region
  - **Resource types (\*required):** [StoredQuery\*](#list_config-resource-StoredQuery)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeliverConfigSnapshot](https://docs.aws.amazon.com/config/latest/APIReference/API_DeliverConfigSnapshot.html)  **
  - **Description:** Grants permission to schedule delivery of a configuration snapshot to the Amazon S3 bucket in the specified delivery channel
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAggregateComplianceByConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeAggregateComplianceByConfigRules.html)  **
  - **Description:** Grants permission to return a list of compliant and noncompliant rules with the number of resources for compliant and noncompliant rules
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAggregateComplianceByConformancePacks](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeAggregateComplianceByConformancePacks.html)  **
  - **Description:** Grants permission to return a list of compliant and noncompliant conformance packs along with count of compliant, non-compliant and total rules within each conformance pack
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAggregationAuthorizations](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeAggregationAuthorizations.html)  **
  - **Description:** Grants permission to return a list of authorizations granted to various aggregator accounts and regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeComplianceByConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeComplianceByConfigRule.html)  **
  - **Description:** Grants permission to indicate whether the specified AWS Config rules are compliant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeComplianceByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeComplianceByResource.html)  **
  - **Description:** Grants permission to indicate whether the specified AWS resources are compliant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConfigRuleEvaluationStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRuleEvaluationStatus.html)  **
  - **Description:** Grants permission to return status information for each of your AWS managed Config rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRules.html)  **
  - **Description:** Grants permission to return details about your AWS Config rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeConfigurationAggregatorSourcesStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationAggregatorSourcesStatus.html)  **
  - **Description:** Grants permission to return status information for sources within an aggregator
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConfigurationAggregators](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationAggregators.html)  **
  - **Description:** Grants permission to return the details of one or more configuration aggregators
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html)  **
  - **Description:** Grants permission to return the current status of the specified configuration recorder
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[config:ConfigurationRecorderServicePrincipal](#list_config-config_ConfigurationRecorderServicePrincipal)
  - **Access level:** Read

- **   [DescribeConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html)  **
  - **Description:** Grants permission to return the names of one or more specified configuration recorders
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[config:ConfigurationRecorderServicePrincipal](#list_config-config_ConfigurationRecorderServicePrincipal)
  - **Access level:** Read

- **   [DescribeConformancePackCompliance](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConformancePackCompliance.html)  **
  - **Description:** Grants permission to return compliance information for each rule in that conformance pack
  - **Resource types (\*required):** [ConformancePack\*](#list_config-resource-ConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConformancePackStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConformancePackStatus.html)  **
  - **Description:** Grants permission to provide one or more conformance packs deployment status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConformancePacks](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConformancePacks.html)  **
  - **Description:** Grants permission to return a list of one or more conformance packs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDeliveryChannelStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeDeliveryChannelStatus.html)  **
  - **Description:** Grants permission to return the current status of the specified delivery channel
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDeliveryChannels](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeDeliveryChannels.html)  **
  - **Description:** Grants permission to return details about the specified delivery channel
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeOrganizationConfigRuleStatuses](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRuleStatuses.html)  **
  - **Description:** Grants permission to provide organization config rule deployment status for an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRules.html)  **
  - **Description:** Grants permission to return a list of organization config rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeOrganizationConformancePackStatuses](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePackStatuses.html)  **
  - **Description:** Grants permission to provide organization conformance pack deployment status for an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationConformancePacks](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePacks.html)  **
  - **Description:** Grants permission to return a list of organization conformance packs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePendingAggregationRequests](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribePendingAggregationRequests.html)  **
  - **Description:** Grants permission to return a list of all pending aggregation requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationConfigurations.html)  **
  - **Description:** Grants permission to return the details of one or more remediation configurations
  - **Resource types (\*required):** [RemediationConfiguration\*](#list_config-resource-RemediationConfiguration)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRemediationExceptions](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationExceptions.html)  **
  - **Description:** Grants permission to return the details of one or more remediation exceptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRemediationExecutionStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationExecutionStatus.html)  **
  - **Description:** Grants permission to provide a detailed view of a Remediation Execution for a set of resources including state, timestamps and any error messages for steps that have failed
  - **Resource types (\*required):** [RemediationConfiguration\*](#list_config-resource-RemediationConfiguration)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRetentionConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRetentionConfigurations.html)  **
  - **Description:** Grants permission to return the details of one or more retention configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html)  **
  - **Description:** Grants permission to remove all specified resource types from the RecordingGroup of configuration recorder and excludes these resource types when recording
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAggregateComplianceDetailsByConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateComplianceDetailsByConfigRule.html)  **
  - **Description:** Grants permission to return the evaluation results for the specified AWS Config rule for a specific resource in a rule
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAggregateConfigRuleComplianceSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateConfigRuleComplianceSummary.html)  **
  - **Description:** Grants permission to return the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAggregateConformancePackComplianceSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateConformancePackComplianceSummary.html)  **
  - **Description:** Grants permission to return the number of compliant and noncompliant conformance packs for one or more accounts and regions in an aggregator
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAggregateDiscoveredResourceCounts](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateDiscoveredResourceCounts.html)  **
  - **Description:** Grants permission to return the resource counts across accounts and regions that are present in your AWS Config aggregator
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateResourceConfig.html)  **
  - **Description:** Grants permission to return configuration item that is aggregated for your specific resource in a specific source account and region
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComplianceDetailsByConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByConfigRule.html)  **
  - **Description:** Grants permission to return the evaluation results for the specified AWS Config rule
  - **Resource types (\*required):** [ConfigRule\*](#list_config-resource-ConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComplianceDetailsByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html)  **
  - **Description:** Grants permission to return the evaluation results for the specified AWS resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetComplianceSummaryByConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceSummaryByConfigRule.html)  **
  - **Description:** Grants permission to return the number of AWS Config rules that are compliant and noncompliant, up to a maximum of 25 for each
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetComplianceSummaryByResourceType](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceSummaryByResourceType.html)  **
  - **Description:** Grants permission to return the number of resources that are compliant and the number that are noncompliant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConformancePackComplianceDetails](https://docs.aws.amazon.com/config/latest/APIReference/API_GetConformancePackComplianceDetails.html)  **
  - **Description:** Grants permission to return compliance details of a conformance pack for all AWS resources that are monitered by conformance pack
  - **Resource types (\*required):** [ConformancePack\*](#list_config-resource-ConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConformancePackComplianceSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetConformancePackComplianceSummary.html)  **
  - **Description:** Grants permission to provide compliance summary for one or more conformance packs
  - **Resource types (\*required):** [ConformancePack\*](#list_config-resource-ConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_GetConnector.html)  **
  - **Description:** Grants permission to return the details of a specific connector configuration
  - **Resource types (\*required):** [Connector\*](#list_config-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomRulePolicy](https://docs.aws.amazon.com/config/latest/APIReference/API_GetCustomRulePolicy.html)  **
  - **Description:** Grants permission to return the policy definition containing the logic for your AWS Config Custom Policy rule
  - **Resource types (\*required):** [ConfigRule\*](#list_config-resource-ConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDiscoveredResourceCounts](https://docs.aws.amazon.com/config/latest/APIReference/API_GetDiscoveredResourceCounts.html)  **
  - **Description:** Grants permission to return the resource types, the number of each resource type, and the total number of resources that AWS Config is recording in this region for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOrganizationConfigRuleDetailedStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConfigRuleDetailedStatus.html)  **
  - **Description:** Grants permission to return detailed status for each member account within an organization for a given organization config rule
  - **Resource types (\*required):** [OrganizationConfigRule\*](#list_config-resource-OrganizationConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOrganizationConformancePackDetailedStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConformancePackDetailedStatus.html)  **
  - **Description:** Grants permission to return detailed status for each member account within an organization for a given organization conformance pack
  - **Resource types (\*required):** [OrganizationConformancePack\*](#list_config-resource-OrganizationConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOrganizationCustomRulePolicy](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationCustomRulePolicy.html)  **
  - **Description:** Grants permission to return the policy definition containing the logic for your organization AWS Config Custom Policy rule
  - **Resource types (\*required):** [OrganizationConfigRule\*](#list_config-resource-OrganizationConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceConfigHistory](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceConfigHistory.html)  **
  - **Description:** Grants permission to return a list of configuration items for the specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceEvaluationSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html)  **
  - **Description:** Grants permission to return the summary of resource evaluations for a specific resource evaluation ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_GetStoredQuery.html)  **
  - **Description:** Grants permission to return the details of a specific stored query
  - **Resource types (\*required):** [StoredQuery\*](#list_config-resource-StoredQuery)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAggregateDiscoveredResources](https://docs.aws.amazon.com/config/latest/APIReference/API_ListAggregateDiscoveredResources.html)  **
  - **Description:** Grants permission to accept a resource type and returns a list of resource identifiers that are aggregated for a specific resource type across accounts and regions
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_ListConfigurationRecorders.html)  **
  - **Description:** Grants permission to list the configuration recorder summaries for an AWS account in an AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConformancePackComplianceScores](https://docs.aws.amazon.com/config/latest/APIReference/API_ListConformancePackComplianceScores.html)  **
  - **Description:** Grants permission to return the percentage of compliant rule-resource combinations in a conformance pack compared to the number of total possible rule-resource combinations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectors](https://docs.aws.amazon.com/config/latest/APIReference/API_ListConnectors.html)  **
  - **Description:** Grants permission to list all connectors in the AWS account and region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDiscoveredResources](https://docs.aws.amazon.com/config/latest/APIReference/API_ListDiscoveredResources.html)  **
  - **Description:** Grants permission to accept a resource type and returns a list of resource identifiers for the resources of that type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceEvaluations](https://docs.aws.amazon.com/config/latest/APIReference/API_ListResourceEvaluations.html)  **
  - **Description:** Grants permission to list the resource evaluation summaries for an AWS account in an AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStoredQueries](https://docs.aws.amazon.com/config/latest/APIReference/API_ListStoredQueries.html)  **
  - **Description:** Grants permission to list the stored queries for an AWS account in an AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/config/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for AWS Config resource
  - **Resource types (\*required):** [AggregationAuthorization](#list_config-resource-AggregationAuthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ConfigRule](#list_config-resource-ConfigRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ConfigurationAggregator](#list_config-resource-ConfigurationAggregator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ConfigurationRecorder](#list_config-resource-ConfigurationRecorder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ConformancePack](#list_config-resource-ConformancePack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Connector](#list_config-resource-Connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OrganizationConfigRule](#list_config-resource-OrganizationConfigRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OrganizationConformancePack](#list_config-resource-OrganizationConformancePack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StoredQuery](#list_config-resource-StoredQuery) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutAggregationAuthorization](https://docs.aws.amazon.com/config/latest/APIReference/API_PutAggregationAuthorization.html)  **
  - **Description:** Grants permission to authorize the aggregator account and region to collect data from the source account and region
  - **Resource types (\*required):** [AggregationAuthorization\*](#list_config-resource-AggregationAuthorization)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Write

- **   [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html)  **
  - **Description:** Grants permission to add or update an AWS Config rule for evaluating whether your AWS resources comply with your desired configurations
  - **Resource types (\*required):** [ConfigRule\*](#list_config-resource-ConfigRule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Write

- **   [PutConfigurationAggregator](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationAggregator.html)  **
  - **Description:** Grants permission to create and update the configuration aggregator with the selected source accounts and regions
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Write

- **   [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html)  **
  - **Description:** Grants permission to create or update a customer managed configuration recorder to record the selected resource configurations
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Write

- **   [PutConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html)  **
  - **Description:** Grants permission to create or update a conformance pack
  - **Resource types (\*required):** [ConformancePack\*](#list_config-resource-ConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html)  **
  - **Description:** Grants permission to create a connector configuration that contains provider identity information, as well as other optional provider-specific information required for third-party recording
  - **Resource types (\*required):** [Connector\*](#list_config-resource-Connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Write

- **   [PutDeliveryChannel](https://docs.aws.amazon.com/config/latest/APIReference/API_PutDeliveryChannel.html)  **
  - **Description:** Grants permission to create a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutEvaluations](https://docs.aws.amazon.com/config/latest/APIReference/API_PutEvaluations.html)  **
  - **Description:** Grants permission to be used by an AWS Lambda function to deliver evaluation results to AWS Config
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutExternalEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_PutExternalEvaluation.html)  **
  - **Description:** Grants permission to deliver evaluation result to AWS Config
  - **Resource types (\*required):** [ConfigRule\*](#list_config-resource-ConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html)  **
  - **Description:** Grants permission to add or update organization config rule for your entire organization evaluating whether your AWS resources comply with your desired configurations
  - **Resource types (\*required):** [OrganizationConfigRule\*](#list_config-resource-OrganizationConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html)  **
  - **Description:** Grants permission to add or update organization conformance pack for your entire organization evaluating whether your AWS resources comply with your desired configurations
  - **Resource types (\*required):** [OrganizationConformancePack\*](#list_config-resource-OrganizationConformancePack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationConfigurations.html)  **
  - **Description:** Grants permission to add or update the remediation configuration with a specific AWS Config rule with the selected target or action
  - **Resource types (\*required):** [RemediationConfiguration\*](#list_config-resource-RemediationConfiguration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutRemediationExceptions](https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationExceptions.html)  **
  - **Description:** Grants permission to add or update remediation exceptions for specific resources for a specific AWS Config rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_PutResourceConfig.html)  **
  - **Description:** Grants permission to record the configuration state for the resource provided in the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutRetentionConfiguration](https://docs.aws.amazon.com/config/latest/APIReference/API_PutRetentionConfiguration.html)  **
  - **Description:** Grants permission to create and update the retention configuration with details about retention period (number of days) that AWS Config stores your historical information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html)  **
  - **Description:** Grants permission to create a new service-linked configuration recorder to record the resource configurations in scope for the linked service
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)<br />[config:ConfigurationRecorderServicePrincipal](#list_config-config_ConfigurationRecorderServicePrincipal)
  - **Access level:** Write

- **   [PutStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html)  **
  - **Description:** Grants permission to save a new query or updates an existing saved query
  - **Resource types (\*required):** [StoredQuery\*](#list_config-resource-StoredQuery)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Write

- **   [PutThirdPartyServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html)  **
  - **Description:** Grants permission to create or update a service-linked configuration recorder for a third-party provider linked to a specific AWS partner service
  - **Resource types (\*required):** [Connector\*](#list_config-resource-Connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)<br />[config:ConfigurationRecorderServicePrincipal](#list_config-config_ConfigurationRecorderServicePrincipal)
  - **Access level:** Write

- **   [SelectAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectAggregateResourceConfig.html)  **
  - **Description:** Grants permission to accept a structured query language (SQL) SELECT command and an aggregator to query configuration state of AWS resources across multiple accounts and regions, performs the corresponding search, and returns resource configurations matching the properties
  - **Resource types (\*required):** [ConfigurationAggregator\*](#list_config-resource-ConfigurationAggregator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SelectResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectResourceConfig.html)  **
  - **Description:** Grants permission to accept a structured query language (SQL) SELECT command, performs the corresponding search, and returns resource configurations matching the properties
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartConfigRulesEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigRulesEvaluation.html)  **
  - **Description:** Grants permission to evaluate your resources against the specified Config rules
  - **Resource types (\*required):** [ConfigRule\*](#list_config-resource-ConfigRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html)  **
  - **Description:** Grants permission to the customer managed configuration recorder to start recording configurations of the AWS resources you have selected to record in your AWS account
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRemediationExecution](https://docs.aws.amazon.com/config/latest/APIReference/API_StartRemediationExecution.html)  **
  - **Description:** Grants permission to run an on-demand remediation for the specified AWS Config rules against the last known remediation configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html)  **
  - **Description:** Grants permission to evaluate your resource details against the AWS Config rules in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html)  **
  - **Description:** Grants permission to the customer managed configuration recorder to stop recording configurations of the AWS resources you have selected to record in your AWS account
  - **Resource types (\*required):** [ConfigurationRecorder\*](#list_config-resource-ConfigurationRecorder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to associate the specified tags to a resource with the specified resourceArn
  - **Resource types (\*required):** [AggregationAuthorization](#list_config-resource-AggregationAuthorization) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConfigRule](#list_config-resource-ConfigRule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConfigurationAggregator](#list_config-resource-ConfigurationAggregator) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConfigurationRecorder](#list_config-resource-ConfigurationRecorder) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConformancePack](#list_config-resource-ConformancePack) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [Connector](#list_config-resource-Connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [OrganizationConfigRule](#list_config-resource-OrganizationConfigRule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [OrganizationConformancePack](#list_config-resource-OrganizationConformancePack) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [StoredQuery](#list_config-resource-StoredQuery) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to delete specified tags from a resource
  - **Resource types (\*required):** [AggregationAuthorization](#list_config-resource-AggregationAuthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConfigRule](#list_config-resource-ConfigRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConfigurationAggregator](#list_config-resource-ConfigurationAggregator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConfigurationRecorder](#list_config-resource-ConfigurationRecorder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [ConformancePack](#list_config-resource-ConformancePack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [Connector](#list_config-resource-Connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [OrganizationConfigRule](#list_config-resource-OrganizationConfigRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [OrganizationConformancePack](#list_config-resource-OrganizationConformancePack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Resource types (\*required):** [StoredQuery](#list_config-resource-StoredQuery) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_config-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Config
<a name="list_config-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AggregationAuthorization](https://docs.aws.amazon.com/config/latest/APIReference/API_AggregationAuthorization.html)  | arn:${Partition}:config:${Region}:${Account}:aggregation-authorization/${AggregatorAccount}/${AggregatorRegion} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [ConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html)  | arn:${Partition}:config:${Region}:${Account}:config-rule/${ConfigRuleId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [ConfigurationAggregator](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationAggregator.html)  | arn:${Partition}:config:${Region}:${Account}:config-aggregator/${AggregatorId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [ConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationRecorder.html)  | arn:${Partition}:config:${Region}:${Account}:configuration-recorder/${RecorderName}/${RecorderId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [ConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackDetail.html)  | arn:${Partition}:config:${Region}:${Account}:conformance-pack/${ConformancePackName}/${ConformancePackId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [Connector](https://docs.aws.amazon.com/config/latest/APIReference/API_Connector.html)  | arn:${Partition}:config:${Region}:${Account}:connector/${Provider}/${ProviderId}/${ConnectorId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [OrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConfigRule.html)  | arn:${Partition}:config:${Region}:${Account}:organization-config-rule/${OrganizationConfigRuleId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [OrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConformancePack.html)  | arn:${Partition}:config:${Region}:${Account}:organization-conformance-pack/${OrganizationConformancePackId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 
|  [RemediationConfiguration](https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationConfiguration.html)  | arn:${Partition}:config:${Region}:${Account}:remediation-configuration/${RemediationConfigurationId} |   | 
|  [StoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_StoredQuery.html)  | arn:${Partition}:config:${Region}:${Account}:stored-query/${StoredQueryName}/${StoredQueryId} | [aws:ResourceTag/${TagKey}](#list_config-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Config
<a name="list_config-policy-keys"></a>

AWS Config defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 
|   [config:ConfigurationRecorderServicePrincipal](https://docs.aws.amazon.com/config/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by service principal of the configuration recorder | String | 