# RollbackStack

When specifying `RollbackStack`, you preserve the state of previously
 provisioned resources when an operation fails. You can check the status of the stack through
 the [DescribeStacks](API_DescribeStacks.md "API_DescribeStacks.md") operation.

Rolls back the specified stack to the last known stable state from
 `CREATE_FAILED` or `UPDATE_FAILED` stack statuses.

This operation will delete a stack if it doesn't contain a last known stable state. A last
 known stable state includes any status in a `*_COMPLETE`. This includes the
 following stack statuses.


* `CREATE_COMPLETE`
* `UPDATE_COMPLETE`
* `UPDATE_ROLLBACK_COMPLETE`
* `IMPORT_COMPLETE`
* `IMPORT_ROLLBACK_COMPLETE`

## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**ClientRequestToken** 


A unique identifier for this `RollbackStack` request.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**RetainExceptOnCreate** 


When set to `true`, newly created resources are deleted when the operation
 rolls back. This includes newly created resources marked with a deletion policy of
 `Retain`.


Default: `false`



Type: Boolean


Required: No




**RoleARN** 


The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to rollback the
 stack.


Type: String


Length Constraints: Minimum length of 20. Maximum length of 2048.


Required: No




**StackName** 


The name that's associated with the stack.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: Yes




## Response Elements


The following element is returned by the service.





**StackId** 


Unique identifier of the stack.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**TokenAlreadyExists** 


A client request token already exists.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RollbackStack")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RollbackStack "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RollbackStack")
