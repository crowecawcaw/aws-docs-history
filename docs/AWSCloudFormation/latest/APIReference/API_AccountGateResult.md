# AccountGateResult

Structure that contains the results of the account gate function which CloudFormation invokes,
 if present, before proceeding with a StackSet operation in an account and Region.

For each account and Region, CloudFormation lets you specify a Lambda function that encapsulates
 any requirements that must be met before CloudFormation can proceed with a StackSet operation in that
 account and Region. CloudFormation invokes the function each time a StackSet operation is requested
 for that account and Region; if the function returns `FAILED`, CloudFormation cancels the
 operation in that account and Region, and sets the StackSet operation result status for that
 account and Region to `FAILED`.

For more information, see [Prevent failed StackSets
 deployments using target account gates](../UserGuide/stacksets-account-gating.md "../UserGuide/stacksets-account-gating.md") in the
 *AWS CloudFormation User Guide*.


## Contents





**Status** 


The status of the account gate function.



* `SUCCEEDED`: The account gate function has determined that the account and
 Region passes any requirements for a StackSet operation to occur. CloudFormation proceeds with the
 stack operation in that account and Region.
* `FAILED`: The account gate function has determined that the account and Region
 doesn't meet the requirements for a StackSet operation to occur. CloudFormation cancels the
 StackSet operation in that account and Region, and sets the StackSet operation result status
 for that account and Region to `FAILED`.
* `SKIPPED`: CloudFormation has skipped calling the account gate function for this
 account and Region, for one of the following reasons:




	+ An account gate function hasn't been specified for the account and Region. CloudFormation
	 proceeds with the StackSet operation in this account and Region.
	+ The `AWSCloudFormationStackSetExecutionRole` of the administration account
	 lacks permissions to invoke the function. CloudFormation proceeds with the StackSet operation in
	 this account and Region.
	+ Either no action is necessary, or no action is possible, on the stack. CloudFormation skips
	 the StackSet operation in this account and Region.

Type: String


Valid Values: `SUCCEEDED | FAILED | SKIPPED`



Required: No




**StatusReason** 


The reason for the account gate status assigned to this account and Region for the StackSet
 operation.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/AccountGateResult "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/AccountGateResult")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/AccountGateResult "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/AccountGateResult")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/AccountGateResult "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/AccountGateResult")
