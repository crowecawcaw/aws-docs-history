# GetAnycastIpList

Gets an Anycast static IP list.


## Request Syntax



```
GET /2020-05-31/anycast-ip-list/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetAnycastIpList_RequestSyntax "#API_GetAnycastIpList_RequestSyntax")**


The ID of the Anycast static IP list.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
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


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[AnycastIpList](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


Root level tag for the AnycastIpList parameters.


Required: Yes




**[AnycastIps](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


The static IP addresses that are allocated to the Anycast static IP list.


Type: Array of strings




**[Arn](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


The Amazon Resource Name (ARN) of the Anycast static IP list.


Type: String




**[Id](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


The ID of the Anycast static IP list.


Type: String




**[IpCount](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


The number of IP addresses in the Anycast static IP list.


Type: Integer




**[LastModifiedTime](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


The last time the Anycast static IP list was modified.


Type: Timestamp




**[Name](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


The name of the Anycast static IP list.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9-_]{1,64}`





**[Status](#API_GetAnycastIpList_ResponseSyntax "#API_GetAnycastIpList_ResponseSyntax")**


The status of the Anycast static IP list. Valid values: `Deployed`, `Deploying`, or `Failed`.


Type: String




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetAnycastIpList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetAnycastIpList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetAnycastIpList")
