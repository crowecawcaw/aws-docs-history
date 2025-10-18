Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchDetachPolicy

Detaches the specified policy from the specified directory inside a [BatchWrite](API_BatchWrite.md "API_BatchWrite.md") operation. For more information, see [DetachPolicy](API_DetachPolicy.md "API_DetachPolicy.md") and [BatchWrite:Operations](API_BatchWrite.md#amazoncds-BatchWrite-request-Operations "API_BatchWrite.md#amazoncds-BatchWrite-request-Operations").


## Contents





**ObjectReference** 


Reference that identifies the object whose policy object will be detached.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**PolicyReference** 


Reference that identifies the policy object.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchDetachPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchDetachPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchDetachPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchDetachPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchDetachPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchDetachPolicy")
