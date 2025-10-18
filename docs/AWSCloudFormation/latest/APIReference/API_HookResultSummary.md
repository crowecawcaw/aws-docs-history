# HookResultSummary

Describes a Hook invocation, its status, and the reason for its status.


## Contents





**FailureMode** 


The failure mode of the invocation.


Type: String


Valid Values: `FAIL | WARN`



Required: No




**HookExecutionTarget** 


The ARN of the target stack or request token of the Cloud Control API operation.


Only shown in responses when the request does not specify `TargetType` and
 `TargetId` filters.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1600.


Pattern: `[a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/]*|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`



Required: No




**HookResultId** 


The unique identifier for this Hook invocation result.


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`



Required: No




**HookStatusReason** 


A description of the Hook results status. For example, if the Hook
 result is in a failed state, this may contain additional information for the failed state.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**InvocationPoint** 


The specific point in the provisioning process where the Hook is invoked.


Type: String


Valid Values: `PRE_PROVISION`



Required: No




**InvokedAt** 


The timestamp when the Hook was invoked.


Only shown in responses when the request does not specify `TargetType` and
 `TargetId` filters.


Type: Timestamp


Required: No




**Status** 


The status of the Hook invocation. The following statuses are possible:



* `HOOK_IN_PROGRESS`: The Hook is currently running.
* `HOOK_COMPLETE_SUCCEEDED`: The Hook completed successfully.
* `HOOK_COMPLETE_FAILED`: The Hook completed but failed
 validation.
* `HOOK_FAILED`: The Hook encountered an error during execution.

Type: String


Valid Values: `HOOK_IN_PROGRESS | HOOK_COMPLETE_SUCCEEDED | HOOK_COMPLETE_FAILED | HOOK_FAILED`



Required: No




**TargetId** 


The unique identifier of the Hook invocation target.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1600.


Pattern: `[a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/]*|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`



Required: No




**TargetType** 


The target type that the Hook was invoked against.


Type: String


Valid Values: `CHANGE_SET | STACK | RESOURCE | CLOUD_CONTROL`



Required: No




**TypeArn** 


The ARN of the Hook that was invoked.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/[A-Za-z0-9-]+/?`



Required: No




**TypeConfigurationVersionId** 


The version of the Hook configuration.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




**TypeName** 


The name of the Hook that was invoked.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 196.


Required: No




**TypeVersionId** 


The version of the Hook that was invoked.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/HookResultSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/HookResultSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/HookResultSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/HookResultSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/HookResultSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/HookResultSummary")
