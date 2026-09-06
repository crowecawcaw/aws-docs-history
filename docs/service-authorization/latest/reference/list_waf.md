

# Actions, resources, and condition keys for AWS WAF
<a name="list_waf"></a>

AWS WAF (service prefix: `waf`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/waf/latest/APIReference/API_Operations_AWS_WAF.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/waf/waf.json) for this service.

**Topics**
+ [API operations defined by AWS WAF](#list_waf-operations)
+ [Actions defined by AWS WAF](#list_waf-actions-as-permissions)
+ [Resource types defined by AWS WAF](#list_waf-resources-for-iam-policies)
+ [Condition keys for AWS WAF](#list_waf-policy-keys)

## API operations defined by AWS WAF
<a name="list_waf-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_waf-actions-as-permissions).




- **   CreateByteMatchSet  **
  - **IAM action:**  [waf:CreateByteMatchSet](#list_waf-action-CreateByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGeoMatchSet  **
  - **IAM action:**  [waf:CreateGeoMatchSet](#list_waf-action-CreateGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIPSet  **
  - **IAM action:**  [waf:CreateIPSet](#list_waf-action-CreateIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRateBasedRule  **
  - **IAM action:**  [waf:CreateRateBasedRule](#list_waf-action-CreateRateBasedRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [waf:TagResource](#list_waf-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegexMatchSet  **
  - **IAM action:**  [waf:CreateRegexMatchSet](#list_waf-action-CreateRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRegexPatternSet  **
  - **IAM action:**  [waf:CreateRegexPatternSet](#list_waf-action-CreateRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRule  **
  - **IAM action:**  [waf:CreateRule](#list_waf-action-CreateRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [waf:TagResource](#list_waf-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRuleGroup  **
  - **IAM action:**  [waf:CreateRuleGroup](#list_waf-action-CreateRuleGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [waf:TagResource](#list_waf-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSizeConstraintSet  **
  - **IAM action:**  [waf:CreateSizeConstraintSet](#list_waf-action-CreateSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSqlInjectionMatchSet  **
  - **IAM action:**  [waf:CreateSqlInjectionMatchSet](#list_waf-action-CreateSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWebACL  **
  - **IAM action:**  [waf:CreateWebACL](#list_waf-action-CreateWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [waf:TagResource](#list_waf-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWebACLMigrationStack  **
  - **IAM action:**  [waf:CreateWebACLMigrationStack](#list_waf-action-CreateWebACLMigrationStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateXssMatchSet  **
  - **IAM action:**  [waf:CreateXssMatchSet](#list_waf-action-CreateXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteByteMatchSet  **
  - **IAM action:**  [waf:DeleteByteMatchSet](#list_waf-action-DeleteByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGeoMatchSet  **
  - **IAM action:**  [waf:DeleteGeoMatchSet](#list_waf-action-DeleteGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIPSet  **
  - **IAM action:**  [waf:DeleteIPSet](#list_waf-action-DeleteIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoggingConfiguration  **
  - **IAM action:**  [waf:DeleteLoggingConfiguration](#list_waf-action-DeleteLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePermissionPolicy  **
  - **IAM action:**  [waf:DeletePermissionPolicy](#list_waf-action-DeletePermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteRateBasedRule  **
  - **IAM action:**  [waf:DeleteRateBasedRule](#list_waf-action-DeleteRateBasedRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegexMatchSet  **
  - **IAM action:**  [waf:DeleteRegexMatchSet](#list_waf-action-DeleteRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegexPatternSet  **
  - **IAM action:**  [waf:DeleteRegexPatternSet](#list_waf-action-DeleteRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **IAM action:**  [waf:DeleteRule](#list_waf-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRuleGroup  **
  - **IAM action:**  [waf:DeleteRuleGroup](#list_waf-action-DeleteRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSizeConstraintSet  **
  - **IAM action:**  [waf:DeleteSizeConstraintSet](#list_waf-action-DeleteSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSqlInjectionMatchSet  **
  - **IAM action:**  [waf:DeleteSqlInjectionMatchSet](#list_waf-action-DeleteSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebACL  **
  - **IAM action:**  [waf:DeleteWebACL](#list_waf-action-DeleteWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteXssMatchSet  **
  - **IAM action:**  [waf:DeleteXssMatchSet](#list_waf-action-DeleteXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetByteMatchSet  **
  - **IAM action:**  [waf:GetByteMatchSet](#list_waf-action-GetByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChangeToken  **
  - **IAM action:**  [waf:GetChangeToken](#list_waf-action-GetChangeToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChangeTokenStatus  **
  - **IAM action:**  [waf:GetChangeTokenStatus](#list_waf-action-GetChangeTokenStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGeoMatchSet  **
  - **IAM action:**  [waf:GetGeoMatchSet](#list_waf-action-GetGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIPSet  **
  - **IAM action:**  [waf:GetIPSet](#list_waf-action-GetIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoggingConfiguration  **
  - **IAM action:**  [waf:GetLoggingConfiguration](#list_waf-action-GetLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPermissionPolicy  **
  - **IAM action:**  [waf:GetPermissionPolicy](#list_waf-action-GetPermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRateBasedRule  **
  - **IAM action:**  [waf:GetRateBasedRule](#list_waf-action-GetRateBasedRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRateBasedRuleManagedKeys  **
  - **IAM action:**  [waf:GetRateBasedRuleManagedKeys](#list_waf-action-GetRateBasedRuleManagedKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegexMatchSet  **
  - **IAM action:**  [waf:GetRegexMatchSet](#list_waf-action-GetRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegexPatternSet  **
  - **IAM action:**  [waf:GetRegexPatternSet](#list_waf-action-GetRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRule  **
  - **IAM action:**  [waf:GetRule](#list_waf-action-GetRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRuleGroup  **
  - **IAM action:**  [waf:GetRuleGroup](#list_waf-action-GetRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSampledRequests  **
  - **IAM action:**  [waf:GetSampledRequests](#list_waf-action-GetSampledRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSizeConstraintSet  **
  - **IAM action:**  [waf:GetSizeConstraintSet](#list_waf-action-GetSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSqlInjectionMatchSet  **
  - **IAM action:**  [waf:GetSqlInjectionMatchSet](#list_waf-action-GetSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebACL  **
  - **IAM action:**  [waf:GetWebACL](#list_waf-action-GetWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetXssMatchSet  **
  - **IAM action:**  [waf:GetXssMatchSet](#list_waf-action-GetXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActivatedRulesInRuleGroup  **
  - **IAM action:**  [waf:ListActivatedRulesInRuleGroup](#list_waf-action-ListActivatedRulesInRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListByteMatchSets  **
  - **IAM action:**  [waf:ListByteMatchSets](#list_waf-action-ListByteMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGeoMatchSets  **
  - **IAM action:**  [waf:ListGeoMatchSets](#list_waf-action-ListGeoMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIPSets  **
  - **IAM action:**  [waf:ListIPSets](#list_waf-action-ListIPSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLoggingConfigurations  **
  - **IAM action:**  [waf:ListLoggingConfigurations](#list_waf-action-ListLoggingConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRateBasedRules  **
  - **IAM action:**  [waf:ListRateBasedRules](#list_waf-action-ListRateBasedRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegexMatchSets  **
  - **IAM action:**  [waf:ListRegexMatchSets](#list_waf-action-ListRegexMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegexPatternSets  **
  - **IAM action:**  [waf:ListRegexPatternSets](#list_waf-action-ListRegexPatternSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleGroups  **
  - **IAM action:**  [waf:ListRuleGroups](#list_waf-action-ListRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRules  **
  - **IAM action:**  [waf:ListRules](#list_waf-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSizeConstraintSets  **
  - **IAM action:**  [waf:ListSizeConstraintSets](#list_waf-action-ListSizeConstraintSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSqlInjectionMatchSets  **
  - **IAM action:**  [waf:ListSqlInjectionMatchSets](#list_waf-action-ListSqlInjectionMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscribedRuleGroups  **
  - **IAM action:**  [waf:ListSubscribedRuleGroups](#list_waf-action-ListSubscribedRuleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [waf:ListTagsForResource](#list_waf-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWebACLs  **
  - **IAM action:**  [waf:ListWebACLs](#list_waf-action-ListWebACLs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListXssMatchSets  **
  - **IAM action:**  [waf:ListXssMatchSets](#list_waf-action-ListXssMatchSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutLoggingConfiguration  **
  - **IAM action:**  [waf:PutLoggingConfiguration](#list_waf-action-PutLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPermissionPolicy  **
  - **IAM action:**  [waf:PutPermissionPolicy](#list_waf-action-PutPermissionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   TagResource  **
  - **IAM action:**  [waf:TagResource](#list_waf-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [waf:UntagResource](#list_waf-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateByteMatchSet  **
  - **IAM action:**  [waf:UpdateByteMatchSet](#list_waf-action-UpdateByteMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGeoMatchSet  **
  - **IAM action:**  [waf:UpdateGeoMatchSet](#list_waf-action-UpdateGeoMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIPSet  **
  - **IAM action:**  [waf:UpdateIPSet](#list_waf-action-UpdateIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRateBasedRule  **
  - **IAM action:**  [waf:UpdateRateBasedRule](#list_waf-action-UpdateRateBasedRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegexMatchSet  **
  - **IAM action:**  [waf:UpdateRegexMatchSet](#list_waf-action-UpdateRegexMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegexPatternSet  **
  - **IAM action:**  [waf:UpdateRegexPatternSet](#list_waf-action-UpdateRegexPatternSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRule  **
  - **IAM action:**  [waf:UpdateRule](#list_waf-action-UpdateRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuleGroup  **
  - **IAM action:**  [waf:UpdateRuleGroup](#list_waf-action-UpdateRuleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSizeConstraintSet  **
  - **IAM action:**  [waf:UpdateSizeConstraintSet](#list_waf-action-UpdateSizeConstraintSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSqlInjectionMatchSet  **
  - **IAM action:**  [waf:UpdateSqlInjectionMatchSet](#list_waf-action-UpdateSqlInjectionMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWebACL  **
  - **IAM action:**  [waf:UpdateWebACL](#list_waf-action-UpdateWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateXssMatchSet  **
  - **IAM action:**  [waf:UpdateXssMatchSet](#list_waf-action-UpdateXssMatchSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS WAF
<a name="list_waf-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateByteMatchSet.html)  **
  - **Description:** Grants permission to create a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateGeoMatchSet.html)  **
  - **Description:** Grants permission to create a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateIPSet.html)  **
  - **Description:** Grants permission to create an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateRateBasedRule.html)  **
  - **Description:** Grants permission to create a RateBasedRule for limiting the volume of requests from a single IP address
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-resource-ratebasedrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateRegexMatchSet.html)  **
  - **Description:** Grants permission to create a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateRegexPatternSet.html)  **
  - **Description:** Grants permission to create a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateRule.html)  **
  - **Description:** Grants permission to create a Rule for filtering web requests
  - **Resource types (\*required):** [rule\*](#list_waf-resource-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateRuleGroup.html)  **
  - **Description:** Grants permission to create a RuleGroup, which is a collection of predefined rules that you can use in a WebACL
  - **Resource types (\*required):** [rulegroup\*](#list_waf-resource-rulegroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateSizeConstraintSet.html)  **
  - **Description:** Grants permission to create a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to create an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateWebACL.html)  **
  - **Description:** Grants permission to create a WebACL, which contains rules for filtering web requests
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [CreateWebACLMigrationStack](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateWebACLMigrationStack.html)  **
  - **Description:** Grants permission to create a CloudFormation web ACL template in an S3 bucket for the purposes of migrating the web ACL from AWS WAF Classic to AWS WAF v2
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateXssMatchSet.html)  **
  - **Description:** Grants permission to create an XssMatchSet, which you use to detect requests that contain cross-site scripting attacks
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteByteMatchSet.html)  **
  - **Description:** Grants permission to delete a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteGeoMatchSet.html)  **
  - **Description:** Grants permission to delete a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteIPSet.html)  **
  - **Description:** Grants permission to delete an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete the LoggingConfiguration from a web ACL
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeletePermissionPolicy.html)  **
  - **Description:** Grants permission to delete an IAM policy from a rule group
  - **Resource types (\*required):** [rulegroup\*](#list_waf-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteRateBasedRule.html)  **
  - **Description:** Grants permission to delete a RateBasedRule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteRegexMatchSet.html)  **
  - **Description:** Grants permission to delete a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteRegexPatternSet.html)  **
  - **Description:** Grants permission to delete a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteRule.html)  **
  - **Description:** Grants permission to delete a Rule
  - **Resource types (\*required):** [rule\*](#list_waf-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteRuleGroup.html)  **
  - **Description:** Grants permission to delete a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteSizeConstraintSet.html)  **
  - **Description:** Grants permission to delete a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to delete an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteWebACL.html)  **
  - **Description:** Grants permission to delete a WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_DeleteXssMatchSet.html)  **
  - **Description:** Grants permission to delete an XssMatchSet
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetByteMatchSet.html)  **
  - **Description:** Grants permission to retrieve a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChangeToken](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetChangeToken.html)  **
  - **Description:** Grants permission to retrieve a change token to use in create, update, and delete requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChangeTokenStatus](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetChangeTokenStatus.html)  **
  - **Description:** Grants permission to retrieve the status of a change token
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetGeoMatchSet.html)  **
  - **Description:** Grants permission to retrieve a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetIPSet.html)  **
  - **Description:** Grants permission to retrieve an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetLoggingConfiguration.html)  **
  - **Description:** Grants permission to retrieve a LoggingConfiguration for a web ACL
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetPermissionPolicy.html)  **
  - **Description:** Grants permission to retrieve an IAM policy for a rule group
  - **Resource types (\*required):** [rulegroup\*](#list_waf-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRateBasedRule.html)  **
  - **Description:** Grants permission to retrieve a RateBasedRule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRateBasedRuleManagedKeys](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRateBasedRuleManagedKeys.html)  **
  - **Description:** Grants permission to retrieve the array of IP addresses that are currently being blocked by a RateBasedRule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRegexMatchSet.html)  **
  - **Description:** Grants permission to retrieve a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRegexPatternSet.html)  **
  - **Description:** Grants permission to retrieve a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRule.html)  **
  - **Description:** Grants permission to retrieve a Rule
  - **Resource types (\*required):** [rule\*](#list_waf-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRuleGroup.html)  **
  - **Description:** Grants permission to retrieve a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSampledRequests](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSampledRequests.html)  **
  - **Description:** Grants permission to retrieve detailed information about a sample set of web requests
  - **Resource types (\*required):** [webacl](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSizeConstraintSet.html)  **
  - **Description:** Grants permission to retrieve a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to retrieve an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetWebACL.html)  **
  - **Description:** Grants permission to retrieve a WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetXssMatchSet.html)  **
  - **Description:** Grants permission to retrieve an XssMatchSet
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListActivatedRulesInRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListActivatedRulesInRuleGroup.html)  **
  - **Description:** Grants permission to retrieve an array of ActivatedRule objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListByteMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListByteMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of ByteMatchSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGeoMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListGeoMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of GeoMatchSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIPSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListIPSets.html)  **
  - **Description:** Grants permission to retrieve an array of IPSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLoggingConfigurations](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListLoggingConfigurations.html)  **
  - **Description:** Grants permission to retrieve an array of LoggingConfiguration objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRateBasedRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRateBasedRules.html)  **
  - **Description:** Grants permission to retrieve an array of RuleSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegexMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRegexMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of RegexMatchSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegexPatternSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRegexPatternSets.html)  **
  - **Description:** Grants permission to retrieve an array of RegexPatternSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRuleGroups.html)  **
  - **Description:** Grants permission to retrieve an array of RuleGroup objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRules.html)  **
  - **Description:** Grants permission to retrieve an array of RuleSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSizeConstraintSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSizeConstraintSets.html)  **
  - **Description:** Grants permission to retrieve an array of SizeConstraintSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSqlInjectionMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSqlInjectionMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of SqlInjectionMatchSet objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscribedRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSubscribedRuleGroups.html)  **
  - **Description:** Grants permission to retrieve an array of RuleGroup objects that you are subscribed to
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve the tags for a resource
  - **Resource types (\*required):** [ratebasedrule](#list_waf-resource-ratebasedrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rule](#list_waf-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rulegroup](#list_waf-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [webacl](#list_waf-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWebACLs](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListWebACLs.html)  **
  - **Description:** Grants permission to retrieve an array of WebACLSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListXssMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListXssMatchSets.html)  **
  - **Description:** Grants permission to retrieve an array of XssMatchSet objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_PutLoggingConfiguration.html)  **
  - **Description:** Grants permission to associate a LoggingConfiguration with a specified web ACL
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_PutPermissionPolicy.html)  **
  - **Description:** Grants permission to attach an IAM policy to a rule group, to share the rule group between accounts
  - **Resource types (\*required):** [rulegroup\*](#list_waf-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [TagResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_TagResource.html)  **
  - **Description:** Grants permission to add a Tag to a resource
  - **Resource types (\*required):** [ratebasedrule](#list_waf-resource-ratebasedrule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_waf-resource-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup](#list_waf-resource-rulegroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Resource types (\*required):** [webacl](#list_waf-resource-webacl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_waf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UntagResource.html)  **
  - **Description:** Grants permission to remove a Tag from a resource
  - **Resource types (\*required):** [ratebasedrule](#list_waf-resource-ratebasedrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_waf-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Resource types (\*required):** [rulegroup](#list_waf-resource-rulegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Resource types (\*required):** [webacl](#list_waf-resource-webacl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_waf-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateByteMatchSet.html)  **
  - **Description:** Grants permission to insert or delete ByteMatchTuple objects in a ByteMatchSet
  - **Resource types (\*required):** [bytematchset\*](#list_waf-resource-bytematchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateGeoMatchSet.html)  **
  - **Description:** Grants permission to insert or delete GeoMatchConstraint objects in a GeoMatchSet
  - **Resource types (\*required):** [geomatchset\*](#list_waf-resource-geomatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateIPSet.html)  **
  - **Description:** Grants permission to insert or delete IPSetDescriptor objects in an IPSet
  - **Resource types (\*required):** [ipset\*](#list_waf-resource-ipset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateRateBasedRule.html)  **
  - **Description:** Grants permission to modify a rate based rule
  - **Resource types (\*required):** [ratebasedrule\*](#list_waf-resource-ratebasedrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateRegexMatchSet.html)  **
  - **Description:** Grants permission to insert or delete RegexMatchTuple objects in a RegexMatchSet
  - **Resource types (\*required):** [regexmatchset\*](#list_waf-resource-regexmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateRegexPatternSet.html)  **
  - **Description:** Grants permission to insert or delete RegexPatternStrings in a RegexPatternSet
  - **Resource types (\*required):** [regexpatternset\*](#list_waf-resource-regexpatternset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateRule.html)  **
  - **Description:** Grants permission to modify a Rule
  - **Resource types (\*required):** [rule\*](#list_waf-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateRuleGroup.html)  **
  - **Description:** Grants permission to insert or delete ActivatedRule objects in a RuleGroup
  - **Resource types (\*required):** [rulegroup\*](#list_waf-resource-rulegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateSizeConstraintSet.html)  **
  - **Description:** Grants permission to insert or delete SizeConstraint objects in a SizeConstraintSet
  - **Resource types (\*required):** [sizeconstraintset\*](#list_waf-resource-sizeconstraintset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateSqlInjectionMatchSet.html)  **
  - **Description:** Grants permission to insert or delete SqlInjectionMatchTuple objects in an SqlInjectionMatchSet
  - **Resource types (\*required):** [sqlinjectionmatchset\*](#list_waf-resource-sqlinjectionmatchset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateWebACL.html)  **
  - **Description:** Grants permission to insert or delete ActivatedRule objects in a WebACL
  - **Resource types (\*required):** [webacl\*](#list_waf-resource-webacl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_UpdateXssMatchSet.html)  **
  - **Description:** Grants permission to insert or delete XssMatchTuple objects in an XssMatchSet
  - **Resource types (\*required):** [xssmatchset\*](#list_waf-resource-xssmatchset)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS WAF
<a name="list_waf-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [bytematchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ByteMatchSet.html)  | arn:${Partition}:waf::${Account}:bytematchset/${Id} |   | 
|  [geomatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GeoMatchSet.html)  | arn:${Partition}:waf::${Account}:geomatchset/${Id} |   | 
|  [ipset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_IPSet.html)  | arn:${Partition}:waf::${Account}:ipset/${Id} |   | 
|  [ratebasedrule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RateBasedRule.html)  | arn:${Partition}:waf::${Account}:ratebasedrule/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_) | 
|  [regexmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexMatchSet.html)  | arn:${Partition}:waf::${Account}:regexmatch/${Id} |   | 
|  [regexpatternset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexPatternSet.html)  | arn:${Partition}:waf::${Account}:regexpatternset/${Id} |   | 
|  [rule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_Rule.html)  | arn:${Partition}:waf::${Account}:rule/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_) | 
|  [rulegroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RuleGroup.html)  | arn:${Partition}:waf::${Account}:rulegroup/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_) | 
|  [sizeconstraintset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SizeConstraintSet.html)  | arn:${Partition}:waf::${Account}:sizeconstraintset/${Id} |   | 
|  [sqlinjectionmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SqlInjectionMatchSet.html)  | arn:${Partition}:waf::${Account}:sqlinjectionset/${Id} |   | 
|  [webacl](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_WebACL.html)  | arn:${Partition}:waf::${Account}:webacl/${Id} | [aws:ResourceTag/${TagKey}](#list_waf-aws_ResourceTag___TagKey_) | 
|  [xssmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_XssMatchSet.html)  | arn:${Partition}:waf::${Account}:xssmatchset/${Id} |   | 

## Condition keys for AWS WAF
<a name="list_waf-policy-keys"></a>

AWS WAF defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of mandatory tags in the request | ArrayOfString | 