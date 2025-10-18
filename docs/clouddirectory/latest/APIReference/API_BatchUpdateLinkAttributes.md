Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchUpdateLinkAttributes

Updates a given typed link’s attributes inside a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. Attributes to be updated must not contribute to the typed link’s identity, as defined by its `IdentityAttributeOrder`. For more information, see [UpdateLinkAttributes](API_UpdateLinkAttributes.md "API_UpdateLinkAttributes.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**AttributeUpdates** 


The attributes update structure.


Type: Array of [LinkAttributeUpdate](API_LinkAttributeUpdate.md "API_LinkAttributeUpdate.md") objects


Required: Yes




**TypedLinkSpecifier** 


Allows a typed link specifier to be accepted as input.


Type: [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchUpdateLinkAttributes "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchUpdateLinkAttributes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchUpdateLinkAttributes "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchUpdateLinkAttributes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchUpdateLinkAttributes "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchUpdateLinkAttributes")
