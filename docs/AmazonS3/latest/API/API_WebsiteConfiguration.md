# WebsiteConfiguration

Specifies website configuration parameters for an Amazon S3 bucket.


## Contents





**ErrorDocument** 


The name of the error document for the website.


Type: [ErrorDocument](API_ErrorDocument.md "API_ErrorDocument.md") data type


Required: No




**IndexDocument** 


The name of the index document for the website.


Type: [IndexDocument](API_IndexDocument.md "API_IndexDocument.md") data type


Required: No




**RedirectAllRequestsTo** 


The redirect behavior for every request to this bucket's website endpoint.


###### Important

If you specify this property, you can't specify any other property.


Type: [RedirectAllRequestsTo](API_RedirectAllRequestsTo.md "API_RedirectAllRequestsTo.md") data type


Required: No




**RoutingRules** 


Rules that define when a redirect is applied and the redirect behavior.


Type: Array of [RoutingRule](API_RoutingRule.md "API_RoutingRule.md") data types


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/WebsiteConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/WebsiteConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/WebsiteConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/WebsiteConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/WebsiteConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/WebsiteConfiguration")
