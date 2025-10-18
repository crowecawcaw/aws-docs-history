Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchGetLinkAttributes

Retrieves attributes that are associated with a typed link inside a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [GetLinkAttributes](API_GetLinkAttributes.md "API_GetLinkAttributes.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**AttributeNames** 


A list of attribute names whose values will be retrieved.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 230.


Pattern: `^[a-zA-Z0-9._:-]*$`



Required: Yes




**TypedLinkSpecifier** 


Allows a typed link specifier to be accepted as input.


Type: [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchGetLinkAttributes "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchGetLinkAttributes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchGetLinkAttributes "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchGetLinkAttributes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchGetLinkAttributes "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchGetLinkAttributes")
