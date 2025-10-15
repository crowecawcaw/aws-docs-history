# RoutingRule

Specifies the redirect behavior and when a redirect is applied. For more information about routing
 rules, see [Configuring
 advanced conditional redirects](https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html#advanced-conditional-redirects "https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html#advanced-conditional-redirects") in the *Amazon S3 User Guide*.


## Contents





**Redirect** 


Container for redirect information. You can redirect requests to another host, to another page, or
 with another protocol. In the event of an error, you can specify a different error code to
 return.


Type: [Redirect](API_Redirect.md "API_Redirect.md") data type


Required: Yes




**Condition** 


A container for describing a condition that must be met for the specified redirect to apply. For
 example, 1. If request is for pages in the `/docs` folder, redirect to the
 `/documents` folder. 2. If request results in HTTP error 4xx, redirect request to another
 host where you might process the error.


Type: [Condition](API_Condition.md "API_Condition.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RoutingRule "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RoutingRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RoutingRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RoutingRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RoutingRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RoutingRule")
