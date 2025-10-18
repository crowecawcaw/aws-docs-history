# GeoRestrictionCustomization

The customizations that you specified for the distribution tenant for geographic restrictions.


## Contents





**RestrictionType** 


The method that you want to use to restrict distribution of your content by
 country:



* `none`: No geographic restriction is enabled, meaning access to content is
 not restricted by client geo location.
* `blacklist`: The `Location` elements specify the
 countries in which you don't want CloudFront to distribute your content.
* `whitelist`: The `Location` elements specify the
 countries in which you want CloudFront to distribute your content.

Type: String


Valid Values: `blacklist | whitelist | none`



Required: Yes




**Locations** 


The locations for geographic restrictions.


Type: Array of strings


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GeoRestrictionCustomization "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GeoRestrictionCustomization")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GeoRestrictionCustomization "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GeoRestrictionCustomization")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GeoRestrictionCustomization "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GeoRestrictionCustomization")
