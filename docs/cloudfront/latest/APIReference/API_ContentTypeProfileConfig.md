# ContentTypeProfileConfig

The configuration for a field-level encryption content type-profile mapping.


## Contents





**ForwardWhenContentTypeIsUnknown** 


The setting in a field-level encryption content type-profile mapping that specifies
 what to do when an unknown content type is provided for the profile. If true, content is
 forwarded without being encrypted when the content type is unknown. If false (the
 default), an error is returned when the content type is unknown.


Type: Boolean


Required: Yes




**ContentTypeProfiles** 


The configuration for a field-level encryption content type-profile.


Type: [ContentTypeProfiles](API_ContentTypeProfiles.md "API_ContentTypeProfiles.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContentTypeProfileConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContentTypeProfileConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContentTypeProfileConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContentTypeProfileConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContentTypeProfileConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContentTypeProfileConfig")
