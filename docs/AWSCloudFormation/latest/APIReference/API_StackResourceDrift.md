# StackResourceDrift

Contains the drift information for a resource that has been checked for drift. This includes
 actual and expected property values for resources in which CloudFormation has detected drift. Only
 resource properties explicitly defined in the stack template are checked for drift. For more
 information, see [Detect unmanaged
 configuration changes to stacks and resources with drift detection](../UserGuide/using-cfn-stack-drift.md "../UserGuide/using-cfn-stack-drift.md").

Resources that don't currently support drift detection can't be checked. For a list of
 resources that support drift detection, see [Resource type
 support for imports and drift detection](../UserGuide/resource-import-supported-resources.md "../UserGuide/resource-import-supported-resources.md").

Use [DetectStackResourceDrift](API_DetectStackResourceDrift.md "API_DetectStackResourceDrift.md") to detect drift on individual resources, or
 [DetectStackDrift](API_DetectStackDrift.md "API_DetectStackDrift.md") to detect drift on all resources in a given stack that
 support drift detection.


## Contents





**LogicalResourceId** 


The logical name of the resource specified in the template.


Type: String


Required: Yes




**ResourceType** 


The type of the resource.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: Yes




**StackId** 


The ID of the stack.


Type: String


Required: Yes




**StackResourceDriftStatus** 


Status of the resource's actual configuration compared to its expected configuration.



* `DELETED`: The resource differs from its expected template configuration
 because the resource has been deleted.
* `MODIFIED`: One or more resource properties differ from their expected values
 (as defined in the stack template and any values specified as template parameters).
* `IN_SYNC`: The resource's actual configuration matches its expected template
 configuration.
* `NOT_CHECKED`: CloudFormation does not currently return this value.
* `UNKNOWN`: CloudFormation could not run drift detection for the resource. See the
 `DriftStatusReason` for details.

Type: String


Valid Values: `IN_SYNC | MODIFIED | DELETED | NOT_CHECKED | UNKNOWN`



Required: Yes




**Timestamp** 


Time at which CloudFormation performed drift detection on the stack resource.


Type: Timestamp


Required: Yes




**ActualProperties** 


A JSON structure that contains the actual property values of the stack resource.


For resources whose `StackResourceDriftStatus` is `DELETED`, this
 structure will not be present.


Type: String


Required: No




**DriftStatusReason** 


The reason for the drift status. 


Type: String


Required: No




**ExpectedProperties** 


A JSON structure that contains the expected property values of the stack resource, as
 defined in the stack template and any values specified as template parameters.


For resources whose `StackResourceDriftStatus` is `DELETED`, this
 structure will not be present.


Type: String


Required: No




**ModuleInfo** 


Contains information about the module from which the resource was created, if the resource
 was created from a module included in the stack template.


Type: [ModuleInfo](API_ModuleInfo.md "API_ModuleInfo.md") object


Required: No




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


A collection of the resource properties whose actual values differ from their expected
 values. These will be present only for resources whose `StackResourceDriftStatus` is
 `MODIFIED`.


Type: Array of [PropertyDifference](API_PropertyDifference.md "API_PropertyDifference.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackResourceDrift "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackResourceDrift")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackResourceDrift "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackResourceDrift")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackResourceDrift "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackResourceDrift")
