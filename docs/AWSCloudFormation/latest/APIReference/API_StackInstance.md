# StackInstance

A CloudFormation stack, in a specific account and Region, that's part of a StackSet operation. A
 stack instance is a reference to an attempted or actual stack in a given account within a given
 Region. A stack instance can exist without a stack—for example, if the stack couldn't be created
 for some reason. A stack instance is associated with only one StackSet. Each stack instance
 contains the ID of its associated StackSet, in addition to the ID of the actual stack and the
 stack status.


## Contents





**Account** 


[Self-managed permissions] The name of the AWS account that the stack instance is
 associated with.


Type: String


Pattern: `^[0-9]{12}$`



Required: No




**DriftStatus** 


Status of the stack instance's actual configuration compared to the expected template and
 parameter configuration of the StackSet it belongs to.



* `DRIFTED`: The stack differs from the expected template and parameter
 configuration of the StackSet it belongs to. A stack instance is considered to have drifted if
 one or more of the resources in the associated stack have drifted.
* `NOT_CHECKED`: CloudFormation hasn't checked if the stack instance differs from its
 expected StackSet configuration.
* `IN_SYNC`: The stack instance's actual configuration matches its expected
 StackSset configuration.
* `UNKNOWN`: This value is reserved for future use.

Type: String


Valid Values: `DRIFTED | IN_SYNC | UNKNOWN | NOT_CHECKED`



Required: No




**LastDriftCheckTimestamp** 


Most recent time when CloudFormation performed a drift detection operation on the stack
 instance. This value will be `NULL` for any stack instance that drift detection hasn't
 yet been performed on.


Type: Timestamp


Required: No




**LastOperationId** 


The last unique ID of a StackSet operation performed on a stack instance.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**OrganizationalUnitId** 


[Service-managed permissions] The organization root ID or organizational unit (OU) IDs that
 you specified for [DeploymentTargets](API_DeploymentTargets.md "API_DeploymentTargets.md").


Type: String


Pattern: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$`



Required: No




**ParameterOverrides.member.N** 


A list of parameters from the StackSet template whose values have been overridden in this
 stack instance.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**Region** 


The name of the AWS Region that the stack instance is associated with.


Type: String


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: No




**StackId** 


The ID of the stack instance.


Type: String


Required: No




**StackInstanceStatus** 


The detailed status of the stack instance.


Type: [StackInstanceComprehensiveStatus](API_StackInstanceComprehensiveStatus.md "API_StackInstanceComprehensiveStatus.md") object


Required: No




**StackSetId** 


The name or unique ID of the StackSet that the stack instance is associated with.


Type: String


Required: No




**Status** 


The status of the stack instance, in terms of its synchronization with its associated stack
 set.



* `INOPERABLE`: A `DeleteStackInstances` operation has failed and left
 the stack in an unstable state. Stacks in this state are excluded from further
 `UpdateStackSet` operations. You might need to perform a
 `DeleteStackInstances` operation, with `RetainStacks` set to
 `true`, to delete the stack instance, and then delete the stack manually.
 `INOPERABLE` can be returned here when the cause is a failed import. If it's due to
 a failed import, the operation can be retried once the failures are fixed. To see if this is
 due to a failed import, look at the `DetailedStatus` member in the
 `StackInstanceSummary` member that is a peer to this `Status`
 member.
* `OUTDATED`: The stack isn't currently up to date with the StackSet
 because:




	+ The associated stack failed during a `CreateStackSet` or
	 `UpdateStackSet` operation.
	+ The stack was part of a `CreateStackSet` or `UpdateStackSet`
	 operation that failed or was stopped before the stack was created or updated.
* `CURRENT`: The stack is currently up to date with the StackSet.

Type: String


Valid Values: `CURRENT | OUTDATED | INOPERABLE`



Required: No




**StatusReason** 


The explanation for the specific status code that's assigned to this stack instance.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackInstance "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackInstance")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackInstance "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackInstance")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackInstance "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackInstance")
