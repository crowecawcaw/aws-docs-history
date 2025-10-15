# PropertyDifference

Information about a resource property whose actual value differs from its expected value, as
 defined in the stack template and any values specified as template parameters. These will be
 present only for resources whose `StackResourceDriftStatus` is `MODIFIED`.
 For more information, see [Detect unmanaged
 configuration changes to stacks and resources with drift detection](../UserGuide/using-cfn-stack-drift.md "../UserGuide/using-cfn-stack-drift.md").


## Contents





**ActualValue** 


The actual property value of the resource property.


Type: String


Required: Yes




**DifferenceType** 


The type of property difference.



* `ADD`: A value has been added to a resource property that's an array or list
 data type.
* `REMOVE`: The property has been removed from the current resource
 configuration.
* `NOT_EQUAL`: The current property value differs from its expected value (as
 defined in the stack template and any values specified as template parameters).

Type: String


Valid Values: `ADD | REMOVE | NOT_EQUAL`



Required: Yes




**ExpectedValue** 


The expected property value of the resource property, as defined in the stack template and
 any values specified as template parameters.


Type: String


Required: Yes




**PropertyPath** 


The fully-qualified path to the resource property.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/PropertyDifference "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/PropertyDifference")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/PropertyDifference "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/PropertyDifference")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/PropertyDifference "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/PropertyDifference")
