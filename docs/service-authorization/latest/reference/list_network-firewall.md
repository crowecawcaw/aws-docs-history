

# Actions, resources, and condition keys for AWS Network Firewall
<a name="list_network-firewall"></a>

AWS Network Firewall (service prefix: `network-firewall`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/network-firewall/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/network-firewall/network-firewall.json) for this service.

**Topics**
+ [API operations defined by AWS Network Firewall](#list_network-firewall-operations)
+ [Actions defined by AWS Network Firewall](#list_network-firewall-actions-as-permissions)
+ [Resource types defined by AWS Network Firewall](#list_network-firewall-resources-for-iam-policies)
+ [Condition keys for AWS Network Firewall](#list_network-firewall-policy-keys)

## API operations defined by AWS Network Firewall
<a name="list_network-firewall-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_network-firewall-actions-as-permissions).




- **   AcceptNetworkFirewallTransitGatewayAttachment  **
  - **IAM action:**  [network-firewall:AcceptNetworkFirewallTransitGatewayAttachment](#list_network-firewall-action-AcceptNetworkFirewallTransitGatewayAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateAvailabilityZones  **
  - **IAM action:**  [network-firewall:AssociateAvailabilityZones](#list_network-firewall-action-AssociateAvailabilityZones) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateFirewallPolicy  **
  - **IAM action:**  [network-firewall:AssociateFirewallPolicy](#list_network-firewall-action-AssociateFirewallPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateSubnets  **
  - **IAM action:**  [network-firewall:AssociateSubnets](#list_network-firewall-action-AssociateSubnets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachRuleGroupsToProxyConfiguration  **
  - **IAM action:**  [network-firewall:AttachRuleGroupsToProxyConfiguration](#list_network-firewall-action-AttachRuleGroupsToProxyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateContainerAssociation  **
  - **IAM action:**  [network-firewall:CreateContainerAssociation](#list_network-firewall-action-CreateContainerAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFirewall  **
  - **IAM action:**  [network-firewall:AssociateFirewallPolicy](#list_network-firewall-action-AssociateFirewallPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:CreateFirewall](#list_network-firewall-action-CreateFirewall)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFirewallPolicy  **
  - **IAM action:**  [network-firewall:CreateFirewallPolicy](#list_network-firewall-action-CreateFirewallPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:ListRuleGroups](#list_network-firewall-action-ListRuleGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [network-firewall:ListTLSInspectionConfigurations](#list_network-firewall-action-ListTLSInspectionConfigurations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProxy  **
  - **IAM action:**  [network-firewall:CreateProxy](#list_network-firewall-action-CreateProxy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProxyConfiguration  **
  - **IAM action:**  [network-firewall:AttachRuleGroupsToProxyConfiguration](#list_network-firewall-action-AttachRuleGroupsToProxyConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:CreateProxyConfiguration](#list_network-firewall-action-CreateProxyConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProxyRuleGroup  **
  - **IAM action:**  [network-firewall:CreateProxyRuleGroup](#list_network-firewall-action-CreateProxyRuleGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProxyRules  **
  - **IAM action:**  [network-firewall:CreateProxyRules](#list_network-firewall-action-CreateProxyRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRuleGroup  **
  - **IAM action:**  [network-firewall:CreateRuleGroup](#list_network-firewall-action-CreateRuleGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTLSInspectionConfiguration  **
  - **IAM action:**  [network-firewall:CreateTLSInspectionConfiguration](#list_network-firewall-action-CreateTLSInspectionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVpcEndpointAssociation  **
  - **IAM action:**  [network-firewall:CreateVpcEndpointAssociation](#list_network-firewall-action-CreateVpcEndpointAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [network-firewall:ListFirewalls](#list_network-firewall-action-ListFirewalls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteContainerAssociation  **
  - **IAM action:**  [network-firewall:DeleteContainerAssociation](#list_network-firewall-action-DeleteContainerAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFirewall  **
  - **IAM action:**  [network-firewall:DeleteFirewall](#list_network-firewall-action-DeleteFirewall) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFirewallPolicy  **
  - **IAM action:**  [network-firewall:DeleteFirewallPolicy](#list_network-firewall-action-DeleteFirewallPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNetworkFirewallTransitGatewayAttachment  **
  - **IAM action:**  [network-firewall:DeleteNetworkFirewallTransitGatewayAttachment](#list_network-firewall-action-DeleteNetworkFirewallTransitGatewayAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProxy  **
  - **IAM action:**  [network-firewall:DeleteProxy](#list_network-firewall-action-DeleteProxy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProxyConfiguration  **
  - **IAM action:**  [network-firewall:DeleteProxyConfiguration](#list_network-firewall-action-DeleteProxyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProxyRuleGroup  **
  - **IAM action:**  [network-firewall:DeleteProxyRuleGroup](#list_network-firewall-action-DeleteProxyRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProxyRules  **
  - **IAM action:**  [network-firewall:DeleteProxyRules](#list_network-firewall-action-DeleteProxyRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [network-firewall:DeleteResourcePolicy](#list_network-firewall-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRuleGroup  **
  - **IAM action:**  [network-firewall:DeleteRuleGroup](#list_network-firewall-action-DeleteRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTLSInspectionConfiguration  **
  - **IAM action:**  [network-firewall:DeleteTLSInspectionConfiguration](#list_network-firewall-action-DeleteTLSInspectionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcEndpointAssociation  **
  - **IAM action:**  [network-firewall:DeleteVpcEndpointAssociation](#list_network-firewall-action-DeleteVpcEndpointAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeContainerAssociation  **
  - **IAM action:**  [network-firewall:DescribeContainerAssociation](#list_network-firewall-action-DescribeContainerAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFirewall  **
  - **IAM action:**  [network-firewall:DescribeFirewall](#list_network-firewall-action-DescribeFirewall) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFirewallMetadata  **
  - **IAM action:**  [network-firewall:DescribeFirewallMetadata](#list_network-firewall-action-DescribeFirewallMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFirewallPolicy  **
  - **IAM action:**  [network-firewall:DescribeFirewallPolicy](#list_network-firewall-action-DescribeFirewallPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlowOperation  **
  - **IAM action:**  [network-firewall:DescribeFlowOperation](#list_network-firewall-action-DescribeFlowOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoggingConfiguration  **
  - **IAM action:**  [network-firewall:DescribeLoggingConfiguration](#list_network-firewall-action-DescribeLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProxy  **
  - **IAM action:**  [network-firewall:DescribeProxy](#list_network-firewall-action-DescribeProxy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProxyConfiguration  **
  - **IAM action:**  [network-firewall:DescribeProxyConfiguration](#list_network-firewall-action-DescribeProxyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProxyRule  **
  - **IAM action:**  [network-firewall:DescribeProxyRule](#list_network-firewall-action-DescribeProxyRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProxyRuleGroup  **
  - **IAM action:**  [network-firewall:DescribeProxyRuleGroup](#list_network-firewall-action-DescribeProxyRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourcePolicy  **
  - **IAM action:**  [network-firewall:DescribeResourcePolicy](#list_network-firewall-action-DescribeResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRuleGroup  **
  - **IAM action:**  [network-firewall:DescribeRuleGroup](#list_network-firewall-action-DescribeRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRuleGroupMetadata  **
  - **IAM action:**  [network-firewall:DescribeRuleGroupMetadata](#list_network-firewall-action-DescribeRuleGroupMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRuleGroupSummary  **
  - **IAM action:**  [network-firewall:DescribeRuleGroupSummary](#list_network-firewall-action-DescribeRuleGroupSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTLSInspectionConfiguration  **
  - **IAM action:**  [network-firewall:DescribeTLSInspectionConfiguration](#list_network-firewall-action-DescribeTLSInspectionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVpcEndpointAssociation  **
  - **IAM action:**  [network-firewall:DescribeVpcEndpointAssociation](#list_network-firewall-action-DescribeVpcEndpointAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachRuleGroupsFromProxyConfiguration  **
  - **IAM action:**  [network-firewall:DetachRuleGroupsFromProxyConfiguration](#list_network-firewall-action-DetachRuleGroupsFromProxyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAvailabilityZones  **
  - **IAM action:**  [network-firewall:DisassociateAvailabilityZones](#list_network-firewall-action-DisassociateAvailabilityZones) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateSubnets  **
  - **IAM action:**  [network-firewall:DisassociateSubnets](#list_network-firewall-action-DisassociateSubnets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAnalysisReportResults  **
  - **IAM action:**  [network-firewall:GetAnalysisReportResults](#list_network-firewall-action-GetAnalysisReportResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnalysisReports  **
  - **IAM action:**  [network-firewall:ListAnalysisReports](#list_network-firewall-action-ListAnalysisReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContainerAssociations  **
  - **IAM action:**  [network-firewall:ListContainerAssociations](#list_network-firewall-action-ListContainerAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFirewallPolicies  **
  - **IAM action:**  [network-firewall:ListFirewallPolicies](#list_network-firewall-action-ListFirewallPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFirewalls  **
  - **IAM action:**  [network-firewall:ListFirewalls](#list_network-firewall-action-ListFirewalls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlowOperationResults  **
  - **IAM action:**  [network-firewall:ListFlowOperationResults](#list_network-firewall-action-ListFlowOperationResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFlowOperations  **
  - **IAM action:**  [network-firewall:ListFlowOperations](#list_network-firewall-action-ListFlowOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProxies  **
  - **IAM action:**  [network-firewall:ListProxies](#list_network-firewall-action-ListProxies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProxyConfigurations  **
  - **IAM action:**  [network-firewall:ListProxyConfigurations](#list_network-firewall-action-ListProxyConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProxyRuleGroups  **
  - **IAM action:**  [network-firewall:ListProxyRuleGroups](#list_network-firewall-action-ListProxyRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleGroups  **
  - **IAM action:**  [network-firewall:ListRuleGroups](#list_network-firewall-action-ListRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTLSInspectionConfigurations  **
  - **IAM action:**  [network-firewall:ListTLSInspectionConfigurations](#list_network-firewall-action-ListTLSInspectionConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [network-firewall:ListTagsForResource](#list_network-firewall-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVpcEndpointAssociations  **
  - **IAM action:**  [network-firewall:ListVpcEndpointAssociations](#list_network-firewall-action-ListVpcEndpointAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutResourcePolicy  **
  - **IAM action:**  [network-firewall:PutResourcePolicy](#list_network-firewall-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectNetworkFirewallTransitGatewayAttachment  **
  - **IAM action:**  [network-firewall:RejectNetworkFirewallTransitGatewayAttachment](#list_network-firewall-action-RejectNetworkFirewallTransitGatewayAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAnalysisReport  **
  - **IAM action:**  [network-firewall:StartAnalysisReport](#list_network-firewall-action-StartAnalysisReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFlowCapture  **
  - **IAM action:**  [network-firewall:StartFlowCapture](#list_network-firewall-action-StartFlowCapture) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFlowFlush  **
  - **IAM action:**  [network-firewall:StartFlowFlush](#list_network-firewall-action-StartFlowFlush) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [network-firewall:TagResource](#list_network-firewall-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [network-firewall:UntagResource](#list_network-firewall-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAvailabilityZoneChangeProtection  **
  - **IAM action:**  [network-firewall:UpdateAvailabilityZoneChangeProtection](#list_network-firewall-action-UpdateAvailabilityZoneChangeProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContainerAssociation  **
  - **IAM action:**  [network-firewall:UpdateContainerAssociation](#list_network-firewall-action-UpdateContainerAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFirewallAnalysisSettings  **
  - **IAM action:**  [network-firewall:UpdateFirewallAnalysisSettings](#list_network-firewall-action-UpdateFirewallAnalysisSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFirewallDeleteProtection  **
  - **IAM action:**  [network-firewall:UpdateFirewallDeleteProtection](#list_network-firewall-action-UpdateFirewallDeleteProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFirewallDescription  **
  - **IAM action:**  [network-firewall:UpdateFirewallDescription](#list_network-firewall-action-UpdateFirewallDescription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFirewallEncryptionConfiguration  **
  - **IAM action:**  [network-firewall:UpdateFirewallEncryptionConfiguration](#list_network-firewall-action-UpdateFirewallEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFirewallPolicy  **
  - **IAM action:**  [network-firewall:ListRuleGroups](#list_network-firewall-action-ListRuleGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [network-firewall:ListTLSInspectionConfigurations](#list_network-firewall-action-ListTLSInspectionConfigurations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [network-firewall:UpdateFirewallPolicy](#list_network-firewall-action-UpdateFirewallPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateFirewallPolicyChangeProtection  **
  - **IAM action:**  [network-firewall:UpdateFirewallPolicyChangeProtection](#list_network-firewall-action-UpdateFirewallPolicyChangeProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLoggingConfiguration  **
  - **IAM action:**  [network-firewall:UpdateLoggingConfiguration](#list_network-firewall-action-UpdateLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProxy  **
  - **IAM action:**  [network-firewall:UpdateProxy](#list_network-firewall-action-UpdateProxy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProxyConfiguration  **
  - **IAM action:**  [network-firewall:UpdateProxyConfiguration](#list_network-firewall-action-UpdateProxyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProxyRule  **
  - **IAM action:**  [network-firewall:UpdateProxyRule](#list_network-firewall-action-UpdateProxyRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProxyRuleGroupPriorities  **
  - **IAM action:**  [network-firewall:UpdateProxyRuleGroupPriorities](#list_network-firewall-action-UpdateProxyRuleGroupPriorities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProxyRulePriorities  **
  - **IAM action:**  [network-firewall:UpdateProxyRulePriorities](#list_network-firewall-action-UpdateProxyRulePriorities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuleGroup  **
  - **IAM action:**  [network-firewall:UpdateRuleGroup](#list_network-firewall-action-UpdateRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubnetChangeProtection  **
  - **IAM action:**  [network-firewall:UpdateSubnetChangeProtection](#list_network-firewall-action-UpdateSubnetChangeProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTLSInspectionConfiguration  **
  - **IAM action:**  [network-firewall:UpdateTLSInspectionConfiguration](#list_network-firewall-action-UpdateTLSInspectionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Network Firewall
<a name="list_network-firewall-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptNetworkFirewallTransitGatewayAttachment](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AcceptNetworkFirewallTransitGatewayAttachment.html)  **
  - **Description:** Grants permission to accept pending Network Firewall attachments on a transit gateway
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateAvailabilityZones](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AssociateAvailabilityZones.html)  **
  - **Description:** Grants permission to associate availability zones to a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateFirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AssociateFirewallPolicy.html)  **
  - **Description:** Grants permission to create an association between a firewall policy and a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [AssociateSubnets](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AssociateSubnets.html)  **
  - **Description:** Grants permission to associate VPC subnets to a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachRuleGroupsToProxyConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AttachRuleGroupsToProxyConfiguration.html)  **
  - **Description:** Grants permission to attach proxy rule groups to a proxy configuration
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateContainerAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateContainerAssociation.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall container association
  - **Resource types (\*required):** [ContainerAssociation\*](#list_network-firewall-resource-ContainerAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFirewall](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateFirewall.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateFirewallPolicy.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall firewall policy
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [TLSInspectionConfiguration](#list_network-firewall-resource-TLSInspectionConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProxy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateProxy.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall proxy
  - **Resource types (\*required):** [Proxy\*](#list_network-firewall-resource-Proxy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProxyConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateProxyConfiguration.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall proxy configuration
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [ProxyRuleGroup](#list_network-firewall-resource-ProxyRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProxyRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateProxyRuleGroup.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall proxy rule group
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProxyRules](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateProxyRules.html)  **
  - **Description:** Grants permission to add proxy rules to a proxy rule group
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateRuleGroup.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall rule group
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTLSInspectionConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateTLSInspectionConfiguration.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall tls inspection configuration
  - **Resource types (\*required):** [TLSInspectionConfiguration\*](#list_network-firewall-resource-TLSInspectionConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVpcEndpointAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateVpcEndpointAssociation.html)  **
  - **Description:** Grants permission to create an AWS Network Firewall vpc endpoint association
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [VpcEndpointAssociation\*](#list_network-firewall-resource-VpcEndpointAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteContainerAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteContainerAssociation.html)  **
  - **Description:** Grants permission to delete an AWS Network Firewall container association
  - **Resource types (\*required):** [ContainerAssociation\*](#list_network-firewall-resource-ContainerAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFirewall](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteFirewall.html)  **
  - **Description:** Grants permission to delete a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteFirewallPolicy.html)  **
  - **Description:** Grants permission to delete a firewall policy
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetworkFirewallTransitGatewayAttachment](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteNetworkFirewallTransitGatewayAttachment.html)  **
  - **Description:** Grants permission to delete Network Firewall attachments on a transit gateway
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProxy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteProxy.html)  **
  - **Description:** Grants permission to delete a proxy
  - **Resource types (\*required):** [Proxy\*](#list_network-firewall-resource-Proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProxyConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteProxyConfiguration.html)  **
  - **Description:** Grants permission to delete a proxy configuration
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProxyRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteProxyRuleGroup.html)  **
  - **Description:** Grants permission to delete a proxy rule group
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProxyRules](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteProxyRules.html)  **
  - **Description:** Grants permission to remove proxy rules from a proxy rule group
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy for a firewall policy or rule group or firewall
  - **Resource types (\*required):** [Firewall](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [FirewallPolicy](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteRuleGroup.html)  **
  - **Description:** Grants permission to delete a rule group
  - **Resource types (\*required):** [StatefulRuleGroup\*](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup\*](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTLSInspectionConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteTLSInspectionConfiguration.html)  **
  - **Description:** Grants permission to delete a tls inspection configuration
  - **Resource types (\*required):** [TLSInspectionConfiguration\*](#list_network-firewall-resource-TLSInspectionConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVpcEndpointAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteVpcEndpointAssociation.html)  **
  - **Description:** Grants permission to delete a vpc endpoint association
  - **Resource types (\*required):** [VpcEndpointAssociation\*](#list_network-firewall-resource-VpcEndpointAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeContainerAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeContainerAssociation.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a container association
  - **Resource types (\*required):** [ContainerAssociation\*](#list_network-firewall-resource-ContainerAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFirewall](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeFirewall.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFirewallMetadata](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeFirewallMetadata.html)  **
  - **Description:** Grants permission to retrieve the high-level information about a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeFirewallPolicy.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a firewall policy
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [TLSInspectionConfiguration](#list_network-firewall-resource-TLSInspectionConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlowOperation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeFlowOperation.html)  **
  - **Description:** Grants permission to describe a flow operation performed on a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLoggingConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeLoggingConfiguration.html)  **
  - **Description:** Grants permission to describe the logging configuration of a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProxy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeProxy.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a proxy
  - **Resource types (\*required):** [Proxy\*](#list_network-firewall-resource-Proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProxyConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeProxyConfiguration.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a proxy configuration
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProxyRule](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeProxyRule.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a proxy rule
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProxyRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeProxyRuleGroup.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a proxy rule group
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeResourcePolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeResourcePolicy.html)  **
  - **Description:** Grants permission to describe a resource policy for a firewall policy or rule group or firewall
  - **Resource types (\*required):** [Firewall](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [FirewallPolicy](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a rule group
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRuleGroupMetadata](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroupMetadata.html)  **
  - **Description:** Grants permission to retrieve the high-level information about a rule group
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRuleGroupSummary](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroupSummary.html)  **
  - **Description:** Grants permission to retrieve the summary information about a rule group
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTLSInspectionConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeTLSInspectionConfiguration.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a tls inspection configuration
  - **Resource types (\*required):** [TLSInspectionConfiguration\*](#list_network-firewall-resource-TLSInspectionConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVpcEndpointAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeVpcEndpointAssociation.html)  **
  - **Description:** Grants permission to retrieve the data objects that define a vpc endpoint association
  - **Resource types (\*required):** [VpcEndpointAssociation\*](#list_network-firewall-resource-VpcEndpointAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetachRuleGroupsFromProxyConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DetachRuleGroupsFromProxyConfiguration.html)  **
  - **Description:** Grants permission to detach proxy rule groups from a proxy configuration
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateAvailabilityZones](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DisassociateAvailabilityZones.html)  **
  - **Description:** Grants permission to disassociate availability zones to a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSubnets](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DisassociateSubnets.html)  **
  - **Description:** Grants permission to disassociate VPC subnets from a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAnalysisReportResults](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_GetAnalysisReportResults.html)  **
  - **Description:** Grants permission to retrieve analysis report results of a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAnalysisReports](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListAnalysisReports.html)  **
  - **Description:** Grants permission to list firewall analysis reports
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListContainerAssociations](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListContainerAssociations.html)  **
  - **Description:** Grants permission to retrieve the metadata for container associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFirewallPolicies](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListFirewallPolicies.html)  **
  - **Description:** Grants permission to retrieve the metadata for firewall policies
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFirewalls](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListFirewalls.html)  **
  - **Description:** Grants permission to retrieve the metadata for firewalls
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFlowOperationResults](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListFlowOperationResults.html)  **
  - **Description:** Grants permission to list results from a flow operation performed on a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFlowOperations](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListFlowOperations.html)  **
  - **Description:** Grants permission to list flow operations performed on a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProxies](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListProxies.html)  **
  - **Description:** Grants permission to retrieve the metadata for proxies
  - **Resource types (\*required):** [Proxy\*](#list_network-firewall-resource-Proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProxyConfigurations](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListProxyConfigurations.html)  **
  - **Description:** Grants permission to retrieve the metadata for proxy configurations
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProxyRuleGroups](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListProxyRuleGroups.html)  **
  - **Description:** Grants permission to retrieve the metadata for proxy rule groups
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRuleGroups](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListRuleGroups.html)  **
  - **Description:** Grants permission to retrieve the metadata for rule groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTLSInspectionConfigurations](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListTLSInspectionConfigurations.html)  **
  - **Description:** Grants permission to retrieve the metadata for tls inspection configurations
  - **Resource types (\*required):** [TLSInspectionConfiguration\*](#list_network-firewall-resource-TLSInspectionConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve the tags for a resource
  - **Resource types (\*required):** [ContainerAssociation](#list_network-firewall-resource-ContainerAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [TLSInspectionConfiguration](#list_network-firewall-resource-TLSInspectionConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VpcEndpointAssociation](#list_network-firewall-resource-VpcEndpointAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVpcEndpointAssociations](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListVpcEndpointAssociations.html)  **
  - **Description:** Grants permission to retrieve the metadata for vpc endpoint associations
  - **Resource types (\*required):** [VpcEndpointAssociation\*](#list_network-firewall-resource-VpcEndpointAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to put a resource policy for a firewall policy or rule group or firewall
  - **Resource types (\*required):** [Firewall](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [FirewallPolicy](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RejectNetworkFirewallTransitGatewayAttachment](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RejectNetworkFirewallTransitGatewayAttachment.html)  **
  - **Description:** Grants permission to reject pending Network Firewall attachments on a transit gateway
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAnalysisReport](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_GetAnalysisReportResults.html)  **
  - **Description:** Grants permission to start an analysis report on a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFlowCapture](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StartFlowCapture.html)  **
  - **Description:** Grants permission to start capture operation on a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFlowFlush](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StartFlowFlush.html)  **
  - **Description:** Grants permission to start flush operation on a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to attach tags to a resource
  - **Resource types (\*required):** [ContainerAssociation](#list_network-firewall-resource-ContainerAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [Firewall](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [FirewallPolicy](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [Proxy](#list_network-firewall-resource-Proxy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [ProxyConfiguration](#list_network-firewall-resource-ProxyConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [ProxyRuleGroup](#list_network-firewall-resource-ProxyRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [TLSInspectionConfiguration](#list_network-firewall-resource-TLSInspectionConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [VpcEndpointAssociation](#list_network-firewall-resource-VpcEndpointAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_network-firewall-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [ContainerAssociation](#list_network-firewall-resource-ContainerAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [Firewall](#list_network-firewall-resource-Firewall) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [FirewallPolicy](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [Proxy](#list_network-firewall-resource-Proxy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [ProxyConfiguration](#list_network-firewall-resource-ProxyConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [ProxyRuleGroup](#list_network-firewall-resource-ProxyRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [TLSInspectionConfiguration](#list_network-firewall-resource-TLSInspectionConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Resource types (\*required):** [VpcEndpointAssociation](#list_network-firewall-resource-VpcEndpointAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_network-firewall-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAvailabilityZoneChangeProtection](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateAvailabilityZoneChangeProtection.html)  **
  - **Description:** Grants permission to add or remove availability zone change protection for a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContainerAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateContainerAssociation.html)  **
  - **Description:** Grants permission to update an AWS Network Firewall container association
  - **Resource types (\*required):** [ContainerAssociation\*](#list_network-firewall-resource-ContainerAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallAnalysisSettings](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallAnalysisSettings.html)  **
  - **Description:** Grants permission to modify firewall analysis settings of a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallDeleteProtection](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallDeleteProtection.html)  **
  - **Description:** Grants permission to add or remove delete protection for a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallDescription](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallDescription.html)  **
  - **Description:** Grants permission to modify the description for a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallEncryptionConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallEncryptionConfiguration.html)  **
  - **Description:** Grants permission to modify the encryption configuration of a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallPolicy.html)  **
  - **Description:** Grants permission to modify a firewall policy
  - **Resource types (\*required):** [FirewallPolicy\*](#list_network-firewall-resource-FirewallPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [TLSInspectionConfiguration](#list_network-firewall-resource-TLSInspectionConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallPolicyChangeProtection](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallPolicyChangeProtection.html)  **
  - **Description:** Grants permission to add or remove firewall policy change protection for a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLoggingConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateLoggingConfiguration.html)  **
  - **Description:** Grants permission to modify the logging configuration of a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProxy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateProxy.html)  **
  - **Description:** Grants permission to modify a proxy
  - **Resource types (\*required):** [Proxy\*](#list_network-firewall-resource-Proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProxyConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateProxyConfiguration.html)  **
  - **Description:** Grants permission to modify a proxy configuration
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProxyRule](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateProxyRule.html)  **
  - **Description:** Grants permission to update an existing proxy rule on a proxy rule group
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProxyRuleGroupPriorities](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateProxyRuleGroupPriorities.html)  **
  - **Description:** Grants permission to modify rule group priorities on a proxy configuration
  - **Resource types (\*required):** [ProxyConfiguration\*](#list_network-firewall-resource-ProxyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProxyRulePriorities](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateProxyRulePriorities.html)  **
  - **Description:** Grants permission to update proxy rule priorities within a proxy rule group
  - **Resource types (\*required):** [ProxyRuleGroup\*](#list_network-firewall-resource-ProxyRuleGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateRuleGroup.html)  **
  - **Description:** Grants permission to modify a rule group
  - **Resource types (\*required):** [StatefulRuleGroup](#list_network-firewall-resource-StatefulRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [StatelessRuleGroup](#list_network-firewall-resource-StatelessRuleGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSubnetChangeProtection](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateSubnetChangeProtection.html)  **
  - **Description:** Grants permission to add or remove subnet change protection for a firewall
  - **Resource types (\*required):** [Firewall\*](#list_network-firewall-resource-Firewall)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTLSInspectionConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateTLSInspectionConfiguration.html)  **
  - **Description:** Grants permission to modify a tls inspection configuration
  - **Resource types (\*required):** [TLSInspectionConfiguration\*](#list_network-firewall-resource-TLSInspectionConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Network Firewall
<a name="list_network-firewall-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ContainerAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContainerAssociation.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:container-association/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [Firewall](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Firewall.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:firewall/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [FirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicyResponse.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:firewall-policy/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [Proxy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Proxy.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:proxy/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [ProxyConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ProxyConfiguration.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:proxy-configuration/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [ProxyRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ProxyRuleGroup.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:proxy-rule-group/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [StatefulRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleGroupResponse.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:stateful-rulegroup/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [StatelessRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleGroupResponse.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:stateless-rulegroup/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [TLSInspectionConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_TLSInspectionConfigurationResponse.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:tls-configuration/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 
|  [VpcEndpointAssociation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_VpcEndpointAssociation.html)  | arn:${Partition}:network-firewall:${Region}:${Account}:vpc-endpoint-association/${Name} | [aws:ResourceTag/${TagKey}](#list_network-firewall-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Network Firewall
<a name="list_network-firewall-policy-keys"></a>

AWS Network Firewall defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 