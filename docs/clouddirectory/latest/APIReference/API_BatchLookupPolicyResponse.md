Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchLookupPolicyResponse

Represents the output of a [LookupPolicy](API_LookupPolicy.md "API_LookupPolicy.md") response operation.


## Contents





**NextToken** 


The pagination token.


Type: String


Required: No




**PolicyToPathList** 


Provides list of path to policies. Policies contain `PolicyId`, `ObjectIdentifier`, and
 `PolicyType`. For more
 information, see [Policies](../developerguide/key_concepts_directory.md#key_concepts_policies "../developerguide/key_concepts_directory.md#key_concepts_policies").


Type: Array of [PolicyToPath](API_PolicyToPath.md "API_PolicyToPath.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchLookupPolicyResponse "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchLookupPolicyResponse")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchLookupPolicyResponse "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchLookupPolicyResponse")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchLookupPolicyResponse "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchLookupPolicyResponse")
