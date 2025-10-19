# DeleteVpcOrigin

Delete an Amazon CloudFront VPC origin.


## Request Syntax



```
DELETE /2020-05-31/vpc-origin/`Id` HTTP/1.1
If-Match: `IfMatch`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_DeleteVpcOrigin_RequestSyntax "#API_DeleteVpcOrigin_RequestSyntax")**


The VPC origin ID.


Required: Yes




**[If-Match](#API_DeleteVpcOrigin_RequestSyntax "#API_DeleteVpcOrigin_RequestSyntax")**


The version identifier of the VPC origin to delete. This is the `ETag` value returned in the response to [GetVpcOrigin](API_GetVpcOrigin.md "API_GetVpcOrigin.md").


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 202
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


If the action is successful, the service sends back an HTTP 202 response.


The following data is returned in XML format by the service.





**[VpcOrigin](#API_DeleteVpcOrigin_ResponseSyntax "#API_DeleteVpcOrigin_ResponseSyntax")**


Root level tag for the VpcOrigin parameters.


Required: Yes




**[Arn](#API_DeleteVpcOrigin_ResponseSyntax "#API_DeleteVpcOrigin_ResponseSyntax")**


The VPC origin ARN.


Type: String




**[CreatedTime](#API_DeleteVpcOrigin_ResponseSyntax "#API_DeleteVpcOrigin_ResponseSyntax")**


The VPC origin created time.


Type: Timestamp




**[Id](#API_DeleteVpcOrigin_ResponseSyntax "#API_DeleteVpcOrigin_ResponseSyntax")**


The VPC origin ID.


Type: String




**[LastModifiedTime](#API_DeleteVpcOrigin_ResponseSyntax "#API_DeleteVpcOrigin_ResponseSyntax")**


The VPC origin last modified time.


Type: Timestamp




**[Status](#API_DeleteVpcOrigin_ResponseSyntax "#API_DeleteVpcOrigin_ResponseSyntax")**


The VPC origin status.


Type: String




**[VpcOriginEndpointConfig](#API_DeleteVpcOrigin_ResponseSyntax "#API_DeleteVpcOrigin_ResponseSyntax")**


The VPC origin endpoint configuration.


Type: [VpcOriginEndpointConfig](API_VpcOriginEndpointConfig.md "API_VpcOriginEndpointConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**CannotDeleteEntityWhileInUse** 


The entity cannot be deleted while it is in use.


HTTP Status Code: 409




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**IllegalDelete** 


Deletion is not allowed for this entity.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**PreconditionFailed** 


The precondition in one or more of the request fields evaluated to
 `false`.


HTTP Status Code: 412




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteVpcOrigin")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteVpcOrigin "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteVpcOrigin")
