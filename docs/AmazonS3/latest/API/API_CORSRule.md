# CORSRule

Specifies a cross-origin access rule for an Amazon S3 bucket.


## Contents





**AllowedMethods** 


An HTTP method that you allow the origin to execute. Valid values are `GET`,
 `PUT`, `HEAD`, `POST`, and `DELETE`.


Type: Array of strings


Required: Yes




**AllowedOrigins** 


One or more origins you want customers to be able to access the bucket from.


Type: Array of strings


Required: Yes




**AllowedHeaders** 


Headers that are specified in the `Access-Control-Request-Headers` header. These headers
 are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request, Amazon S3 returns
 any requested headers that are allowed.


Type: Array of strings


Required: No




**ExposeHeaders** 


One or more headers in the response that you want customers to be able to access from their
 applications (for example, from a JavaScript `XMLHttpRequest` object).


Type: Array of strings


Required: No




**ID** 


Unique identifier for the rule. The value cannot be longer than 255 characters.


Type: String


Required: No




**MaxAgeSeconds** 


The time in seconds that your browser is to cache the preflight response for the specified
 resource.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CORSRule "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CORSRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CORSRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CORSRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CORSRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CORSRule")
