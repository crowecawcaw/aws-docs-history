Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# FacetAttributeReference

The facet attribute reference that specifies the attribute definition that contains the
 attribute facet name and attribute name.


## Contents





**TargetAttributeName** 


The target attribute name that is associated with the facet reference. See [Attribute References](../developerguide/schemas_attributereferences.md "../developerguide/schemas_attributereferences.md") for more information.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 230.


Pattern: `^[a-zA-Z0-9._:-]*$`



Required: Yes




**TargetFacetName** 


The target facet name that is associated with the facet reference. See [Attribute References](../developerguide/schemas_attributereferences.md "../developerguide/schemas_attributereferences.md") for more information.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `^[a-zA-Z0-9._-]*$`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/FacetAttributeReference "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/FacetAttributeReference")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/FacetAttributeReference "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/FacetAttributeReference")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/FacetAttributeReference "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/FacetAttributeReference")
