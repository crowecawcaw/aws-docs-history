# UpdateConnectionGroup

Updates a connection group.


## Request Syntax



```
PUT /2020-05-31/connection-group/`Id` HTTP/1.1
If-Match: `IfMatch`
<?xml version="1.0" encoding="UTF-8"?>
<UpdateConnectionGroupRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <AnycastIpListId>`string`</AnycastIpListId>
   <Enabled>`boolean`</Enabled>
   <Ipv6Enabled>`boolean`</Ipv6Enabled>
</UpdateConnectionGroupRequest>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_UpdateConnectionGroup_RequestSyntax "#API_UpdateConnectionGroup_RequestSyntax")**


The ID of the connection group.


Required: Yes




**[If-Match](#API_UpdateConnectionGroup_RequestSyntax "#API_UpdateConnectionGroup_RequestSyntax")**


The value of the `ETag` header that you received when retrieving the connection group that you're updating.


Required: Yes




## Request Body


The request accepts the following data in XML format.





**[UpdateConnectionGroupRequest](#API_UpdateConnectionGroup_RequestSyntax "#API_UpdateConnectionGroup_RequestSyntax")**


Root level tag for the UpdateConnectionGroupRequest parameters.


Required: Yes




**[AnycastIpListId](#API_UpdateConnectionGroup_RequestSyntax "#API_UpdateConnectionGroup_RequestSyntax")**


The ID of the Anycast static IP list.


Type: String


Required: No




**[Enabled](#API_UpdateConnectionGroup_RequestSyntax "#API_UpdateConnectionGroup_RequestSyntax")**


Whether the connection group is enabled.


Type: Boolean


Required: No




**[Ipv6Enabled](#API_UpdateConnectionGroup_RequestSyntax "#API_UpdateConnectionGroup_RequestSyntax")**


Enable IPv6 for the connection group. For more information, see [Enable IPv6](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesEnableIPv6 "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesEnableIPv6") in the 
 *Amazon CloudFront Developer Guide*.


Type: Boolean


Required: No




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





**[ConnectionGroup](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


Root level tag for the ConnectionGroup parameters.


Required: Yes




**[AnycastIpListId](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The ID of the Anycast static IP list.


Type: String




**[Arn](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The Amazon Resource Name (ARN) of the connection group.


Type: String




**[CreatedTime](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The date and time when the connection group was created.


Type: Timestamp




**[Enabled](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


Whether the connection group is enabled.


Type: Boolean




**[Id](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The ID of the connection group.


Type: String




**[Ipv6Enabled](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


IPv6 is enabled for the connection group.


Type: Boolean




**[IsDefault](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


Whether the connection group is the default connection group for the distribution tenants.


Type: Boolean




**[LastModifiedTime](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The date and time when the connection group was updated.


Type: Timestamp




**[Name](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The name of the connection group.


Type: String




**[RoutingEndpoint](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.


Type: String




**[Status](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


The status of the connection group.


Type: String




**[Tags](#API_UpdateConnectionGroup_ResponseSyntax "#API_UpdateConnectionGroup_ResponseSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityAlreadyExists** 


The entity already exists. You must provide a unique
 entity.


HTTP Status Code: 409




**EntityLimitExceeded** 


The entity limit has been exceeded.


HTTP Status Code: 400




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




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




**ResourceInUse** 


Cannot delete this resource because it is in use.


HTTP Status Code: 409




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateConnectionGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateConnectionGroup")
