# LambdaFunctionAssociation

A complex type that contains a Lambda@Edge function association.


## Contents





**EventType** 


Specifies the event type that triggers a Lambda@Edge function invocation. You can
 specify the following values:



* `viewer-request`: The function executes when CloudFront receives a
 request from a viewer and before it checks to see whether the requested object
 is in the edge cache.
* `origin-request`: The function executes only when CloudFront sends a
 request to your origin. When the requested object is in the edge cache, the
 function doesn't execute.
* `origin-response`: The function executes after CloudFront receives a
 response from the origin and before it caches the object in the response. When
 the requested object is in the edge cache, the function doesn't execute.
* `viewer-response`: The function executes before CloudFront returns the
 requested object to the viewer. The function executes regardless of whether the
 object was already in the edge cache.


If the origin returns an HTTP status code other than HTTP 200 (OK), the
 function doesn't execute.

Type: String


Valid Values: `viewer-request | viewer-response | origin-request | origin-response`



Required: Yes




**LambdaFunctionARN** 


The ARN of the Lambda@Edge function. You must specify the ARN of a function version;
 you can't specify an alias or $LATEST.


Type: String


Required: Yes




**IncludeBody** 


A flag that allows a Lambda@Edge function to have read access to the body content. For
 more information, see [Accessing the Request Body by Choosing the Include Body Option](../../../AmazonCloudFront/latest/DeveloperGuide/lambda-include-body-access.md "../../../AmazonCloudFront/latest/DeveloperGuide/lambda-include-body-access.md") in the
 Amazon CloudFront Developer Guide.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/LambdaFunctionAssociation "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/LambdaFunctionAssociation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/LambdaFunctionAssociation "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/LambdaFunctionAssociation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/LambdaFunctionAssociation "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/LambdaFunctionAssociation")
