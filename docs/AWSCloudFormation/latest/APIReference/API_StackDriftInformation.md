# StackDriftInformation

Contains information about whether the stack's actual configuration differs, or has
 *drifted*, from its expected configuration, as defined in the stack template
 and any values specified as template parameters. A stack is considered to have drifted if one or
 more of its resources have drifted.


## Contents





**StackDriftStatus** 


Status of the stack's actual configuration compared to its expected template
 configuration.



* `DRIFTED`: The stack differs from its expected template configuration. A stack
 is considered to have drifted if one or more of its resources have drifted.
* `NOT_CHECKED`: CloudFormation hasn't checked if the stack differs from its expected
 template configuration.
* `IN_SYNC`: The stack's actual configuration matches its expected template
 configuration.
* `UNKNOWN`: CloudFormation could not run drift detection for a resource in the
 stack.

Type: String


Valid Values: `DRIFTED | IN_SYNC | UNKNOWN | NOT_CHECKED`



Required: Yes




**LastCheckTimestamp** 


Most recent time when a drift detection operation was initiated on the stack, or any of its
 individual resources that support drift detection.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackDriftInformation "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackDriftInformation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackDriftInformation "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackDriftInformation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackDriftInformation "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackDriftInformation")
