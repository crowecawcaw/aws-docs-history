# StackInstanceResourceDriftsSummary

The structure containing summary information about resource drifts for a stack
 instance.


## Contents





**LogicalResourceId** 


The logical name of the resource specified in the template.


Type: String


Required: Yes




**ResourceType** 


Type of resource. For more information, see [AWS resource and
 property types reference](../UserGuide/aws-template-resource-type-ref.md "../UserGuide/aws-template-resource-type-ref.md") in the *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: Yes




**StackId** 


The ID of the stack instance.


Type: String


Required: Yes




**StackResourceDriftStatus** 


The drift status of the resource in a stack instance.



* `DELETED`: The resource differs from its expected template configuration in
 that the resource has been deleted.
* `MODIFIED`: One or more resource properties differ from their expected template
 values.
* `IN_SYNC`: The resource's actual configuration matches its expected template
 configuration.
* `NOT_CHECKED`: CloudFormation doesn't currently return this value.

Type: String


Valid Values: `IN_SYNC | MODIFIED | DELETED | NOT_CHECKED | UNKNOWN`



Required: Yes




**Timestamp** 


Time at which the stack instance drift detection operation was initiated.


Type: Timestamp


Required: Yes




**PhysicalResourceId** 


The name or unique identifier that corresponds to a physical instance ID of a resource
 supported by CloudFormation.


Type: String


Required: No




**PhysicalResourceIdContext.member.N** 


Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses
 context key-value pairs in cases where a resource's logical and physical IDs aren't enough to
 uniquely identify that resource. Each context key-value pair specifies a unique resource that
 contains the targeted resource.


Type: Array of [PhysicalResourceIdContextKeyValuePair](API_PhysicalResourceIdContextKeyValuePair.md "API_PhysicalResourceIdContextKeyValuePair.md") objects


Array Members: Maximum number of 5 items.


Required: No




**PropertyDifferences.member.N** 


Status of the actual configuration of the resource compared to its expected configuration.
 These will be present only for resources whose `StackInstanceResourceDriftStatus` is
 `MODIFIED`. 


Type: Array of [PropertyDifference](API_PropertyDifference.md "API_PropertyDifference.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackInstanceResourceDriftsSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackInstanceResourceDriftsSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackInstanceResourceDriftsSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackInstanceResourceDriftsSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackInstanceResourceDriftsSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackInstanceResourceDriftsSummary")
