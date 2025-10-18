# ActiveTrustedKeyGroups

A list of key groups, and the public keys in each key group, that CloudFront can use to
 verify the signatures of signed URLs and signed cookies.


## Contents





**Enabled** 


This field is `true` if any of the key groups have public keys that CloudFront
 can use to verify the signatures of signed URLs and signed cookies. If not, this field
 is `false`.


Type: Boolean


Required: Yes




**Quantity** 


The number of key groups in the list.


Type: Integer


Required: Yes




**Items** 


A list of key groups, including the identifiers of the public keys in each key group
 that CloudFront can use to verify the signatures of signed URLs and signed cookies.


Type: Array of [KGKeyPairIds](API_KGKeyPairIds.md "API_KGKeyPairIds.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ActiveTrustedKeyGroups "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ActiveTrustedKeyGroups")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ActiveTrustedKeyGroups "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ActiveTrustedKeyGroups")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ActiveTrustedKeyGroups "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ActiveTrustedKeyGroups")
