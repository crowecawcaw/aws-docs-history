# GeoRestriction

A complex type that controls the countries in which your content is distributed. CloudFront
 determines the location of your users using `MaxMind` GeoIP databases.
 


## Contents





**Quantity** 


When geo restriction is `enabled`, this is the number of countries in your
 `whitelist` or `blacklist`. Otherwise, when it is not enabled,
 `Quantity` is `0`, and you can omit `Items`.


Type: Integer


Required: Yes




**RestrictionType** 


The method that you want to use to restrict distribution of your content by country:



* `none`: No geo restriction is enabled, meaning access to content is
 not restricted by client geo location.
* `blacklist`: The `Location` elements specify the
 countries in which you don't want CloudFront to distribute your content.
* `whitelist`: The `Location` elements specify the
 countries in which you want CloudFront to distribute your content.

Type: String


Valid Values: `blacklist | whitelist | none`



Required: Yes




**Items** 


A complex type that contains a `Location` element for each country in
 which you want CloudFront either to distribute your content (`whitelist`) or not
 distribute your content (`blacklist`).


The `Location` element is a two-letter, uppercase country code for a
 country that you want to include in your `blacklist` or
 `whitelist`. Include one `Location` element for each
 country.


CloudFront and `MaxMind` both use `ISO 3166` country codes. For the
 current list of countries and the corresponding codes, see `ISO
 3166-1-alpha-2` code on the *International Organization for
 Standardization* website. You can also refer to the country list on the
 CloudFront console, which includes both country names and codes.


Type: Array of strings


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GeoRestriction "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GeoRestriction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GeoRestriction "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GeoRestriction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GeoRestriction "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GeoRestriction")
