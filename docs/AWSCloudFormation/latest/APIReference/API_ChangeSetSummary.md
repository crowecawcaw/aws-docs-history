# ChangeSetSummary

The `ChangeSetSummary` structure describes a change set, its status, and the
 stack with which it's associated.


## Contents





**ChangeSetId** 


The ID of the change set.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`



Required: No




**ChangeSetName** 


The name of the change set.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z][-a-zA-Z0-9]*`



Required: No




**CreationTime** 


The start time when the change set was created, in UTC.


Type: Timestamp


Required: No




**Description** 


Descriptive information about the change set.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ExecutionStatus** 


If the change set execution status is `AVAILABLE`, you can execute the change
 set. If you can't execute the change set, the status indicates why. For example, a change set
 might be in an `UNAVAILABLE` state because CloudFormation is still creating it or in an
 `OBSOLETE` state because the stack was already updated.


Type: String


Valid Values: `UNAVAILABLE | AVAILABLE | EXECUTE_IN_PROGRESS | EXECUTE_COMPLETE | EXECUTE_FAILED | OBSOLETE`



Required: No




**ImportExistingResources** 


Indicates if the change set imports resources that already exist.


Type: Boolean


Required: No




**IncludeNestedStacks** 


Specifies the current setting of `IncludeNestedStacks` for the change set.


Type: Boolean


Required: No




**ParentChangeSetId** 


The parent change set ID.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`



Required: No




**RootChangeSetId** 


The root change set ID.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`



Required: No




**StackId** 


The ID of the stack with which the change set is associated.


Type: String


Required: No




**StackName** 


The name of the stack with which the change set is associated.


Type: String


Required: No




**Status** 


The state of the change set, such as `CREATE_PENDING`,
 `CREATE_COMPLETE`, or `FAILED`.


Type: String


Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_COMPLETE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED | FAILED`



Required: No




**StatusReason** 


A description of the change set's status. For example, if your change set is in the
 `FAILED` state, CloudFormation shows the error message.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ChangeSetSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ChangeSetSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ChangeSetSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ChangeSetSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ChangeSetSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ChangeSetSummary")
