# ResourceTargetDefinition

The field that CloudFormation will change, such as the name of a resource's property, and
 whether the resource will be recreated.


## Contents





**AfterValue** 


The value of the property after the change is executed. Large values can be
 truncated.


Type: String


Required: No




**Attribute** 


Indicates which resource attribute is triggering this update, such as a change in the
 resource attribute's `Metadata`, `Properties`, or `Tags`.


Type: String


Valid Values: `Properties | Metadata | CreationPolicy | UpdatePolicy | DeletionPolicy | UpdateReplacePolicy | Tags`



Required: No




**AttributeChangeType** 


The type of change to be made to the property if the change is executed.



* `Add` The item will be added.
* `Remove` The item will be removed.
* `Modify` The item will be modified.

Type: String


Valid Values: `Add | Remove | Modify`



Required: No




**BeforeValue** 


The value of the property before the change is executed. Large values can be
 truncated.


Type: String


Required: No




**Name** 


If the `Attribute` value is `Properties`, the name of the property.
 For all other attributes, the value is null.


Type: String


Required: No




**Path** 


The property path of the property.


Type: String


Required: No




**RequiresRecreation** 


If the `Attribute` value is `Properties`, indicates whether a change
 to this property causes the resource to be recreated. The value can be `Never`,
 `Always`, or `Conditionally`. To determine the conditions for a
 `Conditionally` recreation, see the update behavior for that property in the [AWS resource and
 property types reference](../UserGuide/aws-template-resource-type-ref.md "../UserGuide/aws-template-resource-type-ref.md") in the *AWS CloudFormation User Guide*.


Type: String


Valid Values: `Never | Conditionally | Always`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceTargetDefinition "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceTargetDefinition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceTargetDefinition "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceTargetDefinition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceTargetDefinition "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceTargetDefinition")
