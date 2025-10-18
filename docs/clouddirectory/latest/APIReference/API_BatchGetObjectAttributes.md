Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchGetObjectAttributes

Retrieves attributes within a facet that are associated with an object inside an [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [GetObjectAttributes](API_GetObjectAttributes.md "API_GetObjectAttributes.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**AttributeNames** 


List of attribute names whose values will be retrieved.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 230.


Pattern: `^[a-zA-Z0-9._:-]*$`



Required: Yes




**ObjectReference** 


Reference that identifies the object whose attributes will be retrieved.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**SchemaFacet** 


Identifier for the facet whose attributes will be retrieved. See [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") for details.


Type: [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchGetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchGetObjectAttributes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchGetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchGetObjectAttributes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchGetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchGetObjectAttributes")
