# WarningDetail

The warnings generated for a specific resource for this generated template.


## Contents





**Properties.member.N** 


The properties of the resource that are impacted by this warning.


Type: Array of [WarningProperty](API_WarningProperty.md "API_WarningProperty.md") objects


Required: No




**Type** 


The type of this warning. For more information, see [Resolve
 write-only properties](../UserGuide/generate-IaC-write-only-properties.md "../UserGuide/generate-IaC-write-only-properties.md") in the *AWS CloudFormation User Guide*.



* `MUTUALLY_EXCLUSIVE_PROPERTIES` - The resource requires mutually-exclusive
 write-only properties. The IaC generator selects one set of mutually exclusive properties and
 converts the included properties into parameters. The parameter names have a suffix
 `OneOf` and the parameter descriptions indicate that the corresponding property can
 be replaced with other exclusive properties.
* `UNSUPPORTED_PROPERTIES` - Unsupported properties are present in the resource.
 One example of unsupported properties would be a required write-only property that is an array,
 because a parameter cannot be an array. Another example is an optional write-only
 property.
* `MUTUALLY_EXCLUSIVE_TYPES` - One or more required write-only properties are
 found in the resource, and the type of that property can be any of several types.

###### Note

Currently the resource and property reference documentation does not indicate if a property
 uses a type of `oneOf` or `anyOf`. You need to look at the resource
 provider schema.


Type: String


Valid Values: `MUTUALLY_EXCLUSIVE_PROPERTIES | UNSUPPORTED_PROPERTIES | MUTUALLY_EXCLUSIVE_TYPES | EXCLUDED_PROPERTIES`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/WarningDetail "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/WarningDetail")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/WarningDetail "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/WarningDetail")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/WarningDetail "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/WarningDetail")
