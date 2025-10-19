# ListGeneratedTemplates

Lists your generated templates in this Region.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**MaxResults** 


If the number of available results exceeds this maximum, the response includes a
 `NextToken` value that you can use for the `NextToken` parameter to
 get the next set of results. By default the `ListGeneratedTemplates` API action
 will return at most 50 results in each response. The maximum value is 100.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**NextToken** 


A string that identifies the next page of resource scan results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all the remaining results, `NextToken` is set to
 a token. To retrieve the next set of results, call `ListGeneratedTemplates` again
 and use that value for the `NextToken` parameter. If the request returns all
 results, `NextToken` is set to an empty string.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**Summaries.member.N**


A list of summaries of the generated templates.


Type: Array of [TemplateSummary](API_TemplateSummary.md "API_TemplateSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListGeneratedTemplates")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListGeneratedTemplates "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListGeneratedTemplates")
