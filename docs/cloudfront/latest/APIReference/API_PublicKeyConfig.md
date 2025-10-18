# PublicKeyConfig

Configuration information about a public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").

CloudFront supports signed URLs and signed cookies with RSA 2048 or ECDSA 256 key signatures. Field-level encryption is only compatible with RSA 2048 key signatures.


## Contents





**CallerReference** 


A string included in the request to help make sure that the request can't be
 replayed.


Type: String


Required: Yes




**EncodedKey** 


The public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


Type: String


Required: Yes




**Name** 


A name to help identify the public key.


Type: String


Required: Yes




**Comment** 


A comment to describe the public key. The comment cannot be longer than 128
 characters.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKeyConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKeyConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKeyConfig")
