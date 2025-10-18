# EncryptionEntity

Complex data type for field-level encryption profiles that includes the encryption key
 and field pattern specifications.


## Contents





**FieldPatterns** 


Field patterns in a field-level encryption content type profile specify the fields
 that you want to be encrypted. You can provide the full field name, or any beginning
 characters followed by a wildcard (\*). You can't overlap field patterns. For example,
 you can't have both ABC\* and AB\*. Note that field patterns are case-sensitive.


Type: [FieldPatterns](API_FieldPatterns.md "API_FieldPatterns.md") object


Required: Yes




**ProviderId** 


The provider associated with the public key being used for encryption. This value must
 also be provided with the private key for applications to be able to decrypt
 data.


Type: String


Required: Yes




**PublicKeyId** 


The public key associated with a set of field-level encryption patterns, to be used
 when encrypting the fields that match the patterns.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/EncryptionEntity "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/EncryptionEntity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/EncryptionEntity "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/EncryptionEntity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/EncryptionEntity "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/EncryptionEntity")
