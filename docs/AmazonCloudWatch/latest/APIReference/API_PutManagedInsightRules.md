# PutManagedInsightRules

 Creates a managed Contributor Insights rule for a specified AWS
 resource. When you enable a managed rule, you create a Contributor Insights rule that
 collects data from AWS services. You cannot edit these rules with
 `PutInsightRule`. The rules can be enabled, disabled, and deleted using
 `EnableInsightRules`, `DisableInsightRules`, and
 `DeleteInsightRules`. If a previously created managed rule is currently
 disabled, a subsequent call to this API will re-enable it. Use
 `ListManagedInsightRules` to describe all available rules.
 
 


## Request Parameters





**ManagedRules** 


 A list of `ManagedRules` to enable. 


Type: Array of [ManagedRule](API_ManagedRule.md "API_ManagedRule.md") objects


Required: Yes




## Response Elements


The following element is returned by the service.





**Failures** 


 An array that lists the rules that could not be enabled. 


Type: Array of [PartialFailure](API_PartialFailure.md "API_PartialFailure.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutManagedInsightRules")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutManagedInsightRules "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutManagedInsightRules")
