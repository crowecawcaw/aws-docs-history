# DescribeStackRefactor

Describes the stack refactor status.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**StackRefactorId** 


The ID associated with the stack refactor created from the [CreateStackRefactor](API_CreateStackRefactor.md "API_CreateStackRefactor.md") action.


Type: String


Required: Yes




## Response Elements


The following elements are returned by the service.





**Description** 


A description to help you identify the refactor.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**ExecutionStatus** 


The stack refactor execution operation status that's provided after calling the [ExecuteStackRefactor](API_ExecuteStackRefactor.md "API_ExecuteStackRefactor.md") action.


Type: String


Valid Values: `UNAVAILABLE | AVAILABLE | OBSOLETE | EXECUTE_IN_PROGRESS | EXECUTE_COMPLETE | EXECUTE_FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETE | ROLLBACK_FAILED`





**ExecutionStatusReason** 


A detailed explanation for the stack refactor `ExecutionStatus`.


Type: String




**StackIds.member.N**


The unique ID for each stack.


Type: Array of strings




**StackRefactorId** 


The ID associated with the stack refactor created from the [CreateStackRefactor](API_CreateStackRefactor.md "API_CreateStackRefactor.md") action.


Type: String




**Status** 


The stack refactor operation status that's provided after calling the [CreateStackRefactor](API_CreateStackRefactor.md "API_CreateStackRefactor.md") action.


Type: String


Valid Values: `CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED`





**StatusReason** 


A detailed explanation for the stack refactor operation `Status`.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**StackRefactorNotFound** 


The specified stack refactor can't be found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackRefactor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackRefactor "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackRefactor")
