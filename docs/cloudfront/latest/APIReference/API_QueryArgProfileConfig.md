# QueryArgProfileConfig

Configuration for query argument-profile mapping for field-level encryption.


## Contents





**ForwardWhenQueryArgProfileIsUnknown** 


Flag to set if you want a request to be forwarded to the origin even if the profile
 specified by the field-level encryption query argument, fle-profile, is unknown.


Type: Boolean


Required: Yes




**QueryArgProfiles** 


Profiles specified for query argument-profile mapping for field-level
 encryption.


Type: [QueryArgProfiles](API_QueryArgProfiles.md "API_QueryArgProfiles.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/QueryArgProfileConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/QueryArgProfileConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/QueryArgProfileConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/QueryArgProfileConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/QueryArgProfileConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/QueryArgProfileConfig")
