# GetCloudFrontOriginAccessIdentity

Get the information about an origin access identity.


## Request Syntax



```
GET /2020-05-31/origin-access-identity/cloudfront/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetCloudFrontOriginAccessIdentity_RequestSyntax "#API_GetCloudFrontOriginAccessIdentity_RequestSyntax")**


The identity's ID.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
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


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CloudFrontOriginAccessIdentity](#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax "#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax")**


Root level tag for the CloudFrontOriginAccessIdentity parameters.


Required: Yes




**[CloudFrontOriginAccessIdentityConfig](#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax "#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax")**


The current configuration information for the identity.


Type: [CloudFrontOriginAccessIdentityConfig](API_CloudFrontOriginAccessIdentityConfig.md "API_CloudFrontOriginAccessIdentityConfig.md") object




**[Id](#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax "#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax")**


The ID for the origin access identity, for example, `E74FTE3AJFJ256A`.
 


Type: String




**[S3CanonicalUserId](#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax "#API_GetCloudFrontOriginAccessIdentity_ResponseSyntax")**


The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
 access identity read permission to an object in Amazon S3.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchCloudFrontOriginAccessIdentity** 


The specified origin access identity does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentity")
