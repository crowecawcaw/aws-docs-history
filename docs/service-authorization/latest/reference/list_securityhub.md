

# Actions, resources, and condition keys for AWS Security Hub
<a name="list_securityhub"></a>

AWS Security Hub (service prefix: `securityhub`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/securityhub/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/securityhub/1.0/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/securityhub/securityhub.json) for this service.

**Topics**
+ [API operations defined by AWS Security Hub](#list_securityhub-operations)
+ [Actions defined by AWS Security Hub](#list_securityhub-actions-as-permissions)
+ [Permission-only actions for AWS Security Hub](#list_securityhub-permission-only-actions)
+ [Resource types defined by AWS Security Hub](#list_securityhub-resources-for-iam-policies)
+ [Condition keys for AWS Security Hub](#list_securityhub-policy-keys)

## API operations defined by AWS Security Hub
<a name="list_securityhub-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_securityhub-actions-as-permissions).




- **   AcceptAdministratorInvitation  **
  - **IAM action:**  [securityhub:AcceptAdministratorInvitation](#list_securityhub-action-AcceptAdministratorInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcceptInvitation  **
  - **IAM action:**  [securityhub:AcceptInvitation](#list_securityhub-action-AcceptInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteAutomationRules  **
  - **IAM action:**  [securityhub:BatchDeleteAutomationRules](#list_securityhub-action-BatchDeleteAutomationRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisableStandards  **
  - **IAM action:**  [securityhub:BatchDisableStandards](#list_securityhub-action-BatchDisableStandards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchEnableStandards  **
  - **IAM action:**  [securityhub:BatchEnableStandards](#list_securityhub-action-BatchEnableStandards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetAutomationRules  **
  - **IAM action:**  [securityhub:BatchGetAutomationRules](#list_securityhub-action-BatchGetAutomationRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetConfigurationPolicyAssociations  **
  - **IAM action:**  [securityhub:BatchGetConfigurationPolicyAssociations](#list_securityhub-action-BatchGetConfigurationPolicyAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetSecurityControls  **
  - **IAM action:**  [securityhub:BatchGetSecurityControls](#list_securityhub-action-BatchGetSecurityControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [securityhub:DescribeStandardsControls](#list_securityhub-action-DescribeStandardsControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchGetStandardsControlAssociations  **
  - **IAM action:**  [securityhub:BatchGetStandardsControlAssociations](#list_securityhub-action-BatchGetStandardsControlAssociations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [securityhub:DescribeStandardsControls](#list_securityhub-action-DescribeStandardsControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchImportFindings  **
  - **IAM action:**  [securityhub:BatchImportFindings](#list_securityhub-action-BatchImportFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateAutomationRules  **
  - **IAM action:**  [securityhub:BatchUpdateAutomationRules](#list_securityhub-action-BatchUpdateAutomationRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateFindings  **
  - **IAM action:**  [securityhub:BatchUpdateFindings](#list_securityhub-action-BatchUpdateFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateFindingsV2  **
  - **IAM action:**  [securityhub:BatchUpdateFindings](#list_securityhub-action-BatchUpdateFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateStandardsControlAssociations  **
  - **IAM action:**  [securityhub:BatchUpdateStandardsControlAssociations](#list_securityhub-action-BatchUpdateStandardsControlAssociations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:UpdateStandardsControl](#list_securityhub-action-UpdateStandardsControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateActionTarget  **
  - **IAM action:**  [securityhub:CreateActionTarget](#list_securityhub-action-CreateActionTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAggregatorV2  **
  - **IAM action:**  [securityhub:CreateAggregatorV2](#list_securityhub-action-CreateAggregatorV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAutomationRule  **
  - **IAM action:**  [securityhub:CreateAutomationRule](#list_securityhub-action-CreateAutomationRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAutomationRuleV2  **
  - **IAM action:**  [securityhub:CreateAutomationRuleV2](#list_securityhub-action-CreateAutomationRuleV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfigurationPolicy  **
  - **IAM action:**  [securityhub:CreateConfigurationPolicy](#list_securityhub-action-CreateConfigurationPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnector  **
  - **IAM action:**  [securityhub:CreateConnector](#list_securityhub-action-CreateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnectorV2  **
  - **IAM action:**  [securityhub:CreateConnectorV2](#list_securityhub-action-CreateConnectorV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFindingAggregator  **
  - **IAM action:**  [securityhub:CreateFindingAggregator](#list_securityhub-action-CreateFindingAggregator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInsight  **
  - **IAM action:**  [securityhub:CreateInsight](#list_securityhub-action-CreateInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMembers  **
  - **IAM action:**  [securityhub:CreateMembers](#list_securityhub-action-CreateMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTicketV2  **
  - **IAM action:**  [securityhub:CreateTicketV2](#list_securityhub-action-CreateTicketV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeclineInvitations  **
  - **IAM action:**  [securityhub:DeclineInvitations](#list_securityhub-action-DeclineInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteActionTarget  **
  - **IAM action:**  [securityhub:DeleteActionTarget](#list_securityhub-action-DeleteActionTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAggregatorV2  **
  - **IAM action:**  [securityhub:DeleteAggregatorV2](#list_securityhub-action-DeleteAggregatorV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAutomationRuleV2  **
  - **IAM action:**  [securityhub:DeleteAutomationRuleV2](#list_securityhub-action-DeleteAutomationRuleV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationPolicy  **
  - **IAM action:**  [securityhub:DeleteConfigurationPolicy](#list_securityhub-action-DeleteConfigurationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnector  **
  - **IAM action:**  [securityhub:DeleteConnector](#list_securityhub-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectorV2  **
  - **IAM action:**  [securityhub:DeleteConnectorV2](#list_securityhub-action-DeleteConnectorV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFindingAggregator  **
  - **IAM action:**  [securityhub:DeleteFindingAggregator](#list_securityhub-action-DeleteFindingAggregator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInsight  **
  - **IAM action:**  [securityhub:DeleteInsight](#list_securityhub-action-DeleteInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInvitations  **
  - **IAM action:**  [securityhub:DeleteInvitations](#list_securityhub-action-DeleteInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMembers  **
  - **IAM action:**  [securityhub:DeleteMembers](#list_securityhub-action-DeleteMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeActionTargets  **
  - **IAM action:**  [securityhub:DescribeActionTargets](#list_securityhub-action-DescribeActionTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHub  **
  - **IAM action:**  [securityhub:DescribeHub](#list_securityhub-action-DescribeHub) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationConfiguration  **
  - **IAM action:**  [securityhub:DescribeOrganizationConfiguration](#list_securityhub-action-DescribeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProducts  **
  - **IAM action:**  [securityhub:DescribeProducts](#list_securityhub-action-DescribeProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProductsV2  **
  - **IAM action:**  [securityhub:DescribeProductsV2](#list_securityhub-action-DescribeProductsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSecurityHubV2  **
  - **IAM action:**  [securityhub:DescribeSecurityHubV2](#list_securityhub-action-DescribeSecurityHubV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStandards  **
  - **IAM action:**  [securityhub:DescribeStandards](#list_securityhub-action-DescribeStandards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStandardsControls  **
  - **IAM action:**  [securityhub:DescribeStandardsControls](#list_securityhub-action-DescribeStandardsControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableImportFindingsForProduct  **
  - **IAM action:**  [securityhub:DisableImportFindingsForProduct](#list_securityhub-action-DisableImportFindingsForProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableOrganizationAdminAccount  **
  - **IAM action:**  [securityhub:DisableOrganizationAdminAccount](#list_securityhub-action-DisableOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableSecurityHub  **
  - **IAM action:**  [securityhub:DisableSecurityHub](#list_securityhub-action-DisableSecurityHub) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableSecurityHubFeatureV2  **
  - **IAM action:**  [securityhub:DisableSecurityHubFeatureV2](#list_securityhub-action-DisableSecurityHubFeatureV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableSecurityHubV2  **
  - **IAM action:**  [securityhub:DisableSecurityHubV2](#list_securityhub-action-DisableSecurityHubV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFromAdministratorAccount  **
  - **IAM action:**  [securityhub:DisassociateFromAdministratorAccount](#list_securityhub-action-DisassociateFromAdministratorAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFromMasterAccount  **
  - **IAM action:**  [securityhub:DisassociateFromMasterAccount](#list_securityhub-action-DisassociateFromMasterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMembers  **
  - **IAM action:**  [securityhub:DisassociateMembers](#list_securityhub-action-DisassociateMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableImportFindingsForProduct  **
  - **IAM action:**  [securityhub:EnableImportFindingsForProduct](#list_securityhub-action-EnableImportFindingsForProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableOrganizationAdminAccount  **
  - **IAM action:**  [securityhub:EnableOrganizationAdminAccount](#list_securityhub-action-EnableOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableSecurityHub  **
  - **IAM action:**  [securityhub:EnableSecurityHub](#list_securityhub-action-EnableSecurityHub)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   EnableSecurityHubFeatureV2  **
  - **IAM action:**  [securityhub:EnableSecurityHubFeatureV2](#list_securityhub-action-EnableSecurityHubFeatureV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableSecurityHubV2  **
  - **IAM action:**  [securityhub:EnableSecurityHubV2](#list_securityhub-action-EnableSecurityHubV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   GenerateRecommendedPolicyV2  **
  - **IAM action:**  [securityhub:GenerateRecommendedPolicyV2](#list_securityhub-action-GenerateRecommendedPolicyV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAdministratorAccount  **
  - **IAM action:**  [securityhub:GetAdministratorAccount](#list_securityhub-action-GetAdministratorAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAggregatorV2  **
  - **IAM action:**  [securityhub:GetAggregatorV2](#list_securityhub-action-GetAggregatorV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomationRuleV2  **
  - **IAM action:**  [securityhub:GetAutomationRuleV2](#list_securityhub-action-GetAutomationRuleV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationPolicy  **
  - **IAM action:**  [securityhub:GetConfigurationPolicy](#list_securityhub-action-GetConfigurationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationPolicyAssociation  **
  - **IAM action:**  [securityhub:GetConfigurationPolicyAssociation](#list_securityhub-action-GetConfigurationPolicyAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnector  **
  - **IAM action:**  [securityhub:GetConnector](#list_securityhub-action-GetConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectorV2  **
  - **IAM action:**  [securityhub:GetConnectorV2](#list_securityhub-action-GetConnectorV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnabledStandards  **
  - **IAM action:**  [securityhub:GetEnabledStandards](#list_securityhub-action-GetEnabledStandards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetFindingAggregator  **
  - **IAM action:**  [securityhub:GetFindingAggregator](#list_securityhub-action-GetFindingAggregator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingHistory  **
  - **IAM action:**  [securityhub:GetFindingHistory](#list_securityhub-action-GetFindingHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingStatisticsV2  **
  - **IAM action:**  [securityhub:GetAdhocInsightResults](#list_securityhub-action-GetAdhocInsightResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindings  **
  - **IAM action:**  [securityhub:GetFindings](#list_securityhub-action-GetFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsTrendsV2  **
  - **IAM action:**  [securityhub:GetFindingsTrendsV2](#list_securityhub-action-GetFindingsTrendsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsV2  **
  - **IAM action:**  [securityhub:GetFindings](#list_securityhub-action-GetFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightResults  **
  - **IAM action:**  [securityhub:GetInsightResults](#list_securityhub-action-GetInsightResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsights  **
  - **IAM action:**  [securityhub:GetInsights](#list_securityhub-action-GetInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetInvitationsCount  **
  - **IAM action:**  [securityhub:GetInvitationsCount](#list_securityhub-action-GetInvitationsCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMasterAccount  **
  - **IAM action:**  [securityhub:GetMasterAccount](#list_securityhub-action-GetMasterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMembers  **
  - **IAM action:**  [securityhub:GetMembers](#list_securityhub-action-GetMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendedPolicyV2  **
  - **IAM action:**  [securityhub:GetRecommendedPolicyV2](#list_securityhub-action-GetRecommendedPolicyV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcesStatisticsV2  **
  - **IAM action:**  [securityhub:GetResourcesStatisticsV2](#list_securityhub-action-GetResourcesStatisticsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcesTrendsV2  **
  - **IAM action:**  [securityhub:GetResourcesTrendsV2](#list_securityhub-action-GetResourcesTrendsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcesV2  **
  - **IAM action:**  [securityhub:GetResourcesV2](#list_securityhub-action-GetResourcesV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecurityControlDefinition  **
  - **IAM action:**  [securityhub:GetSecurityControlDefinition](#list_securityhub-action-GetSecurityControlDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InviteMembers  **
  - **IAM action:**  [securityhub:InviteMembers](#list_securityhub-action-InviteMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAggregatorsV2  **
  - **IAM action:**  [securityhub:ListAggregatorsV2](#list_securityhub-action-ListAggregatorsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomationRules  **
  - **IAM action:**  [securityhub:ListAutomationRules](#list_securityhub-action-ListAutomationRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomationRulesV2  **
  - **IAM action:**  [securityhub:ListAutomationRulesV2](#list_securityhub-action-ListAutomationRulesV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationPolicies  **
  - **IAM action:**  [securityhub:ListConfigurationPolicies](#list_securityhub-action-ListConfigurationPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationPolicyAssociations  **
  - **IAM action:**  [securityhub:ListConfigurationPolicyAssociations](#list_securityhub-action-ListConfigurationPolicyAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectors  **
  - **IAM action:**  [securityhub:ListConnectors](#list_securityhub-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectorsV2  **
  - **IAM action:**  [securityhub:ListConnectorsV2](#list_securityhub-action-ListConnectorsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnabledProductsForImport  **
  - **IAM action:**  [securityhub:ListEnabledProductsForImport](#list_securityhub-action-ListEnabledProductsForImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindingAggregators  **
  - **IAM action:**  [securityhub:ListFindingAggregators](#list_securityhub-action-ListFindingAggregators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFreeTrialStatusesV2  **
  - **IAM action:**  [securityhub:ListFreeTrialStatusesV2](#list_securityhub-action-ListFreeTrialStatusesV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvitations  **
  - **IAM action:**  [securityhub:ListInvitations](#list_securityhub-action-ListInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembers  **
  - **IAM action:**  [securityhub:ListMembers](#list_securityhub-action-ListMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationAdminAccounts  **
  - **IAM action:**  [securityhub:ListOrganizationAdminAccounts](#list_securityhub-action-ListOrganizationAdminAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityControlDefinitions  **
  - **IAM action:**  [securityhub:ListSecurityControlDefinitions](#list_securityhub-action-ListSecurityControlDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStandardsControlAssociations  **
  - **IAM action:**  [securityhub:DescribeStandardsControls](#list_securityhub-action-DescribeStandardsControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [securityhub:ListStandardsControlAssociations](#list_securityhub-action-ListStandardsControlAssociations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [securityhub:ListTagsForResource](#list_securityhub-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartConfigurationPolicyAssociation  **
  - **IAM action:**  [securityhub:StartConfigurationPolicyAssociation](#list_securityhub-action-StartConfigurationPolicyAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartConfigurationPolicyDisassociation  **
  - **IAM action:**  [securityhub:StartConfigurationPolicyDisassociation](#list_securityhub-action-StartConfigurationPolicyDisassociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [securityhub:TagResource](#list_securityhub-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [securityhub:UntagResource](#list_securityhub-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateActionTarget  **
  - **IAM action:**  [securityhub:UpdateActionTarget](#list_securityhub-action-UpdateActionTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAggregatorV2  **
  - **IAM action:**  [securityhub:UpdateAggregatorV2](#list_securityhub-action-UpdateAggregatorV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAutomationRuleV2  **
  - **IAM action:**  [securityhub:UpdateAutomationRuleV2](#list_securityhub-action-UpdateAutomationRuleV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationPolicy  **
  - **IAM action:**  [securityhub:UpdateConfigurationPolicy](#list_securityhub-action-UpdateConfigurationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnector  **
  - **IAM action:**  [securityhub:UpdateConnector](#list_securityhub-action-UpdateConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectorV2  **
  - **IAM action:**  [securityhub:UpdateConnectorV2](#list_securityhub-action-UpdateConnectorV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFindingAggregator  **
  - **IAM action:**  [securityhub:UpdateFindingAggregator](#list_securityhub-action-UpdateFindingAggregator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFindings  **
  - **IAM action:**  [securityhub:UpdateFindings](#list_securityhub-action-UpdateFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInsight  **
  - **IAM action:**  [securityhub:UpdateInsight](#list_securityhub-action-UpdateInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOrganizationConfiguration  **
  - **IAM action:**  [securityhub:UpdateOrganizationConfiguration](#list_securityhub-action-UpdateOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecurityControl  **
  - **IAM action:**  [securityhub:UpdateSecurityControl](#list_securityhub-action-UpdateSecurityControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityhub:UpdateStandardsControl](#list_securityhub-action-UpdateStandardsControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateSecurityHubConfiguration  **
  - **IAM action:**  [securityhub:UpdateSecurityHubConfiguration](#list_securityhub-action-UpdateSecurityHubConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStandardsControl  **
  - **IAM action:**  [securityhub:UpdateStandardsControl](#list_securityhub-action-UpdateStandardsControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Security Hub
<a name="list_securityhub-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptAdministratorInvitation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AcceptAdministratorInvitation.html)  **
  - **Description:** Grants permission to accept Security Hub invitations to become a member account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AcceptInvitation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AcceptInvitation.html)  **
  - **Description:** Grants permission to accept Security Hub invitations to become a member account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteAutomationRules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to delete one or more automation rules in Security Hub
  - **Resource types (\*required):** [automation-rule\*](#list_securityhub-resource-automation-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisableStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchDisableStandards.html)  **
  - **Description:** Grants permission to disable standards in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchEnableStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchEnableStandards.html)  **
  - **Description:** Grants permission to enable standards in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetAutomationRules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to retrieve a list of details for automation rules from Security Hub based on rule Amazon Resource Names (ARNs)
  - **Resource types (\*required):** [automation-rule\*](#list_securityhub-resource-automation-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetConfigurationPolicyAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetConfigurationPolicyAssociations.html)  **
  - **Description:** Grants permission to retrieve information about configuration policies associated with a specific list of member accounts and organizational units of the calling account's organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetSecurityControls](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetSecurityControls.html)  **
  - **Description:** Grants permission to get details about specific security controls identified by ID or ARN
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetStandardsControlAssociations.html)  **
  - **Description:** Grants permission to get the enablement status of a batch of security controls in standards
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchImportFindings](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html)  **
  - **Description:** Grants permission to import findings into Security Hub from an integrated product
  - **Resource types (\*required):** [product\*](#list_securityhub-resource-product)
  - **Condition keys:** [securityhub:TargetAccount](#list_securityhub-securityhub_TargetAccount)
  - **Access level:** Write

- **   [BatchUpdateAutomationRules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to update one or more automation rules from Security Hub based on rule Amazon Resource Names (ARNs) and input parameters
  - **Resource types (\*required):** [automation-rule\*](#list_securityhub-resource-automation-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchUpdateFindings](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindingsV2.html)  **
  - **Description:** Grants permission to update customer-controlled fields for a selected set of Security Hub findings
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)<br />[securityhub:ASFFSyntaxPath/${ASFFSyntaxPath}](#list_securityhub-securityhub_ASFFSyntaxPath___ASFFSyntaxPath_)<br />[securityhub:OCSFSyntaxPath/${OCSFSyntaxPath}](#list_securityhub-securityhub_OCSFSyntaxPath___OCSFSyntaxPath_)
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)<br />[securityhub:ASFFSyntaxPath/${ASFFSyntaxPath}](#list_securityhub-securityhub_ASFFSyntaxPath___ASFFSyntaxPath_)<br />[securityhub:OCSFSyntaxPath/${OCSFSyntaxPath}](#list_securityhub-securityhub_OCSFSyntaxPath___OCSFSyntaxPath_)
  - **Access level:** Write

- **   [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html)  **
  - **Description:** Grants permission to update the enablement status of a batch of security controls in standards
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ConnectorRegistrationsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ConnectorRegistrationsV2.html)  **
  - **Description:** Grants permission to complete the OAuth 2.0 authorization code flow based on input parameters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateActionTarget](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateActionTarget.html)  **
  - **Description:** Grants permission to create custom actions in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAggregatorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateAggregatorV2.html)  **
  - **Description:** Grants permission to create an aggregatorV2, which configures data aggregation across Regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAutomationRule](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to create an automation rule based on input parameters
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityhub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityhub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAutomationRuleV2](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to create an automation rule V2 based on input parameters
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityhub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityhub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfigurationPolicy](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateConfigurationPolicy.html)  **
  - **Description:** Grants permission to create a configuration policy to manage organization member settings in Security Hub
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityhub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityhub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnector](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateConnector.html)  **
  - **Description:** Grants permission to create a connector based on input parameters
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityhub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityhub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnectorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateConnectorV2.html)  **
  - **Description:** Grants permission to create a connector V2 based on input parameters
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityhub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityhub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFindingAggregator](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateFindingAggregator.html)  **
  - **Description:** Grants permission to create a finding aggregator, which contains the cross-Region finding aggregation configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateInsight](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateInsight.html)  **
  - **Description:** Grants permission to create insights in Security Hub. Insights are collections of related findings
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMembers](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateMembers.html)  **
  - **Description:** Grants permission to create member accounts in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTicketV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateTicketV2.html)  **
  - **Description:** Grants permission to create ticket for a selected OCSF finding
  - **Resource types (\*required):** [connectorv2](#list_securityhub-resource-connectorv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeclineInvitations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeclineInvitations.html)  **
  - **Description:** Grants permission to decline Security Hub invitations to become a member account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteActionTarget](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteActionTarget.html)  **
  - **Description:** Grants permission to delete custom actions in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAggregatorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteAggregatorV2.html)  **
  - **Description:** Grants permission to delete an aggregatorV2, which configures data aggregation across Regions
  - **Resource types (\*required):** [aggregatorv2\*](#list_securityhub-resource-aggregatorv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAutomationRuleV2](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to delete an automation rule V2 in Security Hub
  - **Resource types (\*required):** [automation-rulev2\*](#list_securityhub-resource-automation-rulev2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfigurationPolicy](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteConfigurationPolicy.html)  **
  - **Description:** Grants permission to delete an existing configuration policy
  - **Resource types (\*required):** [configuration-policy\*](#list_securityhub-resource-configuration-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete a connector in Security Hub CSPM
  - **Resource types (\*required):** [connector\*](#list_securityhub-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnectorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteConnectorV2.html)  **
  - **Description:** Grants permission to delete a connector V2 in Security Hub
  - **Resource types (\*required):** [connectorv2\*](#list_securityhub-resource-connectorv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFindingAggregator](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteFindingAggregator.html)  **
  - **Description:** Grants permission to delete a finding aggregator, which disables finding aggregation across Regions
  - **Resource types (\*required):** [finding-aggregator\*](#list_securityhub-resource-finding-aggregator)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInsight](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteInsight.html)  **
  - **Description:** Grants permission to delete insights from Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvitations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteInvitations.html)  **
  - **Description:** Grants permission to delete Security Hub invitations to become a member account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMembers](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteMembers.html)  **
  - **Description:** Grants permission to delete Security Hub member accounts
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeActionTargets](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeActionTargets.html)  **
  - **Description:** Grants permission to retrieve a list of custom actions using the API
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHub](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeHub.html)  **
  - **Description:** Grants permission to retrieve information about the hub resource in your account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeOrganizationConfiguration.html)  **
  - **Description:** Grants permission to describe the organization configuration for Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProducts](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeProducts.html)  **
  - **Description:** Grants permission to retrieve information about the available Security Hub product integrations
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProductsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeProductsV2.html)  **
  - **Description:** Grants permission to retrieve information about the available Security Hub V2 product integrations
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSecurityHubV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeSecurityHubV2.html)  **
  - **Description:** Grants permission to retrieve information about the hub V2 resource in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html)  **
  - **Description:** Grants permission to retrieve information about Security Hub standards
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStandardsControls](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandardsControls.html)  **
  - **Description:** Grants permission to retrieve information about Security Hub standards controls
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableImportFindingsForProduct](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableImportFindingsForProduct.html)  **
  - **Description:** Grants permission to disable the findings importing for a Security Hub integrated product
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableOrganizationAdminAccount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to remove the Security Hub administrator account for your organization
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableSecurityHub](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableSecurityHub.html)  **
  - **Description:** Grants permission to disable Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableSecurityHubFeatureV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableSecurityHubFeatureV2.html)  **
  - **Description:** Grants permission to disable a Security Hub V2 feature
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableSecurityHubV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableSecurityHubV2.html)  **
  - **Description:** Grants permission to disable Security Hub V2
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateFromAdministratorAccount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisassociateFromAdministratorAccount.html)  **
  - **Description:** Grants permission to a Security Hub member account to disassociate from the associated administrator account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateFromMasterAccount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisassociateFromMasterAccount.html)  **
  - **Description:** Grants permission to a Security Hub member account to disassociate from the associated master account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateMembers](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisassociateMembers.html)  **
  - **Description:** Grants permission to disassociate Security Hub member accounts from the associated administrator account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableImportFindingsForProduct](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableImportFindingsForProduct.html)  **
  - **Description:** Grants permission to enable the findings importing for a Security Hub integrated product
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableOrganizationAdminAccount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to designate a Security Hub administrator account for your organization
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableSecurityHub](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableSecurityHub.html)  **
  - **Description:** Grants permission to enable Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityhub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityhub-aws_TagKeys)
  - **Access level:** Write

- **   [EnableSecurityHubFeatureV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableSecurityHubFeatureV2.html)  **
  - **Description:** Grants permission to enable a Security Hub V2 feature
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableSecurityHubV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableSecurityHubV2.html)  **
  - **Description:** Grants permission to enable Security Hub V2
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityhub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityhub-aws_TagKeys)
  - **Access level:** Write

- **   [GenerateRecommendedPolicyV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GenerateRecommendedPolicyV2.html)  **
  - **Description:** Grants permission to generate policy recommendations for an OCSF finding
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAdministratorAccount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetAdministratorAccount.html)  **
  - **Description:** Grants permission to retrieve details about the Security Hub administrator account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAggregatorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetAggregatorV2.html)  **
  - **Description:** Grants permission to retrieve details for an aggregatorV2, which configures data aggregation across Regions
  - **Resource types (\*required):** [aggregatorv2\*](#list_securityhub-resource-aggregatorv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomationRuleV2](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to retrieve details for an automation rule V2 from Security Hub based on rule Amazon Resource Name (ARN)
  - **Resource types (\*required):** [automation-rulev2\*](#list_securityhub-resource-automation-rulev2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfigurationPolicy](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetConfigurationPolicy.html)  **
  - **Description:** Grants permission to get a complete overview of one configuration policy created by the calling account
  - **Resource types (\*required):** [configuration-policy\*](#list_securityhub-resource-configuration-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfigurationPolicyAssociation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetConfigurationPolicyAssociation.html)  **
  - **Description:** Grants permission to retrieve information about a configuration policy associated with a member account or organizational unit of the calling account's organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnector](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetConnector.html)  **
  - **Description:** Grants permission to retrieve details for a connector from Security Hub CSPM based on connector id
  - **Resource types (\*required):** [connector\*](#list_securityhub-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetConnectorV2.html)  **
  - **Description:** Grants permission to retrieve details for a connector V2 from Security Hub based on connector id
  - **Resource types (\*required):** [connectorv2\*](#list_securityhub-resource-connectorv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnabledStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetEnabledStandards.html)  **
  - **Description:** Grants permission to retrieve a list of the standards that are enabled in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetFindingAggregator](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingAggregator.html)  **
  - **Description:** Grants permission to retrieve details for a finding aggregator, which configures finding aggregation across Regions
  - **Resource types (\*required):** [finding-aggregator\*](#list_securityhub-resource-finding-aggregator)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFindingHistory](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingHistory.html)  **
  - **Description:** Grants permission to retrieve a list of finding history from Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindings](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html)  **
  - **Description:** Grants permission to retrieve a list of findings from Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindingsTrendsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsTrendsV2.html)  **
  - **Description:** Grants permission to retrieve findings trends
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInsightResults](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetInsightResults.html)  **
  - **Description:** Grants permission to retrieve insight results from Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInsights](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetInsights.html)  **
  - **Description:** Grants permission to retrieve Security Hub insights
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetInvitationsCount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetInvitationsCount.html)  **
  - **Description:** Grants permission to retrieve the count of Security Hub membership invitations sent to the account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMasterAccount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetMasterAccount.html)  **
  - **Description:** Grants permission to retrieve details about the Security Hub master account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMembers](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetMembers.html)  **
  - **Description:** Grants permission to retrieve the details of Security Hub member accounts
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommendedPolicyV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetRecommendedPolicyV2.html)  **
  - **Description:** Grants permission to retrieve policy recommendations for an OCSF finding
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcesStatisticsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetResourcesStatisticsV2.html)  **
  - **Description:** Grants permission to retrieve aggregate statistics about resources
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcesTrendsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetResourcesTrendsV2.html)  **
  - **Description:** Grants permission to retrieve resources trends
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcesV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetResourcesV2.html)  **
  - **Description:** Grants permission to retrieve a list of resources
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSecurityControlDefinition](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetSecurityControlDefinition.html)  **
  - **Description:** Grants permission to get the definition details of a specific security control identified by ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InviteMembers](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_InviteMembers.html)  **
  - **Description:** Grants permission to invite other AWS accounts to become Security Hub member accounts
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAggregatorsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListAggregatorsV2.html)  **
  - **Description:** Grants permission to retrieve a list of aggregatorsV2, which configures data aggregation across Regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationRules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to retrieve a list of automation rules and their metadata for the calling account from Security Hub
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationRulesV2](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to retrieve a list of automation rules V2 and their metadata for the calling account from Security Hub
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurationPolicies](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConfigurationPolicies.html)  **
  - **Description:** Grants permission to list the summaries of all configuration policies created by the calling account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurationPolicyAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConfigurationPolicyAssociations.html)  **
  - **Description:** Grants permission to retrieve information about all configuration policies associationed with all member accounts and organizational units of the calling account's organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectors](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConnectors.html)  **
  - **Description:** Grants permission to retrieve a list of connectors and their metadata for the calling account from Security Hub CSPM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectorsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConnectorsV2.html)  **
  - **Description:** Grants permission to retrieve a list of connectors V2 and their metadata for the calling account from Security Hub
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnabledProductsForImport](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListEnabledProductsForImport.html)  **
  - **Description:** Grants permission to retrieve the Security Hub integrated products that are currently enabled
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFindingAggregators](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListFindingAggregators.html)  **
  - **Description:** Grants permission to retrieve a list of finding aggregators, which contain the cross-Region finding aggregation configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFreeTrialStatusesV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListFreeTrialStatusesV2.html)  **
  - **Description:** Grants permission to retrieve a list of Security Hub free trial statuses for an account or accounts in an organization
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvitations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListInvitations.html)  **
  - **Description:** Grants permission to retrieve the Security Hub invitations sent to the account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMembers](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListMembers.html)  **
  - **Description:** Grants permission to retrieve details about Security Hub member accounts associated with the administrator account
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOrganizationAdminAccounts](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListOrganizationAdminAccounts.html)  **
  - **Description:** Grants permission to list the Security Hub administrator accounts for your organization
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSecurityControlDefinitions](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListSecurityControlDefinitions.html)  **
  - **Description:** Grants permission to retrieve a list of security control definitions, which contain details for security controls in the current region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html)  **
  - **Description:** Grants permission to list the enablement status of a security control in standards
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list of tags associated with a resource
  - **Resource types (\*required):** [automation-rule](#list_securityhub-resource-automation-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuration-policy](#list_securityhub-resource-configuration-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartConfigurationPolicyAssociation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StartConfigurationPolicyAssociation.html)  **
  - **Description:** Grants permission to associate a configuration policy with a member account or organizational unit in the calling account's organization
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartConfigurationPolicyDisassociation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StartConfigurationPolicyDisassociation.html)  **
  - **Description:** Grants permission to remove a configuration policy association from a member account or organizational unit in the calling account's organization
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a Security Hub resource
  - **Resource types (\*required):** [aggregatorv2](#list_securityhub-resource-aggregatorv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automation-rule](#list_securityhub-resource-automation-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automation-rulev2](#list_securityhub-resource-automation-rulev2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuration-policy](#list_securityhub-resource-configuration-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connector](#list_securityhub-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectorv2](#list_securityhub-resource-connectorv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a Security Hub resource
  - **Resource types (\*required):** [aggregatorv2](#list_securityhub-resource-aggregatorv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automation-rule](#list_securityhub-resource-automation-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automation-rulev2](#list_securityhub-resource-automation-rulev2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuration-policy](#list_securityhub-resource-configuration-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connector](#list_securityhub-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectorv2](#list_securityhub-resource-connectorv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateActionTarget](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateActionTarget.html)  **
  - **Description:** Grants permission to update custom actions in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAggregatorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateAggregatorV2.html)  **
  - **Description:** Grants permission to update an aggregatorV2, which configures data aggregation across Regions
  - **Resource types (\*required):** [aggregatorv2\*](#list_securityhub-resource-aggregatorv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutomationRuleV2](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  **
  - **Description:** Grants permission to update an automation rule V2 in Security Hub based on rule Amazon Resource Name (ARN) and input parameters
  - **Resource types (\*required):** [automation-rulev2\*](#list_securityhub-resource-automation-rulev2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfigurationPolicy](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateConfigurationPolicy.html)  **
  - **Description:** Grants permission to update an existing configuration policy
  - **Resource types (\*required):** [configuration-policy\*](#list_securityhub-resource-configuration-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConnector](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateConnector.html)  **
  - **Description:** Grants permission to update a connector in Security Hub CSPM based on connector id and input parameters
  - **Resource types (\*required):** [connector\*](#list_securityhub-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConnectorV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateConnectorV2.html)  **
  - **Description:** Grants permission to update a connector V2 in Security Hub based on connector id and input parameters
  - **Resource types (\*required):** [connectorv2\*](#list_securityhub-resource-connectorv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFindingAggregator](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateFindingAggregator.html)  **
  - **Description:** Grants permission to update a finding aggregator, which contains the cross-Region finding aggregation configuration
  - **Resource types (\*required):** [finding-aggregator\*](#list_securityhub-resource-finding-aggregator)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFindings](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateFindings.html)  **
  - **Description:** Grants permission to update Security Hub findings
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInsight](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateInsight.html)  **
  - **Description:** Grants permission to update insights in Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateOrganizationConfiguration.html)  **
  - **Description:** Grants permission to update the organization configuration for Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSecurityControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityControl.html)  **
  - **Description:** Grants permission to update properties of a specific security control identified by ID or ARN
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSecurityHubConfiguration](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityHubConfiguration.html)  **
  - **Description:** Grants permission to update Security Hub configuration
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStandardsControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html)  **
  - **Description:** Grants permission to update Security Hub standards controls
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Security Hub
<a name="list_securityhub-permission-only-actions"></a>

The following actions are defined by AWS Security Hub but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AllowVendedLogDeliveryForResource.html)  **
  - **Description:** Grants permission to log delivery for resources
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [BatchGetControlEvaluations](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-permissions-controls-standards.html)  **
  - **Description:** Grants permission to get the enablement and compliance status of controls, the findings count for controls, and the overall security score for controls on the Security Hub console
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetEnabledRegionsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetEnabledRegionsV2.html)  **
  - **Description:** Grants permission to retrieve Security Hub enabled regions for accounts in an organization
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAdhocInsightResults](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingStatisticsV2.html)  **
  - **Description:** Grants permission to retrieve aggregated statistical data about the findings
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hubv2](#list_securityhub-resource-hubv2) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetControlFindingSummary](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetControlFindingSummary.html)  **
  - **Description:** Grants permission to retrieve a security score and counts of finding and control statuses for a security standard
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCoverageStatisticsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetCoverageStatisticsV2.html)  **
  - **Description:** Grants permission to retrieve Security Hub coverage statistics in an organization
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFreeTrialEndDate](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFreeTrialEndDate.html)  **
  - **Description:** Grants permission to retrieve the end date for an account's free trial of Security Hub
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFreeTrialUsage](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFreeTrialUsage.html)  **
  - **Description:** Grants permission to retrieve information about Security Hub usage during the free trial period
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInsightFindingTrend](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetInsightFindingTrend.html)  **
  - **Description:** Grants permission to retrieve an insight finding trend from Security Hub in order to generate a graph
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUsage](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetUsage.html)  **
  - **Description:** Grants permission to retrieve information about Security Hub usage by accounts
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUsageV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetUsageV2.html)  **
  - **Description:** Grants permission to retrieve information about Security Hub usage for an account
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccountUsageV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListAccountUsageV2.html)  **
  - **Description:** Grants permission to retrieve a list of Security Hub usage for accounts in an organization
  - **Resource types (\*required):** [hubv2\*](#list_securityhub-resource-hubv2)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListControlEvaluationSummaries](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListControlEvaluationSummaries.html)  **
  - **Description:** Grants permission to retrieve a list of controls for a standard, including the control IDs, statuses and finding counts
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SendFindingEvents](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SendFindingEvents.html)  **
  - **Description:** Grants permission to use a custom action to send Security Hub findings to Amazon EventBridge
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SendInsightEvents](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SendInsightEvents.html)  **
  - **Description:** Grants permission to use a custom action to send Security Hub insights to Amazon EventBridge
  - **Resource types (\*required):** [hub](#list_securityhub-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by AWS Security Hub
<a name="list_securityhub-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [aggregatorv2](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources)  | arn:${Partition}:securityhub:${Region}:${Account}:aggregatorv2/${AggregatorV2Id} | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [automation-rule](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  | arn:${Partition}:securityhub:${Region}:${Account}:automation-rule/${AutomationRuleId} | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [automation-rulev2](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules)  | arn:${Partition}:securityhub:${Region}:${Account}:automation-rulev2/${AutomationRuleV2Id} | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [configuration-policy](https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html)  | arn:${Partition}:securityhub:${Region}:${Account}:configuration-policy/${ConfigurationPolicyId} | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [connector](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources)  | arn:${Partition}:securityhub:${Region}:${Account}:connector/${ConnectorId} | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [connectorv2](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources)  | arn:${Partition}:securityhub:${Region}:${Account}:connectorv2/${ConnectorV2Id} | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [finding-aggregator](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources)  | arn:${Partition}:securityhub:${Region}:${Account}:finding-aggregator/${FindingAggregatorId} |   | 
|  [hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources)  | arn:${Partition}:securityhub:${Region}:${Account}:hub/default | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [hubv2](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources)  | arn:${Partition}:securityhub:${Region}:${Account}:hubv2/${HubV2Id} | [aws:ResourceTag/${TagKey}](#list_securityhub-aws_ResourceTag___TagKey_) | 
|  [product](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources)  | arn:${Partition}:securityhub:${Region}:${Account}:product/${Company}/${ProductId} |   | 

## Condition keys for AWS Security Hub
<a name="list_securityhub-policy-keys"></a>

AWS Security Hub defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by actions based on the presence of tag keys in the request | ArrayOfString | 
|   [securityhub:ASFFSyntaxPath/${ASFFSyntaxPath}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-asffsyntaxpath)  | Filters access by the specified fields and values in the request | String | 
|   [securityhub:OCSFSyntaxPath/${OCSFSyntaxPath}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-ocsfsyntaxpath)  | Filters access by the specified fields and values in the request | String | 
|   [securityhub:TargetAccount](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#conditions)  | Filters access by the AwsAccountId field that is specified in the request | String | 