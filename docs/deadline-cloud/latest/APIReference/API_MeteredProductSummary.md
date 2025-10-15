# MeteredProductSummary

The details of a metered product.


## Contents





**family** 


The family to which the metered product belongs.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Required: Yes




**port** 


The port on which the metered product should run.


Type: Integer


Valid Range: Minimum value of 1024. Maximum value of 65535.


Required: Yes




**productId** 


The product ID.


Type: String


Pattern: `[0-9a-z]{1,32}-[.0-9a-z]{1,32}`



Required: Yes




**vendor** 


The vendor.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/MeteredProductSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/MeteredProductSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/MeteredProductSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/MeteredProductSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/MeteredProductSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/MeteredProductSummary")
