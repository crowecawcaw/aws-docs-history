Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchCreateIndex

Creates an index object inside of a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [CreateIndex](API_CreateIndex.md "API_CreateIndex.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**IsUnique** 


Indicates whether the attribute that is being indexed has unique values or
 not.


Type: Boolean


Required: Yes




**OrderedIndexedAttributeList** 


Specifies the attributes that should be indexed on. Currently only a single attribute
 is supported.


Type: Array of [AttributeKey](API_AttributeKey.md "API_AttributeKey.md") objects


Required: Yes




**BatchReferenceName** 


The batch reference name. See [Transaction Support](../developerguide/transaction_support.md "../developerguide/transaction_support.md") for more information.


Type: String


Required: No




**LinkName** 


The name of the link between the parent object and the index object.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`



Required: No




**ParentReference** 


A reference to the parent object that contains the index object.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchCreateIndex "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchCreateIndex")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchCreateIndex "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchCreateIndex")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchCreateIndex "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchCreateIndex")
