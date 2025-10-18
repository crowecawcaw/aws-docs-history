# EnableInsightRules

Enables the specified Contributor Insights rules. When rules are enabled, they
 immediately begin analyzing log data.


## Request Parameters





**RuleNames** 


An array of the rule names to enable. If you need to find out the names of your rules,
 use [DescribeInsightRules](API_DescribeInsightRules.md "API_DescribeInsightRules.md").


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[\x20-\x7E]+`



Required: Yes




## Response Elements


The following element is returned by the service.





**Failures** 


An array listing the rules that could not be enabled. You cannot disable or enable
 built-in rules.


Type: Array of [PartialFailure](API_PartialFailure.md "API_PartialFailure.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**LimitExceededException** 


The operation exceeded one or more limits.


HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/EnableInsightRules")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/EnableInsightRules "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/EnableInsightRules")
