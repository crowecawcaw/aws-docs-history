

# Data retrieval APIs for AWS WAF V2
<a name="awswafv2"></a>

AWS WAF V2 provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="wafv2-CheckCapacity"></a>[CheckCapacity](https://docs.aws.amazon.com/waf/latest/APIReference/API_CheckCapacity.html) | Calculate web ACL capacity unit (WCU) requirements for a specified scope and set of rules | Read | 
| <a name="wafv2-DescribeAllManagedProducts"></a>[DescribeAllManagedProducts](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeAllManagedProducts.html) | Retrieve product information for a managed rule group | Read | 
| <a name="wafv2-DescribeManagedProductsByVendor"></a>[DescribeManagedProductsByVendor](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeManagedProductsByVendor.html) | Retrieve product information for a managed rule group by a given vendor | Read | 
| <a name="wafv2-DescribeManagedRuleGroup"></a>[DescribeManagedRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeManagedRuleGroup.html) | Retrieve high-level information for a managed rule group | Read | 
| <a name="wafv2-GenerateMobileSdkReleaseUrl"></a>[GenerateMobileSdkReleaseUrl](https://docs.aws.amazon.com/waf/latest/APIReference/API_GenerateMobileSdkReleaseUrl.html) | Generate a presigned download URL for the specified release of the mobile SDK | Read | 
| <a name="wafv2-GetDecryptedAPIKey"></a>[GetDecryptedAPIKey](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetDecryptedAPIKey.html) | Return your API key in decrypted form. Use this to check the token domains that you have defined for the key | Read | 
| <a name="wafv2-GetIPSet"></a>[GetIPSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetIPSet.html) | Retrieve details about an IPSet | Read | 
| <a name="wafv2-GetLoggingConfiguration"></a>[GetLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetLoggingConfiguration.html) | Retrieve LoggingConfiguration for a WebACL | Read | 
| <a name="wafv2-GetManagedRuleSet"></a>[GetManagedRuleSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetManagedRuleSet.html) | Retrieve details about a ManagedRuleSet | Read | 
| <a name="wafv2-GetMobileSdkRelease"></a>[GetMobileSdkRelease](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetMobileSdkRelease.html) | Retrieve information for the specified mobile SDK release, including release notes and tags | Read | 
| <a name="wafv2-GetPermissionPolicy"></a>[GetPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetPermissionPolicy.html) | Retrieve a PermissionPolicy for a RuleGroup | Read | 
| <a name="wafv2-GetRateBasedStatementManagedKeys"></a>[GetRateBasedStatementManagedKeys](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRateBasedStatementManagedKeys.html) | Retrieve the keys that are currently blocked by a rate-based rule | Read | 
| <a name="wafv2-GetRegexPatternSet"></a>[GetRegexPatternSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRegexPatternSet.html) | Retrieve details about a RegexPatternSet | Read | 
| <a name="wafv2-GetRevenueStatistics"></a>[GetRevenueStatistics](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRevenueStatistics.html) | Retrieve monetization revenue statistics ranked by source or path within a specified time window | Read | 
| <a name="wafv2-GetRevenueStatisticsSummary"></a>[GetRevenueStatisticsSummary](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRevenueStatisticsSummary.html) | Retrieve a summary of monetization revenue statistics within a specified time window | Read | 
| <a name="wafv2-GetRevenueStatisticsTimeSeries"></a>[GetRevenueStatisticsTimeSeries](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRevenueStatisticsTimeSeries.html) | Retrieve monetization revenue statistics as a time series within a specified time window | Read | 
| <a name="wafv2-GetRuleGroup"></a>[GetRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRuleGroup.html) | Retrieve details about a RuleGroup | Read | 
| <a name="wafv2-GetSampledRequests"></a>[GetSampledRequests](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetSampledRequests.html) | Retrieve detailed information about a sampling of web requests | Read | 
| <a name="wafv2-GetTopPathStatisticsByTraffic"></a>[GetTopPathStatisticsByTraffic](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetTopPathStatisticsByTraffic.html) | Retrieve aggregated path statistics with bot traffic analysis for a WebACL within a specified time window | Read | 
| <a name="wafv2-GetWebACL"></a>[GetWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetWebACL.html) | Retrieve details about a WebACL | Read | 
| <a name="wafv2-GetWebACLForResource"></a>[GetWebACLForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetWebACLForResource.html) | Retrieve the WebACL that's associated with a resource | Read | 
| <a name="wafv2-ListAPIKeys"></a>[ListAPIKeys](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListAPIKeys.html) | Retrieve a list of the API keys that you've defined for the specified scope | List | 
| <a name="wafv2-ListAvailableManagedRuleGroupVersions"></a>[ListAvailableManagedRuleGroupVersions](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListAvailableManagedRuleGroupVersions.html) | Retrieve an array of managed rule group versions that are available for you to use | List | 
| <a name="wafv2-ListAvailableManagedRuleGroups"></a>[ListAvailableManagedRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListAvailableManagedRuleGroups.html) | Retrieve an array of managed rule groups that are available for you to use | List | 
| <a name="wafv2-ListIPSets"></a>[ListIPSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListIPSets.html) | Retrieve an array of IPSetSummary objects for the IP sets that you manage | List | 
| <a name="wafv2-ListLoggingConfigurations"></a>[ListLoggingConfigurations](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListLoggingConfigurations.html) | Retrieve an array of your LoggingConfiguration objects | List | 
| <a name="wafv2-ListManagedRuleSets"></a>[ListManagedRuleSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListManagedRuleSets.html) | Retrieve an array of your ManagedRuleSet objects | List | 
| <a name="wafv2-ListMobileSdkReleases"></a>[ListMobileSdkReleases](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListMobileSdkReleases.html) | Retrieve a list of the available releases for the mobile SDK and the specified device platform | List | 
| <a name="wafv2-ListRegexPatternSets"></a>[ListRegexPatternSets](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListRegexPatternSets.html) | Retrieve an array of RegexPatternSetSummary objects for the regex pattern sets that you manage | List | 
| <a name="wafv2-ListResourcesForWebACL"></a>[ListResourcesForWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListResourcesForWebACL.html) | Retrieve an array of the Amazon Resource Names (ARNs) for the resources that are associated with a web ACL | List | 
| <a name="wafv2-ListRuleGroups"></a>[ListRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListRuleGroups.html) | Retrieve an array of RuleGroupSummary objects for the rule groups that you manage | List | 
| <a name="wafv2-ListSettlementRecords"></a>[ListSettlementRecords](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListSettlementRecords.html) | Retrieve a list of monetization settlement records within a specified time window | List | 
| <a name="wafv2-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListTagsForResource.html) | List tags for a resource | Read | 
| <a name="wafv2-ListWebACLs"></a>[ListWebACLs](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListWebACLs.html) | Retrieve an array of WebACLSummary objects for the web ACLs that you manage | List | 