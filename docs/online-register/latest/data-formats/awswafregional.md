

# Data retrieval APIs for AWS WAF Regional
<a name="awswafregional"></a>

AWS WAF Regional provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="waf-regional-GetByteMatchSet"></a>[GetByteMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetByteMatchSet.html) | Retrieve a ByteMatchSet | Read | 
| <a name="waf-regional-GetChangeToken"></a>[GetChangeToken](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetChangeToken.html) | Retrieve a change token to use in create, update, and delete requests | Read | 
| <a name="waf-regional-GetChangeTokenStatus"></a>[GetChangeTokenStatus](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetChangeTokenStatus.html) | Retrieve the status of a change token | Read | 
| <a name="waf-regional-GetGeoMatchSet"></a>[GetGeoMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetGeoMatchSet.html) | Retrieve a GeoMatchSet | Read | 
| <a name="waf-regional-GetIPSet"></a>[GetIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetIPSet.html) | Retrieve an IPSet | Read | 
| <a name="waf-regional-GetLoggingConfiguration"></a>[GetLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetLoggingConfiguration.html) | Retrieve a LoggingConfiguration | Read | 
| <a name="waf-regional-GetPermissionPolicy"></a>[GetPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetPermissionPolicy.html) | Retrieve an IAM policy attached to a RuleGroup | Read | 
| <a name="waf-regional-GetRateBasedRule"></a>[GetRateBasedRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRateBasedRule.html) | Retrieve a RateBasedRule | Read | 
| <a name="waf-regional-GetRateBasedRuleManagedKeys"></a>[GetRateBasedRuleManagedKeys](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRateBasedRuleManagedKeys.html) | Retrieve the array of IP addresses that are currently being blocked by a RateBasedRule | Read | 
| <a name="waf-regional-GetRegexMatchSet"></a>[GetRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRegexMatchSet.html) | Retrieve a RegexMatchSet | Read | 
| <a name="waf-regional-GetRegexPatternSet"></a>[GetRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRegexPatternSet.html) | Retrieve a RegexPatternSet | Read | 
| <a name="waf-regional-GetRule"></a>[GetRule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRule.html) | Retrieve a Rule | Read | 
| <a name="waf-regional-GetRuleGroup"></a>[GetRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetRuleGroup.html) | Retrieve a RuleGroup | Read | 
| <a name="waf-regional-GetSampledRequests"></a>[GetSampledRequests](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetSampledRequests.html) | Retrieve detailed information for a sample set of web requests | Read | 
| <a name="waf-regional-GetSizeConstraintSet"></a>[GetSizeConstraintSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetSizeConstraintSet.html) | Retrieve a SizeConstraintSet | Read | 
| <a name="waf-regional-GetSqlInjectionMatchSet"></a>[GetSqlInjectionMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetSqlInjectionMatchSet.html) | Retrieve an SqlInjectionMatchSet | Read | 
| <a name="waf-regional-GetWebACL"></a>[GetWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetWebACL.html) | Retrieve a WebACL | Read | 
| <a name="waf-regional-GetWebACLForResource"></a>[GetWebACLForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetWebACLForResource.html) | Retrieve a WebACL that's associated with a specified resource | Read | 
| <a name="waf-regional-GetXssMatchSet"></a>[GetXssMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GetXssMatchSet.html) | Retrieve an XssMatchSet | Read | 
| <a name="waf-regional-ListActivatedRulesInRuleGroup"></a>[ListActivatedRulesInRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListActivatedRulesInRuleGroup.html) | Retrieve an array of ActivatedRule objects | List | 
| <a name="waf-regional-ListByteMatchSets"></a>[ListByteMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListByteMatchSets.html) | Retrieve an array of ByteMatchSetSummary objects | List | 
| <a name="waf-regional-ListGeoMatchSets"></a>[ListGeoMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListGeoMatchSets.html) | Retrieve an array of GeoMatchSetSummary objects | List | 
| <a name="waf-regional-ListIPSets"></a>[ListIPSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListIPSets.html) | Retrieve an array of IPSetSummary objects | List | 
| <a name="waf-regional-ListLoggingConfigurations"></a>[ListLoggingConfigurations](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListLoggingConfigurations.html) | Retrieve an array of LoggingConfiguration objects | List | 
| <a name="waf-regional-ListRateBasedRules"></a>[ListRateBasedRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRateBasedRules.html) | Retrieve an array of RuleSummary objects | List | 
| <a name="waf-regional-ListRegexMatchSets"></a>[ListRegexMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRegexMatchSets.html) | Retrieve an array of RegexMatchSetSummary objects | List | 
| <a name="waf-regional-ListRegexPatternSets"></a>[ListRegexPatternSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRegexPatternSets.html) | Retrieve an array of RegexPatternSetSummary objects | List | 
| <a name="waf-regional-ListResourcesForWebACL"></a>[ListResourcesForWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListResourcesForWebACL.html) | Retrieve an array of resources associated with a specified WebACL | List | 
| <a name="waf-regional-ListRuleGroups"></a>[ListRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRuleGroups.html) | Retrieve an array of RuleGroup objects | List | 
| <a name="waf-regional-ListRules"></a>[ListRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRules.html) | Retrieve an array of RuleSummary objects | List | 
| <a name="waf-regional-ListSizeConstraintSets"></a>[ListSizeConstraintSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListSizeConstraintSets.html) | Retrieve an array of SizeConstraintSetSummary objects | List | 
| <a name="waf-regional-ListSqlInjectionMatchSets"></a>[ListSqlInjectionMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListSqlInjectionMatchSets.html) | Retrieve an array of SqlInjectionMatchSet objects | List | 
| <a name="waf-regional-ListSubscribedRuleGroups"></a>[ListSubscribedRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListSubscribedRuleGroups.html) | Retrieve an array of RuleGroup objects that you are subscribed to | List | 
| <a name="waf-regional-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListTagsForResource.html) | Lists the Tags for a resource | Read | 
| <a name="waf-regional-ListWebACLs"></a>[ListWebACLs](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListWebACLs.html) | Retrieve an array of WebACLSummary objects | List | 
| <a name="waf-regional-ListXssMatchSets"></a>[ListXssMatchSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListXssMatchSets.html) | Retrieve an array of XssMatchSet objects | List | 