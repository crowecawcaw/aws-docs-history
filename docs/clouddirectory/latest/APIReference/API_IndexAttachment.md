Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# IndexAttachment

Represents an index and an attached object.


## Contents





**IndexedAttributes** 


The indexed attribute values.


Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md "API_AttributeKeyAndValue.md") objects


Required: No




**ObjectIdentifier** 


In response to [ListIndex](API_ListIndex.md "API_ListIndex.md"), the `ObjectIdentifier` of the object attached to the index. In response to [ListAttachedIndices](API_ListAttachedIndices.md "API_ListAttachedIndices.md"), the `ObjectIdentifier` of the index attached to the object. This field will always contain the `ObjectIdentifier` of the object on the opposite side of the attachment specified in the query.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/IndexAttachment "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/IndexAttachment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/IndexAttachment "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/IndexAttachment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/IndexAttachment "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/IndexAttachment")
