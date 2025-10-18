# FieldLevelEncryptionConfig

A complex data type that includes the profile configurations specified for field-level
 encryption.


## Contents





**CallerReference** 


A unique number that ensures the request can't be replayed.


Type: String


Required: Yes




**Comment** 


An optional comment about the configuration. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**ContentTypeProfileConfig** 


A complex data type that specifies when to forward content if a content type isn't
 recognized and profiles to use as by default in a request if a query argument doesn't
 specify a profile to use.


Type: [ContentTypeProfileConfig](API_ContentTypeProfileConfig.md "API_ContentTypeProfileConfig.md") object


Required: No




**QueryArgProfileConfig** 


A complex data type that specifies when to forward content if a profile isn't found
 and the profile that can be provided as a query argument in a request.


Type: [QueryArgProfileConfig](API_QueryArgProfileConfig.md "API_QueryArgProfileConfig.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionConfig")
