# FleetAttributeCapability

Defines the fleet's capability name, minimum, and maximum.


## Contents





**name** 


The name of the fleet attribute capability for the worker.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Pattern: `([a-zA-Z][a-zA-Z0-9]{0,63}:)?attr(\.[a-zA-Z][a-zA-Z0-9]{0,63})+`



Required: Yes




**values** 


The number of fleet attribute capabilities.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Length Constraints: Minimum length of 1. Maximum length of 100.


Pattern: `[a-zA-Z_]([a-zA-Z0-9_\-]{0,99})`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FleetAttributeCapability "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FleetAttributeCapability")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FleetAttributeCapability "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FleetAttributeCapability")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FleetAttributeCapability "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FleetAttributeCapability")
