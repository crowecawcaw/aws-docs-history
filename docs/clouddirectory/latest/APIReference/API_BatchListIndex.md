Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchListIndex

Lists objects attached to the specified index inside a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [ListIndex](API_ListIndex.md "API_ListIndex.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**IndexReference** 


The reference to the index to list.


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




**RangesOnIndexedValues** 


Specifies the ranges of indexed values that you want to query.


Type: Array of [ObjectAttributeRange](API_ObjectAttributeRange.md "API_ObjectAttributeRange.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListIndex "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListIndex")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListIndex "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListIndex")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListIndex "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListIndex")
