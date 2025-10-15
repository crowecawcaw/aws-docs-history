# Stack

The Stack data type.


## Contents





**CreationTime** 


The time at which the stack was created.


Type: Timestamp


Required: Yes




**StackName** 


The name associated with the stack.


Type: String


Required: Yes




**StackStatus** 


Current status of the stack.


Type: String


Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE | ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_COMPLETE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE_CLEANUP_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | UPDATE_ROLLBACK_IN_PROGRESS | UPDATE_ROLLBACK_FAILED | UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS | UPDATE_ROLLBACK_COMPLETE | REVIEW_IN_PROGRESS | IMPORT_IN_PROGRESS | IMPORT_COMPLETE | IMPORT_ROLLBACK_IN_PROGRESS | IMPORT_ROLLBACK_FAILED | IMPORT_ROLLBACK_COMPLETE`



Required: Yes




**Capabilities.member.N** 


The capabilities allowed in the stack.


Type: Array of strings


Valid Values: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`



Required: No




**ChangeSetId** 


The unique ID of the change set.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`



Required: No




**DeletionMode** 


Specifies the deletion mode for the stack. Possible values are:



* `STANDARD` - Use the standard behavior. Specifying this value is the same as
 not specifying this parameter.
* `FORCE_DELETE_STACK` - Delete the stack if it's stuck in a
 `DELETE_FAILED` state due to resource deletion failure.

Type: String


Valid Values: `STANDARD | FORCE_DELETE_STACK`



Required: No




**DeletionTime** 


The time the stack was deleted.


Type: Timestamp


Required: No




**Description** 


A user-defined description associated with the stack.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**DetailedStatus** 


The detailed status of the resource or stack. If `CONFIGURATION_COMPLETE` is
 present, the resource or resource configuration phase has completed and the stabilization of the
 resources is in progress. The StackSets `CONFIGURATION_COMPLETE` when all of the
 resources in the stack have reached that event. For more information, see [Understand
 CloudFormation stack creation events](../UserGuide/stack-resource-configuration-complete.md "../UserGuide/stack-resource-configuration-complete.md") in the *AWS CloudFormation User Guide*.


Type: String


Valid Values: `CONFIGURATION_COMPLETE | VALIDATION_FAILED`



Required: No




**DisableRollback** 


Boolean to enable or disable rollback on stack creation failures:



* `true`: disable rollback.
* `false`: enable rollback.

Type: Boolean


Required: No




**DriftInformation** 


Information about whether a stack's actual configuration differs, or has
 *drifted*, from its expected configuration, as defined in the stack template
 and any values specified as template parameters. For more information, see [Detect
 unmanaged configuration changes to stacks and resources with drift detection](../UserGuide/using-cfn-stack-drift.md "../UserGuide/using-cfn-stack-drift.md").


Type: [StackDriftInformation](API_StackDriftInformation.md "API_StackDriftInformation.md") object


Required: No




**EnableTerminationProtection** 


Whether termination protection is enabled for the stack.


For [nested stacks](../UserGuide/using-cfn-nested-stacks.md "../UserGuide/using-cfn-nested-stacks.md"),
 termination protection is set on the root stack and can't be changed directly on the nested
 stack. For more information, see [Protect a CloudFormation
 stack from being deleted](../UserGuide/using-cfn-protect-stacks.md "../UserGuide/using-cfn-protect-stacks.md") in the *AWS CloudFormation User Guide*.


Type: Boolean


Required: No




**LastUpdatedTime** 


The time the stack was last updated. This field will only be returned if the stack has been
 updated at least once.


Type: Timestamp


Required: No




**NotificationARNs.member.N** 


Amazon SNS topic Amazon Resource Names (ARNs) to which stack related events are published.


Type: Array of strings


Array Members: Maximum number of 5 items.


Required: No




**Outputs.member.N** 


A list of output structures.


Type: Array of [Output](API_Output.md "API_Output.md") objects


Required: No




**Parameters.member.N** 


A list of `Parameter` structures.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**ParentId** 


For nested stacks, the stack ID of the direct parent of this stack. For the first level of
 nested stacks, the root stack is also the parent stack.


For more information, see [Nested stacks](../UserGuide/using-cfn-nested-stacks.md "../UserGuide/using-cfn-nested-stacks.md") in
 the *AWS CloudFormation User Guide*.


Type: String


Required: No




**RetainExceptOnCreate** 


When set to `true`, newly created resources are deleted when the operation rolls
 back. This includes newly created resources marked with a deletion policy of
 `Retain`.


Default: `false`



Type: Boolean


Required: No




**RoleARN** 


The Amazon Resource Name (ARN) of an IAM role that's associated with the stack. During a
 stack operation, CloudFormation uses this role's credentials to make calls on your behalf.


Type: String


Length Constraints: Minimum length of 20. Maximum length of 2048.


Required: No




**RollbackConfiguration** 


The rollback triggers for CloudFormation to monitor during stack creation and updating
 operations, and for the specified monitoring period afterwards.


Type: [RollbackConfiguration](API_RollbackConfiguration.md "API_RollbackConfiguration.md") object


Required: No




**RootId** 


For nested stacks, the stack ID of the top-level stack to which the nested stack ultimately
 belongs.


For more information, see [Nested stacks](../UserGuide/using-cfn-nested-stacks.md "../UserGuide/using-cfn-nested-stacks.md") in
 the *AWS CloudFormation User Guide*.


Type: String


Required: No




**StackId** 


Unique identifier of the stack.


Type: String


Required: No




**StackStatusReason** 


Success/failure message associated with the stack status.


Type: String


Required: No




**Tags.member.N** 


A list of `Tag`s that specify information about the stack.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 50 items.


Required: No




**TimeoutInMinutes** 


The amount of time within which stack creation should complete.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Stack "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Stack")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Stack "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Stack")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Stack "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Stack")
