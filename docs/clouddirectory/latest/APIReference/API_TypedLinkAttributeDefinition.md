Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# TypedLinkAttributeDefinition

A typed link attribute definition.


## Contents





**Name** 


The unique name of the typed link attribute.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 230.


Pattern: `^[a-zA-Z0-9._:-]*$`



Required: Yes




**RequiredBehavior** 


The required behavior of the `TypedLinkAttributeDefinition`.


Type: String


Valid Values: `REQUIRED_ALWAYS | NOT_REQUIRED`



Required: Yes




**Type** 


The type of the attribute.


Type: String


Valid Values: `STRING | BINARY | BOOLEAN | NUMBER | DATETIME | VARIANT`



Required: Yes




**DefaultValue** 


The default value of the attribute (if configured).


Type: [TypedAttributeValue](API_TypedAttributeValue.md "API_TypedAttributeValue.md") object


Required: No




**IsImmutable** 


Whether the attribute is mutable or not.


Type: Boolean


Required: No




**Rules** 


Validation rules that are attached to the attribute definition.


Type: String to [Rule](API_Rule.md "API_Rule.md") object map


Key Length Constraints: Minimum length of 1. Maximum length of 64.


Key Pattern: `^[a-zA-Z0-9._-]*$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkAttributeDefinition "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkAttributeDefinition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkAttributeDefinition "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkAttributeDefinition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkAttributeDefinition "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkAttributeDefinition")
