# PublicKey

A public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").

CloudFront supports signed URLs and signed cookies with RSA 2048 or ECDSA 256 key signatures. Field-level encryption is only compatible with RSA 2048 key signatures.


## Contents





**CreatedTime** 


The date and time when the public key was uploaded.


Type: Timestamp


Required: Yes




**Id** 


The identifier of the public key.


Type: String


Required: Yes




**PublicKeyConfig** 


Configuration information about a public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


Type: [PublicKeyConfig](API_PublicKeyConfig.md "API_PublicKeyConfig.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKey "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKey")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKey "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKey")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKey "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKey")
