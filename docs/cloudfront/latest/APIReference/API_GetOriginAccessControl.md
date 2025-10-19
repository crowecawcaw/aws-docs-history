# GetOriginAccessControl

Gets a CloudFront origin access control, including its unique identifier.


## Request Syntax



```
GET /2020-05-31/origin-access-control/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetOriginAccessControl_RequestSyntax "#API_GetOriginAccessControl_RequestSyntax")**


The unique identifier of the origin access control.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<OriginAccessControl>
   <Id>***string***</Id>
   <OriginAccessControlConfig>
      <Description>***string***</Description>
      <Name>***string***</Name>
      <OriginAccessControlOriginType>***string***</OriginAccessControlOriginType>
      <SigningBehavior>***string***</SigningBehavior>
      <SigningProtocol>***string***</SigningProtocol>
   </OriginAccessControlConfig>
</OriginAccessControl>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[OriginAccessControl](#API_GetOriginAccessControl_ResponseSyntax "#API_GetOriginAccessControl_ResponseSyntax")**


Root level tag for the OriginAccessControl parameters.


Required: Yes




**[Id](#API_GetOriginAccessControl_ResponseSyntax "#API_GetOriginAccessControl_ResponseSyntax")**


The unique identifier of the origin access control.


Type: String




**[OriginAccessControlConfig](#API_GetOriginAccessControl_ResponseSyntax "#API_GetOriginAccessControl_ResponseSyntax")**


The origin access control.


Type: [OriginAccessControlConfig](API_OriginAccessControlConfig.md "API_OriginAccessControlConfig.md") object




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetOriginAccessControl")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetOriginAccessControl "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetOriginAccessControl")
