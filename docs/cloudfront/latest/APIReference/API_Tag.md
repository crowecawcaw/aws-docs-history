# Tag

A complex type that contains `Tag` key and `Tag` value.


## Contents





**Key** 


A string that contains `Tag` key.


The string length should be between 1 and 128 characters. Valid characters include
 `a-z`, `A-Z`, `0-9`, space, and the special
 characters `_ - . : / = + @`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`



Required: Yes




**Value** 


A string that contains an optional `Tag` value.


The string length should be between 0 and 256 characters. Valid characters include
 `a-z`, `A-Z`, `0-9`, space, and the special
 characters `_ - . : / = + @`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Tag "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Tag")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Tag "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Tag")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Tag "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Tag")
