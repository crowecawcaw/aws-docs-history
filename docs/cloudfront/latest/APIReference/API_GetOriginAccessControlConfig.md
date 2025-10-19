# GetOriginAccessControlConfig

Gets a CloudFront origin access control configuration.


## Request Syntax



```
GET /2020-05-31/origin-access-control/`Id`/config HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetOriginAccessControlConfig_RequestSyntax "#API_GetOriginAccessControlConfig_RequestSyntax")**


The unique identifier of the origin access control.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<OriginAccessControlConfig>
   <Description>***string***</Description>
   <Name>***string***</Name>
   <OriginAccessControlOriginType>***string***</OriginAccessControlOriginType>
   <SigningBehavior>***string***</SigningBehavior>
   <SigningProtocol>***string***</SigningProtocol>
</OriginAccessControlConfig>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[OriginAccessControlConfig](#API_GetOriginAccessControlConfig_ResponseSyntax "#API_GetOriginAccessControlConfig_ResponseSyntax")**


Root level tag for the OriginAccessControlConfig parameters.


Required: Yes




**[Description](#API_GetOriginAccessControlConfig_ResponseSyntax "#API_GetOriginAccessControlConfig_ResponseSyntax")**


A description of the origin access control.


Type: String




**[Name](#API_GetOriginAccessControlConfig_ResponseSyntax "#API_GetOriginAccessControlConfig_ResponseSyntax")**


A name to identify the origin access control. You can specify up to 64 characters.


Type: String




**[OriginAccessControlOriginType](#API_GetOriginAccessControlConfig_ResponseSyntax "#API_GetOriginAccessControlConfig_ResponseSyntax")**


The type of origin that this origin access control is for.


Type: String


Valid Values: `s3 | mediastore | mediapackagev2 | lambda`





**[SigningBehavior](#API_GetOriginAccessControlConfig_ResponseSyntax "#API_GetOriginAccessControlConfig_ResponseSyntax")**


Specifies which requests CloudFront signs (adds authentication information to). Specify
 `always` for the most common use case. For more information, see [origin access control advanced settings](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md#oac-advanced-settings "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md#oac-advanced-settings") in the
 *Amazon CloudFront Developer Guide*.


This field can have one of the following values:



* `always` – CloudFront signs all origin requests, overwriting the
 `Authorization` header from the viewer request if one
 exists.
* `never` – CloudFront doesn't sign any origin requests. This value turns
 off origin access control for all origins in all distributions that use this
 origin access control.
* `no-override` – If the viewer request doesn't contain the
 `Authorization` header, then CloudFront signs the origin request. If
 the viewer request contains the `Authorization` header, then CloudFront
 doesn't sign the origin request and instead passes along the
 `Authorization` header from the viewer request. **WARNING: To pass along the `Authorization` header
 from the viewer request, you *must* add the
 `Authorization` header to a [cache policy](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md") for all cache behaviors that
 use origins associated with this origin access control.**

Type: String


Valid Values: `never | always | no-override`





**[SigningProtocol](#API_GetOriginAccessControlConfig_ResponseSyntax "#API_GetOriginAccessControlConfig_ResponseSyntax")**


The signing protocol of the origin access control, which determines how CloudFront signs
 (authenticates) requests. The only valid value is `sigv4`.


Type: String


Valid Values: `sigv4`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchOriginAccessControl** 


The origin access control does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetOriginAccessControlConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetOriginAccessControlConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetOriginAccessControlConfig")
