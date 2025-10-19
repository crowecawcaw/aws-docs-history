# ListKeyGroups

Gets a list of key groups.

You can optionally specify the maximum number of items to receive in the response. If
 the total number of items in the list exceeds the maximum that you specify, or the
 default maximum, the response is paginated. To get the next page of items, send a
 subsequent request that specifies the `NextMarker` value from the current
 response as the `Marker` value in the subsequent request.


## Request Syntax



```
GET /2020-05-31/key-group?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListKeyGroups_RequestSyntax "#API_ListKeyGroups_RequestSyntax")**


Use this field when paginating results to indicate where to begin in your list of key
 groups. The response includes key groups in the list that occur after the marker. To get
 the next page of the list, set this field's value to the value of
 `NextMarker` from the current page's response.




**[MaxItems](#API_ListKeyGroups_RequestSyntax "#API_ListKeyGroups_RequestSyntax")**


The maximum number of key groups that you want in the response.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<KeyGroupList>
   <Items>
      <KeyGroupSummary>
         <KeyGroup>
            <Id>***string***</Id>
            <KeyGroupConfig>
               <Comment>***string***</Comment>
               <Items>
                  <PublicKey>***string***</PublicKey>
               </Items>
               <Name>***string***</Name>
            </KeyGroupConfig>
            <LastModifiedTime>***timestamp***</LastModifiedTime>
         </KeyGroup>
      </KeyGroupSummary>
   </Items>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</KeyGroupList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[KeyGroupList](#API_ListKeyGroups_ResponseSyntax "#API_ListKeyGroups_ResponseSyntax")**


Root level tag for the KeyGroupList parameters.


Required: Yes




**[Items](#API_ListKeyGroups_ResponseSyntax "#API_ListKeyGroups_ResponseSyntax")**


A list of key groups.


Type: Array of [KeyGroupSummary](API_KeyGroupSummary.md "API_KeyGroupSummary.md") objects




**[MaxItems](#API_ListKeyGroups_ResponseSyntax "#API_ListKeyGroups_ResponseSyntax")**


The maximum number of key groups requested.


Type: Integer




**[NextMarker](#API_ListKeyGroups_ResponseSyntax "#API_ListKeyGroups_ResponseSyntax")**


If there are more items in the list than are in this response, this element is
 present. It contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing key groups.


Type: String




**[Quantity](#API_ListKeyGroups_ResponseSyntax "#API_ListKeyGroups_ResponseSyntax")**


The number of key groups returned in the response.


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListKeyGroups")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListKeyGroups "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListKeyGroups")
