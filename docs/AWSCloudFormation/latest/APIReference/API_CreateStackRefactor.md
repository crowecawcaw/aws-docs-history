# CreateStackRefactor

Creates a refactor across multiple stacks, with the list of stacks and resources that are
 affected.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Description** 


A description to help you identify the stack refactor.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**EnableStackCreation** 


Determines if a new stack is created with the refactor.


Type: Boolean


Required: No




**ResourceMappings.member.N**


The mappings for the stack resource `Source` and stack resource
 `Destination`.


Type: Array of [ResourceMapping](API_ResourceMapping.md "API_ResourceMapping.md") objects


Required: No




**StackDefinitions.member.N**


The stacks being refactored.


Type: Array of [StackDefinition](API_StackDefinition.md "API_StackDefinition.md") objects


Required: Yes




## Response Elements


The following element is returned by the service.





**StackRefactorId** 


The ID associated with the stack refactor created from the [CreateStackRefactor](API_CreateStackRefactor.md "API_CreateStackRefactor.md") action.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStackRefactor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStackRefactor "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStackRefactor")
