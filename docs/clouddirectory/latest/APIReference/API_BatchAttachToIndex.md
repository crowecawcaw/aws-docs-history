Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchAttachToIndex

Attaches the specified object to the specified index inside a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [AttachToIndex](API_AttachToIndex.md "API_AttachToIndex.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**IndexReference** 


A reference to the index that you are attaching the object to.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**TargetReference** 


A reference to the object that you are attaching to the index.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachToIndex "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachToIndex")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachToIndex "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachToIndex")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachToIndex "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachToIndex")
