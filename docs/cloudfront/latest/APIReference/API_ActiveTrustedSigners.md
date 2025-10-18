# ActiveTrustedSigners

A list of AWS accounts and the active CloudFront key pairs in each account that CloudFront can
 use to verify the signatures of signed URLs and signed cookies.


## Contents





**Enabled** 


This field is `true` if any of the AWS accounts in the list are configured as
 trusted signers. If not, this field is `false`.


Type: Boolean


Required: Yes




**Quantity** 


The number of AWS accounts in the list.


Type: Integer


Required: Yes




**Items** 


A list of AWS accounts and the identifiers of active CloudFront key pairs in each account
 that CloudFront can use to verify the signatures of signed URLs and signed cookies.


Type: Array of [Signer](API_Signer.md "API_Signer.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ActiveTrustedSigners "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ActiveTrustedSigners")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ActiveTrustedSigners "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ActiveTrustedSigners")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ActiveTrustedSigners "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ActiveTrustedSigners")
