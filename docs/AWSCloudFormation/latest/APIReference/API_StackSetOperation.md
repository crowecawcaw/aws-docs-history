# StackSetOperation

The structure that contains information about a StackSet operation.


## Contents





**Action** 


The type of StackSet operation: `CREATE`, `UPDATE`, or
 `DELETE`. Create and delete operations affect only the specified stack instances that
 are associated with the specified StackSet. Update operations affect both the StackSet itself, in
 addition to *all* associated stack instances.


Type: String


Valid Values: `CREATE | UPDATE | DELETE | DETECT_DRIFT`



Required: No




**AdministrationRoleARN** 


The Amazon Resource Name (ARN) of the IAM role used to perform this StackSet
 operation.


Use customized administrator roles to control which users or groups can manage specific
 StackSets within the same administrator account. For more information, see [Grant self-managed
 permissions](../UserGuide/stacksets-prereqs-self-managed.md "../UserGuide/stacksets-prereqs-self-managed.md") in the *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 20. Maximum length of 2048.


Required: No




**CreationTimestamp** 


The time at which the operation was initiated. Note that the creation times for the stack
 set operation might differ from the creation time of the individual stacks themselves. This is
 because CloudFormation needs to perform preparatory work for the operation, such as dispatching the
 work to the requested Regions, before actually creating the first stacks.


Type: Timestamp


Required: No




**DeploymentTargets** 


The AWS Organizations accounts affected by the stack operation. Valid only if the
 StackSet uses service-managed permissions.


Type: [DeploymentTargets](API_DeploymentTargets.md "API_DeploymentTargets.md") object


Required: No




**EndTimestamp** 


The time at which the StackSet operation ended, across all accounts and Regions specified.
 Note that this doesn't necessarily mean that the StackSet operation was successful, or even
 attempted, in each account or Region.


Type: Timestamp


Required: No




**ExecutionRoleName** 


The name of the IAM execution role used to create or update the StackSet.


Use customized execution roles to control which stack resources users and groups can include
 in their StackSets.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z_0-9+=,.@-]+`



Required: No




**OperationId** 


The unique ID of a StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**OperationPreferences** 


The preferences for how CloudFormation performs this StackSet operation.


Type: [StackSetOperationPreferences](API_StackSetOperationPreferences.md "API_StackSetOperationPreferences.md") object


Required: No




**RetainStacks** 


For StackSet operations of action type `DELETE`, specifies whether to remove the
 stack instances from the specified StackSet, but doesn't delete the stacks. You can't
 re-associate a retained stack, or add an existing, saved stack to a new StackSet.


Type: Boolean


Required: No




**StackSetDriftDetectionDetails** 


Detailed information about the drift status of the StackSet. This includes information about
 drift operations currently being performed on the StackSet.


This information will only be present for StackSet operations whose `Action` type
 is `DETECT_DRIFT`.


For more information, see [Performing drift detection on
 CloudFormation StackSets](../UserGuide/stacksets-drift.md "../UserGuide/stacksets-drift.md") in the *AWS CloudFormation User Guide*.


Type: [StackSetDriftDetectionDetails](API_StackSetDriftDetectionDetails.md "API_StackSetDriftDetectionDetails.md") object


Required: No




**StackSetId** 


The ID of the StackSet.


Type: String


Required: No




**Status** 


The status of the operation.



* `FAILED`: The operation exceeded the specified failure tolerance. The failure
 tolerance value that you've set for an operation is applied for each Region during stack create
 and update operations. If the number of failed stacks within a Region exceeds the failure
 tolerance, the status of the operation in the Region is set to `FAILED`. This in
 turn sets the status of the operation as a whole to `FAILED`, and CloudFormation cancels
 the operation in any remaining Regions.
* `QUEUED`: [Service-managed permissions] For automatic deployments that require
 a sequence of operations, the operation is queued to be performed. For more information, see
 the [StackSets status codes](../UserGuide/stacksets-concepts.md#stackset-status-codes "../UserGuide/stacksets-concepts.md#stackset-status-codes") in the *AWS CloudFormation User Guide*.
* `RUNNING`: The operation is currently being performed.
* `STOPPED`: The user has canceled the operation.
* `STOPPING`: The operation is in the process of stopping, at user
 request.
* `SUCCEEDED`: The operation completed creating or updating all the specified
 stacks without exceeding the failure tolerance for the operation.

Type: String


Valid Values: `RUNNING | SUCCEEDED | FAILED | STOPPING | STOPPED | QUEUED`



Required: No




**StatusDetails** 


Detailed information about the StackSet operation.


Type: [StackSetOperationStatusDetails](API_StackSetOperationStatusDetails.md "API_StackSetOperationStatusDetails.md") object


Required: No




**StatusReason** 


The status of the operation in details.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperation "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperation")
