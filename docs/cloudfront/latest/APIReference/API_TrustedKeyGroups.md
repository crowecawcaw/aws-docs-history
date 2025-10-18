# TrustedKeyGroups

A list of key groups whose public keys CloudFront can use to verify the signatures of signed
 URLs and signed cookies.


## Contents





**Enabled** 


This field is `true` if any of the key groups in the list have public keys
 that CloudFront can use to verify the signatures of signed URLs and signed cookies. If not,
 this field is `false`.


Type: Boolean


Required: Yes




**Quantity** 


The number of key groups in the list.


Type: Integer


Required: Yes




**Items** 


A list of key groups identifiers.


Type: Array of strings


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TrustedKeyGroups "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TrustedKeyGroups")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TrustedKeyGroups "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TrustedKeyGroups")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TrustedKeyGroups "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TrustedKeyGroups")
