# StackSetSummary

The structures that contain summary information about the specified StackSet.


## Contents





**AutoDeployment** 


[Service-managed permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organizational unit (OU).


Type: [AutoDeployment](API_AutoDeployment.md "API_AutoDeployment.md") object


Required: No




**Description** 


A description of the StackSet that you specify when the StackSet is created or
 updated.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**DriftStatus** 


Status of the StackSet's actual configuration compared to its expected template and
 parameter configuration.



* `DRIFTED`: One or more of the stack instances belonging to the StackSet differs
 from the expected template and parameter configuration. A stack instance is considered to have
 drifted if one or more of the resources in the associated stack have drifted.
* `NOT_CHECKED`: CloudFormation hasn't checked the StackSet for drift.
* `IN_SYNC`: All the stack instances belonging to the StackSet match the expected
 template and parameter configuration.
* `UNKNOWN`: This value is reserved for future use.

Type: String


Valid Values: `DRIFTED | IN_SYNC | UNKNOWN | NOT_CHECKED`



Required: No




**LastDriftCheckTimestamp** 


Most recent time when CloudFormation performed a drift detection operation on the StackSet. This
 value will be `NULL` for any StackSet that drift detection hasn't yet been performed
 on.


Type: Timestamp


Required: No




**ManagedExecution** 


Describes whether StackSets performs non-conflicting operations concurrently and queues
 conflicting operations.


Type: [ManagedExecution](API_ManagedExecution.md "API_ManagedExecution.md") object


Required: No




**PermissionModel** 


Describes how the IAM roles required for StackSet operations are created.



* With `self-managed` permissions, you must create the administrator and
 execution roles required to deploy to target accounts. For more information, see [Grant
 self-managed permissions](../UserGuide/stacksets-prereqs-self-managed.md "../UserGuide/stacksets-prereqs-self-managed.md").
* With `service-managed` permissions, StackSets automatically creates the IAM
 roles required to deploy to accounts managed by AWS Organizations. For more information,
 see [Activate
 trusted access for StackSets with AWS Organizations](../UserGuide/stacksets-orgs-activate-trusted-access.md "../UserGuide/stacksets-orgs-activate-trusted-access.md").

Type: String


Valid Values: `SERVICE_MANAGED | SELF_MANAGED`



Required: No




**StackSetId** 


The ID of the StackSet.


Type: String


Required: No




**StackSetName** 


The name of the StackSet.


Type: String


Required: No




**Status** 


The status of the StackSet.


Type: String


Valid Values: `ACTIVE | DELETED`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetSummary")
