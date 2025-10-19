# GetConnectionGroupByRoutingEndpoint

Gets information about a connection group by using the endpoint that you specify.


## Request Syntax



```
GET /2020-05-31/connection-group?RoutingEndpoint=`RoutingEndpoint` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[RoutingEndpoint](#API_GetConnectionGroupByRoutingEndpoint_RequestSyntax "#API_GetConnectionGroupByRoutingEndpoint_RequestSyntax")**


The routing endpoint for the target connection group, such as d111111abcdef8.cloudfront.net.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ConnectionGroup>
   <AnycastIpListId>***string***</AnycastIpListId>
   <Arn>***string***</Arn>
   <CreatedTime>***timestamp***</CreatedTime>
   <Enabled>***boolean***</Enabled>
   <Id>***string***</Id>
   <Ipv6Enabled>***boolean***</Ipv6Enabled>
   <IsDefault>***boolean***</IsDefault>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
   <Name>***string***</Name>
   <RoutingEndpoint>***string***</RoutingEndpoint>
   <Status>***string***</Status>
   <Tags>
      <Items>
         <Tag>
            <Key>***string***</Key>
            <Value>***string***</Value>
         </Tag>
      </Items>
   </Tags>
</ConnectionGroup>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ConnectionGroup](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


Root level tag for the ConnectionGroup parameters.


Required: Yes




**[AnycastIpListId](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The ID of the Anycast static IP list.


Type: String




**[Arn](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The Amazon Resource Name (ARN) of the connection group.


Type: String




**[CreatedTime](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The date and time when the connection group was created.


Type: Timestamp




**[Enabled](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


Whether the connection group is enabled.


Type: Boolean




**[Id](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The ID of the connection group.


Type: String




**[Ipv6Enabled](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


IPv6 is enabled for the connection group.


Type: Boolean




**[IsDefault](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


Whether the connection group is the default connection group for the distribution tenants.


Type: Boolean




**[LastModifiedTime](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The date and time when the connection group was updated.


Type: Timestamp




**[Name](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The name of the connection group.


Type: String




**[RoutingEndpoint](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.


Type: String




**[Status](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


The status of the connection group.


Type: String




**[Tags](#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax "#API_GetConnectionGroupByRoutingEndpoint_ResponseSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetConnectionGroupByRoutingEndpoint")
