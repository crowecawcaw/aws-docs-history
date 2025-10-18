# CreateConnectionGroup

Creates a connection group.


## Request Syntax



```
POST /2020-05-31/connection-group HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateConnectionGroupRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <AnycastIpListId>`string`</AnycastIpListId>
   <Enabled>`boolean`</Enabled>
   <Ipv6Enabled>`boolean`</Ipv6Enabled>
   <Name>`string`</Name>
   <Tags>
      <Items>
         <Tag>
            <Key>`string`</Key>
            <Value>`string`</Value>
         </Tag>
      </Items>
   </Tags>
</CreateConnectionGroupRequest>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[CreateConnectionGroupRequest](#API_CreateConnectionGroup_RequestSyntax "#API_CreateConnectionGroup_RequestSyntax")**


Root level tag for the CreateConnectionGroupRequest parameters.


Required: Yes




**[AnycastIpListId](#API_CreateConnectionGroup_RequestSyntax "#API_CreateConnectionGroup_RequestSyntax")**


The ID of the Anycast static IP list.


Type: String


Required: No




**[Enabled](#API_CreateConnectionGroup_RequestSyntax "#API_CreateConnectionGroup_RequestSyntax")**


Enable the connection group.


Type: Boolean


Required: No




**[Ipv6Enabled](#API_CreateConnectionGroup_RequestSyntax "#API_CreateConnectionGroup_RequestSyntax")**


Enable IPv6 for the connection group. The default is `true`. For more information, see [Enable IPv6](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesEnableIPv6 "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesEnableIPv6") in the 
 *Amazon CloudFront Developer Guide*.


Type: Boolean


Required: No




**[Name](#API_CreateConnectionGroup_RequestSyntax "#API_CreateConnectionGroup_RequestSyntax")**


The name of the connection group. Enter a friendly identifier that is unique within your AWS account. This name can't be updated after you create the connection group.


Type: String


Required: Yes




**[Tags](#API_CreateConnectionGroup_RequestSyntax "#API_CreateConnectionGroup_RequestSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object


Required: No




## Response Syntax



```
HTTP/1.1 201
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


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[ConnectionGroup](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


Root level tag for the ConnectionGroup parameters.


Required: Yes




**[AnycastIpListId](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The ID of the Anycast static IP list.


Type: String




**[Arn](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The Amazon Resource Name (ARN) of the connection group.


Type: String




**[CreatedTime](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The date and time when the connection group was created.


Type: Timestamp




**[Enabled](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


Whether the connection group is enabled.


Type: Boolean




**[Id](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The ID of the connection group.


Type: String




**[Ipv6Enabled](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


IPv6 is enabled for the connection group.


Type: Boolean




**[IsDefault](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


Whether the connection group is the default connection group for the distribution tenants.


Type: Boolean




**[LastModifiedTime](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The date and time when the connection group was updated.


Type: Timestamp




**[Name](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The name of the connection group.


Type: String




**[RoutingEndpoint](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.


Type: String




**[Status](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


The status of the connection group.


Type: String




**[Tags](#API_CreateConnectionGroup_ResponseSyntax "#API_CreateConnectionGroup_ResponseSyntax")**


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




**InvalidTagging** 


The tagging specified is not valid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateConnectionGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateConnectionGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateConnectionGroup")
