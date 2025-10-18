Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# PolicyToPath

Used when a regular object exists in a [Directory](API_Directory.md "API_Directory.md") and you want to find
 all of the policies that are associated with that object and the parent to that
 object.


## Contents





**Path** 


The path that is referenced from the root.


Type: String


Required: No




**Policies** 


List of policy objects.


Type: Array of [PolicyAttachment](API_PolicyAttachment.md "API_PolicyAttachment.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/PolicyToPath "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/PolicyToPath")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/PolicyToPath "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/PolicyToPath")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/PolicyToPath "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/PolicyToPath")
