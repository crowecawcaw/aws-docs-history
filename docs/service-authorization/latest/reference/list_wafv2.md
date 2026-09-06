

# Actions, resources, and condition keys for AWS WAF V2
<a name="list_wafv2"></a>

AWS WAF V2 (service prefix: `wafv2`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/waf/latest/APIReference/API_Operations_AWS_WAFV2.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/waf/latest/developerguide/waf-auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/wafv2/wafv2.json) for this service.

**Topics**
+ [API operations defined by AWS WAF V2](#list_wafv2-operations)
+ [Actions defined by AWS WAF V2](#list_wafv2-actions-as-permissions)
+ [Permission-only actions for AWS WAF V2](#list_wafv2-permission-only-actions)
+ [Resource types defined by AWS WAF V2](#list_wafv2-resources-for-iam-policies)
+ [Condition keys for AWS WAF V2](#list_wafv2-policy-keys)

## API operations defined by AWS WAF V2
<a name="list_wafv2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_wafv2-actions-as-permissions).




- **   AssociateWebACL  **
  - **IAM action:**  [wafv2:AssociateWebACL](#list_wafv2-action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:SetWebACL](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [appsync:AssociateWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:SetWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [elasticloadbalancing:CreateWebACLAssociation](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticloadbalancing:SetWebAcl](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CheckCapacity  **
  - **IAM action:**  [wafv2:CheckCapacity](#list_wafv2-action-CheckCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateAPIKey  **
  - **IAM action:**  [wafv2:CreateAPIKey](#list_wafv2-action-CreateAPIKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIPSet  **
  - **IAM action:**  [wafv2:CreateIPSet](#list_wafv2-action-CreateIPSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wafv2:TagResource](#list_wafv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegexPatternSet  **
  - **IAM action:**  [wafv2:CreateRegexPatternSet](#list_wafv2-action-CreateRegexPatternSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wafv2:TagResource](#list_wafv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRuleGroup  **
  - **IAM action:**  [wafv2:CreateRuleGroup](#list_wafv2-action-CreateRuleGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wafv2:TagResource](#list_wafv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWebACL  **
  - **IAM action:**  [wafv2:CreateWebACL](#list_wafv2-action-CreateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wafv2:TagResource](#list_wafv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAPIKey  **
  - **IAM action:**  [wafv2:DeleteAPIKey](#list_wafv2-action-DeleteAPIKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFirewallManagerRuleGroups  **
  - **IAM action:**  [wafv2:DeleteFirewallManagerRuleGroups](#list_wafv2-action-DeleteFirewallManagerRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIPSet  **
  - **IAM action:**  [wafv2:DeleteIPSet](#list_wafv2-action-DeleteIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoggingConfiguration  **
  - **IAM action:**  [wafv2:DeleteLoggingConfiguration](#list_wafv2-action-DeleteLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePermissionPolicy  **
  - **IAM action:**  [wafv2:DeletePermissionPolicy](#list_wafv2-action-DeletePermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteRegexPatternSet  **
  - **IAM action:**  [wafv2:DeleteRegexPatternSet](#list_wafv2-action-DeleteRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRuleGroup  **
  - **IAM action:**  [wafv2:DeleteRuleGroup](#list_wafv2-action-DeleteRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebACL  **
  - **IAM action:**  [wafv2:DeleteWebACL](#list_wafv2-action-DeleteWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAllManagedProducts  **
  - **IAM action:**  [wafv2:DescribeAllManagedProducts](#list_wafv2-action-DescribeAllManagedProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeManagedProductsByVendor  **
  - **IAM action:**  [wafv2:DescribeManagedProductsByVendor](#list_wafv2-action-DescribeManagedProductsByVendor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeManagedRuleGroup  **
  - **IAM action:**  [wafv2:DescribeManagedRuleGroup](#list_wafv2-action-DescribeManagedRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateWebACL  **
  - **IAM action:**  [wafv2:DisassociateWebACL](#list_wafv2-action-DisassociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:SetWebACL](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [appsync:DisassociateWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:SetWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [elasticloadbalancing:DeleteWebACLAssociation](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticloadbalancing:SetWebAcl](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GenerateMobileSdkReleaseUrl  **
  - **IAM action:**  [wafv2:GenerateMobileSdkReleaseUrl](#list_wafv2-action-GenerateMobileSdkReleaseUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDecryptedAPIKey  **
  - **IAM action:**  [wafv2:GetDecryptedAPIKey](#list_wafv2-action-GetDecryptedAPIKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIPSet  **
  - **IAM action:**  [wafv2:GetIPSet](#list_wafv2-action-GetIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoggingConfiguration  **
  - **IAM action:**  [wafv2:GetLoggingConfiguration](#list_wafv2-action-GetLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedRuleSet  **
  - **IAM action:**  [wafv2:GetManagedRuleSet](#list_wafv2-action-GetManagedRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMobileSdkRelease  **
  - **IAM action:**  [wafv2:GetMobileSdkRelease](#list_wafv2-action-GetMobileSdkRelease) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPermissionPolicy  **
  - **IAM action:**  [wafv2:GetPermissionPolicy](#list_wafv2-action-GetPermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRateBasedStatementManagedKeys  **
  - **IAM action:**  [wafv2:GetRateBasedStatementManagedKeys](#list_wafv2-action-GetRateBasedStatementManagedKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegexPatternSet  **
  - **IAM action:**  [wafv2:GetRegexPatternSet](#list_wafv2-action-GetRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevenueStatistics  **
  - **IAM action:**  [wafv2:GetRevenueStatistics](#list_wafv2-action-GetRevenueStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevenueStatisticsSummary  **
  - **IAM action:**  [wafv2:GetRevenueStatisticsSummary](#list_wafv2-action-GetRevenueStatisticsSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevenueStatisticsTimeSeries  **
  - **IAM action:**  [wafv2:GetRevenueStatisticsTimeSeries](#list_wafv2-action-GetRevenueStatisticsTimeSeries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRuleGroup  **
  - **IAM action:**  [wafv2:GetRuleGroup](#list_wafv2-action-GetRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSampledRequests  **
  - **IAM action:**  [wafv2:GetSampledRequests](#list_wafv2-action-GetSampledRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTopPathStatisticsByTraffic  **
  - **IAM action:**  [wafv2:GetTopPathStatisticsByTraffic](#list_wafv2-action-GetTopPathStatisticsByTraffic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebACL  **
  - **IAM action:**  [wafv2:GetWebACL](#list_wafv2-action-GetWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebACLForResource  **
  - **IAM action:**  [wafv2:GetWebACLForResource](#list_wafv2-action-GetWebACLForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [appsync:GetWebACLForResource](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [elasticloadbalancing:GetLoadBalancerWebACL](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListAPIKeys  **
  - **IAM action:**  [wafv2:ListAPIKeys](#list_wafv2-action-ListAPIKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAvailableManagedRuleGroupVersions  **
  - **IAM action:**  [wafv2:ListAvailableManagedRuleGroupVersions](#list_wafv2-action-ListAvailableManagedRuleGroupVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAvailableManagedRuleGroups  **
  - **IAM action:**  [wafv2:ListAvailableManagedRuleGroups](#list_wafv2-action-ListAvailableManagedRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIPSets  **
  - **IAM action:**  [wafv2:ListIPSets](#list_wafv2-action-ListIPSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLoggingConfigurations  **
  - **IAM action:**  [wafv2:ListLoggingConfigurations](#list_wafv2-action-ListLoggingConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedRuleSets  **
  - **IAM action:**  [wafv2:ListManagedRuleSets](#list_wafv2-action-ListManagedRuleSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMobileSdkReleases  **
  - **IAM action:**  [wafv2:ListMobileSdkReleases](#list_wafv2-action-ListMobileSdkReleases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegexPatternSets  **
  - **IAM action:**  [wafv2:ListRegexPatternSets](#list_wafv2-action-ListRegexPatternSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourcesForWebACL  **
  - **IAM action:**  [wafv2:ListResourcesForWebACL](#list_wafv2-action-ListResourcesForWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [appsync:ListResourcesForWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [elasticloadbalancing:DescribeWebACLAssociation](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListRuleGroups  **
  - **IAM action:**  [wafv2:ListRuleGroups](#list_wafv2-action-ListRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSettlementRecords  **
  - **IAM action:**  [wafv2:ListSettlementRecords](#list_wafv2-action-ListSettlementRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [wafv2:ListTagsForResource](#list_wafv2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWebACLs  **
  - **IAM action:**  [wafv2:ListWebACLs](#list_wafv2-action-ListWebACLs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutLoggingConfiguration  **
  - **IAM action:**  [wafv2:PutLoggingConfiguration](#list_wafv2-action-PutLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutManagedRuleSetVersions  **
  - **IAM action:**  [wafv2:PutManagedRuleSetVersions](#list_wafv2-action-PutManagedRuleSetVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPermissionPolicy  **
  - **IAM action:**  [wafv2:PutPermissionPolicy](#list_wafv2-action-PutPermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   TagResource  **
  - **IAM action:**  [wafv2:TagResource](#list_wafv2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [wafv2:UntagResource](#list_wafv2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateIPSet  **
  - **IAM action:**  [wafv2:UpdateIPSet](#list_wafv2-action-UpdateIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateManagedRuleSetVersionExpiryDate  **
  - **IAM action:**  [wafv2:UpdateManagedRuleSetVersionExpiryDate](#list_wafv2-action-UpdateManagedRuleSetVersionExpiryDate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegexPatternSet  **
  - **IAM action:**  [wafv2:UpdateRegexPatternSet](#list_wafv2-action-UpdateRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuleGroup  **
  - **IAM action:**  [wafv2:UpdateRuleGroup](#list_wafv2-action-UpdateRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWebACL  **
  - **IAM action:**  [wafv2:UpdateWebACL](#list_wafv2-action-UpdateWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS WAF V2
<a name="list_wafv2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociateWebACL.html)  **
  - **Description:** Grants permission to associate a WebACL with a resource
  - **Resource types (\*required):** [agentcore-gateway](#list_wafv2-resource-agentcore-gateway) / **Condition keys:**  
  - **Resource types (\*required):** [amplify-app](#list_wafv2-resource-amplify-app) / **Condition keys:**  
  - **Resource types (\*required):** [apigateway](#list_wafv2-resource-apigateway) / **Condition keys:**  
  - **Resource types (\*required):** [apprunner](#list_wafv2-resource-apprunner) / **Condition keys:**  
  - **Resource types (\*required):** [appsync](#list_wafv2-resource-appsync) / **Condition keys:**  
  - **Resource types (\*required):** [loadbalancer/app/](#list_wafv2-resource-loadbalancer_app_) / **Condition keys:**  
  - **Resource types (\*required):** [userpool](#list_wafv2-resource-userpool) / **Condition keys:**  
  - **Resource types (\*required):** [verified-access-instance](#list_wafv2-resource-verified-access-instance) / **Condition keys:**  
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CheckCapacity](https://docs.aws.amazon.com/waf/latest/APIReference/API_CheckCapacity.html)  **
  - **Description:** Grants permission to calculate web ACL capacity unit (WCU) requirements for a specified scope and set of rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateAPIKey](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateAPIKey.html)  **
  - **Description:** Grants permission to create an API key for use in the integration of the CAPTCHA API in your JavaScript client applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateIPSet.html)  **
  - **Description:** Grants permission to create an IPSet
  - **Resource types (\*required):** [ipset\*](#list_wafv2-resource-ipset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateRegexPatternSet.html)  **
  - **Description:** Grants permission to create a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_wafv2-resource-regexpatternset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateRuleGroup.html)  **
  - **Description:** Grants permission to create a RuleGroup
  - **Resource types (\*required):** [ipset](#list_wafv2-resource-ipset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [regexpatternset](#list_wafv2-resource-regexpatternset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateWebACL.html)  **
  - **Description:** Grants permission to create a WebACL
  - **Resource types (\*required):** [ipset](#list_wafv2-resource-ipset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [managedruleset](#list_wafv2-resource-managedruleset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [regexpatternset](#list_wafv2-resource-regexpatternset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAPIKey](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteAPIKey.html)  **
  - **Description:** Grants permission to delete an API key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFirewallManagerRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteFirewallManagerRuleGroups.html)  **
  - **Description:** Grants permission to delete FirewallManagedRulesGroups from a WebACL if not managed by Firewall Manager anymore
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteIPSet.html)  **
  - **Description:** Grants permission to delete an IPSet
  - **Resource types (\*required):** [ipset\*](#list_wafv2-resource-ipset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete the LoggingConfiguration from a WebACL
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[wafv2:LogScope](#list_wafv2-wafv2_LogScope)
  - **Access level:** Write

- **   [DeletePermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeletePermissionPolicy.html)  **
  - **Description:** Grants permission to delete the PermissionPolicy on a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteRegexPatternSet.html)  **
  - **Description:** Grants permission to delete a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_wafv2-resource-regexpatternset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteRuleGroup.html)  **
  - **Description:** Grants permission to delete a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteWebACL.html)  **
  - **Description:** Grants permission to delete a WebACL
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAllManagedProducts](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeAllManagedProducts.html)  **
  - **Description:** Grants permission to retrieve product information for a managed rule group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeManagedProductsByVendor](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeManagedProductsByVendor.html)  **
  - **Description:** Grants permission to retrieve product information for a managed rule group by a given vendor
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeManagedRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeManagedRuleGroup.html)  **
  - **Description:** Grants permission to retrieve high-level information for a managed rule group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_DisassociateWebACL.html)  **
  - **Description:** Grants permission to disassociate a WebACL from an application resource
  - **Resource types (\*required):** [agentcore-gateway](#list_wafv2-resource-agentcore-gateway) / **Condition keys:**  
  - **Resource types (\*required):** [amplify-app](#list_wafv2-resource-amplify-app) / **Condition keys:**  
  - **Resource types (\*required):** [apigateway](#list_wafv2-resource-apigateway) / **Condition keys:**  
  - **Resource types (\*required):** [apprunner](#list_wafv2-resource-apprunner) / **Condition keys:**  
  - **Resource types (\*required):** [appsync](#list_wafv2-resource-appsync) / **Condition keys:**  
  - **Resource types (\*required):** [loadbalancer/app/](#list_wafv2-resource-loadbalancer_app_) / **Condition keys:**  
  - **Resource types (\*required):** [userpool](#list_wafv2-resource-userpool) / **Condition keys:**  
  - **Resource types (\*required):** [verified-access-instance](#list_wafv2-resource-verified-access-instance) / **Condition keys:**  
  - **Access level:** Write

- **   [GenerateMobileSdkReleaseUrl](https://docs.aws.amazon.com/waf/latest/APIReference/API_GenerateMobileSdkReleaseUrl.html)  **
  - **Description:** Grants permission to generate a presigned download URL for the specified release of the mobile SDK
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDecryptedAPIKey](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetDecryptedAPIKey.html)  **
  - **Description:** Grants permission to return your API key in decrypted form. Use this to check the token domains that you have defined for the key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetIPSet.html)  **
  - **Description:** Grants permission to retrieve details about an IPSet
  - **Resource types (\*required):** [ipset\*](#list_wafv2-resource-ipset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetLoggingConfiguration.html)  **
  - **Description:** Grants permission to retrieve LoggingConfiguration for a WebACL
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[wafv2:LogScope](#list_wafv2-wafv2_LogScope)
  - **Access level:** Read

- **   [GetManagedRuleSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetManagedRuleSet.html)  **
  - **Description:** Grants permission to retrieve details about a ManagedRuleSet
  - **Resource types (\*required):** [managedruleset\*](#list_wafv2-resource-managedruleset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMobileSdkRelease](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetMobileSdkRelease.html)  **
  - **Description:** Grants permission to retrieve information for the specified mobile SDK release, including release notes and tags
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetPermissionPolicy.html)  **
  - **Description:** Grants permission to retrieve a PermissionPolicy for a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRateBasedStatementManagedKeys](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRateBasedStatementManagedKeys.html)  **
  - **Description:** Grants permission to retrieve the keys that are currently blocked by a rate-based rule
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRegexPatternSet.html)  **
  - **Description:** Grants permission to retrieve details about a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_wafv2-resource-regexpatternset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRevenueStatistics](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRevenueStatistics.html)  **
  - **Description:** Grants permission to retrieve monetization revenue statistics ranked by source or path within a specified time window
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRevenueStatisticsSummary](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRevenueStatisticsSummary.html)  **
  - **Description:** Grants permission to retrieve a summary of monetization revenue statistics within a specified time window
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRevenueStatisticsTimeSeries](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRevenueStatisticsTimeSeries.html)  **
  - **Description:** Grants permission to retrieve monetization revenue statistics as a time series within a specified time window
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRuleGroup.html)  **
  - **Description:** Grants permission to retrieve details about a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSampledRequests](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetSampledRequests.html)  **
  - **Description:** Grants permission to retrieve detailed information about a sampling of web requests
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTopPathStatisticsByTraffic](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetTopPathStatisticsByTraffic.html)  **
  - **Description:** Grants permission to retrieve aggregated path statistics with bot traffic analysis for a WebACL within a specified time window
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetWebACL.html)  **
  - **Description:** Grants permission to retrieve details about a WebACL
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWebACLForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetWebACLForResource.html)  **
  - **Description:** Grants permission to retrieve the WebACL that's associated with a resource
  - **Resource types (\*required):** [agentcore-gateway](#list_wafv2-resource-agentcore-gateway) / **Condition keys:**  
  - **Resource types (\*required):** [amplify-app](#list_wafv2-resource-amplify-app) / **Condition keys:**  
  - **Resource types (\*required):** [apigateway](#list_wafv2-resource-apigateway) / **Condition keys:**  
  - **Resource types (\*required):** [apprunner](#list_wafv2-resource-apprunner) / **Condition keys:**  
  - **Resource types (\*required):** [appsync](#list_wafv2-resource-appsync) / **Condition keys:**  
  - **Resource types (\*required):** [loadbalancer/app/](#list_wafv2-resource-loadbalancer_app_) / **Condition keys:**  
  - **Resource types (\*required):** [userpool](#list_wafv2-resource-userpool) / **Condition keys:**  
  - **Resource types (\*required):** [verified-access-instance](#list_wafv2-resource-verified-access-instance) / **Condition keys:**  
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAPIKeys](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListAPIKeys.html)  **
  - **Description:** Grants permission to retrieve a list of the API keys that you've defined for the specified scope
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAvailableManagedRuleGroupVersions](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListAvailableManagedRuleGroupVersions.html)  **
  - **Description:** Grants permission to retrieve an array of managed rule group versions that are available for you to use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAvailableManagedRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListAvailableManagedRuleGroups.html)  **
  - **Description:** Grants permission to retrieve an array of managed rule groups that are available for you to use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIPSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListIPSets.html)  **
  - **Description:** Grants permission to retrieve an array of IPSetSummary objects for the IP sets that you manage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLoggingConfigurations](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListLoggingConfigurations.html)  **
  - **Description:** Grants permission to retrieve an array of your LoggingConfiguration objects
  - **Resource types (\*required):** 
  - **Condition keys:** [wafv2:LogScope](#list_wafv2-wafv2_LogScope)
  - **Access level:** List

- **   [ListManagedRuleSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListManagedRuleSets.html)  **
  - **Description:** Grants permission to retrieve an array of your ManagedRuleSet objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMobileSdkReleases](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListMobileSdkReleases.html)  **
  - **Description:** Grants permission to retrieve a list of the available releases for the mobile SDK and the specified device platform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegexPatternSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListRegexPatternSets.html)  **
  - **Description:** Grants permission to retrieve an array of RegexPatternSetSummary objects for the regex pattern sets that you manage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourcesForWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListResourcesForWebACL.html)  **
  - **Description:** Grants permission to retrieve an array of the Amazon Resource Names (ARNs) for the resources that are associated with a web ACL
  - **Resource types (\*required):** [agentcore-gateway](#list_wafv2-resource-agentcore-gateway) / **Condition keys:**  
  - **Resource types (\*required):** [amplify-app](#list_wafv2-resource-amplify-app) / **Condition keys:**  
  - **Resource types (\*required):** [apprunner](#list_wafv2-resource-apprunner) / **Condition keys:**  
  - **Resource types (\*required):** [userpool](#list_wafv2-resource-userpool) / **Condition keys:**  
  - **Resource types (\*required):** [verified-access-instance](#list_wafv2-resource-verified-access-instance) / **Condition keys:**  
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListRuleGroups.html)  **
  - **Description:** Grants permission to retrieve an array of RuleGroupSummary objects for the rule groups that you manage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSettlementRecords](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListSettlementRecords.html)  **
  - **Description:** Grants permission to retrieve a list of monetization settlement records within a specified time window
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [ipset](#list_wafv2-resource-ipset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [regexpatternset](#list_wafv2-resource-regexpatternset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rulegroup](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [webacl](#list_wafv2-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWebACLs](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListWebACLs.html)  **
  - **Description:** Grants permission to retrieve an array of WebACLSummary objects for the web ACLs that you manage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_PutLoggingConfiguration.html)  **
  - **Description:** Grants permission to enable a LoggingConfiguration, to start logging for a web ACL
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[wafv2:LogDestinationResource](#list_wafv2-wafv2_LogDestinationResource)<br />[wafv2:LogScope](#list_wafv2-wafv2_LogScope)
  - **Access level:** Write

- **   [PutManagedRuleSetVersions](https://docs.aws.amazon.com/waf/latest/APIReference/API_PutManagedRuleSetVersions.html)  **
  - **Description:** Grants permission to enable create a new or update an existing version of a ManagedRuleSet
  - **Resource types (\*required):** [managedruleset\*](#list_wafv2-resource-managedruleset) / **Condition keys:**  
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_PutPermissionPolicy.html)  **
  - **Description:** Grants permission to attach an IAM policy to a resource, used to share rule groups between accounts
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [TagResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to associate tags with a AWS resource
  - **Resource types (\*required):** [ipset](#list_wafv2-resource-ipset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [regexpatternset](#list_wafv2-resource-regexpatternset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [webacl](#list_wafv2-resource-webacl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wafv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate tags from an AWS resource
  - **Resource types (\*required):** [ipset](#list_wafv2-resource-ipset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [regexpatternset](#list_wafv2-resource-regexpatternset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Resource types (\*required):** [webacl](#list_wafv2-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wafv2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateIPSet.html)  **
  - **Description:** Grants permission to update an IPSet
  - **Resource types (\*required):** [ipset\*](#list_wafv2-resource-ipset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateManagedRuleSetVersionExpiryDate](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateManagedRuleSetVersionExpiryDate.html)  **
  - **Description:** Grants permission to update the expiry date of a version in ManagedRuleSet
  - **Resource types (\*required):** [managedruleset\*](#list_wafv2-resource-managedruleset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateRegexPatternSet.html)  **
  - **Description:** Grants permission to update a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_wafv2-resource-regexpatternset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateRuleGroup.html)  **
  - **Description:** Grants permission to update a RuleGroup
  - **Resource types (\*required):** [ipset](#list_wafv2-resource-ipset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [regexpatternset](#list_wafv2-resource-regexpatternset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rulegroup\*](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateWebACL.html)  **
  - **Description:** Grants permission to update a WebACL
  - **Resource types (\*required):** [ipset](#list_wafv2-resource-ipset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managedruleset](#list_wafv2-resource-managedruleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [regexpatternset](#list_wafv2-resource-regexpatternset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rulegroup](#list_wafv2-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS WAF V2
<a name="list_wafv2-permission-only-actions"></a>

The following actions are defined by AWS WAF V2 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DisassociateFirewallManager](https://docs.aws.amazon.com/waf/latest/APIReference/API_DisassociateFirewallManager.html)  **
  - **Description:** Grants permission to disassociate Firewall Manager from a WebACL
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFirewallManagerRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_PutFirewallManagerRuleGroups.html)  **
  - **Description:** Grants permission to create FirewallManagedRulesGroups in a WebACL
  - **Resource types (\*required):** [webacl\*](#list_wafv2-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS WAF V2
<a name="list_wafv2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [agentcore-gateway](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:gateway/${GatewayId} |   | 
|  [amplify-app](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:amplify:${Region}:${Account}:apps/${AppId} |   | 
|  [apigateway](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/stages/${StageName} |   | 
|  [apprunner](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:apprunner:${Region}:${Account}:service/${ServiceName}/${ServiceId} |   | 
|  [appsync](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${GraphQLAPIId} |   | 
|  [ipset](https://docs.aws.amazon.com/waf/latest/APIReference/API_IPSet.html)  | arn:${Partition}:wafv2:${Region}:${Account}:${Scope}/ipset/${Name}/${Id} | [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_) | 
|  [loadbalancer/app/](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/app/${LoadBalancerName}/${LoadBalancerId} |   | 
|  [managedruleset](https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleSet.html)  | arn:${Partition}:wafv2:${Region}:${Account}:${Scope}/managedruleset/${Name}/${Id} |   | 
|  [regexpatternset](https://docs.aws.amazon.com/waf/latest/APIReference/API_RegexPatternSet.html)  | arn:${Partition}:wafv2:${Region}:${Account}:${Scope}/regexpatternset/${Name}/${Id} | [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_) | 
|  [rulegroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html)  | arn:${Partition}:wafv2:${Region}:${Account}:${Scope}/rulegroup/${Name}/${Id} | [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_) | 
|  [userpool](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:cognito-idp:${Region}:${Account}:userpool/${UserPoolId} |   | 
|  [verified-access-instance](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:ec2:${Region}:${Account}:verified-access-instance/${VerifiedAccessInstanceId} |   | 
|  [webacl](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html)  | arn:${Partition}:wafv2:${Region}:${Account}:${Scope}/webacl/${Name}/${Id} | [aws:ResourceTag/${TagKey}](#list_wafv2-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS WAF V2
<a name="list_wafv2-policy-keys"></a>

AWS WAF V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 
|   [wafv2:LogDestinationResource](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by log destination ARN for PutLoggingConfiguration API | ARN | 
|   [wafv2:LogScope](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by log scope for Logging Configuration API | String | 