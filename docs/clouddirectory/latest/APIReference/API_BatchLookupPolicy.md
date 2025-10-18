Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchLookupPolicy

Lists all policies from the root of the Directory to the object specified inside a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [LookupPolicy](API_LookupPolicy.md "API_LookupPolicy.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**ObjectReference** 


Reference that identifies the object whose policies will be looked up.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**MaxResults** 


The maximum number of results to retrieve.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**NextToken** 


The pagination token.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchLookupPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchLookupPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchLookupPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchLookupPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchLookupPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchLookupPolicy")
