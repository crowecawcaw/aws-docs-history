# StackRefactorSummary

The summary of a stack refactor operation.


## Contents





**Description** 


A description to help you identify the refactor.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ExecutionStatus** 


The operation status that's provided after calling the [ExecuteStackRefactor](API_ExecuteStackRefactor.md "API_ExecuteStackRefactor.md") action.


Type: String


Valid Values: `UNAVAILABLE | AVAILABLE | OBSOLETE | EXECUTE_IN_PROGRESS | EXECUTE_COMPLETE | EXECUTE_FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETE | ROLLBACK_FAILED`



Required: No




**ExecutionStatusReason** 


A detailed explanation for the stack refactor `ExecutionStatus`.


Type: String


Required: No




**StackRefactorId** 


The ID associated with the stack refactor created from the [CreateStackRefactor](API_CreateStackRefactor.md "API_CreateStackRefactor.md") action.


Type: String


Required: No




**Status** 


The stack refactor operation status that's provided after calling the [CreateStackRefactor](API_CreateStackRefactor.md "API_CreateStackRefactor.md") action.


Type: String


Valid Values: `CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED`



Required: No




**StatusReason** 


A detailed explanation for the stack refactor `Status`.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackRefactorSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackRefactorSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackRefactorSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackRefactorSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackRefactorSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackRefactorSummary")
