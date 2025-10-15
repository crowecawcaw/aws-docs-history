# WorkerAttributeCapability

The details of the worker attribute capability.


## Contents





**name** 


The name of the worker attribute capability.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Pattern: `([a-zA-Z][a-zA-Z0-9]{0,63}:)?attr(\.[a-zA-Z][a-zA-Z0-9]{0,63})+`



Required: Yes




**values** 


The values of the worker amount capability.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Length Constraints: Minimum length of 1. Maximum length of 100.


Pattern: `[a-zA-Z_]([a-zA-Z0-9_\-]{0,99})`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerAttributeCapability "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerAttributeCapability")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerAttributeCapability "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerAttributeCapability")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerAttributeCapability "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerAttributeCapability")
