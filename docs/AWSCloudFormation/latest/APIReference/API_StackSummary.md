# StackSummary

The StackSummary Data Type


## Contents





**CreationTime** 


The time the stack was created.


Type: Timestamp


Required: Yes




**StackName** 


The name associated with the stack.


Type: String


Required: Yes




**StackStatus** 


The current status of the stack.


Type: String


Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE | ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_COMPLETE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE_CLEANUP_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | UPDATE_ROLLBACK_IN_PROGRESS | UPDATE_ROLLBACK_FAILED | UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS | UPDATE_ROLLBACK_COMPLETE | REVIEW_IN_PROGRESS | IMPORT_IN_PROGRESS | IMPORT_COMPLETE | IMPORT_ROLLBACK_IN_PROGRESS | IMPORT_ROLLBACK_FAILED | IMPORT_ROLLBACK_COMPLETE`



Required: Yes




**DeletionTime** 


The time the stack was deleted.


Type: Timestamp


Required: No




**DriftInformation** 


Summarizes information about whether a stack's actual configuration differs, or has
 *drifted*, from its expected configuration, as defined in the stack template
 and any values specified as template parameters. For more information, see [Detect
 unmanaged configuration changes to stacks and resources with drift detection](../UserGuide/using-cfn-stack-drift.md "../UserGuide/using-cfn-stack-drift.md").


Type: [StackDriftInformationSummary](API_StackDriftInformationSummary.md "API_StackDriftInformationSummary.md") object


Required: No




**LastUpdatedTime** 


The time the stack was last updated. This field will only be returned if the stack has been
 updated at least once.


Type: Timestamp


Required: No




**ParentId** 


For nested stacks, the stack ID of the direct parent of this stack. For the first level of
 nested stacks, the root stack is also the parent stack.


For more information, see [Nested stacks](../UserGuide/using-cfn-nested-stacks.md "../UserGuide/using-cfn-nested-stacks.md") in
 the *AWS CloudFormation User Guide*.


Type: String


Required: No




**RootId** 


For nested stacks, the stack ID of the top-level stack to which the nested stack ultimately
 belongs.


For more information, see [Nested stacks](../UserGuide/using-cfn-nested-stacks.md "../UserGuide/using-cfn-nested-stacks.md") in
 the *AWS CloudFormation User Guide*.


Type: String


Required: No




**StackId** 


Unique stack identifier.


Type: String


Required: No




**StackStatusReason** 


Success/Failure message associated with the stack status.


Type: String


Required: No




**TemplateDescription** 


The template description of the template used to create the stack.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSummary")
