# DeleteGeneratedTemplate

Deleted a generated template.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**GeneratedTemplateName** 


The name or Amazon Resource Name (ARN) of a generated template.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ConcurrentResourcesLimitExceeded** 


No more than 5 generated templates can be in an `InProgress` or `Pending` status at one
 time. This error is also returned if a generated template that is in an `InProgress` or
 `Pending` status is attempted to be updated or deleted.


HTTP Status Code: 429




**GeneratedTemplateNotFound** 


The generated template was not found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeleteGeneratedTemplate")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeleteGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeleteGeneratedTemplate")
