Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchAddFacetToObject

Represents the output of a batch add facet to object operation.


## Contents





**ObjectAttributeList** 


The attributes to set on the object.


Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md "API_AttributeKeyAndValue.md") objects


Required: Yes




**ObjectReference** 


A reference to the object being mutated.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**SchemaFacet** 


Represents the facet being added to the object.


Type: [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAddFacetToObject "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAddFacetToObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAddFacetToObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAddFacetToObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAddFacetToObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAddFacetToObject")
