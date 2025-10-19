# CreateCloudFrontOriginAccessIdentity

Creates a new origin access identity. If you're using Amazon S3 for your origin, you can
 use an origin access identity to require users to access your content using a CloudFront URL
 instead of the Amazon S3 URL. For more information about how to use origin access identities,
 see [Serving Private
 Content through CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md") in the *Amazon CloudFront Developer Guide*.


## Request Syntax



```
POST /2020-05-31/origin-access-identity/cloudfront HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CloudFrontOriginAccessIdentityConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CallerReference>`string`</CallerReference>
   <Comment>`string`</Comment>
</CloudFrontOriginAccessIdentityConfig>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[CloudFrontOriginAccessIdentityConfig](#API_CreateCloudFrontOriginAccessIdentity_RequestSyntax "#API_CreateCloudFrontOriginAccessIdentity_RequestSyntax")**


Root level tag for the CloudFrontOriginAccessIdentityConfig parameters.


Required: Yes




**[CallerReference](#API_CreateCloudFrontOriginAccessIdentity_RequestSyntax "#API_CreateCloudFrontOriginAccessIdentity_RequestSyntax")**


A unique value (for example, a date-time stamp) that ensures that the request can't be
 replayed.


If the value of `CallerReference` is new (regardless of the content of the
 `CloudFrontOriginAccessIdentityConfig` object), a new origin access
 identity is created.


If the `CallerReference` is a value already sent in a previous identity
 request, and the content of the `CloudFrontOriginAccessIdentityConfig` is
 identical to the original request (ignoring white space), the response includes the same
 information returned to the original request.


If the `CallerReference` is a value you already sent in a previous request
 to create an identity, but the content of the
 `CloudFrontOriginAccessIdentityConfig` is different from the original
 request, CloudFront returns a `CloudFrontOriginAccessIdentityAlreadyExists` error.
 


Type: String


Required: Yes




**[Comment](#API_CreateCloudFrontOriginAccessIdentity_RequestSyntax "#API_CreateCloudFrontOriginAccessIdentity_RequestSyntax")**


A comment to describe the origin access identity. The comment cannot be longer than
 128 characters.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<CloudFrontOriginAccessIdentity>
   <CloudFrontOriginAccessIdentityConfig>
      <CallerReference>***string***</CallerReference>
      <Comment>***string***</Comment>
   </CloudFrontOriginAccessIdentityConfig>
   <Id>***string***</Id>
   <S3CanonicalUserId>***string***</S3CanonicalUserId>
</CloudFrontOriginAccessIdentity>
```

## Response Elements


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[CloudFrontOriginAccessIdentity](#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax "#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax")**


Root level tag for the CloudFrontOriginAccessIdentity parameters.


Required: Yes




**[CloudFrontOriginAccessIdentityConfig](#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax "#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax")**


The current configuration information for the identity.


Type: [CloudFrontOriginAccessIdentityConfig](API_CloudFrontOriginAccessIdentityConfig.md "API_CloudFrontOriginAccessIdentityConfig.md") object




**[Id](#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax "#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax")**


The ID for the origin access identity, for example, `E74FTE3AJFJ256A`.
 


Type: String




**[S3CanonicalUserId](#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax "#API_CreateCloudFrontOriginAccessIdentity_ResponseSyntax")**


The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
 access identity read permission to an object in Amazon S3.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudFrontOriginAccessIdentityAlreadyExists** 


If the `CallerReference` is a value you already sent in a previous request
 to create an identity but the content of the
 `CloudFrontOriginAccessIdentityConfig` is different from the original
 request, CloudFront returns a `CloudFrontOriginAccessIdentityAlreadyExists` error.
 


HTTP Status Code: 409




**InconsistentQuantities** 


The value of `Quantity` and the size of `Items` don't
 match.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**MissingBody** 


This operation requires a body. Ensure that the body is present and the
 `Content-Type` header is set.


HTTP Status Code: 400




**TooManyCloudFrontOriginAccessIdentities** 


Processing your request would cause you to exceed the maximum number of origin access
 identities allowed.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateCloudFrontOriginAccessIdentity")
