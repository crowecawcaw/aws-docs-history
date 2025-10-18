# CreateAnycastIpList

Creates an Anycast static IP list.


## Request Syntax



```
POST /2020-05-31/anycast-ip-list HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateAnycastIpListRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <IpCount>`integer`</IpCount>
   <Name>`string`</Name>
   <Tags>
      <Items>
         <Tag>
            <Key>`string`</Key>
            <Value>`string`</Value>
         </Tag>
      </Items>
   </Tags>
</CreateAnycastIpListRequest>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[CreateAnycastIpListRequest](#API_CreateAnycastIpList_RequestSyntax "#API_CreateAnycastIpList_RequestSyntax")**


Root level tag for the CreateAnycastIpListRequest parameters.


Required: Yes




**[IpCount](#API_CreateAnycastIpList_RequestSyntax "#API_CreateAnycastIpList_RequestSyntax")**


The number of static IP addresses that are allocated to the Anycast static IP list. Valid values: 21 or 3.


Type: Integer


Required: Yes




**[Name](#API_CreateAnycastIpList_RequestSyntax "#API_CreateAnycastIpList_RequestSyntax")**


Name of the Anycast static IP list.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9-_]{1,64}`



Required: Yes




**[Tags](#API_CreateAnycastIpList_RequestSyntax "#API_CreateAnycastIpList_RequestSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object


Required: No




## Response Syntax



```
HTTP/1.1 202
<?xml version="1.0" encoding="UTF-8"?>
<AnycastIpList>
   <AnycastIps>
      <AnycastIp>***string***</AnycastIp>
   </AnycastIps>
   <Arn>***string***</Arn>
   <Id>***string***</Id>
   <IpCount>***integer***</IpCount>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
   <Name>***string***</Name>
   <Status>***string***</Status>
</AnycastIpList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 202 response.


The following data is returned in XML format by the service.





**[AnycastIpList](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


Root level tag for the AnycastIpList parameters.


Required: Yes




**[AnycastIps](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


The static IP addresses that are allocated to the Anycast static IP list.


Type: Array of strings




**[Arn](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


The Amazon Resource Name (ARN) of the Anycast static IP list.


Type: String




**[Id](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


The ID of the Anycast static IP list.


Type: String




**[IpCount](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


The number of IP addresses in the Anycast static IP list.


Type: Integer




**[LastModifiedTime](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


The last time the Anycast static IP list was modified.


Type: Timestamp




**[Name](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


The name of the Anycast static IP list.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9-_]{1,64}`





**[Status](#API_CreateAnycastIpList_ResponseSyntax "#API_CreateAnycastIpList_ResponseSyntax")**


The status of the Anycast static IP list. Valid values: `Deployed`, `Deploying`, or `Failed`.


Type: String




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




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidTagging** 


The tagging specified is not valid.


HTTP Status Code: 400




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateAnycastIpList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateAnycastIpList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateAnycastIpList")
