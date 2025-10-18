# InsightRuleContributor

One of the unique contributors found by a Contributor Insights rule. If the rule
 contains multiple keys, then a unique contributor is a unique combination of values from
 all the keys in the rule.

If the rule contains a single key, then each unique contributor is each unique value
 for this key.

For more information, see [GetInsightRuleReport](API_GetInsightRuleReport.md "API_GetInsightRuleReport.md").


## Contents





**ApproximateAggregateValue** 


An approximation of the aggregate value that comes from this contributor.


Type: Double


Required: Yes




**Datapoints** 


An array of the data points where this contributor is present. Only the data points
 when this contributor appeared are included in the array.


Type: Array of [InsightRuleContributorDatapoint](API_InsightRuleContributorDatapoint.md "API_InsightRuleContributorDatapoint.md") objects


Required: Yes




**Keys** 


One of the log entry field keywords that is used to define contributors for this
 rule.


Type: Array of strings


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/InsightRuleContributor "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/InsightRuleContributor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/InsightRuleContributor "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/InsightRuleContributor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/InsightRuleContributor "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/InsightRuleContributor")
