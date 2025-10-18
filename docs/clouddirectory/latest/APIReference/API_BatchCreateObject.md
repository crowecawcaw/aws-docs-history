Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchCreateObject

Represents the output of a [CreateObject](API_CreateObject.md "API_CreateObject.md") operation.


## Contents





**ObjectAttributeList** 


An attribute map, which contains an attribute ARN as the key and attribute value as
 the map value.


Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md "API_AttributeKeyAndValue.md") objects


Required: Yes




**SchemaFacet** 


A list of `FacetArns` that will be associated with the object. For more
 information, see [Arn Examples](arns.md "arns.md").


Type: Array of [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") objects


Required: Yes




**BatchReferenceName** 


The batch reference name. See [Transaction Support](../developerguide/transaction_support.md "../developerguide/transaction_support.md") for more information.


Type: String


Required: No




**LinkName** 


The name of the link.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`



Required: No




**ParentReference** 


If specified, the parent reference to which this object will be attached.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchCreateObject "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchCreateObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchCreateObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchCreateObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchCreateObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchCreateObject")
