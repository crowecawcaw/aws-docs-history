# ListAnycastIpLists

Lists your Anycast static IP lists.


## Request Syntax



```
GET /2020-05-31/anycast-ip-list?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListAnycastIpLists_RequestSyntax "#API_ListAnycastIpLists_RequestSyntax")**


Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur
 after the marker. To get the next page of the list, set this field's value to the value
 of `NextMarker` from the current page's response.




**[MaxItems](#API_ListAnycastIpLists_RequestSyntax "#API_ListAnycastIpLists_RequestSyntax")**


The maximum number of Anycast static IP lists that you want returned in the
 response.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<AnycastIpListCollection>
   <IsTruncated>***boolean***</IsTruncated>
   <Items>
      <AnycastIpListSummary>
         <Arn>***string***</Arn>
         <Id>***string***</Id>
         <IpCount>***integer***</IpCount>
         <LastModifiedTime>***timestamp***</LastModifiedTime>
         <Name>***string***</Name>
         <Status>***string***</Status>
      </AnycastIpListSummary>
   </Items>
   <Marker>***string***</Marker>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</AnycastIpListCollection>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[AnycastIpListCollection](#API_ListAnycastIpLists_ResponseSyntax "#API_ListAnycastIpLists_ResponseSyntax")**


Root level tag for the AnycastIpListCollection parameters.


Required: Yes




**[IsTruncated](#API_ListAnycastIpLists_ResponseSyntax "#API_ListAnycastIpLists_ResponseSyntax")**


If there are more items in the list collection than are in this response, this value is
 `true`.


Type: Boolean




**[Items](#API_ListAnycastIpLists_ResponseSyntax "#API_ListAnycastIpLists_ResponseSyntax")**


Items in the Anycast static IP list collection. Each item is of the [AnycastIpListSummary](API_AnycastIpListSummary.md "API_AnycastIpListSummary.md") structure type.


Type: Array of [AnycastIpListSummary](API_AnycastIpListSummary.md "API_AnycastIpListSummary.md") objects




**[Marker](#API_ListAnycastIpLists_ResponseSyntax "#API_ListAnycastIpLists_ResponseSyntax")**


Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur
 after the marker. To get the next page of the list, set this field's value to the value
 of `NextMarker` from the current page's response.


Type: String




**[MaxItems](#API_ListAnycastIpLists_ResponseSyntax "#API_ListAnycastIpLists_ResponseSyntax")**


The maximum number of Anycast static IP list collections that you want returned in the
 response.


Type: Integer




**[NextMarker](#API_ListAnycastIpLists_ResponseSyntax "#API_ListAnycastIpLists_ResponseSyntax")**


Indicates the next page of the Anycast static IP list collection. To get the next page of the
 list, use this value in the `Marker` field of your request.


Type: String




**[Quantity](#API_ListAnycastIpLists_ResponseSyntax "#API_ListAnycastIpLists_ResponseSyntax")**


The quantity of Anycast static IP lists in the collection.


Type: Integer




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListAnycastIpLists")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListAnycastIpLists "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListAnycastIpLists")
