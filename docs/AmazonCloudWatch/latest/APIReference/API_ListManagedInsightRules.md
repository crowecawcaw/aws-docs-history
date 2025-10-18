# ListManagedInsightRules

 Returns a list that contains the number of managed Contributor Insights rules in your
 account.
 
 


## Request Parameters





**MaxResults** 


 The maximum number of results to return in one operation. If you omit this parameter,
 the default number is used. The default number is `100`. 


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 500.


Required: No




**NextToken** 


 Include this value to get the next set of rules if the value was returned by the
 previous operation. 


Type: String


Required: No




**ResourceARN** 


 The ARN of an AWS resource that has managed Contributor Insights
 rules. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




## Response Elements


The following elements are returned by the service.





**ManagedRules** 


 The managed rules that are available for the specified AWS resource.
 


Type: Array of [ManagedRuleDescription](API_ManagedRuleDescription.md "API_ManagedRuleDescription.md") objects




**NextToken** 


 Include this value to get the next set of rules if the value was returned by the
 previous operation. 


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidNextToken** 


The next token specified is invalid.





**message** 





HTTP Status Code: 400




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListManagedInsightRules")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListManagedInsightRules")
