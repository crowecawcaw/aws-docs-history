

# Actions, resources, and condition keys for AWS WAF Regional
<a name="list_waf-regional"></a>

AWS WAF Regional (service prefix: `waf-regional`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.htm).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/waf/latest/APIReference/API_Operations_AWS_WAF_Regional.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/waf-regional/waf-regional.json) for this service.

**Topics**
+ [API operations defined by AWS WAF Regional](#list_waf-regional-operations)
+ [Actions defined by AWS WAF Regional](#list_waf-regional-actions-as-permissions)
+ [Resource types defined by AWS WAF Regional](#list_waf-regional-resources-for-iam-policies)
+ [Condition keys for AWS WAF Regional](#list_waf-regional-policy-keys)

## API operations defined by AWS WAF Regional
<a name="list_waf-regional-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_waf-regional-actions-as-permissions).




- **   AssociateWebACL  **
  - **IAM action:**  [waf-regional:AssociateWebACL](#list_waf-regional-action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:SetWebACL](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [elasticloadbalancing:SetWebAcl](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateByteMatchSet  **
  - **IAM action:**  [waf-regional:CreateByteMatchSet](#list_waf-regional-action-CreateByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGeoMatchSet  **
  - **IAM action:**  [waf-regional:CreateGeoMatchSet](#list_waf-regional-action-CreateGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIPSet  **
  - **IAM action:**  [waf-regional:CreateIPSet](#list_waf-regional-action-CreateIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRateBasedRule  **
  - **IAM action:**  [waf-regional:CreateRateBasedRule](#list_waf-regional-action-CreateRateBasedRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [waf-regional:TagResource](#list_waf-regional-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegexMatchSet  **
  - **IAM action:**  [waf-regional:CreateRegexMatchSet](#list_waf-regional-action-CreateRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRegexPatternSet  **
  - **IAM action:**  [waf-regional:CreateRegexPatternSet](#list_waf-regional-action-CreateRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRule  **
  - **IAM action:**  [waf-regional:CreateRule](#list_waf-regional-action-CreateRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [waf-regional:TagResource](#list_waf-regional-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRuleGroup  **
  - **IAM action:**  [waf-regional:CreateRuleGroup](#list_waf-regional-action-CreateRuleGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [waf-regional:TagResource](#list_waf-regional-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSizeConstraintSet  **
  - **IAM action:**  [waf-regional:CreateSizeConstraintSet](#list_waf-regional-action-CreateSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSqlInjectionMatchSet  **
  - **IAM action:**  [waf-regional:CreateSqlInjectionMatchSet](#list_waf-regional-action-CreateSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWebACL  **
  - **IAM action:**  [waf-regional:CreateWebACL](#list_waf-regional-action-CreateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [waf-regional:TagResource](#list_waf-regional-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWebACLMigrationStack  **
  - **IAM action:**  [waf-regional:CreateWebACLMigrationStack](#list_waf-regional-action-CreateWebACLMigrationStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateXssMatchSet  **
  - **IAM action:**  [waf-regional:CreateXssMatchSet](#list_waf-regional-action-CreateXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteByteMatchSet  **
  - **IAM action:**  [waf-regional:DeleteByteMatchSet](#list_waf-regional-action-DeleteByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGeoMatchSet  **
  - **IAM action:**  [waf-regional:DeleteGeoMatchSet](#list_waf-regional-action-DeleteGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIPSet  **
  - **IAM action:**  [waf-regional:DeleteIPSet](#list_waf-regional-action-DeleteIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoggingConfiguration  **
  - **IAM action:**  [waf-regional:DeleteLoggingConfiguration](#list_waf-regional-action-DeleteLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePermissionPolicy  **
  - **IAM action:**  [waf-regional:DeletePermissionPolicy](#list_waf-regional-action-DeletePermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteRateBasedRule  **
  - **IAM action:**  [waf-regional:DeleteRateBasedRule](#list_waf-regional-action-DeleteRateBasedRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegexMatchSet  **
  - **IAM action:**  [waf-regional:DeleteRegexMatchSet](#list_waf-regional-action-DeleteRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegexPatternSet  **
  - **IAM action:**  [waf-regional:DeleteRegexPatternSet](#list_waf-regional-action-DeleteRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **IAM action:**  [waf-regional:DeleteRule](#list_waf-regional-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRuleGroup  **
  - **IAM action:**  [waf-regional:DeleteRuleGroup](#list_waf-regional-action-DeleteRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSizeConstraintSet  **
  - **IAM action:**  [waf-regional:DeleteSizeConstraintSet](#list_waf-regional-action-DeleteSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSqlInjectionMatchSet  **
  - **IAM action:**  [waf-regional:DeleteSqlInjectionMatchSet](#list_waf-regional-action-DeleteSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebACL  **
  - **IAM action:**  [waf-regional:DeleteWebACL](#list_waf-regional-action-DeleteWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteXssMatchSet  **
  - **IAM action:**  [waf-regional:DeleteXssMatchSet](#list_waf-regional-action-DeleteXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWebACL  **
  - **IAM action:**  [apigateway:SetWebACL](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [elasticloadbalancing:SetWebAcl](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetByteMatchSet  **
  - **IAM action:**  [waf-regional:GetByteMatchSet](#list_waf-regional-action-GetByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChangeToken  **
  - **IAM action:**  [waf-regional:GetChangeToken](#list_waf-regional-action-GetChangeToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChangeTokenStatus  **
  - **IAM action:**  [waf-regional:GetChangeTokenStatus](#list_waf-regional-action-GetChangeTokenStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGeoMatchSet  **
  - **IAM action:**  [waf-regional:GetGeoMatchSet](#list_waf-regional-action-GetGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIPSet  **
  - **IAM action:**  [waf-regional:GetIPSet](#list_waf-regional-action-GetIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoggingConfiguration  **
  - **IAM action:**  [waf-regional:GetLoggingConfiguration](#list_waf-regional-action-GetLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPermissionPolicy  **
  - **IAM action:**  [waf-regional:GetPermissionPolicy](#list_waf-regional-action-GetPermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRateBasedRule  **
  - **IAM action:**  [waf-regional:GetRateBasedRule](#list_waf-regional-action-GetRateBasedRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRateBasedRuleManagedKeys  **
  - **IAM action:**  [waf-regional:GetRateBasedRuleManagedKeys](#list_waf-regional-action-GetRateBasedRuleManagedKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegexMatchSet  **
  - **IAM action:**  [waf-regional:GetRegexMatchSet](#list_waf-regional-action-GetRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegexPatternSet  **
  - **IAM action:**  [waf-regional:GetRegexPatternSet](#list_waf-regional-action-GetRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRule  **
  - **IAM action:**  [waf-regional:GetRule](#list_waf-regional-action-GetRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRuleGroup  **
  - **IAM action:**  [waf-regional:GetRuleGroup](#list_waf-regional-action-GetRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSampledRequests  **
  - **IAM action:**  [waf-regional:GetSampledRequests](#list_waf-regional-action-GetSampledRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSizeConstraintSet  **
  - **IAM action:**  [waf-regional:GetSizeConstraintSet](#list_waf-regional-action-GetSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSqlInjectionMatchSet  **
  - **IAM action:**  [waf-regional:GetSqlInjectionMatchSet](#list_waf-regional-action-GetSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebACL  **
  - **IAM action:**  [waf-regional:GetWebACL](#list_waf-regional-action-GetWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebACLForResource  **
  - **IAM action:**  [waf-regional:GetWebACLForResource](#list_waf-regional-action-GetWebACLForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetXssMatchSet  **
  - **IAM action:**  [waf-regional:GetXssMatchSet](#list_waf-regional-action-GetXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActivatedRulesInRuleGroup  **
  - **IAM action:**  [waf-regional:ListActivatedRulesInRuleGroup](#list_waf-regional-action-ListActivatedRulesInRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListByteMatchSets  **
  - **IAM action:**  [waf-regional:ListByteMatchSets](#list_waf-regional-action-ListByteMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGeoMatchSets  **
  - **IAM action:**  [waf-regional:ListGeoMatchSets](#list_waf-regional-action-ListGeoMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIPSets  **
  - **IAM action:**  [waf-regional:ListIPSets](#list_waf-regional-action-ListIPSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLoggingConfigurations  **
  - **IAM action:**  [waf-regional:ListLoggingConfigurations](#list_waf-regional-action-ListLoggingConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRateBasedRules  **
  - **IAM action:**  [waf-regional:ListRateBasedRules](#list_waf-regional-action-ListRateBasedRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegexMatchSets  **
  - **IAM action:**  [waf-regional:ListRegexMatchSets](#list_waf-regional-action-ListRegexMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegexPatternSets  **
  - **IAM action:**  [waf-regional:ListRegexPatternSets](#list_waf-regional-action-ListRegexPatternSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourcesForWebACL  **
  - **IAM action:**  [waf-regional:ListResourcesForWebACL](#list_waf-regional-action-ListResourcesForWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleGroups  **
  - **IAM action:**  [waf-regional:ListRuleGroups](#list_waf-regional-action-ListRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRules  **
  - **IAM action:**  [waf-regional:ListRules](#list_waf-regional-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSizeConstraintSets  **
  - **IAM action:**  [waf-regional:ListSizeConstraintSets](#list_waf-regional-action-ListSizeConstraintSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSqlInjectionMatchSets  **
  - **IAM action:**  [waf-regional:ListSqlInjectionMatchSets](#list_waf-regional-action-ListSqlInjectionMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscribedRuleGroups  **
  - **IAM action:**  [waf-regional:ListSubscribedRuleGroups](#list_waf-regional-action-ListSubscribedRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [waf-regional:ListTagsForResource](#list_waf-regional-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWebACLs  **
  - **IAM action:**  [waf-regional:ListWebACLs](#list_waf-regional-action-ListWebACLs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListXssMatchSets  **
  - **IAM action:**  [waf-regional:ListXssMatchSets](#list_waf-regional-action-ListXssMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutLoggingConfiguration  **
  - **IAM action:**  [waf-regional:PutLoggingConfiguration](#list_waf-regional-action-PutLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPermissionPolicy  **
  - **IAM action:**  [waf-regional:PutPermissionPolicy](#list_waf-regional-action-PutPermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   TagResource  **
  - **IAM action:**  [waf-regional:TagResource](#list_waf-regional-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [waf-regional:UntagResource](#list_waf-regional-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateByteMatchSet  **
  - **IAM action:**  [waf-regional:UpdateByteMatchSet](#list_waf-regional-action-UpdateByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGeoMatchSet  **
  - **IAM action:**  [waf-regional:UpdateGeoMatchSet](#list_waf-regional-action-UpdateGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIPSet  **
  - **IAM action:**  [waf-regional:UpdateIPSet](#list_waf-regional-action-UpdateIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRateBasedRule  **
  - **IAM action:**  [waf-regional:UpdateRateBasedRule](#list_waf-regional-action-UpdateRateBasedRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegexMatchSet  **
  - **IAM action:**  [waf-regional:UpdateRegexMatchSet](#list_waf-regional-action-UpdateRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegexPatternSet  **
  - **IAM action:**  [waf-regional:UpdateRegexPatternSet](#list_waf-regional-action-UpdateRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRule  **
  - **IAM action:**  [waf-regional:UpdateRule](#list_waf-regional-action-UpdateRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuleGroup  **
  - **IAM action:**  [waf-regional:UpdateRuleGroup](#list_waf-regional-action-UpdateRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSizeConstraintSet  **
  - **IAM action:**  [waf-regional:UpdateSizeConstraintSet](#list_waf-regional-action-UpdateSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSqlInjectionMatchSet  **
  - **IAM action:**  [waf-regional:UpdateSqlInjectionMatchSet](#list_waf-regional-action-UpdateSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWebACL  **
  - **IAM action:**  [waf-regional:UpdateWebACL](#list_waf-regional-action-UpdateWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateXssMatchSet  **
  - **IAM action:**  [waf-regional:UpdateXssMatchSet](#list_waf-regional-action-UpdateXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS WAF Regional
<a name="list_waf-regional-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_AssociateWebACL.html)  **
  - **Description:** Grants permission to associate a web ACL with a resource
  - **Resource types (\*required):** [loadbalancer/app/\*](#list_waf-regional-resource-loadbalancer_app_) / **Condition keys:**  
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateByteMatchSet.html)  **
  - **Description:** Grants permission to create a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-regional-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateGeoMatchSet.html)  **
  - **Description:** Grants permission to create a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-regional-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateIPSet.html)  **
  - **Description:** Grants permission to create an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-regional-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateRateBasedRule.html)  **
  - **Description:** Grants permission to create a RateBasedRule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-regional-resource-ratebasedrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateRegexMatchSet.html)  **
  - **Description:** Grants permission to create a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-regional-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateRegexPatternSet.html)  **
  - **Description:** Grants permission to create a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-regional-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateRule.html)  **
  - **Description:** Grants permission to create a Rule
  - **Resource types (\*required):** [rule\*](#list_waf-regional-resource-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateRuleGroup.html)  **
  - **Description:** Grants permission to create a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-regional-resource-rulegroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateSizeConstraintSet.html)  **
  - **Description:** Grants permission to create a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-regional-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to create an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-regional-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateWebACL.html)  **
  - **Description:** Grants permission to create a WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [CreateWebACLMigrationStack](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateWebACLMigrationStack.html)  **
  - **Description:** Grants permission to create a CloudFormation web ACL template in an S3 bucket for the purposes of migrating the web ACL from AWS WAF Classic to AWS WAF v2
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_CreateXssMatchSet.html)  **
  - **Description:** Grants permission to create an XssMatchSet
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-regional-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteByteMatchSet.html)  **
  - **Description:** Grants permission to delete a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-regional-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteGeoMatchSet.html)  **
  - **Description:** Grants permission to delete a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-regional-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteIPSet.html)  **
  - **Description:** Grants permission to delete an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-regional-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete a LoggingConfiguration from a web ACL
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeletePermissionPolicy.html)  **
  - **Description:** Grants permission to delete an IAM policy from a rule group
  - **Resource types (\*required):** [rulegroup\*](#list_waf-regional-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteRateBasedRule.html)  **
  - **Description:** Grants permission to delete a RateBasedRule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-regional-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteRegexMatchSet.html)  **
  - **Description:** Grants permission to delete a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-regional-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteRegexPatternSet.html)  **
  - **Description:** Grants permission to delete a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-regional-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteRule.html)  **
  - **Description:** Grants permission to delete a Rule
  - **Resource types (\*required):** [rule\*](#list_waf-regional-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteRuleGroup.html)  **
  - **Description:** Grants permission to delete a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-regional-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteSizeConstraintSet.html)  **
  - **Description:** Grants permission to delete a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-regional-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to delete an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-regional-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteWebACL.html)  **
  - **Description:** Grants permission to delete a WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DeleteXssMatchSet.html)  **
  - **Description:** Grants permission to delete an XssMatchSet
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-regional-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_DisassociateWebACL.html)  **
  - **Description:** Grants permission to delete an association between a web ACL and a resource
  - **Resource types (\*required):** [loadbalancer/app/\*](#list_waf-regional-resource-loadbalancer_app_)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetByteMatchSet.html)  **
  - **Description:** Grants permission to retrieve a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-regional-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChangeToken](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetChangeToken.html)  **
  - **Description:** Grants permission to retrieve a change token to use in create, update, and delete requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChangeTokenStatus](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetChangeTokenStatus.html)  **
  - **Description:** Grants permission to retrieve the status of a change token
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetGeoMatchSet.html)  **
  - **Description:** Grants permission to retrieve a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-regional-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetIPSet.html)  **
  - **Description:** Grants permission to retrieve an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-regional-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetLoggingConfiguration.html)  **
  - **Description:** Grants permission to retrieve a LoggingConfiguration
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetPermissionPolicy.html)  **
  - **Description:** Grants permission to retrieve an IAM policy attached to a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-regional-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRateBasedRule.html)  **
  - **Description:** Grants permission to retrieve a RateBasedRule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-regional-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRateBasedRuleManagedKeys](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRateBasedRuleManagedKeys.html)  **
  - **Description:** Grants permission to retrieve the array of IP addresses that are currently being blocked by a RateBasedRule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-regional-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRegexMatchSet.html)  **
  - **Description:** Grants permission to retrieve a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-regional-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRegexPatternSet.html)  **
  - **Description:** Grants permission to retrieve a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-regional-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRule.html)  **
  - **Description:** Grants permission to retrieve a Rule
  - **Resource types (\*required):** [rule\*](#list_waf-regional-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRuleGroup.html)  **
  - **Description:** Grants permission to retrieve a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-regional-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSampledRequests](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetSampledRequests.html)  **
  - **Description:** Grants permission to retrieve detailed information for a sample set of web requests
  - **Resource types (\*required):** [webacl](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetSizeConstraintSet.html)  **
  - **Description:** Grants permission to retrieve a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-regional-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to retrieve an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-regional-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetWebACL.html)  **
  - **Description:** Grants permission to retrieve a WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWebACLForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetWebACLForResource.html)  **
  - **Description:** Grants permission to retrieve a WebACL that's associated with a specified resource
  - **Resource types (\*required):** [loadbalancer/app/\*](#list_waf-regional-resource-loadbalancer_app_)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetXssMatchSet.html)  **
  - **Description:** Grants permission to retrieve an XssMatchSet
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-regional-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListActivatedRulesInRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListActivatedRulesInRuleGroup.html)  **
  - **Description:** Grants permission to retrieve an array of ActivatedRule objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListByteMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListByteMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of ByteMatchSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGeoMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListGeoMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of GeoMatchSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIPSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListIPSets.html)  **
  - **Description:** Grants permission to retrieve an array of IPSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLoggingConfigurations](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListLoggingConfigurations.html)  **
  - **Description:** Grants permission to retrieve an array of LoggingConfiguration objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRateBasedRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRateBasedRules.html)  **
  - **Description:** Grants permission to retrieve an array of RuleSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegexMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRegexMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of RegexMatchSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegexPatternSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRegexPatternSets.html)  **
  - **Description:** Grants permission to retrieve an array of RegexPatternSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourcesForWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListResourcesForWebACL.html)  **
  - **Description:** Grants permission to retrieve an array of resources associated with a specified WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRuleGroups.html)  **
  - **Description:** Grants permission to retrieve an array of RuleGroup objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRules.html)  **
  - **Description:** Grants permission to retrieve an array of RuleSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSizeConstraintSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListSizeConstraintSets.html)  **
  - **Description:** Grants permission to retrieve an array of SizeConstraintSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSqlInjectionMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListSqlInjectionMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of SqlInjectionMatchSet objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscribedRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListSubscribedRuleGroups.html)  **
  - **Description:** Grants permission to retrieve an array of RuleGroup objects that you are subscribed to
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists the Tags for a resource
  - **Resource types (\*required):** [ratebasedrule](#list_waf-regional-resource-ratebasedrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rule](#list_waf-regional-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rulegroup](#list_waf-regional-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [webacl](#list_waf-regional-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWebACLs](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListWebACLs.html)  **
  - **Description:** Grants permission to retrieve an array of WebACLSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListXssMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListXssMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of XssMatchSet objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_PutLoggingConfiguration.html)  **
  - **Description:** Grants permission to associates a LoggingConfiguration with a web ACL
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_PutPermissionPolicy.html)  **
  - **Description:** Grants permission to attach an IAM policy to a specified rule group, to support rule group sharing between accounts
  - **Resource types (\*required):** [rulegroup\*](#list_waf-regional-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [TagResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_TagResource.html)  **
  - **Description:** Grants permission to add a Tag to a resource
  - **Resource types (\*required):** [ratebasedrule](#list_waf-regional-resource-ratebasedrule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_waf-regional-resource-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup](#list_waf-regional-resource-rulegroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Resource types (\*required):** [webacl](#list_waf-regional-resource-webacl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-regional-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UntagResource.html)  **
  - **Description:** Grants permission to remove a Tag from a resource
  - **Resource types (\*required):** [ratebasedrule](#list_waf-regional-resource-ratebasedrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_waf-regional-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup](#list_waf-regional-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Resource types (\*required):** [webacl](#list_waf-regional-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-regional-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateByteMatchSet.html)  **
  - **Description:** Grants permission to insert or delete ByteMatchTuple objects in a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-regional-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateGeoMatchSet.html)  **
  - **Description:** Grants permission to insert or delete GeoMatchConstraint objects in a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-regional-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateIPSet.html)  **
  - **Description:** Grants permission to insert or delete IPSetDescriptor objects in an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-regional-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateRateBasedRule.html)  **
  - **Description:** Grants permission to insert or delete predicate objects in a rate based rule and update the RateLimit in the rule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-regional-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateRegexMatchSet.html)  **
  - **Description:** Grants permission to insert or delete RegexMatchTuple objects in a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-regional-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateRegexPatternSet.html)  **
  - **Description:** Grants permission to insert or delete RegexPatternStrings in a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-regional-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateRule.html)  **
  - **Description:** Grants permission to insert or delete predicate objects in a Rule
  - **Resource types (\*required):** [rule\*](#list_waf-regional-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateRuleGroup.html)  **
  - **Description:** Grants permission to insert or delete ActivatedRule objects in a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-regional-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateSizeConstraintSet.html)  **
  - **Description:** Grants permission to insert or delete SizeConstraint objects in a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-regional-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to insert or delete SqlInjectionMatchTuple objects in an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-regional-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateWebACL.html)  **
  - **Description:** Grants permission to insert or delete ActivatedRule objects in a WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-regional-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateXssMatchSet.html)  **
  - **Description:** Grants permission to insert or delete XssMatchTuple objects in an XssMatchSet
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-regional-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS WAF Regional
<a name="list_waf-regional-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [bytematchset](${ActionsDocRoot}API_wafRegional_ByteMatchSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:bytematchset/${Id} |   | 
|  [geomatchset](${ActionsDocRoot}API_wafRegional_GeoMatchSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:geomatchset/${Id} |   | 
|  [ipset](${ActionsDocRoot}API_wafRegional_IPSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:ipset/${Id} |   | 
|  [loadbalancer/app/](${ActionsDocRoot}API_wafRegional_WebACL.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/app/${LoadBalancerName}/${LoadBalancerId} |   | 
|  [ratebasedrule](${ActionsDocRoot}API_wafRegional_RateBasedRule.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:ratebasedrule/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_) | 
|  [regexmatchset](${ActionsDocRoot}API_wafRegional_RegexMatchSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:regexmatch/${Id} |   | 
|  [regexpatternset](${ActionsDocRoot}API_wafRegional_RegexPatternSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:regexpatternset/${Id} |   | 
|  [rule](${ActionsDocRoot}API_wafRegional_Rule.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:rule/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_) | 
|  [rulegroup](${ActionsDocRoot}API_wafRegional_RuleGroup.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:rulegroup/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_) | 
|  [sizeconstraintset](${ActionsDocRoot}API_wafRegional_SizeConstraintSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:sizeconstraintset/${Id} |   | 
|  [sqlinjectionmatchset](${ActionsDocRoot}API_wafRegional_SqlInjectionMatchSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:sqlinjectionset/${Id} |   | 
|  [webacl](${ActionsDocRoot}API_wafRegional_WebACL.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:webacl/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-regional-aws_ResourceTag___TagKey_) | 
|  [xssmatchset](${ActionsDocRoot}API_wafRegional_XssMatchSet.html)  | arn:${Partition}:waf-regional:${Region}:${Account}:xssmatchset/${Id} |   | 

## Condition keys for AWS WAF Regional
<a name="list_waf-regional-policy-keys"></a>

AWS WAF Regional defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag-value assoicated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of mandatory tags in the request | ArrayOfString | 