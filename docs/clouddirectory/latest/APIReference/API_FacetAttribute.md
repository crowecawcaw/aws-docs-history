Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# FacetAttribute

An attribute that is associated with the [Facet](API_Facet.md "API_Facet.md").


## Contents





**Name** 


The name of the facet attribute.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 230.


Pattern: `^[a-zA-Z0-9._:-]*$`



Required: Yes




**AttributeDefinition** 


A facet attribute consists of either a definition or a reference. This structure
 contains the attribute definition. See [Attribute References](../developerguide/schemas_attributereferences.md "../developerguide/schemas_attributereferences.md") for more information.


Type: [FacetAttributeDefinition](API_FacetAttributeDefinition.md "API_FacetAttributeDefinition.md") object


Required: No




**AttributeReference** 


An attribute reference that is associated with the attribute. See [Attribute References](../developerguide/schemas_attributereferences.md "../developerguide/schemas_attributereferences.md") for more information.


Type: [FacetAttributeReference](API_FacetAttributeReference.md "API_FacetAttributeReference.md") object


Required: No




**RequiredBehavior** 


The required behavior of the `FacetAttribute`.


Type: String


Valid Values: `REQUIRED_ALWAYS | NOT_REQUIRED`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/FacetAttribute "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/FacetAttribute")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/FacetAttribute "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/FacetAttribute")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/FacetAttribute "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/FacetAttribute")
