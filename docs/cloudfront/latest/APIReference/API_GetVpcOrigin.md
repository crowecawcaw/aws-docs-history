# GetVpcOrigin

Get the details of an Amazon CloudFront VPC origin.


## Request Syntax



```
GET /2020-05-31/vpc-origin/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetVpcOrigin_RequestSyntax "#API_GetVpcOrigin_RequestSyntax")**


The VPC origin ID.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<VpcOrigin>
   <Arn>***string***</Arn>
   <CreatedTime>***timestamp***</CreatedTime>
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
   <Status>***string***</Status>
   <VpcOriginEndpointConfig>
      <Arn>***string***</Arn>
      <HTTPPort>***integer***</HTTPPort>
      <HTTPSPort>***integer***</HTTPSPort>
      <Name>***string***</Name>
      <OriginProtocolPolicy>***string***</OriginProtocolPolicy>
      <OriginSslProtocols>
         <Items>
            <SslProtocol>***string***</SslProtocol>
         </Items>
         <Quantity>***integer***</Quantity>
      </OriginSslProtocols>
   </VpcOriginEndpointConfig>
</VpcOrigin>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[VpcOrigin](#API_GetVpcOrigin_ResponseSyntax "#API_GetVpcOrigin_ResponseSyntax")**


Root level tag for the VpcOrigin parameters.


Required: Yes




**[Arn](#API_GetVpcOrigin_ResponseSyntax "#API_GetVpcOrigin_ResponseSyntax")**


The VPC origin ARN.


Type: String




**[CreatedTime](#API_GetVpcOrigin_ResponseSyntax "#API_GetVpcOrigin_ResponseSyntax")**


The VPC origin created time.


Type: Timestamp




**[Id](#API_GetVpcOrigin_ResponseSyntax "#API_GetVpcOrigin_ResponseSyntax")**


The VPC origin ID.


Type: String




**[LastModifiedTime](#API_GetVpcOrigin_ResponseSyntax "#API_GetVpcOrigin_ResponseSyntax")**


The VPC origin last modified time.


Type: Timestamp




**[Status](#API_GetVpcOrigin_ResponseSyntax "#API_GetVpcOrigin_ResponseSyntax")**


The VPC origin status.


Type: String




**[VpcOriginEndpointConfig](#API_GetVpcOrigin_ResponseSyntax "#API_GetVpcOrigin_ResponseSyntax")**


The VPC origin endpoint configuration.


Type: [VpcOriginEndpointConfig](API_VpcOriginEndpointConfig.md "API_VpcOriginEndpointConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetVpcOrigin")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetVpcOrigin "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetVpcOrigin")
