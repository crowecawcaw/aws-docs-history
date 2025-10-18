Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# LinkAttributeAction

The action to take on a typed link attribute value. Updates are only supported for attributes which don’t contribute to link identity.


## Contents





**AttributeActionType** 


A type that can be either `UPDATE_OR_CREATE` or `DELETE`.


Type: String


Valid Values: `CREATE_OR_UPDATE | DELETE`



Required: No




**AttributeUpdateValue** 


The value that you want to update to.


Type: [TypedAttributeValue](API_TypedAttributeValue.md "API_TypedAttributeValue.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/LinkAttributeAction "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/LinkAttributeAction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/LinkAttributeAction "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/LinkAttributeAction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/LinkAttributeAction "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/LinkAttributeAction")
