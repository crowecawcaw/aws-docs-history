# CacheBehaviors

A complex type that contains zero or more `CacheBehavior` elements.


## Contents





**Quantity** 


The number of cache behaviors for this distribution.


Type: Integer


Required: Yes




**Items** 


Optional: A complex type that contains cache behaviors for this distribution. If
 `Quantity` is `0`, you can omit `Items`.


Type: Array of [CacheBehavior](API_CacheBehavior.md "API_CacheBehavior.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CacheBehaviors "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CacheBehaviors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CacheBehaviors "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CacheBehaviors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CacheBehaviors "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CacheBehaviors")
