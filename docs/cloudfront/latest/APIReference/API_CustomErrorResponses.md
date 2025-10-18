# CustomErrorResponses

A complex type that controls:


* Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom
 error messages before returning the response to the viewer.
* How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
For more information about custom error pages, see [Customizing
 Error Responses](../../../AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.md "../../../AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.md") in the *Amazon CloudFront Developer Guide*.


## Contents





**Quantity** 


The number of HTTP status codes for which you want to specify a custom error page
 and/or a caching duration. If `Quantity` is `0`, you can omit
 `Items`.


Type: Integer


Required: Yes




**Items** 


A complex type that contains a `CustomErrorResponse` element for each HTTP
 status code for which you want to specify a custom error page and/or a caching duration.
 


Type: Array of [CustomErrorResponse](API_CustomErrorResponse.md "API_CustomErrorResponse.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CustomErrorResponses "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CustomErrorResponses")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CustomErrorResponses "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CustomErrorResponses")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CustomErrorResponses "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CustomErrorResponses")
