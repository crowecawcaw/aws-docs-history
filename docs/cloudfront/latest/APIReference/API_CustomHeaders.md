# CustomHeaders

A complex type that contains the list of Custom Headers for each origin.


## Contents





**Quantity** 


The number of custom headers, if any, for this distribution.


Type: Integer


Required: Yes




**Items** 



**Optional**: A list that contains one
 `OriginCustomHeader` element for each custom header that you want CloudFront to
 forward to the origin. If Quantity is `0`, omit `Items`.


Type: Array of [OriginCustomHeader](API_OriginCustomHeader.md "API_OriginCustomHeader.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CustomHeaders "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CustomHeaders")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CustomHeaders "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CustomHeaders")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CustomHeaders "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CustomHeaders")
